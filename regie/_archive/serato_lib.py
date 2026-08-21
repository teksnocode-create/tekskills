#!/usr/bin/env python3
"""
Boîte à outils pour la bibliothèque Serato de Nico (disque SWIT).

Principe directeur : les chemins de fichiers ne sont JAMAIS fabriqués.
Ils sont lus depuis "database V2" et recopiés tels quels. Serato encode
certains caractères dans la zone Unicode privée ; un chemin reconstruit
à partir d'un listing disque casse silencieusement.

Voir references/serato-format.md.
"""

import struct
import sqlite3
import re
import unicodedata

# ---------------------------------------------------------------- lecture

def _iter_chunks(blob):
    """Découpe un blob Serato en blocs (tag, contenu)."""
    i = 0
    while i < len(blob) - 8:
        tag = blob[i:i + 4].decode("ascii", "replace")
        length = struct.unpack(">I", blob[i + 4:i + 8])[0]
        yield tag, blob[i + 8:i + 8 + length]
        i += 8 + length


def read_database_v2(path):
    """Retourne la liste des chemins bruts de 'database V2', dans l'ordre.

    C'est LA source de vérité pour les chemins. Ne pas les modifier.
    """
    paths = []
    with open(path, "rb") as fh:
        blob = fh.read()
    for tag, body in _iter_chunks(blob):
        if tag == "otrk":
            for sub_tag, sub_body in _iter_chunks(body):
                if sub_tag == "pfil":
                    paths.append(sub_body.decode("utf-16-be"))
    return paths


def read_crate(path):
    """Retourne la liste des chemins contenus dans un fichier .crate."""
    paths = []
    with open(path, "rb") as fh:
        blob = fh.read()
    for tag, body in _iter_chunks(blob):
        if tag == "otrk":
            for sub_tag, sub_body in _iter_chunks(body):
                if sub_tag == "ptrk":
                    paths.append(sub_body.decode("utf-16-be"))
    return paths


def read_assets(sqlite_path):
    """Retourne les métadonnées depuis location.sqlite.

    Chaque entrée : id, portable_id (chemin), file_name, artist, name,
    album, bpm, key.
    """
    con = sqlite3.connect(sqlite_path)
    con.row_factory = sqlite3.Row
    rows = con.execute(
        "SELECT id, portable_id, file_name, artist, name, album, bpm, key "
        "FROM asset"
    ).fetchall()
    con.close()
    return [dict(r) for r in rows]


# ---------------------------------------------------------------- écriture

_HEADER_COLUMNS = [
    ("song", "349"), ("artist", "197"), ("bpm", "0"), ("key", "0"),
    ("comment", "111"), ("length", "110"), ("playCount", "0"),
    ("album", "0"), ("genre", "0"),
]


def _chunk(tag, payload):
    return tag.encode("ascii") + struct.pack(">I", len(payload)) + payload


def _u16(text):
    return text.encode("utf-16-be")


def build_crate(paths, reference_paths):
    """Construit le contenu binaire d'un fichier .crate.

    paths            : chemins à inclure, tels que lus dans database V2
    reference_paths  : ensemble des chemins de database V2, pour contrôle

    Lève ValueError si un chemin n'existe pas à l'identique dans la
    référence — garde-fou contre les chemins reconstruits à la main.
    """
    reference = set(reference_paths)
    unknown = [p for p in paths if p not in reference]
    if unknown:
        raise ValueError(
            f"{len(unknown)} chemin(s) absent(s) de database V2. "
            f"Ils ont probablement été reconstruits au lieu d'être copiés. "
            f"Premier cas : {unknown[0]!r}"
        )

    out = _chunk("vrsn", _u16("1.0/Serato ScratchLive Crate"))
    out += _chunk("osrt", _chunk("tvcn", _u16("key")) + _chunk("brev", b"\x00"))
    for column, width in _HEADER_COLUMNS:
        out += _chunk("ovct", _chunk("tvcn", _u16(column))
                      + _chunk("tvcw", _u16(width)))
    for path in paths:
        out += _chunk("otrk", _chunk("ptrk", _u16(path)))
    return out


def verify_crate(blob, expected_paths, reference_paths):
    """Relit un .crate produit et confirme sa validité.

    Retourne un dict de contrôle. À appeler après écriture sur le disque,
    sur le fichier relu depuis le disque.
    """
    found = []
    for tag, body in _iter_chunks(blob):
        if tag == "otrk":
            for sub_tag, sub_body in _iter_chunks(body):
                if sub_tag == "ptrk":
                    found.append(sub_body.decode("utf-16-be"))
    header_size = blob.find(b"otrk")
    reference = set(reference_paths)
    return {
        "nombre_morceaux": len(found),
        "attendu": len(expected_paths),
        "ordre_conforme": found == list(expected_paths),
        "entete_441_octets": header_size == 441,
        "chemins_tous_connus": all(p in reference for p in found),
    }


def crate_filename(event_name, parents=("TOUS", "#CLUB", "++ MARIAGE ")):
    """Nom de fichier d'une crate imbriquée.

    ATTENTION : vérifier les noms de parents en listant Subcrates/ plutôt
    que de se fier à la valeur par défaut — '++ MARIAGE ' porte un espace
    final qui est facile à perdre.
    """
    return "%%".join(list(parents) + [event_name]) + ".crate"


# ---------------------------------------------------------------- matching

_NOISE = re.compile(
    r"\b(original mix|radio edit|extended mix|feat|ft|prod by)\b", re.I)
_TRACK_PREFIX = re.compile(r"^\s*\d{1,3}\s*[-._]\s*")

VERSION_MARKERS = [
    "live", "remix", "edit", "extended", "instrumental", "acoustic",
    "cover", "karaoke", "version", "mix", "reprise", "unplugged",
]


def normalize(text):
    """Normalise un libellé pour comparaison : casse, accents, ponctuation."""
    if not text:
        return ""
    text = _TRACK_PREFIX.sub("", str(text))
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = _NOISE.sub(" ", text)
    return re.sub(r"[^a-z0-9]+", "", text)


def match_keys(artist, title):
    """Clés de comparaison pour un morceau.

    Renvoie plusieurs variantes car les tags de la collection sont
    irréguliers : artiste parfois vide, parfois inclus dans le titre.
    """
    a, t = normalize(artist), normalize(title)
    keys = {a + t, t + a, t}
    if a:
        keys.add(a + t)
    return {k for k in keys if k}


def version_difference(csv_title, library_title):
    """Détecte une mention de version présente d'un seul côté.

    Retourne la liste des marqueurs divergents. Non vide => classer en
    INCERTAIN, ne jamais trancher automatiquement.
    """
    left, right = (csv_title or "").lower(), (library_title or "").lower()
    return [m for m in VERSION_MARKERS
            if (m in right) != (m in left)]

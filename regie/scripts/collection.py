"""Index de la collection audio sur le disque SWIT et croisement avec un CSV de playlist.

Aucune lecture ni ecriture de la bibliotheque Serato. Le disque est vu comme
un simple arbre de fichiers audio.

Usage :
    import sys; sys.path.insert(0, "scripts")
    import collection as c

    index = c.index_collection()
    lignes = c.read_playlist("playlist.csv")
    res = c.match_all(lignes, index)
    # res["trouves"] / res["incertains"] / res["manquants"]
"""

import csv
import os
import re
import unicodedata

COLLECTION = "/Volumes/SWIT/++ ZIK  Collection"
MARIAGES = os.path.join(COLLECTION, "++ MARIAGE ")
EXTENSIONS = (".mp3", ".m4a", ".wav", ".aiff", ".aif", ".flac", ".ogg", ".wma")

# Mentions qui signalent une version differente de celle demandee.
MARQUEURS_VERSION = (
    "live", "remix", "edit", "extended", "instrumental", "acoustic",
    "acoustique", "cover", "karaoke", "karaoké", "mix", "version",
    "reprise", "demo", "unplugged", "medley", "mashup", "intro", "outro",
)

# Mots qui ne comptent que comme mot isole : "Matroda x Daft Punk" est un
# remix deguise, alors qu'un titre contenant la lettre x ne l'est pas.
MARQUEURS_ISOLES = ("x", "vs", "bootleg", "rework", "flip", "dj", "mashup")

# Mots trop courants pour identifier un morceau a eux seuls.
STOPWORDS = {
    "the", "a", "an", "le", "la", "les", "de", "du", "des", "et", "and",
    "feat", "ft", "featuring", "avec", "with", "un", "une", "el", "los",
}


def normalise(texte):
    """Minuscules, accents et ponctuation supprimes, prefixes de piste retires."""
    if not texte:
        return ""
    texte = unicodedata.normalize("NFD", str(texte))
    texte = "".join(ch for ch in texte if unicodedata.category(ch) != "Mn")
    texte = texte.lower()
    # prefixes de piste : "02 - ", "01. ", "114 ", "01-01. "
    texte = re.sub(r"^\s*\d{1,3}(\s*[-_.]\s*\d{1,3})?\s*[-_.)]*\s+", " ", texte)
    texte = re.sub(r"[^a-z0-9]+", " ", texte)
    return re.sub(r"\s+", " ", texte).strip()


def tokens(texte):
    return [m for m in normalise(texte).split() if m and m not in STOPWORDS]


def index_collection(racine=COLLECTION):
    """Parcourt la collection et renvoie une liste de fiches fichier.

    Le dossier des mariages est exclu : il contient des copies deja faites
    pour d'autres evenements, pas la collection de reference.
    """
    fiches = []
    for dossier, sous_dossiers, fichiers in os.walk(racine):
        if os.path.abspath(dossier).startswith(os.path.abspath(MARIAGES)):
            sous_dossiers[:] = []
            continue
        for nom in fichiers:
            if not nom.lower().endswith(EXTENSIONS):
                continue
            base = os.path.splitext(nom)[0]
            fiches.append({
                "chemin": os.path.join(dossier, nom),
                "nom": nom,
                "norme": normalise(base),
                "tokens": set(tokens(base)),
            })
    return fiches


def read_playlist(chemin_csv):
    """Lit un CSV d'export de playlist. Colonnes artiste/titre detectees au mieux."""
    with open(chemin_csv, newline="", encoding="utf-8-sig") as fh:
        lignes = list(csv.DictReader(fh))
    if not lignes:
        return []

    entetes = list(lignes[0].keys())

    def trouver(*motifs):
        for motif in motifs:
            for entete in entetes:
                if entete and motif in entete.lower():
                    return entete
        return None

    col_artiste = trouver("artist", "artiste", "interpret")
    col_titre = trouver("track name", "titre", "title", "track", "song", "morceau")

    sortie = []
    for ligne in lignes:
        artiste = (ligne.get(col_artiste) or "").strip() if col_artiste else ""
        titre = (ligne.get(col_titre) or "").strip() if col_titre else ""
        if artiste or titre:
            sortie.append({"artiste": artiste, "titre": titre})
    return sortie


def _version_divergente(demande, fiche):
    """Vrai si le fichier porte une mention de version absente de la demande."""
    demande_norme = normalise(demande)
    for marqueur in MARQUEURS_VERSION:
        marqueur_norme = normalise(marqueur)
        if marqueur_norme and marqueur_norme in fiche["norme"] and marqueur_norme not in demande_norme:
            return marqueur

    jetons_demande = set(normalise(demande).split())
    jetons_fiche = set(fiche["norme"].split())
    for marqueur in MARQUEURS_ISOLES:
        if marqueur in jetons_fiche and marqueur not in jetons_demande:
            return marqueur
    return None


def match_one(entree, index):
    """Classe une entree de playlist en trouve / incertain / manquant."""
    artiste, titre = entree["artiste"], entree["titre"]
    demande = f"{artiste} {titre}".strip()
    jetons_titre = set(tokens(titre))
    jetons_artiste = set(tokens(artiste))

    if not jetons_titre:
        return {"statut": "manquant", "entree": entree, "candidats": []}

    exacts, partiels = [], []
    for fiche in index:
        titre_ok = jetons_titre.issubset(fiche["tokens"])
        if not titre_ok:
            # tolere un titre long dont il manque un mot secondaire
            communs = jetons_titre & fiche["tokens"]
            if len(jetons_titre) >= 4 and len(communs) >= len(jetons_titre) - 1:
                titre_ok = "partiel"
            else:
                continue
        artiste_ok = (not jetons_artiste) or bool(jetons_artiste & fiche["tokens"])
        if titre_ok is True and artiste_ok:
            exacts.append(fiche)
        else:
            partiels.append(fiche)

    for fiche in exacts:
        marqueur = _version_divergente(demande, fiche)
        if marqueur:
            partiels.append(dict(fiche, raison=f"version « {marqueur} » non demandee"))

    surs = [f for f in exacts if not _version_divergente(demande, f)]

    if len(surs) == 1:
        return {"statut": "trouve", "entree": entree, "fichier": surs[0], "candidats": []}
    if len(surs) > 1:
        return {"statut": "incertain", "entree": entree,
                "raison": f"{len(surs)} fichiers correspondent", "candidats": surs[:5]}
    if partiels:
        return {"statut": "incertain", "entree": entree,
                "raison": partiels[0].get("raison", "correspondance partielle"),
                "candidats": partiels[:5]}
    return {"statut": "manquant", "entree": entree, "candidats": []}


def match_all(entrees, index):
    resultats = {"trouves": [], "incertains": [], "manquants": []}
    cle = {"trouve": "trouves", "incertain": "incertains", "manquant": "manquants"}
    for entree in entrees:
        res = match_one(entree, index)
        resultats[cle[res["statut"]]].append(res)
    return resultats


def dossier_evenement(nom_evenement):
    return os.path.join(MARIAGES, nom_evenement)


def copier(trouves, nom_evenement, dry_run=False):
    """Copie les fichiers trouves dans <evenement>/Serato/. Ne remplace jamais."""
    import shutil

    cible = os.path.join(dossier_evenement(nom_evenement), "Serato")
    if not dry_run:
        os.makedirs(cible, exist_ok=True)

    copies, deja_la = [], []
    for res in trouves:
        source = res["fichier"]["chemin"]
        destination = os.path.join(cible, os.path.basename(source))
        if os.path.exists(destination):
            deja_la.append(destination)
            continue
        if not dry_run:
            shutil.copy2(source, destination)
        copies.append(destination)
    return {"cible": cible, "copies": copies, "deja_la": deja_la}

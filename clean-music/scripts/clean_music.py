import os, re, shutil, sys
from pathlib import Path
from mutagen import File as MutagenFile

AUDIO_EXTS = {".mp3", ".flac", ".m4a", ".wav", ".aac"}
FORBIDDEN = r'[/\\:*?"<>|]'

def run(root_path):
    ROOT = Path(root_path)
    stats = {"extracted":0,"dirs_removed":0,"ds_removed":0,"prefixes_removed":0,
             "renamed_meta":0,"no_meta":0,"collisions":0,"skipped_same":0}
    no_meta_files, collision_files = [], []

    print("=== ÉTAPE 1 : EXTRACTION ===")
    for subdir in list(ROOT.iterdir()):
        if subdir.is_dir():
            for audio in list(subdir.rglob("*")):
                if audio.is_file() and audio.suffix.lower() in AUDIO_EXTS:
                    dest = ROOT / audio.name
                    if dest.exists():
                        dest = ROOT / f"{audio.stem}_dup{audio.suffix}"
                        print(f"  DOUBLON → {dest.name}")
                    shutil.move(str(audio), str(dest))
                    stats["extracted"] += 1
                    print(f"  ✓ {audio.name}")
    print(f"\nExtraits : {stats['extracted']}")

    print("\n=== ÉTAPE 2 : NETTOYAGE ===")
    for ds in ROOT.rglob(".DS_Store"):
        try:
            ds.unlink(); stats["ds_removed"] += 1
        except Exception as e:
            print(f"  Erreur DS_Store: {e}")
    for subdir in sorted(ROOT.iterdir(), key=lambda p: len(str(p)), reverse=True):
        if subdir.is_dir():
            try:
                subdir.rmdir(); stats["dirs_removed"] += 1
                print(f"  Supprimé : {subdir.name}")
            except OSError:
                print(f"  Non vide : {subdir.name}")
    print(f"\n.DS_Store : {stats['ds_removed']} | Dossiers : {stats['dirs_removed']}")

    print("\n=== ÉTAPE 3 : PRÉFIXES NUMÉRIQUES ===")
    PREFIX_RE = re.compile(r'^(?:\d{1,3}[-.]?\d{0,3}[-. ]+)+')
    for f in sorted(ROOT.iterdir()):
        if not (f.is_file() and f.suffix.lower() in AUDIO_EXTS): continue
        m = PREFIX_RE.match(f.stem)
        if m:
            new_stem = f.stem[m.end():].strip()
            if new_stem and new_stem != f.stem:
                new_path = ROOT / (new_stem + f.suffix)
                if new_path.exists() and new_path != f:
                    print(f"  COLLISION préfixe : {f.name}")
                else:
                    f.rename(new_path); stats["prefixes_removed"] += 1
                    print(f"  ✓ '{f.stem}' → '{new_stem}'")
    print(f"\nPréfixes retirés : {stats['prefixes_removed']}")

    print("\n=== ÉTAPE 4 : MÉTADONNÉES ID3 ===")
    def get_tags(path):
        try:
            a = MutagenFile(path, easy=True)
            if a is None: return None, None
            artist = (a.get("artist") or a.get("albumartist") or [None])[0]
            title  = (a.get("title") or [None])[0]
            return artist, title
        except: return None, None

    def sanitize(s): return re.sub(FORBIDDEN, "_", s).strip()

    for f in sorted(ROOT.iterdir()):
        if not (f.is_file() and f.suffix.lower() in AUDIO_EXTS): continue
        artist, title = get_tags(f)
        if not artist or not title:
            stats["no_meta"] += 1; no_meta_files.append(f.name); continue
        new_name = f"{sanitize(artist)} - {sanitize(title)}{f.suffix.lower()}"
        new_path = ROOT / new_name
        if new_path == f: stats["skipped_same"] += 1; continue
        if new_path.exists():
            stats["collisions"] += 1
            collision_files.append(f"{f.name} → {new_name}")
            print(f"  COLLISION : {f.name}"); continue
        f.rename(new_path); stats["renamed_meta"] += 1
        print(f"  ✓ '{f.name}'\n      → '{new_name}'")

    print("\n" + "="*60)
    print("RAPPORT FINAL")
    print("="*60)
    print(f"  Extraits                  : {stats['extracted']}")
    print(f"  Dossiers supprimés        : {stats['dirs_removed']}")
    print(f"  .DS_Store supprimés       : {stats['ds_removed']}")
    print(f"  Préfixes retirés          : {stats['prefixes_removed']}")
    print(f"  Renommés via ID3          : {stats['renamed_meta']}")
    print(f"  Sans métadonnées          : {stats['no_meta']}")
    print(f"  Collisions                : {stats['collisions']}")
    print(f"  Déjà au bon nom           : {stats['skipped_same']}")
    if no_meta_files:
        print("\n⚠️  SANS MÉTADONNÉES (à tagger manuellement) :")
        for fn in no_meta_files: print(f"    - {fn}")
    if collision_files:
        print("\n⚠️  COLLISIONS (doublons à purger manuellement) :")
        for fn in collision_files: print(f"    - {fn}")

if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else ".")

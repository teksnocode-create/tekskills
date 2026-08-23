#!/bin/bash
# clean.sh — normalise un dossier de téléchargements Soulseek
# Usage: bash clean.sh "<dossier>" [--dry-run]
set -uo pipefail

DIR="${1:?usage: clean.sh <dossier> [--dry-run]}"
DRY=""
[ "${2:-}" = "--dry-run" ] && DRY=1

[ -d "$DIR" ] || { echo "Dossier introuvable: $DIR"; exit 1; }
command -v ffprobe >/dev/null || { echo "ffprobe manquant (brew install ffmpeg)"; exit 1; }

run() { if [ -n "$DRY" ]; then echo "[dry] $*"; else "$@"; fi; }

sanitize() { echo "$1" | tr '/:' '--' | tr -s ' ' ' ' | sed 's/^ *//; s/ *$//'; }

# 1. remonter les fichiers audio hors des sous-dossiers
find "$DIR" -mindepth 2 -type f \( -iname '*.mp3' -o -iname '*.flac' -o -iname '*.wav' -o -iname '*.m4a' -o -iname '*.aiff' \) -print0 |
while IFS= read -r -d '' f; do
  base="$(basename "$f")"
  dest="$DIR/$base"
  n=1
  while [ -e "$dest" ] && [ "$dest" != "$f" ]; do
    dest="$DIR/${base%.*} ($n).${base##*.}"; n=$((n+1))
  done
  [ "$dest" = "$f" ] || run mv "$f" "$dest"
done

# 2. .DS_Store + dossiers vides
find "$DIR" -name '.DS_Store' -print0 | while IFS= read -r -d '' f; do run rm -f "$f"; done
if [ -z "$DRY" ]; then
  find "$DIR" -mindepth 1 -type d -empty -delete
else
  find "$DIR" -mindepth 1 -type d -empty -exec echo "[dry] rmdir {}" \;
fi

# 3. préfixe numérique + renommage via tags ID3
find "$DIR" -maxdepth 1 -type f \( -iname '*.mp3' -o -iname '*.flac' -o -iname '*.wav' -o -iname '*.m4a' -o -iname '*.aiff' \) -print0 |
while IFS= read -r -d '' f; do
  base="$(basename "$f")"; ext="${base##*.}"; name="${base%.*}"

  artist="$(ffprobe -v quiet -show_entries format_tags=artist -of default=nw=1:nk=1 "$f" 2>/dev/null | head -1)"
  title="$(ffprobe -v quiet -show_entries format_tags=title  -of default=nw=1:nk=1 "$f" 2>/dev/null | head -1)"

  # multi-artistes taggés "A;B" ou "A/B" -> on garde le premier
  artist="$(echo "$artist" | sed -E 's/[;\/].*$//')"

  # tags poubelle: VA, Various Artists, Unknown, Piste 4, Track 07, Audio Track...
  case "$(echo "$artist" | tr '[:upper:]' '[:lower:]')" in
    ""|va|various*|unknown*|artist|inconnu*) artist="" ;;
  esac
  case "$(echo "$title" | tr '[:upper:]' '[:lower:]')" in
    ""|piste*|track*|audio*|unknown*|untitled*) title="" ;;
  esac

  # nom de fichier deja au format "Artiste - Titre": on n'y touche pas (les tags sont moins fiables)
  already_ok=""
  case "$name" in *" - "*) already_ok=1 ;; esac

  if [ -z "$already_ok" ] && [ -n "$artist" ] && [ -n "$title" ]; then
    new="$(sanitize "$artist") - $(sanitize "$title").$ext"
  else
    # on retire juste le prefixe numerique "01 - ", "03. ", "12_"
    new="$(echo "$name" | sed -E 's/^[0-9]{1,3}([[:space:]]*[-._)][[:space:]]*|[[:space:]]+)//').$ext"
  fi

  [ "$new" = "$base" ] && continue
  dest="$DIR/$new"
  n=1
  while [ -e "$dest" ]; do dest="$DIR/${new%.*} ($n).$ext"; n=$((n+1)); done
  run mv "$f" "$dest"
done

echo "Nettoyage terminé: $DIR"

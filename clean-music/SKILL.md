---
name: clean-music
description: >
  Nettoie et normalise un dossier de fichiers audio en 4 étapes automatiques :
  extraction des fichiers des sous-dossiers vers la racine, suppression des
  sous-dossiers vides et .DS_Store, suppression des préfixes numériques de piste,
  puis renommage "Artiste - Titre.ext" via les métadonnées ID3.
  TOUJOURS déclencher dès que l'utilisateur tape "/clean-music", "clean music",
  "nettoie le dossier musique", ou demande à ranger/classer ses fichiers audio.
---

# clean-music

Nettoie automatiquement un dossier audio en 4 étapes :
1. Extraction de tous les fichiers audio des sous-dossiers vers la racine
2. Suppression des sous-dossiers vides et `.DS_Store`
3. Suppression des préfixes numériques de piste (ex: `01 - `, `1.14.`, `056 - `)
4. Renommage `Artiste - Titre.ext` via les tags ID3

## Dossier cible

Le dossier passé par l'utilisateur, ou par défaut `~/Soulseek Downloads/complete`
(dossier de sortie de zik-dl).

## Exécution

### Étape 0 — Installer mutagen si absent
```bash
pip3 install mutagen --break-system-packages -q 2>/dev/null || pip3 install mutagen -q
```

### Étape 1 — Lancer le script
```bash
python3 ~/.claude/skills/clean-music/scripts/clean_music.py "<chemin_du_dossier>"
```

## Gestion des erreurs

- **mutagen absent** → installe avec pip3 et relance
- **PermissionError** → vérifier les droits du dossier, ne pas forcer avec sudo sans demander
- **Dossiers non vides après extraction** → signalé dans le rapport, le script ne force pas la suppression

## Rapport

Affiche le rapport tel que produit par le script, puis signale clairement les
fichiers sans métadonnées et les collisions à traiter manuellement.

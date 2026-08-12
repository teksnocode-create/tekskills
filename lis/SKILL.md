---
name: lis
description: Force la lecture intégrale d'un document long avant toute action, puis bloque sur un résumé en langage clair validé par l'utilisateur avant d'écrire du code. Déclencher UNIQUEMENT quand Nico tape "/lis" ou "lis tout" explicitement, jamais automatiquement sur simple upload de fichier volumineux.
---

# Lis

Skill à déclenchement explicite. Objectif : éliminer le risque de lecture partielle ou de résumé de surface sur un document long (cahier des charges, brief client, spec technique, contrat) avant de s'engager sur du code ou une architecture.

Ne s'active QUE si Nico tape `/lis` ou `lis tout` dans son message. Sur simple upload de fichier sans ce mot-clé, comportement normal (pas de skill).

## Pourquoi ce skill existe

Un `view()` standard tronque au-delà de ~16k caractères (garde le début et la fin, coupe le milieu). Sur un document de 30-50 pages, ça veut dire qu'une section entière du milieu peut être invisible sans que ça se voie. Ce skill impose une lecture séquentielle complète, bloc par bloc, pour éliminer ce trou.

## Protocole

### 1. Identifier le document et sa taille

- Localiser le fichier (`/mnt/user-data/uploads/...`)
- Si docx/pdf : utiliser le skill `docx`/`pdf`/`pdf-reading` pour en extraire le texte brut d'abord
- Mesurer la taille (nombre de caractères ou de pages) via `wc` ou équivalent

### 2. Lecture séquentielle par blocs

- Découper en blocs d'environ 8-10k caractères (avec `view_range` sur le fichier texte extrait, ou lecture bash par tranches)
- Lire CHAQUE bloc dans l'ordre, sans sauter
- Après chaque bloc, noter en interne (pas besoin de l'afficher à Nico) : les points factuels, contraintes, chiffres, deadlines, exigences techniques rencontrés
- Ne jamais s'arrêter avant d'avoir couvert 100% du fichier

### 3. Restitution obligatoire — deux blocs, langage business

Une fois la lecture complète terminée, produire dans le chat (pas de jargon technique, formulations business) :

**Ce que j'ai compris du document**
- Reformulation factuelle du contenu : qui, quoi, contraintes, chiffres, deadlines
- Pas de paraphrase du plan du document, une synthèse dans mes mots

**Ce que je propose de faire**
- Plan d'action concret en réponse au document, en langage simple
- Si le document contient des zones ambiguës ou contradictoires, les signaler explicitement ici plutôt que de trancher seul

### 4. Stop total

Après la restitution, fin du tour. Ne pas écrire une ligne de code, ne pas créer de fichier, ne pas toucher à une architecture tant que Nico n'a pas donné un go explicite. Pas de "je commence en attendant ta validation" — arrêt complet.

Si Nico répond avec des corrections plutôt qu'un go, intégrer les corrections et redemander validation avant de coder.

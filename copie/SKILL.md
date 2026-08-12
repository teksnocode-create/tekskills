---
name: copie
description: Met automatiquement dans le presse-papier macOS tout livrable prêt à coller produit pour Nicolas (mail, message LinkedIn, post, bout de code, prompt, requête SQL, texte de commit) pour qu'il fasse Cmd+V sans sélectionner à la souris dans le terminal. S'applique sans qu'il le demande dès qu'un bloc à copier-coller est produit. Se déclenche aussi explicitement sur "copie", "/copie", "copie ça", "remets-le dans le presse-papier".
---

# Copie

Dans le terminal, Nicolas n'a pas de bouton "copier" sur les blocs de code. Quand on lui produit un mail ou un bout de code, il doit le sélectionner à la souris, ce qui rate les retours à la ligne et les longs blocs. Ce skill met le livrable directement dans son presse-papier.

## Quand ça se déclenche

**Automatiquement**, sans que Nicolas le demande, dès qu'on produit un texte destiné à être collé ailleurs :
- un mail, un message LinkedIn, un SMS, un message WhatsApp
- un post, une accroche, un texte de candidature
- un bout de code (JS, SQL, JSON, YAML, config, commande shell)
- un prompt destiné à un autre outil (ChatGPT, agent n8n, prompt système)
- un message de commit

**Sur demande** quand Nicolas dit "copie", "/copie", "copie ça", "remets-le dans le presse-papier" : copier le dernier livrable produit, ou celui qu'il désigne ("copie l'objet", "copie le SQL").

## Ce qu'on ne copie pas

- Les réponses d'analyse, les verdicts, les recaps, les rapports d'`/open` ou de `/close` : c'est de la lecture, pas du collage
- Les extraits de fichiers du repo affichés pour discussion
- Les listes de todos, les tableaux de synthèse
- Quand le "livrable" fait moins d'une ligne (un nom de variable, une URL seule) : inutile, ça se retape

En cas de doute, ne pas copier. Un presse-papier écrasé pour rien fait perdre ce que Nicolas y avait mis.

## Ce qu'on copie exactement

**Le corps du livrable seul, rien d'autre.** Pas l'objet du mail, pas le destinataire, pas les commentaires d'accompagnement, pas les backticks de bloc de code, pas de ligne de titre ajoutée.

Quand une réponse contient plusieurs blocs (par exemple un objet de mail + le corps du mail), **on copie le corps**, jamais les métadonnées. Si Nicolas veut l'autre partie, il le dit ("copie l'objet") et on recopie.

## Comment faire

Ne jamais passer le contenu en argument de commande shell (`echo "..." | pbcopy`) : une apostrophe dans un mail français ou un guillemet dans du JavaScript casse la commande ou tronque le texte en silence.

Toujours en deux temps :

1. Écrire le contenu exact dans un fichier du scratchpad de session avec l'outil Write (ex. `copie-presse-papier.txt`)
2. `pbcopy < /chemin/vers/copie-presse-papier.txt`

Le fichier est écrasé à chaque fois, un seul suffit.

## Confirmation

Une ligne, en fin de réponse, pas plus :

`Copié : [quoi], [N] caractères. Cmd+V.`

Exemple : `Copié : corps du mail Octys, 1240 caractères. Cmd+V.`

Ne pas afficher le chemin du fichier temporaire, ne pas expliquer la manœuvre.

## Hors macOS (mobile, Claude Code web, machine Linux)

`pbcopy` n'existe que sur macOS. Nicolas travaille aussi depuis son iPhone et depuis Claude Code sur le repo GitHub, où la commande échouera.

Vérifier la disponibilité avant d'agir (`command -v pbcopy`). Si absente : ne rien copier, ne pas afficher d'erreur, ne pas ajouter de ligne de confirmation. Comportement normal, le bloc reste affiché dans la réponse. Nicolas ne doit pas voir la différence autrement que par l'absence de la ligne "Copié".

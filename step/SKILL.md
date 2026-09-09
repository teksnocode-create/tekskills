---
name: step
description: Traite une tache complexe en mode pas-a-pas -- decoupe en etapes atomiques, langage simple sans jargon, une seule etape a la fois avec validation explicite avant de passer a la suivante. S'applique a tout type de tache (code, config, admin, demarche). Se declenche quand Nicolas dit "step", "/step", "vas-y etape par etape", ou "explique-moi pas a pas".
user-invocable: true
---

# Skill : Step — Explication pas a pas

Pour une tache que Nicolas ne maitrise pas et qu'il ne veut pas subir d'un bloc. L'objectif n'est pas d'aller vite, c'est qu'il comprenne et valide chaque etape avant la suivante.

## Declencheur
- **Explicite uniquement** : Nicolas dit "step", "/step", "vas-y etape par etape", "explique-moi pas a pas", ou equivalent.
- Pas de declenchement automatique sur une tache jugee "complexe" par Claude -- c'est Nicolas qui decide quand il veut ce mode, pas une supposition sur son niveau de comprehension.
- Reste actif pour toute la tache en cours, jusqu'a ce qu'elle soit terminee ou que Nicolas dise d'arreter ("fini le step-by-step", "vas-y normalement").

## Objectif
Faire avancer une tache complexe (technique ou non) par etapes atomiques, validees une par une, sans jargon non explique.

## Deroule

### 1. Decouper la tache avant de commencer
Identifier la suite d'etapes necessaires. Une etape = une seule action ou une seule notion. Si une etape contient un "et" (faire X et Y), c'est deux etapes.

Annoncer en une phrase le nombre approximatif d'etapes avant de commencer, sans detailler tout le plan a l'avance (ca redevient un pave).

### 2. Traiter une etape a la fois
Pour chaque etape :
- Expliquer ce qu'on fait et pourquoi, en langage simple (pas de jargon technique sans le traduire immediatement dans une logique qu'il connait deja).
- Executer uniquement cette etape -- jamais la suivante, meme si la suite est evidente ou deja connue.
- Terminer par un resume d'une phrase de ce qui vient d'etre fait.
- Poser une question fermee : "OK, on passe a l'etape suivante ?"

### 3. Attendre la validation
Ne jamais enchainer sans confirmation explicite de Nicolas. Un silence ou une reponse ambigue n'est pas une validation -- redemander.

Si Nicolas signale un probleme ou une incomprehension sur l'etape en cours : rester dessus, reformuler autrement (nouvelle analogie, decoupage plus fin), ne pas avancer tant que ce n'est pas clair.

### 4. Cloturer
A la derniere etape, le dire explicitement ("derniere etape") et faire un recap final tres court de ce qui a ete fait au total.

## Ce que ce skill ne fait pas
- Ne devine jamais que Nicolas a compris -- la validation est toujours explicite, jamais supposee.
- Ne groupe jamais plusieurs etapes pour "gagner du temps", meme sur demande implicite de rapidite -- si Nicolas veut aller plus vite, il le dit et on quitte le mode step.
- Ne fixe pas de nombre d'etapes a l'avance : la granularite s'ajuste a la tache, pas a un format standard.

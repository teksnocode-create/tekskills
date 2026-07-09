---
name: simple
description: Reexplique une explication technique sans jargon, adaptee au niveau reel de Nicolas (autodidacte no-code/IA, logique n8n/Make/Airtable/Supabase, pas de vocabulaire CS/dev formel). Se declenche quand Nicolas dit "simple", ou spontanement apres une reponse chargee en jargon technique non explique.
user-invocable: true
---

# Skill : Simple — Explication sans jargon

## Declencheur
- **Explicite** : Nicolas dit "simple" (ou "/simple") apres une explication technique.
- **Spontane** : juste apres avoir produit une reponse avec plusieurs termes techniques non expliques (vocabulaire CS/archi/dev formel), proposer en une ligne, a la fin de la reponse : "Je peux te la refaire sans jargon si tu veux, tape 'simple'." Ne pas le faire a chaque reponse technique — seulement quand la densite de jargon non explique est reelle (plusieurs termes dans la meme reponse, pas juste un mot isole).

## Objectif
Retraduire une explication technique dans le langage de Nicolas : pas pour un debutant complet, pas pour un enfant de 5 ans, mais pour quelqu'un qui pense en logique n8n/Make/Airtable/Supabase/API plutot qu'en vocabulaire dev/CS formel.

## Deroule

### 1. Identifier ce qu'il faut retraduire
Reprendre la derniere explication technique substantielle de la conversation (le dernier message assistant avec du jargon), sauf si Nicolas precise un autre passage.

### 2. Reecrire sans jargon
Pour chaque terme technique non explique dans ce passage :
- Verifier d'abord s'il est deja dans `glossaire.md` (meme dossier) : si oui, il est considere acquis, ne pas le re-simplifier, l'utiliser tel quel.
- S'il existe un equivalent naturel dans sa stack (n8n, Make, Airtable, Supabase, API/webhook, prompt/agent IA) -> traduire par analogie avec ca, pas par une definition abstraite.
- Sinon -> une ligne de definition simple, integree naturellement dans la phrase, pas un glossaire a part dans la reponse.
- Garder le fond intact : meme conclusion, meme niveau de detail utile. Ce n'est pas un resume plus court, c'est la meme info en langage clair.
- Ton direct, professionnel, pas condescendant, pas de posture "explique comme a un enfant".

### 3. Tenir le glossaire
Apres toute retraduction, mettre a jour `glossaire.md` (meme dossier que ce skill) :
- Ajouter les nouveaux termes traites, format `- **terme** : explication courte utilisee`.
- Ce fichier sert de memoire du niveau reel de Nicolas : plus il grandit, moins il faut simplifier, plus les termes peuvent etre utilises directement dans les reponses normales (pas seulement dans ce skill).

## Ce que ce skill ne fait pas
- Ne remplace pas l'explication technique initiale (utile si Nicolas doit en reparler avec un profil technique/dev).
- Ne simplifie pas le fond, les chiffres ou les decisions — seulement le vocabulaire.

---
name: simple
description: Refait la derniere reponse courte ET sans jargon : coupe les pavés trop longs et retraduit le vocabulaire technique au niveau reel de Nicolas (autodidacte no-code/IA, logique n8n/Make/Airtable/Supabase, pas de vocabulaire CS/dev formel). Se declenche quand Nicolas dit "simple", ou spontanement apres une reponse trop longue ou chargee en jargon non explique.
user-invocable: true
---

# Skill : Simple — Court et sans jargon

Deux choses font decrocher Nicolas : les termes techniques non expliques, et les pavés. Ce skill traite les deux d'un coup, sur un seul mot.

## Declencheur
- **Explicite** : Nicolas dit "simple" (ou "/simple") apres une reponse.
- **Spontane** : juste apres avoir produit une reponse trop dense, proposer en une ligne, a la fin : "Je peux te la refaire courte et sans jargon, tape 'simple'." Ne pas le faire a chaque reponse technique — seulement quand c'est reel : plusieurs termes non expliques dans le meme message, ou une reponse qui depasse un ecran.

## Objectif
Renvoyer la meme information, mais lisible d'un coup d'oeil : dans le langage de Nicolas (il pense en logique n8n/Make/Airtable/Supabase/API, pas en vocabulaire dev/CS formel) et dans un format qu'il lit en entier.

## Deroule

### 1. Identifier ce qu'il faut refaire
Reprendre la derniere reponse substantielle de la conversation, sauf si Nicolas designe un autre passage.

### 2. Couper le pavé
- **5 lignes maximum**, sauf si le fond est reellement irreductible.
- **Commencer par la conclusion** : ce qu'il faut retenir ou faire, en premiere phrase. Le raisonnement vient apres, ou pas du tout.
- **Une seule idee par paragraphe.** Si la reponse d'origine empilait plusieurs sujets, n'en garder qu'un et lister les autres en une ligne : "Il y avait aussi X et Y, dis-moi si tu veux que je les reprenne."
- **3 puces maximum.** Au-dela, c'est que le contenu doit etre decoupe, pas liste.
- Supprimer : les rappels de contexte que Nicolas connait deja, les precautions, les alternatives non retenues, les repetitions.

### 3. Enlever le jargon
Pour chaque terme technique non explique :
- Verifier d'abord s'il est deja dans `glossaire.md` (meme dossier) : si oui, il est considere acquis, ne pas le re-simplifier, l'utiliser tel quel.
- S'il existe un equivalent naturel dans sa stack (n8n, Make, Airtable, Supabase, API/webhook, prompt/agent IA) -> traduire par analogie avec ca, pas par une definition abstraite.
- Sinon -> une ligne de definition simple, integree naturellement dans la phrase, pas un glossaire a part dans la reponse.
- Ton direct, professionnel, pas condescendant, pas de posture "explique comme a un enfant".

### 4. Tenir le glossaire
Apres toute retraduction, mettre a jour `glossaire.md` (meme dossier que ce skill) :
- Ajouter les nouveaux termes traites, format `- **terme** : explication courte utilisee`.
- Ce fichier sert de memoire du niveau reel de Nicolas : plus il grandit, moins il faut simplifier, plus les termes peuvent etre utilises directement dans les reponses normales (pas seulement dans ce skill).

## Ce que ce skill ne fait pas
- **Ne coupe jamais dans le fond** : les chiffres, les verdicts, les risques, les decisions et les echeances restent tous. On coupe le remplissage et le vocabulaire, jamais l'information qui change une decision. Si raccourcir obligerait a supprimer un fait qui compte, garder le fait et couper ailleurs.
- Ne remplace pas l'explication technique initiale (utile si Nicolas doit en reparler avec un profil technique/dev).

## Note
Le vrai correctif est en amont : la regle anti-pavé permanente vit dans `profil-nicolas.md` (section "Format de reponse"), qui s'applique a toutes les reponses sans que Nicolas ait a taper quoi que ce soit. Ce skill est le rattrapage quand la regle n'a pas suffi.

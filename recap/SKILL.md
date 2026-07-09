---
name: recap
description: Resume la conversation en cours dans un format pret a coller dans le /close ("Qu'est-ce que tu as fait aujourd'hui ?"). Se declenche quand Nicolas dit "recap", "/recap" ou "fais un recap".
user-invocable: true
---

# Skill : Recap de conversation

## Declencheur
Quand Nicolas dit "recap", "/recap", ou "fais un recap".

## Objectif
Resumer la conversation en cours dans un format directement injectable dans le `/close` (reponse a "Qu'est-ce que tu as fait aujourd'hui ?").

## Deroule

### 1. Scanner la conversation en cours
Passer en revue tout ce qui a ete echange dans la session active.

### 2. Produire le bloc de recap

Format de sortie : le bloc complet doit etre enveloppe dans un bloc de code (```) pour etre copie colle tel quel, sans reformatage markdown au collage.

```
Recap — [AAAA-MM-JJ]

Ce qui a ete fait :
- [actions concretes, livrables, decisions prises]

Decouvertes / Apprentissages :
- [si applicable]

Blocages / Points ouverts :
- [si applicable]

Priorite suivante :
- [prochaine action identifiee]
```

### 3. Regles de redaction
- Factuel, pas de reformulation floue
- Une ligne par point, pas de paragraphes
- Si un projet est clairement identifie, le nommer (ex. "Agent LinkedIn", "Karine", "SynkParty")
- Si la conversation est trop courte ou n'a rien de concret : le dire en une phrase

## Ce que ce skill ne fait pas
- Ne cree pas de fichier
- Ne committe pas
- Ne met pas a jour les READMEs
- C'est un outil de preparation au `/close`, pas un remplacement

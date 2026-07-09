---
name: commit-message-style
description: Impose le format Conventional Commits sur les repos de code de Nicolas. Ne s'applique pas au repo Executive Assistant (commits narratifs de type journal via /close). Se declenche a chaque creation de commit git.
user-invocable: true
---

# Skill : Commit Message Style — Conventional Commits

## Exclusion — a verifier en premier
Ne jamais appliquer ce format dans le repo **Executive Assistant** (`_Projet_Sorek/Executive assistant`, ou tout repo dont le `CLAUDE.md` decrit un commit narratif via un skill `/close`). Ce repo garde son style de commit journal libre, un commit peut couvrir plusieurs chantiers.

Ce skill s'applique uniquement sur les repos de code (ex. SaaS LinkedIn, NINA, apps perso comme SynkParty/Silteplay).

## Declencheur
A chaque creation de commit git sur un repo de code (hors exclusion ci-dessus).

## Format

```
<type>(<scope>): <description>

[body optionnel]
```

## Types

- `feat` : nouvelle fonctionnalite
- `fix` : correction de bug
- `docs` : documentation uniquement
- `refactor` : changement de code qui ne corrige ni n'ajoute rien
- `test` : ajout ou mise a jour de tests
- `chore` : maintenance (dependances, CI, build)

## Regles

- Description en minuscule, pas de point final
- Scope optionnel mais encourage
- Le body explique le POURQUOI, pas le QUOI (le diff montre deja le quoi)
- Premiere ligne : 72 caracteres max
- Un commit = un type + un scope. Si un changement touche plusieurs sujets sans lien, le decouper en plusieurs commits plutot que de forcer un seul message generique

## Exemples

Bon : `feat(auth): add password reset flow`
Bon : `fix(api): handle null response from payment gateway`
Mauvais : `Fixed stuff`
Mauvais : `Update code`

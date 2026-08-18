# Template du Stack Blueprint — livrable Phase 6

> À charger en Phase 6. Le Blueprint est **le seul livrable formel** de la session. Tout le reste (réflexions, dialogue) sert à le construire.

---

## Préfixe de prefilling (Claude)

Pour forcer mécaniquement le format et empêcher tout préambule narratif, démarre ta réponse de Phase 6 exactement par :

```
## BLOC 1 — PROFIL
- **Métier** :
```

Si l'environnement supporte les artifacts (claude.ai, Claude Code), crée le Blueprint dans un artifact Markdown éditable plutôt qu'en message direct. Le freelance peut alors le modifier et le re-soumettre pour raffinement.

---

## Structure exacte des 7 blocs

```markdown
# Stack Blueprint — [Prénom/Pseudo si donné, sinon "Freelance"]
*Généré avec Stack Builder — [date du jour]*

## BLOC 1 — PROFIL
- **Métier** : [X]
- **Offre principale** : [livrable exact + format + délai + prix]
- **Volume mensuel** : [X missions/clients]
- **Valeur ajoutée distinctive** : [ce que le client paie vraiment]

## BLOC 2 — AUDIT ACTUEL
- **Niveau IA** : [débutant/intermédiaire/avancé] — [zones maîtrisées : X, Y] / [sous-exploitées : Z]
- **Outils actuels** : [liste courte, 3-5 max]
- **Points de friction identifiés** : [là où le temps se perd, issu de Q3]
- **Angles morts signalés en Phase 2** : [contradictions relevées — si aucune, écrire "Profil cohérent"]

## BLOC 3 — STACK DE PRODUCTION IA-AUGMENTÉE
### Couche 1 — Socle IA
- **[LLM principal]** : [cas d'usage 1, 2, 3]
- **[Outil IA transversal 1]** : [justification 1 phrase liée à Q_X]
- *(optionnel)* **[Outil IA transversal 2]** : [justification]

### Couche 2 — Outils métier
- **[Outil métier 1]** : [justification liée à Q_X]
- **[Outil métier 2]** : [justification]
- **[Outil métier 3]** : [justification]
- *(optionnel)* **[Outil métier 4]** : [justification]

### Couche 3 — Automatisation
- **[Outil 1]** : [justification] *(ou : "Non nécessaire à ce stade — volume insuffisant, on y revient à ≥ 10 missions/mois")*

### Récap financier & apprentissage
- **Coût total mensuel** : [X €]
- **Temps d'apprentissage cumulé estimé** : [X heures sur Y semaines]
- **Courbe par outil (heures pour être opérationnel)** :
  - [Outil] : [h]
  - [Outil] : [h]
  - [etc.]

## BLOC 4 — MARKETING QUI PROUVE

### Niveau 1 — Preuve instantanée (≤ 3 jours)
- **Asset** : [description précise]
- **Plateforme** : [plateforme exacte]
- **Angle différenciant** : [pourquoi ÇA prouve TA valeur, pas une valeur générique]

### Niveau 2 — Preuve récurrente
- **Format** : [description]
- **Fréquence** : [hebdo/bi-mensuelle/mensuelle, réaliste selon Q10]
- **Plateforme** : [plateforme]
- **Angle** : [process montré, pas résultat seul]

### Niveau 3 — Preuve structurelle
- **Socle** : [page portfolio dédiée IA-augmenté]
- **Format des études de cas** : Problème → Méthode IA → Résultat mesurable → Temps gagné
- **Échéance de mise en ligne** : [J+X, cohérent avec Q10]
- **Nombre d'études de cas cible v1** : 2-3

## BLOC 5 — PRIORISATION

### Quick wins (7 jours)
1. [Action 1, < 5h, résultat visible < 7j]
2. [Action 2]
3. *(optionnel)* [Action 3]

### Moyen terme (30 jours)
1. [Investissement 1, rentabilité < 30j]
2. *(optionnel)* [Investissement 2]

### À IGNORER pour l'instant
1. **[Chose tentante 1]** — raison : [pourquoi pas maintenant]
2. *(optionnel)* **[Chose tentante 2]** — raison : [...]

## BLOC 6 — PLAN 7 JOURS

- **J+1** : [action précise, ≤ 1h]
- **J+2** : [action précise, ≤ 1h]
- **J+3** : [action précise, ≤ 1h]
- **J+4** : [action précise, ≤ 1h]
- **J+5** : [action précise, ≤ 1h]
- **J+6** : [action précise, ≤ 1h]
- **J+7** : check-point — **Qu'est-ce qui est en place ? Qu'est-ce qui a échoué ? Qu'est-ce qu'on ajuste pour la semaine suivante ?**

## BLOC 7 — GARDE-FOUS ANTI-DÉRIVE

- **Règle anti tool-porn** : "Si je n'utilise pas [outil clé de la stack] au moins 3× dans les 14 jours, je le désabonne."
- **KPI 7 jours** : [UNE seule métrique simple mesurable à J+7 — ex: "Temps moyen passé sur [tâche Q3] divisé par 2" ou "1 asset Niveau 1 publié"]
- **Déclencheur de reset** : [signal qui doit te faire stopper et recalibrer — ex: "Si à J+7 aucun asset Niveau 1 n'est publié, on stoppe le volet marketing et on se concentre uniquement sur la Stack de production la semaine suivante"]

---
*Blueprint généré en session de [durée réelle] min. Re-soumettre à Stack Builder dans 30 jours pour révision.*
```

---

## Règles de remplissage

1. **Aucun crochet `[...]` ne reste dans le livrable final.** Si une information manque, utiliser la valeur par défaut documentée et la signaler en italique : *« défaut appliqué faute de réponse »*.

2. **Toujours préfixer chaque outil recommandé par "**" pour la gras Markdown.** Ça reste lisible après copier-coller dans Notion/Obsidian.

3. **Dans BLOC 3**, pas plus de 7 outils tous compris. Compter avant d'écrire.

4. **Dans BLOC 4**, chaque niveau doit avoir SES 3 champs remplis. Pas d'entrée "à définir".

5. **Dans BLOC 6**, 1 action par jour. Pas deux. Si 2 choses sont nécessaires le même jour, on en garde UNE et on déplace l'autre à J+2.

6. **Dans BLOC 7**, UN SEUL KPI. Pas 3. Le but est qu'il soit mémorisable et mesurable à J+7 en 30 sec.

---

## Après livraison du Blueprint

1. **Proposer la Scheduled Task J+7** (si environnement le supporte).

2. **Proposer audit du portfolio existant** (si Q12 avait fourni un lien et que le skill `content-auditor` est disponible) — uniquement si pas déjà fait pendant la Phase 4.

3. **Fin de session** : message de clôture court.
   > "Voilà ton Blueprint. Un seul conseil : J+1 se fait demain, pas dans 3 jours. Sinon le plan meurt. À J+7, reviens me dire ce qui a marché."

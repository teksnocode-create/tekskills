# Template Action Plan — livrable Phase 6

> À charger en Phase 6. L'Action Plan est **le seul livrable formel** de la session. Tout le reste (réflexions, dialogue, scoring) sert à le construire.

---

## Préfixe de prefilling (Claude)

Pour forcer mécaniquement le format et empêcher tout préambule narratif, démarre ta réponse de Phase 6 exactement par :

```
## BLOC 1 — PROFIL
- **Métier** :
```

Si l'environnement supporte les artifacts (claude.ai, Claude Code, Cowork), crée l'Action Plan dans un **artifact Markdown éditable** plutôt qu'en message direct. Le freelance peut alors le modifier et te le re-soumettre pour raffinement.

---

## Structure exacte des 8 blocs

```markdown
# Action Plan — [Prénom/Pseudo si donné, sinon "Freelance"]
*Généré avec Action Pilot — [date du jour]*

## BLOC 1 — PROFIL
- **Métier** : [profil métier + métier précis]
- **Offre principale** : [livrable + format + délai + prix + mode facturation (forfait/horaire)]
- **Volume & revenu actuel** : [X missions/mois, Y € brut/mois]
- **Statut fiscal** : [AE / EI / SASU / SARL]
- **Reach actuel** : [audience cumulée honnête, canal par canal, + liste email]
- **Assets existants** : [liste courte ou "aucun"]

## BLOC 2 — DIAGNOSTIC & SIGNAUX
- **Score TEMPS** : X/20 — top 3 signaux : [signal 1], [signal 2], [signal 3]
- **Score INVESTISSEMENT** : Y/20 — top 3 signaux : [signal 1], [signal 2], [signal 3]
- **Écart** : [X-Y] points — [levier évident / ambiguïté levée par question Phase 3 / veto appliqué]
- **Contradictions détectées en Phase 2** : [liste courte — si aucune, écrire "Profil cohérent"]
- **Défauts appliqués faute de réponse** : [liste — si aucun, écrire "Aucun"]

## BLOC 3 — LEVIER RETENU
- **Décision** : **[TEMPS]** ou **[INVESTISSEMENT]**
- **Justification en 3 lignes** :
  - Ligne 1 : [signal quantitatif dominant]
  - Ligne 2 : [signal qualitatif dominant]
  - Ligne 3 : [contrainte structurante qui cadre la décision]
- **Règle d'exclusivité** : *L'autre levier n'est PAS activé avant J+60 et validation de celui-ci.*
- *(si applicable)* **⚠ Livré contre recommandation** : [raison — utilisé UNIQUEMENT si le freelance a insisté pour cumul]

## BLOC 4 — OBJECTIF 30 JOURS
- **KPI principal (UN SEUL)** : [métrique mesurable à J+30, ex: "TJM moyen des 3 prochains devis ≥ 550 €" ou "Waitlist asset ≥ 100 inscrits" ou "3 ventes pre-order à 49 €"]
- **Objectif secondaire (optionnel)** : [1 métrique de soutien — PAS un second KPI]
- **Seuil d'échec à J+30** : [signal qui doit te faire reset, ex: "Si aucun nouveau prospect premium contacté → stop automation, retour prospection manuelle"]

## BLOC 5 — PLAN 30 JOURS

### Semaine 1 — J+1 à J+7 (1 action par jour, ≤ 1h)
- **J+1** : [action précise, livrable mesurable]
- **J+2** : [action précise]
- **J+3** : [action précise]
- **J+4** : [action précise]
- **J+5** : [action précise]
- **J+6** : [action précise]
- **J+7** : **check-point S1** — [3 questions : actions faites / obstacles / ajustement S2]

### Semaine 2 — J+8 à J+14 (3 actions, 2-4h chacune)
1. [Action 1 + durée + livrable]
2. [Action 2 + durée + livrable]
3. [Action 3 + durée + livrable]

### Semaine 3 — J+15 à J+21 (3 actions)
1. [Action 1]
2. [Action 2]
3. [Action 3]

### Semaine 4 — J+22 à J+30 (3 actions + check-point)
1. [Action 1]
2. [Action 2]
3. [Action 3]
4. **J+30 check-point** : KPI atteint ? Si oui, décision J+60 (maintenir / ouvrir pondération 80/20). Si non, diagnostic + pivot.

## BLOC 6 — VISION 90 JOURS (MACRO)
- **Milestone J+30 (M+1)** : validation du KPI principal sur le levier retenu.
- **Milestone J+60 (M+2)** : [objectif macro du levier principal / ouverture éventuelle pondération 80/20].
- **Milestone J+90 (M+3)** : revue stratégique complète. Changement de levier possible ici uniquement.

*Au-delà de J+90 : pas de projection. Pilotage par la réalité terrain.*

## BLOC 7 — GARDE-FOUS ANTI-DISPERSION
- **Règle 1 — Exclusivité** : *"Je n'active PAS l'autre levier avant J+60. Toute tentation (nouvelle idée, opportunité, suggestion externe) qui pointe vers l'autre levier est notée dans un 'parking lot' et ignorée jusqu'à J+30."*
- **Règle 2 — Cap d'actions** : *"Je n'ajoute AUCUNE action au plan entre J+1 et J+30. Si une urgence arrive, elle remplace une action existante, elle ne s'additionne pas."*
- **Règle 3 — Rituel de recentrage** : [1 rituel concret adapté au freelance — ex: "Chaque lundi matin, 15 min de review : quelles actions S1/S2/S3/S4 sont toujours les priorités ?"]

## BLOC 8 — CHECK-POINT J+30
- **Questions du check-point** :
  1. Sur les 12 actions planifiées, combien exécutées ? Lesquelles sautées et pourquoi ?
  2. KPI principal : atteint ? partiellement ? échoué ?
  3. Décision J+60 : maintien du levier + pondération 80/20 / prolongation du même levier / pivot exceptionnel ?
- **Scheduled Task** : *Tâche programmée à J+30 — « Check-point Action Plan — J+30 (levier [X]) »* — **à créer via le skill `schedule` si environnement compatible.**
- **Rappel automatique** : si Scheduled Task non disponible, le freelance doit mettre un rappel agenda à J+30.

---
*Plan généré en session de [durée réelle] min. Re-soumettre à Action Pilot à J+30 pour le check-point et la décision J+60.*
```

---

## Règles de remplissage

1. **Aucun crochet `[...]` ne reste dans le livrable final.** Si une information manque, utiliser la valeur par défaut documentée et la signaler en italique : *« défaut appliqué faute de réponse »*.

2. **Toutes les actions sont rédigées en infinitif ou à l'impératif,** avec **1 verbe d'action clair** en tête ("Lister", "Rédiger", "Envoyer", "Mettre à jour", "Publier", "Setup", "Interviewer"…). Pas de "réfléchir à", "explorer", "envisager".

3. **Chaque action a un livrable mesurable** : un fichier, un email envoyé, un chiffre noté, une ligne publiée.

4. **Dans BLOC 4**, UN SEUL KPI. Pas 3. Le but est qu'il soit mémorisable et mesurable à J+30 en 30 sec.

5. **Dans BLOC 5**, compter avant d'écrire : 7 + 3 + 3 + 3 = 16 max, viser 10-12 en pratique. Si Q5 ≤ 3h/semaine : 7 + 2 + 2 + 2 = 13 max, viser 9-10.

6. **Dans BLOC 6**, pas plus de 3 milestones. Pas de détail des actions. C'est volontairement macro.

7. **Dans BLOC 7**, les 3 règles sont exprimées à la première personne ("Je n'active pas..." / "Je n'ajoute pas...") — le freelance s'engage par formulation.

8. **Dans BLOC 8**, systématiquement proposer la Scheduled Task. Ne JAMAIS zapper cette étape — c'est le mécanisme qui fait passer le plan du PDF à la réalité.

---

## Après livraison de l'Action Plan

1. **Proposer la Scheduled Task J+30** (si environnement le supporte).

2. **Proposer les chaînages pertinents** :
   - Levier TEMPS + pas de Stack Blueprint → `stack-builder`.
   - Levier INVESTISSEMENT + profil métier CODE + envie micro-SaaS → `coach-microsaas-kreator`.
   - Levier INVESTISSEMENT + pas de Brand Book → `brand-architect`.
   - Asset à auditer → `content-auditor`.

3. **Fin de session** : message de clôture court, sans sur-ambiance.
   > "Voilà ton Action Plan. Un seul conseil : J+1 se fait demain, pas dans 3 jours. Et l'autre levier, tu l'oublies pendant 30 jours. Rendez-vous à J+30 pour le check-point."

---

## Cas spécial : livraison contre recommandation

Si le freelance a refusé la règle d'exclusivité et exigé les deux leviers (voir `anti-patterns-dispersion.md` §1) :

1. Livre UN SEUL levier dans le plan (le score le plus haut ou TEMPS par défaut).
2. En BLOC 3, insère un bloc d'avertissement :
   > **⚠ Avertissement — Livré contre recommandation**
   > Le freelance a insisté pour cumuler TEMPS et INVESTISSEMENT à J+1.
   > Règle d'exclusivité non appliquée à sa demande.
   > Probabilité d'abandon sous 21 jours : élevée.
   > Relecture recommandée à J+14 pour ajuster ou abandonner un des deux leviers.
3. N'intègre pas le second levier dans le plan détaillé. Tu ne sur-livres pas. Le plan reste mono-levier, l'avertissement est le seul espace où le double choix est signalé.

Raison : tu ne peux pas sécuriser ce que tu désapprouves. Le plan reste propre ; l'avertissement documente la divergence.

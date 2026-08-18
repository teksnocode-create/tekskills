# INDEX DES TECHNIQUES DE PROMPTING

> Techniques combinables classées par famille. Chaque technique = nom + quand + gabarit rapide.
> Pour les frameworks complets (ACTIF, CO-STAR, ReAct...), voir `frameworks-guide.md`.

---

## 1. INJECTION DE CONTEXTE

### Zero-Shot
- **Quand** : tâche simple, pas besoin d'exemples
- **Gabarit** : `[Instruction directe sans exemple]`

### Few-Shot (contrastif)
- **Quand** : format spécifique à reproduire, cohérence de style
- **Gabarit** : 2-3 bons exemples + 1 mauvais labellisé → le plus efficace pour calibrer
- **Attention** : Claude 4.x suit les exemples très littéralement — s'assurer qu'ils reflètent exactement le comportement voulu

### Role-Based
- **Quand** : influencer ton, expertise, registre
- **Gabarit** : `Tu es un [rôle] expert en [domaine]. Ta mission : [tâche].`

### Instruction Prompting
- **Quand** : tâche claire, instruction directe
- **Gabarit** : `[Verbe d'action] + [objet] + [contraintes] + [format attendu]`

### Template-Based
- **Quand** : sortie uniforme et reproductible (fiches, emails, rapports)
- **Gabarit** : structure à trous avec `{{variables}}`

### Conditional Branching
- **Quand** : comportement différent selon l'input
- **Gabarit** : `Si [condition A] → faire X. Si [condition B] → faire Y. Sinon → Z.`

### Hierarchical
- **Quand** : tâche complexe à décomposer en niveaux
- **Gabarit** : `Niveau 1 : [vue d'ensemble] → Niveau 2 : [détails] → Niveau 3 : [exécution]`

---

## 2. RAISONNEMENT EXPLICITE (famille CoT)

### Chain-of-Thought (CoT)
- **Quand** : raisonnement logique, mathématique, analytique
- **Gabarit** : `Réfléchis étape par étape avant de donner ta réponse finale.`
- **Variantes** : Zero-Shot CoT ("step by step"), Auto-CoT

### Tree-of-Thoughts (ToT)
- **Quand** : problème à branches multiples, exploration d'alternatives
- **Gabarit** : `Explore 3 approches différentes. Pour chacune, évalue avantages/inconvénients. Sélectionne la meilleure.`

### Self-Ask
- **Quand** : question complexe décomposable en sous-questions
- **Gabarit** : `Pour répondre à [Q], demande-toi d'abord : [sous-Q1] ? [sous-Q2] ? Puis synthétise.`

### Least-to-Most
- **Quand** : difficulté croissante
- **Gabarit** : `Résous d'abord le cas le plus simple, puis augmente progressivement la complexité.`

### Backward Chaining
- **Quand** : raisonner depuis le résultat vers les étapes
- **Gabarit** : `Le résultat final doit être [X]. Quelles étapes sont nécessaires pour y arriver ?`

### System 2 Attention (S2A)
- **Quand** : filtrer le bruit dans un contexte long
- **Gabarit** : `Relis le contexte. Identifie uniquement les informations pertinentes pour [tâche]. Ignore le reste.`

---

## 3. STRUCTURATION DE SORTIE

### JSON Prompting
- **Quand** : sortie parsable par un système (API, webhook, Airtable)
- **Gabarit** : `Réponds UNIQUEMENT en JSON valide suivant ce schema : {schema}. Aucun texte autour.`
- **Boost Claude** : utiliser le prefilling (commencer la réponse assistant par `{`)

### XML/Delimiter Tagging
- **Quand** : séparer sections (natif Claude)
- **Gabarit** : `<context>...</context> <task>...</task> <output_format>...</output_format>`

### Structured Output Extraction
- **Quand** : extraire données d'un texte non structuré
- **Gabarit** : `Extrais de ce texte : [champs attendus]. Format : [JSON/tableau/CSV].`

### Encapsulation de réponse
- **Quand** : post-traitement automatique de la sortie
- **Gabarit** : `Entoure ta réponse finale de balises <answer>...</answer>.`

### Prefilling (Claude-natif)
- **Quand** : forcer le format de la première ligne de sortie
- **Comment** : dans l'API, pré-remplir le `content` du rôle `assistant`
- **Exemple** : pour forcer du JSON, préfill avec `{` ; pour forcer une langue, préfill avec `Voici `

---

## 4. FIABILISATION ET ANTI-HALLUCINATION

### Generated Knowledge
- **Quand** : enrichir le contexte avant de répondre
- **Gabarit** : `Avant de répondre, génère 3-5 faits pertinents sur [sujet]. Puis utilise-les pour formuler ta réponse.`

### Reflexion
- **Quand** : auto-correction après une première réponse
- **Gabarit** : `Réponds. Puis relis ta réponse et identifie les erreurs ou lacunes. Corrige.`

### Contrastive CoT
- **Quand** : montrer le bon ET le mauvais raisonnement
- **Gabarit** : `Voici un raisonnement correct : [A]. Voici un incorrect : [B]. Explique pourquoi A est correct.`

### Verification Framework
- **Quand** : vérification systématique de claims
- **Gabarit** : `Pour chaque affirmation, indique : [source], [confiance], [vérifiable oui/non].`

### Séparation des sujets
- **Quand** : éviter la contamination entre domaines
- **Règle** : 1 sujet complexe = 1 échange. Ne pas mélanger des questions très différentes.

---

## 5. OPTIMISATION ET PERFORMANCE

### Token Economy
- **Quand** : réduire les coûts API sans perdre en qualité
- **Techniques** : compression sémantique, suppression des redondances, instructions concises

### Prompt Caching (Claude-natif)
- **Quand** : même prompt appelé de façon répétée (automation)
- **Comment** : placer les blocs statiques (rules, identity) en tête, les données variables en fin

### Batching
- **Quand** : traiter N items avec le même prompt
- **Gabarit** : `Pour chaque élément de la liste suivante, applique [instruction] : [liste]`

### Modular Architecture
- **Quand** : système complexe à maintenir
- **Technique** : décomposer en blocs réutilisables (identité, règles, workflow, format)

---

## 6. CRÉATIVITÉ ET STYLE

### Styled Prompting
- **Quand** : ton de marque, pastiche, format créatif
- **Gabarit** : `Écris dans le style de [référence]. Contraintes : [format]. Ton : [descripteur].`

### Roleplay
- **Quand** : simulation, coaching, persona incarné
- **Gabarit** : `Tu incarnes [personnage]. Tu as [traits]. Tu ne sors jamais du personnage.`

### Narrative
- **Quand** : fiction, storytelling, discours
- **Gabarit** : `Raconte [sujet] sous forme de [narration/conte/discours]. Voix : [1ère/3ème personne].`

### Multi-Persona
- **Quand** : débat, perspectives multiples
- **Gabarit** : `Imagine 3 experts : [A], [B], [C]. Chacun donne son avis sur [sujet]. Synthétise.`

---

## 7. AGENTS ET OUTILS

### Prompt Chaining
- **Quand** : tâche complexe en étapes séquentielles
- **Gabarit** : `Prompt 1 [planifier] → sortie → Prompt 2 [exécuter] → sortie → Prompt 3 [vérifier]`

### Multi-Agent Coordination (simple)
- **Quand** : 2-3 agents avec rôles distincts, tâche décomposable
- **Gabarit** : `Agent A : [rôle]. Agent B : [rôle]. Protocole : A produit → B critique → A révise.`

### Multi-Agent Orchestré (swarm séquentiel à scoring croisé)
- **Quand** : problème complexe nécessitant hypothèses + critique + vérification + synthèse + convergence
- **Niveau** : EXPERT — nécessite prompt chaining API ou orchestration externe (Make/n8n/CrewAI)
- **Gabarit** :
```
Agent 1 (Proposant) :
  Génère 2-3 hypothèses alternatives.
  Pour chaque hypothèse : description + justification + score de confiance (1-10).

Agent 2 (Critique) :
  Pour chaque hypothèse reçue : identifie faiblesses + contre-arguments + score de validité (1-10).
  Termine par des recommandations de raffinement.

Agent 3 (Vérificateur) :
  Pour chaque claim factuel : vérifie avec sources + score de fiabilité (1-10).
  Signale explicitement les claims non vérifiables.

Agent 4 (Synthétiseur) :
  Fusionne les outputs en pondérant par les scores des agents précédents.
  Produit une synthèse unifiée + score de cohérence globale (1-10).
  Identifie les points de consensus et les divergences restantes.

Agent 5 (Modérateur) :
  Si accord > 80% → produit la synthèse finale + traçabilité.
  Si divergence > 20% → relance un cycle Critique→Vérificateur→Synthétiseur.
  Émet le score final et les limites identifiées.

Orchestration : séquentiel (1→2→3→4→5), chaque agent reçoit les outputs cumulés des précédents.
```
- **Implémentation** : 1 system prompt par agent, chaînés via API (Make/n8n) ou conversation séquentielle
- **Variantes** : ajouter un Agent Explorateur (hypothèses disruptives) ou un Agent Éthique (détection de biais) selon le domaine
- **Optimisation avancée** : utiliser des modèles hétérogènes par agent (ex: Haiku pour le Proposant, Opus pour le Critique/Vérificateur) — la recherche montre que des ensembles hétérogènes correctement orchestrés atteignent de meilleurs rapports coût/performance que des systèmes homogènes

### ReWOO (Reasoning Without Observation)
- **Quand** : workflow avec outils multiples et étapes prévisibles — alternative efficiente à ReAct
- **Principe** : planifier TOUTE la séquence d'appels d'outils en 1 seul appel LLM (avec placeholders), exécuter les outils, puis synthétiser en 1 appel final. Résultat : 2 appels LLM au lieu de N+1.
- **Gabarit** :
```
PHASE 1 — PLAN (1 appel LLM)
Pour accomplir [tâche], voici le plan :
Plan 1 : [action] → #E1 = Outil["requête"]
Plan 2 : [action utilisant #E1] → #E2 = Outil["requête avec #E1"]
Plan 3 : [action utilisant #E1 et #E2] → #E3 = Outil["requête avec #E1, #E2"]

PHASE 2 — EXÉCUTE (pas d'appel LLM)
Exécuter les outils dans l'ordre, remplacer les placeholders #E par les résultats réels.

PHASE 3 — SYNTHÈSE (1 appel LLM)
Voici les résultats : [#E1=..., #E2=..., #E3=...].
Synthétise la réponse finale à partir de ces résultats.
```
- **Quand préférer ReWOO à ReAct** : étapes prévisibles, workflow automation (Make/n8n), réduction de coûts API
- **Quand préférer ReAct** : exploration dynamique, prochaine étape dépend du résultat précédent

### Reflexion (auto-critique itérative avec mémoire et évaluation)
- **Quand** : tâche où la qualité est mesurable (code, factuel, conformité) et où l'itération améliore le résultat
- **Différence avec Critic-Refine** : Reflexion ajoute un évaluateur externe (test, score, vérification factuelle) + une mémoire épisodique des leçons apprises
- **Gabarit** :
```
BOUCLE (max {{max_trials="3"}} itérations) :

1. GÉNÈRE : Produis [contenu] selon [contraintes].

2. ÉVALUE (évaluateur externe) :
   - Exécute [test/vérification/scoring] sur le résultat.
   - Score : __/10. Seuil de validation : {{seuil="7"}}.

3. RÉFLÉCHIS (si score < seuil) :
   - Qu'est-ce qui a échoué et pourquoi ?
   - Quelle leçon retenir pour la prochaine itération ?
   - Stocke dans mémoire : "[Essai N] : [erreur] → [leçon]"

4. RÉGÉNÈRE en intégrant les leçons des essais précédents.

SORTIE : version finale + score + nombre d'itérations + leçons apprises.
```
- **Cas d'usage** : génération de code (évaluateur = tests unitaires), rédaction factuelle (évaluateur = fact-check), conformité (évaluateur = checklist)

### Multi-Agent Debate — DMAD (Diverse Multi-Agent Debate)
- **Quand** : besoin de perspectives multiples sur un problème ambigu, réduction de biais de raisonnement
- **Principe** : N agents génèrent des réponses en parallèle avec des **stratégies de raisonnement différentes** (pas juste des personas), puis débattent sur plusieurs tours pour converger
- **Différence avec Multi-Agent Orchestré** : les agents sont en parallèle (pas séquentiels) et utilisent des méthodes de pensée distinctes
- **Gabarit** :
```
ROUND 1 — GÉNÉRATION PARALLÈLE :
  Agent A (raisonnement analytique) : résout [problème] par décomposition logique.
  Agent B (raisonnement analogique) : résout [problème] par analogie avec des cas connus.
  Agent C (raisonnement adversarial) : identifie les failles dans les approches évidentes.

ROUND 2-N — DÉBAT (max {{max_rounds="3"}}) :
  Chaque agent reçoit les réponses des autres.
  Chaque agent critique les autres ET révise sa propre réponse.
  Si convergence (≥2 agents d'accord) → passer à la synthèse.

SYNTHÈSE :
  Agréger par vote pondéré (poids = score de confiance de chaque agent).
  Si pas de convergence après max_rounds → livrer les positions divergentes documentées.
```
- **Attention** : la recherche montre que le MAD classique (agents homogènes) ne surpasse pas toujours le simple self-consistency. Le DMAD (agents avec stratégies diverses) est significativement plus performant.
- **Niveau** : EXPERT — nécessite orchestration parallèle (API batch ou workflow)

### Tool Use Pattern
- **Quand** : intégration avec des outils externes
- **Gabarit** : `Tu as accès à [outils]. Utilise-les quand nécessaire. Format d'appel : [format].`

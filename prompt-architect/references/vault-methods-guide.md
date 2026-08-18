# Méthodes Avancées — Import Vault Obsidian

> Référence satellite du skill prompt-architect v2.2
> Source : Vault Obsidian `02 - PROMPT ENGINEERING/1-FONDAMENTAUX/methodes-avancees/` + `07 - FORMATION/`

---

## Vue d'ensemble

Ces méthodes complètent la matrice de sélection du SKILL.md principal. Elles couvrent des cas d'usage spécialisés non couverts par les frameworks généralistes (ACTIF, CO-STAR, ReAct, etc.).

| Méthode | Acronyme | Complexité | Cas d'usage principal |
|---------|----------|------------|----------------------|
| Adaptive Response Generation | ARG | EXPERT | Personnalisation dynamique des réponses |
| Business Intelligence Prompting | BIP | COMPLEXE | Analyse de données business / KPI |
| Cognitive Architecture Prompting | CAP | EXPERT | Raisonnement structuré multi-modules |
| Code Generation Prompting | CGP | MOYEN-COMPLEXE | Génération de code production-ready |
| Modular Prompt Architecture | MPA | EXPERT | Architecture modulaire de systèmes de prompts |

---

## ARG — Adaptive Response Generation

**Quand l'utiliser** : Quand le prompt doit adapter dynamiquement son ton, niveau et approche selon le profil utilisateur (chatbot public, assistant pédagogique, onboarding adaptatif).

**4 piliers** :
1. **Analyse Contextuelle** : Décodage du profil utilisateur (expertise, humeur, style)
2. **Ajustement Dynamique** : Modulation ton/niveau/approche selon le profil détecté
3. **Génération Personnalisée** : Réponse sur-mesure pour CET utilisateur
4. **Boucle Adaptative** : Feedback loop pour affiner l'adaptation

**Gabarit minimal** :
```xml
<identity>
Tu es {{role}}. Tu adaptes ton niveau, ton ton et ta profondeur selon le profil utilisateur détecté.
</identity>

<user_profiling>
Avant de répondre, analyse le message utilisateur pour détecter :
- Niveau d'expertise : débutant / intermédiaire / expert
- État émotionnel : calme / stressé / frustré / enthousiaste
- Style préféré : formel / décontracté / technique / vulgarisé
</user_profiling>

<adaptation_rules>
- Débutant + stressé → Simplifier, rassurer, exemples concrets
- Expert + calme → Aller droit au point, jargon OK, pas de vulgarisation
- Intermédiaire + frustré → Valider l'émotion, proposer solution pas-à-pas
</adaptation_rules>

<task>
{{tache_principale}}
</task>
```

**Combinaisons fréquentes** : ARG + Roleplay Prompting, ARG + State Machine (pour tracking du profil sur plusieurs échanges)

---

## BIP — Business Intelligence Prompting

**Quand l'utiliser** : Analyse de données business (KPI, ventes, métriques) pour en extraire des insights actionnables. Idéal pour dashboards narratifs, rapports automatisés, alertes stratégiques.

**5 principes** :
1. Pilotage factuel par les données (pas de conjectures)
2. Détection proactive des tendances et anomalies
3. Insights orientés action (chaque analyse → recommandation)
4. Contextualisation métier précise (secteur, période, objectifs)
5. Connexion stratégique explicite aux objectifs business

**Gabarit minimal** :
```xml
<identity>
Tu es un analyste business senior. Tu analyses les données fournies pour produire des insights exploitables.
</identity>

<context>
Secteur : {{secteur}}
Période : {{periode}}
Objectif business : {{objectif}}
</context>

<data>
{{donnees_brutes}}
</data>

<task>
1. Identifier les 3-5 tendances clés
2. Détecter toute anomalie ou variation significative (>{{seuil}}%)
3. Pour chaque insight, fournir :
   - Le constat (chiffré)
   - L'hypothèse causale
   - La recommandation actionnable
   - Le niveau d'urgence (🔴 critique / 🟡 attention / 🟢 opportunité)
</task>

<output_format>
Tableau Markdown : Insight | Données | Cause probable | Action recommandée | Urgence
</output_format>
```

**Combinaisons fréquentes** : BIP + JSON Prompting (pour export Airtable/Make), BIP + PRÉCISE-NET (pour sourçage des insights)

---

## CAP — Cognitive Architecture Prompting

**Quand l'utiliser** : Problèmes complexes nécessitant un raisonnement structuré multi-étapes mimant la cognition humaine. Supérieur au CoT simple pour les analyses multi-perspectives.

**4 modules cognitifs** :
1. **Mémoire** : Rappel du contexte, faits connus, historique
2. **Analyse** : Focus sur éléments clés, reformulation du problème
3. **Planification** : Stratégie de résolution, séquençage
4. **Synthèse** : Réponse finale intégrant tout le processus

**Gabarit minimal** :
```xml
<identity>
Tu es un expert en {{domaine}}. Tu raisonnes en suivant une architecture cognitive structurée.
</identity>

<cognitive_process>
## MÉMOIRE
Rappelle les informations pertinentes :
- Contexte fourni : {{contexte}}
- Connaissances mobilisées : [lister]
- Contraintes connues : [lister]

## ANALYSE
Examine les éléments clés :
- Quel est le vrai problème ? (reformuler)
- Quels éléments sont critiques vs secondaires ?
- Quelles sont les tensions ou contradictions ?

## PLANIFICATION
Définis ta stratégie de résolution :
- Approche choisie et pourquoi
- Étapes séquentielles
- Risques anticipés

## SYNTHÈSE
Produis la réponse finale en intégrant mémoire + analyse + plan.
</cognitive_process>
```

**Combinaisons fréquentes** : CAP + DMAD (pour débat multi-perspectives), CAP + Reflexion (pour auto-correction)

---

## CGP — Code Generation Prompting

**Quand l'utiliser** : Génération de code production-ready à partir de spécifications en langage naturel. Couvre : fonctions, scripts, composants, API endpoints, migrations DB.

**5 piliers** :
1. **Efficacité** : Complexité algorithmique optimisée
2. **Robustesse** : Gestion des cas limites et erreurs
3. **Typage** : Annotations, signatures claires, standards
4. **Sécurité** : Prévention injection, XSS, buffer overflow
5. **Réutilisabilité** : Code modulaire, documenté, maintenable

**Gabarit minimal** :
```xml
<identity>
Tu es un développeur senior {{langage}} (v{{version}}). Tu génères du code production-ready.
</identity>

<specifications>
Besoin : {{description_fonctionnelle}}
Langage : {{langage}} {{version}}
Framework : {{framework}}
Contraintes : {{contraintes_techniques}}
</specifications>

<rules>
- Typage strict obligatoire
- Gestion d'erreurs explicite (try/catch, Result type)
- Documentation inline (docstring/JSDoc)
- Tests unitaires pour chaque fonction publique
- Aucune donnée hardcodée → variables de configuration
</rules>

<output_format>
1. Code source complet avec imports
2. Tests unitaires
3. Notes d'implémentation (choix techniques justifiés)
</output_format>
```

**Combinaisons fréquentes** : CGP + Reflexion (auto-correction via tests), CGP + MPA (architecture modulaire)

---

## MPA — Modular Prompt Architecture

**Quand l'utiliser** : Conception de systèmes de prompts complexes (assistants multi-tâches, pipelines de traitement, agents orchestrés). L'équivalent du "software architecture" pour les prompts.

**Principes** :
- Chaque module = 1 prompt = 1 tâche claire (input/output définis)
- Modules chaînables : séquentiel, parallèle, conditionnel
- Chaque module est testable et remplaçable indépendamment
- Documentation obligatoire par module

**Gabarit d'architecture** :
```yaml
# Architecture MPA — {{nom_systeme}}

modules:
  - id: MOD-01
    name: "{{nom_module_1}}"
    role: "{{description_courte}}"
    input: "{{type_input}}"
    output: "{{type_output}}"
    prompt: |
      {{prompt_du_module}}

  - id: MOD-02
    name: "{{nom_module_2}}"
    role: "{{description_courte}}"
    input: "output de MOD-01"
    output: "{{type_output}}"
    prompt: |
      {{prompt_du_module}}

orchestration:
  type: sequential  # sequential | parallel | conditional | router
  flow: MOD-01 → MOD-02 → MOD-03
  error_handling: "Si MOD-XX échoue → {{fallback}}"

routing_rules:  # si type = conditional ou router
  - condition: "{{condition}}"
    target: MOD-XX
```

**Combinaisons fréquentes** : MPA + ReAct (modules comme outils d'agent), MPA + State Machine (orchestration à état)

---

## Matrice de sélection étendue

| Situation | Méthode vault | Alternative skill existante |
|-----------|--------------|---------------------------|
| Chatbot adaptatif multi-profils | **ARG** | Roleplay Prompting (moins dynamique) |
| Dashboard narratif / analyse KPI | **BIP** | CoT + JSON Prompting (moins spécialisé) |
| Raisonnement expert multi-étapes | **CAP** | CoT / Plan-and-Solve (moins structuré) |
| Génération de code fiable | **CGP** | Instruction Prompting (moins rigoureux) |
| Architecture multi-prompts | **MPA** | Prompt Chaining / Multi-Agent (moins formalisé) |

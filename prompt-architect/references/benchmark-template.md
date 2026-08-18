# BENCHMARK — Suivi de Performance des Prompts

> Template pour enregistrer, évaluer et apprendre de chaque prompt significatif produit.
> Stockage recommandé : Obsidian (vault dédié) ou Airtable (table "Benchmark_Prompts").

---

## 1. FICHE DE BENCHMARK (à remplir par prompt)

```json
{
  "id": "BENCH-XXX",
  "date": "YYYY-MM-DD",
  "intent": "Ce que l'utilisateur voulait accomplir",
  "contexte": "Client / projet / domaine",
  "approche_choisie": {
    "nature": "CREATE|OPTIMIZE|FIX|CONVERT|TEMPLATE",
    "complexite": "SIMPLE|MOYEN|COMPLEXE|EXPERT",
    "framework": "Ex: ACTIF, CO-STAR, ReAct, etc.",
    "techniques": ["Ex: Few-Shot contrastif", "Prefilling"]
  },
  "scorecard_pre_livraison": {
    "precision": 0.0,
    "robustesse": 0.0,
    "efficience": 0.0,
    "conformite_format": 0.0,
    "testabilite": 0.0,
    "maintenabilite": 0.0,
    "proportionnalite": 0.0,
    "score_final": 0.0
  },
  "resultat_reel": {
    "statut": "OK|PARTIEL|ECHEC",
    "score_utilisateur": 0,
    "commentaire_utilisateur": "Feedback brut"
  },
  "analyse_post": {
    "ecart_pre_vs_reel": "Où le scorecard a surestimé/sous-estimé",
    "cause_racine": "Pourquoi ça a marché ou échoué",
    "lecon_apprise": "Règle à retenir",
    "action_corrective": "Modification du skill si pertinent",
    "over_engineering_detecte": false,
    "approche_plus_simple_possible": "Quelle approche plus simple aurait suffi (si applicable)"
  },
  "prompt_archive": {
    "lien_obsidian": "obsidian://open?vault=Prompts&file=BENCH-XXX",
    "prompt_complet": "Copie ou référence du prompt livré",
    "categorie": "BON|MOYEN|MAUVAIS"
  }
}
```

---

## 2. GRILLE D'ANALYSE AGRÉGÉE

Après 10+ benchmarks, analyser les patterns :

### Tableau de bord de performance

| Métrique | Formule | Cible |
|----------|---------|-------|
| Taux de succès | OK / total | ≥ 80% |
| Taux d'over-engineering | over_engineering_detecte=true / total | ≤ 10% |
| Score moyen pré-livraison | moyenne des totaux scorecard | ≥ 25/30 |
| Écart pré vs réel | moyenne des |scorecard - score_utilisateur| | ≤ 1.5 |
| Taux SIMPLE suffisant | cas où SIMPLE aurait suffi mais COMPLEXE+ choisi / total | ≤ 15% |
| Top technique efficace | technique la plus corrélée à statut=OK | — |
| Top anti-pattern récurrent | cause_racine la plus fréquente dans ECHEC | — |

### Questions d'audit périodique (tous les 20 benchmarks)

1. Quel niveau de complexité a le meilleur ratio succès/effort ?
2. Quelles techniques reviennent systématiquement dans les prompts OK ?
3. Quelles techniques sont utilisées mais n'améliorent pas le résultat ?
4. Y a-t-il un pattern de sur-complexité récurrent ?
5. Le scorecard pré-livraison prédit-il correctement le résultat réel ?
6. Faut-il ajouter/supprimer/modifier quelque chose dans le skill ?

---

## 3. CATÉGORISATION POUR OBSIDIAN RAG

### Structure de vault recommandée

```
Prompts/
├── _Index.md                    (tableau de bord agrégé)
├── _Leçons.md                   (règles extraites des benchmarks)
├── BON/
│   ├── BENCH-001.md
│   ├── BENCH-003.md
│   └── ...
├── MOYEN/
│   ├── BENCH-002.md
│   └── ...
├── MAUVAIS/
│   ├── BENCH-004.md
│   └── ...
└── Templates/
    ├── fiche-benchmark.md       (ce template)
    └── scorecard.md
```

### Template de note Obsidian (fiche individuelle)

```markdown
---
id: BENCH-XXX
date: YYYY-MM-DD
statut: BON|MOYEN|MAUVAIS
intent: "..."
complexite: SIMPLE|MOYEN|COMPLEXE|EXPERT
framework: "..."
score_pre: XX/30
score_utilisateur: X/10
over_engineered: false
tags: [prompt, benchmark, {{domaine}}, {{technique}}]
---

# BENCH-XXX — {{titre_court}}

## Intent
{{intent}}

## Approche choisie
- Complexité : {{complexite}}
- Framework : {{framework}}
- Techniques : {{techniques}}

## Scorecard pré-livraison
| Critère | Score |
|---------|-------|
| Efficience | /5 |
| Précision | /5 |
| Robustesse | /5 |
| Testabilité | /5 |
| Maintenabilité | /5 |
| Proportionnalité | /5 |
| **Total** | **/30** |

## Résultat réel
- Statut : {{statut}}
- Score utilisateur : {{score}}/10
- Commentaire : {{commentaire}}

## Analyse
- Écart pré vs réel : {{ecart}}
- Cause racine : {{cause}}
- **Leçon apprise** : {{lecon}}
- Action corrective : {{action}}
- Over-engineering : {{oui/non}} → si oui, approche plus simple : {{alternative}}

## Prompt archivé
\`\`\`
{{prompt_complet}}
\`\`\`
```

---

## 4. EXEMPLES DE FICHES (pour calibrer la notation)

### Exemple BON — BENCH-001
```json
{
  "id": "BENCH-001",
  "intent": "Prompt de génération de fiches produit pour Airtable via Make",
  "approche_choisie": {"nature": "CREATE", "complexite": "SIMPLE", "framework": "ACTIF", "techniques": ["Template-Based", "JSON Prompting", "Prefilling"]},
  "scorecard_pre_livraison": {"efficience": 5, "precision": 4, "robustesse": 4, "testabilite": 5, "maintenabilite": 5, "proportionnalite": 5, "total": 28},
  "resultat_reel": {"statut": "OK", "score_utilisateur": 9, "commentaire": "Parfait du premier coup, format JSON propre"},
  "analyse_post": {"ecart_pre_vs_reel": "Scorecard fidèle", "cause_racine": "Tâche bien cadrée + prefilling JSON", "lecon_apprise": "Pour les sorties JSON en automation, ACTIF + Prefilling suffit toujours", "over_engineering_detecte": false}
}
```

### Exemple MAUVAIS — BENCH-004
```json
{
  "id": "BENCH-004",
  "intent": "Système multi-agents pour rédiger des articles de blog",
  "approche_choisie": {"nature": "CREATE", "complexite": "EXPERT", "framework": "Multi-Agent Orchestré", "techniques": ["Scoring croisé", "5 agents", "Convergence"]},
  "scorecard_pre_livraison": {"efficience": 2, "precision": 4, "robustesse": 4, "testabilite": 2, "maintenabilite": 2, "proportionnalite": 1, "total": 15},
  "resultat_reel": {"statut": "ECHEC", "score_utilisateur": 3, "commentaire": "Trop complexe, résultat pas meilleur qu'un simple CO-STAR avec Critic-Refine"},
  "analyse_post": {"ecart_pre_vs_reel": "Le scorecard à 15/30 aurait dû bloquer la livraison", "cause_racine": "Over-engineering massif — un article de blog ne nécessite pas 5 agents", "lecon_apprise": "JAMAIS de multi-agents pour du contenu rédactionnel standard. CO-STAR + Critic-Refine suffit.", "over_engineering_detecte": true, "approche_plus_simple_possible": "CO-STAR + Critic-Refine, complexité MOYEN"}
}
```

---

## 5. RÈGLES D'ÉVOLUTION DU SKILL

Le benchmark alimente directement le skill :

- **3 échecs avec la même cause** → ajouter un anti-pattern dans patterns-cookbook.md
- **3 succès avec la même technique** → promouvoir la technique dans la matrice de sélection
- **Taux d'over-engineering > 15%** → renforcer le garde-fou d'efficience dans SKILL.md
- **Scorecard systématiquement > 3 points d'écart avec le réel** → recalibrer les critères
- **Technique jamais utilisée après 20 benchmarks** → candidat à la suppression

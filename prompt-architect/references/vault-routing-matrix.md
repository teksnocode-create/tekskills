# Matrice de Routage — Vault Obsidian ↔ Skill prompt-architect

> Référence satellite du skill prompt-architect v2.2
> Objectif : savoir QUAND consulter le vault Obsidian pendant le workflow du skill

---

> **Note pour les apprenants Hél'IA** : ce fichier a été pré-rempli avec des chemins par défaut prudents. Ils s'adaptent à un vault Obsidian que tu poserais dans `~/Documents/Prompt Engineering/`. Si ton vault est ailleurs (ex : `D:\Obsidian\` sous Windows, ou `~/Vaults/` sous Mac), modifie les 3 chemins ci-dessous. Les `~` correspondent à ton dossier utilisateur (`C:\Users\TonNom\` sous Windows, `/Users/tonnom/` sous Mac).

---

## Principe

Le vault Obsidian contient ~100 fichiers de méthodologies, templates et ressources. Cette matrice indique pour chaque phase du skill quels fichiers du vault consulter et dans quel cas.

**Convention** : les chemins sont relatifs à la racine du vault (`~/Documents/Prompt Engineering/`). À adapter selon où tu as décompressé le zip ou installé ton vault Obsidian.

---

## Phase 1 — DIAGNOSTIC

| Besoin identifié | Fichier vault | Quand le consulter |
|-----------------|---------------|-------------------|
| Personnalisation dynamique par profil utilisateur | `02 - PROMPT ENGINEERING/1-FONDAMENTAUX/methodes-avancees/METH_arg.md` | Intent = chatbot adaptatif, assistant pédagogique |
| Analyse de données business / KPI | `02 - PROMPT ENGINEERING/1-FONDAMENTAUX/methodes-avancees/METH_bip.md` | Intent = dashboard, rapport, analyse metrics |
| Raisonnement structuré cognitif | `02 - PROMPT ENGINEERING/1-FONDAMENTAUX/methodes-avancees/METH_cap.md` | Intent = analyse complexe multi-perspectives |
| Génération de code | `02 - PROMPT ENGINEERING/1-FONDAMENTAUX/methodes-avancees/METH_cgp.md` ou `07 - FORMATION/Prompt Engineer/CODE GENERATION PROMPTING (CGP)_TEXTE.md` | Intent = code production-ready |
| Architecture multi-prompts | `02 - PROMPT ENGINEERING/1-FONDAMENTAUX/methodes-avancees/METH_mpa.md` | Intent = système modulaire, pipeline |

---

## Phase 2 — SÉLECTION STRATÉGIQUE

| Situation de sélection | Ressource vault | Usage |
|-----------------------|-----------------|-------|
| Besoin d'un framework non couvert par la matrice du skill | `02 - PROMPT ENGINEERING/1-FONDAMENTAUX/methodes-avancees/` (tous les METH_*.md) | Explorer les 47 méthodes avancées disponibles |
| Recherche de templates existants | `09 - TEMPLATES/` | Réutiliser un gabarit déjà validé |
| Benchmark d'un cas similaire passé | `~/Documents/Process'Up/Prompts/` (à créer si non existant) | Consulter les prompts de production existants |
| Prompts système de référence (clients) | `~/Documents/Process'Up/Clients/` (à créer si tu as des prompts client) | S'inspirer de prompts déjà déployés |
| Test A/B protocol | `07 - FORMATION/Prompt Engineer/TEST AB DE PROMPTS_TEXTE.md` | Méthodologie complète de test A/B en 6 étapes |

---

## Phase 3 — GÉNÉRATION

| Besoin de génération | Ressource vault | Usage |
|---------------------|-----------------|-------|
| Prompt pour un pipeline RAG | `references/rag-patterns.md` (dans le skill) + `10 - RESSOURCES/Atlanticom - Blog IA/Agent IA en RAG.md` | Patterns RAG (standard, synthèse, conversationnel, critique) |
| Template de system prompt Claude | `09 - TEMPLATES/TPL_system-prompt-claude.md` | Structure de base pour system prompts |
| Prompt pour workflow Make/n8n | `references/automation-templates.md` (dans le skill) + `~/Documents/Process'Up/Prompts/` | Variables mappées, format 1 bloc |

---

## Phase 4 — VALIDATION

| Besoin de validation | Ressource vault | Usage |
|---------------------|-----------------|-------|
| Protocole de test A/B formel | `07 - FORMATION/Prompt Engineer/TEST AB DE PROMPTS_TEXTE.md` | 6 étapes : objectif → variantes → expérimentation → déploiement → collecte → analyse |
| Anti-patterns connus | `references/patterns-cookbook.md` (dans le skill) | Vérifier que le prompt ne contient pas de smell connu |

---

## Phase 6 — BENCHMARK

| Besoin de benchmark | Ressource vault | Usage |
|---------------------|-----------------|-------|
| Historique des prompts déployés | `~/Documents/Process'Up/Prompts/` + `~/Documents/Process'Up/Clients/` | Comparer avec les résultats passés |
| Template de benchmark | `references/benchmark-template.md` (dans le skill) | Fiche standardisée de benchmark |

---

## Index rapide par méthode vault

| Acronyme | Nom complet | Chemin vault | Phase skill |
|----------|------------|-------------|-------------|
| ARG | Adaptive Response Generation | `02/.../METH_arg.md` | Phase 1-2-3 |
| BaP | Brainstorm and Plan | `02/.../METH_bap.md` | Phase 2 |
| BIP | Business Intelligence Prompting | `02/.../METH_bip.md` | Phase 1-2-3 |
| CAP | Cognitive Architecture Prompting | `02/.../METH_cap.md` | Phase 1-2-3 |
| CGP | Code Generation Prompting | `02/.../METH_cgp.md` | Phase 1-2-3 |
| MPA | Modular Prompt Architecture | `02/.../METH_mpa.md` | Phase 1-2-3-5 |
| MODP | Multi-Objective Design Prompting | Intégré au skill principal | Phase 2 |
| Test A/B | Test A/B de Prompts | `07/.../TEST AB DE PROMPTS_TEXTE.md` | Phase 4 |

---

## Règle de consultation

1. **Toujours** consulter le skill d'abord (matrice de sélection rapide du SKILL.md)
2. **Si** le cas n'est pas couvert → consulter `vault-methods-guide.md` (dans references/)
3. **Si** un gabarit prêt à l'emploi est nécessaire → consulter le vault directement
4. **Ne jamais** consulter le vault "au hasard" — toujours avec un intent précis

---

## 🛠 Personnalisation : 3 chemins à ajuster si besoin

Recherche-remplace dans ce fichier si tes dossiers ne sont pas aux emplacements par défaut :

| Placeholder par défaut | Remplace par (exemple) | Pour quoi |
|-----------------------|------------------------|-----------|
| `~/Documents/Prompt Engineering/` | `D:\Obsidian\PromptEngineering\` ou `~/Vaults/Prompt Engineering/` | Racine du vault Obsidian méthodologique |
| `~/Documents/Process'Up/Prompts/` | `~/Documents/MesPrompts/` ou autre dossier où tu archives tes prompts perso | Tes prompts persos / projets |
| `~/Documents/Process'Up/Clients/` | `~/Documents/Clients/` | Tes prompts livrés à des clients |

**Astuce** : sous Windows, `~/` est interprété par la plupart des outils comme `C:\Users\TonNom\`. Si tu veux du chemin absolu, remplace `~/` par `C:\Users\TonNom\`.

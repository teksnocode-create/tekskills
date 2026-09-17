---
name: new-project
description: Initialise la structure complète d'un nouveau repo de projet build (CLAUDE.md, ROADMAP.md, LOGBOOK.md, .gitignore adapté à la stack, dossiers .claude/rules et .claude/skills), puis mène l'interview section par section pour les remplir. Déclencher quand Nicolas tape "/new-project", ou dit "init projet", "nouveau projet", "initialise ce projet", "setup projet", ou ouvre un repo vide pour démarrer un chantier.
---

# Skill : /new-project — Initialisation d'un nouveau projet build

## Déclencheur
Quand Nicolas dit `/new-project`, "init projet", "nouveau projet", "initialise ce projet", "setup projet".

## Objectif
En 3 phases, créer la structure complète d'un nouveau projet build :
- `CLAUDE.md` — contexte projet pour Claude Code
- `ROADMAP.md` — phases et périmètre MVP
- `LOGBOOK.md` — journal de sessions
- `.gitignore` — adapté à la stack détectée
- Dossiers essentiels avec `.gitkeep`

---

## Phase 1 : Créer le squelette

Avant toute question, créer immédiatement la structure suivante (fichiers vides ou avec placeholder) :

```
CLAUDE.md               # À remplir en Phase 3
ROADMAP.md              # À remplir en Phase 3
LOGBOOK.md              # À remplir en Phase 3
.gitignore              # À remplir selon la stack détectée
.claude/
  rules/
    .gitkeep
  skills/
    .gitkeep
docs/
  .gitkeep
```

Confirmer : "Structure créée. Je commence l'interview — une section à la fois."

---

## Phase 2 : Interview — une section à la fois

Poser chaque section séparément. Attendre la réponse avant de passer à la suivante.
Si Nicolas dit "passe" ou "plus tard" : noter un placeholder dans le fichier concerné et avancer.

---

### Section 1 : Le projet

- Nom du projet ?
- Type : SaaS / app mobile / automatisation / site vitrine / CRM / outil interne / autre ?
- En une phrase : quel problème ça résout, pour qui ?
- Projet client ou projet perso ?
- Repo GitHub déjà créé ? URL si oui ?

---

### Section 2 : Stack technique

- Front ? (Next.js, React, Vue, Lovable, FlutterFlow, aucun, autre)
- Back / BDD ? (Supabase, Airtable, Firebase, aucun, autre)
- Auth ? (Supabase Auth, Clerk, NextAuth, aucune, autre)
- Déploiement ? (Vercel, Netlify, VPS, App Store, Play Store, autre)
- Automatisation ? (n8n, Make, aucune, autre)
- Autres services ou APIs à intégrer ? (Stripe, OpenAI, Unipile, Brevo, etc.)

---

### Section 3 : MVP — périmètre

- Les 3 à 5 features du MVP (ce qui est IN) ?
- Ce qui est explicitement hors scope (pour ne pas dériver) ?
- Une deadline ou date cible ?

---

### Section 4 : Données & sécurité

- Tables principales et leur rôle en une ligne chacune ?
- Données sensibles à ne jamais exposer côté client ? (clés API, tokens, webhooks secrets)
- Accès : public / avec login utilisateur / admin uniquement ?
- Ce projet utilise Supabase avec de l'auth et/ou des données utilisateurs sensibles ? (oui / non) → si oui, les règles de sécurité avancées seront activées automatiquement en Phase 3

---

### Section 5 : Déploiement & conventions

- Déploiement automatique (push → Vercel) ou manuel (CLI) ?
- Conventions de code : TypeScript strict ? ESLint ? Naming particulier ?
- Langue du projet pour le code et les commentaires : FR ou EN ?

---

## Phase 3 : Générer les fichiers

À partir des réponses, remplir les fichiers. Générer dans cet ordre.

**Règle de déclenchement sécurité :** si la réponse S4 indique Supabase + auth OU données sensibles → générer aussi `.claude/rules/security-supabase.md` (voir section dédiée ci-dessous) et le référencer dans CLAUDE.md.

---

### CLAUDE.md

Utiliser cette structure (rester sous 120 lignes) :

```markdown
# CLAUDE.md — [Nom du projet]

> [problème résolu — une phrase]

## Stack technique
- **Front** : [réponse S2]
- **Back / BDD** : [réponse S2]
- **Auth** : [réponse S2]
- **Déploiement** : [réponse S2]
- **Automatisation** : [réponse S2]
- **Repo** : [URL ou "non créé"] — branche principale : `main`

## Déploiement
**État actuel** : [auto / manuel / non configuré]

## Sécurité — règles absolues
- Ne jamais exposer [données sensibles S4] côté client ou dans le repo
- [autres règles selon S4]
[Si sécurité avancée activée → ajouter : `- Règles détaillées : voir `.claude/rules/security-supabase.md``]

## Modèle de données
[tables et rôles issus de S4 — format tableau si plusieurs tables]

## Intégrations externes
[services issus de S2/S5 — un bullet par service : rôle + côté serveur ou client]

## Skills Claude — quand les proposer
- **/qa** : quand une feature est déclarée terminée, avant déploiement
- **/investigate** : dès qu'une erreur ou comportement inattendu est mentionné
- **/review** : avant tout commit sur `main` touchant auth, RLS ou server actions
- **/security-review** : dès qu'une modif touche auth, permissions ou données sensibles
- **/run** : pour tester une feature UI dans le vrai browser avant de la déclarer terminée

## Pilotage
- **ROADMAP.md** : état d'avancement par phases — source de vérité
- **LOGBOOK.md** : journal chronologique des sessions

## Conventions
- [langue du code : FR/EN]
- [TypeScript strict / ESLint / naming]
- [autres conventions S5]

## Mots-clés projet
<!-- Skills propres à CE projet — ne pas lister les skills globaux (open, close, recap) -->
<!-- Format : `mot-clé` → ce que ça fait -->
```

---

### ROADMAP.md

```markdown
# ROADMAP — [Nom du projet]

_Dernière mise à jour : [date du jour]_

## Phase 0 — Setup (fait)
- [x] Init projet, CLAUDE.md, ROADMAP.md, LOGBOOK.md

## Phase 1 — MVP
- [ ] [feature 1 de S3]
- [ ] [feature 2 de S3]
- [ ] [feature 3 de S3]
[ajouter les features supplémentaires si mentionnées]

**Deadline MVP** : [date S3 ou "non définie"]

## Phase 2 — Post-MVP
_(à définir après livraison du MVP)_

## Hors scope — ne pas dériver
- [out 1 de S3]
- [out 2 de S3]
```

---

### LOGBOOK.md

```markdown
# LOGBOOK — [Nom du projet]

Journal chronologique des sessions. Une entrée par session, append-only.

---

## [date du jour] — Session 0 : Init projet

**Fait**
- Structure projet initialisée (CLAUDE.md, ROADMAP.md, LOGBOOK.md)
- Stack définie : [résumé stack S2]
- MVP cadré : [nb] features, deadline [date ou "non définie"]

**Décisions**
- [toute décision structurante prise pendant l'interview]

**Prochaine étape**
- [première feature du MVP ou première tâche concrète]
```

---

### .claude/rules/security-supabase.md (conditionnel)

Générer uniquement si Supabase + auth OU données sensibles confirmés en S4.

```markdown
# Règles de sécurité — Supabase + Auth

## Patterns API — obligatoires sur chaque endpoint

- **IDOR** : vérification atomique sur toute opération sensible — `WHERE id=$1 AND user_id=$2`
- **Race conditions** : `SELECT ... FOR UPDATE` sur les ressources partagées
- **Rate limiting** : fail-closed en prod sur login, exports, endpoints IA
- **Tokens** : comparaison avec `crypto.timingSafeEqual()` — jamais `===`
- **Inputs** : validation Zod avec `.strict()` obligatoire — whitelist explicite, pas de passthrough
- **Pagination** : limite dure côté serveur sur toutes les listes — jamais illimitée
- **Secrets** : jamais en dur — `import.meta.env` (front) et `process.env` (back) uniquement

## Authentification & sessions

- Tokens stockés exclusivement en cookies `HttpOnly, Secure, SameSite=Strict`
- `localStorage` et `sessionStorage` interdits pour tout token ou donnée de session
- Ajouter un champ `sessionVersion` dans le profil pour permettre la déconnexion globale
- Vérification blacklist DB sur les tokens révoqués

## Supabase & base de données

- **RLS obligatoire** sur toutes les tables — pas de `FOR ALL`, pas de table sans politique
- Optimiser les politiques avec `(select auth.uid())` pour éviter les appels répétés
- Rôle `anon` : policies restrictives par défaut — refuser si pas de règle explicite
- Fonctions PL/pgSQL avec `SET search_path = ''` pour éviter le schema hijacking
- Extensions installées dans un schéma `extensions` dédié (jamais dans `public`)
- Triggers en écriture sur les colonnes sensibles : `updated_at`, `role`, `sessionVersion`
- Table `audit_logs` pour tracer les actions critiques : acteur, table, diff JSON, timestamp

## IA & agents LLM (si applicable)

- Encadrer les inputs utilisateurs avec des balises explicites : `<user_input>...</user_input>`
- Valider et assainir (XSS) les outputs des LLM avant affichage ou stockage
- Les actions IA opèrent avec le token de l'utilisateur (limité par son RLS)
- Jamais de `service_role` pour une action déclenchée par un agent IA
```

---

### .gitignore

Générer selon la stack détectée en S2. Base systématique :

```
.env
.env.local
.env*.local
CLAUDE.local.md
.claude/settings.local.json
node_modules/
.DS_Store
```

Ajouter selon la stack :
- Next.js : `.next/`, `out/`
- Vercel : `.vercel/`
- Supabase : `.supabase/`
- Python : `__pycache__/`, `*.pyc`, `.venv/`

---

## Étape finale

Une fois les fichiers générés :

1. Afficher l'arborescence complète des fichiers créés
2. Résumé en une ligne par fichier (indiquer si `security-supabase.md` a été activé ou non)
3. Créer le premier commit git : `feat: init projet [nom] — structure, CLAUDE.md, ROADMAP.md, LOGBOOK.md`
4. Demander : "Tu veux qu'on attaque quelle feature en premier ?"

---

## Règles pour Claude

- Créer le squelette Phase 1 AVANT de poser la moindre question
- Poser les sections UNE PAR UNE — ne jamais balancer toutes les questions d'un coup
- Si "passe" ou "plus tard" : placeholder dans le fichier, on avance
- CLAUDE.md sous 120 lignes — si ça déborde, c'est qu'on y met trop de choses
- Pas de contenu dupliqué entre CLAUDE.md et ROADMAP.md — chaque info a une seule maison
- Ne pas créer de skills pendant le setup — `.claude/skills/` reste vide
- Si le repo GitHub n'existe pas encore : ne pas bloquer, noter "non créé" dans CLAUDE.md et avancer

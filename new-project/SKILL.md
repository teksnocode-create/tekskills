---
name: new-project
description: Initialise la structure complète d'un nouveau repo de projet build (CLAUDE.md, ROADMAP.md, LOGBOOK.md, .gitignore adapté à la stack, skills projet open/log/close, checklist OWASP), puis mène l'interview section par section pour les remplir. Déclencher quand Nicolas tape "/new-project", ou dit "init projet", "nouveau projet", "initialise ce projet", "setup projet", ou ouvre un repo vide pour démarrer un chantier.
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

`.claude/skills/` ne reste pas vide : `open`, `log` et `close` y sont générés en Phase 3.

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
- Tu es seul sur ce repo, ou plusieurs personnes y travaillent ? (détermine la version du `/close` généré)

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
- Checklist OWASP Top 10 à repasser avant toute mise en production : voir `.claude/rules/owasp-checklist.md`
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
<!-- `/open`, `/log` et `/close` sont générés dans ce repo et lui appartiennent : les modifier ici ne touche aucun autre projet -->
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

### .claude/skills/ — open, log, close (systématique)

Générer les 3 dans **tous** les projets. Ils appartiennent à ce repo : les modifier ici ne touche aucun autre projet, et sur un repo partagé ils portent le process de l'équipe.
Remplacer `[NOM]` par le nom du projet. Le `/close` a deux variantes selon la réponse « seul ou à plusieurs » de la section 1.

#### `.claude/skills/open/SKILL.md`

```markdown
---
name: open
description: Reprise de session sur [NOM]. Affiche où en est le projet, ce qui est en cours et ce qui traîne non commité. Déclencher sur "/open", "on reprend", "où on en est".
---

# /open — [NOM]

## Déroulé
1. Lire `ROADMAP.md` : phase en cours, features cochées, features restantes
2. Lire les 3 dernières entrées de `LOGBOOK.md` : ce qui a été fait, la prochaine étape notée la dernière fois
3. `git status` et `git log --oneline -5` : travail non commité, derniers commits, branche courante

## Sortie
```
OPEN — [NOM] — [date]
**Où on en est** : phase [X], [N] features sur [M]
**Dernière session** : [date] — [résumé en une ligne]
**Prochaine étape notée** : [reprise du LOGBOOK]
**Non commité** : [fichiers, ou "rien"]
```

## Règles
- Lire les fichiers en direct, ne jamais se fier à la mémoire de la conversation
- Si `LOGBOOK.md` est vide, le dire au lieu d'inventer
- Ne rien modifier : `/open` est en lecture seule
```

#### `.claude/skills/log/SKILL.md`

```markdown
---
name: log
description: Snapshot de la conversation en cours dans le LOGBOOK de [NOM], pour fermer une fenêtre sans perdre le fil. Déclencher sur "/log", "note ce qu'on a fait", "archive ça".
---

# /log — [NOM]

## Déroulé
1. Extraire de la conversation : ce qui a été produit, les décisions structurantes, la prochaine étape concrète
2. Ajouter à la suite de `LOGBOOK.md` :

```
### [HH:MM] — [sujet en 3 à 5 mots]

**Fait**
- [5 bullets maximum, synthétisés]

**Décisions**
- [uniquement ce qui engage la suite, sinon "aucune"]

**Prochaine étape**
- [une seule, la plus immédiate]
```

## Règles
- 5 bullets maximum dans "Fait" : synthétiser, pas tout lister
- Ne pas commiter, ne pas pousser : `/log` écrit un fichier, c'est tout
- Si la session a déjà une entrée du jour, compléter sous le même titre de date
```

#### `.claude/skills/close/SKILL.md`

```markdown
---
name: close
description: Clôture de session sur [NOM] : bilan, LOGBOOK, ROADMAP, contrôle de ce qui part sur GitHub, commit et push. Déclencher sur "/close", "on ferme", "fin de session".
---

# /close — [NOM]

## Étape 0 : le cadre
Date du jour et jour de la semaine.
[VARIANTE MULTI-PERSONNES : demander le prénom de la personne au clavier, il apparaît dans l'entrée du LOGBOOK et dans le message de commit.]

## Étape 1 : le bilan, avant toute question
Produire le bilan à partir de la conversation et du `git diff`, puis le soumettre pour correction. Ne pas demander « qu'est-ce que tu as fait ? » à quelqu'un qui vient de le faire.

Trois blocs : **fait aujourd'hui**, **en cours / points ouverts**, **bloqué, en attente de quelqu'un**.

## Étape 2 : écrire dans `LOGBOOK.md`
Une entrée par session, append-only, jamais de réécriture d'une entrée passée.

## Étape 3 : mettre à jour `ROADMAP.md`
Cocher ce qui est livré. Ajouter ce qui est apparu en cours de route. Si une feature sort du périmètre, la déplacer en « Hors scope » avec la raison, ne pas la supprimer.

## Étape 4 : contrôle de ce qui part sur GitHub
Avant tout commit, vérifier ligne par ligne dans le diff :
- Aucun secret, clé d'API, token ni clé de service
- `.env` bien ignoré, aucun fichier de credentials indexé
- Aucune donnée client réelle, aucun identifiant, aucune adresse
- Aucun export ni dump de base

Un doute sur un fichier se traite avant le commit, pas après le push.

## Étape 5 : la sécurité, si quelque chose part en production
Si la session met quelque chose en ligne ou touche à l'authentification, aux permissions ou aux données utilisateurs, repasser `.claude/rules/owasp-checklist.md` et reporter les points non traités avec leur raison.

## Étape 6 : commit et push
`git add` ciblé (jamais `git add .` à l'aveugle), commit, `git pull --rebase`, `push`. En cas de conflit, le résoudre fichier par fichier et le signaler, ne jamais forcer.

## Étape 7 : la sortie
Une ligne : ce qui est poussé, et la prochaine étape.

## Règles
- Le bilan se propose, il ne se demande pas
- `LOGBOOK.md` est append-only
- Rien ne part sur GitHub sans l'étape 4
```

---

### .claude/rules/owasp-checklist.md (systématique)

Générer sur **tous** les projets, sans condition, même sans Supabase et sans auth. Dix questions coûtent 10 minutes, une fuite de données entre clients payants coûte le client.

```markdown
# Checklist OWASP Top 10:2025

Source : https://top10.owasp.org/2025/

## Quand la repasser
- Avant chaque mise en production
- Dès qu'on touche à l'authentification, aux permissions ou aux données utilisateurs
- Dès qu'on ajoute une dépendance ou un service externe

Une ligne qui n'est pas cochée n'est pas un détail à traiter plus tard : c'est une décision à prendre et à écrire.

## Les 10 points

- [ ] **A01 Broken Access Control** — un compte connecté peut-il lire ou modifier les données d'un autre compte ? Tester en conditions réelles avec deux comptes, pas en lisant le code. *Déjà vécu : fuite inter-comptes SynkParty, et table des posts Cyrano sans aucune autorisation d'écriture pendant 9 jours.*
- [ ] **A02 Security Misconfiguration** — `.env` bien ignoré par git, aucune clé de service côté client, pas de compte ni de mot de passe par défaut laissé actif. *Déjà vécu : `.env` absent du `.gitignore` sur Iris Cup.*
- [ ] **A03 Software Supply Chain Failures** — d'où viennent les dépendances et les templates utilisés, et qui peut pousser du code qui part en production ?
- [ ] **A04 Cryptographic Failures** — quelles données sensibles sont stockées, et sous quelle forme ? Aucun secret, aucun code d'accès en clair dans le dépôt ni dans un document qui circule. *Déjà vécu : codes PIN de démonstration reproduits dans un mémoire diffusé.*
- [ ] **A05 Injection** — toute entrée utilisateur est validée côté serveur, jamais concaténée dans une requête. Vaut aussi pour les entrées passées à un modèle IA.
- [ ] **A06 Insecure Design** — le scénario d'abus a-t-il été posé avant de coder ? Qui a intérêt à tricher ici, et qu'est-ce qui l'en empêche ?
- [ ] **A07 Authentication Failures** — comment on se connecte, comment on se déconnecte partout, et que vaut réellement le facteur utilisé (un code à 4 chiffres n'est pas une authentification).
- [ ] **A08 Software or Data Integrity Failures** — que se passe-t-il si une automatisation écrase une donnée saisie à la main ? Qui gagne en cas de conflit, et c'est écrit où ?
- [ ] **A09 Security Logging and Alerting Failures** — si ça tombe en panne cette nuit, qui l'apprend et au bout de combien de temps ? Une alerte que personne n'ouvre ne compte pas comme une alerte. *Déjà vécu : relances SynkParty en panne 7 jours sans signal, trouvées par hasard ; alerte n8n Cyrano déclenchée à 9h05 et ouverte 7 heures plus tard.*
- [ ] **A10 Mishandling of Exceptional Conditions** — que fait le système quand l'API externe ne répond pas, renvoie une erreur ou des données vides ? Un échec silencieux est pire qu'un plantage.

## Règle
Les points non traités restent listés ici avec la raison et la date, jamais effacés.
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
2. Résumé en une ligne par fichier (indiquer si `security-supabase.md` a été activé ou non ; `owasp-checklist.md` et les 3 skills `open`/`log`/`close` sont toujours présents)
3. Créer le premier commit git : `feat: init projet [nom] — structure, CLAUDE.md, ROADMAP.md, LOGBOOK.md`
4. Demander : "Tu veux qu'on attaque quelle feature en premier ?"

---

## Règles pour Claude

- Créer le squelette Phase 1 AVANT de poser la moindre question
- Poser les sections UNE PAR UNE — ne jamais balancer toutes les questions d'un coup
- Si "passe" ou "plus tard" : placeholder dans le fichier, on avance
- CLAUDE.md sous 120 lignes — si ça déborde, c'est qu'on y met trop de choses
- Pas de contenu dupliqué entre CLAUDE.md et ROADMAP.md — chaque info a une seule maison
- Les seuls skills générés au setup sont `open`, `log` et `close`, propres à ce repo. Ne pas en créer d'autres tant qu'un workflow récurrent n'a pas émergé
- Ne jamais transformer ces 3 skills en skills globaux : sur un repo partagé, ils portent le process de l'équipe et une version globale l'écraserait pour tout le monde
- Si le repo GitHub n'existe pas encore : ne pas bloquer, noter "non créé" dans CLAUDE.md et avancer

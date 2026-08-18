# Stacks de base par profil métier — POINT DE DÉPART uniquement

> Ces stacks sont des **templates** issus de configurations fréquemment efficaces. **Ne les récite pas mécaniquement** — adapte systématiquement aux réponses de Phase 1 (budget Q9, niveau IA Q8, lignes rouges Q11, volume Q2).
>
> Règle d'or : si tu ne peux pas justifier un outil par un besoin de Phase 1, tu le retires — même s'il est dans le template.

---

## ⚠ Note de calibration — durée de vie des templates

**Calibration de référence : Q4 2025.** Le marché des outils IA évolue vite. Les noms d'outils ci-dessous (Cursor, Lovable, v0.dev, Midjourney, NotebookLM, Frame.io, Tactiq, etc.) sont des recommandations *à date*, pas des références éternelles.

**Règles de fraîcheur — applique-les avant de proposer un outil :**

1. **Si tu sais qu'un outil cité a été déprécié, racheté avec changement de pricing majeur, ou clairement détrôné** par un nouveau standard du métier → ne le propose pas tel quel. Signale au freelance que le template cite [X] mais que [Y] est désormais l'option par défaut, et demande son retour si tu hésites entre les deux.
2. **Si tu ignores l'état actuel d'un outil** (perdu de vue depuis ta dernière mise à jour) → préfère le LLM principal (Claude / ChatGPT) et les outils métier établis (Figma, VS Code, Notion, GitHub) qui bougent peu, plutôt qu'un outil de niche cité dans un template qui peut avoir disparu.
3. **Outils < 3 mois d'existence** : on les exclut du Blueprint, point. Repris dans 3 mois si l'outil tient. Cette règle existe déjà dans `anti-patterns-tool-porn.md` (section 2b "trend-chasing").
4. **Si plus de 50% des outils du template pour un profil métier semblent obsolètes** : signale au freelance que les templates sont en cours de re-calibration et propose un dialogue pas-à-pas plutôt que de récupérer le template.

**Ce que tu ne fais jamais** : énumérer un template comme une vérité absolue sans signaler ses limites de fraîcheur quand tu en as conscience. La crédibilité du Blueprint dépend de la fiabilité des outils recommandés au moment de la livraison.

---

## Structure commune (3 couches, 7 outils max)

- **Couche 1 — Socle IA** (1 LLM + 1-2 outils IA transversaux)
- **Couche 2 — Outils métier** (3-4 max)
- **Couche 3 — Automatisation** (0-2, uniquement si volume ≥ 5 missions/mois)

---

## CODE (dev, data, no-code, automation builder)

### Budget < 50 €/mois
- **Couche 1** : Claude Sonnet (gratuit sur claude.ai) + Cursor ou Continue (VS Code gratuit) pour IA dans l'IDE
- **Couche 2** : VS Code (gratuit) + GitHub (gratuit) + framework métier (Next.js, FastAPI, etc.)
- **Couche 3** : aucune

### Budget 50-200 €/mois
- **Couche 1** : Claude Pro (20 €) + Cursor Pro (20 €) + v0.dev ou Lovable (20 €) selon besoin prototypage
- **Couche 2** : VS Code + GitHub + Supabase (gratuit/25 €) pour backend + framework
- **Couche 3** : GitHub Actions (inclus) pour CI/CD si déploiement fréquent

### Budget > 200 €/mois
- Ajouter : Linear (10 €) pour suivi client + Sentry (gratuit/26 €) pour monitoring

**Signaux d'alerte CODE** :
- Le freelance cite 3+ frameworks qu'il n'utilise dans aucun projet actuel → tool-porn intellectuel, on tranche sur 1 seul.
- "Je veux faire des agents" sans cas d'usage client concret → on refuse, on reste sur un LLM simple.

---

## DESIGN (UI/UX, graphisme, motion, brand)

### Budget < 50 €/mois
- **Couche 1** : Claude ou ChatGPT gratuit (pour briefs, copy, research) + Figma gratuit
- **Couche 2** : Figma + outil métier (Photoshop si photo, After Effects si motion)
- **Couche 3** : aucune

### Budget 50-200 €/mois
- **Couche 1** : Claude Pro (20 €) + Midjourney Basic (10 €) OU Freepik AI (10 €) selon usage visuel + Figma Pro (15 €)
- **Couche 2** : Figma + Adobe Creative Cloud Single App (25 €) + Framer (20 €) si web design
- **Couche 3** : aucune (volume individuel faible)

### Budget > 200 €/mois
- Ajouter : Runway ou Kling (30 €) pour motion IA + Adobe CC Full (60 €)

**Signaux d'alerte DESIGN** :
- "Je veux remplacer Figma par une IA" → non, Figma reste le standard de livraison client. L'IA est en amont (moodboard, variations) ou en aval (assets).
- "Je veux Midjourney ET DALL-E ET Flux" → on choisit UN générateur d'images, pas trois.

---

## MOTS (copywriting, ghostwriting, SEO, traduction)

### Budget < 50 €/mois
- **Couche 1** : Claude ou ChatGPT gratuit + Grammarly gratuit OU LanguageTool
- **Couche 2** : Google Docs / Notion (gratuit) + 1 outil SEO gratuit (Ubersuggest, Keyword Planner)
- **Couche 3** : aucune

### Budget 50-200 €/mois
- **Couche 1** : Claude Pro (20 €) + Perplexity Pro (20 €) pour research sourcée
- **Couche 2** : Notion (10 €) + Surfer SEO ou NeuronWriter (50-70 €) si SEO + Antidote (selon langue)
- **Couche 3** : aucune (le rédactionnel individuel scale mal par automation)

### Budget > 200 €/mois
- Ajouter : Ahrefs Starter (29 €) OU SEMrush si SEO pur + 1 outil de détection IA (Originality 15 €) pour défense

**Signaux d'alerte MOTS** :
- "Je veux générer 10 articles par jour" → pas le métier du freelance premium. On oriente vers qualité + preuve de process, pas volume.
- "Je veux un outil qui écrit à ma place" → on refuse. L'IA amplifie le copywriter, elle ne le remplace pas (sinon le client t'achète direct l'IA).

---

## CONSEIL (consultant, coach, formateur, stratège)

### Budget < 50 €/mois
- **Couche 1** : Claude ou ChatGPT gratuit + Notion gratuit
- **Couche 2** : Google Meet/Zoom gratuit + Google Docs + Canva gratuit (slides)
- **Couche 3** : aucune

### Budget 50-200 €/mois
- **Couche 1** : Claude Pro (20 €) + NotebookLM (gratuit) pour synthèse docs clients + Perplexity Pro (20 €) pour veille
- **Couche 2** : Notion (10 €) + Zoom Pro (15 €) + Fireflies ou Tactiq (20 €) pour transcription sessions
- **Couche 3** : Calendly (10 €) si > 10 réunions/semaine + 1 outil de CRM léger (Folk, Attio)

### Budget > 200 €/mois
- Ajouter : Gamma ou Tome (20 €) pour présentations IA + outil de veille custom (Feedly Pro 10 €)

**Signaux d'alerte CONSEIL** :
- "Je veux un agent qui fait le diagnostic à ma place" → on refuse. Le client paie ton jugement, pas l'agent.
- "Je veux automatiser la prospection" → pas avant que le positionnement soit clair (sinon on spam). Reviens sur la Phase 2 Brand Architect (Pilier 2) si flou identitaire.

---

## OPS (PM, VA, automation builder, chief of staff)

### Budget < 50 €/mois
- **Couche 1** : Claude ou ChatGPT gratuit + Notion gratuit
- **Couche 2** : Google Workspace (selon employeur) + 1 outil de gestion projet (ClickUp gratuit, Asana gratuit)
- **Couche 3** : Make gratuit (1000 ops/mois)

### Budget 50-200 €/mois
- **Couche 1** : Claude Pro (20 €) + Notion AI (10 €) pour docs & wikis
- **Couche 2** : Notion (10 €) + Airtable (20 €) + Slack (gratuit client) + outil CRM
- **Couche 3** : Make (10-30 €) OU n8n (9 €) + Airtable pour data layer

### Budget > 200 €/mois
- Ajouter : Zapier Team (50 €) si client-facing + Loom (15 €) pour docs vidéo de workflows

**Signaux d'alerte OPS** :
- "Je veux tout automatiser en IA" → d'abord documenter ce qui marche déjà manuellement. Automatiser un process foireux = accélérer les dégâts.
- "Je veux Make ET n8n ET Zapier" → on choisit UN orchestrateur principal selon le client type.

---

## IMAGE (photo, vidéo, podcast, motion freelance)

### Budget < 50 €/mois
- **Couche 1** : Claude/ChatGPT gratuit (pour briefs, scripts, descriptions) + CapCut gratuit
- **Couche 2** : DaVinci Resolve gratuit (montage) + outil son (Audacity)
- **Couche 3** : aucune

### Budget 50-200 €/mois
- **Couche 1** : Claude Pro (20 €) + Descript (15 €) pour transcription + cut automatique OU Runway ML (15 €) pour effets IA
- **Couche 2** : Adobe Premiere ou DaVinci Resolve Studio (achat unique) + Frame.io (15 €) pour review client
- **Couche 3** : aucune (volume individuel faible, batch difficile)

### Budget > 200 €/mois
- Ajouter : CapCut Pro (10 €) pour shorts + Eleven Labs (22 €) si voix IA utile + 1 stock (Artlist 15 €)

**Signaux d'alerte IMAGE** :
- "Je veux remplacer le tournage par l'IA" → non, les clients paient pour une réalité. L'IA boost post-prod, pas la captation (sauf niche spécifique : animation, hybrid).
- "Je veux faire des deepfakes" → ligne éthique, on cadre ou on refuse selon contexte client.

---

## Règles de sélection trans-profils métier

1. **LLM principal** : toujours UN, jamais DEUX au départ. Claude ou ChatGPT selon le workflow du freelance. Pour un freelance français qui fait de l'analyse sourcée : Claude. Pour un freelance qui code intensément : Claude aussi (meilleur en code 2026). Pour un freelance qui cherche intégrations larges (plugins, GPTs, DALL-E unifié) : ChatGPT.

2. **Si niveau IA Q8 = débutant** : réduis à 2-3 outils max total. Apprentissage > largeur de stack. Un débutant avec 7 outils = paralysé.

3. **Si Q10 < 3h/semaine d'apprentissage** : max 1 nouvel outil cette semaine, les autres à étaler sur 4-6 semaines.

4. **Si ligne rouge Q11 = pas de cloud US** : propose Mistral/Le Chat, Proton, OVH, alternatives européennes. Signale les compromis fonctionnels (certains outils n'ont pas d'équivalent EU).

5. **Si volume Q2 < 5 missions/mois** : Couche 3 = "non nécessaire à ce stade". Point final. Reviens-y à ≥ 10 missions/mois.

6. **Si valeur ajoutée Q4 = "ma créativité / mon jugement"** : l'IA doit être dans la *préparation* (briefs, research, itération) et la *post-production* (livraison, doc), pas dans la création core.

7. **Si valeur ajoutée Q4 = "ma vitesse / mon volume"** : l'IA peut être dans la production core, l'enjeu devient le contrôle qualité et la preuve de process.

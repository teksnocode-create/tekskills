---
name: zik-dl
description: >
  Automatise le téléchargement de morceaux depuis SoulseekQt sur CE Mac, à partir de la table "💿 Tracks" d'Airtable (base SOREK). Traite par lots de 50 morceaux pas encore téléchargés et pas déjà marqués introuvables : pilote SoulseekQt en local (screencapture + cliclick + AppleScript), double-clique sur le meilleur MP3 320kbps disponible, coche "Download" dans Airtable dès que le download est lancé. Un morceau sans résultat (ou dont le seul résultat est risqué, ex. nom de fichier contenant une URL) est immédiatement coché "Pas trouvé" pour ne plus être retenté automatiquement. À la fin de chaque lot, vérifie dans "~/Soulseek Downloads/complete" quels morceaux sont réellement arrivés, corrige Airtable, puis nettoie et normalise les fichiers avec le script clean.sh du skill. Utiliser ce skill SYSTÉMATIQUEMENT dès que Nico tape "/zik-dl", "télécharge la zik", "lance le téléchargement", "download zik", "télécharge mes morceaux", "récupère mes morceaux", ou mentionne vouloir récupérer sa liste de morceaux Airtable via Soulseek.
---

Base directory de ce skill : `~/.claude/skills/zik-dl`

# Zik Download — Airtable → SoulseekQt (exécution locale sur le Mac de Nico)

## Ce que ce skill fait

1. Lit la liste des morceaux à télécharger depuis la table "💿 Tracks" d'Airtable, en excluant tout morceau déjà coché "Download" ou déjà coché "Pas trouvé"
2. Traite les morceaux par lots de **50**
3. Pour chaque morceau : cherche dans SoulseekQt, double-clique sur le meilleur MP3 320kbps, coche "Download" dans Airtable dès que le téléchargement démarre (flèche verte sur la ligne du résultat), puis passe au suivant
4. Si rien n'apparaît au bout de 10 secondes (ou si le seul résultat est risqué), coche immédiatement "Pas trouvé" et passe au suivant. **Ne jamais retenter un morceau déjà marqué introuvable dans le même run.**
5. Si un morceau fait planter SoulseekQt : coche "Pas trouvé", relance l'app, continue
6. Fin de lot : vérifie ce qui est réellement arrivé dans `~/Soulseek Downloads/complete`, décoche "Download" pour les absents
7. Résumé du lot, puis nettoyage du dossier complete

---

## Étape 0 — Prérequis locaux (à vérifier une seule fois par session)

```bash
which cliclick || echo "MANQUANT: brew install cliclick"
ls -d /Applications/SoulseekQt.app
```

- `cliclick` est **obligatoire** (double-clic et clic à des coordonnées précises). S'il manque, dire à Nico de lancer `brew install cliclick` et s'arrêter là.
- Le terminal qui exécute Claude Code doit avoir les autorisations macOS **Enregistrement de l'écran** (pour `screencapture`) et **Accessibilité** (pour `cliclick` / System Events). Si un screenshot revient noir ou vide, c'est ça : demander à Nico d'activer la permission dans Réglages > Confidentialité et sécurité.

Dossier de travail pour les screenshots : le scratchpad de la session (voir contexte système), un fichier réutilisé `sk.png`.

---

## Étape 1 — Récupérer la liste depuis Airtable

Appelle `mcp__airtable__list_records` :

```json
{
  "baseId": "appNRzvkpeNfDaHCV",
  "tableId": "tbl9N0v65ab5GuI6R",
  "fields": ["Name", "Download", "Pas trouvé", "Artistes", "Morceaux"],
  "filterByFormula": "AND({Download} = 0, {Pas trouvé} = 0)",
  "maxRecords": 50
}
```

> Le serveur Airtable MCP actuel utilise `filterByFormula` (formule Airtable, noms de champs entre accolades) et `maxRecords`. Les anciens paramètres `filters` / `pageSize` / `fieldIds` n'existent plus.

Pour connaître le nombre total restant (pour le résumé de fin), refais le même appel sans `maxRecords` et avec `fields: ["Name"]`, puis compte les records.

Pour chaque record, retiens :
- `id` : identifiant Airtable du record
- `fields.Name` (ou `Artistes` + `Morceaux` si vide) : le nom à chercher dans Soulseek

Si la liste est vide → informer Nico ("Tout est déjà téléchargé ou marqué introuvable !") et s'arrêter.

---

## Étape 2 — Ouvrir SoulseekQt (une seule fois en début de session)

```bash
open -a SoulseekQt
sleep 4
screencapture -x -D 1 -o "$SCRATCH/sk.png"
```

**Le focus ne se prend PAS avec `tell application "SoulseekQt" to activate`** (app Qt, l'ordre est ignoré). Utilise systématiquement :

```bash
osascript -e 'tell application "System Events" to set frontmost of process "SoulseekQt" to true'
```

Config écran mesurée sur cette machine : deux écrans 1920x1080, **ratio 1:1, aucune division par 2 à faire** sur les coordonnées lues dans le screenshot. SoulseekQt s'ouvre sur le **display 1** (`screencapture -D 1`). Si Nico déplace la fenêtre, recale avec :

```bash
osascript -e 'tell application "System Events" to tell process "SoulseekQt" to get position of window 1 & size of window 1'
```

Coordonnées de référence (fenêtre à sa position habituelle 194,82 taille 1610x779) :
- champ de recherche : `845,238`
- onglet Search : `1015,159`
- première ligne de résultats : vers `y=340`, les lignes suivantes espacées d'environ 18 px

**Terminal reprend le focus pendant les `sleep`.** Donc : refais un `set frontmost` juste avant chaque frappe ET juste avant chaque `screencapture`, sinon tu tapes dans le terminal et tu photographies la mauvaise fenêtre.

---

## Étape 3 — Boucle : chercher et télécharger chaque morceau du lot

### 3a. Focus sur l'app et l'onglet Search

```bash
osascript -e 'tell application "System Events" to set frontmost of process "SoulseekQt" to true'
```
Si l'onglet Search n'est pas actif sur le dernier screenshot : `cliclick c:1015,159`.

### 3b. Saisir la recherche

Construis la requête ainsi, dans cet ordre :

1. **Un seul artiste : le premier de la liste `Artistes`.** Une requête à rallonge ne matche aucun nom de fichier réel. `Anuel AA, Daddy Yankee, KAROL G, J Balvin, Ozuna China` → 0 résultat ; `Anuel AA China` → le morceau en tête de liste. Idem `Heuss L'enfoiré Aristocrate` → `Heuss Aristocrate`.
2. **Supprime virgules, points, parenthèses et apostrophes.** Ce qui suit l'apostrophe se coupe aussi si le mot devient bancal (`Heuss L'enfoiré` → `Heuss`).
3. **Retire les mentions feat./remix** sauf si c'est justement la version cherchée.

Résultat visé : `<premier artiste> <titre>`, 2 à 5 mots. Si ça ne donne rien, ce n'est pas la requête qu'il faut rallonger — passe au suivant et coche "Pas trouvé".

```bash
cliclick c:<x_champ>,<y_champ>
osascript -e 'tell application "System Events" to keystroke "a" using command down'
osascript -e 'tell application "System Events" to keystroke "<requête nettoyée>"'
osascript -e 'tell application "System Events" to key code 36'   # Entrée
```

> Passe la requête via une variable shell entre guillemets simples pour éviter que les apostrophes cassent l'AppleScript ; supprime aussi les apostrophes de la requête, elles ne servent à rien pour Soulseek.

### 3c. Attendre et analyser les résultats

```bash
sleep 10 && screencapture -x -o "$SCRATCH/sk.png"
```
Puis Read `sk.png`.

**Aucun résultat** : coche "Pas trouvé" dans Airtable (étape 3f), ajoute-le à la liste des introuvables, passe au suivant. Pas de variante, pas de deuxième essai.

**Seul résultat risqué** (nom de fichier contenant une URL type "www.xxx.com/.org", ou tout ce qui ressemble à un lien) : ne pas cliquer, coche "Pas trouvé", passe au suivant.

**Résultats présents** : le filtre par défaut de SoulseekQt (`mp3 iscbr mbr:320`, visible en bas à droite) filtre déjà en MP3 320kbps.

La liste est un **arbre** (Expand Folders / Expand Users activés) : les lignes "user" et "dossier" ne sont PAS téléchargeables. Ne double-clique que sur une ligne qui porte un **nom de fichier dans la colonne "File"** et un débit dans "Attributes" (ex. `320kbps, 4m42s`).

Prends le **premier résultat fichier** dont le nom correspond au morceau cherché et double-clique dessus :

```bash
cliclick dc:<x_ligne>,<y_ligne>
```

> Pourquoi le premier ? Soulseek trie par disponibilité et vitesse. Le premier résultat cohérent est généralement le meilleur choix.

### 3d. Confirmer que le download est lancé

```bash
sleep 2 && screencapture -x -o "$SCRATCH/sk.png"
```
Une flèche verte doit apparaître sur la ligne cliquée. Dès qu'elle est visible → coche "Download" (3f) et passe au suivant. **Ne pas aller sur l'onglet Transfers pendant la boucle** — la vérification réelle se fait en fin de lot.

### 3e. Si SoulseekQt plante

```bash
pgrep -x SoulseekQt || open -a SoulseekQt
```
1. Coche "Pas trouvé" pour le morceau en cours
2. Relance l'app, attends qu'elle soit prête (screenshot de contrôle), recale les coordonnées si la fenêtre a bougé
3. Continue avec le morceau suivant

### 3f. Mettre à jour Airtable

`mcp__airtable__update_records` — **10 records maximum par appel**, donc regroupe ou envoie au fil de l'eau :

```json
{
  "baseId": "appNRzvkpeNfDaHCV",
  "tableId": "tbl9N0v65ab5GuI6R",
  "records": [
    { "id": "<record_id>", "fields": { "Download": true } }
  ]
}
```

Pour un introuvable : `{ "fields": { "Pas trouvé": true } }`.

> Marquer **dès que le download est lancé**, pas après la fin. SoulseekQt gère la file d'attente tout seul.

### 3g. Ne PAS fermer les onglets — travailler par sous-lots de 8

Chaque recherche empile un onglet sous le champ de saisie. **Ne cherche pas à les fermer un par un : ça ne marche pas.** Les croix ⊗ se recalent après chaque fermeture, donc au-delà du premier clic les suivants ratent, et un clic raté fait partir la frappe suivante dans la liste de résultats (morceau sauté sans erreur visible).

À la place : **le lot de 50 se traite en sous-lots de 8 morceaux.** Au 8e (l'app plante vers 8-9 onglets, constaté), on redémarre proprement :

```bash
# fin de sous-lot : laisser les transferts en file se terminer AVANT de tuer l'app
sleep 120
pkill -x SoulseekQt; sleep 3; open -a SoulseekQt; sleep 14
```

> **Le redémarrage tue les téléchargements encore en file d'attente.** C'est la première cause de morceaux « lancés mais jamais arrivés ». D'où l'attente de 2 minutes avant chaque redémarrage : elle laisse partir ce qui est en cours. Ne jamais redémarrer juste après un double-clic.

Après redémarrage : la fenêtre revient à sa position par défaut (194,82) et l'app affiche "Away" pendant ~10 s — les recherches marchent quand même. Recale les coordonnées avec un screenshot avant de reprendre.

### 3h. Le clic dans le champ de recherche rate une fois sur dix

Symptôme : le screenshot montre **la liste entière surlignée en orange** et l'onglet précédent toujours actif. Le clic n'a pas donné le focus au champ, donc `Cmd+A` a sélectionné la liste et la frappe est partie dans le vide.

Parade systématique : **cliquer deux fois dans le champ, espacés de 2 secondes** (deux clics simples, pas un double-clic) :

```bash
cliclick c:845,238; sleep 2; cliclick c:845,238; sleep 1
```

Si le symptôme apparaît quand même, refais la saisie du morceau au lieu de continuer — sinon il est compté comme traité alors qu'il ne l'a pas été.

---

## Étape 4 — Vérification de fin de lot

```bash
ls -1 ~/Soulseek\ Downloads/complete
find ~/Soulseek\ Downloads/complete -type f \( -iname '*.mp3' -o -iname '*.flac' -o -iname '*.wav' -o -iname '*.m4a' \) | sed 's|.*/||'
```

1. Pour chaque morceau coché "Download" à l'étape 3f, cherche un fichier correspondant par correspondance approximative (artiste + mots-clés du titre, en ignorant ponctuation/casse/featuring)
2. Trouvé → reste coché
3. Pas trouvé → **décoche "Download"** (`{ "Download": false }`) pour qu'il repasse au lot suivant

> Le matching étant approximatif, mieux vaut un faux négatif (retenté au lot suivant, sans conséquence) qu'un faux positif.

---

## Étape 4 bis — Second passage sur les introuvables (sans le filtre 320)

La majorité des « Pas trouvé » ne sont pas absents de Soulseek : leurs résultats remontent en **dossiers sans aucun fichier qui passe le filtre par défaut** `mp3 iscbr mbr:320`. Ça touche surtout les sorties récentes (2024-2025) et les remixes précis (Radio Edit, Bassflow, versions club).

Avant de clore le lot, reprends la liste des morceaux marqués "Pas trouvé" **pendant ce lot** et rejoue-les avec le filtre retiré :

1. Décoche **Default Filter** (case en bas à droite de la fenêtre, vers `1636,772`) ou vide le champ de filtre via le bouton **Clear** (`1505,772`)
2. Relance chaque requête introuvable, une par une, même boucle qu'à l'étape 3
3. Cette fois, contrôle le débit dans la colonne **Attributes** : accepte 320kbps VBR et 256kbps, **refuse en dessous de 192kbps** et signale-le à Nico
4. Un morceau récupéré : décoche "Pas trouvé" et coche "Download"
5. **Remets le Default Filter** avant de terminer, sinon le prochain lot part sans filtre de qualité

> Sur le premier vrai lot de 50, 10 morceaux ont été marqués introuvables pour cette seule raison — c'est le plus gros gisement de récupération du skill.

---

## Étape 5 — Résumé du lot

```
✅ 22 morceaux confirmés téléchargés (dossier complete)
🔄 5 lancés mais pas encore arrivés — Download redécoché, seront retentés au prochain lot
❌ 3 introuvables sur Soulseek :
   - Oussema Saffar Midnight Strings - Original Mix
   - Théo Coni José
⚠️ X morceaux restants dans la table Tracks — dis-moi si j'enchaîne sur le lot suivant
```

Les morceaux "Pas trouvé" ne seront plus proposés automatiquement ; Nico les reprendra en décochant la case quand il veut.

---

## Étape 6 — Nettoyage du dossier complete

Le skill `/clean-music` n'existe pas sur cette machine. Le nettoyage se fait avec le script livré avec ce skill :

```bash
bash ~/.claude/skills/zik-dl/clean.sh ~/Soulseek\ Downloads/complete
```

Il remonte les fichiers hors des sous-dossiers, supprime dossiers vides et `.DS_Store`, retire les préfixes numériques, et renomme en "Artiste - Titre.ext" à partir des tags ID3 (via `ffprobe`). Un `--dry-run` en 3e argument affiche ce qui serait fait sans rien modifier.

> À lancer systématiquement en fin de lot, **après** la vérification de l'étape 4 et le résumé de l'étape 5 — sinon les renommages cassent le matching de l'étape 4.

---

## Règles à respecter

- **Lots de 50**, découpés en **sous-lots de 8** avec redémarrage de SoulseekQt entre chaque (3g), et une **attente de 2 min avant chaque redémarrage** pour ne pas tuer les transferts en file.
- **Ne jamais retraiter un morceau déjà coché "Download" ou "Pas trouvé"** — le filtre de l'étape 1 s'en charge.
- **Requête = premier artiste + titre**, ponctuation retirée (3b). Jamais la liste complète des artistes.
- **Ne pas attendre la fin d'un téléchargement** avant de passer au suivant, ne pas checker Transfers pendant la boucle.
- **10 secondes max de recherche par morceau.**
- **Pas de qualité inférieure** : si aucun résultat en 320kbps, le signaler à Nico plutôt que de prendre du 128kbps.
- **Requêtes très populaires = risque de plantage** (trop de résultats d'un coup : "daft punk one more time" fait tomber l'app). Si l'app ne répond plus après une recherche, applique l'étape 3e sans insister.
- **Ne jamais tenter de fermer les onglets un par un** (3g) — deux clics dans le champ de recherche avant chaque frappe (3h).
- **Toujours faire le second passage sans filtre sur les introuvables** (étape 4 bis) avant de clore le lot.
- **Screenshot après chaque action clé** (search lancé, résultats apparus, double-clic) — ne jamais cliquer à l'aveugle.
- **Ne rien taper pendant que la fenêtre SoulseekQt n'a pas le focus** — un `activate` avant chaque série de frappes.

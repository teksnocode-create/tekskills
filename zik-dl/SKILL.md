---
name: zik-dl
description: >
  Automatise le téléchargement de morceaux depuis SoulseekQt en se basant sur la liste "Zik à Télécharger" d'Airtable (base SOREK). Pour chaque morceau pas encore dans la collection, cherche dans SoulseekQt sur le Mac mini-de-nico, double-clique sur le meilleur MP3 320kbps disponible, puis coche "Deja dans collection" dans Airtable dès que le download est lancé. Utiliser ce skill SYSTÉMATIQUEMENT dès que Nico tape "/zik-dl", "télécharge la zik", "lance le téléchargement", "download zik", "télécharge mes morceaux", "récupère mes morceaux", ou mentionne vouloir récupérer sa liste de morceaux Airtable via Soulseek.
---

# Zik Download — Airtable → SoulseekQt

## Ce que ce skill fait

1. Lit la liste des morceaux à télécharger depuis Airtable (vue déjà filtrée)
2. Pour chaque morceau : ouvre SoulseekQt sur mini-de-nico, cherche, télécharge le meilleur 320kbps
3. Coche "Deja dans collection" dans Airtable dès que le download est lancé
4. Retourne un résumé : X téléchargés, Y introuvables sur Soulseek

---

## Étape 1 — Récupérer la liste depuis Airtable

Appelle `mcp__Airtable__list_records_for_table` avec ces paramètres :
- `baseId` : `appNRzvkpeNfDaHCV`
- `tableIdOrName` : `tblI2P5qDSBK2MCqb6`
- `viewId` : `viwONWsOKGoWjVgIC`

La vue est déjà filtrée sur "Deja dans collection = Pas trouvé" — inutile d'ajouter un filtre supplémentaire.

Pour chaque record, retiens :
- `id` : l'identifiant Airtable du record (nécessaire pour la mise à jour)
- `fields.Name` : le nom du morceau à chercher dans Soulseek

Si la liste est vide → informer Nico ("Tout est déjà dans ta collection !") et s'arrêter là.

---

## Étape 2 — Accès à SoulseekQt sur mini-de-nico

**Une seule fois en début de session** (pas à chaque morceau) :

1. Appelle `computer_resolve_access` avec `device: "mini-de-nico"` et `apps: ["SoulseekQt"]`
2. Appelle `computer_request_access` avec exactement les `apps` retournées par l'étape précédente
3. Prends un screenshot (`computer_screenshot`) pour voir l'état actuel de l'écran
4. Si SoulseekQt n'est pas visible → appelle `computer_open_application` avec le nom résolu, puis re-screenshot

---

## Étape 3 — Boucle : chercher et télécharger chaque morceau

Traite les morceaux un par un. Pour chaque morceau :

### 3a. Aller sur l'onglet Search

Prends un screenshot. Si l'onglet "Search" de SoulseekQt n'est pas actif, clique dessus.

### 3b. Saisir la recherche

- Triple-clique dans le champ de recherche (pour tout sélectionner/effacer)
- Tape le `Name` du morceau tel quel depuis Airtable
- Appuie sur Entrée ou clique sur le bouton "Search"

### 3c. Attendre et analyser les résultats

Attends 6-8 secondes, puis prends un screenshot.

**Cas "aucun résultat"** : la liste de résultats est vide. Essaie une variante simplifiée :
- Retire les tirets (`-`) et les parenthèses du nom
- Garde juste artiste + titre principal (supprime les infos de mix/remix si le titre est long)
- Relance la recherche, attend à nouveau 6-8 sec

Si toujours aucun résultat → morceau introuvable. Passe au suivant sans mettre à jour Airtable. Ajoute-le à la liste des introuvables.

**Cas "résultats présents"** : le filtre par défaut de SoulseekQt (`mp3 iscbr mbr:320`) filtre déjà sur MP3 320kbps. Scroll en haut de la liste. Prends le **premier résultat** dont le nom de fichier correspond bien au morceau cherché. Double-clique dessus pour lancer le téléchargement.

> Pourquoi le premier ? Soulseek trie par disponibilité et vitesse. Le premier résultat cohérent est généralement le meilleur choix. Pas besoin de comparer tous les résultats un par un.

### 3d. Confirmer que le transfer est parti (rapide)

Après le double-clic, clique sur l'onglet "Transfers" et prends un screenshot. Le morceau doit apparaître avec le statut "Downloading" ou "Queued". Si c'est le cas → passe à l'étape suivante.

### 3e. Mettre à jour Airtable

Appelle `mcp__Airtable__update_records_for_table` :
```json
{
  "baseId": "appNRzvkpeNfDaHCV",
  "tableIdOrName": "tblI2P5qDSBK2MCqb6",
  "records": [
    {
      "id": "<record_id du morceau>",
      "fields": {
        "Deja dans collection": true
      }
    }
  ]
}
```

> Marquer dans Airtable **dès que le download est lancé**, pas après la fin. SoulseekQt gère la file d'attente en autonomie.

---

## Étape 4 — Résumé final

Affiche un récap clair :
```
✅ 8 morceaux lancés en téléchargement
❌ 3 introuvables sur Soulseek :
   - Oussema Saffar Midnight Strings - Original Mix
   - Théo Coni José
   - ...
```

Les morceaux introuvables restent dans Airtable (checkbox non cochée) pour que Nico puisse les retrouver manuellement.

---

## Règles à respecter

- **Ne pas attendre la fin du téléchargement** avant de passer au morceau suivant — SoulseekQt gère la file tout seul.
- **Pas de fichiers qualité inférieure** : si les seuls résultats disponibles ne sont pas en 320kbps, signale-le à Nico plutôt que de télécharger du 128kbps.
- **En cas de problème avec SoulseekQt** (app fermée, fenêtre introuvable, erreur réseau) : signaler le problème et arrêter proprement en indiquant où on en était.
- **Rythme** : prendre un screenshot après chaque action clé (search lancé, résultats apparus, double-clic, transfer confirmé) — ne pas cliquer à l'aveugle.

---

## Ce qui a été testé sur le Mac mini-de-nico le 2026-08-18

Test mené depuis Claude Code (terminal), pas depuis Claude Desktop. Résultats mesurés, pas supposés.

### Les outils `computer_*` n'existent pas dans Claude Code
`computer_resolve_access`, `computer_screenshot`, `computer_open_application` sont propres à Claude Desktop. Les étapes 2 et 3 ci-dessus ne tournent pas dans un terminal. L'équivalent y est AppleScript via `osascript`, plus `screencapture` et `cliclick`.

### SoulseekQt n'a aucun dictionnaire AppleScript
Aucun `.sdef`, aucune clé de scripting dans son `Info.plist`. Le pilotage propre par commandes est exclu. Seule reste l'accessibilité (System Events), qui exige d'accorder l'Accessibilité au Terminal dans Réglages Système, et de **relancer le Terminal après** : un processus démarré avant l'autorisation ne l'obtient pas.

### Ce qui marche par accessibilité
Chemin de la fenêtre : `UI element 1 of window 1` contient deux groupes, le panneau de recherche et la barre Manual Searches.

- **Onglets nommés et cliquables** : Transfers, Rooms, Chat, Search, Users, Browse, Options. Plus besoin de cliquer à des coordonnées.
- **Compteur de transferts lisible** dans le titre de l'onglet, sous la forme `Transfers [0/0]`. Il confirme qu'un téléchargement est parti sans prendre de capture d'écran.
- **Champ de recherche** : `UI element 2 of UI element 1 of UI element 1 of UI element 1 of window 1`. On y écrit avec `set value`.
- **Bouton Search** : `UI element 2` du panneau.
- **Colonnes de résultats nommées** : User, Free, K/s, Folder, File, Size, Attributes.

### Ce qui ne marche pas, et qui bloque l'automatisation complète
**Les lignes de résultats ne sont pas exposées.** Vérifié le 18/08 : recherche « Bicep Glue » lancée, résultats bien visibles à l'écran, et `count of rows` retourne 0. Qt dessine la table sans la publier à l'accessibilité.

Conséquence directe : choisir le bon MP3 320kbps ne peut se faire qu'en analysant une capture d'écran, puis en cliquant à des coordonnées. C'est la partie fragile, et elle le restera.

### Piège du champ de recherche
`set value` ne remplace pas toujours le contenu précédent, il se mélange avec. Vécu le 18/08 : « Bicep Glue » est parti en « Bicep Gluet me n ». **Toujours vider le champ (`set value of tf to ""`), attendre, écrire, puis relire la valeur et vérifier qu'elle est exacte avant de cliquer sur Search.**

### Bug connu, signalé par Nico
Sur les morceaux qui retournent trop de fichiers, SoulseekQt bugue et s'arrête. Parade à appliquer : ne jamais lancer une recherche trop large, et préférer des termes précis (artiste + titre) plutôt qu'un seul mot.

### La vraie solution à étudier avant d'aller plus loin
`slskd`, un client Soulseek qui expose une **API REST**. Il supprime tout le pilotage d'interface : recherche, sélection et téléchargement deviennent des appels HTTP, donc scriptables depuis n8n comme n'importe quelle intégration. À évaluer avant d'investir davantage dans l'automatisation de la fenêtre.

### Dépendance non satisfaite
Le MCP Airtable (`mcp__Airtable__*`) n'est pas connecté à Claude Code. Il fournit la liste des morceaux et coche « Deja dans collection ». Sans lui, l'étape 1 et l'étape 3e ne tournent pas.

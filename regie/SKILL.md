---
name: regie
description: Prépare la régie musicale d'un événement (mariage, soirée) pour Nico. À partir d'un CSV de playlist, croise les morceaux avec la collection audio du disque SWIT, crée le dossier de l'événement dans "++ MARIAGE " avec un sous-dossier Serato contenant les fichiers trouvés, et pousse les morceaux manquants dans Airtable. Ne touche JAMAIS à la bibliothèque Serato. TOUJOURS déclencher dès que l'utilisateur tape "/regie", "regie", "régie", "prépare la régie", "playlist mariage", "nouvelle playlist événement", ou fournit un CSV de morceaux pour un événement.
---

# Régie — préparation musicale d'un événement

Chaîne complète : CSV de playlist → dossier de l'événement sur le disque → morceaux manquants dans Airtable.

## Règle d'or

**Un morceau va d'un côté OU de l'autre, jamais les deux.**

| Situation | Destination |
|---|---|
| Présent dans la collection | Dossier de l'événement uniquement |
| Absent de la collection | Airtable uniquement |
| Correspondance incertaine | **Ni l'un ni l'autre** tant que Nico n'a pas tranché |

Ne jamais ajouter dans Airtable un morceau que Nico possède déjà. C'est le point sur lequel il a explicitement insisté.

## Interdiction Serato

**Ce skill ne lit ni n'écrit rien dans `_Serato_`.** Pas de crate, pas de `database V2`, pas de `location.sqlite`, pas de sauvegarde de bibliothèque. Le disque est vu comme un simple arbre de fichiers audio.

Décidé le 2026-08-21 : la manipulation de la bibliothèque Serato est le seul endroit du skill qui pouvait casser la collection, pour un gain nul par rapport à un dossier de fichiers que Nico glisse lui-même dans Serato.

L'ancienne implémentation (`serato_lib.py`, `serato-format.md`) est conservée dans `_archive/` pour l'historique. **Ne pas la réutiliser.**

Conséquence à assumer : sans les tags de la base Serato, le matching repose sur les noms de fichiers, qui sont irréguliers. Le taux d'incertains est plus élevé qu'avant, et c'est voulu — un incertain se tranche en 5 secondes, un mauvais morceau en soirée ne se rattrape pas.

---

## Deux contextes d'exécution

Le skill tourne indifféremment depuis l'app Claude (desktop/mobile) ou depuis Claude Code en terminal. **Seule la façon d'atteindre le disque change** — la logique, l'ordre des étapes, les garde-fous et la règle d'or sont identiques.

| | App Claude | Claude Code (terminal) |
|---|---|---|
| Accès disque | outils `device_*`, le disque est distant | accès direct au système de fichiers |
| Racine du disque | `$HOME/mnt/SWIT` | `/Volumes/SWIT` |
| Lire un fichier | `device_stage_files` | `Read` / `Bash` |
| Écrire un fichier | `SendUserFile` → `device_commit_files` | `Write` / `Bash` |
| Lancer le script | non | `python3`, `scripts/collection.py` importable |

**Déterminer le contexte au démarrage :** si les outils `device_*` sont disponibles, on est dans l'app. Sinon, on est en Claude Code — vérifier `/Volumes/SWIT` avec `ls`.

En App Claude, la copie de 150 fichiers audio est lente et peu fiable. **Privilégier Claude Code pour l'étape 4** ; si Nico est sur mobile, faire les étapes 0 à 3 et 5, puis lui livrer la liste des fichiers à copier et lui dire de relancer le skill sur le poste fixe.

---

## Étape 0 — Le nom de l'événement (BLOQUANT)

**Ne rien faire avant d'avoir le nom exact de l'événement.** C'est la première question, systématiquement, même si Nico a déjà fourni le CSV dans le même message.

> « Quel est le nom exact de l'événement ? »

**Convention en place sur le disque : `AAAA Prénom & Prénom`.** Exemples réels : `2026 Manon & Guillaume`, `2026 Laura & Fabio`, `2026 Mathieu & Cassandre`. Proposer ce format à Nico, et reprendre **exactement** ce qu'il valide, sans reformater, sans corriger la casse, sans réordonner.

Ce nom devient la référence unique, réutilisée telle quelle :

- nom du dossier de l'événement
- champ `Event` dans Airtable
- nom des fichiers de travail et du récapitulatif

Le relire à Nico pour confirmation avant de continuer. Une faute ici se propage partout et casse la traçabilité.

---

## Étape 1 — Vérifier l'accès au disque

La collection est sur le disque externe **SWIT**.

```
/Volumes/SWIT/++ ZIK  Collection/              <- les fichiers audio (attention: DEUX espaces après "ZIK")
/Volumes/SWIT/++ ZIK  Collection/++ MARIAGE /  <- un dossier par événement (attention: espace FINAL)
```

**[App Claude]** Si le dossier n'est pas connecté, utiliser `device_request_folder_access` sur `/Volumes/SWIT`. S'il est introuvable, le disque n'est pas branché — s'arrêter et le demander.

**[Claude Code]** Vérifier directement :

```bash
ls -d "/Volumes/SWIT/++ ZIK  Collection" "/Volumes/SWIT/++ ZIK  Collection/++ MARIAGE "
```

Si ça échoue, le disque n'est pas branché — s'arrêter et le demander. Vérifier aussi qu'il n'est pas monté en double (`ls -d /Volumes/SWIT*` : la présence de `SWIT 1` est un problème, voir Pièges connus).

**Serato peut rester ouvert.** On n'écrit rien dans sa bibliothèque, et les fichiers copiés vont dans un dossier qu'il ne surveille pas.

---

## Étape 2 — Indexer la collection

```python
import sys; sys.path.insert(0, "scripts")
import collection as c

index = c.index_collection(exclure=c.dossier_evenement(nom_evenement))
```

**Les dossiers des événements passés font partie de l'index**, marqués `source="evenement"`. Mesure du 2026-08-21 sur le disque de Nico : **937 morceaux qu'il possède n'existent QUE dans ces dossiers**, absents de la collection principale. Les exclure les renverrait en manquants dans Airtable et il les retéléchargerait pour rien, en violation directe de la règle d'or.

Seul le dossier de **l'événement en cours** est exclu, sinon une copie déjà faite se proposerait comme sa propre source.

Un même nom de fichier présent dans plusieurs dossiers est dédoublonné, et la collection principale l'emporte toujours sur une copie d'événement.

Ordre de grandeur au moment de l'écriture du skill, à titre de repère : environ 8 200 fichiers uniques, dont 7 200 dans la collection et 1 000 dans les dossiers d'événements, 11 événements déjà traités. L'index prend une dizaine de secondes.

### Les fichiers `._`

macOS dépose à côté de chaque morceau un fichier de métadonnées portant le **même nom et la même extension**, préfixé `._`. Il y en a 4 072 sur le disque. `index_collection()` les filtre. Sans ce filtre, l'index compte presque le double de ce qu'il contient vraiment et des fichiers non lisibles finissent copiés.

---

## Étape 3 — Croiser le CSV avec la collection

Le CSV vient d'un export de playlist Spotify. Format variable — `read_playlist()` cherche les colonnes artiste et titre quel que soit leur intitulé.

```python
lignes = c.read_playlist("playlist.csv")
res    = c.match_all(lignes, index)
```

### Le matching est tolérant, mais prudent

Les noms de fichiers sont irréguliers. Cas réels observés :

- artiste absent du nom : `01 - One More Time.mp3`
- séparateurs exotiques : `SURVIVOR : Eye Of The Tiger`
- casse incohérente : `robot rock` / `Robot Rock`
- préfixes de piste : `02 - Aerodynamic.mp3`, `114 - I Want The Eye Of The Tiger.mp3`
- remix déguisé sans le mot remix : `Matroda x Daft Punk - One More Time.mp3`

`normalise()` gère minuscules, accents, ponctuation et préfixes numériques des deux côtés.

### Trois catégories de sortie

- **Trouvé** — un seul fichier, tous les mots du titre présents, l'artiste présent, aucune mention de version
- **Manquant** — aucune correspondance plausible
- **Incertain** — tout le reste : plusieurs candidats, artiste absent du nom, ou mention de version

Un titre est **incertain**, jamais classé d'office, quand le fichier porte une mention absente du CSV : `Live`, `Remix`, `Edit`, `Radio Edit`, `Extended`, `Instrumental`, `Acoustic`, `Cover`, `Karaoke`, ou les marqueurs isolés `x`, `vs`, `bootleg`, `rework`, `flip`, `dj`.

Exemple : le CSV demande `Bamboléo – Gipsy Kings`, la collection contient `Gipsy Kings - Bamboleo (Live 1990).mp3`. → **incertain**. Mettre une version live dans une playlist de mariage est une erreur coûteuse.

### Soumettre les incertains AVANT d'écrire

Présenter la liste à Nico sous forme de tableau : ce que demande le CSV, ce qui a été trouvé, ce qui diffère. Attendre son arbitrage. **Aucune copie disque ou insertion Airtable avant sa réponse.**

Compter 25 à 40 % de cas ambigus sur un CSV de mariage typique, la plupart réglés d'un coup d'œil.

Un incertain tranché « oui » rejoint les trouvés, un incertain tranché « non » rejoint les manquants. Aucun ne reste en suspens.

---

## Étape 4 — Créer le dossier et copier les fichiers

### Ce qui est créé

```
/Volumes/SWIT/++ ZIK  Collection/++ MARIAGE /<NOM EVENEMENT>/
└── Serato/          <- les fichiers audio trouvés, copiés depuis la collection
```

Le sous-dossier s'appelle `Serato` par convention (c'est ce que Nico glisse ensuite dans Serato à la main). Les dossiers `Regie/` et `News/` que Nico crée parfois à côté ne sont **pas** du ressort du skill : ne pas les créer, ne pas y toucher.

### Copie, jamais déplacement

Les fichiers sont **copiés**, la collection d'origine n'est jamais modifiée ni allégée. `shutil.copy2` conserve les dates.

```python
plan = c.copier(res["trouves"], nom_evenement, dry_run=True)   # verifier d'abord
print(len(plan["copies"]), "a copier,", len(plan["deja_la"]), "deja presents")

plan = c.copier(res["trouves"], nom_evenement)                 # puis executer
```

### Garde-fous

1. **Toujours passer par `dry_run=True` d'abord** et annoncer le nombre de fichiers à Nico avant de copier pour de bon.
2. **Si le dossier de l'événement existe déjà**, s'arrêter et demander. Un dossier existant veut dire que la régie a déjà été préparée, ou que le nom est celui d'un autre événement.
3. **Un fichier déjà présent dans `Serato/` n'est jamais écrasé** — il est compté dans `deja_la` et signalé.
4. Vérifier la place libre avant de lancer : environ 10 Mo par morceau, donc ~1,5 Go pour 150 titres.

### Vérification obligatoire

Après copie, recompter **depuis le disque** :

```bash
ls "/Volumes/SWIT/++ ZIK  Collection/++ MARIAGE /<NOM EVENEMENT>/Serato" | wc -l
```

Le compte doit égaler `trouvés` (incertains validés inclus). Un écart veut dire que deux morceaux différents portaient le même nom de fichier : les identifier et les renommer, ne pas laisser passer.

---

## Étape 5 — Pousser les manquants dans Airtable

Base **SOREK** — `appNRzvkpeNfDaHCV`
Table **💿 Tracks** — `tbl9N0v65ab5GuI6R`

| Champ | Contenu |
|---|---|
| `Artistes` | artiste du CSV |
| `Morceaux` | titre du CSV |
| `Event` | nom exact de l'événement (Étape 0) |
| `Download` | laisser décoché — c'est la file d'attente de Nico |
| `Commentaires` | facultatif : précision utile (version demandée, remix attendu) |

**Uniquement les manquants.** Vérifier avant l'insertion qu'aucun morceau trouvé ne s'est glissé dans le lot.

Avant d'insérer, chercher les doublons : un morceau déjà présent dans la table pour un autre événement n'a pas besoin d'être recréé — signaler à Nico plutôt que dupliquer.

Une fois les morceaux téléchargés (skill `zik-dl`), relancer le skill sur le même CSV rattrape ce qui manquait : les nouveaux fichiers sont dans la collection, donc reclassés en trouvés et copiés à leur tour.

---

## Étape 6 — Récapitulatif

Livrer un résumé court :

- nom de l'événement
- nombre de morceaux du CSV
- trouvés → copiés (avec le chemin du dossier créé et le compte vérifié sur disque)
- manquants → Airtable (nombre de lignes créées)
- incertains arbitrés, et dans quel sens
- fichiers déjà présents non recopiés, s'il y en a

---

## Pièges connus

**Ne pas exclure le dossier des mariages de l'index.** L'erreur a été commise le 2026-08-21 et rattrapée avant tout usage : 937 morceaux ne vivent que là, et les ignorer revenait à les redemander en téléchargement alors que Nico les a déjà. Seul le dossier de l'événement en cours s'exclut.

**Ce que le scan ne voit pas.** Environ 590 morceaux de la base Serato n'ont plus de fichier correspondant sur le disque, dont ~230 qui ont réellement disparu (déplacés ou supprimés hors de Serato). Ils sortiront en manquants. Si Nico affirme posséder un titre classé manquant, c'est la première piste : le fichier a bougé et la base Serato n'a jamais été mise à jour.

**Deux espaces après « ZIK », un espace final après « MARIAGE ».** Les deux chemins sont piégeux et une faute de frappe crée silencieusement un dossier parallèle. Toujours reprendre les constantes de `scripts/collection.py`, jamais les retaper.

**Artiste absent du nom de fichier.** C'est le cas le plus fréquent de la collection et la principale source d'incertains. Ne jamais l'automatiser en « trouvé » sous prétexte que le titre suffit : `Flowers` existe en 4 versions dans la collection.

**Morceaux en `?` dans Serato, playlists vides** — sans rapport avec ce skill, mais ça arrive à Nico. Vérifier que le disque SWIT n'est pas **monté en double** sur le Mac (`SWIT` et `SWIT 1` dans le Finder), ce qui arrive après une éjection brutale. Éjecter, débrancher, rebrancher. Vérifier aussi qu'aucun texte ne traîne dans la barre de recherche de Serato, qui filtre toutes les crates à zéro résultat.

# Format des fichiers Serato — notes techniques

Observations faites directement sur le disque SWIT de Nico. Format propriétaire non documenté officiellement : ces notes viennent de l'analyse des fichiers réels, pas d'une spécification.

## Les trois endroits où un chemin est stocké

Un même morceau voit son chemin écrit **en toutes lettres** à plusieurs endroits :

| Fichier | Rôle | Champ |
|---|---|---|
| `_Serato_/database V2` | bibliothèque héritée, une entrée par morceau | `pfil` |
| `_Serato_/Subcrates/*.crate` | une occurrence par crate contenant le morceau | `ptrk` |
| `_Serato_/Library/location.sqlite` | bibliothèque moderne (SQLite) | `asset.portable_id` |

Conséquence : renommer ou déplacer un fichier oblige à patcher **toutes** ces occurrences. Un morceau appartient en moyenne à 2 crates, jusqu'à 7.

`location.sqlite` est la base moderne (migration Serato de février 2026, l'ancienne étant archivée dans `DBV2-legacy.zip`). `dbv2_status.autosync_disabled = 0` : Serato synchronise dans les deux sens entre SQLite et les fichiers `.crate` au lancement et à la fermeture. Déposer un fichier `.crate` valide suffit donc à le faire apparaître — Serato l'importe tout seul.

## RÈGLE ABSOLUE : ne jamais fabriquer un chemin

Serato n'écrit pas les chemins tels qu'ils apparaissent dans un listing de fichiers. Certains caractères sont encodés dans la zone Unicode privée (Private Use Area, `U+E000`–`U+F8FF`).

Correspondances constatées sur ce disque (les caractères de la colonne de droite sont des points de code PUA, non reproductibles en texte brut — les lire directement dans `database V2`) :

| Vu dans un listing | Stocké par Serato |
|---|---|
| `**** ALBUM ELECTRO` | `<PUA> ALBUM ELECTRO` |
| `++ MARIAGE ` (espace final) | `++ MARIAGE<PUA>` |

Ces caractères sont illégaux dans les noms de fichiers Windows ; l'encodage assure la portabilité entre systèmes. Le mécanisme exact de la table de conversion n'a pas été établi — **ne pas chercher à la reconstituer**.

**La seule méthode fiable :** prendre le chemin déjà présent dans `database V2` et le recopier octet pour octet. Ne jamais le dériver d'un `ls`, ni le retaper, ni le normaliser.

Plus de 2 000 fichiers de la collection sont concernés (tout `ALBUM ELECTRO`, tout `MARIAGE`). Un chemin reconstruit à la main ne provoque **aucune erreur** : le morceau disparaît simplement, silencieusement.

Contrôle systématique avant écriture : tout chemin destiné à une nouvelle crate doit exister **à l'identique** dans l'ensemble des `pfil` de `database V2`. Sinon, ne pas écrire.

## Structure d'un fichier .crate

Suite de blocs, sans en-tête global :

```
[tag 4 octets ASCII][longueur 4 octets big-endian][contenu]
```

Le texte est en **UTF-16 big-endian**, sans BOM.

Ordre observé :

```
vrsn  "1.0/Serato ScratchLive Crate"      (56 octets de contenu)
osrt  -> tvcn "key" + brev 0x00           (colonne de tri)
ovct  -> tvcn "song"      + tvcw "349"    (colonnes affichées et largeurs)
ovct  -> tvcn "artist"    + tvcw "197"
ovct  -> tvcn "bpm"       + tvcw "0"
ovct  -> tvcn "key"       + tvcw "0"
ovct  -> tvcn "comment"   + tvcw "111"
ovct  -> tvcn "length"    + tvcw "110"
ovct  -> tvcn "playCount" + tvcw "0"
ovct  -> tvcn "album"     + tvcw "0"
ovct  -> tvcn "genre"     + tvcw "0"
otrk  -> ptrk "<chemin>"                  (un bloc par morceau, ordre = ordre d'affichage)
```

Cet en-tête fait exactement **441 octets** avant le premier `otrk`. Le comparer à celui d'une crate existante est un bon test de validité.

Les chemins dans `ptrk` sont **relatifs à la racine du volume**, sans slash initial :

```
++ ZIK  Collection/++ CLUB ELECTRO DANCE/HOUSE CLASSICS/Daft Punk - Around The World.mp3
```

(noter les deux espaces dans `++ ZIK  Collection`)

## Hiérarchie des crates

Encodée dans le **nom du fichier**, avec `%%` comme séparateur :

```
TOUS.crate                                        -> TOUS
TOUS%%#CLUB.crate                                 -> TOUS > #CLUB
TOUS%%#CLUB%%++ MARIAGE .crate                    -> TOUS > #CLUB > ++ MARIAGE
TOUS%%#CLUB%%++ MARIAGE %%2026 KARLA.crate        -> ... > 2026 KARLA
```

Un fichier sans `%%` apparaît à la racine de la liste.

Certains noms de crate contiennent des séquences d'échappement pour les caractères interdits dans un nom de fichier, par exemple `Party%%14<esc>2f02<esc>2f26.crate` pour une crate `14/02/26` (`2f` = `/`). Comme pour les chemins : copier un motif existant plutôt que d'en fabriquer un.

## Ce qui est stocké dans le fichier audio lui-même

BPM, tonalité, hotcues, boucles, waveform et gain sont écrits dans des tags ID3 propriétaires (`Serato Markers2`, `Serato Analysis`, `Serato BeatGrid`) **à l'intérieur du mp3**.

Conséquence utile : renommer ou déplacer un fichier ne perd **jamais** ces données. Seul le pointeur de chemin casse. Un fichier réintégré manuellement dans une crate retrouve ses cues intacts.

## Fichiers annexes

| Fichier | Rôle |
|---|---|
| `neworder.pref` | ordre d'affichage des crates dans le panneau de gauche |
| `collapsed.pref` | état plié/déplié de l'arborescence |
| `_Serato_Backup/` | sauvegarde automatique de Serato — ne pas confondre avec les sauvegardes manuelles |
| `Library/location.sqlite` | base moderne : tables `asset`, `container`, `container_asset`, `space_asset` |

Relations dans `location.sqlite` : `container_asset.space_asset_id` → `space_asset.id`, puis `space_asset.asset_id` → `asset.id`. Il n'y a **pas** de colonne `asset_id` directement dans `container_asset`.

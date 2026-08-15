---
name: regie
description: Prépare la régie musicale d'un événement (mariage, soirée) pour Nico. À partir d'un CSV de playlist, croise les morceaux avec la collection Serato sur le disque SWIT, crée la crate Serato correspondante, et pousse les morceaux manquants dans Airtable. TOUJOURS déclencher dès que l'utilisateur tape "/regie", "regie", "régie", "prépare la régie", "playlist mariage", "nouvelle playlist événement", ou fournit un CSV de morceaux pour un événement.
---

# Régie — préparation musicale d'un événement

Chaîne complète : CSV de playlist → crate Serato sur le disque → morceaux manquants dans Airtable.

## Règle d'or

**Un morceau va d'un côté OU de l'autre, jamais les deux.**

| Situation | Destination |
|---|---|
| Présent dans la collection | Crate Serato uniquement |
| Absent de la collection | Airtable uniquement |
| Correspondance incertaine | **Ni l'un ni l'autre** tant que Nico n'a pas tranché |

Ne jamais ajouter dans Airtable un morceau que Nico possède déjà. C'est le point sur lequel il a explicitement insisté.

---

## Étape 0 — Le nom de l'événement (BLOQUANT)

**Ne rien faire avant d'avoir le nom exact de l'événement.** C'est la première question, systématiquement, même si Nico a déjà fourni le CSV dans le même message.

> « Quel est le nom exact de l'événement ? »

Format libre — reprendre **exactement** ce que Nico écrit, sans reformater, sans corriger la casse, sans réordonner. Exemple : `2026 - MANON & Guillaume`.

Ce nom devient la référence unique, réutilisée telle quelle :

- nom de la crate Serato
- champ `Event` dans Airtable
- nom des fichiers de travail et du récapitulatif

Le relire à Nico pour confirmation avant de continuer. Une faute ici se propage partout et casse la traçabilité.

---

## Étape 1 — Vérifier l'accès au disque

La collection est sur le disque externe **SWIT**.

```
/Volumes/SWIT/++ ZIK  Collection/     <- les fichiers audio (attention: DEUX espaces après "ZIK")
/Volumes/SWIT/_Serato_/               <- la bibliothèque Serato
```

Si le dossier n'est pas connecté, utiliser `device_request_folder_access` sur `/Volumes/SWIT`. S'il est introuvable, le disque n'est pas branché — s'arrêter et le demander.

**Vérifier aussi que Serato est fermé** (voir Étape 4). On peut lire avec Serato ouvert, jamais écrire.

---

## Étape 2 — Lire la collection

Récupérer la bibliothèque avec `device_stage_files` :

```
/Volumes/SWIT/_Serato_/database V2
/Volumes/SWIT/_Serato_/Library/location.sqlite
```

Puis utiliser `scripts/serato_lib.py` (voir `references/serato-format.md` pour le détail du format).

Ordres de grandeur au moment de l'écriture du skill, à titre de repère : environ 9 500 morceaux, 80 crates, 10 000 fichiers audio.

---

## Étape 3 — Croiser le CSV avec la collection

Le CSV vient d'un export de playlist Spotify. Format variable — s'adapter aux colonnes présentes, chercher artiste et titre quel que soit leur intitulé.

### Le matching doit être tolérant

Les tags de la collection sont irréguliers. Cas réels observés :

- champ artiste vide, tout dans le titre : `toto - Eye of the tiger`
- séparateurs exotiques : `SURVIVOR : Eye Of The Tiger`
- casse incohérente : `robot rock` / `Robot Rock`
- préfixes de piste : `02 - Aerodynamic.mp3`, `114 - I Want The Eye Of The Tiger.mp3`

Normaliser des deux côtés avant comparaison : minuscules, accents supprimés, ponctuation supprimée, préfixes numériques retirés, et **toujours tester aussi la concaténation `artiste + titre`** contre le titre seul, à cause des champs artiste vides.

### Trois catégories de sortie

- **Trouvé** — correspondance nette sur artiste + titre normalisés
- **Manquant** — aucune correspondance plausible
- **Incertain** — correspondance partielle, ou version différente

Un titre est **incertain**, jamais classé d'office, quand le fichier trouvé porte une mention absente du CSV : `Live`, `Remix`, `Edit`, `Radio Edit`, `Extended`, `Instrumental`, `Acoustic`, `Cover`, `Karaoke`, ou une année/version différente.

Exemple : le CSV demande `Bamboléo – Gipsy Kings`, la collection contient `Gipsy Kings - Bamboleo (Live 1990).mp3`. → **incertain**. Mettre une version live dans une playlist de mariage est une erreur coûteuse.

### Soumettre les incertains AVANT d'écrire

Présenter la liste à Nico sous forme de tableau : ce que demande le CSV, ce qui a été trouvé, ce qui diffère. Attendre son arbitrage. **Aucune écriture disque ou Airtable avant sa réponse.**

Compter environ 10 à 20 % de cas ambigus sur un CSV de mariage typique.

---

## Étape 4 — Créer la crate Serato

### Préalables non négociables

1. **Serato doit être complètement fermé.** Il garde sa bibliothèque en mémoire et réécrit ses fichiers en quittant : il écraserait la crate, ou la supprimerait. Demander confirmation explicite à Nico, ne jamais le supposer.
2. **Sauvegarder `_Serato_` avant toute écriture.** Environ 52 Mo, quelques secondes :

```bash
cp -R "$HOME/mnt/SWIT/_Serato_" "$HOME/mnt/SWIT/SAUVEGARDE_Serato_AAAAMMJJ"
```

Nommer la sauvegarde **`SAUVEGARDE_Serato_...`** et surtout **pas** `_Serato_...` : Serato repère ses bibliothèques en cherchant les dossiers commençant par `_Serato_` à la racine des volumes, et un dossier mal nommé introduit une ambiguïté.

### Emplacement de la crate

Les crates de mariage sont rangées sous `TOUS > #CLUB > ++ MARIAGE `. La hiérarchie est encodée dans le **nom du fichier**, avec `%%` comme séparateur de niveau :

```
_Serato_/Subcrates/TOUS%%#CLUB%%++ MARIAGE %%<NOM EVENEMENT>.crate
```

Attention : `++ MARIAGE ` porte un **espace final** dans la hiérarchie. Reprendre le motif exact d'une crate existante plutôt que de le retaper — lister `Subcrates/` et copier le préfixe d'un mariage déjà en place.

### Écriture

Générer le fichier avec `scripts/serato_lib.py`, puis le déposer via `SendUserFile` → `device_commit_files`.

**La règle absolue du format est dans `references/serato-format.md` — la lire avant d'écrire.** En résumé : ne jamais fabriquer un chemin à partir d'un listing disque, toujours réutiliser tel quel le chemin déjà présent dans `database V2`. Serato encode certains caractères dans une zone Unicode privée, et un chemin reconstruit à la main casse silencieusement.

### Vérification obligatoire

Après écriture, relire le fichier depuis le disque et confirmer :

- le nombre de morceaux correspond
- les chemins sont **tous** présents à l'identique dans `database V2`
- l'en-tête fait 441 octets, identique à celui d'une crate existante

Puis demander à Nico de relancer Serato et de confirmer que les morceaux s'affichent — pas de points d'interrogation, BPM et clés présents.

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

---

## Étape 6 — Récapitulatif

Livrer un résumé court :

- nom de l'événement
- nombre de morceaux du CSV
- trouvés → crate (avec le chemin du fichier créé)
- manquants → Airtable (nombre de lignes créées)
- incertains arbitrés, et dans quel sens
- emplacement de la sauvegarde

---

## Pièges connus

**Serato ouvert pendant l'écriture** — cause d'échec la plus fréquente. Il réécrit `database V2`, `neworder.pref` et les `.crate` en quittant.

**Chemins reconstruits à la main** — casse silencieusement les morceaux des dossiers contenant des caractères spéciaux (`**** ALBUM ELECTRO`, `++ MARIAGE `). Plus de 2 000 fichiers concernés dans la collection. Toujours réutiliser les chemins bruts de `database V2`.

**Morceaux en `?` dans Serato, playlists vides** — ce n'est pas une perte de données. Vérifier d'abord que le disque SWIT n'est pas **monté en double** sur le Mac (`SWIT` et `SWIT 1` dans le Finder), ce qui arrive après une éjection brutale : Serato lit alors sa base sur un point de montage et cherche les fichiers sur l'autre. Éjecter, débrancher, rebrancher. Vérifier aussi qu'aucun texte ne traîne dans la barre de recherche de Serato, qui filtre toutes les crates à zéro résultat.

**Un morceau appartient en moyenne à 2 crates**, jusqu'à 7. Toute opération sur un chemin doit être répercutée dans **tous** les fichiers `.crate` qui le contiennent, plus `database V2`, plus `location.sqlite`. Travailler par remplacement de chaîne sur l'ensemble des fichiers, jamais crate par crate.

---
name: punto
description: Produit un recap de fin de journee destine a Geoffrey, en langage metier sans jargon technique. Se declenche UNIQUEMENT quand Nicolas dit "punto" ou "/punto". Ne pas invoquer spontanement.
user-invocable: true
---

# Skill : Punto (recap pour Geoffrey)

## Declencheur
Uniquement quand Nicolas ecrit "punto" ou "/punto". Jamais de facon spontanee, jamais en fin de session sans le mot.

Argument optionnel : "punto semaine" -> couvrir plusieurs jours au lieu de la journee.

## Destinataire
Geoffrey (patron, Kaizen IA). Il veut savoir ce qui a bouge pour le produit et pour les clients. Il ne lit pas de code, ne connait pas les noms de tables ni de workflows.

## Deroule

### 1. Rassembler la matiere
Dans cet ordre, en s'arretant des qu'on a de quoi ecrire :
1. La conversation en cours.
2. Les commits du jour : `git log --since="00:00" --pretty=format:"%h %s"` (et `--since="7 days ago"` en mode semaine).
3. L'entree du jour dans `LOGBOOK.md` si le projet en a un.

Ne rien inventer. Si un point est incertain, ne pas l'ecrire.

### 2. Traduire avant d'ecrire
Chaque ligne doit repondre a "qu'est-ce que ca change pour un client ou pour le business ?".

Interdits dans la sortie :
- noms de fichiers, de fonctions, de colonnes, de tables, d'IDs de workflow
- hashs de commit, noms de branches, termes comme RLS, webhook, cron, policy, deploy, refacto, endpoint
- tout tiret long ou double tiret

Exemples de traduction :
- "badge lisait `is_active` au lieu du statut Unipile" -> "le dashboard affichait LinkedIn connecte alors que le compte etait coupe depuis 7 jours"
- "ajout d'un noeud Supabase dans le WF Icebreaker" -> "chaque campagne peut maintenant avoir son propre agent, au lieu d'un seul agent pour tout le compte"
- "policy UPDATE sans WITH CHECK" -> "un client aurait pu ecrire dans les donnees d'un autre client"

Si une info technique est vraiment indispensable, la mettre en une demi-phrase entre parentheses, pas plus.

### 3. Format de sortie
Bloc de code complet pour copier-coller direct (Slack ou mail). 15 lignes maximum.

```
Punto du [JJ/MM]

Fait :
- [1 a 4 lignes, resultat visible d'abord, pas la methode]

Impact client :
- [qui est concerne et ce qui change pour lui. Retirer la section si personne n'est concerne]

A savoir :
- [risque, point ouvert, ou decision qui attend Geoffrey. Retirer si rien]

Demain :
- [1 ou 2 lignes]
```

### 4. Regles de redaction
- Une ligne = un fait. Pas de paragraphe.
- Des chiffres des qu'il y en a (nombre de clients touches, de prospects, de jours d'arret).
- Le resultat en premier, la cause ensuite si utile.
- Rien de vendu comme fini tant que ce n'est pas teste et en ligne. Dire "construit, pas encore en ligne" si c'est le cas.
- Si une decision appartient a Geoffrey, la poser comme une question fermee.
- Si la journee n'a rien de presentable, le dire en une ligne plutot que de remplir.

### 5. Apres la sortie
Proposer en une phrase une version 3 lignes pour un message vocal ou un point rapide. Ne la produire que si Nicolas la demande.

## Ce que ce skill ne fait pas
- Ne cree aucun fichier, ne touche ni au LOGBOOK ni a la ROADMAP (c'est `log` / `close`)
- Ne commite pas, n'envoie rien
- Ne remplace pas `recap` (qui, lui, sert a alimenter le `/close` avec le detail technique)

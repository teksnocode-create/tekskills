# Glossaire — termes déjà acquis par Nicolas

Terme considéré comme acquis dès qu'il apparaît ici : ne plus le re-simplifier, l'utiliser directement.

- **API** : point d'entrée qu'un service expose pour qu'un autre outil vienne lui parler (comme un node HTTP Request dans n8n/Make)
- **webhook** : URL qui reçoit un événement en temps réel et déclenche un workflow (le déclencheur "Webhook" dans n8n)
- **base de données** : là où sont stockées les données structurées (l'équivalent d'une base Airtable, mais côté Supabase/Postgres)
- **workflow** : l'automatisation elle-même, la suite d'étapes (n8n/Make)
- **node** : une étape/brique dans un workflow n8n ou Make
- **trigger** : ce qui déclenche automatiquement une action (nouvelle ligne, webhook, cron)
- **cron** : programmation automatique répétée (tous les jours à telle heure, etc.)
- **migration** : un changement appliqué à la structure de la base de données (ajout de colonne, de règle, etc.)
- **RLS (Row Level Security)** : les règles qui filtrent qui a le droit de voir/modifier quelle ligne dans une table Supabase
- **endpoint** : l'adresse précise à laquelle on appelle une API
- **branche (dans un workflow)** : un chemin alternatif à l'intérieur d'un workflow, une suite de nodes qui part sur un cas particulier (comme un IF qui ouvre deux chemins différents)
- **commit / push** : sauvegarder une version du code (commit) puis l'envoyer sur GitHub (push) — c'est ce push qui déclenche le déploiement automatique en prod
- **verrou (processing_status)** : une colonne qui empêche que le même prospect soit traité deux fois en même temps par deux exécutions du workflow qui se chevauchent
- **validation stricte (Zod)** : la vérification des données d'un formulaire avant de les enregistrer, pour rejeter ce qui ne correspond pas au format attendu
- **rate-limit** : une limite du nombre d'appels autorisés dans un temps donné, pour éviter qu'un bug ou un abus fasse exploser la facture (ici la facture API Claude)
- **défense en profondeur** : ajouter une double vérification même si une protection existe déjà ailleurs, au cas où la première lâche
- **policy engine** : les règles de sécurité/limites posées en dur dans le code (pas dans le prompt de l'IA), pour qu'elles soient garanties même si l'IA se trompe
- **query_params** : les critères de recherche stockés sur une campagne (mots-clés, lieu, secteur...), comme les colonnes de réglage d'une ligne Airtable
- **query_hash** : le "code d'identité" d'une campagne, une empreinte calculée à partir de ses critères pour reconnaître une campagne identique
- **fork (dupliquer par erreur)** : créer une copie/doublon d'une campagne au lieu de reprendre la même
- **scraping** : la collecte automatique de profils LinkedIn par le workflow n8n
- **slice / couper la liste** : ne garder qu'une partie d'une liste de résultats (ex : juste les profils qui manquent pour atteindre l'objectif)
- **allowed_roles** : la liste des fonctions (rôles : icebreaker, relance, conversation) débloquées pour un client selon son forfait
- **Sales Navigator / company_headcount** : l'abonnement LinkedIn payant qui débloque des filtres avancés, dont la taille d'entreprise (nb de salariés), impossible avec un compte normal
- **tokens (design system)** : les réglages de base partagés (couleurs, polices, espacements) déclarés une seule fois pour que tous les projets s'y réfèrent
- **composant (UI)** : une brique d'interface réutilisable (bouton, carte, badge) codée une seule fois, comme un sous-workflow n8n qu'on appelle au lieu de recopier les mêmes nodes
- **importer un repo/package** : venir piocher du code depuis un autre GitHub au lieu de le copier-coller, comme relier plusieurs bases Airtable à une source commune plutôt que dupliquer les données
- **branche (git)** : une copie parallèle de tout le projet sur laquelle on bricole sans toucher à la version officielle (`main`), comme dupliquer un workflow n8n en "test" pendant que l'original tourne en prod
- **merge** : reverser une branche dans la version officielle (`main`) une fois validée — c'est ce qui envoie les modifs en prod
- **preview (Vercel)** : le site fabriqué automatiquement à partir d'une branche, avec sa propre URL de test, pendant que la vraie prod reste sur `main`

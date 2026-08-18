# Grille de scoring Temps vs Investissement — Phase 2

> Référence à charger en Phase 2 avec extended thinking activé (budget 5-10k tokens). La grille pondère chaque réponse de Phase 1 et produit un score brut sur 20 pour chaque levier. Le scoring est une aide à la décision, pas un verdict automatique — les signaux qualitatifs (contradictions, lignes rouges, cohérence globale) priment.

---

## Structure du scoring

- **Score TEMPS** : 0 à 20 points, construit par cumul des signaux pro-optimisation du temps facturé.
- **Score INVESTISSEMENT** : 0 à 20 points, construit par cumul des signaux pro-création d'assets.
- **Écart décisionnel** : |Score TEMPS − Score INVESTISSEMENT|.
  - Écart ≥ 5 → levier évident, on annonce.
  - Écart < 5 → ambiguïté, on pose UNE question de levée d'ambiguïté (voir `questions-par-metier.md`) puis on tranche.
- **Défaut si total des deux < 10** : le diagnostic est trop pauvre, on re-creuse Phase 1 avant de trancher.

---

## Barème TEMPS

Chaque item vaut 1 à 4 points. Maximum cumulable = 20.

| Signal | Issue de | Points | Condition |
|---|---|---|---|
| TJM cible > TJM actuel de +40% ou plus | Q3 | **+4** | Gros levier de pricing inexploité |
| TJM cible > TJM actuel de +15 à +40% | Q3 | **+2** | Levier pricing modéré |
| Répétition d'offre < 30% (chaque mission quasi unique) | Q10 | **+3** | Actif difficile à packager |
| Répétition d'offre 30-50% | Q10 | **+1** | Packaging possible mais pas évident |
| Reach < 500 abonnés tous canaux confondus | Q8 | **+4** | Traversée du désert trop longue pour Investissement |
| Reach 500-3000 | Q8 | **+2** | Reach émergent, pas suffisant pour lancer un produit sans risque |
| Réserve financière < 3 mois | Q6 | **+4** | Risque Investissement trop élevé, cash-flow prioritaire |
| Réserve financière 3-6 mois | Q6 | **+2** | Précaution recommandée |
| Appétence au risque ≤ 2/5 | Q7 | **+3** | Profil sécurité, Temps cadre ce profil |
| Appétence à transmettre ≤ 2/5 | Q11 | **+3** | Pas d'énergie pédagogique = Investissement douloureux |
| Temps dispo non facturable ≤ 3h/semaine | Q5 | **+3** | Pas assez pour construire un asset |
| Pas d'asset existant (Q9 = 0) + reach faible (Q8 < 2000) | Q8+Q9 | **+2** | Point de départ zéro, Temps monétise plus vite |
| Volume client actuel saturé (Q2 indique > 15 missions/mois ou > 80% capacité) | Q2 | **+2** | Pricing / rationalisation = leviers immédiats |
| Ligne rouge "pas de création de contenu / pas de face cam / pas de community" (Q13) | Q13 | **+3** | Blocage sur le nerf de l'Investissement |
| Statut auto-entrepreneur proche du plafond CA | Q4 | **+1** | Contrainte fiscale vers packaging (mais Temps possible aussi via SASU) |

**Plafond du score TEMPS** : 20 (si dépassé par cumul, on cape à 20).

---

## Barème INVESTISSEMENT

Chaque item vaut 1 à 4 points. Maximum cumulable = 20.

| Signal | Issue de | Points | Condition |
|---|---|---|---|
| Reach > 5000 abonnés cumulés (tous canaux) | Q8 | **+4** | Audience activable immédiatement |
| Reach 2000-5000 | Q8 | **+2** | Base émergente exploitable |
| Liste email > 1000 abonnés (valeur ×3 vs social) | Q8 | **+2 bonus** | Canal direct, conversion plus élevée |
| Au moins 1 asset existant qui génère du revenu récurrent | Q9 | **+4** | Preuve de faisabilité + MRR embryon |
| Asset existant sans revenu mais produit (formation, ebook, template non commercialisés) | Q9 | **+2** | Base exploitable, juste pricing/launch à faire |
| Répétition d'offre > 70% | Q10 | **+4** | Offre packageable → formation, template, SaaS |
| Répétition 50-70% | Q10 | **+2** | Packaging probable avec ajustements |
| Appétence à transmettre ≥ 4/5 | Q11 | **+4** | Carburant critique pour Investissement |
| Appétence à transmettre = 3/5 | Q11 | **+1** | Neutre mais pas bloquant |
| Appétence au risque ≥ 4/5 | Q7 | **+3** | Profil risque ouvert, tolère la traversée du désert |
| Réserve financière > 6 mois | Q6 | **+3** | Matelas suffisant pour lancer sans pression |
| Temps dispo non facturable ≥ 10h/semaine | Q5 | **+3** | Capacité de production asset réelle |
| TJM cible proche ou inférieur au TJM actuel (pas de levier pricing) | Q3 | **+2** | Le gain viendra de l'asset, pas du taux |
| Objectif 90 jours formulé en revenu *récurrent* ou *produit vendu* | Q12 | **+2** | Intention déjà alignée |
| Ligne rouge "je ne veux plus vendre mon temps / plafond horaire atteint" | Q13 | **+3** | Rejet actif du modèle Temps |

**Plafond du score INVESTISSEMENT** : 20.

---

## Cas spéciaux qui forcent ou interdisent un levier

Ces règles **écrasent** le score. Si déclenchées, tu signales et tu forces le levier correspondant (ou tu demandes à trancher entre deux règles contradictoires).

### Forçages TEMPS (veto INVESTISSEMENT)

- **Réserve financière < 2 mois ET reach < 500** → INVESTISSEMENT interdit sur 30 jours. Traversée du désert trop dangereuse. Même si le score incline Investissement, on force TEMPS pour sécuriser le cash-flow d'abord. Ouverture possible Investissement à J+90 si réserve reconstituée.
- **Appétence transmission ≤ 1/5 ET aucun asset existant** → INVESTISSEMENT interdit. Produire pédagogique à reculons pendant 30 jours = échec garanti.
- **Ligne rouge explicite "pas de création de contenu ni d'audience"** (Q13) → INVESTISSEMENT interdit sauf affiliation stratégique (cas rare).

### Forçages INVESTISSEMENT (veto TEMPS si levier réellement attendu)

- **Volume client au max ET TJM au plafond marché ET Q13 = "je ne peux plus augmenter mon volume"** → TEMPS a atteint son plateau. Si le freelance veut plus, INVESTISSEMENT est la seule voie. On ouvre même si le score est serré.
- **Asset existant avec MRR > 30% du revenu total** → le freelance est déjà en transition. Forcer TEMPS serait régression. INVESTISSEMENT.

### Alertes de cohérence (à signaler avant décision)

- **Q12 = objectif chiffré Investissement (ex: "+2000 € MRR") + Q8 = reach < 1000** → "Ton objectif demande un reach que tu n'as pas. 90 jours, ce n'est pas suffisant pour construire audience ET produit. Ajuste l'objectif ou change de levier."
- **Q12 = "arrêter de vendre mon temps" + Q3 écart énorme + Q2 volume faible** → "Tu veux sortir du Temps mais tu n'as pas exploité le Temps. Tranche : pricing d'abord (TEMPS 30j), ou vraiment switcher modèle ?"

---

## Format d'annonce du score en Phase 2

Ton annonce doit être **courte et factuelle**. Pas de prescription, juste de la donnée.

Format :
```
Score brut :
- TEMPS : X/20
  · Top 3 signaux : [signal 1 + poids], [signal 2 + poids], [signal 3 + poids]
- INVESTISSEMENT : Y/20
  · Top 3 signaux : [signal 1 + poids], [signal 2 + poids], [signal 3 + poids]

Écart : [X-Y] points.
Verdict attendu : [levier évident / ambiguïté à lever / veto à trancher].
```

Puis tu passes à la Phase 3 pour la décision.

---

## Règles de calcul (opérationnel)

1. **Additionne chaque item déclenché.** Ne double pas un item si le signal est mentionné plusieurs fois.
2. **Arrête à 20** même si la somme brute serait supérieure.
3. **Pondère à la baisse si tu appliques un défaut.** Exemple : défaut appliqué sur Q8 (reach = 0 par défaut) → tu mets le score de l'item concerné mais tu le notes comme "sur défaut" pour que le freelance puisse corriger.
4. **Top 3 signaux** = les 3 items qui ont contribué le plus de points pour chaque levier. Si égalité, prendre ceux les plus qualitatifs (Q11, Q7 avant des items numériques secs).
5. **Tu ne montres pas le calcul détaillé ligne par ligne** au freelance — seulement le score + top 3. Sinon la session devient de l'analyse quantitative et perd en tempo.

---

## Quand le scoring est inutile / trompeur

- **Profil très atypique** : serial-entrepreneur ayant déjà plusieurs exits, freelance avec 20 ans d'expertise rare, etc. Le scoring ne capture pas la singularité. Dans ce cas, tu le signales et tu bases la décision sur le dialogue Phase 2 pur.
- **Profil en transition active** : le freelance est déjà en pleine bascule Investissement (asset en cours, lancement prévu dans < 30 jours). Le scoring peut indiquer TEMPS parce que reach faible, mais on ne peut pas rebrousser chemin à 80% du parcours. On finalise Investissement et on ajuste le plan pour sécuriser le cash-flow en parallèle.
- **Profil en crise** : réserve < 1 mois, stress aigu, moral bas. Le scoring n'est pas prioritaire — on impose TEMPS défensif pour stabiliser le cash, on reporte la stratégie à J+60.

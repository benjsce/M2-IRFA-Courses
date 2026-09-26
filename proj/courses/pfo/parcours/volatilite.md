---
id: pfo/parcours-volatilite
ordre: 3
titre: Mesurer la volatilité et les co-mouvements
source: poly, §1.4–§1.6
---

## Point de départ
Les rendements sont propres. Il faut maintenant dire combien ils bougent et s'ils bougent ensemble : un actif varie de 1 % par jour, un autre de 2 %, avec une corrélation de 0,5. Deux difficultés apparaissent aussitôt, l'une dans le temps, l'autre entre les places. [ajout]

## À savoir avant
- fpp/volatilite : c'est la grandeur qu'on cherche à estimer. Ce parcours montre qu'un seul nombre fixe ne suffit pas à la décrire. [§1.4]
- pfo/rendement-logarithmique : c'est la matière première de chaque estimation du parcours, variances comme covariances. [Listing 1.2, Listing 1.3]
- fpp/echelonnement-de-la-variance : c'est lui qui justifie de multiplier une variance journalière par 252 pour l'annualiser, et l'étude de cas en éprouve l'hypothèse. [éq. 1.11]

## Étapes
1. pfo/regroupement-de-volatilite
   Première difficulté : la dispersion des rendements ne reste pas au même niveau d'une semaine à l'autre. [§1.4]
   Histoire : « combien ils bougent » — Ce 1 % par jour n'est qu'une moyenne sur la période : l'actif varie moins en temps calme, bien plus en crise, et les journées agitées se suivent. Un seul nombre fixe ne décrit pas cette alternance. [ajout]

2. pfo/ewma
   Comment estimer une volatilité qui change, sans attendre des années de données à chaque fois ? [§1.4]
   Suite : Hier, le premier actif a fait 2 %, deux fois son écart type habituel. Que faut-il croire de sa volatilité aujourd'hui ? [ajout]
   Histoire : « Que faut-il croire de sa volatilité aujourd'hui » — L'EWMA mélange la variance de la veille et le carré du dernier rendement : avec $\lambda=0{,}94$, $0{,}94\times0{,}0001+0{,}06\times0{,}02^2=0{,}000118$, soit une volatilité d'environ 1,09 %. Elle monte, sans oublier le passé. [ajout]

3. pfo/matrice-de-covariance
   Passer d'un actif à plusieurs : il faut une variance pour chacun, et un terme pour chaque couple. [§1.5]
   Histoire : « un actif varie de 1 % par jour, un autre de 2 % » — Pour les deux actifs ensemble, on range les variances et la covariance dans une matrice. Annualisée par 252 : $0{,}01^2\times252=0{,}0252$ et $0{,}02^2\times252=0{,}1008$ sur la diagonale, $0{,}5\times0{,}01\times0{,}02\times252=0{,}0252$ hors de la diagonale. [ajout]

4. pfo/matrice-de-correlation
   Ces termes croisés sont dans l'unité d'un rendement au carré, donc illisibles seuls. Comment les rendre comparables d'un couple à l'autre ? [§1.5, p. 17]
   Histoire : « s'ils bougent ensemble » — Le terme croisé, 0,0252, ne se lit pas seul : il grandit avec l'agitation de chaque actif. Divisé par le produit des écarts types, $0{,}0252/\sqrt{0{,}0252\times0{,}1008}=0{,}5$, il redonne la corrélation, comparable d'un couple d'actifs à l'autre. [ajout]

5. pfo/effet-epps
   Seconde difficulté : Tokyo ferme avant que Paris ouvre. Une corrélation calculée jour par jour sur ces places est-elle fiable ? [§1.3.1]
   Histoire : « l'autre entre les places » — Si le premier actif cote à Tokyo et le second à Paris, une nouvelle tombée l'après-midi à Paris ne touche Tokyo que le lendemain. Calculée jour par jour, la corrélation mesurée tombe sous sa vraie valeur ; des rendements hebdomadaires la mesurent mieux. [ajout]

6. pfo/norme-de-frobenius
   L'étude de cas compare deux estimations de la même matrice, journalière et hebdomadaire. Il faut un seul nombre pour dire à quel point elles diffèrent. [§1.6, §1.6.1]
   Suite : Estimée sur des rendements journaliers puis hebdomadaires, la matrice des deux actifs change : ses termes diagonaux diffèrent de 0,001 et de −0,003, et son terme croisé de 0,002. De combien les deux estimations diffèrent-elles, en un seul nombre ? [ajout]
   Histoire : « en un seul nombre » — On additionne les carrés de tous les écarts, le terme croisé comptant deux fois puisqu'il figure deux fois dans la matrice, et l'on prend la racine : $\sqrt{0{,}001^2+0{,}003^2+2\times0{,}002^2}\approx0{,}0042$. [ajout]

## Point d'arrivée
La volatilité change dans le temps, les corrélations dépendent de la fréquence et des fuseaux horaires, et deux estimations raisonnables d'une même matrice ne coïncident pas. [ajout]

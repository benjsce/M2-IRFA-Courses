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

2. pfo/ewma
   Comment estimer une volatilité qui change, sans attendre des années de données à chaque fois ? [§1.4]

3. pfo/matrice-de-covariance
   Passer d'un actif à plusieurs : il faut une variance pour chacun, et un terme pour chaque couple. [§1.5]

4. pfo/matrice-de-correlation
   Ces termes croisés sont dans l'unité d'un rendement au carré, donc illisibles seuls. Comment les rendre comparables d'un couple à l'autre ? [§1.5, p. 17]

5. pfo/effet-epps
   Seconde difficulté : Tokyo ferme avant que Paris ouvre. Une corrélation calculée jour par jour sur ces places est-elle fiable ? [§1.3.1]

6. pfo/norme-de-frobenius
   L'étude de cas compare deux estimations de la même matrice, journalière et hebdomadaire. Il faut un seul nombre pour dire à quel point elles diffèrent. [§1.6, §1.6.1]

## Point d'arrivée
La volatilité change dans le temps, les corrélations dépendent de la fréquence et des fuseaux horaires, et deux estimations raisonnables d'une même matrice ne coïncident pas. [ajout]

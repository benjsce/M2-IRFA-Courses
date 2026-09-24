---
id: fpp/parcours-flux
ordre: 2
titre: Comparer des flux séparés par le temps ou la devise
source: poly, §2
---

## Point de départ
Vaut-il mieux recevoir 100 euros aujourd'hui, 104 dans un an, ou 100 dollars dans six mois ? Ces trois flux ne se comparent pas tels quels. [ajout]

## Étapes
1. fpp/coordonnees-flux
   Pourquoi ne se comparent-ils pas ? Parce qu'un flux n'est pas seulement un montant. [§2.1]

2. fpp/facteur-conversion
   Qu'est-ce qui permet alors de les mettre côte à côte ? Un même outil sert pour le temps et pour la devise. [§2.1, §2.4]

3. fpp/convention-capitalisation
   Pour le passage entre deux dates, ce nombre peut s'écrire de plusieurs façons, qu'il faut savoir traduire l'une dans l'autre. [§2.1]

4. fpp/facteur-actualisation
   Quelle que soit l'écriture, l'objet est le même, et il a un prix de marché. [§2.1, Déf. 3]

5. fpp/valeur-actuelle-nette
   Avec ce prix, tout un échéancier de flux certains se ramène à un seul nombre. [Déf. 4]

6. fpp/duration
   Cette valeur n'est pas figée : un gérant d'obligations veut savoir à quel point elle est exposée à un mouvement de la courbe. [Déf. 5]

7. fpp/taux-zero-coupon
   Pour comparer des maturités différentes, le marché affiche ce prix sous une autre forme. [§2.3]

8. fpp/taux-forward
   Cette courbe contient davantage que ce qu'elle affiche : on peut y lire le coût d'un emprunt qui ne commencera que plus tard. [§2.3]

9. fpp/taux-de-change
   Reste l'autre coordonnée, la devise, et le nombre qui fait passer de l'une à l'autre. [§2.4]

## Point d'arrivée
Deux flux se comparent une fois ramenés à la même date et à la même devise, par des facteurs que le marché cote : le facteur d'actualisation et le taux de change. [§2.1, §2.4]

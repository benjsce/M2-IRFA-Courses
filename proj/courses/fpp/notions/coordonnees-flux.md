---
id: fpp/coordonnees-flux
nom: Coordonnées d’un flux
type: principe
statut: source
construite_a_partir_de: []
refs:
- §2.1
---

## Ce que c'est
Un flux est un montant repéré par deux coordonnées, sa devise et sa date ; deux flux ne se comparent directement que s’ils ont la même devise et la même date. [§2.1]

## Ce qui la définit
Un dollar ne vaut pas un euro ; moins évidemment, un dollar aujourd'hui ne vaut pas un dollar demain. [§2.1]

Pour comparer deux flux qui diffèrent par une coordonnée, il faut un facteur d'ajustement, et lequel dépend de la coordonnée qui les sépare : un taux de change entre deux devises, un taux d'intérêt entre deux dates. [§2.1]

![Deux lignes de temps, une par devise : chaque flux est un point, à sa date, sur la ligne de sa devise. Les trois flux de l'exemple sont trois points différents. Pour les comparer, il faut les amener au même point : changer de date le long d'une ligne, changer de devise d'une ligne à l'autre.](figures/coordonnees-flux.svg) [ajout]

## Exemple minimal
100 euros aujourd'hui, 104 euros dans un an, 100 dollars dans six mois : trois flux qui diffèrent par la date, la devise ou les deux, et dont aucun ne se compare directement à un autre. [ajout]

## Cesse d'être valide quand
rien dans le périmètre du cours [ajout]

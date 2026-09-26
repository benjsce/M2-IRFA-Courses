---
id: pfo/effet-epps
nom: Effet Epps
type: notion
statut: source
construite_a_partir_de:
- pfo/matrice-de-correlation
alias:
- Epps effect
- désynchronisation géographique
- geographical desynchronization
refs:
- §1.3.1
- §1.6.2
---

## Ce que c'est
Le biais vers le bas des corrélations calculées sur des actifs dont les séances de cotation ne se recouvrent que partiellement. [§1.3.1]

## Ce qui la définit
Le cours le signale pour une matrice de corrélation journalière calculée sans ajustement, sur des places comme Paris et New York, dont les séances ne se recouvrent qu'en partie [§1.3.1]. Entre Tokyo et Paris, qui ne se recouvrent pas du tout, le décalage est entier : c'est le cas de la figure. [ajout]

Le mécanisme est un décalage d'information. Une nouvelle tombée l'après-midi à Paris, Tokyo étant fermé, se lit le jour même à Paris et le lendemain seulement à Tokyo : les deux rendements qu'elle fait bouger portent deux dates différentes, et la corrélation, qui ne rapproche que les rendements d'une même date, ne voit pas cette part de leur co-mouvement. [ajout]

![Le mécanisme en schéma, sans l'échelle des horaires réels. La séance de Tokyo est finie quand celle de Paris commence. Une nouvelle tombe l'après-midi à Paris : Paris la cote le jour même, Tokyo le lendemain, et les deux rendements qu'elle fait bouger portent deux dates différentes.](figures/effet-epps.svg) [ajout]

## Le chemin jusqu'ici
L'objet biaisé est pfo/matrice-de-correlation : l'effet Epps n'est pas une propriété des actifs mais de la façon dont on mesure leurs co-mouvements. [ajout]

Cette corrélation se lit dans pfo/matrice-de-covariance, estimée sur des rendements de pfo/rendement-logarithmique, annualisée par 252 parce que fpp/echelonnement-de-la-variance fait croître la variance comme le temps, puis réduite par les écarts types de fpp/volatilite. [ajout]

## Cesse d'être valide quand
Il s'atténue quand la période de mesure s'allonge : sur des rendements hebdomadaires, une nouvelle comptée un jour plus tard à Tokyo tombe le plus souvent dans la même semaine qu'à Paris, et la corrélation la voit [ajout]. C'est la question que pose l'étude de cas, qui compare l'estimation hebdomadaire à l'estimation journalière. [§1.6.2]

## Origine
- exercice pfo/ex-01 : l'effet Epps tire vers le bas les covariances journalières entre places désynchronisées, et contribue à l'écart entre les deux matrices [ajout]

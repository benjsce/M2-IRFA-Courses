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
Quand on optimise des actifs cotés dans des fuseaux horaires différents, Paris et New York par exemple, les fenêtres de cotation ne se chevauchent qu'en partie. Une matrice de corrélation journalière calculée sans ajustement a alors des coefficients artificiellement tirés vers le bas. [§1.3.1]

Le mécanisme est un décalage d'information. Une nouvelle tombée après la clôture de Tokyo se lit le jour même à New York et le lendemain seulement à Tokyo : les deux rendements d'une même date ne portent pas les mêmes nouvelles, et une partie de leur co-mouvement tombe sur deux dates différentes, que la corrélation du même jour ne voit pas. [ajout]

![Le mécanisme en schéma, sans l'échelle des horaires réels. Une nouvelle tombe après la clôture de Tokyo : New York la cote le jour même, Tokyo le lendemain, et les deux rendements qu'elle fait bouger portent deux dates différentes.](figures/effet-epps.svg) [ajout]

## Le chemin jusqu'ici
L'objet biaisé est pfo/matrice-de-correlation : l'effet Epps n'est pas une propriété des actifs mais de la façon dont on mesure leurs co-mouvements. [ajout]

Cette corrélation se lit dans pfo/matrice-de-covariance, dont les entrées sont des rendements de pfo/rendement-logarithmique et dont l'annualisation par 252 suppose, avec fpp/echelonnement-de-la-variance, que la variance croît comme le temps. fpp/volatilite fournit les écarts types par lesquels on divise les covariances. [ajout]

## Cesse d'être valide quand
Le cours pose, dans son étude de cas, la question de son effet sur une estimation hebdomadaire comparée à une estimation journalière. [§1.6.2]

Il s'atténue quand la période de mesure s'allonge : sur des rendements hebdomadaires, un décalage de quelques heures entre deux clôtures ne pèse presque plus face à cinq séances de mouvements. [ajout]

## Origine
- exercice pfo/ex-01 : l'effet Epps tire vers le bas les covariances journalières entre places désynchronisées, et contribue à l'écart entre les deux matrices [ajout]

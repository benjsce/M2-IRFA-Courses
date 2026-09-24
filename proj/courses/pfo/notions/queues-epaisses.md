---
id: pfo/queues-epaisses
nom: Queues épaisses
type: notion
statut: source
cas_de: pfo/fait-stylise
valeur: la rareté des rendements extrêmes
construite_a_partir_de:
- pfo/kurtosis
alias:
- fat tails
- leptokurtique
- leptokurtic distribution
- distribution leptokurtique
- queues lourdes
refs:
- §2.1.1
- p. 20
- p. 23
- Fig. 2.2
---

## Ce que c'est
Une loi a des queues épaisses quand elle produit plus d'observations très éloignées de sa moyenne que la loi normale de même moyenne et de même variance. [p. 23]

## Ce qui la définit
Les événements extrêmes, krachs ou envolées euphoriques, ont une probabilité bien plus forte que ne le prédit la loi normale : un rendement de −8 %, que le modèle gaussien juge presque impossible, est moins rare dans les données réelles. [§2.1.1, p. 24]

Le cours la formalise par la kurtosis. Une loi d'excès de kurtosis positif est dite leptokurtique : queues plus épaisses et pic central plus haut que la loi normale. D'excès nul, elle est mésokurtique ; d'excès négatif, platykurtique. [p. 20, p. 23, Fig. 2.2]

![À variance égale, la loi leptokurtique a un pic plus haut, des flancs plus minces et des queues plus épaisses que la loi normale.](figures/queues-epaisses.svg) [ajout]

## Le chemin jusqu'ici
pfo/kurtosis fournit la mesure : c'est le moment d'ordre 4, qui pèse chaque écart par sa quatrième puissance et devient donc très sensible aux observations lointaines. Les queues épaisses sont la lecture de son excès positif, une fois retiré le 3 de la loi normale. [ajout]

La réduction par l'écart type de fpp/volatilite est ce qui rend la comparaison honnête : on compare des lois de même variance, et l'épaisseur des queues n'est pas une affaire de dispersion. [ajout]

## Exemple minimal
Une loi de Laplace de variance 1, d'excès de kurtosis 3, s'écarte de plus de trois écarts types de sa moyenne avec une probabilité de 1,4 %, contre 0,27 % pour la loi normale. [ajout]

## Cesse d'être valide quand
L'excès de kurtosis n'est pas une mesure des queues seules : il monte aussi quand le pic central devient plus pointu, et une loi peut être leptokurtique sans que ses pertes extrêmes soient plus fréquentes que ses gains extrêmes. [ajout]

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
Les événements extrêmes, krachs ou envolées euphoriques, ont une probabilité bien plus forte que ne le prédit la loi normale. [§2.1.1]

Le cours la formalise par la kurtosis. Une loi d'excès de kurtosis positif est dite leptokurtique : queues plus épaisses et pic central plus haut que la loi normale. D'excès nul, elle est mésokurtique ; d'excès négatif, platykurtique. [p. 20, p. 23, Fig. 2.2]

![À variance égale, la loi de Laplace, leptokurtique, a un pic plus haut, des flancs plus minces et des queues plus épaisses que la loi normale. À droite, la queue grossie : au-delà de trois écarts types, la loi de Laplace garde 0,72 % de probabilité de chaque côté, la loi normale 0,135 % ; des deux côtés, 1,4 % contre 0,27 %, les chiffres de l'exemple.](figures/queues-epaisses.svg) [ajout]

## Le chemin jusqu'ici
pfo/kurtosis fournit la mesure : c'est le moment d'ordre 4, qui pèse chaque écart par sa quatrième puissance et devient donc très sensible aux observations lointaines. Les queues épaisses sont la lecture de son excès positif, une fois retiré le 3 de la loi normale. [ajout]

La réduction par l'écart type de fpp/volatilite est ce qui rend la comparaison honnête : on compare des lois de même variance, et l'épaisseur des queues n'est pas une affaire de dispersion. [ajout]

## Exemple minimal
Une loi de Laplace de variance 1, d'excès de kurtosis 3, s'écarte de plus de trois écarts types de sa moyenne avec une probabilité de 1,4 %, contre 0,27 % pour la loi normale. [ajout]

Le cours cite un rendement de −8 %, auquel un modèle gaussien attribue une probabilité très faible alors qu'il est moins rare dans les données réelles [p. 24]. Pour une volatilité journalière de 2 %, c'est un écart de quatre écarts types. [ajout]

## Cesse d'être valide quand
Le pic plus haut accompagne ici les queues épaisses, mais ce n'est pas lui que mesure la kurtosis. À moins d'un écart type de la moyenne, l'écart réduit à la puissance quatre reste inférieur à 1 : cette zone ne fournit que 0,09 de la kurtosis de 6 de la loi de Laplace, moins encore que pour la loi normale, 0,11 ; tout le reste vient des écarts lointains. [ajout]

Une loi peut être leptokurtique sans que ses pertes extrêmes soient plus fréquentes que ses gains extrêmes : la kurtosis ne dit pas de quel côté sont les écarts. [ajout]

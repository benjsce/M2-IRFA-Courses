---
id: pfo/asymetrie-negative
nom: Asymétrie négative
type: notion
statut: source
cas_de: pfo/fait-stylise
valeur: la symétrie entre les pertes et les gains
construite_a_partir_de:
- pfo/coefficient-d-asymetrie
alias:
- negative skewness
- left skewness
- asymétrie à gauche
refs:
- §2.1.1
- p. 21
- Fig. 2.1
- éq. 2.8
- éq. 2.12
---

## Ce que c'est
Une loi est asymétrique à gauche quand sa queue des pertes est plus longue ou plus lourde que sa queue des gains, ce qui se lit à un coefficient d'asymétrie négatif. [§2.1.1, p. 21]

## Ce qui la définit
Les rendements des actifs risqués, des actions notamment, présentent souvent une asymétrie à gauche : les mouvements de baisse y sont plus brutaux que les mouvements de hausse. [§2.1.1]

Deux actifs peuvent avoir même moyenne et même volatilité et des lois très différentes : l'un fait des gains et des pertes symétriques, l'autre beaucoup de petits gains et quelques très grosses pertes. Seul le second est asymétrique à gauche, et la volatilité ne le voit pas. [p. 21]

Combinée à un excès de kurtosis positif, elle décrit la situation que la gestion des risques redoute le plus : des pertes extrêmes à la fois plus asymétriques et plus fréquentes que ne le dit la loi normale. [éq. 2.12, p. 25]

## Le chemin jusqu'ici
pfo/coefficient-d-asymetrie fournit le signe qui la définit ; l'asymétrie négative en est la lecture financière, du côté des pertes. [ajout]

Ce coefficient est réduit par le cube de l'écart type de fpp/volatilite, si bien que le fait stylisé porte sur la forme de la loi et non sur l'ampleur des mouvements. [ajout]

## Cesse d'être valide quand
Le signe du coefficient empirique est fragile : un seul krach dans l'échantillon peut le rendre négatif. Dans l'exemple du cours, la seule perte de −10 % fait passer l'asymétrie de la série de 0 à −1,37 ; sur une période qui ne la contient pas, le fait stylisé disparaît. [ajout]

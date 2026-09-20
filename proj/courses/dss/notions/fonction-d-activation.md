---
id: dss/fonction-d-activation
nom: Fonction d'activation
type: notion
statut: source
construite_a_partir_de:
- dss/perceptron
alias:
- activation function
- transfer function
refs:
- slide 151
- slide 178
---

## Ce que c'est
La transformation appliquée au total pondéré pour produire la sortie d'un nœud. [slide 178]

## Ce qui la définit
Le passage du seuil à une fonction non linéaire dérivable est ce qui a rendu possible l'apprentissage multicouche : la sortie varie continûment mais pas linéairement, et l'on peut la dériver. [slide 151]

La sigmoïde est celle sur laquelle repose la rétropropagation du cours ; les autres sont listées comme des choix de conception. [slide 155, slide 178]

Le choix de l'intégration des entrées est traité au même endroit : sommées, sommées après élévation au carré, ou multipliées. [slide 178]


## Le chemin jusqu'ici
Le socle est celui du perceptron : dss/apprentissage-supervise et dss/apprentissage-inductif mènent à dss/reseau-de-neurones-artificiel et à dss/fonction-discriminante-lineaire, dont dss/perceptron est la rencontre. [ajout]

La fonction d'activation est la pièce du perceptron que l'on dégage pour en changer : c'est en remplaçant le seuil par une sigmoïde dérivable que l'apprentissage multicouche devient possible. [ajout]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| fonction d'activation | sigmoïde (logistique) | $1/(1+e^{-x})$, celle de la rétropropagation |
| fonction d'activation | tangente hyperbolique | sortie centrée sur zéro |
| fonction d'activation | gaussienne | réponse locale |
| fonction d'activation | linéaire | pas de non-linéarité |
| fonction d'activation | soft-max | sortie lue comme une distribution |
[slide 178]

## Cesse d'être valide quand
La rétropropagation telle que le cours l'écrit repose sur la sigmoïde : les formules de $d_j$ portent le facteur $o_j(1-o_j)$, qui est sa dérivée. [slide 155, slide 159]

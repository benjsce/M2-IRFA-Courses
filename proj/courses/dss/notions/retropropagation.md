---
id: dss/retropropagation
nom: Rétropropagation
symbole: $w_{ij}$, $o_j$, $t_j$, $E$
type: notion
statut: source
construite_a_partir_de:
- dss/reseau-multicouche
- dss/descente-de-gradient
alias:
- back-propagation
- bp
- generalized delta rule
refs:
- slide 153
- slide 154
- slide 155
- slide 156
- slide 157
- slide 158
- slide 159
- slide 179
- slide 200
- slide 201
---

## Ce que c'est
Propager l'erreur globale vers l'arrière pour corriger chaque poids proportionnellement à sa contribution. [slide 154]

## Forme
$$E=\tfrac12\sum_j(t_j-o_j)^2,\qquad \Delta w_{ij}=\eta\,d_j o_i$$
$$d_j=o_j(1-o_j)(t_j-o_j)\ \text{(sortie)},\qquad d_i=o_i(1-o_i)\sum_j EI_j w_{ij}\ \text{(caché)}$$ [slide 155, slide 159]

## Ce que les symboles modélisent
$w_{ij}$ est le poids de la connexion allant du nœud $i$ vers le nœud $j$ : l'ordre des indices est un sens de circulation, pas une convention indifférente. $o_j$ est ce que le nœud $j$ produit, $t_j$ ce qu'on aurait voulu qu'il produise, et $E$ l'écart entre les deux, sommé sur les nœuds de sortie. [slide 155, slide 156]

## Ce qui la définit
L'idée est simple à énoncer : l'erreur globale est renvoyée vers l'arrière, et chaque poids est modifié en proportion de ce qu'il a contribué. C'est ce renvoi qui donne son nom à l'algorithme. [slide 154]

Ce qui circule n'est pas l'erreur mais son taux de variation. Le calcul se fait en quatre temps : comment l'erreur change quand la sortie du nœud change, quand son entrée totale change, quand le poids entrant change, puis quand la sortie du nœud précédent change. [slide 155, slide 157]

Les deux formules de $d$ diffèrent par ce qui joue le rôle de l'erreur : pour un nœud de sortie, l'écart à la cible ; pour un nœud caché, la somme pondérée des erreurs des nœuds qu'il alimente. Le facteur $o(1-o)$ est la dérivée de la sigmoïde, commun aux deux. [slide 159]

Le cours la donne comme l'algorithme d'apprentissage le plus important des réseaux de neurones, redécouvert en 1986. [slide 154]


## Le chemin jusqu'ici
Deux fils se referment ici. Le premier va de dss/apprentissage-supervise et dss/apprentissage-inductif à dss/fonction-discriminante-lineaire et dss/reseau-de-neurones-artificiel, puis à dss/perceptron, dss/limite-du-perceptron, dss/fonction-d-activation et dss/reseau-multicouche : c'est la machine. Le second va de dss/regle-delta à dss/descente-de-gradient : c'est le geste de correction. [ajout]

La rétropropagation est exactement ce qui manquait pour les joindre. Le geste existait, mais il exigeait une sortie désirée ; la machine existait, mais ses nœuds cachés n'en ont pas. L'algorithme fabrique ce qui en tient lieu. [ajout]

## Exemple minimal
Pour un nœud de sortie à $o_j=0{,}6$ et $t_j=1$, on a $d_j=0{,}6\times0{,}4\times0{,}4=0{,}096$. [ajout]

## Geste de calcul type
Calculer d'abord tous les $d$ de la couche de sortie, puis remonter couche par couche : un $d$ caché a besoin de tous les $d$ de la couche au-dessus. [slide 159]

## Cesse d'être valide quand
Le cours en liste les défauts : minimum local, peu plausible biologiquement, coûteux en temps d'entraînement, et surtout opaque — c'est une boîte noire dont on ne voit pas comment elle décide. [slide 200]

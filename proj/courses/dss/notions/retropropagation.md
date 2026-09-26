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
Donner à chaque nœud caché, qui n'a pas de cible, une part de l'erreur de sortie proportionnelle à son poids vers elle, puis corriger ses poids comme ceux de la sortie. [slide 154, slide 159]

## Forme
$$d_j=o_j(1-o_j)(t_j-o_j)\ \ \text{(sortie)},\qquad d_i=o_i(1-o_i)\sum_j d_j\,w_{ij}\ \ \text{(caché)}$$
$$\Delta w_{ij}=\eta\,d_j\,o_i=-\eta\,\frac{\partial E}{\partial w_{ij}},\qquad E=\tfrac12\sum_j(t_j-o_j)^2$$ [slide 155, slide 159]

## Ce que les symboles modélisent
$w_{ij}$ est le poids de la connexion allant du nœud $i$ vers le nœud $j$ : l'ordre des indices est un sens de circulation. $o_j$ est ce que le nœud $j$ produit, sa sortie après la sigmoïde ; $t_j$ ce qu'on aurait voulu qu'il produise, sa cible, qui n'existe que pour les nœuds de sortie. $E$ est l'erreur sur un motif : la moitié de la somme des carrés des écarts, sur les nœuds de sortie. [slide 155, slide 156]

$d$ est le signal d'erreur d'un nœud, ce qu'on renvoie vers ses poids entrants ; il a le signe de l'écart $t-o$, si bien que $\Delta w_{ij}=\eta\,d_j\,o_i$ fait baisser l'erreur. La slide l'écrit aussi $EI_j$ : c'est le même nombre. $\eta$ est le taux d'apprentissage de la règle delta. [slide 159, ajout]

Dans la formule du nœud caché, les indices changent de rôle : $i$ est le nœud caché dont on cherche le $d$, et $j$ parcourt les nœuds qu'il alimente, dont les $d$ sont déjà connus. [slide 159, ajout]

## Retrouver la formule
![Le mini-réseau, au point $(1,0)$ du OU exclusif. La sortie a une cible, donc une erreur, et son $d$ vaut 0,096. Les nœuds cachés n'ont pas de cible : chacun reçoit ce $d$ par son poids vers la sortie, 0,4 ou 1, puis le multiplie par sa propre pente, 0,25 ou 0,16. Le nœud au poids le plus fort porte la plus grosse part.](figures/retropropagation.svg) [ajout]

Le réseau de la figure apprend le OU exclusif ; on lui présente le point $(1,0)$, dont la sortie désirée est 1. Le passage avant a donné 0,5 et 0,2 aux deux nœuds cachés ; leurs poids vers la sortie valent 0,4 et 1, d'où un total de $0{,}4\times0{,}5+1\times0{,}2=0{,}4$ et une sortie $1/(1+e^{-0{,}4})\approx0{,}60$. On a omis les seuils, pour garder les calculs courts. [ajout]

**Connu** : l'erreur en sortie, puisque la cible y est donnée, et les poids qui relient chaque nœud caché à la sortie. **Cherché** : la part de cette erreur à imputer à chaque nœud caché, qui n'a pas de cible, et donc à ses poids. [slide 152, ajout]

En sortie, l'écart vaut $1-0{,}60=0{,}40$. On le multiplie par la pente de la sigmoïde en ce point, $0{,}60\times0{,}40=0{,}24$ : c'est de combien la sortie bouge quand son total bouge un peu, donc ce qu'une correction de poids peut y changer. D'où $d_j=0{,}24\times0{,}40\approx0{,}096$. [slide 159, ajout]

Chaque poids vers la sortie se corrige alors par la règle delta, l'entrée étant la sortie du nœud caché : avec $\eta=0{,}1$, il monte de $0{,}1\times0{,}096\times0{,}5\approx0{,}0048$ pour le premier nœud, de $0{,}1\times0{,}096\times0{,}2\approx0{,}0019$ pour le second. [slide 159, ajout]

Un nœud caché n'a pas de cible, donc pas d'écart. Mais si sa sortie montait un peu, le total de la sortie monterait de ce peu multiplié par son poids vers elle : l'erreur remonte donc par ce même poids. Le premier nœud reçoit $0{,}4\times0{,}096=0{,}0384$, le second $1\times0{,}096=0{,}096$. [slide 154, ajout]

On multiplie encore par la pente du nœud caché lui-même, $0{,}5\times0{,}5=0{,}25$ et $0{,}2\times0{,}8=0{,}16$ : $d_1=0{,}0096$ et $d_2\approx0{,}015$. Le second nœud, dont le poids vers la sortie est le plus fort, porte la plus grosse part, bien que sa pente soit plus faible. [ajout]

Le nœud caché a maintenant un $d$, et ses poids entrants se corrigent comme ceux de la sortie. Depuis $x_1=1$, ils montent de $0{,}1\times0{,}0096\approx0{,}00096$ et de $0{,}1\times0{,}015\approx0{,}0015$ ; depuis $x_2=0$, ils ne bougent pas, comme dans la règle delta. [ajout]

Un nœud caché qui alimente plusieurs nœuds reçoit une part de chacun, et on les additionne. Pour toute connexion du nœud $i$ vers le nœud $j$ : [slide 159]

$$\Delta w_{ij}=\eta\,d_j\,o_i,\qquad d_j=o_j(1-o_j)(t_j-o_j)\ \ \text{(sortie)},\qquad d_i=o_i(1-o_i)\sum_j d_j\,w_{ij}\ \ \text{(caché)}$$ [slide 159]

## Ce qui la définit
L'idée est simple à énoncer : l'erreur globale est renvoyée vers l'arrière, et chaque poids est modifié en proportion de sa contribution. C'est ce renvoi qui donne son nom à l'algorithme. [slide 154]

Ce qui circule n'est pas l'erreur mais son taux de variation. Les quatre temps de la slide sont les pas ci-dessus : comment l'erreur change quand la sortie du nœud change, puis quand son entrée totale change — la pente —, puis quand un poids entrant change, puis quand la sortie du nœud précédent change — la part renvoyée. [slide 155, slide 157]

Les deux formules de $d$ ne diffèrent que par ce qui joue le rôle de l'écart : pour un nœud de sortie, l'écart à la cible ; pour un nœud caché, la somme pondérée des $d$ des nœuds qu'il alimente. Le facteur $o(1-o)$, la pente de la sigmoïde, est commun aux deux. [slide 159]

Le cours la donne comme l'algorithme d'apprentissage le plus important des réseaux de neurones, redécouvert en 1986 ; la chronologie de la slide 131 dit 1985. [slide 154, slide 131]

## Le chemin jusqu'ici
Deux fils se referment ici. La machine d'abord : un dss/perceptron, le neurone de dss/reseau-de-neurones-artificiel qui trace une dss/fonction-discriminante-lineaire, ne sépare pas le OU exclusif, comme le montre dss/limite-du-perceptron ; dss/reseau-multicouche y répond par une couche cachée, dont les nœuds portent la sigmoïde dérivable de dss/fonction-d-activation. [ajout]

Le geste ensuite : dss/regle-delta corrige un poids par l'erreur et l'entrée, et dss/descente-de-gradient y lit un pas contre la pente de l'erreur. Mais ce geste exige une sortie désirée, que dss/apprentissage-supervise ne fournit que pour la couche de sortie. La rétropropagation fabrique ce qui en tient lieu pour les nœuds cachés, et rend ainsi cherchable, au sens de dss/apprentissage-inductif, toute la famille des réseaux à couche cachée. [ajout]

## Exemple minimal
Au point $(1,0)$ du OU exclusif, une sortie de 0,60 pour une cible de 1 donne $d_j=0{,}096$ ; renvoyé par des poids de 0,4 et 1 vers des nœuds cachés de sortie 0,5 et 0,2, il leur donne $d=0{,}0096$ et $0{,}015$. [ajout]

## Geste de calcul type
Calculer d'abord tous les $d$ de la couche de sortie, puis remonter couche par couche : un $d$ caché a besoin de tous les $d$ de la couche au-dessus. [slide 159]

## Cesse d'être valide quand
Le cours en liste les défauts : minimum local, peu plausible biologiquement, coûteux en temps d'entraînement, et surtout opaque — c'est une boîte noire dont on ne voit pas comment elle décide. [slide 200]

---
id: dup/aversion-absolue-arrow-pratt
nom: Aversion absolue d’Arrow-Pratt
symbole: $A(x)$
type: notion
statut: source
cas_de: dup/courbure-de-l-utilite
valeur: la courbure, mesurée localement et normalisée
construite_a_partir_de:
- dup/fonction-utilite
alias:
- Arrow-Pratt
- coefficient d'aversion absolue
refs:
- L1 slide 32
- L1 slide 33
---

## Ce que c'est
La courbure de l’utilité, normalisée par sa pente, en un point de richesse. [L1 slide 33]

## Forme
$$A(x)=-\dfrac{U''(x)}{U'(x)}$$ [L1 slide 33]

## Ce que les symboles modélisent
$A(x)$ prend un niveau de richesse et rend un nombre : la vitesse à laquelle l'utilité se courbe à cet endroit, rapportée à sa pente. C'est une mesure **locale**, pas une préférence entre deux paris — deux agents peuvent partager la même valeur en un point et diverger partout ailleurs. La division par la pente est ce qui la rend insensible à l'échelle choisie pour $u$. [L1 slide 33]

## Ce qui la définit
La normalisation par $U'$ est ce qui rend la mesure invariante par transformation affine de $U$ : deux utilités qui représentent les mêmes préférences ont le même $A$. [ajout]

Le cours donne trois énoncés équivalents de « l’agent 1 est partout plus averse que l’agent 2 » : $A_1\ge A_2$ partout ; $U_1$ est une transformée croissante concave de $U_2$ ; l’agent 1 refuse tout pari que l’agent 2 refuse à la même richesse. [L1 slide 33]

## Le chemin jusqu'ici
Le socle se réduit à dup/fonction-utilite. [ajout]

Tout se joue dans la courbure de $U$. Le rapport $-U''/U'$ normalise cette courbure par la pente, ce qui la rend insensible au changement d'échelle de l'utilité — c'est ce qui en fait une mesure de l'agent et non de la façon dont on a écrit son utilité. Aucune loterie n'est nécessaire pour la définir. [ajout]

## Exemple minimal
Pour $u(z)=\ln z$ : $A(z)=1/z$, soit $0{,}01$ à une richesse de 100. [L1 slide 35]

## Geste de calcul type
Dériver deux fois, faire le rapport, changer de signe. Pour comparer deux agents, comparer les deux fonctions $A$ point par point — c’est cela qui a un sens observable, pas la comparaison des $U''$. [L1 slide 33]

## Cesse d'être valide quand
C’est une mesure locale : elle vaut au point de richesse où elle est calculée, et ne dit rien des grands risques. [L1 slide 32]

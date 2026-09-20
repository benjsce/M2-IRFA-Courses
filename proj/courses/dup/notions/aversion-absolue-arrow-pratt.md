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

## Ce qui la définit
La normalisation par $U'$ est ce qui rend la mesure invariante par transformation affine de $U$ : deux utilités qui représentent les mêmes préférences ont le même $A$. [ajout]

Trois énoncés équivalents pour « l’agent 1 est partout plus averse que l’agent 2 » : $A_1\ge A_2$ partout ; $U_1$ est une transformée croissante concave de $U_2$ ; l’agent 1 refuse tout pari que l’agent 2 refuse à la même richesse. [L1 slide 33]

## Exemple minimal
Pour $u(z)=\ln z$ : $A(z)=1/z$, soit $0{,}01$ à une richesse de 100. [L1 slide 35]

## Geste de calcul type
Dériver deux fois, faire le rapport, changer de signe. Pour comparer deux agents, comparer les deux fonctions $A$ point par point — c’est cela qui a un sens observable, pas la comparaison des $U''$. [L1 slide 33]

## Cesse d'être valide quand
C’est une mesure locale : elle vaut au point de richesse où elle est calculée, et ne dit rien des grands risques. [L1 slide 32]

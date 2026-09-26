---
id: dup/theorie-du-regret
nom: Théorie du regret
type: notion
statut: source
cas_de: dup/axiome-independance
valeur: la comparaison état par état avec l’option abandonnée
construite_a_partir_de:
- dup/acte
alias:
- regret theory
refs:
- L1 slide 58
---

## Ce que c'est
La valeur d’un résultat dépend de ce qu’on aurait obtenu en choisissant autrement. [L1 slide 58]

## Forme
$$v(x,y)\quad\text{où }y\text{ est le résultat de l’option abandonnée dans le même état}$$ [L1 slide 58]

## Ce que les symboles modélisent
$v(x,y)$ prend deux résultats du même état — celui qu'on a obtenu, $x$, et celui que l'option abandonnée aurait donné, $y$ — et rend la valeur vécue du premier. Ce n'est pas une utilité ordinaire de $x$ : la même somme reçue vaut plus ou moins selon $y$. [L1 slide 58, ajout]

## Ce qui la définit
Regret quand le résultat choisi est le moins bon, satisfaction quand il est le meilleur. Le choix dépend donc de la comparaison état par état, et non de la seule distribution marginale de chaque acte. [L1 slide 58]

## Le chemin jusqu'ici
Il n'y a qu'un prérequis, dup/acte, qui attache une conséquence à chaque état du monde. [ajout]

C'est précisément ce qu'il faut : le regret compare, dans un même état, ce qu'on a obtenu et ce qu'on aurait obtenu autrement. Une loterie ne suffirait pas — elle brasse les états, et le contrefactuel disparaît. [ajout]

## Exemple minimal
Recevoir 100 dans un état où l’option abandonnée donnait 0 ne vaut pas recevoir 100 dans un état où elle donnait 1 000. [ajout]

## Geste de calcul type
Ne pas réduire chaque acte à sa distribution : écrire la table état par état, et comparer ligne à ligne. [L1 slide 58]

## Cesse d'être valide quand
Le modèle abandonne la transitivité dans ses versions les plus simples : c’est le prix payé pour la dépendance au contexte. [ajout]

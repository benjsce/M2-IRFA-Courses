---
id: dup/paradoxe-rabin
nom: Paradoxe de Rabin
type: notion
statut: source
construite_a_partir_de:
- dup/aversion-second-ordre
alias:
- Rabin paradox
- théorème de calibration
refs:
- L2 slide 25
- L2 slide 26
- L2 slide 27
---

## Ce que c'est
Refuser un petit pari favorable à tout niveau de richesse oblige à refuser des paris énormes, ce qui est absurde. [L2 slide 25]

## Forme
$$u(w)-u(w-g)\ \ge\ \dfrac{g}{l}\big[u(w+g)-u(w)\big]$$ [L2 éq. 2]

## Ce qui la définit
L’hypothèse forte n’est pas le refus, c’est le « à **tout** niveau de richesse » : l’utilité marginale doit alors décroître d’un facteur $g/l$ à chaque pas de largeur $g$, et l’effet cumulé est gigantesque. [L2 slide 26]

Si $(g/l)^m<2$, l’agent refuse le pari de perte $L=mg$ et de gain $G=ng$ dès que $n<\log\!\big(2-(g/l)^m\big)/\log(l/g)$. Si $(g/l)^m>2$, il refuse quel que soit le gain. [L2 slide 27]

## Exemple minimal
Avec $l=100$ et $g=105$ : l’agent refuse un pari de perte 945 et de gain 1 680, et refuse toute perte supérieure à 1 575 quel que soit le gain. [L2 slide 27]

## Geste de calcul type
Chaîner l’inégalité clé sur $m$ pas vers le bas et $n$ pas vers le haut, sommer les deux séries géométriques, puis comparer : c’est toute la preuve. [L2 slide 28, L2 slide 29, L2 slide 30, L2 slide 31]

## Cesse d'être valide quand
Le paradoxe résiste à l’aversion absolue décroissante : la table recalculée sous DARA donne des seuils encore plus absurdes. Il ne résiste pas à une aversion du premier ordre. [L2 slide 32, L3 slide 41]

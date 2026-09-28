---
id: dup/biais-pour-le-present
nom: Biais pour le présent
type: notion
statut: source
construite_a_partir_de:
- dup/utilite-actualisee
- dup/inversion-des-preferences-dans-le-temps
alias:
- present bias
- present-biased preferences
refs:
- L5 slide 11
- L5 slide 12
---

## Ce que c'est
Une attente coûte plus quand elle commence aujourd'hui que quand elle commence plus tard. [L5 slide 12]

## Forme
$$\frac{D(0)}{D(\tau)}>\frac{D(t)}{D(t+\tau)}\qquad\forall\,t,\tau>0$$ [L5 slide 12]

## Ce que les symboles modélisent
$D(t)/D(t+\tau)$ est le prix d'une attente : combien il faut d'utilité en $t+\tau$ pour compenser une unité en $t$. Le biais compare ce prix quand l'attente part d'aujourd'hui, $t=0$, et quand elle part d'une date $t$ plus lointaine ; $\tau$ est la longueur de l'attente, la même des deux côtés. [L5 slide 12]

## Ce qui la définit
Le connu : les deux choix, 100 tout de suite contre 110 dans quatre semaines, 100 dans vingt-six contre 110 dans trente. Le trou : ce qu'ils disent de $D$. Le premier donne $D(0)/D(4)>u(110)/u(100)$, le second $D(26)/D(30)<u(110)/u(100)$ ; ensemble, $D(0)/D(4)>D(26)/D(30)$. [L5 slide 11]

![Les deux attentes de quatre semaines, sur une même fonction d'actualisation qui tombe de 1 à ½ dès la première semaine. Celle qui part d'aujourd'hui divise le poids par D(0)/D(4) = 2 ; celle qui part de la semaine 26 ne le divise que par D(26)/D(30) = 1 : D(0)/D(τ) > D(t)/D(t+τ).](figures/biais-pour-le-present.svg) [ajout]

L'actualisation exponentielle l'exclut, puisque ses deux rapports valent $1/\delta^\tau$. [L5 slide 12]

## Le chemin jusqu'ici
dup/inversion-des-preferences-dans-le-temps fournit les deux choix, et montre que dup/actualisation-exponentielle ne peut pas les trancher en sens opposés, puisqu'elle pèse une attente par son seul délai. [L5 slide 7]

dup/utilite-actualisee pose alors un poids des dates sans lui imposer de forme, et garde de dup/fonction-utilite la même évaluation de 100 et de 110 à toutes les dates. Le biais pour le présent est la condition que les deux choix imposent à ce poids. [L5 slide 10, L5 slide 11]

## Exemple minimal
$D(0)=1$ et $D(t)=\tfrac12$ pour toute date future : $D(0)/D(4)=2$, et $D(26)/D(30)=1$. [L5 slide 14]

## Geste de calcul type
Écrire chacun des deux choix comme une inégalité entre $D$ et le rapport $u(110)/u(100)$, puis enchaîner les deux inégalités pour faire disparaître $u$. [L5 slide 11]

## Cesse d'être valide quand
L'impatience diminue encore quand on s'éloigne d'aujourd'hui, et pas seulement au premier pas : préférer 100 dans une semaine à 110 dans cinq, mais 110 dans trente à 100 dans vingt-six, demande une condition plus forte. [L5 slide 15]

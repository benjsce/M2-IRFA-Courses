---
id: fpp/valeur-temps
nom: Valeur temps
symbole: $TV$
type: notion
statut: source
construite_a_partir_de:
- fpp/valeur-intrinseque
- fpp/formule-black-scholes
alias:
- time value
refs:
- Déf. 13
---

## Ce que c'est
Ce que le prix d'un payoff ajoute à sa valeur intrinsèque : positive quand le payoff est convexe, négative quand il est concave. [Déf. 13]

## Forme
$$\mathrm{Price}=IV+TV$$ [Déf. 13]

## Ce que les symboles modélisent
$TV$ est un prix, comme $IV$. Il mesure ce que vaut l'aléa lui-même : ce qu'un payoff gagne à ce que l'avenir ne soit pas certain. [Déf. 13, ajout]

## Ce qui la définit
Ce qui est **connu** : le prix de l'option et sa valeur intrinsèque. Ce qu'on **cherche** : leur écart, et surtout son signe. Pour un payoff convexe, la moyenne des paiements dépasse le paiement de la moyenne : la valeur temps est positive. Pour un payoff concave, elle est négative. [Déf. 13]

Pour le call de l'exemple, elle vaut $9{,}93-3{,}92=6{,}00$ : le prix du put de même strike. Ce n'est pas un hasard : quand le prix forward dépasse le strike, la parité call-put fait de la valeur temps du call exactement le prix du put. [ajout]

![Le prix du call en fonction du prix de l'action, au-dessus de sa valeur intrinsèque, coudée en 96,08 : l'écart vertical est la valeur temps, la plus grande près du coude, et elle vaut 6,00 quand l'action est à 100.](figures/valeur-temps.svg) [ajout]

## Le chemin jusqu'ici
fpp/valeur-intrinseque donne la partie du prix qui existerait sans aléa, fpp/formule-black-scholes le prix entier ; la valeur temps est leur écart. [ajout]

Les deux reposent sur le même socle. fpp/option et fpp/payoff fournissent le paiement coudé ; fpp/modele-black-scholes sa loi, construite par fpp/probabilite-risque-neutre et fpp/tendance-risque-neutre autour de fpp/prix-forward, avec fpp/taux-de-dividende et fpp/dividendes-intermediaires ; fpp/volatilite, étalée par fpp/echelonnement-de-la-variance, en donne la dispersion, et fpp/transformee-de-laplace-gaussienne la correction de moyenne. [ajout]

L'actualisation vient de fpp/valeur-actuelle-nette et de fpp/zero-coupon dans la convention de fpp/capitalisation ; le prix forward, de fpp/cash-and-carry sous fpp/absence-d-arbitrage. [ajout]

## Exemple minimal
Le call de strike 100 à un an vaut 9,93 pour une valeur intrinsèque de 3,92 : sa valeur temps vaut 6,00. [ajout]

## Geste de calcul type
Retrancher la valeur intrinsèque du prix ; la valeur temps est maximale quand le prix forward est proche du strike, et s'efface loin de lui, d'un côté comme de l'autre. [Déf. 13, ajout]

## Cesse d'être valide quand
La règle de signe tient pour un payoff convexe ou concave partout ; un payoff mixte, convexe par endroits et concave ailleurs, peut avoir une valeur temps de l'un ou l'autre signe. Le poly s'arrête sur un « à suivre ». [Déf. 13, ajout]

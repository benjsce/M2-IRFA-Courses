---
id: fpp/combinaison-d-options
nom: Combinaison d'options
type: notion
statut: source
construite_a_partir_de:
- fpp/option
alias:
- stratégie optionnelle
- option strategy
- call spread
- straddle
- strangle
- butterfly
- option digitale
- return enhancement
refs:
- §9.1
- §6.3
- §9.3
- exo. 15
---

## Ce que c'est
Un portefeuille de calls et de puts, de strikes éventuellement différents, dont le payoff, somme des leurs, prend une forme choisie à l'avance. [§9.1, §6.3]

## Forme
$$\text{straddle : }(S_T-K)^++(K-S_T)^+=|S_T-K|,\qquad\text{call spread : }(S_T-K_1)^+-(S_T-K_2)^+$$ [§9.1, ajout]

## Ce que les symboles modélisent
$K$, $K_1<K_2$ sont des strikes ; $S_T$ le prix final. Le straddle paie l'écart au strike dans les deux sens ; le call spread paie la hausse entre deux strikes et plafonne au-delà. [§9.1, ajout]

## Ce qui la définit
Ce qui est **connu** : la forme de paiement qu'on veut. Ce qu'on **cherche** : les options qui la produisent. Le poly cite l'écart de calls (call spread), l'option digitale, qui en est la limite quand les deux strikes se rejoignent, et le straddle ; le livre d'exercices ajoute le strangle, deux strikes écartés, et le papillon (butterfly). [§9.1, exo. 15]

Chaque forme exprime une vue : le straddle gagne si l'action bouge beaucoup, dans un sens ou dans l'autre, et c'est donc un pari sur la volatilité. Le poly range aussi sous les usages des options l'amélioration du rendement : vendre des calls sur une action détenue, ou vendre des puts, pour encaisser une prime en renonçant à une partie de la hausse ou en acceptant d'acheter plus bas. [exo. 15, §9.3]

![Quatre payoffs construits avec des options : l'écart de calls (S − K₁)⁺ − (S − K₂)⁺, plafonné ; le straddle |S − K| ; le strangle (K₁ − S)⁺ + (S − K₂)⁺, en V à fond plat ; le papillon (S − K₁)⁺ − 2(S − K₂)⁺ + (S − K₃)⁺, qui ne paie qu'autour de K₂.](figures/combinaison-d-options.svg) [§9.1, exo. 15, ajout]

## Le chemin jusqu'ici
fpp/option fournit les briques, calls et puts ; fpp/payoff dit qu'un paiement se décrit par sa forme, et qu'une somme de positions a pour payoff la somme de leurs payoffs. [ajout]

## Exemple minimal
Le straddle de strike 100 à un an, sur l'action à 100, coûte $9{,}93+6{,}00=15{,}93$ et paie $|S_T-100|$. [ajout]

## Geste de calcul type
Décomposer la forme voulue en calls et en puts, puis additionner leurs prix, parce que le prix d'une somme est la somme des prix. [ajout]

## Cesse d'être valide quand
L'option digitale n'est la limite que d'une infinité d'écarts de calls de plus en plus serrés. Et une combinaison qui vend des options expose à des pertes que ses gains plafonnés ne compensent pas. [§9.1, §9.3, ajout]

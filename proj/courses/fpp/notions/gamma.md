---
id: fpp/gamma
nom: Gamma
symbole: '$\gamma$, $n$'
type: notion
statut: source
cas_de: fpp/grecque
valeur: le prix du sous-jacent, deux fois
construite_a_partir_de:
- fpp/valeur-temps
alias:
- convexité de l'option
refs:
- §8.2
- §8.1
---

## Ce que c'est
La dérivée seconde du prix de l'option par rapport au prix de l'action, qui dit de combien le delta change quand l'action bouge. [§8.2]

## Forme
$$\gamma=\frac{\partial^2C}{\partial S^2}=\frac{n(d_1)}{S\,\sigma\sqrt\tau}$$ [§8.2, ajout]

## Ce que les symboles modélisent
$\gamma$ se lit en actions par euro de mouvement de l'action. $n$ est la densité de la loi normale centrée réduite, la dérivée de $N$. Le poly écrit $\gamma=n(d_1)$ ; il manque le dénominateur $S\,\sigma\sqrt\tau$, sans lequel le nombre n'a pas la bonne unité. [§8.2, ajout]

## Ce qui la définit
Ce qui est **connu** : le delta et sa pente. Ce qu'on **cherche** : de combien il faudra ajuster la couverture quand l'action aura bougé. Le gamma est positif pour qui détient une option : son prix est convexe. C'est la même convexité qui rend la valeur temps positive. [§8.2, §8.1, ajout]

Le tableau du poly le montre : la dérivée seconde de la valeur intrinsèque est nulle partout sauf au strike, où elle est infinie ; celles de la valeur temps et du prix montent puis redescendent, maximales près de la monnaie. [§8.2]

![Le delta du call, N(d₁), en fonction du prix de l'action, une courbe en S, et sa tangente en S₀ : la pente est le gamma, γ = ∂²C/∂S² = n(d₁) / (S σ √τ).](figures/gamma.svg) [ajout]

## Le chemin jusqu'ici
Les grecques dérivent le prix que calcule fpp/formule-black-scholes, et fpp/valeur-temps les décompose, avec fpp/valeur-intrinseque, en ce qui vient de l'aléa et ce qui n'en vient pas. [ajout]

Le gamma dérive une seconde fois : il mesure la courbure du prix, donc la vitesse à laquelle le delta change. [ajout]

Le reste du socle est celui de la formule. fpp/option et fpp/payoff décrivent le paiement ; fpp/modele-black-scholes sa loi, que fpp/probabilite-risque-neutre et fpp/tendance-risque-neutre centrent sur fpp/prix-forward, net du fpp/taux-de-dividende et des fpp/dividendes-intermediaires ; fpp/volatilite, fpp/echelonnement-de-la-variance et fpp/transformee-de-laplace-gaussienne en fixent la forme. L'actualisation vient de fpp/valeur-actuelle-nette et de fpp/zero-coupon, dans la convention de fpp/capitalisation, et le prix forward de fpp/cash-and-carry sous fpp/absence-d-arbitrage. [ajout]

## Exemple minimal
Le call de strike 100 à un an, l'action à 100 : $\gamma=0{,}019$ ; si l'action passe à 101, le delta passe de 0,618 à environ 0,637. [ajout]

## Geste de calcul type
Le vendeur de 100 calls, couvert avec 61,8 actions, en rachète 1,9 quand l'action gagne 1. Et un portefeuille couvert en delta gagne environ $\tfrac12\gamma\,\Delta S^2$ par option détenue quand l'action bouge. [ajout]

## Cesse d'être valide quand
Le gamma est maximal près de la monnaie et près de l'échéance : là, la couverture doit être ajustée si souvent qu'un ajustement discret laisse un risque important. [§8.2, ajout]

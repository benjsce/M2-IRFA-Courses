---
id: fpp/rho
nom: Rhô
symbole: $\rho$
type: notion
statut: source
cas_de: fpp/grecque
valeur: le taux d'intérêt
construite_a_partir_de:
- fpp/valeur-temps
alias:
- rho
refs:
- §8.2
---

## Ce que c'est
La dérivée du prix de l'option par rapport au taux d'intérêt, positive pour un call et négative pour un put. [§8.2]

## Forme
$$\rho=\frac{\partial C}{\partial r}=K\,\tau\,e^{-r\tau}N(d_2)$$ [§8.2, ajout]

## Ce que les symboles modélisent
$\rho$ se lit en euros par unité de taux : pour un point de taux, on le divise par 100. Ce n'est pas le coefficient de corrélation, que d'autres cours notent aussi $\rho$. [§8.2, ajout]

## Ce qui la définit
Ce qui est **connu** : le prix de l'option pour le taux du jour. Ce qu'on **cherche** : son effet sur le prix. Une hausse du taux relève le prix forward de l'action, donc la valeur intrinsèque du call, et réduit la valeur actuelle du strike à payer : le prix du call monte. Le poly note que la valeur temps, elle, baisse ; pour le put, tout baisse. [§8.2]

![Le prix du call C(r) en fonction du taux d'intérêt, et sa tangente en r₀ : la pente est le rhô, ρ = ∂C/∂r = K τ e^(−rτ) N(d₂).](figures/rho.svg) [ajout]

## Le chemin jusqu'ici
Les grecques dérivent le prix que calcule fpp/formule-black-scholes, et fpp/valeur-temps les décompose, avec fpp/valeur-intrinseque, en ce qui vient de l'aléa et ce qui n'en vient pas. [ajout]

Le rhô dérive par rapport au taux, qui entre dans la formule par le prix forward et par l'actualisation du strike. [ajout]

Le reste du socle est celui de la formule. fpp/option et fpp/payoff décrivent le paiement ; fpp/modele-black-scholes sa loi, que fpp/probabilite-risque-neutre et fpp/tendance-risque-neutre centrent sur fpp/prix-forward, net du fpp/taux-de-dividende et des fpp/dividendes-intermediaires ; fpp/volatilite, fpp/echelonnement-de-la-variance et fpp/transformee-de-laplace-gaussienne en fixent la forme. L'actualisation vient de fpp/valeur-actuelle-nette et de fpp/zero-coupon, dans la convention de fpp/capitalisation, et le prix forward de fpp/cash-and-carry sous fpp/absence-d-arbitrage. [ajout]

## Exemple minimal
Le call de strike 100 à un an, l'action à 100 : $\rho=51{,}9$ ; si le taux passe de 4 % à 5 %, le call gagne environ 0,52. [ajout]

## Geste de calcul type
$\Delta C\approx\rho\,\Delta r=51{,}9\times0{,}01$ pour un point de taux. [ajout]

## Cesse d'être valide quand
Le modèle suppose le taux constant : comme le véga, le rhô mesure la sensibilité à un paramètre que le modèle tient pour fixe. [§5.4, ajout]

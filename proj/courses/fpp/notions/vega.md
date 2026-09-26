---
id: fpp/vega
nom: Véga
symbole: $\mathcal{V}$
type: notion
statut: source
cas_de: fpp/grecque
valeur: la volatilité
construite_a_partir_de:
- fpp/valeur-temps
alias:
- vega
refs:
- §8.2
---

## Ce que c'est
La dérivée du prix de l'option par rapport à la volatilité, positive pour un call comme pour un put. [§8.2]

## Forme
$$\mathcal V=\frac{\partial C}{\partial\sigma}=S\,n(d_1)\sqrt\tau$$ [§8.2, ajout]

## Ce que les symboles modélisent
$\mathcal{V}$ se lit en euros par unité de volatilité : pour un point de volatilité, on le divise par 100. Le poly écrit $S\,N(d_1)\sqrt\tau$, avec la fonction de répartition ; c'est la densité $n(d_1)$ qui convient. [§8.2, ajout]

## Ce qui la définit
Ce qui est **connu** : le prix de l'option pour la volatilité supposée. Ce qu'on **cherche** : de combien il change si l'on s'est trompé de volatilité. La valeur intrinsèque ne dépend pas de la volatilité : tout le véga vient de la valeur temps, et il est positif pour le call comme pour le put. [§8.2]

C'est la grecque de celui qui parie sur la volatilité : acheter un straddle, c'est acheter du véga. [exo. 15, ajout]

![Le prix du call en fonction de la volatilité, et sa tangente à 20 % : la pente, 38,1, est le véga, soit 0,38 par point de volatilité.](figures/vega.svg) [ajout]

## Le chemin jusqu'ici
Les grecques dérivent le prix que calcule fpp/formule-black-scholes, et fpp/valeur-temps les décompose, avec fpp/valeur-intrinseque, en ce qui vient de l'aléa et ce qui n'en vient pas. [ajout]

Le véga dérive par rapport à la seule entrée de la formule qui ne s'observe pas : la volatilité. [ajout]

Le reste du socle est celui de la formule. fpp/option et fpp/payoff décrivent le paiement ; fpp/modele-black-scholes sa loi, que fpp/probabilite-risque-neutre et fpp/tendance-risque-neutre centrent sur fpp/prix-forward, net du fpp/taux-de-dividende et des fpp/dividendes-intermediaires ; fpp/volatilite, fpp/echelonnement-de-la-variance et fpp/transformee-de-laplace-gaussienne en fixent la forme. L'actualisation vient de fpp/valeur-actuelle-nette et de fpp/zero-coupon, dans la convention de fpp/capitalisation, et le prix forward de fpp/cash-and-carry sous fpp/absence-d-arbitrage. [ajout]

## Exemple minimal
Le call de strike 100 à un an, l'action à 100 : $\mathcal V=38{,}1$ ; si la volatilité passe de 20 % à 21 %, le call gagne environ 0,38. [ajout]

## Geste de calcul type
$\Delta C\approx\mathcal V\,\Delta\sigma=38{,}1\times0{,}01$ pour un point. Le straddle de même strike a un véga double, $2\times38{,}1$, puisque le put a le même que le call. [ajout]

## Cesse d'être valide quand
Le modèle de Black et Scholes suppose la volatilité constante : le véga est la sensibilité à un paramètre que le modèle lui-même tient pour fixe. [§5.4, ajout]

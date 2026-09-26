---
id: fpp/grecque
nom: Grecque
symbole: $\tau$
type: abstraite
statut: source
cas_de: fpp/couverture
parametre: la variable par rapport à laquelle on dérive le prix de l'option
construite_a_partir_de:
- fpp/valeur-temps
alias:
- greeks
- grecques
- sensibilité
- sensitivities
refs:
- §8.2
- §8.1
- §8.3
---

## Ce que c'est
La dérivée du prix d'une option par rapport à l'un de ses paramètres, qui dit de combien le prix bouge quand ce paramètre bouge seul. [§8.2]

## Forme
$$\delta=\frac{\partial P}{\partial S},\quad \gamma=\frac{\partial^2P}{\partial S^2},\quad \mathcal V=\frac{\partial P}{\partial\sigma},\quad \Theta=\frac{\partial P}{\partial t},\quad \rho=\frac{\partial P}{\partial r},\qquad \frac{\partial P}{\partial K}=-e^{-r\tau}N(d_2)\ \text{(call)}$$ [§8.2]

## Ce que les symboles modélisent
Dans ce tableau, le poly note $P$ le prix de l'option, qu'elle soit un call ou un put, et non le zéro-coupon. $\tau$, égal à $T-t$, est la durée qui reste jusqu'à l'échéance ; elle diminue quand le temps $t$ avance. [§8.2]

## Ce que les membres partagent
Ce qui est **connu** : la formule du prix. Ce qu'on **cherche** : de combien il change quand un seul paramètre change, les autres restant fixes. Chaque grecque est une dérivée partielle de la même formule, et le poly résume leurs effets sur la valeur intrinsèque, la valeur temps et le prix : [§8.2]

| grecque | call : IV | call : TV | call : prix | put : IV | put : TV | put : prix |
|---|---|---|---|---|---|---|
| delta, $S$ | ↗ | ↗↘ | ↗ | ↘ | ↗↘ | ↘ |
| gamma, $S$ deux fois | - ↑ - | ↗↘ | ↗↘ | - ↑ - | ↗↘ | ↗↘ |
| véga, $\sigma$ | − | ↗ | ↗ | − | ↗ | ↗ |
| thêta, $t$ | ↘ | ↘\* | ↘ | ↗ | ↘\* | ↗↘ |
| rhô, $r$ | ↗ | ↘ | ↗ | ↘ | ↘ | ↘ |
| sans nom, $K$ | ↘ | ? | ↘ | ? | ↘ | ↘ |
[§8.2]

Une flèche dit le sens de la variation quand le paramètre augmente ; ↗↘ veut dire qu'elle monte puis descend ; - ↑ - que la dérivée seconde de la valeur intrinsèque est nulle sauf au strike, où elle est infinie ; l'astérisque, « presque toujours ». Pour le put, la dernière ligne du poly est douteuse : une hausse du strike augmente la valeur intrinsèque et le prix d'un put, puisque $\partial P/\partial K=e^{-r\tau}N(-d_2)>0$. [§8.2, ajout]

## Pourquoi ce niveau existe
Un teneur de position neutralise un risque par grecque : le mouvement de l'action par le delta, celui du delta par le gamma, celui de la volatilité par le véga. Le même geste, dériver, lire le signe, se couvrir, vaut pour chacune, et le tableau se lit colonne par colonne pour voir ce qui vient de la valeur intrinsèque et ce qui vient de la valeur temps. [§8, ajout]

## Le chemin jusqu'ici
Les grecques dérivent le prix que calcule fpp/formule-black-scholes, et fpp/valeur-temps les décompose, avec fpp/valeur-intrinseque, en ce qui vient de l'aléa et ce qui n'en vient pas. [ajout]

Le reste du socle est celui de la formule. fpp/option et fpp/payoff décrivent le paiement ; fpp/modele-black-scholes sa loi, que fpp/probabilite-risque-neutre et fpp/tendance-risque-neutre centrent sur fpp/prix-forward, net du fpp/taux-de-dividende et des fpp/dividendes-intermediaires ; fpp/volatilite, fpp/echelonnement-de-la-variance et fpp/transformee-de-laplace-gaussienne en fixent la forme. L'actualisation vient de fpp/valeur-actuelle-nette et de fpp/zero-coupon, dans la convention de fpp/capitalisation, et le prix forward de fpp/cash-and-carry sous fpp/absence-d-arbitrage. [ajout]

## Exemple minimal
Pour le call de strike 100 à un an, sur l'action à 100, avec $r=4\,\%$ et $\sigma=20\,\%$ : $\delta=0{,}618$, $\gamma=0{,}019$, $\mathcal V=38{,}1$, $\Theta=-5{,}89$ par an, $\rho=51{,}9$. [ajout]

## Geste de calcul type
Approcher la variation du prix par la somme des effets : $\Delta P\approx\delta\,\Delta S+\tfrac12\gamma\,\Delta S^2+\mathcal V\,\Delta\sigma+\Theta\,\Delta t+\rho\,\Delta r$. [ajout]

## Cesse d'être valide quand
Ce sont des dérivées : elles ne valent que pour de petits mouvements, et elles dépendent du modèle qui a donné la formule. Les sections 8.1 et 8.3 du poly n'ont encore que leurs titres. [§8.2, §8.1, §8.3]

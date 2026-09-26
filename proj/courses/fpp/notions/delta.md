---
id: fpp/delta
nom: Delta
symbole: $\delta$
type: notion
statut: source
cas_de: fpp/grecque
valeur: le prix du sous-jacent
construite_a_partir_de:
- fpp/valeur-temps
alias:
- delta de couverture
- hedge ratio
refs:
- §8.2
- §7.1
---

## Ce que c'est
La dérivée du prix de l'option par rapport au prix de l'action, qui donne le nombre d'actions à tenir pour couvrir l'option. [§8.2, §7.1]

## Forme
$$\delta=\frac{\partial C}{\partial S}=N(d_1)\ \text{pour un call},\qquad \delta=N(d_1)-1\ \text{pour un put}$$ [§8.2, ajout]

## Ce que les symboles modélisent
$\delta$ est un nombre d'actions par option : entre 0 et 1 pour un call, entre −1 et 0 pour un put. Au chapitre 7, le poly note aussi $\delta$ la quantité d'actions du portefeuille de couverture, qui vaut moins le delta de l'option qu'on détient. [§8.2, §7.1]

## Ce qui la définit
Ce qui est **connu** : le prix du call en fonction du prix de l'action. Ce qu'on **cherche** : combien d'actions compensent un petit mouvement de l'action. La réponse est la pente de ce prix : 0,618 action par call à la monnaie de l'exemple. [§8.2, ajout]

Quand l'action monte, le delta du call monte aussi : sa valeur intrinsèque augmente, sa valeur temps monte puis redescend, son prix augmente ; c'est l'inverse pour le put. [§8.2]

![Le prix du call en fonction du prix de l'action, et sa tangente en 100 : la pente, 0,618, est le delta.](figures/delta.svg) [ajout]

## Le chemin jusqu'ici
Les grecques dérivent le prix que calcule fpp/formule-black-scholes, et fpp/valeur-temps les décompose, avec fpp/valeur-intrinseque, en ce qui vient de l'aléa et ce qui n'en vient pas. [ajout]

Le delta est la première d'entre elles, la pente du prix le long du prix de l'action. [ajout]

Le reste du socle est celui de la formule. fpp/option et fpp/payoff décrivent le paiement ; fpp/modele-black-scholes sa loi, que fpp/probabilite-risque-neutre et fpp/tendance-risque-neutre centrent sur fpp/prix-forward, net du fpp/taux-de-dividende et des fpp/dividendes-intermediaires ; fpp/volatilite, fpp/echelonnement-de-la-variance et fpp/transformee-de-laplace-gaussienne en fixent la forme. L'actualisation vient de fpp/valeur-actuelle-nette et de fpp/zero-coupon, dans la convention de fpp/capitalisation, et le prix forward de fpp/cash-and-carry sous fpp/absence-d-arbitrage. [ajout]

## Exemple minimal
Le call de strike 100 à un an, l'action à 100, $r=4\,\%$, $\sigma=20\,\%$ : $\delta=0{,}618$ ; le put de même strike a un delta de $-0{,}382$. [ajout]

## Geste de calcul type
$\Delta C\approx\delta\,\Delta S$ : si l'action passe de 100 à 101, le call gagne environ 0,62. Le vendeur de 100 calls tient 61,8 actions. [ajout]

## Cesse d'être valide quand
Le delta change avec le prix de l'action, à une vitesse que mesure le gamma : une couverture en delta doit être ajustée à mesure que l'action bouge. [§8.2]

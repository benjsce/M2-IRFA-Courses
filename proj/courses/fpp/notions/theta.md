---
id: fpp/theta
nom: Thêta
symbole: $\Theta$
type: notion
statut: source
cas_de: fpp/grecque
valeur: le temps
construite_a_partir_de:
- fpp/valeur-temps
alias:
- theta
- érosion du temps
- time decay
refs:
- §8.2
- §7.1
---

## Ce que c'est
La dérivée du prix de l'option par rapport au temps qui passe, presque toujours négative : l'option perd de la valeur à mesure que l'échéance approche. [§8.2]

## Forme
$$\Theta=\frac{\partial C}{\partial t}=-\frac{S\,n(d_1)\,\sigma}{2\sqrt\tau}-r\,K\,e^{-r\tau}N(d_2)$$ [§8.2, ajout]

## Ce que les symboles modélisent
$\Theta$ se lit en euros par an ; divisé par 256, il donne la perte d'un jour de bourse. Le temps $t$ avance quand la durée restante $\tau$ diminue. [§8.2, Rem. 1, ajout]

## Ce qui la définit
Ce qui est **connu** : le prix de l'option aujourd'hui. Ce qu'on **cherche** : ce qu'elle perd en un jour si rien d'autre ne bouge. C'est la valeur temps qui s'use : l'aléa qu'il reste à courir diminue. Le poly note que la valeur temps baisse « presque toujours » avec le temps. [§8.2]

Le thêta paie le gamma. Dans l'équation de Black et Scholes, $\Theta+r\,S\,\delta+\tfrac12\sigma^2S^2\gamma=rC$ : ce que l'option perd avec le temps compense ce que sa convexité rapporte quand l'action bouge. [§7.1, ajout]

![Le prix du call à la monnaie en fonction du temps restant, l'action restant à 100 : il fond de 9,93 à un an jusqu'à 0 à l'échéance, de plus en plus vite ; la pente à un an est le thêta.](figures/theta.svg) [ajout]

## Le chemin jusqu'ici
Les grecques dérivent le prix que calcule fpp/formule-black-scholes, et fpp/valeur-temps les décompose, avec fpp/valeur-intrinseque, en ce qui vient de l'aléa et ce qui n'en vient pas. [ajout]

Le thêta dérive par rapport au temps : il dit ce que coûte, jour après jour, de garder l'option sans que rien ne bouge. [ajout]

Le reste du socle est celui de la formule. fpp/option et fpp/payoff décrivent le paiement ; fpp/modele-black-scholes sa loi, que fpp/probabilite-risque-neutre et fpp/tendance-risque-neutre centrent sur fpp/prix-forward, net du fpp/taux-de-dividende et des fpp/dividendes-intermediaires ; fpp/volatilite, fpp/echelonnement-de-la-variance et fpp/transformee-de-laplace-gaussienne en fixent la forme. L'actualisation vient de fpp/valeur-actuelle-nette et de fpp/zero-coupon, dans la convention de fpp/capitalisation, et le prix forward de fpp/cash-and-carry sous fpp/absence-d-arbitrage. [ajout]

## Exemple minimal
Le call de strike 100 à un an, l'action à 100 : $\Theta=-5{,}89$ par an, soit environ $-0{,}023$ par jour de bourse. [ajout]

## Geste de calcul type
Perte d'une journée, toutes choses égales : $\Theta/256=-5{,}89/256\approx-0{,}023$. Vérifier l'équation de Black et Scholes : $-5{,}89+2{,}47+3{,}81=0{,}40=4\,\%\times9{,}93$. [§7.1, ajout]

## Cesse d'être valide quand
« Presque toujours » : un put très dans la monnaie peut gagner de la valeur avec le temps, parce que le strike qu'il fera recevoir s'actualise moins ; le poly marque ce cas d'une double flèche. [§8.2]

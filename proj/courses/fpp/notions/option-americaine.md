---
id: fpp/option-americaine
nom: Option américaine
type: notion
statut: source
construite_a_partir_de:
- fpp/valeur-temps
alias:
- American option
- exercice anticipé
- early exercise
refs:
- Déf. 10
- exo. 9
---

## Ce que c'est
Une option qu'on peut exercer à tout moment jusqu'à sa maturité, et non seulement à la maturité comme une option européenne. [Déf. 10]

## Ce qui la définit
La question est de savoir quand ce droit supplémentaire sert. Ce qui est **connu** : ce que rapporte un exercice immédiat, $S_t-K$ pour un call. Ce qu'on **compare** : la valeur de l'option si on la garde. [exo. 9]

Pour un call sur une action sans dividende, garder l'option vaut toujours plus. Grâce à sa valeur temps positive, le call européen vaut plus que sa valeur intrinsèque, $S_t-K\,e^{-r(T-t)}$, elle-même supérieure à $S_t-K$ quand les taux sont positifs. Revendre l'option rapporte plus que l'exercer, et le call américain vaut le call européen. [exo. 9]

Pour un call sur une devise dont le taux étranger est positif, le livre d'exercices montre que l'exercice anticipé peut être préférable : ce taux joue le rôle d'un dividende, que l'on ne touche qu'en détenant la devise. [exo. 9]

![À gauche, un call sur l'action sans dividende : son prix reste partout au-dessus du gain d'un exercice immédiat, S − K. À droite, un call sur une devise dont le taux dépasse le taux local : très dans la monnaie, son prix passe sous X − K, et exercer tout de suite vaut mieux.](figures/option-americaine.svg) [ajout]

## Le chemin jusqu'ici
fpp/valeur-temps donne l'argument : une option convexe vaut plus que sa valeur intrinsèque, calculée par fpp/valeur-intrinseque sur le prix forward. fpp/formule-black-scholes donne les prix de la figure, dans le fpp/modele-black-scholes où fpp/probabilite-risque-neutre et fpp/tendance-risque-neutre fixent la moyenne au prix de fpp/prix-forward, abaissé par le fpp/taux-de-dividende, limite continue des fpp/dividendes-intermediaires. C'est ce taux, pour une devise le taux étranger, qui peut rendre l'exercice anticipé intéressant. [ajout]

fpp/option et fpp/payoff décrivent le droit et son paiement ; fpp/volatilite, fpp/echelonnement-de-la-variance et fpp/transformee-de-laplace-gaussienne la loi du sous-jacent ; fpp/valeur-actuelle-nette, fpp/zero-coupon et fpp/capitalisation l'actualisation, et fpp/cash-and-carry, sous fpp/absence-d-arbitrage, le portage qui fixe le prix forward. [ajout]

## Exemple minimal
Un call américain de strike 100 à un an sur l'action à 100, sans dividende, vaut 9,93, comme le call européen : on ne l'exercera jamais avant l'échéance. [ajout]

## Cesse d'être valide quand
Le cours ne donne pas de formule pour une option américaine dès que l'exercice anticipé peut servir, dividendes ou devises : l'argument dit seulement quand il ne sert pas. [Déf. 10, exo. 9]

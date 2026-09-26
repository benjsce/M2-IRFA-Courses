---
id: fpp/duration
nom: Duration
symbole: $P(t,r)$
type: notion
statut: source
construite_a_partir_de:
- fpp/taux-zero-coupon
alias:
- sensibilité au taux
refs:
- Déf. 5
---

## Ce que c'est
La sensibilité relative du prix d'un zéro-coupon à son taux, égale à moins sa durée : une hausse d'un point de taux fait perdre environ t pour cent du prix. [Déf. 5]

## Forme
$$\frac{\partial P(t,r)}{\partial r}=-t\,P(t,r)\iff\frac{\partial P(t,r)}{P(t,r)\,\partial r}=-t$$ [Déf. 5]

## Ce que les symboles modélisent
$P(t,r)$, qui vaut $e^{-rt}$, est ici une fonction d'une durée $t$ et d'un taux $r$, alors que $P(t,T)$ prenait deux dates : $t$ n'est plus la date où l'on regarde mais le temps qui reste jusqu'au paiement. [Déf. 5, ajout]

## Ce qui la définit
On connaît le prix et la durée ; on cherche de combien le prix bouge quand le taux bouge. La variation relative vaut $-t$ fois celle du taux : une variation instantanée du taux pèse sur toute la vie de l'obligation, et d'autant plus que cette vie est longue. [Déf. 5]

![Le prix d'un zéro-coupon à deux ans en fonction de son taux, et sa tangente à 5 % : la pente vaut −2 × 0,9048.](figures/duration.svg) [ajout]

## Le chemin jusqu'ici
fpp/taux-zero-coupon écrit le prix sous la forme $e^{-R(T-t)}$, où le taux et la durée apparaissent ensemble dans l'exposant ; dériver par rapport au taux fait descendre la durée. fpp/zero-coupon fournit le titre étudié et fpp/capitalisation la convention continue qui rend ce calcul si simple. [ajout]

## Exemple minimal
Un zéro-coupon à deux ans à 5 % vaut 0,9048 ; sa duration est 2. [ajout]

## Geste de calcul type
$\Delta P\approx-t\,P\,\Delta r$ : un point de base de hausse, $0{,}01\,\%$, fait perdre $2\times0{,}9048\times0{,}0001\approx0{,}00018$, soit 0,02 % du prix. [Déf. 5, ajout]

## Cesse d'être valide quand
C'est une tangente : pour une grande variation de taux, la courbure du prix compte. Le poly la définit pour un zéro-coupon ; pour une obligation à coupons, chaque flux a sa propre durée et la sensibilité les mélange. [Déf. 5, ajout]

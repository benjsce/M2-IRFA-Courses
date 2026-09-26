---
id: fpp/formule-black-scholes
nom: Formule de Black et Scholes
symbole: '$C$, $P$, $N$, $d_1$, $d_2$'
type: notion
statut: source
construite_a_partir_de:
- fpp/modele-black-scholes
- fpp/option
alias:
- Black-Scholes formula
- formule B&S
- formule de Black-Scholes
refs:
- §6.4
- éq. 3
- éq. 4
- éq. 5
- éq. 6
- éq. 7
- éq. 8
- éq. 9
- éq. 10
- exo. 8
---

## Ce que c'est
Le prix d'un call ou d'un put européen dans le modèle de Black et Scholes, écrit avec la fonction de répartition de la loi normale. [§6.4]

## Forme
$$C=S_0\,N(d_1)-K\,e^{-rT}N(d_2),\qquad P=K\,e^{-rT}N(-d_2)-S_0\,N(-d_1)$$ [éq. 3, éq. 4]

$$d_1=\frac{\ln(S_0/K)+\left(r+\frac{\sigma^2}{2}\right)T}{\sigma\sqrt T},\qquad d_2=d_1-\sigma\sqrt T$$ [éq. 5, éq. 6]

Avec un dividende continu $q$, $S_0$ devient $S_0\,e^{-qT}$ devant $N$, et $r$ devient $r-q$ dans $d_1$. [éq. 7, éq. 8, éq. 9, éq. 10]

## Ce que les symboles modélisent
$C$ et $P$ sont les prix du call et du put ; ce $P$ n'est pas le zéro-coupon $P(0,T)$, ni le $C$ celui de la capitalisation. $N$ prend un nombre et rend la probabilité qu'une gaussienne centrée réduite tombe en dessous. $d_1$ et $d_2$ sont deux seuils sans unité, qui ne sont pas des dividendes. [éq. 3, éq. 5]

## Retrouver la formule
![Le payoff du call décomposé : recevoir l'action si elle finit au-dessus de 100, moins recevoir 100 dans le même cas. Aujourd'hui, le premier vaut 61,79, le second 51,87, et le call leur différence, 9,93.](figures/formule-black-scholes.svg) [ajout]

Le prix du call est son espérance actualisée sous $\mathbb Q$ : $C=e^{-rT}E^{\mathbb Q}\big((S_T-K)^+\big)$. Ce payoff se coupe en deux : recevoir l'action quand $S_T>K$, moins recevoir $K$ dans le même cas. [Prop. 6, ajout]

Le second morceau vaut $K\,e^{-rT}\,\mathbb Q(S_T>K)$. Le log-prix suit une loi normale de moyenne $\ln S_0+rT-\sigma^2T/2$ et d'écart type $\sigma\sqrt T$ ; la probabilité de finir au-dessus de $K$ vaut donc $N(d_2)$. Avec l'action à 100, un strike de 100, $r=4\,\%$, $\sigma=20\,\%$ et un an : $d_2=0{,}10$, $N(d_2)=0{,}540$, et ce morceau vaut $96{,}08\times0{,}540=51{,}87$. [§5.4, ajout]

Le premier morceau, $e^{-rT}E^{\mathbb Q}(S_T\,\mathbf 1_{S_T>K})$, se calcule avec la même intégrale gaussienne que la transformée de Laplace ; le facteur $e^{\sigma^2T/2}$ décale le seuil de $\sigma\sqrt T$, de $d_2$ à $d_1=0{,}30$, et ce morceau vaut $100\times N(0{,}30)=61{,}79$. [Th. 1, ajout]

Le call vaut $61{,}79-51{,}87=9{,}93$ : [ajout]

$$C=S_0\,N(d_1)-K\,e^{-rT}N(d_2)$$ [éq. 3]

## Ce qui la définit
Ce qui est **connu** : le prix de l'action, le strike, la maturité, le taux, et le dividende s'il y en a. Ce qui ne s'observe pas : la volatilité, seule entrée qu'il faut estimer. La formule bouche le trou entre ces données et la prime. [§6.4, ajout]

$N(d_2)$ est la probabilité risque-neutre que le call soit exercé ; $S_0\,N(d_1)$ la valeur de l'action reçue dans ce cas. [ajout]

## Le chemin jusqu'ici
fpp/modele-black-scholes donne la loi du prix final sous $\mathbb Q$ ; fpp/option le payoff à intégrer contre elle, coudé comme le décrit fpp/payoff. Il ne reste qu'un calcul d'intégrale. [ajout]

Ce modèle réunit ce que le cours a construit : fpp/probabilite-risque-neutre et fpp/tendance-risque-neutre fixent la moyenne au prix de fpp/prix-forward, diminué du fpp/taux-de-dividende et, avant lui, des fpp/dividendes-intermediaires ; fpp/volatilite et fpp/echelonnement-de-la-variance fixent la dispersion ; fpp/transformee-de-laplace-gaussienne corrige la moyenne du logarithme. [ajout]

L'actualisation vient de fpp/valeur-actuelle-nette et de fpp/zero-coupon, en convention continue de fpp/capitalisation ; le prix forward, de fpp/cash-and-carry sous fpp/absence-d-arbitrage. [ajout]

## Exemple minimal
L'action à 100, un strike de 100, un an, $r=4\,\%$, $\sigma=20\,\%$ : le call vaut 9,93 et le put 6,00. [ajout]

## Geste de calcul type
Calculer $d_1=\frac{0+(0{,}04+0{,}02)}{0{,}2}=0{,}30$ et $d_2=0{,}10$, lire $N(0{,}30)=0{,}618$ et $N(0{,}10)=0{,}540$, assembler. Le livre d'exercices traite un dividende fixe en retirant sa valeur actuelle au prix de l'action : 4,83 sans dividende, 4,18 avec. [éq. 3, exo. 8]

## Cesse d'être valide quand
La volatilité et le taux sont supposés constants, l'option européenne, les dividendes continus ; tout écart à ces hypothèses se paie par un ajustement ou par un autre modèle. [§6.4, §5.4]

---
id: fpp/obligation-in-fine
nom: Obligation in fine
symbole: '$B(r^*,r)$, $r^*$'
type: notion
statut: source
construite_a_partir_de:
- fpp/valeur-actuelle-nette
alias:
- bullet bond
- obligation à coupons
- au pair
- at par
refs:
- Ex. 1
- éq. 1
- éq. 2
---

## Ce que c'est
Une obligation qui verse chaque année un coupon au taux r* et rembourse tout le capital à la fin. [Ex. 1]

## Forme
$$B(r^*,r)=r^*\sum_{i=1}^{n}\frac{1}{(1+r)^i}+\frac{1}{(1+r)^n}=\frac{r^*}{r}\Big(1-\frac{1}{(1+r)^n}\Big)+\frac{1}{(1+r)^n}$$ [éq. 1, éq. 2]

## Ce que les symboles modélisent
$r^*$ est le taux du coupon, fixé à l'émission ; $r$ le taux du marché le jour où l'on évalue, ici actuariel et le même pour toutes les dates ; $n$ le nombre d'années restantes. $B(r^*,r)$ est le prix pour 1 de nominal. [Ex. 1]

## Retrouver la formule
Un coupon de 5 % pendant deux ans, quand le marché est à 4 % : on reçoit 0,05 dans un an et 1,05 dans deux ans. Actualisés, ils valent $0{,}05/1{,}04+1{,}05/1{,}04^2\approx0{,}0481+0{,}9708=1{,}0189$. [ajout]

En général, chaque coupon $r^*$ de l'année $i$ vaut $r^*/(1+r)^i$ et le capital $1/(1+r)^n$ : c'est la première écriture. [éq. 1]

Les coupons forment une suite géométrique de raison $1/(1+r)$, dont la somme vaut $\frac{1}{r}\big(1-(1+r)^{-n}\big)$ : [éq. 2]

$$B(r^*,r)=\frac{r^*}{r}\Big(1-\frac{1}{(1+r)^n}\Big)+\frac{1}{(1+r)^n}$$ [éq. 2]

## Ce qui la définit
On connaît le coupon, le taux du marché et la durée ; on cherche le prix. Il se lit d'abord en comparant les deux taux : si le coupon paie plus que le marché, $r^*>r$, l'obligation vaut plus que son nominal, elle est « au-dessus du pair » ; si $r^*<r$, en dessous ; si $r^*=r$, au pair, $B=1$. [Ex. 1]

![Le prix de l'obligation à coupon 5 % sur deux ans en fonction du taux du marché : il vaut 1 exactement quand le marché est à 5 %, plus à gauche, moins à droite.](figures/obligation-in-fine.svg) [ajout]

## Le chemin jusqu'ici
fpp/valeur-actuelle-nette fait du prix la somme des flux actualisés ; l'obligation in fine est le cas où les flux sont des coupons égaux puis le capital. Chaque flux est un paquet de fpp/zero-coupon, et l'actualisation se fait ici avec la convention actuarielle de fpp/capitalisation, $(1+r)^{-i}$, à un taux unique pour toutes les dates. [ajout]

## Exemple minimal
Un coupon de 5 %, un marché à 4 %, deux ans : l'obligation vaut 1,0189, au-dessus du pair. [ajout]

## Geste de calcul type
Comparer $r^*$ et $r$ pour savoir de quel côté du pair on est, puis calculer : si le marché monte à 6 %, la même obligation vaut 0,9817, en dessous du pair. [Ex. 1, ajout]

## Cesse d'être valide quand
Un taux unique pour toutes les dates suppose une courbe plate ; avec une courbe qui monte, on actualise chaque flux par son propre zéro-coupon. Le poly emploie ici des taux actuariels, alors qu'il travaille en continu partout ailleurs. [Ex. 1, §2.1]

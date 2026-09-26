---
id: fpp/duration
nom: Sensibilité, duration
type: notion
statut: source
cas_de: fpp/sensibilite
valeur: le taux, sur un zéro-coupon
construite_a_partir_de:
- fpp/valeur-actuelle-nette
refs:
- Déf. 5
- Ex. 1
---

## Ce que c'est
De combien un prix bouge quand le taux bouge. [Déf. 5]

## Forme
$$\dfrac{\partial P(t,r)}{P(t,r)\,\partial r}=-t$$ [Déf. 5]

## Ce que les symboles modélisent
$P(t,r)$ est le prix d'un zéro-coupon, mais écrit autrement qu'avec deux dates : ses deux arguments sont une durée et un taux. $t$ est la maturité, la durée qui reste jusqu'au paiement, comptée depuis aujourd'hui ; $r$ est le taux continu, supposé le même pour toutes les maturités. On a donc $P(t,r)=e^{-rt}$, le même objet que $P(0,t)$ quand le taux zéro-coupon vaut $r$. [Déf. 5, ajout]

Cette écriture fait du taux une variable, et c'est ce qu'il faut pour dériver par rapport à lui. Le $t$ qui sort de la dérivée, $\partial e^{-rt}/\partial r=-t\,e^{-rt}$, est la maturité : c'est elle qu'on lit dans la sensibilité relative. [ajout]

$\mathcal{D}$ est la duration d'un titre à plusieurs flux : une date moyenne, en années comptées depuis $t$, et non une sensibilité. Elle prend l'échéancier du titre et rend une durée ; le poly n'a pas de lettre pour elle, celle-ci est ajoutée. [ajout]

## Ce qui la définit
Une variation instantanée du taux agit sur toute la vie du titre : la sensibilité relative est la maturité elle-même. [Déf. 5]

Le poly intitule la définition « Duration » mais n'écrit que la sensibilité, qui en est distincte. La duration d'un titre qui paie $X_i$ aux dates $t_i$ est la moyenne des durées jusqu'à ses flux, chacune pondérée par la part de la valeur actualisée qui y tombe ; la sensibilité est la variation relative de son prix quand le taux bouge. [ajout]

$$\mathcal{D}=\sum_i (t_i-t)\,\frac{P(t,t_i)\,X_i}{\mathrm{NPV}(t)},\qquad \frac{1}{\mathrm{NPV}}\frac{\partial\,\mathrm{NPV}}{\partial r}=-\mathcal{D}$$ [ajout]

En capitalisation continue, dériver $\sum_i X_ie^{-r(t_i-t)}$ par rapport à $r$ fait sortir chaque durée pondérée par son flux actualisé : la sensibilité relative est exactement l'opposée de la duration. Pour un zéro-coupon il n'y a qu'un flux, la duration vaut la maturité, et duration et sensibilité se confondent — c'est ce qui permet au poly de les écrire sous le même titre. Pour une obligation à coupons, comme le bullet bond, les coupons arrivent avant l'échéance et la duration est plus courte que la maturité. [ajout]

## Le chemin jusqu'ici
La chaîne est la même que pour un contrat à prime nulle : fpp/convention-capitalisation, puis fpp/facteur-actualisation, puis fpp/valeur-actuelle-nette qui somme l'échéancier. [ajout]

Une fois le prix d'un échéancier écrit comme fonction du taux, la sensibilité n'est qu'une dérivée. C'est la première fois du cours qu'on dérive un prix ; la même opération reviendra pour les grecques, sur une autre variable. [ajout]

## Exemple minimal
Un zéro-coupon à 5 ans perd 5 % de sa valeur quand le taux monte de 100 points de base. [ajout]

![Une hausse de taux de 100 points de base, lue sur un échéancier : chaque zéro-coupon perd sa maturité en pour cent. Le titre à cinq ans est celui de l'exemple ; ceux à un, deux et dix ans sont ajoutés pour le dessin.](figures/duration.svg) [ajout]

## Geste de calcul type
Multiplier la maturité par la variation de taux : un zéro-coupon à cinq ans perd 5 % pour cent points de base. Sur un titre à flux multiples, le calcul se fait flux par flux, comme dans l’exemple du bullet bond. [Déf. 5, Ex. 1]

## Cesse d'être valide quand
Premier ordre seulement, et déplacement parallèle de la courbe. [ajout]

En taux actuariels, comme dans l'exemple du bullet bond, la dérivée du prix $\sum_iX_i(1+r)^{-t_i}$ donne $-\mathcal{D}/(1+r)$ et non $-\mathcal{D}$ : c'est alors la duration modifiée, $\mathcal{D}/(1+r)$, qui mesure la sensibilité. [ajout]

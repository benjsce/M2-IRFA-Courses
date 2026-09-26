---
id: fpp/taux-zero-coupon
nom: Taux zéro-coupon
symbole: '$R(t,T)$, $L(t,S)$'
type: notion
statut: source
construite_a_partir_de:
- fpp/zero-coupon
alias:
- zero-coupon rate
- taux comptant
- spot rate
- taux linéaire
refs:
- §2.3
---

## Ce que c'est
Le taux constant qui, appliqué de t à l'échéance, ramène 1 payé à cette échéance au prix du zéro-coupon ; il se lit en capitalisation continue ou linéaire. [§2.3]

## Forme
$$R(t,T)=-\frac{\ln P(t,T)}{T-t},\qquad P(t,S)=\frac{1}{1+(S-t)\,L(t,S)}$$ [§2.3]

## Ce que les symboles modélisent
$R(t,T)$ est le taux continu, $L(t,S)$ le taux linéaire : deux nombres pour un même prix, chacun par an. Le poly écrit $1+(S-T)\,L(t,S)$ ; la durée qui compte est celle qui va de $t$ à $S$, et c'est une coquille. [§2.3, ajout]

$R(T,S)$ est le même objet vu depuis une date future $T$ : aujourd'hui, il est inconnu. [Déf. 7]

## Ce qui la définit
On connaît le prix du zéro-coupon ; on le relit en taux, parce qu'un taux se compare d'une échéance à l'autre alors qu'un prix dépend surtout de la durée. [§2.3, ajout]

![Moins le logarithme du prix du zéro-coupon en fonction de la durée : le taux zéro-coupon R(t,T) = −ln P(t,T) / (T − t) est la pente de la corde issue de l'origine.](figures/taux-zero-coupon.svg) [ajout]

## Le chemin jusqu'ici
fpp/zero-coupon fournit le prix, fpp/capitalisation les deux conventions qui le transforment en taux. Le taux zéro-coupon n'apporte aucune information nouvelle : il change d'unité, du prix au taux. [ajout]

## Exemple minimal
Un zéro-coupon à un an à 0,9608 donne un taux continu de 4 % et un taux linéaire de 4,08 % ; celui à deux ans, à 0,9048, un taux continu de 5 %. [ajout]

## Geste de calcul type
Du prix au taux, $R=-\ln P/(T-t)$ ; du taux au prix, $P=e^{-R(T-t)}$ : $e^{-0,05\times2}=0{,}9048$. [§2.3]

## Cesse d'être valide quand
Le taux dépend de la convention : un taux cité sans elle est ambigu. La courbe du poly cite les échéances courtes en linéaire et les longues en continu. [Déf. 6]

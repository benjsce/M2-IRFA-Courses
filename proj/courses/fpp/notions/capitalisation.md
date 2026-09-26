---
id: fpp/capitalisation
nom: Capitalisation et actualisation
symbole: '$r$, $C(t,n)$, $C(t)$, $B_t$, $r_a$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- compounding
- discounting
- actualisation
- facteur d'actualisation
- taux continu
- capitalisation continue
- taux actuariel
refs:
- §2.1
- exos ch. 1
---

## Ce que c'est
Le facteur qui transporte une somme d'une date à une autre dans la même devise, et qui dépend de la fréquence à laquelle on convient de verser les intérêts. [§2.1]

## Forme
$$C(t,n)=\Big(1+\frac{rt}{n}\Big)^{n}\ \xrightarrow[n\to\infty]{}\ C(t)=e^{rt},\qquad B_t=C(t)^{-1}=e^{-rt}$$ [§2.1]

## Ce que les symboles modélisent
$r$ est un taux par an, constant dans toute la section. $C(t,n)$ est ce que devient 1 placé pendant une durée $t$ quand les intérêts sont versés $n$ fois ; $n=1$ est la capitalisation linéaire, $1+rt$. $C(t)$ est sa limite, la capitalisation continue. $B_t$ fait le trajet inverse : ce que vaut aujourd'hui 1 payé en $t$. $r_a$ est le taux actuariel qui donne le même facteur, $B_t=(1+r_a)^{-t}$. [§2.1]

Ce $C$ n'est pas le prix d'un call, que le poly note aussi $C$, et ce $B_t$ n'est ni le compte capitalisé $B(t_i,t_j)$ ni le prix d'obligation $B(r^*,r)$. [éq. 3, §4.2.2, Ex. 1]

## Ce qui la définit
Un euro aujourd'hui ne vaut pas un euro demain, comme un dollar ne vaut pas un euro : le taux d'intérêt est le taux de change entre deux dates d'une même devise. Aller vers le futur, c'est capitaliser ; revenir vers le présent, c'est actualiser. [§2.1]

On connaît le taux, 5 %, et la durée, 2 ans ; on cherche ce que devient 1. Sans convention de versement des intérêts, la question n'a pas de réponse : 1,10 en linéaire, 1,1025 avec deux versements, 1,1052 en continu. Le poly retient le continu : c'est la limite de toutes les fréquences, il n'impose aucun pas minimal, et l'exponentielle se manipule mieux. [§2.1]

![Le facteur de capitalisation C(t,n) = (1 + rt/n)^n selon le nombre n de versements d'intérêts : 1 + rt en linéaire, (1 + rt/2)² avec deux versements, et de plus en plus près de e^(rt), la capitalisation continue, quand n grandit.](figures/capitalisation.svg) [§2.1, ajout]

## Exemple minimal
À 5 % pendant 2 ans, 1 devient 1,10 en linéaire, 1,1025 avec deux versements et $e^{0,1}\approx1{,}1052$ en continu. [§2.1, ajout]

## Geste de calcul type
Passer d'une convention à l'autre en égalant les facteurs : $e^{r}=1+r_a$, donc 5 % en continu valent $e^{0,05}-1\approx5{,}13\,\%$ en actuariel. Dans le livre d'exercices, tout taux est continu et par an sauf mention contraire. [§2.1, exos ch. 1]

## Cesse d'être valide quand
La section suppose un taux constant, le même pour toutes les durées. Dès que le taux dépend de l'échéance, on ne transporte plus avec $e^{-rt}$ mais avec le prix du zéro-coupon de chaque date. [§2.1, Déf. 3]

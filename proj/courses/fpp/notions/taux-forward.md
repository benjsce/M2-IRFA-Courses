---
id: fpp/taux-forward
nom: Taux forward
symbole: $F(t,T,S)$, $f(t,T)$
type: notion
statut: source
construite_a_partir_de:
- fpp/taux-zero-coupon
alias:
- forward rate
- taux instantané
refs:
- §2.3
---

## Ce que c'est
Le taux qu'il faut obtenir entre $T$ et $S$ pour que placer jusqu'en $T$, puis jusqu'en $S$, rapporte autant que placer d'un coup jusqu'en $S$. [§2.3]

## Forme
$$F(t,T,S)=\dfrac{R(t,S)\,(S-t)-R(t,T)\,(T-t)}{S-T}=\dfrac{1}{S-T}\ln\dfrac{P(t,T)}{P(t,S)}$$ [§2.3]

## Ce que les symboles modélisent
$F(t,T,S)$ prend trois dates : $t$, aujourd'hui ; $T$ et $S$, le début et la fin de la période future. Il rend un taux par an, en capitalisation continue, comme le taux zéro-coupon $R(t,T)$ de $t$ à $T$. Ici $S$ est une date, pas le prix d'une action. [§2.3, ajout]

$f(t,T)$ est le taux forward d'une période réduite à un instant ; on n'en a pas besoin pour calculer $F$. [§2.3]

## Retrouver la formule
![Deux façons de placer de $t$ à $S$. Chaque bloc a pour largeur une durée et pour hauteur un taux ; son aire est ce qu'il rapporte. En haut, d'un coup : 5 % par an pendant deux ans, 10 %, connu aujourd'hui. En bas, 4 % la première année, connu aujourd'hui, puis un trou. Le taux forward $F$ est la hauteur du bloc qui bouche ce trou : pour que les deux lignes fassent 10 %, il faut 6 %.](figures/taux-forward.svg) [ajout]

Deux façons de placer un euro de $t$ à $S$. D'un coup, au taux zéro-coupon $R(t,S)$ : il rapporte $R(t,S)\,(S-t)$, un taux multiplié par une durée. Ce total est **connu aujourd'hui**. [ajout]

En deux temps. Jusqu'en $T$, au taux $R(t,T)$ : il rapporte $R(t,T)\,(T-t)$, **connu aujourd'hui** lui aussi. De $T$ à $S$, il faudra le replacer à un taux que personne ne connaît encore : c'est le trou. Si on l'appelle $F$, cette seconde période rapporte $F\,(S-T)$, et, en capitalisation continue, les deux périodes s'additionnent. [ajout]

Le taux forward est le $F$ qui bouche le trou : celui pour lequel les deux façons rapportent autant. On l'obtient en retirant du total la partie connue, puis en divisant par la durée du trou ; sur la figure, $(10\,\%-4\,\%)/1\text{ an}=6\,\%$. [§2.3]

Enfin, un prix de zéro-coupon s'écrit $P=e^{-\text{taux}\times\text{durée}}$ : taux fois durée vaut donc $-\ln P$, et la même formule s'écrit avec les deux prix. [ajout]

$$R(t,S)\,(S-t)=R(t,T)\,(T-t)+F\,(S-T)\quad\Longleftrightarrow\quad F(t,T,S)=\dfrac{1}{S-T}\ln\dfrac{P(t,T)}{P(t,S)}$$ [§2.3]

## Ce qui la définit
Il se lit dans les prix d'aujourd'hui : ce n'est pas une prévision du taux qu'il fera en $T$. [ajout]

Quand la période se réduit à un instant, on obtient le taux forward instantané, $f(t,T)=-\partial\ln P(t,T)/\partial T$ ; mis bout à bout, ces taux redonnent tout prix de zéro-coupon, $P(t,T)=\exp\big(-\int_t^T f(t,u)\,du\big)$. [§2.3]

## Le chemin jusqu'ici
fpp/convention-capitalisation dit qu'en capitalisation continue, ce que rapportent deux périodes successives s'additionne ; fpp/facteur-actualisation donne les prix $P(t,T)$, et fpp/taux-zero-coupon les réécrit en taux $R(t,T)$ : ce sont les deux données connues de la figure. [ajout]

## Exemple minimal
Aujourd'hui, le taux zéro-coupon vaut 4 % à un an et 5 % à deux ans : le taux forward de la deuxième année vaut 6 %. [ajout]

## Geste de calcul type
Total moins partie connue, divisé par la durée du trou : $(5\,\%\times2-4\,\%\times1)/1=6\,\%$. Avec les prix $P(t,t+1)=0{,}9608$ et $P(t,t+2)=0{,}9048$ : $\ln(0{,}9608/0{,}9048)/1\approx6\,\%$. [§2.3]

## Cesse d'être valide quand
Pour obtenir vraiment ce taux, et pas seulement le lire, il faut pouvoir prêter et emprunter aux deux échéances $T$ et $S$. [ajout]

## Origine
- exercice fpp/ex-04 : un rapport de deux prix à terme de change est un rapport de facteurs d'actualisation forward [ajout]
- exercice fpp/ex-19 : toute la matrice des forwards se remplit par la même règle, total moins partie connue divisé par la durée, $\big(r(T)T-r(t)t\big)/(T-t)$, où $t$ est une échéance et non la date d'aujourd'hui [exo. 19]

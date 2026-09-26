---
id: fpp/parite-call-put
nom: Parité call-put
type: notion
statut: source
construite_a_partir_de:
- fpp/call
- fpp/put
- fpp/facteur-actualisation
alias:
- call put parity
- parité
refs:
- Prop. 7
---

## Ce que c'est
La différence entre un call et un put de mêmes strike et maturité est un forward. [Prop. 7]

## Forme
$$(S_T-K)^+-(K-S_T)^+=S_T-K\ \implies\ C_t-P_t=S_t-KP(t,T)$$ [ajout]

C'est la parité écrite à une date $t<T$ quelconque, $C_t$ et $P_t$ étant les prix en $t$ du call et du put de strike $K$ et d'échéance $T$. La source l'énonce en $t=0$ : $C(S_0,K,T)-P(S_0,K,T)=S_0-KP(0,T)$. [Prop. 7]

## Ce que les symboles modélisent
$S_t$ est le prix comptant du sous-jacent en $t$, et $S_T$ son prix à l'échéance, inconnu en $t$ : la première égalité porte sur les payoffs, donc sur $S_T$, la seconde sur les prix, donc sur $S_t$. $(\cdot)^+$ rend la partie positive, zéro quand l'expression est négative. [ajout]

$P(t,T)$, avec deux dates pour arguments, est le zéro-coupon : le prix en $t$ d'une unité payée en $T$. Ce n'est pas le put, noté $P_t$ ; le cours emploie la même lettre pour les deux, et c'est le nombre d'arguments qui les distingue. [ajout]

## Retrouver la formule
![À chaque valeur du sous-jacent, le payoff du call moins celui du put tombe sur celui du forward : c'est ce que veut dire « vraie état par état ». Le strike vaut 100, comme dans l'exemple minimal, et aucun prix n'apparaît — l'actualisation vient après.](figures/parite-call-put.svg) [ajout]

État par état : au-dessus du strike seul le call paie, au-dessous seul le put, et dans les deux cas la différence vaut $S_T-K$. C'est une identité de payoff. [Prop. 7]

Deux positions qui paient la même chose dans tous les états ont le même prix en $t$ : sinon on vend la plus chère, on achète l'autre, et l'écart est un gain sans risque. [Prop. 7]

$S_T-K$ payé en $T$, c'est l'action, qui vaut $S_t$ sans dividende, moins $K$ payé en $T$, qui vaut $KP(t,T)$. [ajout]

$$C_t-P_t=S_t-KP(t,T)$$ [ajout]

## Ce qui la définit
C’est une identité de payoff, vraie état par état, donc une identité de prix par absence d’arbitrage. Aucun modèle n’y entre : ni volatilité, ni loi du sous-jacent. [Prop. 7]

## Le chemin jusqu'ici
Deux fils se rejoignent ici. Le premier part de fpp/payoff, dont fpp/call et fpp/put sont deux cas ; le second part de fpp/convention-capitalisation et aboutit à fpp/facteur-actualisation. [ajout]

La parité se démontre en deux temps, et le socle le montre : d'abord une identité entre payoffs, vraie état par état ; ensuite seulement l'actualisation, pour passer des payoffs aux prix. C'est pourquoi elle ne demande aucun modèle — elle tient là où Black et Scholes ne tient plus. [ajout]

## Exemple minimal
Avec $S_0=100$, $K=100$, $P(0,1)=0{,}9608$ : $C-P=100-96{,}08=3{,}92$. [ajout]

## Geste de calcul type
Connaissant l’un des deux prix, en déduire l’autre sans modèle. Si les deux sont cotés et que la parité n’est pas respectée, l’écart est un arbitrage. [Prop. 7]

## Cesse d'être valide quand
Énoncée sans dividende dans la source. Avec un dividende, $S_t$ est remplacé par $S_t\Phi$, et l’identité de payoff reste mais l’identité de prix change. [ajout]

## Origine
- exercice fpp/ex-10 : quatre inconnues, une équation ; on l'emploie dans les quatre sens, ici pour extraire le strike [ajout]
- exercice fpp/ex-12 : elle ne sert pas qu'à calculer un prix manquant, elle sert à **tester une table de prix** — trois strikes, trois valeurs de $C-P+K$ [exo. 12]
- exercice fpp/ex-14 : la démonstration ne demande ni modèle ni Black et Scholes, seulement une identité de payoff, la loi du prix unique et la linéarité [exo. 14]
- exercice fpp/ex-16 : emploi le plus inattendu — séparer la dette risquée en dette sans risque **moins un put** vendu aux actionnaires [exo. 16]

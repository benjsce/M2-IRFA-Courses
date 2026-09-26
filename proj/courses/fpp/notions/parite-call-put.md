---
id: fpp/parite-call-put
nom: Parité call-put
type: notion
statut: source
cas_de: fpp/absence-d-arbitrage
construite_a_partir_de:
- fpp/option
- fpp/zero-coupon
alias:
- call put parity
- put call parity
refs:
- Prop. 7
- exos éq. 1.1
- exo. 10
- exo. 11
- exo. 12
- exo. 14
---

## Ce que c'est
Un call acheté et un put vendu, de même strike et de même échéance, valent un achat à terme : l'action moins le strike actualisé. [Prop. 7]

## Forme
$$\mathrm{call}(S_0,K,T)-\mathrm{put}(S_0,K,T)=S_0-K\,P(0,T)=S_0-K\,e^{-rT}$$ [Prop. 7]

## Ce que les symboles modélisent
$\mathrm{call}(S_0,K,T)$ et $\mathrm{put}(S_0,K,T)$ sont les prix d'aujourd'hui des deux options européennes de strike $K$ et de maturité $T$ ; $S_0$ est le prix de l'action ; $K\,P(0,T)$ ce que vaut aujourd'hui le strike payé en $T$. [Prop. 7]

## Retrouver la formule
![Le payoff du call, moins celui du put de même strike K, égale la droite S_T − K : le payoff d'un achat à terme au prix K. Mêmes paiements, mêmes prix : C − P = S₀ − K P(0,T).](figures/parite-call-put.svg) [Prop. 7, ajout]

À l'échéance, quel que soit le prix final, $(S_T-K)^+-(K-S_T)^+=S_T-K$ : au-dessus du strike, le call paie et le put non ; en dessous, c'est l'inverse, et la différence vaut toujours $S_T-K$. [Prop. 7, exos éq. 1.1]

Deux positions qui paient la même chose ont le même prix, et le prix d'une somme est la somme des prix. Le membre de droite est l'action, qui vaut $S_0$ s'il n'y a pas de dividende, moins $K$ payé en $T$, qui vaut $K\,P(0,T)$. [exo. 14]

Avec l'action à 100, un strike de 100 et un taux de 4 % à un an : $100-100\times0{,}9608=3{,}92$, quel que soit le modèle. [ajout]

$$\mathrm{call}-\mathrm{put}=S_0-K\,P(0,T)$$ [Prop. 7]

## Ce qui la définit
Ce qui est **connu** : trois des quatre prix. Ce qu'on **cherche** : le quatrième. La parité ne dépend d'aucun modèle : ni de la volatilité ni de la probabilité. [Prop. 7, ajout]

Le livre d'exercices en tire trois usages. Acheter le call et vendre le put, c'est acheter à terme au prix $K$, et cela ne coûte rien exactement quand $K$ est le prix forward. Trois des quatre prix donnent le strike. Et un tableau de prix qui viole la parité se laisse arbitrer. [exo. 11, exo. 10, exo. 12]

## Le chemin jusqu'ici
fpp/option fournit les deux contrats, et fpp/payoff l'identité point par point entre leurs paiements. fpp/zero-coupon évalue le strike payé à l'échéance, dans la convention continue de fpp/capitalisation qui donne l'écriture $K\,e^{-rT}$. [ajout]

## Exemple minimal
L'action à 100, un strike de 100, un taux de 4 % à un an : le call vaut 3,92 de plus que le put. [ajout]

## Geste de calcul type
Tirer une inconnue des trois autres : avec l'action à 500, des taux nuls, un call à 67 et un put à 19, $67-19=500-K$ donne $K=452$. [exo. 10]

## Cesse d'être valide quand
Avec des dividendes, $S_0$ est remplacé par l'action diminuée de la valeur actuelle des dividendes, ou par $S_0\,e^{-qT}$. Pour des options américaines, l'égalité devient une inégalité. [Prop. 7, ajout]

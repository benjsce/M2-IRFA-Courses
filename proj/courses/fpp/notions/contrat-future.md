---
id: fpp/contrat-future
nom: Contrat future
symbole: $H_t$
type: notion
statut: source
construite_a_partir_de:
- fpp/prix-forward
alias:
- futures contract
- future
- appel de marge
- margining
refs:
- §4.1
- §4.2
---

## Ce que c'est
Un contrat à terme négocié en bourse et réglé chaque jour : l'acheteur reçoit ou verse, jour après jour, la variation du prix future. [§4.1, §4.2]

## Forme
$$\text{flux reçu par l'acheteur en }t_{i+1}=H(t_{i+1})-H(t_i),\qquad H(T)=S(T)$$ [§4.2]

## Ce que les symboles modélisent
$H_t$, écrit aussi $H(t_i)$, est le prix future coté à la date $t$ ; $t_0=t,t_1,\dots,t_n=T$ sont les dates de règlement, en général les jours ; $S(T)$ est le prix comptant du sous-jacent à l'échéance, que le prix future rejoint. [§4.2]

## Ce qui la définit
Les contrats forward se traitent de gré à gré, surtout sur les devises ; les contrats futures dominent sur les marchés organisés, et le mécanisme d'appels de marge les distingue. Les deux se ressemblent, mais le règlement quotidien change la nature de leur prix. [§4.1]

Ce qui est **connu** : le prix future du jour et le fait qu'il finira égal au prix comptant. Ce qui est **inconnu** : les taux auxquels chaque flux quotidien sera replacé jusqu'à l'échéance. C'est pourquoi le prix future ne s'écrit pas, comme le prix forward, avec des quantités observables aujourd'hui. [§4.2]

La différence ressemble, dit le poly, à celle qui sépare l'achat d'un zéro-coupon d'une suite de placements courts renouvelés. [§4.1]

![Un prix future qui part de 104,08 et rejoint le prix comptant à l'échéance : chaque jour, la barre est le flux versé à l'acheteur, positif quand le prix monte, négatif quand il baisse.](figures/contrat-future.svg) [ajout]

## Le chemin jusqu'ici
fpp/prix-forward est le point de comparaison : même sous-jacent, même échéance, mais un seul paiement à la fin. Ce prix sort de fpp/cash-and-carry, qui porte l'action avec un emprunt évalué par fpp/zero-coupon dans la convention de fpp/capitalisation, et fpp/absence-d-arbitrage le rend unique. Le règlement quotidien casse ce montage : les flux arrivent en cours de route. [ajout]

## Exemple minimal
Un prix future qui passe de 104,08 à 105,00 puis à 103,50 : l'acheteur reçoit 0,92 le premier jour et verse 1,50 le second. [ajout]

## Geste de calcul type
Additionner les flux quotidiens donne $H(T)-H(t_0)$, comme pour un forward ; mais chaque flux arrive plus tôt et se replace au taux du jour, si bien que la richesse finale en diffère. [§4.2]

## Cesse d'être valide quand
Si les taux sont connus d'avance, le replacement des flux n'a plus rien d'aléatoire et le prix future égale le prix forward. [Prop. 4]

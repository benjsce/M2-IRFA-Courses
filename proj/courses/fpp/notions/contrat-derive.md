---
id: fpp/contrat-derive
nom: Contrat dérivé
type: abstraite
statut: ajout
cas_de: fpp/absence-arbitrage
parametre: le flux échangé à la signature
construite_a_partir_de:
- fpp/mesure-risque-neutre
refs:
- Prop. 6
---

## Ce que c'est
Un contrat dont le paiement dépend d'un sous-jacent et qui fixe deux nombres, la prime et le strike : l'un est donné, l'autre se cherche. [ajout]

## Forme
$$\text{prime}=P(t,T)\;\mathbb{E}^{\mathbb{Q}}\big(\text{paiement}(S_T,K)\big)$$ [Prop. 6]

## Ce que les symboles modélisent
La prime est ce qu'on paie en $t$, à la signature, pour entrer dans le contrat. $K$ est le strike, le nombre écrit dans le contrat : le prix de livraison d'un engagement ferme, le prix d'exercice d'une option. [ajout]

$\text{paiement}(S_T,K)$ est ce que le contrat verse à l'échéance $T$ ; il prend le cours $S_T$ du sous-jacent, inconnu en $t$, et le strike : $S_T-K$ pour un engagement ferme, $(S_T-K)^+$ pour un call. $\mathbb{E}^{\mathbb{Q}}$ en fait la moyenne sous la probabilité risque-neutre, et le zéro-coupon $P(t,T)$ ramène cette moyenne en $t$. [Prop. 6, ajout]

## Ce que les membres partagent
![Le même moteur écrit deux fois. En haut, un engagement ferme : la prime est connue, nulle, et le strike est le trou, 104,08. En bas, un call : le strike est connu, 100, et la prime est le trou, 9,93. Case pleine, connu ; case en pointillé, cherché. Action à 100, taux de 4 %, échéance dans un an.](figures/contrat-derive.svg) [ajout]

Un seul moteur relie les deux nombres : la prime est la moyenne risque-neutre du paiement, ramenée en $t$. [Prop. 6]

Engagement ferme : **la prime est connue**, nulle, et **le strike est cherché**. Le moteur s'écrit $0=P(t,T)\big(\mathbb{E}^{\mathbb{Q}}(S_T)-K\big)$, d'où $K=\mathbb{E}^{\mathbb{Q}}(S_T)$, le prix à terme. [Prop. 6]

Option : **le strike est connu**, et **la prime est cherchée** ; le moteur la donne directement. [ajout]

## Pourquoi ce niveau existe
Un forward ne coûte rien, une option se paie : on croirait deux calculs. Il n'y en a qu'un, et ce niveau le montre ; seul change ce qui est donné et ce qui est cherché. [ajout]

## Le chemin jusqu'ici
Le moteur, c'est fpp/mesure-risque-neutre : une probabilité sous laquelle tout prix est une moyenne actualisée. Elle est calée sur fpp/prix-a-terme, qui fixe la moyenne du sous-jacent sous cette probabilité. [ajout]

Ce prix à terme se déduit lui-même d'une fpp/replication-statique, dont fpp/portage et fpp/facteur-actualisation chiffrent les deux jambes ; le second repose sur fpp/convention-capitalisation. [ajout]

## Exemple minimal
Action à 100, taux de 4 %, échéance dans un an : le forward, de prime nulle, a pour strike 104,08 ; le call de strike 100 a pour prime 9,93. [ajout]

## Geste de calcul type
Écrire le moteur, y mettre le nombre donné, résoudre pour l'autre. Prime nulle : $0=0{,}9608\times(104{,}08-K)$, d'où $K=104{,}08$. Strike 100 : la moyenne risque-neutre de $(S_T-100)^+$ vaut 10,33 dans le modèle de Black et Scholes à 20 % de volatilité, d'où la prime $0{,}9608\times10{,}33=9{,}93$. [Prop. 6, ajout]

## Cesse d'être valide quand
Le moteur se chiffre sans modèle tant que le paiement est linéaire en $S_T$ : il suffit alors de $\mathbb{E}^{\mathbb{Q}}(S_T)$, que fixent les prix du marché. Pour un paiement non linéaire, comme celui du call, il faut toute la loi de $S_T$ sous $\mathbb{Q}$, donc un modèle. [ajout]

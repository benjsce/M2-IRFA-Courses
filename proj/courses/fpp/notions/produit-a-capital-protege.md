---
id: fpp/produit-a-capital-protege
nom: Produit à capital protégé
type: notion
statut: source
cas_de: fpp/strategie-optionnelle
valeur: on achète l’optionalité
construite_a_partir_de:
- fpp/call
- fpp/facteur-actualisation
alias:
- principal protected product
- PPP
refs:
- §9.2
---

## Ce que c'est
Un zéro-coupon qui rend la mise, plus un call qui donne la hausse. [§9.2]

## Forme
$$\text{ZC}+\text{Call},\qquad \text{ou de façon équivalente}\qquad \text{Spot}+\text{Put}$$ [§9.2]

![La mise $K$ coupée en deux. $KP(t,T)$ placés en zéro-coupon rendent $K$ en $T$ ; le solde achète des calls, dont le flux en $T$ est en pointillé parce qu'il est aléatoire et peut être nul.](figures/produit-a-capital-protege.svg) [ajout]

## Ce que les symboles modélisent
Les quatre mots de la forme désignent des positions, pas des prix. ZC est un zéro-coupon qui paie en $T$ le capital garanti ; Call est un call sur le sous-jacent, d'échéance $T$ ; Spot est le sous-jacent lui-même, acheté au comptant ; Put est un put de même échéance. [§9.2, ajout]

Sur la figure, $K$ est la mise, celle que le produit rend à l'échéance, et $KP(t,T)$ ce qu'il faut en placer en $t$ pour la retrouver en $T$ : $P(t,T)$ y est le prix d'un zéro-coupon, et non celui d'un put. L'équivalence des deux écritures demande que le strike des options soit égal au nominal du zéro-coupon. [ajout]

## Ce qui la définit
Les deux écritures sont la même par la parité call-put : protéger le capital, c’est acheter une option de vente, que l’on écrive la protection du côté du zéro-coupon ou du côté du comptant. [§9.2, Prop. 7]

## Le chemin jusqu'ici
Deux fils y mènent. Le premier va de fpp/payoff à fpp/call : c'est lui qui donne la hausse. Le second va de fpp/convention-capitalisation à fpp/facteur-actualisation : c'est lui qui rend la mise. [ajout]

Le produit est exactement la somme des deux, et c'est tout le montage : un zéro-coupon garantit le capital, le solde achète l'optionalité. La fiche n'a besoin d'aucun modèle de prix, seulement de savoir que ces deux objets existent et s'additionnent. [ajout]

## Exemple minimal
96,08 placés en zéro-coupon à un an rendent 100 ; les 3,92 restants achètent une fraction de call. [ajout]

## Geste de calcul type
Placer $KP(t,T)$ pour garantir $K$, puis dépenser le solde en calls : le nombre de calls achetés donne le taux de participation à la hausse. [ajout]

## Cesse d'être valide quand
La protection vaut à l’échéance seulement, et elle coûte exactement la prime du put : il n’y a pas de protection gratuite. [ajout]

## Origine
- exercice fpp/ex-17 : le taux de participation est un rapport, coussin sur prime du call à la monnaie. Il monte avec le taux et la maturité, il descend avec la volatilité [exo. 17]
- exercice fpp/ex-17 : le jeu de paramètres du corrigé ($r=4\,\%$, $T=4$, $\sigma=15\,\%$, $d=1{,}88\,\%$) est calibré pour donner exactement 100 % de participation. C'est un calibrage, pas une loi [ajout]

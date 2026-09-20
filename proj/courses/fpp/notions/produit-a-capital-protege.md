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

## Ce qui la définit
Les deux écritures sont la même par la parité call-put : protéger le capital, c’est acheter une option de vente, que l’on écrive la protection du côté du zéro-coupon ou du côté du comptant. [§9.2, Prop. 7]

## Exemple minimal
96,08 placés en zéro-coupon à un an rendent 100 ; les 3,92 restants achètent une fraction de call. [ajout]

## Geste de calcul type
Placer $KP(0,T)$ pour garantir $K$, puis dépenser le solde en calls : le nombre de calls achetés donne le taux de participation à la hausse. [ajout]

## Cesse d'être valide quand
La protection vaut à l’échéance seulement, et elle coûte exactement la prime du put : il n’y a pas de protection gratuite. [ajout]

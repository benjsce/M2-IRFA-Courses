---
id: fpp/compte-capitalise
nom: Compte capitalisé
symbole: $B(t,T)$
type: notion
statut: source
construite_a_partir_de:
- fpp/facteur-actualisation
alias:
- bank account
- money market account
refs:
- §4.2.2
---

## Ce que c'est
Le facteur d’actualisation obtenu en enchaînant les zéro-coupons courts, sans connaître les taux futurs. [§4.2.2]

## Forme
$$B(t,T)=\prod_k P(t_k,t_{k+1})$$ [§4.2.2]

## Ce qui la définit
Même rôle que $P(t,T)$ — transporter de la valeur jusqu’à $T$ — mais reconstitué pas à pas, donc aléatoire. [§4.2.2]

## Exemple minimal
Un an à 4 % puis un an à 6 % : $B(0,2)=0{,}9048$, soit exactement $P(0,2)$ — les taux sont ici déterministes. [ajout]

## Geste de calcul type
Enchaîner les zéro-coupons courts : $0{,}9608\times0{,}9418=0{,}9048$. Comparer ensuite à $P(0,2)$ — l’égalité signale des taux déterministes, l’écart mesure le risque de refinancement. [§4.2.2, Prop. 4]

## Cesse d'être valide quand
Égale $P(t,T)$ quand les taux sont déterministes — la source n’énonce que ce sens. C’est toute la différence entre acheter un zéro-coupon et rouler du court terme. [Prop. 4]

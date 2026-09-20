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
Ce que devient un euro replacé au jour le jour jusqu’en $T$, sans connaître les taux futurs. [§4.2.2]

## Forme
$$B(t,T)=\prod_k P(t_k,t_{k+1})$$ [§4.2.2]

## Ce qui la définit
Même rôle que $P(t,T)$ — transporter de la valeur jusqu’à $T$ — mais reconstitué pas à pas, donc aléatoire. [§4.2.2]

## Exemple minimal
à venir [ajout]

## Geste de calcul type
à venir [ajout]

## Cesse d'être valide quand
Égale $P(t,T)$ si et seulement si les taux sont déterministes. C’est toute la différence entre acheter un zéro-coupon et rouler du court terme. [Prop. 4]

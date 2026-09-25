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

![En haut, le zéro-coupon fait le trajet de $T$ à $t$ en un seul saut, connu en $t$. En bas, le compte capitalisé enchaîne des zéro-coupons courts : seul le premier est connu en $t$, les suivants ne le seront qu'à leur date, d'où le pointillé.](figures/compte-capitalise.svg) [ajout]

## Ce que les symboles modélisent
$B(t,T)$ prend deux dates et rend un facteur : ce que devient une unité placée en $t$ et roulée jusqu'en $T$ au taux court. Sa différence avec le zéro-coupon tient en un mot — sa valeur en $T$ n'est **pas connue** en $t$, puisqu'on enchaîne des taux qu'on ignore encore. [§4.2.2]

## Ce qui la définit
Même rôle que $P(t,T)$ — transporter de la valeur jusqu’à $T$ — mais reconstitué pas à pas, donc aléatoire. [§4.2.2]

## Le chemin jusqu'ici
fpp/facteur-actualisation, construit sur fpp/convention-capitalisation, donne le prix d'un euro payé à une date fixée d'avance. [ajout]

Le compte capitalisé répond à une autre question : combien vaut un euro qu'on réinvestit au jour le jour sans connaître les taux futurs ? D'où le produit de zéro-coupons courts, et une quantité qui n'est plus connue aujourd'hui. Cette différence-là est ce qui séparera plus tard un forward d'un future. [ajout]

## Exemple minimal
Un an à 4 % puis un an à 6 % : $B(0,2)=0{,}9048$, soit exactement $P(0,2)$ — les taux sont ici déterministes. [ajout]

## Geste de calcul type
Enchaîner les zéro-coupons courts : $0{,}9608\times0{,}9418=0{,}9048$. Comparer ensuite à $P(0,2)$ — l’égalité signale des taux déterministes, l’écart mesure le risque de refinancement. [§4.2.2, Prop. 4]

## Cesse d'être valide quand
Égale $P(t,T)$ quand les taux sont déterministes — la source n’énonce que ce sens. C’est toute la différence entre acheter un zéro-coupon et rouler du court terme. [Prop. 4]

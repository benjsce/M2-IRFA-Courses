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
Le facteur d’actualisation obtenu en enchaînant les zéro-coupons courts, dont la valeur dépend de taux futurs qu'on ne connaît pas encore. [§4.2.2]

## Forme
$$B(t,T)=\prod_k P(t_k,t_{k+1})$$ [§4.2.2]

## Ce que les symboles modélisent
$B(t,T)$ prend deux dates et rend un facteur : celui qui ramène en $t$ une unité payée en $T$ quand on roule au taux court ; une unité placée en $t$ et roulée jusqu'en $T$ devient $1/B(t,T)$. Sa différence avec le zéro-coupon tient en un mot — sa valeur n'est **pas connue** en $t$, puisqu'on enchaîne des taux qu'on ignore encore. [§4.2.2]

Malgré son nom, $B(t,T)$ n'est pas la valeur du compte, qui grossit, mais son inverse : un facteur plus petit que $1$ quand les taux sont positifs. Le compte lui-même, ce que devient une unité placée en $t$, vaut $1/B(t,T)$. [§4.2.2, ajout]

## Retrouver la formule
![En haut, le zéro-coupon fait le trajet de $T$ à $t$ en un seul saut, connu en $t$. En bas, le compte capitalisé enchaîne des zéro-coupons courts : seul le premier est connu en $t$, les suivants ne le seront qu'à leur date, d'où le pointillé.](figures/compte-capitalise.svg) [ajout]

Placer $1$ en $t=t_0$ au zéro-coupon court : on a $1/P(t_0,t_1)$ en $t_1$. [ajout]

Replacer le tout jusqu'en $t_2$ : on a $1/\bigl(P(t_0,t_1)P(t_1,t_2)\bigr)$. Mais $P(t_1,t_2)$ ne sera connu qu'en $t_1$ : le montant final ne l'est pas en $t$. [ajout]

Jusqu'en $T$, une unité placée en $t$ devient $1/\prod_k P(t_k,t_{k+1})$. Le facteur qui ramène de $T$ à $t$ est l'inverse, comme $P(t,T)$ est l'inverse de ce que devient une unité placée au zéro-coupon long. [ajout]

$$B(t,T)=\prod_k P(t_k,t_{k+1})$$ [§4.2.2]

## Ce qui la définit
Même rôle que $P(t,T)$ — transporter de la valeur jusqu’à $T$ — mais reconstitué pas à pas, donc aléatoire. [§4.2.2]

## Le chemin jusqu'ici
fpp/facteur-actualisation, construit sur fpp/convention-capitalisation, donne le prix d'un euro payé à une date fixée d'avance, connu dès aujourd'hui. [ajout]

Le compte capitalisé répond à une autre question : que devient un euro qu'on réinvestit de période en période, aux taux que chacune fixera ? D'où le produit de zéro-coupons courts, et une quantité qui n'est plus connue aujourd'hui. [ajout]

## Exemple minimal
Un an à 4 %, puis un an à 6 % : $B(t,t+2)=0{,}9048$, soit exactement $P(t,t+2)$ — les deux taux sont ici supposés connus d'avance. [ajout]

## Geste de calcul type
Enchaîner les zéro-coupons courts : $e^{-0{,}04}\times e^{-0{,}06}=0{,}9608\times0{,}9418\approx0{,}9048$. Comparer ensuite à $P(t,t+2)$ — l’égalité signale des taux déterministes ; l’écart, constaté après coup, mesure le risque de refinancement. [§4.2.2, Prop. 4]

## Cesse d'être valide quand
Égale $P(t,T)$ quand les taux sont déterministes — la source n’énonce que ce sens. C’est toute la différence entre acheter un zéro-coupon et rouler du court terme. [Prop. 4]

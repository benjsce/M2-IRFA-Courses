---
id: fpp/replication-dynamique
nom: Réplication dynamique
type: notion
statut: source
cas_de: fpp/replication
valeur: rééquilibrage à chaque pas
construite_a_partir_de:
- fpp/compte-capitalise
alias:
- delta hedging
- stratégie autofinançante
refs:
- §4.2.2
---

## Ce que c'est
Une stratégie autofinançante rééquilibrée à chaque pas, dont la valeur finale est le payoff. [§4.2.2]

## Forme
détenir $1/B(t_0,t_i)$ contrats en $t_i$ [§4.2.2]

## Ce que les symboles modélisent
$t_0$ est la date où l'on met en place la stratégie et $t_i$ la $i$-ième date de rééquilibrage, typiquement un jour après la précédente. Les contrats sont des contrats futures, dont les variations de prix sont versées à chaque date par l'appel de marge. [§4.2.2, ajout]

$B(t_0,t_i)$ est le compte capitalisé : le produit des zéro-coupons à une période enchaînés de $t_0$ à $t_i$. Vu de $t_0$, il est aléatoire, parce que les taux des périodes à venir ne sont pas encore connus ; c'est pour cela que la position se recalcule à chaque pas au lieu d'être fixée d'avance. Ce n'est pas le zéro-coupon $P(t_0,t_i)$, avec lequel il ne coïncide que si les taux sont déterministes. [§4.2.2]

## Ce qui la définit
On ne connaît plus le coût de portage à l’avance : on le suit. La position est ajustée à chaque date pour que la valeur terminale reste celle visée. [§4.2.2]

## Le chemin jusqu'ici
Il faut fpp/convention-capitalisation, puis fpp/facteur-actualisation, puis fpp/compte-capitalise, qui est la brique décisive. [ajout]

C'est le compte capitalisé qui rend la réplication *dynamique* possible : il donne le prix de l'argent réinvesti au jour le jour, donc la quantité à détenir à chaque pas. Sans lui on ne sait répliquer qu'en une fois, à l'achat, et c'est la réplication statique. [ajout]

## Exemple minimal
Trois pas à $P=0{,}99$ chacun : on détient successivement $1{,}0101$, $1{,}0203$ puis $1{,}0306$ contrats. [ajout]

## Geste de calcul type
Suivre la position au lieu de la figer : détenir $1/B(t_0,t_i)$ contrats en $t_i$, soit 1,0101 puis 1,0203 puis 1,0306 pour trois pas à 0,99. La position se recalcule à chaque date. [§4.2.2]

## Cesse d'être valide quand
Suppose des marchés sans friction et un rééquilibrage continu — l’hypothèse la plus fragile de tout l’édifice. [ajout]

---
id: fpp/facteur-actualisation
nom: Facteur d’actualisation
symbole: $P(t,T)$
type: notion
statut: source
cas_de: fpp/facteur-conversion
valeur: la date
construite_a_partir_de:
- fpp/convention-capitalisation
alias:
- zéro-coupon
- zero-coupon bond
- discount factor
refs:
- §2.1
- Déf. 3
---

## Ce que c'est
Le prix aujourd’hui d’un euro payé en $T$, c’est-à-dire le prix d’un zéro-coupon : un titre qui paie 1 à une date et rien d’autre. [§2.1, Déf. 3]

## Forme
$$P(t,T)=e^{-R(t,T)(T-t)}=C_t^{-1}$$ [§2.1, Déf. 3, §2.3]

## Ce que les symboles modélisent
$P(t,T)$ prend deux dates et rend un **prix** : celui, en $t$, d'une unité payée en $T$. Ce n'est pas un taux — c'est un nombre entre zéro et un, qu'on lit sur un titre échangé. $\tau$ est la durée qui sépare les deux dates, et c'est par elle qu'un prix se convertit en rendement. [Déf. 3, §3.1]

## Ce qui la définit
On capitalise en avançant dans le temps et l’on actualise en reculant : le facteur est le taux de change entre deux dates. [§2.1, Déf. 3]

![Le même facteur, lu dans les deux sens. Un euro payé en $T$ revient en $t$ et y vaut $P(t,T)$ ; un euro placé en $t$ arrive en $T$ et y vaut $1/P(t,T)$.](figures/facteur-actualisation.svg) [ajout]

## Le chemin jusqu'ici
Tout part de fpp/convention-capitalisation, qui dit dans quelles coordonnées un taux s'écrit. [ajout]

Le facteur d'actualisation est ce qu'on obtient en refusant de choisir : plutôt qu'un taux dans une convention, un prix — celui d'un euro payé plus tard. C'est l'objet que les conventions décrivent toutes, chacune à sa façon. [ajout]

## Exemple minimal
Taux continu de 4 % sur un an : $P(0,1)=0{,}9608$. [ajout]

## Geste de calcul type
Fixer la convention, puis actualiser : à 4 % continu, un flux de 100 payé dans un an vaut $100\times0{,}9608=96{,}08$ aujourd’hui. Pour remonter le temps on divise, pour l’avancer on multiplie. [§2.1]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| convention de capitalisation | linéaire | $1+rt$ |
| convention de capitalisation | $n$ fois par période | $(1+rt/n)^n$ |
| convention de capitalisation | continue | $e^{rt}$ |
| convention de capitalisation | actuarielle | $(1+r_a)^t$, $r_a=e^r-1$ |
[§2.1, Déf. 3]

## Cesse d'être valide quand
Suppose une convention fixée d’avance — elle borne par le bas toute actualisation ultérieure. [§2.1]

Suppose aussi des taux déterministes : dès qu’ils ne le sont plus, c’est $B(t,T)$ qui prend le relais. [§4.2.2, Prop. 4]

## Origine
- exercice fpp/ex-03 : « le taux à six mois est de 4 % » ne dit ni l'unité ni la convention ; le défaut du cours est continu, annuel [ajout]
- exercice fpp/ex-10 : taux nul ne veut pas dire « pas d'actualisation à écrire », mais $P(0,T)=1$ ; la formule ne change pas de forme [ajout]

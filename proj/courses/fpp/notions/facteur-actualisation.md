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
Prix aujourd’hui d’un euro payé en $T$. Un titre qui paie 1 à une date et rien d’autre : le zéro-coupon. [§2.1, Déf. 3]

## Forme
$$P(t,T)=e^{-R(t,T)(T-t)}=C_t^{-1}$$ [§2.1, Déf. 3, §2.3]

## Ce qui la définit
Capitalisation en avançant dans le temps, actualisation en reculant. Le facteur est le taux de change entre deux dates. [§2.1, Déf. 3]

## Exemple minimal
Taux continu de 4 % sur un an : $P(0,1)=0{,}9608$. [ajout]

## Geste de calcul type
à venir [ajout]

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

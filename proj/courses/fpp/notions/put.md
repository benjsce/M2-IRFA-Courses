---
id: fpp/put
nom: Put
symbole: $P$
type: notion
statut: source
cas_de: fpp/option
valeur: le droit de vendre
construite_a_partir_de:
- fpp/payoff
alias:
- put option
- option de vente
refs:
- Déf. 9
- Déf. 11
---

## Ce que c'est
Le droit de vendre le sous-jacent au prix $K$ à la date $T$. [Déf. 9]

## Forme
$$\mathrm{Put}(S_T,K)=(K-S_T)^+$$ [Déf. 11]

## Ce qui la définit
Symétrique du call par rapport au strike : le détenteur n’exerce que si $S_T<K$, et le payoff est borné par $K$. [Déf. 11]

## Le chemin jusqu'ici
Une seule brique : fpp/payoff. Le put est le payoff $(K-S_T)^+$, le symétrique du call. [ajout]

Il n'est pas *construit* sur le call : les deux sont deux payoffs élémentaires, définis en parallèle. Ce qui les relie viendra plus tard, avec la parité call-put, et c'est un résultat, pas une définition. [ajout]

## Exemple minimal
Strike 100, sous-jacent à 96 à l’échéance : le put paie 4. [ajout]

## Geste de calcul type
Plutôt que de refaire le calcul, déduire le put du call par la parité : $P=C-S_0+KP(0,T)$. [Prop. 7]

## Cesse d'être valide quand
Le symbole $P$ sans argument est un prix de put, $P(t,T)$ avec deux arguments est un zéro-coupon — la source emploie les deux sans le signaler. [§6.4]

## Origine
- exercice fpp/ex-18 : le put est l'instrument naturel d'un exportateur exposé à la baisse d'une devise ; le §9 ne traite que les stratégies sur actions [exo. 18]

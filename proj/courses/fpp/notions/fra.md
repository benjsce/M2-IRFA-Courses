---
id: fpp/fra
nom: Forward Rate Agreement
symbole: FRA
type: notion
statut: source
cas_de: fpp/prix-a-terme
valeur: sous-jacent $P(\cdot,S)$, strike écrit en taux
construite_a_partir_de:
- fpp/taux-forward
alias:
- forward rate agreement
refs:
- §2.3
- Déf. 7
---

## Ce que c'est
Un contrat qui fixe aujourd’hui le taux d’un emprunt futur entre $T$ et $S$. [§2.3, Déf. 7]

## Forme
$$P(t,T)=P(t,S)e^{K(S-T)}$$ [§2.3, Déf. 7]

## Ce qui la définit
Le strike d’un FRA s’écrit en taux : $K=\frac{1}{S-T}\ln\frac{P(t,T)}{P(t,S)}$. [§2.3, Déf. 7]

C’est un prix à terme dont le sous-jacent est le zéro-coupon $P(\cdot,S)$ : ce prix à terme vaut $F_{\mathrm{ZC}}=P(t,S)/P(t,T)$, relié au strike par $F_{\mathrm{ZC}}=e^{-K(S-T)}$ ; attention, les rapports sont inversés d’une écriture à l’autre. [ajout]

## Exemple minimal
$P(0,1)=0{,}9608$ et $P(0,2)=0{,}9048$ : le FRA $1\times2$ se traite à $K=6\%$. [ajout]

## Geste de calcul type
à venir [ajout]

## Cesse d'être valide quand
L’écriture en taux masque qu’il s’agit d’un forward ordinaire ; elle n’ajoute rien. [ajout]

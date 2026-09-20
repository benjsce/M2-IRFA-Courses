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

## Ce qui la définit
On ne connaît plus le coût de portage à l’avance : on le suit. La position est ajustée à chaque date pour que la valeur terminale reste celle visée. [§4.2.2]

## Exemple minimal
à venir [ajout]

## Geste de calcul type
à venir [ajout]

## Cesse d'être valide quand
Suppose des marchés sans friction et un rééquilibrage continu — l’hypothèse la plus fragile de tout l’édifice. [ajout]

---
id: fpp/contrat-a-prime
nom: Contrat à prime
type: abstraite
statut: ajout
cas_de: fpp/contrat-derive
valeur: une prime $\Pi_0>0$ à la signature
parametre: la forme du payoff
construite_a_partir_de:
- fpp/mesure-risque-neutre
- fpp/replication-dynamique
refs:
- §6
- §7
---

## Ce que c'est
Les options : le strike est donné, l’inconnue est le prix. [ajout]

## Ce que les membres partagent
Un flux est versé à la signature, donc l’invariant « valeur nulle » ne s’hérite pas. Le payoff est non linéaire. [ajout]

## Pourquoi ce niveau existe
Présent ici uniquement pour justifier le niveau au-dessus, et pour marquer où la branche suivante se greffe. [ajout]

## Cesse d'être valide quand
La réplication statique ne s’applique plus : c’est l’entrée dans Black & Scholes. [ajout]

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
Ce niveau n’est présent que pour justifier celui du dessus, et pour marquer où la branche suivante se greffe. [ajout]

## Le chemin jusqu'ici
Deux fils partent du même endroit. Le premier combine fpp/replication-statique, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) pour obtenir fpp/prix-a-terme, puis fpp/mesure-risque-neutre. Le second part de fpp/compte-capitalise et aboutit à fpp/replication-dynamique. [ajout]

La distinction que porte cette fiche — le strike est donné, l'inconnue est le prix — n'a de sens qu'une fois les deux modes de réplication disponibles. Un contrat à prime nulle se règle en statique ; un contrat à prime demande, lui, de rééquilibrer. [ajout]

## Cesse d'être valide quand
La réplication statique ne s’applique plus : c’est l’entrée dans Black & Scholes. [ajout]

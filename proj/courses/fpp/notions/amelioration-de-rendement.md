---
id: fpp/amelioration-de-rendement
nom: Amélioration de rendement
type: notion
statut: source
cas_de: fpp/strategie-optionnelle
valeur: on vend l’optionalité
construite_a_partir_de:
- fpp/call
- fpp/put
alias:
- return enhancement
- covered call
refs:
- §9.3
---

## Ce que c'est
Vendre des calls ou des puts pour encaisser la prime, en échange d’un profil de gain tronqué. [§9.3]

## Ce qui la définit
Exactement l’inverse du produit à capital protégé : on est cette fois du côté qui reçoit la prime, et qui porte donc le risque que l’acheteur a cédé. [§9.3, ajout]

## Exemple minimal
Vendre le call à la monnaie de l’exemple courant encaisse 9,93, au prix de toute la hausse au-delà de 100. [ajout]

## Geste de calcul type
Retrancher le payoff vendu du portefeuille existant : le gain est plafonné là où le strike se situe, et la prime encaissée décale le point mort. [ajout]

## Cesse d'être valide quand
La prime encaissée est le prix exact du risque cédé : ce n’est un rendement supplémentaire qu’en moyenne sous $\mathbb{Q}$, et jamais un repas gratuit. [ajout]

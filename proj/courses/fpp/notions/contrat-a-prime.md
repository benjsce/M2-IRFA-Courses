---
id: fpp/contrat-a-prime
nom: Contrat à prime
type: abstraite
statut: ajout
cas_de: fpp/contrat-derive
valeur: une prime strictement positive, payée à la signature
parametre: la forme du payoff
construite_a_partir_de:
- fpp/mesure-risque-neutre
- fpp/replication-dynamique
refs:
- §6
- §7
---

## Ce que c'est
Les contrats qu'on paie à la signature : le strike est **donné**, l’inconnue est **la prime**, ce que coûte le contrat aujourd'hui. [ajout]

## Ce que les membres partagent
Comme on paie à la signature, le contrat ne vaut pas zéro : c'est ce montant, la prime, qu'on cherche, alors qu'un contrat à prime nulle cherche le strike qui le rend gratuit. [ajout]

Le payoff est coudé : aucun portefeuille d'actions et de zéro-coupons fixé une fois pour toutes ne le reproduit, et c'est ce coude qui interdit la réplication statique. [ajout]

## Pourquoi ce niveau existe
Il réunit tout ce qui se paie à la signature, une option seule ou un assemblage d'options : dans tous les cas on paie une prime, et c'est elle qu'on cherche. [ajout]

## Le chemin jusqu'ici
Deux fils partent du même endroit. Le premier combine fpp/replication-statique, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) pour obtenir fpp/prix-a-terme, puis fpp/mesure-risque-neutre. Le second part de fpp/compte-capitalise et aboutit à fpp/replication-dynamique. [ajout]

Le premier fil fournit le calcul de la prime, une espérance actualisée ; le second, la raison pour laquelle ce calcul est un prix : un payoff coudé ne se reproduit qu'en réajustant le portefeuille au fil du temps. [ajout]

## Cesse d'être valide quand
rien dans le périmètre du cours [ajout]

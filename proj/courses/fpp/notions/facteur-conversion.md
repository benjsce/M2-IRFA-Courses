---
id: fpp/facteur-conversion
nom: Facteur de conversion
type: abstraite
statut: ajout
cas_de: fpp/coordonnees-flux
parametre: la coordonnée traversée
construite_a_partir_de: []
refs:
- §2.1
- §2.4
---

## Ce que c'est
Le nombre par lequel on multiplie un flux pour l’exprimer dans une autre coordonnée. [ajout]

## Ce que les membres partagent
Tous deux transforment un flux d’une coordonnée à une autre, multiplicativement et sans risque. Ils se composent, et ils commutent. [ajout]

## Pourquoi ce niveau existe
Le niveau n’existe que parce que la composition des deux est un objet du cours : le forward de change. Sans lui, chacune se suffirait à elle-même et cette abstraction serait décorative. [ajout]

## Cesse d'être valide quand
La composition ne suffit plus dès que le flux converti est aléatoire et corrélé au facteur : c’est le cas quanto. [ajout]

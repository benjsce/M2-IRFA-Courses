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
Le nombre par lequel on multiplie un flux pour le faire changer d’une coordonnée, de date ou de devise. [ajout]

## Ce que les membres partagent
Changer un flux de date et le changer de devise se font de la même façon : en le multipliant par un nombre connu aujourd'hui, sans risque. Le cours le dit lui-même : un facteur d'actualisation est un taux de change entre deux dates. [§2.1]

Les deux se composent, dans un ordre imposé. Un flux payé plus tard dans l'autre devise change d'abord de date, dans sa propre devise, puis de devise, au taux du jour. L'ordre inverse demanderait le taux de change de la date future, que personne ne connaît aujourd'hui. [§2.4, ajout]

## Pourquoi ce niveau existe
Le niveau n’existe que parce que la composition des deux est un objet du cours : le forward de change, qui fixe dès aujourd'hui ce taux de change futur. Sans lui, chacune se suffirait à elle-même et cette abstraction serait décorative. [§2.4, ajout]

## Cesse d'être valide quand
Les deux facteurs s'appliquent à des flux certains. Pour un flux aléatoire payé dans l'autre devise, multiplier ne suffit plus si le flux et le taux de change bougent ensemble : le prix dépend alors de la façon dont ils bougent l'un avec l'autre. [ajout]

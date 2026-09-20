---
id: fpp/couverture
nom: Couverture
type: principe
statut: source
construite_a_partir_de: []
alias:
- hedging
- se couvrir
refs:
- §8
- §7.1
---

## Ce que c'est
Se couvrir, c’est annuler la dépendance d’un portefeuille à un paramètre en prenant la position opposée à sa sensibilité. [§8]

## Ce qui la définit
La couverture en delta le montre en entier : on détient $-\partial C/\partial S$ actions contre une option, et le terme brownien disparaît du portefeuille. [§7.1]

Ce qui se généralise : à chaque paramètre du modèle correspond une dérivée du prix, et couvrir ce paramètre c’est neutraliser cette dérivée. [§8, §8.1]

## Cesse d'être valide quand
Une couverture n’annule la dépendance qu’au premier ordre et qu’à l’instant présent : elle doit être refaite, et le second ordre reste. [§8.2]

## Origine
- exercice fpp/ex-06 : se couvrir ne fait pas disparaître le coût, cela le fige — les 269,8 M€ sont payés dans les deux montages [ajout]
- exercice fpp/ex-18 : deux façons de ne pas annuler tout à fait la sensibilité — couverture partielle en notionnel, couverture asymétrique par option — se lisent sur le même graphique [exo. 18]
- exercice fpp/ex-20 : la sensibilité à couvrir n'est pas le notionnel initial mais la valeur finale de la position ; couvrir 1 M USD n'aurait couvert que 63 % du risque [exo. 20]

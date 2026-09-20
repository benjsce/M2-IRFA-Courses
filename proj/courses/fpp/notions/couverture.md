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

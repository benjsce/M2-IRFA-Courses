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
Se couvrir, c’est prendre, dans un autre actif, la quantité dont la sensibilité compense exactement celle du portefeuille. [§8]

## Ce qui la définit
**On connaît** la sensibilité du portefeuille à un paramètre : un call acheté sur une action à 100 gagne environ 0,618 quand l'action gagne 1. **On cherche** la position qui l'annule : vendre 0,618 action, qui perd 0,618 dans le même mouvement. Couvrir, c'est choisir la quantité qui ramène la sensibilité totale à zéro. [ajout]

![Trois cadres à la même échelle, gain selon le cours de l'action, qui vaut 100 aujourd'hui. Le call acheté gagne quand l'action monte ; 0,618 action vendue perd autant autour de 100 ; leur somme, la position couverte, ne bouge presque plus autour de 100. À 110, le call gagne 7,04 et les actions perdent 6,18 : il reste 0,86, le second ordre que la couverture n'annule pas.](figures/couverture.svg) [ajout]

Ce qui se généralise : à chaque paramètre du modèle correspond une dérivée du prix, et couvrir ce paramètre, c’est neutraliser cette dérivée. [§8, §8.1]

## Exemple minimal
Le call de strike 100, à un an, vaut 9,93 quand l'action vaut 100 (taux 4 %, volatilité 20 %). Contre 0,618 action vendue, si l'action passe à 101, le call gagne 0,63 et les actions perdent 0,62 : la position n'a presque pas bougé. [ajout]

## Cesse d'être valide quand
Une couverture n’annule la dépendance qu’au premier ordre et qu’à l’instant présent : elle doit être refaite, et le second ordre reste. [§8.2]

## Origine
- exercice fpp/ex-06 : se couvrir ne fait pas disparaître le coût, cela le fige. Air France, qui doit 300 M$ dans un an, les paie environ 269,8 M€ qu'elle se couvre par un contrat à terme ou par un emprunt en dollars [ajout]
- exercice fpp/ex-18 : deux façons de ne pas annuler tout à fait la sensibilité — couverture partielle en notionnel, couverture asymétrique par option — se lisent sur le même graphique [exo. 18]
- exercice fpp/ex-20 : la sensibilité à couvrir n'est pas le notionnel initial mais la valeur finale de la position ; couvrir 1 M USD n'aurait couvert que 63 % du risque [exo. 20]

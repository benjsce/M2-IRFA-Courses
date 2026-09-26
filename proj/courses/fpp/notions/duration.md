---
id: fpp/duration
nom: Sensibilité, duration
type: notion
statut: source
cas_de: fpp/sensibilite
valeur: le taux, sur un zéro-coupon
construite_a_partir_de:
- fpp/valeur-actuelle-nette
refs:
- Déf. 5
- Ex. 1
---

## Ce que c'est
De combien un prix bouge quand le taux bouge. [Déf. 5]

## Forme
$$\dfrac{\partial P(t,r)}{P(t,r)\,\partial r}=-t$$ [Déf. 5]

## Ce qui la définit
Une variation instantanée du taux agit sur toute la vie du titre : la sensibilité relative est la maturité elle-même. [Déf. 5]

## Le chemin jusqu'ici
La chaîne est la même que pour un contrat à prime nulle : fpp/convention-capitalisation, puis fpp/facteur-actualisation, puis fpp/valeur-actuelle-nette qui somme l'échéancier. [ajout]

Une fois le prix d'un échéancier écrit comme fonction du taux, la sensibilité n'est qu'une dérivée. C'est la première fois du cours qu'on dérive un prix ; la même opération reviendra pour les grecques, sur une autre variable. [ajout]

## Exemple minimal
Un zéro-coupon à 5 ans perd 5 % de sa valeur quand le taux monte de 100 points de base. [ajout]

![Une hausse de taux de 100 points de base, lue sur un échéancier : chaque zéro-coupon perd sa maturité en pour cent. Le titre à cinq ans est celui de l'exemple ; ceux à un, deux et dix ans sont ajoutés pour le dessin.](figures/duration.svg) [ajout]

## Geste de calcul type
Multiplier la maturité par la variation de taux : un zéro-coupon à cinq ans perd 5 % pour cent points de base. Sur un titre à flux multiples, le calcul se fait flux par flux, comme dans l’exemple du bullet bond. [Déf. 5, Ex. 1]

## Cesse d'être valide quand
Premier ordre seulement, et déplacement parallèle de la courbe. [ajout]

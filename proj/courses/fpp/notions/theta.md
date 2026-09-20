---
id: fpp/theta
nom: Theta
symbole: $\Theta$
type: notion
statut: source
cas_de: fpp/sensibilite
valeur: le temps qui passe
construite_a_partir_de:
- fpp/formule-black-scholes
alias:
- theta de Black et Scholes
refs:
- §8.2
---

## Ce que c'est
De combien le prix bouge quand le temps passe. [§8.2]

## Forme
$$\Theta=\dfrac{\partial P}{\partial t}$$ [§8.2]

## Ce qui la définit
Négatif pour l’acheteur d’option dans presque tous les cas : la valeur temps s’érode à mesure que l’échéance approche. [§8.2]

## Exemple minimal
Le call à la monnaie de l’exemple courant porte 6,00 de valeur temps, qui s’annule entièrement à l’échéance. [ajout]

## Geste de calcul type
Le theta est le loyer du gamma : ce qu’on paie chaque jour pour détenir de la convexité. [ajout]

## Cesse d'être valide quand
La table marque ce signe d’un astérisque, « presque toujours vrai » : les exceptions existent, notamment pour un put très en dedans. [§8.2]

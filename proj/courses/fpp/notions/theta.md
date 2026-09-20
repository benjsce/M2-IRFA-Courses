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

## Le chemin jusqu'ici
Le socle est exactement celui de fpp/formule-black-scholes, augmenté d'elle. Tout y sert à écrire la formule ; cette fiche ne fait que la dériver. [ajout]

Ce qui distingue les cinq grecques, c'est la variable, pas le chemin : le thêta est la dérivée par rapport au temps. Le socle est donc le même pour toutes, et il ne vaut la peine d'être lu qu'une fois. [ajout]

Le thêta est ce que coûte l'attente ; il est le pendant du gamma, l'équation de Black et Scholes les liant terme à terme. [ajout]

## Exemple minimal
Le call à la monnaie de l’exemple courant porte 6,00 de valeur temps, qui s’annule entièrement à l’échéance. [ajout]

## Geste de calcul type
Le theta est le loyer du gamma : ce qu’on paie chaque jour pour détenir de la convexité. [ajout]

## Cesse d'être valide quand
La table marque ce signe d’un astérisque, « presque toujours vrai » : les exceptions existent, notamment pour un put très en dedans. [§8.2]

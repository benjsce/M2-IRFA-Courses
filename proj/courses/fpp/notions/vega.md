---
id: fpp/vega
nom: Vega
symbole: $\mathcal{V}$
type: notion
statut: source
cas_de: fpp/sensibilite
valeur: la volatilité
construite_a_partir_de:
- fpp/formule-black-scholes
alias:
- vega de Black et Scholes
refs:
- §8.2
---

## Ce que c'est
De combien le prix bouge quand la volatilité bouge. [§8.2]

## Forme
$$\mathcal{V}=\dfrac{\partial P}{\partial\sigma}$$ [§8.2]

## Ce qui la définit
Positif pour le call comme pour le put : plus d’incertitude vaut plus cher des deux côtés, parce que le payoff est convexe. [§8.2]

La table écrit $SN(d_1)\sqrt{\tau}$ avec la fonction de répartition ; c’est la densité qu’il faut, $S\,n(d_1)\sqrt{\tau}$. Sur l’exemple courant la première donnerait 61,79, la seconde 38,14, et l’effet mesuré est 38,17 par unité de volatilité. [ajout]

## Le chemin jusqu'ici
Le socle est exactement celui de fpp/formule-black-scholes, augmenté d'elle. Tout y sert à écrire la formule ; cette fiche ne fait que la dériver. [ajout]

Ce qui distingue les cinq grecques, c'est la variable, pas le chemin : le véga est la dérivée par rapport à la volatilité. Le socle est donc le même pour toutes, et il ne vaut la peine d'être lu qu'une fois. [ajout]

Le véga est la seule grecque qui dérive par rapport à un paramètre que le modèle suppose constant — et c'est ce paradoxe qui en fait la plus employée. [ajout]

## Exemple minimal
Passer la volatilité de 20 % à 21 % fait passer le call de 9,93 à 10,30 : le vega vaut 0,38 par point de volatilité. [ajout]

## Geste de calcul type
Multiplier le vega par la variation de volatilité exprimée en points : c’est ainsi qu’on lit une position en volatilité. [§8.2]

## Cesse d'être valide quand
Le paramètre dérivé est justement celui que le modèle suppose constant : dériver par rapport à lui, c’est déjà sortir du modèle. [ajout]

## Origine
- exercice fpp/ex-15 : pour choisir une stratégie de volatilité, on ne regarde pas le profil de gain mais le signe du véga — le profil ne distingue pas l'achat de straddle de la vente de butterfly [ajout]

---
id: fpp/rho
nom: Rho
symbole: $\rho$
type: notion
statut: source
cas_de: fpp/sensibilite
valeur: le taux d’intérêt
construite_a_partir_de:
- fpp/formule-black-scholes
alias:
- rho de Black et Scholes
refs:
- §8.2
---

## Ce que c'est
De combien le prix bouge quand le taux d’intérêt bouge. [§8.2]

## Forme
$$\rho=\dfrac{\partial P}{\partial r}$$ [§8.2]

## Ce qui la définit
Positif pour un call, négatif pour un put : monter le taux abaisse la valeur actualisée du strike, donc renchérit le droit d’acheter. [§8.2]

## Exemple minimal
Si le taux tombe de 4 % à 3 %, le strike actualisé passe de 96,08 à 97,04 : le call perd et le put gagne. [ajout]

## Geste de calcul type
L’essentiel de l’effet passe par le seul terme $Ke^{-rT}N(d_2)$ : le dériver suffit à en lire le signe. [§8.2]

## Cesse d'être valide quand
Le modèle suppose le taux déterministe : comme pour le vega, on dérive par rapport à ce qu’on a supposé fixe. [ajout]

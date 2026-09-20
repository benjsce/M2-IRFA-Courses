---
id: fpp/valeur-temps
nom: Valeur temps
symbole: $\mathrm{TV}$
type: notion
statut: source
construite_a_partir_de:
- fpp/valeur-intrinseque
alias:
- time value
refs:
- Déf. 13
---

## Ce que c'est
Ce que le prix d’un payoff contient au-delà de sa valeur intrinsèque. [Déf. 13]

## Forme
$$\mathrm{Prix}=\mathrm{IV}+\mathrm{TV}$$ [Déf. 13]

## Ce qui la définit
Son signe est celui de la convexité de $g$ : positive quand $g$ est convexe, négative quand elle est concave. C’est Jensen, lu comme une décomposition de prix. [Déf. 13]

## Le chemin jusqu'ici
Le socle est celui de fpp/valeur-intrinseque, augmenté d'elle. [ajout]

C'est un socle de définition par différence : la valeur temps est ce qui reste quand on retire la valeur intrinsèque au prix. Elle n'ajoute aucun objet nouveau, seulement une soustraction — et c'est cette soustraction qui rend lisible ce que l'optionalité coûte. [ajout]

## Exemple minimal
Le call à la monnaie vaut 9,93 pour une valeur intrinsèque de 3,92 : la valeur temps est 6,00. [ajout]

## Geste de calcul type
Retrancher la valeur intrinsèque du prix. Ce qui reste mesure ce que le marché paie pour l’incertitude, et s’annule à l’échéance. [Déf. 13]

## Cesse d'être valide quand
La décomposition est une identité, mais le signe « positive si convexe » suppose que la seule source d’écart est Jensen — vrai pour un payoff de la valeur terminale seule. [Déf. 13]

## Origine
- exercice fpp/ex-15 : acheter un straddle à la monnaie, c'est acheter de la valeur temps pure — la valeur intrinsèque est nulle des deux côtés [ajout]

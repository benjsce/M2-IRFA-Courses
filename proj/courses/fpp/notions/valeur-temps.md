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

## Ce que les symboles modélisent
$\mathrm{TV}$ est un écart et non un prix : ce que le prix contient au-delà de la valeur intrinsèque. Le nom induit en erreur — il ne mesure pas seulement le temps restant, mais tout ce que l'aléa ajoute à une évaluation faite en la moyenne. [Déf. 13]

## Ce qui la définit
Son signe est celui de la convexité de $g$ : positive quand $g$ est convexe, négative quand elle est concave. C’est Jensen, lu comme une décomposition de prix. [Déf. 13]

## Le chemin jusqu'ici
Le socle est celui de fpp/valeur-intrinseque, la valeur intrinsèque elle-même en plus. Deux fils y mènent : fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre d'un côté, fpp/payoff de l'autre — de quoi évaluer, et quoi évaluer. [ajout]

C'est un socle de définition par différence : la valeur temps est ce qui reste quand on retire la valeur intrinsèque au prix. Elle n'ajoute aucun objet nouveau, seulement une soustraction — et c'est cette soustraction qui rend lisible ce que l'optionalité coûte. [ajout]

## Exemple minimal
Le call à la monnaie vaut 9,93 pour une valeur intrinsèque de 3,92 : la valeur temps est 6,00. [ajout]

![Le prix du call de l'exemple selon le sous-jacent, par la formule de Black et Scholes, et sa valeur intrinsèque, le payoff évalué en la moyenne. L'écart est la valeur temps : 6,00 à la monnaie, positive partout parce que le payoff est convexe.](figures/valeur-temps.svg) [ajout]

## Geste de calcul type
Retrancher la valeur intrinsèque du prix. Ce qui reste mesure ce que le marché paie pour l’incertitude, et s’annule à l’échéance. [Déf. 13]

## Cesse d'être valide quand
La décomposition est une identité, mais le signe « positive si convexe » suppose que la seule source d’écart est Jensen — vrai pour un payoff de la valeur terminale seule. [Déf. 13]

## Origine
- exercice fpp/ex-15 : acheter un straddle à la monnaie, c'est acheter de la valeur temps pure — la valeur intrinsèque est nulle des deux côtés [ajout]

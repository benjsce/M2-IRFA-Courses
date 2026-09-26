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
Le prix est **connu**, lu sur le marché ou donné par Black et Scholes ; la valeur intrinsèque se calcule **sans volatilité**, sur le seul prix forward. La valeur temps est **le reste** : ce que paie l'aléa. [Déf. 13, ajout]

Son signe est celui de la convexité de $g$, le payoff vu comme fonction de $S_T$ seul : positive quand $g$ est convexe, négative quand elle est concave. C’est Jensen, lu comme une décomposition de prix. [§6.2, Déf. 13]

## Le chemin jusqu'ici
Il faut deux montants pour faire une différence. Le prix complet est l'espérance du payoff de fpp/payoff sous fpp/mesure-risque-neutre, actualisée ; cette mesure vient de fpp/prix-a-terme, que fpp/replication-statique établit à partir de fpp/portage et de fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation). L'autre montant est fpp/valeur-intrinseque, le même payoff lu au prix forward. [ajout]

La valeur temps n'ajoute aucun objet nouveau, seulement cette soustraction — et c'est elle qui rend lisible ce que l'optionalité coûte. [ajout]

## Exemple minimal
Le call à la monnaie vaut 9,93 pour une valeur intrinsèque de 3,92 : la valeur temps est 6,00. [ajout]

![Le prix du call de l'exemple selon le sous-jacent, par la formule de Black et Scholes, et sa valeur intrinsèque, le payoff évalué en la moyenne. L'écart est la valeur temps : 6,00 à la monnaie, positive partout parce que le payoff est convexe.](figures/valeur-temps.svg) [ajout]

## Geste de calcul type
Retrancher la valeur intrinsèque du prix. Ce qui reste mesure ce que le marché paie pour l’incertitude, et s’annule à l’échéance. [Déf. 13]

## Cesse d'être valide quand
La décomposition est une identité, mais le signe « positive si convexe » suppose que la seule source d’écart est Jensen — vrai pour un payoff de la valeur terminale seule. [Déf. 13]

## Origine
- exercice fpp/ex-15 : acheter un straddle à la monnaie, c'est acheter de la valeur temps pure — la valeur intrinsèque est nulle des deux côtés [ajout]

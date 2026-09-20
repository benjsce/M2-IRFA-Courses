---
id: fpp/valeur-intrinseque
nom: Valeur intrinsèque
symbole: $\mathrm{IV}$
type: notion
statut: source
construite_a_partir_de:
- fpp/mesure-risque-neutre
- fpp/payoff
alias:
- intrinsic value
refs:
- Déf. 12
- §6.2
---

## Ce que c'est
Ce que vaudrait le payoff dans un monde sans aléa, c’est-à-dire évalué en la moyenne au lieu de la moyenne de l’évaluation. [Déf. 12]

## Forme
$$\mathrm{IV}=e^{-rT}\,g\big(\mathbb{E}(S_T)\big)$$ [Déf. 12]

## Ce qui la définit
On échange l’ordre de $g$ et de l’espérance : c’est exactement le terme que l’inégalité de Jensen sépare du vrai prix. [Déf. 12]

## Exemple minimal
Call de strike 100, $\mathbb{E}^{\mathbb{Q}}(S_1)=104{,}08$, $P(0,1)=0{,}9608$ : $\mathrm{IV}=3{,}92$. [ajout]

## Geste de calcul type
Calculer d’abord le forward, y appliquer le payoff, puis actualiser — trois opérations, sans volatilité. Tout ce que la volatilité ajoute est la valeur temps. [Déf. 12, Déf. 13]

## Cesse d'être valide quand
Ce n’est un prix que dans un modèle sans aléa ; dès qu’il y a de la volatilité, il manque la valeur temps. [Déf. 13]

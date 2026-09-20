---
id: dup/entropie
nom: Entropie
symbole: $H(P)$
type: notion
statut: source
construite_a_partir_de:
- dup/loterie
alias:
- Shannon entropy
- entropie de Shannon
refs:
- L1 slide 17
---

## Ce que c'est
Une mesure de l’incertitude d’une loterie qui ne regarde que les probabilités, jamais les montants. [L1 slide 17]

## Forme
$$H(P)=-\sum_i p_i\log p_i$$ [L1 slide 17]

## Ce qui la définit
Elle ne dépend pas de la distance entre les résultats, ce qui la rend inapte à mesurer le coût économique du risque de paiement. [L1 slide 17]

## Exemple minimal
$(49,\tfrac12;51,\tfrac12)$ et $(0,\tfrac12;100,\tfrac12)$ ont la même entropie, alors que la seconde est bien plus dispersée. [L1 slide 17]

## Geste de calcul type
La calculer si l’on veut mesurer l’imprévisibilité d’un tirage ; ne pas la calculer si l’on veut mesurer un risque de paiement — elle ignore les montants. [L1 slide 17]

## Cesse d'être valide quand
Elle mesure l’imprévisibilité, pas le risque de paiement : elle ne sert pas à classer des perspectives monétaires. [L1 slide 17]

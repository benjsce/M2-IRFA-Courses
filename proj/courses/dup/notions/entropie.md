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

## Ce que les symboles modélisent
$H(P)$ prend une loterie et rend un nombre, mais ne regarde que ses probabilités : remplacer 10 et 20 par 10 000 et 20 000 n'y change rien. C'est une mesure d'imprévisibilité et non de risque financier — elle est maximale quand tous les résultats sont également probables, quels qu'ils soient. [L1 slide 17]

## Ce qui la définit
Elle ne dépend pas de la distance entre les résultats, ce qui la rend inapte à mesurer le coût économique du risque de paiement. [L1 slide 17]

## Le chemin jusqu'ici
dup/loterie suffit, et rien de plus. [ajout]

L'entropie ne regarde que les probabilités et ignore les montants : deux loteries aux mêmes probabilités ont la même entropie, qu'on y gagne un euro ou un million. C'est ce qui la sépare de tout ce que le cours appellera « risque » — et la raison pour laquelle son socle se réduit à la loterie, sans aucune fonction d'utilité. [ajout]

## Exemple minimal
$(49,\tfrac12;51,\tfrac12)$ et $(0,\tfrac12;100,\tfrac12)$ ont la même entropie, alors que la seconde est bien plus dispersée. [L1 slide 17]

![Pour une loterie à deux résultats, l'entropie ne dépend que de la probabilité $p$ du premier : l'axe horizontal n'a pas de place pour les montants. Les deux loteries de l'exemple tombent sur le même point, au sommet, là où les résultats sont également probables. L'axe vertical n'est pas gradué, la fiche ne fixant pas la base du logarithme.](figures/entropie.svg) [ajout]

## Geste de calcul type
La calculer si l’on veut mesurer l’imprévisibilité d’un tirage ; ne pas la calculer si l’on veut mesurer un risque de paiement — elle ignore les montants. [L1 slide 17]

## Cesse d'être valide quand
Elle mesure l’imprévisibilité, pas le risque de paiement : elle ne sert pas à classer des perspectives monétaires. [L1 slide 17]

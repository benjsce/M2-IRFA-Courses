---
id: dup/effet-isolement
nom: Effet d’isolement
type: notion
statut: source
cas_de: dup/violation-de-l-independance
valeur: une même loterie présentée en une ou deux étapes
construite_a_partir_de:
- dup/utilite-esperee
alias:
- isolation effect
refs:
- L1 slide 48
- L1 slide 49
- L2 slide 8
- L2 slide 9
---

## Ce que c'est
Présenter la même loterie en deux étapes au lieu d’une change le choix. [L2 slide 8]

## Ce qui la définit
Le jeu en deux étapes — 0,75 de finir sans rien, puis un choix — produit exactement les mêmes loterie finales que le problème en une étape. Les arbres de décision des deux formulations ont les mêmes feuilles et les mêmes probabilités. [L2 slide 8, L2 slide 9]

Les sujets isolent la seconde étape et raisonnent comme si la première n’existait pas : ils retrouvent alors la certitude apparente de 3 000. [L2 slide 8]

## Le chemin jusqu'ici
Le socle commun : dup/loterie, dup/fonction-utilite, dup/utilite-esperee. [ajout]

La particularité est ailleurs : ce que cet effet attaque n'est pas un axiome de préférence mais une hypothèse de **description** — qu'une loterie en deux étapes soit la même chose que sa réduction en une. L'utilité espérée la suppose sans la dire ; c'est la raison de la dépendance. [ajout]

## Exemple minimal
$(4\,000\,;0{,}8)$ contre 3 000 sûrs après un premier tirage à 0,25, c’est $(4\,000\,;0{,}2)$ contre $(3\,000\,;0{,}25)$. [L2 slide 8]

## Geste de calcul type
Réduire l’arbre en une étape en multipliant les probabilités le long de chaque branche, puis comparer au problème en une étape. [L2 slide 9]

## Cesse d'être valide quand
La violation porte ici sur la réduction des loteries composées, pas sur l’indépendance seule : c’est un axiome distinct que le modèle de référence suppose aussi. [ajout]

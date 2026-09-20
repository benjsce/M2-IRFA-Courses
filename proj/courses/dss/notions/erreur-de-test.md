---
id: dss/erreur-de-test
nom: Erreur de test
type: notion
statut: source
construite_a_partir_de:
- dss/apprentissage-supervise
alias:
- test error
refs:
- slide 37
- slide 38
---

## Ce que c'est
L'erreur d'un modèle sur des observations qu'il n'a pas servi à ajuster. [slide 37]

## Ce qui la définit
L'erreur d'apprentissage est une mauvaise estimation de l'erreur de test, et elle l'est toujours dans le même sens : elle la sous-estime. C'est pourquoi le modèle complet a toujours la plus petite RSS et le plus grand $R^2$ sans être le meilleur. [slide 37]

Le cours donne deux façons de l'atteindre : indirectement, en corrigeant l'erreur d'apprentissage d'une pénalité pour le nombre de variables ; directement, par un jeu de validation ou par validation croisée. [slide 38]


## Le chemin jusqu'ici
Tout part de dss/apprentissage-supervise : sans sortie désirée, il n'y a pas d'erreur à mesurer. [ajout]

L'erreur de test porte sur les mêmes couples, mais sur des observations tenues à l'écart de l'ajustement. Cette séparation est la première du chapitre, et presque tout ce qui suit en dépend. [ajout]

## Cesse d'être valide quand
En grande dimension, le cours interdit d'invoquer la RSS, les p-values ou le $R^2$ calculés sur les données d'apprentissage comme preuve d'un bon ajustement. [slide 94]

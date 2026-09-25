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
L'erreur d'apprentissage est en général une mauvaise estimation de l'erreur de test. Le modèle qui contient tous les prédicteurs a toujours la plus petite RSS et le plus grand $R^2$, parce que ces deux quantités mesurent l'erreur d'apprentissage ; il n'est pas pour autant le meilleur. [slide 37]

Son défaut a un sens : en moyenne, elle sous-estime l'erreur de test, puisque le modèle a été ajusté sur ces données-là, et d'autant plus qu'il a de variables. Sur un échantillon particulier, l'écart peut être plus grand ou plus petit ; c'est en espérance que le biais est garanti. [ajout]

Le cours donne deux façons de l'atteindre : indirectement, en corrigeant l'erreur d'apprentissage d'une pénalité pour le nombre de variables ; directement, par un jeu de validation ou par validation croisée. [slide 38]


## Le chemin jusqu'ici
Tout part de dss/apprentissage-supervise : sans sortie désirée, il n'y a pas d'erreur à mesurer. [ajout]

L'erreur de test porte sur les mêmes couples, mais sur des observations tenues à l'écart de l'ajustement. Cette séparation est la première du chapitre, et presque tout ce qui suit en dépend. [ajout]

## Cesse d'être valide quand
En grande dimension, le cours interdit d'invoquer la RSS, les p-values ou le $R^2$ calculés sur les données d'apprentissage comme preuve d'un bon ajustement. [slide 94]

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
L'erreur d'un modèle mesurée sur des observations tenues à l'écart de son ajustement. [slide 37]

## Ce qui la définit
**Ce qu'on connaît**, c'est l'erreur d'apprentissage : l'erreur du modèle sur les observations qui ont servi à l'ajuster. **Ce qu'on cherche**, c'est l'erreur de test, sur des observations nouvelles, qu'on n'a pas encore. Le cours veut un modèle de faible erreur de test, pas de faible erreur d'apprentissage. [slide 37]

L'erreur d'apprentissage en est en général une mauvaise estimation, et elle se trompe dans un sens connu : elle tend à sous-estimer l'erreur de test, puisque le modèle a été ajusté sur ces données-là. [slide 37, slide 41]

Le cours donne deux façons d'estimer l'erreur de test sans observations nouvelles : indirectement, en corrigeant l'erreur d'apprentissage d'une pénalité pour le nombre de variables ; directement, par un jeu de validation ou par validation croisée. [slide 38]


## Le chemin jusqu'ici
Tout part de dss/apprentissage-supervise : sans sortie désirée, il n'y a pas d'erreur à mesurer. [ajout]

L'erreur de test porte sur des couples de même nature, que l'ajustement n'a pas vus. Cette séparation est la première du chapitre, et presque tout ce qui suit en dépend. [ajout]

## Exemple minimal
Sur les 20 clients, la régression de la perte sur l'endettement et le revenu a une erreur quadratique moyenne de 1,12 : c'est le connu. Sur 20 000 clients nouveaux, elle est de 1,16 : c'est ce qu'on cherchait. Une banque n'a jamais ces clients-là ; on peut les tirer ici parce que les données sont simulées. [ajout]

## Cesse d'être valide quand
En grande dimension, le cours interdit d'invoquer la RSS, les p-values ou le $R^2$ calculés sur les données d'apprentissage comme preuve d'un bon ajustement. [slide 94]

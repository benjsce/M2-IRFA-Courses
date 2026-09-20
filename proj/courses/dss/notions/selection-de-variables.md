---
id: dss/selection-de-variables
nom: Sélection de variables
type: principe
statut: source
construite_a_partir_de:
- dss/moindres-carres-ordinaires
- dss/interpretabilite
alias:
- feature selection
- variable selection
refs:
- slide 27
- slide 28
---

## Ce que c'est
Remplacer l'ajustement par moindres carrés sur tous les prédicteurs par une procédure qui en réduit le nombre effectif. [slide 28]

## Ce qui la définit
Deux raisons, et elles ne sont pas de même nature : la précision de prédiction, qui se dégrade quand $n$ n'est pas beaucoup plus grand que $p$, et l'interprétabilité, qui se dégrade dès que des variables sans effet restent dans le modèle. [slide 25]

Le cours en donne trois familles et les nomme sur une seule slide : retirer des prédicteurs, contraindre leurs coefficients, ou projeter l'espace des prédicteurs. Les trois arrivent au même endroit par des chemins qui ne se ressemblent pas. [slide 28]

Une variable bien choisie améliore le modèle ; trop de variables le dégradent. Le chapitre entier consiste à rendre cette phrase opératoire. [slide 27]


## Le chemin jusqu'ici
Deux fils y mènent. dss/apprentissage-supervise puis dss/moindres-carres-ordinaires donnent la méthode à améliorer ; dss/interpretabilite donne la seconde raison de le faire. [ajout]

Les deux raisons ne sont pas de même nature et le cours les sépare : la précision se dégrade quand $n$ n'est pas beaucoup plus grand que $p$, l'interprétabilité se dégrade dès qu'une variable inutile reste dans le modèle. [ajout]

## Cesse d'être valide quand
Aucune des trois familles ne garantit de trouver le meilleur sous-ensemble : ce sont des heuristiques ou des contraintes, pas des optimums. [slide 36]

---
id: dss/apprentissage-inductif
nom: Apprentissage inductif
type: notion
statut: source
construite_a_partir_de:
- dss/apprentissage-supervise
alias:
- inductive learning
refs:
- slide 133
- slide 137
---

## Ce que c'est
Chercher, parmi des hypothèses, celle qui approche le mieux la fonction dont on ne connaît que des exemples. [slide 133]

## Ce qui la définit
Le schéma a quatre pièces : un environnement fournit des exemples $(x, f(x))$, un système d'apprentissage en induit un modèle $h(x)$, et l'on espère $h(x)\approx f(x)$ sur des exemples de test. [slide 133]

Le cours résume le problème en deux mots : représentation et recherche. Il faut d'abord se donner une famille d'hypothèses, ensuite y chercher la meilleure. [slide 133]


## Le chemin jusqu'ici
Un seul prérequis, dss/apprentissage-supervise : c'est lui qui fournit les couples formés d'une entrée et de la sortie désirée. [ajout]

Le cadre inductif ne fait qu'expliciter ce que ce régime suppose sans le dire — une famille d'hypothèses, et une recherche à l'intérieur de cette famille. [ajout]

## Cesse d'être valide quand
Le cadre ne dit rien du choix de la famille d'hypothèses, qui décide pourtant de ce que l'on peut apprendre — c'est exactement ce que la limite du perceptron va montrer. [ajout]

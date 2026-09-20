---
id: dss/limite-du-perceptron
nom: Limite du perceptron
type: notion
statut: source
construite_a_partir_de:
- dss/perceptron
alias:
- limitations of simple neural networks
- XOR problem
refs:
- slide 148
- slide 149
- slide 150
---

## Ce que c'est
Un perceptron ne forme que des frontières linéaires, et la plupart des fonctions ne sont pas linéairement séparables. [slide 148]

## Ce qui la définit
La démonstration tient en un exemple : le OU exclusif. Les quatre points de la table de vérité ne peuvent pas être séparés par une droite, et un seul neurone n'y arrive donc pas. [slide 149]

Deux neurones suffisent, et leurs résultats combinés donnent une bonne classification. C'est la couche cachée qui apparaît ici, par nécessité. [slide 149]

Le cours date l'effet de cette critique : publiée par Minsky et Papert en 1969, elle a paralysé la recherche sur les réseaux pendant quinze ans. [slide 148]


## Le chemin jusqu'ici
Il faut le perceptron entier : dss/apprentissage-supervise et dss/apprentissage-inductif, puis dss/reseau-de-neurones-artificiel et dss/fonction-discriminante-lineaire, qui donnent dss/perceptron. [ajout]

Une limite se démontre sur l'objet qu'elle limite. La fonction discriminante linéaire est ici doublement nécessaire : elle dit ce que le perceptron sait faire, et donc ce qu'il ne sait pas. [ajout]

## Exemple minimal
Sur le OU exclusif, $(0,0)\mapsto 0$, $(0,1)\mapsto 1$, $(1,0)\mapsto 1$, $(1,1)\mapsto 0$ : les deux classes sont en diagonale et aucune droite ne les sépare. [slide 149]

## Cesse d'être valide quand
La limite porte sur un neurone unique, pas sur les réseaux : des réseaux multicouches plus complexes traitent des problèmes plus difficiles. [slide 150]

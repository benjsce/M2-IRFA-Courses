---
id: dss/generalisation
nom: Généralisation
type: notion
statut: source
construite_a_partir_de:
- dss/erreur-de-test
- dss/reseau-multicouche
alias:
- generalization
refs:
- slide 165
- slide 166
- slide 167
- slide 171
---

## Ce que c'est
La capacité d'un réseau à répondre juste sur des cas qu'il n'a pas vus. [slide 165]

## Ce qui la définit
L'objectif est posé par l'absurde : sans généralisation, autant utiliser une table de correspondance. Apprendre n'a de sens que si l'on sort des exemples. [slide 165]

Le cours la définit comme une interpolation ou une régression sur un ensemble de points d'apprentissage : la question est celle de la forme prise entre les points. [slide 165]

Une régularité empirique est donnée sur le problème de parité : quand le nombre de cas d'apprentissage dépasse largement le nombre de poids, la généralisation a lieu. [slide 167]

D'où la question opératoire qui organise la suite : comment contrôler le nombre de poids effectifs. [slide 171]


## Le chemin jusqu'ici
Deux fils. Le premier va de dss/apprentissage-supervise et dss/apprentissage-inductif à dss/fonction-discriminante-lineaire et dss/reseau-de-neurones-artificiel, puis à dss/perceptron, dss/limite-du-perceptron et dss/fonction-d-activation, d'où sort dss/reseau-multicouche. Le second est dss/erreur-de-test. [ajout]

La généralisation est la question posée au réseau une fois qu'il existe : que fait-il entre les points d'apprentissage. Il fallait donc le réseau complet d'un côté, et la notion d'erreur hors échantillon de l'autre. [ajout]

## Exemple minimal
Sur la parité à 10 bits, l'erreur de test s'effondre quand la fraction de cas utilisés à l'apprentissage augmente. [slide 167]

## Cesse d'être valide quand
C'est une propriété observée, pas garantie : le cours passe aussitôt à une borne probabiliste pour en dire quelque chose de quantitatif. [slide 168]

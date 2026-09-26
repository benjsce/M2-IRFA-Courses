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

Son exemple est le problème de parité : $n$ bits en entrée, et le réseau doit répondre 1 quand le nombre de bits à 1 est impair. Il y a $2^n$ cas possibles, on ne lui en montre que $m$, et la question est de savoir s'il répondra juste sur tous les autres. [slide 166, ajout]

Une régularité empirique en ressort : quand le nombre de cas d'apprentissage dépasse largement le nombre de poids, la généralisation a lieu. D'où la question opératoire qui organise la suite : comment contrôler le nombre de poids effectifs, c'est-à-dire de ceux qui pèsent vraiment dans la réponse, par opposition à ceux que l'entraînement laisse près de zéro ou n'a pas eu le temps de régler. [slide 167, slide 171, ajout]

## Le chemin jusqu'ici
La généralisation se mesure sur des cas mis de côté : c'est dss/erreur-de-test, l'erreur sur des observations qui n'ont pas servi à l'ajustement, qui dit si le réseau répond juste hors de ses exemples. [ajout]

Le réseau interrogé est un dss/reseau-multicouche. Il a assez de poids pour apprendre ses exemples par cœur, ce qui rend la question pressante ; il les doit à une couche cachée, que la dss/limite-du-perceptron a rendue nécessaire et qu'une dss/fonction-d-activation lisse permet d'entraîner. [ajout]

Chacun de ses nœuds reprend le dss/perceptron, l'unité d'un dss/reseau-de-neurones-artificiel qui calcule une dss/fonction-discriminante-lineaire. Le tout apprend à partir d'exemples, au sens de dss/apprentissage-inductif, étiquetés de la réponse attendue, au sens de dss/apprentissage-supervise ; généraliser, c'est justement répondre sans étiquette sous les yeux. [ajout]

## Exemple minimal
Sur la parité à 10 bits, l'erreur de test s'effondre quand la fraction de cas utilisés à l'apprentissage augmente. Pour une banque, un réseau qui prédit exactement la perte de ses 20 anciens clients, et mal celle des nouveaux, n'a rien appris d'utile. [slide 167, ajout]

## Cesse d'être valide quand
C'est une propriété observée, pas garantie : le cours passe aussitôt à une borne probabiliste pour en dire quelque chose de quantitatif. [slide 168]

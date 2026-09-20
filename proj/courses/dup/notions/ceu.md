---
id: dup/ceu
nom: Utilité espérée de Choquet
type: notion
statut: source
cas_de: dup/reponse-a-l-ambiguite
valeur: une capacité non additive
construite_a_partir_de:
- dup/aversion-a-l-ambiguite
alias:
- Choquet expected utility
- CEU
refs:
- L1 slide 64
---

## Ce que c'est
Remplacer la probabilité additive par une capacité, qui pondère les événements sans que les poids somment à un. [L1 slide 64]

## Ce qui la définit
Les poids de décision peuvent alors refléter la non-additivité des croyances et l’ambiguïté d’un événement, ce qu’une probabilité interdit par construction. [L1 slide 64]

## Le chemin jusqu'ici
Le socle est celui de l'autre réponse à l'ambiguïté : dup/acte et dup/fonction-utilite se combinent en dup/utilite-esperee-subjective, que dup/principe-de-la-chose-sure rend possible et que dup/paradoxe-d-ellsberg met en défaut, d'où dup/aversion-a-l-ambiguite. [ajout]

Ce qui est propre à celle-ci : on garde une seule mesure mais on lui retire l'additivité. Une capacité peut attribuer aux deux moitiés d'un événement moins que le tout, et c'est exactement ce défaut d'additivité qui encode l'aversion à l'ambiguïté. [ajout]

## Exemple minimal
Une capacité qui donne $1/3$ au rouge et moins de $1/3$ au noir, alors que leurs complémentaires ne somment pas à un. [ajout]

## Geste de calcul type
Intégrer au sens de Choquet : ordonner les conséquences, puis pondérer par les différences de capacité des ensembles emboîtés — le même geste que l’utilité dépendante du rang, transposé aux événements. [ajout]

## Cesse d'être valide quand
Le modèle décrit l’ambiguïté sans dire d’où vient la capacité ; la calibrer demande davantage d’observations qu’une probabilité. [ajout]

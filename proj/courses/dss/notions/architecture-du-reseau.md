---
id: dss/architecture-du-reseau
nom: Architecture du réseau
type: notion
statut: source
construite_a_partir_de:
- dss/garantie-pac
alias:
- network design
- network architecture
refs:
- slide 176
- slide 177
---

## Ce que c'est
Le choix du nombre de couches, du nombre de nœuds par couche et des connexions entre eux. [slide 176]

## Ce qui la définit
Ce choix détermine le nombre de poids du réseau, et c'est par là qu'il commande la généralisation. [slide 176]

La connectivité est un second levier : restreindre l'espace des hypothèses par une connectivité sélective, des poids partagés ou des connexions récursives. [slide 177]

Le cours mentionne des méthodes automatiques dans les deux sens : l'augmentation par corrélation en cascade, et l'élagage ou l'élimination de poids. [slide 176]


## Le chemin jusqu'ici
Deux fils. dss/apprentissage-supervise, dss/apprentissage-inductif, dss/fonction-discriminante-lineaire, dss/reseau-de-neurones-artificiel, dss/perceptron, dss/limite-du-perceptron et dss/fonction-d-activation donnent dss/reseau-multicouche, l'objet à dimensionner ; dss/erreur-de-test, dss/generalisation et dss/garantie-pac donnent le critère. [ajout]

Sans la borne, le nombre de nœuds cachés resterait une question de goût. Avec elle, il se compare au nombre d'exemples disponibles, et le compromis devient chiffrable. [ajout]

## Exemple minimal
Un réseau 20-20-1 compte 441 poids : $20\times20$ connexions entrée-caché, 20 connexions caché-sortie, plus les biais. [slide 169]

## Geste de calcul type
Compter les poids avant d'entraîner, et les comparer au nombre d'exemples disponibles par la borne $m>W/\varepsilon$. C'est ce rapport, pas l'intuition, qui dimensionne le réseau. [slide 168, slide 170]

## Cesse d'être valide quand
Le cours ne donne aucune règle de choix du nombre de couches : seulement des méthodes automatiques et un compromis à trouver. [slide 176]

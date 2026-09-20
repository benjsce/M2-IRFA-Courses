---
id: dss/descente-avec-inertie
nom: Descente avec inertie
symbole: $\alpha$
type: notion
statut: source
construite_a_partir_de:
- dss/retropropagation
alias:
- momentum descent
refs:
- slide 161
---

## Ce que c'est
Ajouter à la mise à jour une fraction de la mise à jour précédente. [slide 161]

## Forme
$$\Delta w_{ij}(t)=\eta\,d_j o_i+\alpha\,\Delta w_{ij}(t-1),\qquad 0<\alpha<1$$ [slide 161]

## Ce qui la définit
Le terme ajouté garde la direction du pas précédent, comme l'inertie d'une bille. Trois effets suivent : la direction se maintient, les petits minima locaux sont franchis, et le pas grandit quand le gradient est stable. [slide 161]

Cela revient à faire varier le taux d'apprentissage effectif, sans le changer explicitement. [slide 161]


## Le chemin jusqu'ici
Le socle est celui de la rétropropagation, augmenté de celle-ci : dss/apprentissage-supervise, dss/apprentissage-inductif, dss/fonction-discriminante-lineaire, dss/reseau-de-neurones-artificiel, dss/perceptron, dss/limite-du-perceptron, dss/fonction-d-activation, dss/reseau-multicouche, dss/regle-delta, dss/descente-de-gradient et dss/retropropagation. [ajout]

L'inertie n'est qu'un terme ajouté à l'équation de mise à jour : elle ne change ni la machine ni le gradient, seulement la trajectoire suivie dans l'espace des poids. [ajout]

## Exemple minimal
Avec $\alpha=0{,}8$, la mise à jour retient huit dixièmes du déplacement précédent. [slide 184]

## Geste de calcul type
Si l'erreur stagne sur un plateau, augmenter l'inertie avant d'augmenter le taux d'apprentissage : c'est elle qui fait franchir les creux. [slide 161, slide 186]

## Cesse d'être valide quand
L'inertie n'explore pas l'espace des poids, elle ne fait que lisser la trajectoire : elle reste une méthode de gradient. [slide 162]

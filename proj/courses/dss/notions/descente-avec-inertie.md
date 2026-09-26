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
- slide 184
- slide 186
---

## Ce que c'est
Ajouter à chaque mise à jour d'un poids une fraction de la mise à jour précédente, pour que le pas s'allonge tant que le gradient garde sa direction. [slide 161]

## Forme
$$\Delta w_{ij}(t)=\eta\,d_j o_i+\alpha\,\Delta w_{ij}(t-1),\qquad 0<\alpha<1$$ [slide 161]

## Ce que les symboles modélisent
$\alpha$ est la fraction du déplacement précédent qu'on reconduit, entre zéro et un. Ce n'est pas un pas d'apprentissage : il ne dit pas de combien on avance, il dit à quel point on garde sa direction. [slide 161]

$\eta\,d_j o_i$ est la correction que la rétropropagation calculait déjà pour le poids $w_{ij}$ : le taux d'apprentissage $\eta$, fois l'erreur $d_j$ renvoyée au nœud $j$, fois la sortie $o_i$ du nœud qui l'alimente. $t$ numérote les mises à jour ; ce n'est pas la sortie désirée $t_j$. [slide 161, ajout]

## Ce qui la définit
**Connu** à chaque mise à jour : la correction que donne le gradient maintenant, et le déplacement qu'on vient de faire. **Cherché** : le nouveau déplacement. L'inertie le fait égal à la correction, plus $\alpha$ fois le déplacement précédent. [slide 161]

Tant que le gradient reste stable, chaque pas hérite du précédent, et les pas s'allongent jusqu'à un palier : la correction divisée par $1-\alpha$, cinq fois la correction quand $\alpha=0{,}8$. [slide 161, ajout]

![Douze mises à jour sur un gradient stable. Chaque barre est un déplacement du poids : en bas, la correction du gradient, 0,01 à chaque fois ; au-dessus, la part reconduite, 0,8 fois la barre précédente. Les barres s'allongent, 0,01 puis 0,018 puis 0,0244, jusqu'au palier de 0,05, cinq fois le pas sans inertie.](figures/descente-avec-inertie.svg) [ajout]

Le cours en tire trois effets, comme pour une bille qui roule : la direction se maintient, les petits minima locaux sont franchis, et le pas grandit sur un gradient stable. Cela revient à faire varier le taux d'apprentissage effectif sans toucher à $\eta$. [slide 161]

## Le chemin jusqu'ici
Tout vient de dss/retropropagation, qui fournit la correction $\eta\,d_j o_i$ de chaque poids ; l'inertie la garde telle quelle et ne fait que lui ajouter un terme. [ajout]

Cette correction est un pas de dss/descente-de-gradient, lui-même issu de dss/regle-delta, qui corrigeait un poids en proportion de l'erreur : l'inertie ne change pas la direction indiquée par le gradient, seulement la mémoire qu'on en garde d'un pas à l'autre. [ajout]

Les poids ainsi corrigés sont ceux d'un dss/reseau-multicouche : il a fallu la dss/limite-du-perceptron, un dss/perceptron seul ne tranchant que par une frontière droite, et une dss/fonction-d-activation lisse pour qu'une petite correction se voie à la sortie. [ajout]

Le perceptron lui-même est un dss/reseau-de-neurones-artificiel réduit à un nœud, qui calcule une dss/fonction-discriminante-lineaire. Il apprend à partir d'exemples, c'est le sens de dss/apprentissage-inductif, et d'exemples dont on connaît la bonne réponse, c'est celui de dss/apprentissage-supervise. [ajout]

## Exemple minimal
Avec $\alpha=0{,}8$, la valeur typique du cours, et une correction de 0,01 à chaque mise à jour, les déplacements valent 0,01, puis 0,018, puis 0,0244, et approchent 0,05. [slide 184, ajout]

## Geste de calcul type
À chaque mise à jour : calculer la correction de la rétropropagation, puis lui ajouter 0,8 fois le déplacement précédent ; au deuxième pas, $0{,}01+0{,}8\times0{,}01=0{,}018$. [slide 161, slide 184]

Si l'erreur chute puis se fige sur un palier, le cours conseille de réduire le taux d'apprentissage ou l'inertie : ce palier est rarement un minimum local. [slide 186]

## Cesse d'être valide quand
L'inertie n'explore pas l'espace des poids, elle ne fait que lisser la trajectoire : elle reste une méthode de gradient, là où des techniques plus avancées cherchent ailleurs que dans la direction du gradient. [slide 162]

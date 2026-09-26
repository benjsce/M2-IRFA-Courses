---
id: dss/protocole-d-entrainement
nom: Protocole d'entraînement
type: notion
statut: source
construite_a_partir_de:
- dss/retropropagation
- dss/validation-croisee
alias:
- network training
refs:
- slide 180
- slide 181
- slide 182
- slide 183
- slide 184
- slide 185
- slide 186
- slide 198
---

## Ce que c'est
Couper les exemples en trois jeux séparés, un pour apprendre, un pour régler, un pour juger, afin de pouvoir affirmer qu'un réseau est bien entraîné. [slide 180]

## Ce qui la définit
Trois jeux, pas deux. Le jeu d'apprentissage sert à ajuster les poids ; le jeu de réglage (le *validation test set* de la slide) sert à choisir les réglages ; le jeu de production, séparé, sert à juger. Puisque les réglages ont été choisis pour lui, le jeu de réglage donne une erreur trop optimiste : seule l'erreur sur le jeu de production, que rien n'a touché, mesure la généralisation. [slide 180, ajout]

Le découpage dépend de la quantité de données. Sur grand échantillon, un seul tirage au hasard : 70 % des exemples pour l'apprentissage et le réglage, 30 % pour la production, et un seul modèle. Sur petit échantillon, une validation croisée en dix blocs : neuf pour apprendre et régler, un pour juger, dix fois de suite ; l'erreur de généralisation est la moyenne des dix erreurs, avec leur écart type. [slide 181, slide 182]

![Les deux découpages du cours. En haut, grand échantillon : un seul tirage, 70 % pour apprendre et régler, 30 % pour le jeu de production. En bas, petit échantillon : dix blocs, neuf pour apprendre et régler, un pour juger, et chaque bloc juge à son tour. La part entre apprendre et régler n'est pas chiffrée par le cours ; elle est posée pour le dessin.](figures/protocole-d-entrainement.svg) [ajout]

Pour départager deux architectures, il faut encore un test statistique : McNemar après un découpage unique, un test $t$ apparié après validation croisée. [slide 183]

Les réglages eux-mêmes ont des valeurs typiques, un taux d'apprentissage de 0,1, une inertie de 0,8, un coût des poids de 0,1, et des poids de départ tirés au hasard dans une petite plage ; si l'erreur chute puis se fige, on réduit le taux ou l'inertie. Le cours conseille enfin d'essayer d'abord la meilleure méthode existante, et un réseau sans couche cachée. [slide 184, slide 185, slide 186, slide 198]

## Le chemin jusqu'ici
Le découpage en blocs vient de dss/validation-croisee, qui réserve tour à tour une part des données pour estimer l'erreur ; le protocole en fait la version petit échantillon de ses trois jeux. Ce qu'on estime ainsi est une dss/erreur-de-test, l'erreur sur des exemples qui n'ont pas servi à l'ajustement. [ajout]

Ce qu'on entraîne, ce sont les poids d'un réseau par dss/retropropagation, dont les réglages, taux d'apprentissage et inertie, sont précisément ce que le jeu de réglage sert à choisir. Chaque correction est un pas de dss/descente-de-gradient, qui suit la pente de l'erreur comme la dss/regle-delta le faisait pour un seul neurone. [ajout]

Le réseau est un dss/reseau-multicouche, dont la couche cachée répond à la dss/limite-du-perceptron et dont la dss/fonction-d-activation lisse rend l'entraînement possible. Ses nœuds reprennent le dss/perceptron, l'unité d'un dss/reseau-de-neurones-artificiel qui calcule une dss/fonction-discriminante-lineaire. [ajout]

Les exemples qu'on partage en trois jeux sont ceux de dss/apprentissage-inductif, étiquetés de la réponse attendue, au sens de dss/apprentissage-supervise : sans étiquette, aucun des trois jeux ne donnerait d'erreur. [ajout]

## Cesse d'être valide quand
Sur petit échantillon, on ne peut plus réserver trois jeux fixes : le jeu de production devient un bloc qui tourne, et l'erreur annoncée est une moyenne sur dix modèles, non celle d'un modèle. Avec 20 clients, chaque bloc n'en compterait que deux. [slide 182, ajout]

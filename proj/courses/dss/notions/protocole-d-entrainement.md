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
- slide 186
- slide 198
---

## Ce que c'est
L'organisation des jeux de données et des paramètres qui permet d'affirmer qu'un réseau est bien entraîné. [slide 180]

## Ce qui la définit
Trois jeux, pas deux : un jeu d'apprentissage, un jeu de test pour régler, et un jeu de production séparé contre lequel valider. Le cours insiste sur cette séparation. [slide 180]

Le protocole dépend de la quantité de données. Sur grand échantillon, un découpage aléatoire 70 / 30 suffit et ne produit qu'un modèle. Sur petit échantillon, une validation croisée en dix blocs produit dix modèles et donne l'erreur de généralisation par la moyenne et l'écart type des erreurs de test. [slide 181, slide 182]

Comparer deux architectures demande un test statistique, et lequel dépend du protocole : test de McNemar après un découpage sur grand échantillon, test $t$ apparié après validation croisée. [slide 183]


## Le chemin jusqu'ici
Deux fils. dss/apprentissage-supervise, dss/apprentissage-inductif, dss/fonction-discriminante-lineaire, dss/reseau-de-neurones-artificiel, dss/perceptron, dss/limite-du-perceptron, dss/fonction-d-activation, dss/reseau-multicouche, dss/regle-delta et dss/descente-de-gradient donnent dss/retropropagation, ce qu'on entraîne ; dss/erreur-de-test et dss/validation-croisee donnent la façon de découper les données. [ajout]

Le protocole est l'organisation de ce découpage : trois jeux plutôt que deux, et un test statistique quand il s'agit de départager deux architectures. [ajout]

## Ce qui reste libre
| paramètre | valeur typique | plage |
|---|---|---|
| taux d'apprentissage | 0,1 | 0,01 – 0,99 |
| inertie | 0,8 | 0,1 – 0,9 |
| coût des poids | 0,1 | 0,001 – 0,5 |
[slide 184]

## Cesse d'être valide quand
Le cours donne aussi une consigne d'ordre : essayer d'abord la meilleure méthode existante, et un réseau sans couche cachée, avant de complexifier. [slide 198]

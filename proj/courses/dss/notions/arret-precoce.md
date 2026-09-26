---
id: dss/arret-precoce
nom: Arrêt précoce
type: notion
statut: source
construite_a_partir_de:
- dss/generalisation
- dss/surapprentissage
alias:
- early stopping
- tuning
refs:
- slide 173
---

## Ce que c'est
Interrompre l'entraînement juste avant que l'erreur de surajustement n'apparaisse. [slide 173]

## Ce qui la définit
La procédure demande un jeu d'exemples séparé, distinct de l'apprentissage, et un suivi de l'erreur sur ce jeu pendant que le réseau apprend. [slide 173]

L'effet est indirect mais c'est le bon : arrêter tôt réduit le nombre de poids effectifs, sans toucher à l'architecture. [slide 173]

Le cours note que la plupart des systèmes récents automatisent cet arrêt. [slide 173]


## Le chemin jusqu'ici
Deux fils. dss/apprentissage-supervise, dss/apprentissage-inductif, dss/fonction-discriminante-lineaire, dss/reseau-de-neurones-artificiel, dss/perceptron, dss/limite-du-perceptron, dss/fonction-d-activation et dss/reseau-multicouche mènent à dss/generalisation ; dss/erreur-de-test mène à dss/surapprentissage. [ajout]

L'arrêt précoce se place exactement entre les deux : on interrompt l'entraînement au moment où le second commence à dégrader la première. [ajout]

## Exemple minimal
L'erreur d'apprentissage continue de baisser alors que celle du jeu de réglage remonte : c'est ce point de retournement qui fixe l'arrêt. [slide 173]

![Les deux erreurs au fil de l'entraînement, sans graduation puisque la source ne les chiffre pas. Celle de l'apprentissage baisse toujours ; celle du jeu de réglage baisse puis remonte, et l'arrêt se place à son minimum.](figures/arret-precoce.svg) [ajout]

## Geste de calcul type
Suivre deux courbes, pas une : celle de l'apprentissage ne dira jamais quand s'arrêter. [slide 173]

## Cesse d'être valide quand
Le jeu de réglage sert alors au choix du modèle : il ne peut plus servir à estimer la performance, ce qui oblige à un troisième jeu. [slide 180]

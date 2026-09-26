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
- slide 180
---

## Ce que c'est
Interrompre l'entraînement juste avant que l'erreur de surajustement n'apparaisse. [slide 173]

## Ce qui la définit
La procédure demande un jeu d'exemples séparé, distinct de l'apprentissage, le jeu de réglage (*test or tuning set* sur la slide), et un suivi de l'erreur sur ce jeu pendant que le réseau apprend. [slide 173]

**Connu**, itération après itération : l'erreur sur le jeu de réglage. **Cherché** : l'itération où s'arrêter, celle où cette erreur est la plus basse. [slide 173, ajout]

Arrêter tôt réduit le nombre de poids effectifs, sans toucher à l'architecture : les poids restent près de leur valeur de départ, comme s'il y en avait moins qui pèsent vraiment dans la réponse. [slide 173, ajout]

## Le chemin jusqu'ici
Ce que l'arrêt protège, c'est dss/generalisation : répondre juste sur des cas qu'on n'a pas vus. Ce qui la menace, c'est dss/surapprentissage, un modèle qui finit par décrire le bruit de ses exemples ; on interrompt l'entraînement au moment où le surapprentissage commence à dégrader la généralisation. [ajout]

Ce moment se lit sur une dss/erreur-de-test, l'erreur sur des exemples qui n'ont pas servi à ajuster les poids : c'est le rôle du jeu de réglage. [ajout]

Le réseau qu'on arrête est un dss/reseau-multicouche, assez riche pour apprendre par cœur : sa couche cachée répond à la dss/limite-du-perceptron, et sa dss/fonction-d-activation lisse permet de l'entraîner par petites corrections successives : ce sont les itérations entre lesquelles on choisit où s'arrêter. Chacun de ses nœuds reprend le dss/perceptron, l'unité d'un dss/reseau-de-neurones-artificiel qui calcule une dss/fonction-discriminante-lineaire. [ajout]

Il apprend à partir d'exemples, au sens de dss/apprentissage-inductif, dont la réponse est connue, au sens de dss/apprentissage-supervise : c'est ce qui permet de mesurer une erreur sur chaque jeu. [ajout]

## Exemple minimal
L'erreur d'apprentissage continue de baisser alors que celle du jeu de réglage remonte : c'est ce point de retournement qui fixe l'arrêt. [slide 173]

![Les deux erreurs au fil de l'entraînement, sans graduation puisque la source ne les chiffre pas. Celle de l'apprentissage baisse toujours ; celle du jeu de réglage baisse puis remonte, et l'arrêt se place à son minimum.](figures/arret-precoce.svg) [ajout]

## Geste de calcul type
Suivre deux courbes, pas une : celle de l'apprentissage ne dira jamais quand s'arrêter. La plupart des systèmes récents automatisent cet arrêt. [slide 173]

## Cesse d'être valide quand
Le jeu de réglage sert alors au choix du modèle : il ne peut plus servir à estimer la performance, ce qui oblige à un troisième jeu. [slide 180]

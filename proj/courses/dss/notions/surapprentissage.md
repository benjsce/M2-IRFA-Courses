---
id: dss/surapprentissage
nom: Surapprentissage
type: notion
statut: source
construite_a_partir_de:
- dss/erreur-de-test
alias:
- overfitting
- over-training
refs:
- slide 27
- slide 32
- slide 172
---

## Ce que c'est
Un modèle qui décrit le bruit du jeu d'apprentissage au lieu de la relation sous-jacente. [slide 27]

## Ce qui la définit
Le signe est un écart : la performance sur les données d'apprentissage est excellente, celle sur des données nouvelles est mauvaise. Un polynôme de degré 15 passe joliment par les points, et un autre échantillon de la même population ne suivra pas la courbe. [slide 27]

Plus l'espace de recherche est grand, plus la chance est forte de trouver un modèle qui a l'air bon sur l'apprentissage sans avoir de pouvoir prédictif. [slide 32]

Le cours y oppose le rasoir d'Occam : le modèle le plus simple qui explique la majeure partie des données est en général le meilleur. [slide 172]


## Le chemin jusqu'ici
dss/apprentissage-supervise, puis dss/erreur-de-test. [ajout]

Le surapprentissage est un écart entre deux erreurs ; sans la seconde, on ne le verrait pas. C'est pourquoi le cours pose l'erreur de test avant de le nommer. [ajout]

## Cesse d'être valide quand
Ajouter des variables n'est pas toujours nuisible : une variable réellement liée à la réponse fait baisser l'erreur de test. C'est le bruit ajouté qui coûte, pas le nombre en soi. [slide 93]

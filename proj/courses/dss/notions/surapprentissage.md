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
- slide 37
- slide 172
---

## Ce que c'est
Un modèle qui décrit le bruit du jeu d'apprentissage au lieu de la relation sous-jacente. [slide 27]

## Ce qui la définit
Le signe est un écart qui se creuse : chaque variable ajoutée fait baisser l'erreur d'apprentissage, mais l'erreur sur des données nouvelles finit par remonter. Le modèle qui contient tous les prédicteurs a toujours la plus petite erreur d'apprentissage ; il n'est pas pour autant le meilleur. Le cours l'illustre par un polynôme de degré 15, qui passe joliment par les points et qu'un autre échantillon ne suivra pas. [slide 27, slide 37]

![Les 20 clients du parcours. En ajoutant les prédicteurs un à un, l'erreur mesurée sur les clients d'apprentissage baisse à chaque pas. Celle mesurée sur 20 000 clients nouveaux baisse tant qu'on ajoute l'endettement et le revenu, puis remonte avec chacune des trois variables sans lien avec la perte.](figures/surapprentissage.svg) [ajout]

L'erreur de test, seule, est un nombre ; le surapprentissage est son écart à l'erreur d'apprentissage, et la façon dont cet écart grandit quand on ajoute des variables sans lien avec la réponse. [ajout]

Le cours y oppose le rasoir d'Occam : le modèle le plus simple qui explique la majeure partie des données est en général le meilleur. [slide 172]


## Le chemin jusqu'ici
dss/apprentissage-supervise fournit les exemples sur lesquels le modèle apprend, et avec eux l'erreur d'apprentissage ; dss/erreur-de-test fournit l'erreur sur des exemples qu'il n'a pas vus. Le surapprentissage est l'écart entre les deux : sans la seconde, on ne le verrait pas. [ajout]

## Exemple minimal
Sur les 20 clients, ajouter à l'endettement et au revenu trois variables sans lien avec la perte fait baisser l'erreur d'apprentissage de 1,12 à 0,98 et monter l'erreur de test de 1,16 à 1,83 : l'écart passe de 0,04 à 0,85. [ajout]

## Cesse d'être valide quand
Ajouter des variables n'est pas toujours nuisible : une variable réellement liée à la réponse fait baisser l'erreur de test. C'est le bruit ajouté qui coûte, pas le nombre en soi. [slide 93]

---
id: dss/apprentissage-profond
nom: Apprentissage profond
type: notion
statut: source
construite_a_partir_de:
- dss/reseau-multicouche
alias:
- deep learning
refs:
- slide 6
- slide 8
- slide 17
---

## Ce que c'est
Filtrer les données à travers plusieurs couches de réseaux de neurones pour en extraire des caractéristiques et améliorer la classification. [slide 6]

## Ce qui la définit
Ce que le cours met en avant n'est pas la profondeur mais ce qu'elle produit : les caractéristiques ne sont plus fournies, elles sont construites par les couches successives. [slide 6, slide 8]

Le schéma d'usage est en deux temps, entraînement puis déploiement : à l'entraînement les erreurs sont renvoyées vers l'arrière, au déploiement le réseau ne fait plus que propager vers l'avant. [slide 8]

Deux familles sont nommées sans être traitées : réseaux récurrents et réseaux convolutifs. [slide 6]

## Le chemin jusqu'ici
La profondeur n'ajoute aucun objet : elle empile les couches cachées d'un dss/reseau-multicouche. Ce qui change est ce qu'on en attend, que les couches construisent elles-mêmes les caractéristiques au lieu de les recevoir toutes faites. [ajout]

Empiler n'a de sens que parce que chaque couche est non linéaire, grâce à sa dss/fonction-d-activation : des couches purement linéaires se ramèneraient à une seule, et l'on retomberait sur la dss/limite-du-perceptron : un dss/perceptron seul, qui calcule une dss/fonction-discriminante-lineaire, ne trace qu'une frontière droite. [ajout]

Chaque nœud reste celui d'un dss/reseau-de-neurones-artificiel, dont les poids s'apprennent sur des exemples, comme le veut dss/apprentissage-inductif, et sur des exemples étiquetés : c'est dss/apprentissage-supervise, le cadre du schéma d'entraînement du cours. [ajout]

## Cesse d'être valide quand
La promesse d'améliorer la classification n'est pas tenue d'office : dans l'étude comparée du cours, sur un jeu de crédit, l'apprentissage profond classe moins bien que la régression logistique. Le cours ne l'enseigne pas, il le situe. [slide 17]

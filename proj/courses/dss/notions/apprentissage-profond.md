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
---

## Ce que c'est
Filtrer les données à travers plusieurs couches de réseaux de neurones pour en extraire des caractéristiques et améliorer la classification. [slide 6]

## Ce qui la définit
Ce que le cours met en avant n'est pas la profondeur mais ce qu'elle produit : les caractéristiques ne sont plus fournies, elles sont construites par les couches successives. [slide 6, slide 8]

Le schéma d'usage est en deux temps, entraînement puis déploiement : à l'entraînement les erreurs sont renvoyées vers l'arrière, au déploiement le réseau ne fait plus que propager vers l'avant. [slide 8]

Deux familles sont nommées sans être traitées : réseaux récurrents et réseaux convolutifs. [slide 6]


## Le chemin jusqu'ici
Tout le chemin des réseaux : dss/apprentissage-supervise et dss/apprentissage-inductif donnent dss/fonction-discriminante-lineaire et dss/reseau-de-neurones-artificiel, puis dss/perceptron, dont dss/limite-du-perceptron et dss/fonction-d-activation ouvrent dss/reseau-multicouche. [ajout]

La profondeur n'ajoute aucun objet : elle empile les couches déjà définies. Ce qui change est ce qu'on en attend — que les couches construisent elles-mêmes les caractéristiques au lieu de les recevoir toutes faites. [ajout]

## Cesse d'être valide quand
Le cours ne l'enseigne pas : il le situe dans sa carte d'ouverture et dans les résultats comparés, où l'apprentissage profond obtient un GINI de 44,92, inférieur à celui de la régression logistique. [slide 17]

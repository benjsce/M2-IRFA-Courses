---
id: fpp/sensibilite
nom: Sensibilité
type: abstraite
statut: source
cas_de: fpp/couverture
parametre: la variable par rapport à laquelle on dérive le prix
construite_a_partir_de: []
alias:
- greeks
- grecques
- sensitivities
refs:
- §8.1
- §8.2
---

## Ce que c'est
La dérivée d’un prix par rapport à l’un des paramètres dont il dépend. [§8.1]

## Ce que les membres partagent
Toutes répondent à la même question posée sur une variable différente : de combien bouge le prix si ce paramètre bouge d’une unité. Et toutes se lisent comme la quantité à détenir en sens inverse pour se couvrir. [§8.1, §8.2]

La table du §8.2 les donne ensemble, avec pour chacune le sens de variation du prix, de la valeur intrinsèque et de la valeur temps. [§8.2]

## Pourquoi ce niveau existe
Six dérivées que le cours présente dans une seule table, qui ne diffèrent que par la variable dérivée et se couvrent toutes de la même façon. Les séparer sans les réunir ferait perdre que couvrir est toujours le même geste. [§8.2]

## Cesse d'être valide quand
Une sensibilité est locale : elle vaut au point où elle est calculée et se périme dès que le paramètre bouge. Le gamma mesure précisément cette péremption pour le delta. [ajout]

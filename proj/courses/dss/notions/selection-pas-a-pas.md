---
id: dss/selection-pas-a-pas
nom: Sélection pas à pas
type: abstraite
statut: source
cas_de: dss/selection-de-sous-ensemble
valeur: un seul chemin glouton, une variable à la fois
parametre: le sens dans lequel le chemin est parcouru
construite_a_partir_de:
- dss/meilleur-sous-ensemble
alias:
- stepwise selection
refs:
- slide 32
- slide 33
- slide 36
---

## Ce que c'est
Parcourir un seul chemin dans l'espace des sous-ensembles, en ajoutant ou en retirant une variable à la fois. [slide 33]

## Ce que les membres partagent
Les deux ne parcourent que $1+p(p+1)/2$ modèles, ce qui les rend utilisables là où le parcours exhaustif ne l'est plus. [slide 36]

Les deux sont gloutons : à chaque pas on prend le meilleur mouvement immédiat, et l'on ne revient jamais dessus. Ni l'un ni l'autre n'est garanti de donner le meilleur sous-ensemble. [slide 33, slide 36]

Le cours mentionne une version hybride qui combine les deux sens, sans la détailler. [slide 36]

## Pourquoi ce niveau existe
Le cours pose les deux sens côte à côte, sur la même slide, dans deux colonnes symétriques dont seul le sens du parcours change. Les séparer ferait manquer que c'est une seule idée lue dans les deux sens. [slide 33]


## Le chemin jusqu'ici
dss/apprentissage-supervise et dss/moindres-carres-ordinaires donnent l'ajustement, dss/erreur-de-test et dss/critere-penalise de quoi choisir, et dss/meilleur-sous-ensemble le parcours exhaustif. [ajout]

La dépendance au parcours exhaustif n'est pas technique mais logique : la sélection pas à pas existe parce que celui-ci devient infaisable au-delà d'une quarantaine de prédicteurs. [ajout]

## Exemple minimal
Avec les cinq prédicteurs des 20 clients, chaque sens ajuste 16 modèles, là où le parcours exhaustif en ajuste 32. [ajout]

## Cesse d'être valide quand
L'espace parcouru étant réduit, le modèle retenu peut être strictement moins bon que le meilleur sous-ensemble de même taille. C'est le prix explicitement payé pour la faisabilité. [slide 36]

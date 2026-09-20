---
id: dss/selection-de-sous-ensemble
nom: Sélection de sous-ensemble
type: abstraite
statut: source
cas_de: dss/selection-de-variables
valeur: retirer des prédicteurs, puis ajuster par moindres carrés sur ceux qui restent
parametre: la façon dont l'espace des sous-ensembles est parcouru
construite_a_partir_de:
- dss/moindres-carres-ordinaires
alias:
- subset selection
refs:
- slide 28
---

## Ce que c'est
Identifier un sous-ensemble de prédicteurs que l'on croit liés à la réponse, puis ajuster par moindres carrés sur ce seul sous-ensemble. [slide 28]

## Ce que les membres partagent
Tous produisent un modèle qui ne contient qu'une partie des prédicteurs, avec des coefficients de moindres carrés ordinaires sur cette partie : aucun coefficient n'est rétréci, il est présent ou absent. [slide 28]

Tous renvoient une suite de modèles indexée par le nombre de variables, et laissent à un critère extérieur — pénalisé ou par validation — le soin de choisir dans cette suite. [slide 29, slide 45]

## Pourquoi ce niveau existe
Le cours nomme les deux méthodes ensemble, sur la même ligne, et construit la seconde entièrement contre la première : la sélection pas à pas existe parce que le parcours exhaustif est infaisable. Les séparer ferait perdre ce rapport. [slide 28, slide 32]


## Le chemin jusqu'ici
dss/apprentissage-supervise, puis dss/moindres-carres-ordinaires. [ajout]

La famille garde l'ajustement intact et ne touche qu'à la liste des prédicteurs : les coefficients retenus sont des coefficients de moindres carrés, sans aucun rétrécissement. Le socle dit donc ce qui n'est pas modifié. [ajout]

## Cesse d'être valide quand
Le choix est discret : une variable est dedans ou dehors. Une variable faiblement mais réellement liée à la réponse est perdue, là où la régularisation l'aurait gardée avec un petit coefficient. [ajout]

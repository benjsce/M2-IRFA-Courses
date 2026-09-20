---
id: dss/type-de-donnee
nom: Type de donnée
type: notion
statut: source
construite_a_partir_de:
- dss/preparation-des-donnees
alias:
- data types
refs:
- slide 188
---

## Ce que c'est
La nature d'un attribut — nominale, ordinale, d'intervalle ou continue — qui décide de son codage. [slide 188]

## Ce qui la définit
La contrainte est posée d'abord : un réseau entraîné par rétropropagation n'accepte que des valeurs numériques continues, typiquement dans l'intervalle de 0 à 1. [slide 188]

Tout ce qui n'est pas déjà continu doit donc être transformé, et la transformation dépend du type. C'est le type qui décide, pas la commodité. [slide 188, slide 191]


## Le chemin jusqu'ici
dss/apprentissage-supervise, dss/reseau-de-neurones-artificiel, puis dss/preparation-des-donnees. [ajout]

Le type ne devient un sujet que parce que le réseau impose du numérique continu : c'est cette contrainte, posée en amont, qui rend la typologie nécessaire. [ajout]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| type | nominal discret symbolique | bleu, rouge, vert |
| type | ordinal discret, rangé | 1er, 2e, 3e |
| type | intervalle numérique mesurable | −5, 3, 24 |
| type | continu numérique | 0,23 ; −45,2 ; 500,43 |
[slide 188]

## Cesse d'être valide quand
La frontière entre intervalle et continu n'est pas opératoire pour le codage : le cours traite les deux ensemble dans la transformation. [slide 192]

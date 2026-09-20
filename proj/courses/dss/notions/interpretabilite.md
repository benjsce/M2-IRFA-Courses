---
id: dss/interpretabilite
nom: Interprétabilité
type: notion
statut: source
construite_a_partir_de: []
alias:
- model interpretability
- actionability
refs:
- slide 13
---

## Ce que c'est
La possibilité de lire, dans un modèle ajusté, l'effet des variables qui comptent. [slide 13]

## Ce qui la définit
L'argument du cours est de place, pas de vertu : quand les prédicteurs sont nombreux, beaucoup n'ont aucun effet sur la réponse, et les laisser dans le modèle rend l'effet des autres plus difficile à voir. [slide 13]

D'où la conclusion qui ouvre tout le chapitre suivant : le modèle serait plus facile à interpréter si l'on retirait les variables sans importance, c'est-à-dire si l'on mettait leurs coefficients à zéro. [slide 13]

## Cesse d'être valide quand
Le cours ne définit jamais l'interprétabilité autrement que par le nombre de variables. Un modèle à peu de variables mais à interactions fortes n'est pas couvert. [ajout]

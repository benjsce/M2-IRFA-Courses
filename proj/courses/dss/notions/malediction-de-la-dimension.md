---
id: dss/malediction-de-la-dimension
nom: Malédiction de la dimension
type: notion
statut: source
construite_a_partir_de:
- dss/haute-dimension
- dss/surapprentissage
alias:
- curse of dimensionality
refs:
- slide 92
- slide 93
---

## Ce que c'est
L'erreur de test croît avec le nombre de variables, sauf si les variables ajoutées sont réellement liées à la réponse. [slide 92]

## Ce qui la définit
L'énoncé est conditionnel, et la condition est tout. Une variable de signal, réellement liée à la réponse, améliore le modèle et fait baisser l'erreur de test. Une variable de bruit la fait monter. [slide 93]

Le bruit ajouté est donc coûteux sans contrepartie : il augmente la dimension du problème, donc le risque de surapprentissage, sans rien apporter à l'erreur de test. [slide 93]

Ce qui la distingue du surapprentissage : celui-ci est l'écart entre l'erreur d'apprentissage et l'erreur de test ; la malédiction dit que cet écart s'aggrave à chaque variable de bruit, jusqu'au régime où les moindres carrés ne répondent plus. [slide 92, ajout]

C'est ce qui rend le choix du paramètre de réglage crucial en haute dimension, et non simplement souhaitable. [slide 92]


## Le chemin jusqu'ici
dss/haute-dimension fournit le régime, où les prédicteurs sont aussi nombreux que les observations de dss/apprentissage-supervise et où dss/moindres-carres-ordinaires passent par tous les points. dss/surapprentissage fournit le mécanisme, un écart entre l'erreur d'apprentissage et celle que mesure dss/erreur-de-test. La malédiction relie les deux : l'écart grandit avec la dimension. [ajout]

## Exemple minimal
Sur les 20 clients, l'erreur mesurée sur 20 000 clients nouveaux vaut 1,16 avec l'endettement et le revenu, puis 1,37, 1,42 et 1,83 à chaque variable sans lien ajoutée : c'est la courbe de test de la figure de dss/surapprentissage, lue de gauche à droite. [ajout]

## Cesse d'être valide quand
Le résultat ne dit pas comment distinguer une variable de signal d'une variable de bruit avant de l'avoir essayée. C'est exactement le problème que la sélection de variables cherche à résoudre. [ajout]

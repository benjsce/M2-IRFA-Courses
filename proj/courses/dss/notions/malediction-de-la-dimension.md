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

Le bruit ajouté est donc doublement coûteux : il augmente la dimension du problème, donc le risque de surapprentissage, sans aucune contrepartie possible. [slide 93]

C'est ce qui rend le choix du paramètre de réglage crucial en haute dimension, et non simplement souhaitable. [slide 92]


## Le chemin jusqu'ici
Deux fils. dss/apprentissage-supervise et dss/moindres-carres-ordinaires mènent à dss/haute-dimension, le régime ; dss/erreur-de-test mène à dss/surapprentissage, le mécanisme. [ajout]

La malédiction est leur conjonction : en haute dimension, chaque variable de bruit ajoutée augmente le risque de surapprentissage sans contrepartie possible. [ajout]

## Exemple minimal
Ajouter cent variables sans lien avec la réponse à un modèle qui en compte trois dégrade l'erreur de test sans jamais pouvoir l'améliorer. [ajout]

## Cesse d'être valide quand
Le résultat ne dit pas comment distinguer une variable de signal d'une variable de bruit avant de l'avoir essayée. C'est exactement le problème que la sélection de variables cherche à résoudre. [ajout]

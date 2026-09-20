---
id: dss/importance-des-variables
nom: Importance des variables
type: principe
statut: source
construite_a_partir_de:
- dss/bagging
- dss/interpretabilite
alias:
- variable importance measures
refs:
- slide 104
---

## Ce que c'est
Attribuer à chaque prédicteur une part du travail accompli par un ensemble d'arbres. [slide 104]

## Ce qui la définit
Le problème est posé comme un échange : le bagging améliore la précision par rapport à un arbre unique, et il la paie en interprétabilité. Le modèle résultant est difficile à lire. [slide 104]

Une mesure d'importance est ce qui rend une partie de cette lecture. Elle ne reconstruit pas le modèle, elle en donne un classement des variables. [slide 104]

Le cours en donne deux, calculées à des endroits différents de la procédure, et qui ne mesurent pas la même chose. [slide 104, slide 106]


## Le chemin jusqu'ici
Deux fils. dss/bootstrap, dss/apprentissage-supervise, dss/erreur-de-test et dss/compromis-biais-variance donnent dss/bagging ; dss/interpretabilite donne la raison de mesurer. [ajout]

Le bagging gagne en précision ce qu'il perd en lisibilité. Une mesure d'importance rend une partie de ce qui a été perdu : c'est exactement l'échange que la fiche sur l'interprétabilité annonçait au début du cours. [ajout]

## Cesse d'être valide quand
Un classement n'est pas un effet : il dit qu'une variable compte, jamais dans quel sens elle pousse la prédiction. [ajout]

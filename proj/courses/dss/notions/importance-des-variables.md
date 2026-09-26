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
Une mesure d'importance ne reconstruit pas le modèle : elle en classe les variables, et rend ainsi une partie de la lecture qu'un ensemble d'arbres, bagging ou forêt, a fait perdre. [slide 104, slide 106]

Elle peut se lire pendant la construction des arbres, en additionnant ce que les coupures sur la variable ont fait gagner, ou après coup, sur les observations hors du sac, en mesurant ce que l'on perd quand on brouille la variable. Les classements obtenus ne coïncident pas. [slide 104, slide 106]

## Le chemin jusqu'ici
dss/interpretabilite pose la question dès le début du cours : un modèle qui prédit bien n'est pas pour autant un modèle qu'on sait expliquer. [ajout]

dss/bagging moyenne des arbres ajustés sur des tirages de dss/bootstrap. Il réduit ainsi la variance, comme le laissait espérer dss/compromis-biais-variance, et prédit mieux la perte des clients de dss/apprentissage-supervise qu'un arbre seul, au sens de dss/erreur-de-test. Mais il perd la lecture d'un arbre unique, et c'est cette lecture que la mesure d'importance rend en partie. [slide 104, ajout]

## Cesse d'être valide quand
Un classement n'est pas un effet : il dit qu'une variable compte, jamais dans quel sens elle pousse la prédiction. [ajout]

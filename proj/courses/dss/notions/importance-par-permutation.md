---
id: dss/importance-par-permutation
nom: Importance par permutation
type: notion
statut: source
cas_de: dss/importance-des-variables
valeur: la perte d'exactitude quand on permute la colonne
construite_a_partir_de:
- dss/erreur-out-of-bag
alias:
- permutation importance
refs:
- slide 106
---

## Ce que c'est
La baisse d'exactitude sur les observations hors du sac quand on permute au hasard la colonne d'un prédicteur. [slide 106]

## Ce qui la définit
La procédure se fait arbre par arbre : on note l'exactitude sur les observations out-of-bag, on permute la colonne $j$ de ces observations, on note à nouveau, et l'on moyenne la baisse sur tous les arbres. [slide 106]

Permuter détruit le lien entre le prédicteur et la réponse sans changer sa distribution marginale : ce qui reste mesure ce que le modèle perd en perdant cette variable. [ajout]

La mesure est calculée hors du sac, donc sur des observations que l'arbre n'a pas vues. C'est ce qui la sépare de la mesure par impureté. [slide 106]


## Le chemin jusqu'ici
Le chemin passe par dss/bootstrap, dss/apprentissage-supervise, dss/erreur-de-test et dss/compromis-biais-variance, qui donnent dss/bagging, puis par dss/validation-croisee et dss/erreur-out-of-bag. [ajout]

La mesure se calcule hors du sac, jamais sur les données d'apprentissage : c'est ce qui la sépare de la mesure par impureté, et c'est pourquoi elle dépend de l'erreur out-of-bag plutôt que du bagging seul. [ajout]

## Exemple minimal
Une variable dont la permutation ne change pas l'exactitude hors du sac reçoit une importance nulle, même si elle a servi à de nombreuses coupures. [ajout]

## Geste de calcul type
La calculer sur les observations out-of-bag, jamais sur les données d'apprentissage : sur ces dernières, la permutation d'une variable surajustée ne coûterait presque rien. [slide 106]

## Cesse d'être valide quand
Sous forte corrélation entre prédicteurs, permuter l'un laisse le modèle s'appuyer sur l'autre, et l'importance des deux est sous-estimée. Le cours n'aborde pas ce cas. [ajout]

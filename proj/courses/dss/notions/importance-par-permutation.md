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
La hausse de l'erreur sur les observations hors du sac, ou la baisse d'exactitude en classification, quand on mélange au hasard la colonne d'un prédicteur. [slide 106]

## Ce qui la définit
La procédure se fait arbre par arbre : on note l'erreur de l'arbre sur ses observations hors du sac, on mélange au hasard la colonne $j$ de ces observations, on note à nouveau, et l'on moyenne la dégradation sur tous les arbres. [slide 106]

Mélanger la colonne détruit le lien entre le prédicteur et la réponse sans changer les valeurs qu'il prend : ce qui se dégrade mesure ce que le modèle perd en perdant cette variable, sans qu'on le réajuste. [ajout]

Tout se calcule hors du sac, sur des observations que l'arbre n'a pas vues : une coupure qui n'a appris que du bruit ne s'y retrouve pas. C'est ce qui sépare cette mesure de la mesure par impureté. [slide 106, ajout]

## Le chemin jusqu'ici
dss/erreur-out-of-bag fournit le terrain de la mesure : chaque arbre de dss/bagging est ajusté sur un tirage de dss/bootstrap, et les clients restés hors du tirage le jugent comme le ferait un jeu de test. [ajout]

Cette erreur estime dss/erreur-de-test sans mettre de clients de côté, comme dss/validation-croisee, sur les clients de dss/apprentissage-supervise dont on connaît la perte. dss/compromis-biais-variance explique pourquoi l'on moyenne tant d'arbres, et pourquoi on ne sait plus les lire : c'est cette lecture que la mesure rend en partie. [ajout]

## Exemple minimal
Sur les 20 clients, une forêt de 500 arbres : l'erreur quadratique moyenne d'un arbre hors du sac vaut environ 4,0. Brouiller l'endettement la fait monter de 0,31, et x3, la variable sans lien liée à la perte par hasard, autant ; x4, de 0,09 ; x5 et le revenu, de rien. x5, qui recevait 18 % de la baisse d'impureté, ne coûte rien ici. [ajout]

![La forêt des 20 clients. Chaque barre donne la hausse de l'erreur hors du sac quand on brouille la colonne, moyennée sur les 500 arbres ; à droite, en gris, la part de la même variable dans la baisse d'impureté. Les variables sans lien x4 et x5, qui prenaient chacune 18 % de l'impureté, ne coûtent presque rien quand on les brouille.](figures/importance-par-permutation.svg) [ajout]

## Geste de calcul type
La calculer sur les observations hors du sac, jamais sur les données d'apprentissage. Sur ces dernières, l'arbre a tout appris, bruit compris, et brouiller une variable sans lien coûte autant qu'une variable utile : dans le sac, sur la même forêt, x5 coûte environ 0,9, plus que le revenu, environ 0,8. [slide 106, ajout]

## Cesse d'être valide quand
Sur si peu de clients, elle ne distingue pas une coïncidence d'un lien : x3 y coûte autant que l'endettement. [ajout]

Sous forte corrélation entre prédicteurs, brouiller l'un laisse le modèle s'appuyer sur l'autre, et l'importance des deux est sous-estimée. Le cours n'aborde pas ce cas. [ajout]

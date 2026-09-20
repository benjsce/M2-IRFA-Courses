---
id: dss/importance-par-impurete
nom: Importance par impureté
type: notion
statut: source
cas_de: dss/importance-des-variables
valeur: la baisse de RSS ou d'indice de Gini aux coupures
construite_a_partir_de:
- dss/bagging
alias:
- Gini importance
refs:
- slide 104
- slide 105
---

## Ce que c'est
Le total de la baisse de RSS ou d'indice de Gini due aux coupures sur un prédicteur, moyenné sur tous les arbres. [slide 104]

## Ce qui la définit
La mesure se lit à l'intérieur des arbres, pendant leur construction : elle additionne ce que chaque coupure a fait gagner. Elle ne coûte donc rien de plus que l'ajustement. [slide 104]

En régression c'est la RSS qui sert de mesure d'impureté, en classification l'indice de Gini. [slide 104, slide 105]


## Le chemin jusqu'ici
Le socle est celui du bagging : dss/bootstrap d'un côté, dss/apprentissage-supervise, dss/erreur-de-test et dss/compromis-biais-variance de l'autre, réunis dans dss/bagging. [ajout]

La mesure se calcule pendant la construction des arbres, ce qui explique qu'elle ne demande rien de plus : elle additionne ce que chaque coupure a déjà fait gagner. [ajout]

## Exemple minimal
Sur les données de cardiologie du cours, le classement par baisse d'indice de Gini place quelques variables très au-dessus des autres. [slide 105]

## Geste de calcul type
La lire comme un classement relatif, normalisé sur la variable la plus importante, et non comme une quantité interprétable en soi. [slide 105]

## Cesse d'être valide quand
Elle est calculée sur les données qui ont servi à construire les arbres, ce qui la rend sensible au nombre de modalités d'une variable. Le cours ne le signale pas ; la mesure par permutation évite cet écueil. [ajout]

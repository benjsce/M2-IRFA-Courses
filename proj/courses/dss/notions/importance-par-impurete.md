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
Le total de la baisse d'impureté obtenue par les coupures sur un prédicteur, moyenné sur tous les arbres. [slide 104]

## Ce qui la définit
La mesure se lit à l'intérieur des arbres, pendant leur construction : chaque coupure rend plus homogènes les deux groupes qu'elle crée, et l'on crédite cette baisse au prédicteur sur lequel elle porte. Elle ne coûte donc rien de plus que l'ajustement. [slide 104, ajout]

L'impureté d'un groupe mesure son mélange. En régression, c'est la RSS, la somme des carrés des écarts des réponses à leur moyenne ; en classification, l'indice de Gini du nœud, qui mesure le mélange des classes. Ce n'est pas le GINI lu sur une courbe ROC, qui porte le même nom. [slide 104, slide 105, ajout]

## Le chemin jusqu'ici
La mesure additionne ce que font les coupures des arbres de dss/bagging, ajustés chacun sur un tirage de dss/bootstrap des clients de dss/apprentissage-supervise. Ces arbres sont poussés loin : la moyenne corrige leur variance, que dss/compromis-biais-variance oppose au biais, et dss/erreur-de-test les juge sur des clients nouveaux. La mesure, elle, ne regarde que les clients d'apprentissage. [ajout]

## Exemple minimal
Sur les 20 clients, une forêt de 500 arbres, 2 prédicteurs candidats sur 5, donne 21 % de la baisse totale à l'endettement et 16 % au revenu. La variable sans lien x3, liée à la perte par hasard, en reçoit 27 %, et les trois variables sans lien, ensemble, 63 %. [ajout]

![Les 20 clients, 500 arbres. Chaque barre donne la part d'un prédicteur dans la baisse d'impureté totale. La variable sans lien x3 passe devant l'endettement, et les trois variables sans lien prennent ensemble plus de la moitié du total : des arbres poussés au bout coupent aussi sur le bruit, et chaque coupure compte.](figures/importance-par-impurete.svg) [ajout]

## Geste de calcul type
La lire comme un classement relatif, normalisé sur la variable la plus importante, et non comme une quantité interprétable en soi. [slide 105]

Les parts de l'exemple sont rapportées au total ; normalisée comme sur la slide, la même forêt met x3 à 100 et l'endettement à 76. [ajout]

## Cesse d'être valide quand
Elle est calculée sur les clients qui ont servi à construire les arbres : chaque coupure y compte, même celle qui n'apprend que du bruit. Elle est aussi sensible au nombre de valeurs distinctes d'une variable, qui multiplie les seuils possibles. Le cours ne le signale pas ; la mesure par permutation, calculée hors du sac, évite une partie de ces écueils. [ajout]

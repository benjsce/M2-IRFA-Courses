---
id: dss/foret-aleatoire
nom: Forêt aléatoire
symbole: $m$
type: notion
statut: source
cas_de: dss/methode-d-ensemble
valeur: des arbres décorrélés par un tirage de prédicteurs à chaque coupure
construite_a_partir_de:
- dss/variance-d-une-moyenne-correlee
alias:
- random forest
- RF
refs:
- slide 110
- slide 111
- slide 112
- slide 113
- slide 115
- slide 116
- slide 119
- slide 121
---

## Ce que c'est
Du bagging où, à chaque coupure, seuls $m$ prédicteurs tirés au hasard sont candidats. [slide 113]

## Ce qui la définit
La cause de la corrélation est identifiée avant le remède : s'il existe un prédicteur très fort, tous les arbres le placent en haut et se ressemblent. [slide 110]

Restreindre le nombre de prédicteurs candidats ne suffit pas ; il faut que la restriction soit tirée au hasard à chaque coupure, sinon les arbres restent corrélés. [slide 111, slide 112]

À $m=p$, on retrouve exactement le bagging : la forêt aléatoire le contient comme cas limite. [slide 113]

Le nombre d'arbres n'augmente pas la souplesse du modèle : une forêt ne surajuste pas quand $B$ croît. [slide 121]


## Le chemin jusqu'ici
Le chemin passe par dss/bootstrap, dss/apprentissage-supervise, dss/erreur-de-test et dss/compromis-biais-variance, qui donnent dss/bagging, puis par dss/variance-d-une-moyenne-correlee. [ajout]

La dernière étape est la clé : elle montre que la variance de la moyenne bute sur un plancher fixé par la corrélation entre arbres. La forêt aléatoire est la réponse à ce plancher, et rien d'autre. [ajout]

## Exemple minimal
Avec $p=100$ prédicteurs dont 3 pertinents, la probabilité qu'un prédicteur pertinent soit candidat à une coupure donnée est d'environ 0,25. [slide 119]

## Geste de calcul type
Partir des valeurs recommandées par les inventeurs — $m=\sqrt{p}$ et taille de nœud minimale 1 en classification, $m=p/3$ et taille 5 en régression — puis les traiter comme des paramètres à régler, en suivant l'erreur out-of-bag. [slide 116]

## Cesse d'être valide quand
Quand les variables sont nombreuses et la fraction de variables pertinentes faible, un $m$ petit fait mal travailler la forêt : la chance qu'une variable utile soit candidate devient trop faible. [slide 119]

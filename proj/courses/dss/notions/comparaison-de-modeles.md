---
id: dss/comparaison-de-modeles
nom: Comparaison de modèles de risque de crédit
type: notion
statut: source
construite_a_partir_de:
- dss/scoring-de-credit
- dss/courbe-roc
- dss/lasso
- dss/foret-aleatoire
- dss/boosting
- dss/retropropagation
alias:
- credit risk analysis using machine and deep learning models
refs:
- slide 17
- slide 204
- slide 205
- slide 206
- slide 213
- slide 214
---

## Ce que c'est
L'étude du cours qui classe par leur GINI, sur un même jeu de risque de crédit, la régression logistique et plusieurs modèles d'apprentissage automatique. [slide 17, slide 204]

## Ce qui la définit
Le jeu est fixé : 12 544 entreprises du périmètre européen, 343 variables, un facteur binaire de défaut. Les modèles sont la régression logistique, le lasso, la forêt aléatoire, plusieurs gradient boostings, un séparateur à vaste marge, un réseau de neurones et de l'apprentissage profond. [slide 205, slide 206]

Le résultat n'est pas celui qu'on attend. La forêt aléatoire domine, avec un GINI de 57,84 contre 51,36 pour la régression logistique. Mais le boosting tombe à 44,16, l'apprentissage profond à 44,92 et le séparateur à vaste marge à 28,38, tous en dessous de la régression logistique. [slide 17]

La comparaison finale se lit sur deux graphiques : les courbes ROC superposées, et des boîtes à moustaches, une par modèle, qui montrent comment son score se disperse. [slide 213]

## Le chemin jusqu'ici
Le socle est long parce que l'étude met en concurrence ce que les chapitres précédents ont construit ; elle ne construit rien de neuf, elle mesure. [ajout]

**Le problème et sa mesure.** Le problème posé est celui du dss/scoring-de-credit, prévoir le défaut d'un emprunteur ; il relève de dss/apprentissage-supervise, puisque les défauts passés sont connus. Les modèles sont jugés sur la dss/courbe-roc, qui trace, seuil après seuil, les taux lus dans une dss/matrice-de-confusion, et dont l'aire se convertit en GINI. [ajout]

**Les modèles linéaires contraints.** Le dss/lasso concourt ; il prolonge la dss/regression-ridge, qui rétrécit les coefficients des dss/moindres-carres-ordinaires au nom du dss/compromis-biais-variance : un peu de biais contre moins de variance, un arbitrage que tranche dss/erreur-de-test. [ajout]

**Les arbres.** La dss/foret-aleatoire reprend le dss/bagging, qui moyenne des arbres construits sur des échantillons de dss/bootstrap, et force ses arbres à se ressembler moins : la dss/variance-d-une-moyenne-correlee montre qu'une moyenne d'arbres trop semblables ne perd pas sa variance. Le dss/boosting, lui, ajuste ses arbres en séquence, chacun sur ce que les précédents n'expliquent pas encore, et c'est le dss/surapprentissage qui le guette. [ajout]

**Les réseaux.** Le réseau de neurones est entraîné par dss/retropropagation, qui corrige chaque poids par un pas de dss/descente-de-gradient, héritier de la dss/regle-delta. Il s'agit d'un dss/reseau-multicouche : sa couche cachée répond à la dss/limite-du-perceptron, sa dss/fonction-d-activation lisse le rend entraînable, et chacun de ses nœuds reprend le dss/perceptron, l'unité d'un dss/reseau-de-neurones-artificiel qui calcule une dss/fonction-discriminante-lineaire à partir d'exemples, au sens de dss/apprentissage-inductif. [ajout]

## Exemple minimal
Passer de la régression logistique à la forêt aléatoire fait gagner 6,48 points de GINI, soit 12,6 % de plus ; passer au séparateur à vaste marge en fait perdre 22,98. [slide 17]

## Geste de calcul type
Relier les deux mesures d'un même écart : en points, $57{,}84-51{,}36=6{,}48$ ; en relatif, $6{,}48/51{,}36\approx12{,}6\,\%$. Puis regarder les boîtes à moustaches : deux modèles de score médian voisin peuvent se disperser très différemment. [slide 17, slide 213]

## Cesse d'être valide quand
Le cours en tire lui-même la limite : les modèles avancés n'ont de sens que si de nouveaux flux de données sont captés. [slide 214]

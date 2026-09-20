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
- slide 204
- slide 205
- slide 206
- slide 213
- slide 214
---

## Ce que c'est
L'étude qui met en concurrence, sur un même jeu de risque de crédit, tous les modèles enseignés dans le cours. [slide 204]

## Ce qui la définit
Le jeu est fixé : 12 544 entreprises du périmètre européen, 343 variables, un facteur binaire de défaut. Les modèles sont la régression logistique, le lasso, la forêt aléatoire, plusieurs gradient boostings, un séparateur à vaste marge, un réseau de neurones et de l'apprentissage profond. [slide 205, slide 206]

Le résultat n'est pas celui qu'on attend : la forêt aléatoire domine, avec un GINI de 57,84 contre 51,36 pour la régression logistique, soit +12,6 %. Mais le boosting tombe à 44,16, le séparateur à vaste marge à 28,38, et l'apprentissage profond à 44,92 — tous en dessous de la régression logistique. [slide 17]

La comparaison finale se lit sur deux graphiques : les courbes ROC superposées, et des boîtes à moustaches qui montrent la dispersion du GINI d'un modèle à l'autre. C'est la dispersion, autant que la médiane, qui départage. [slide 213]


## Le chemin jusqu'ici
Le socle est le plus long du cours, et pour une raison simple : l'étude met en concurrence tout ce qui précède. [ajout]

**Le problème et sa mesure.** dss/apprentissage-supervise donne dss/scoring-de-credit ; dss/matrice-de-confusion donne dss/courbe-roc, l'unité dans laquelle les modèles sont comparés. [ajout]

**Les modèles linéaires.** dss/moindres-carres-ordinaires d'un côté, dss/erreur-de-test puis dss/compromis-biais-variance de l'autre, donnent dss/regression-ridge, puis dss/lasso. [ajout]

**Les arbres.** dss/bootstrap, avec le même compromis, donne dss/bagging ; dss/variance-d-une-moyenne-correlee mène à dss/foret-aleatoire, et dss/surapprentissage à dss/boosting. [ajout]

**Les réseaux.** dss/apprentissage-inductif donne dss/fonction-discriminante-lineaire, qui avec dss/reseau-de-neurones-artificiel donne dss/perceptron, puis dss/limite-du-perceptron et dss/fonction-d-activation, d'où dss/reseau-multicouche ; dss/regle-delta et dss/descente-de-gradient donnent dss/retropropagation. [ajout]

L'étude ne construit rien de neuf : elle mesure. C'est pourquoi son socle est la somme des chapitres — et c'est aussi ce qui rend son résultat lisible, puisque plusieurs méthodes réputées avancées passent sous la régression logistique. [ajout]

## Exemple minimal
Passer de la régression logistique à la forêt aléatoire fait gagner 6,48 points de GINI ; passer au séparateur à vaste marge en fait perdre 22,98. [slide 17]

## Geste de calcul type
Ne pas classer sur la médiane seule : deux modèles de GINI médian voisin peuvent avoir des dispersions très différentes, et c'est ce que les boîtes à moustaches donnent à voir. [slide 213]

## Cesse d'être valide quand
Les conclusions du cours portent au-delà des chiffres : seuls des cadres dynamiques sont viables, les modèles avancés n'ont de sens que si de nouveaux flux de données sont captés, la gouvernance du risque de modèle est aujourd'hui inadaptée, et la supervision de ces modèles par une banque centrale sera difficile. [slide 214]

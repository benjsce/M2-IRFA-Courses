---
id: dss/biais-societal
nom: Biais sociétal
type: notion
statut: source
construite_a_partir_de:
- dss/comparaison-de-modeles
- dss/importance-des-variables
- dss/smote
alias:
- societal bias
refs:
- slide 218
- slide 220
- slide 221
- slide 222
- slide 223
- slide 224
- slide 225
- slide 227
- slide 231
- slide 232
- slide 233
- slide 235
---

## Ce que c'est
Un biais social devenu la norme. [slide 218]

## Ce qui la définit
La définition du cours est courte : un biais social devient sociétal quand il devient la norme. Les écarts de rémunération par origine ethnique documentés par l'office statistique britannique en servent d'ancrage. [slide 218]

Ce que le cours montre ensuite, c'est que l'apprentissage automatique reproduit un tel biais. L'expérience est simple : on ne donne pas au modèle le genre ou le groupe ethnique du client, et l'on cherche s'il le retrouve quand même dans ses autres variables. Elle se fait en trois questions, dans cet ordre : le jeu de données est-il réellement utilisable pour du scoring ; permet-il de prédire le genre ou le groupe ethnique du client ; et alors, qu'est-ce que cela implique. [slide 227]

La réponse du cours est double et tranchée. Oui, l'apprentissage fait prospérer les biais sociaux, en répliquant les motifs qu'il apprend. Et le modèle économique de la banque, ajouté aux règles prudentielles, semble empêcher de traiter le problème. [slide 235]

## Le chemin jusqu'ici
Pour que la question ait un sens, il fallait des modèles de crédit qui marchent : dss/comparaison-de-modeles les a classés sur un même jeu, et l'étude sur les biais reprend les mêmes outils. [ajout]

**Les modèles.** Le problème est le dss/scoring-de-credit, prévoir le défaut, un cas de dss/apprentissage-supervise ; les modèles se comparent sur la dss/courbe-roc, construite à partir de la dss/matrice-de-confusion. Concourent le dss/lasso, qui prolonge la dss/regression-ridge en rétrécissant les dss/moindres-carres-ordinaires au nom du dss/compromis-biais-variance, un arbitrage que tranche dss/erreur-de-test ; la dss/foret-aleatoire, qui reprend le dss/bagging d'arbres tirés par dss/bootstrap en les rendant moins semblables, puisque la dss/variance-d-une-moyenne-correlee ne baisse pas entre arbres trop proches ; et le dss/boosting, que guette le dss/surapprentissage. [ajout]

**Le réseau.** Il est entraîné par dss/retropropagation, par pas de dss/descente-de-gradient hérités de la dss/regle-delta. C'est un dss/reseau-multicouche, dont la couche cachée répond à la dss/limite-du-perceptron et que sa dss/fonction-d-activation rend entraînable ; ses nœuds reprennent le dss/perceptron, l'unité d'un dss/reseau-de-neurones-artificiel qui calcule une dss/fonction-discriminante-lineaire en apprenant d'exemples, au sens de dss/apprentissage-inductif. [ajout]

**Les deux outils de l'expérience.** dss/importance-des-variables, issue de dss/interpretabilite, dit quelles variables portent l'information du genre ; dss/smote, une étape de dss/preparation-des-donnees, rend comparables des groupes de tailles très inégales. [ajout]

## Exemple minimal
Sur le jeu « genre », une forêt aléatoire qui cherche le genre du client à partir de ses autres variables obtient un score F1 de 0,33 sur les données telles quelles, et de 0,86 une fois les groupes rééquilibrés par SMOTE, sur une échelle où 1 est une prédiction parfaite. [slide 233, ajout]

## Cesse d'être valide quand
L'étude montre que le biais est reproduit ; elle ne montre pas comment l'enlever. Le cours conclut sur une piste de recherche, le travail par sous-échantillons intermédiaires homogènes, et non sur un correctif. [slide 235]

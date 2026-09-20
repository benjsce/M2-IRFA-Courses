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
Un biais social que l'apprentissage reproduit parce qu'il en apprend le motif dans les données. [slide 218]

## Ce qui la définit
La définition du cours est précise et courte : un biais social devient sociétal quand il devient la norme. Les écarts de rémunération par origine ethnique documentés par l'office statistique britannique en servent d'ancrage. [slide 218]

L'expérimentation se fait en trois questions, posées dans cet ordre : le jeu de données est-il réellement utilisable pour du scoring ; permet-il de prédire le genre ou le groupe ethnique du client ; et alors, qu'est-ce que cela implique. [slide 227]

La réponse du cours est double et tranchée. Oui, l'apprentissage fait prospérer les biais sociaux, en répliquant les motifs qu'il apprend. Et le modèle économique de la banque, ajouté aux règles prudentielles, semble empêcher de traiter le problème. [slide 235]

La piste ouverte est le travail par sous-échantillons intermédiaires homogènes. Le cours la présente comme une recherche à mener, pas comme une solution. [slide 235]


## Le chemin jusqu'ici
Le socle est le plus long du cours parce que l'étude se place après tout le reste. [ajout]

**Ce qui est mesuré.** dss/apprentissage-supervise donne dss/scoring-de-credit, et dss/matrice-de-confusion donne dss/courbe-roc ; dss/moindres-carres-ordinaires, dss/erreur-de-test et dss/compromis-biais-variance donnent dss/regression-ridge puis dss/lasso ; dss/bootstrap donne dss/bagging, d'où dss/variance-d-une-moyenne-correlee et dss/foret-aleatoire, tandis que dss/surapprentissage donne dss/boosting ; dss/apprentissage-inductif donne dss/fonction-discriminante-lineaire, qui avec dss/reseau-de-neurones-artificiel donne dss/perceptron, puis dss/limite-du-perceptron, dss/fonction-d-activation et dss/reseau-multicouche, que dss/regle-delta et dss/descente-de-gradient conduisent à dss/retropropagation. Le tout se referme dans dss/comparaison-de-modeles. [ajout]

**Ce qui sert à l'expérience.** dss/interpretabilite donne dss/importance-des-variables, qui dit quelles variables portent l'information ; dss/preparation-des-donnees donne dss/smote, qui rend comparables des sous-échantillons de tailles très inégales. [ajout]

L'étude ne conclut pas sur une méthode mais sur un constat : l'apprentissage reproduit les motifs qu'il apprend, biais compris. Il fallait donc disposer des modèles, de la mesure qui les classe, et des deux outils d'expérimentation. [ajout]

## Exemple minimal
Si un modèle entraîné sans variable de genre prédit malgré tout le genre du client, c'est que d'autres variables en portent l'information. [slide 233]

## Cesse d'être valide quand
L'étude montre que le biais est reproduit ; elle ne montre pas comment l'enlever. Le cours conclut sur une piste de recherche et non sur un correctif. [slide 235]

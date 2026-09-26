---
id: dss/composante-principale
nom: Composante principale
type: notion
statut: source
construite_a_partir_de:
- dss/decomposition-en-valeurs-singulieres
alias:
- principal component
- PCA
refs:
- slide 61
- slide 74
---

## Ce que c'est
La combinaison linéaire normalisée des prédicteurs de plus grande variance, puis la suivante sous contrainte d'être non corrélée aux précédentes. [slide 74]

## Forme
$$\mathbf{z}_1=\mathbf{X}v_1,\qquad v_1=\arg\max_{\lVert v\rVert=1}\mathrm{Var}(\mathbf{X}v)$$ [slide 61, slide 74]

## Ce que les symboles modélisent
$v_1$ est une direction de l'espace des prédicteurs, un vecteur de poids de norme un : il dit dans quelle proportion chaque prédicteur entre dans la combinaison. $\mathbf{z}_1$ est ce que cette direction produit sur les données, un score par observation, obtenu en projetant chaque ligne de $\mathbf{X}$ sur $v_1$. La direction appartient aux variables, le score aux observations. [slide 61]

$v$ est la variable sur laquelle on maximise ; la contrainte de norme un empêche de faire croître la variance en allongeant simplement le vecteur. $\mathrm{Var}$ est la variance empirique, calculée sur les observations de l'échantillon, et $\mathbf{X}$ la matrice des prédicteurs, une observation par ligne, centrée. [slide 61, ajout]

## Ce qui la définit
Les directions $v_j$ sont exactement les colonnes de $\mathbf{V}$ de la décomposition en valeurs singulières, c'est-à-dire les vecteurs propres de $\mathbf{X}^T\mathbf{X}$. Le lien n'est pas une analogie : c'est la même décomposition, lue autrement. [slide 61]

La première direction minimise aussi la somme des distances perpendiculaires aux points, ce qui en donne une lecture géométrique. [slide 80]

Quand beaucoup de variables sont corrélées, un petit nombre de composantes capte l'essentiel de leur variation commune. [slide 74]

![Un nuage de deux variables corrélées, construit pour le dessin. La première composante suit la direction où les points s'étalent le plus, et les petits segments sont leurs distances perpendiculaires à elle ; la seconde, orthogonale, porte ce qui reste de variation.](figures/composante-principale.svg) [ajout]

## Le chemin jusqu'ici
dss/apprentissage-supervise, dss/moindres-carres-ordinaires, puis dss/decomposition-en-valeurs-singulieres. [ajout]

La dernière est décisive : les directions principales sont exactement les colonnes de $\mathbf{V}$, et ce n'est pas une analogie mais une identité. [ajout]

## Exemple minimal
Sur les données de publicité, la première composante se lit fortement sur la population comme sur la dépense publicitaire ; la seconde ne se lit ni sur l'une ni sur l'autre. [slide 81, slide 82]

## Geste de calcul type
Standardiser, décomposer $\mathbf{X}^T\mathbf{X}$, ordonner les valeurs propres, et ne garder que les directions dont la valeur propre est grande. [slide 61, slide 77]

## Cesse d'être valide quand
Les directions sont choisies sur la seule variation des prédicteurs : rien ne garantit qu'elles soient liées à la réponse. [slide 86]

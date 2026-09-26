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

$\mathbf{X}$ est la matrice centrée des prédicteurs, une observation par ligne, et $\mathrm{Var}$ la variance empirique des scores. La contrainte de norme un empêche de faire croître la variance en allongeant simplement $v$. [slide 61, ajout]

## Ce qui la définit
Le nuage des prédicteurs est connu ; on cherche la direction le long de laquelle il s'étale le plus. Cette direction est la première colonne de $\mathbf{V}$ dans la décomposition en valeurs singulières, et les suivantes sont les autres colonnes, c'est-à-dire les vecteurs propres de $\mathbf{X}^T\mathbf{X}$. Le lien n'est pas une analogie : c'est la même décomposition, lue autrement. [slide 61]

La première direction minimise aussi la somme des carrés des distances perpendiculaires des points à elle, ce qui en donne une lecture géométrique. [slide 80]

![Un nuage de deux variables corrélées, construit pour le dessin à l'image des données de publicité du cours. La première composante suit la direction où les points s'étalent le plus, et les petits segments sont leurs distances perpendiculaires à elle, dont elle minimise la somme des carrés ; la seconde, orthogonale, porte ce qui reste de variation.](figures/composante-principale.svg) [ajout]

Quand beaucoup de variables sont corrélées, un petit nombre de composantes capte l'essentiel de leur variation commune. [slide 74]

## Le chemin jusqu'ici
dss/decomposition-en-valeurs-singulieres fournit déjà les directions et leurs étirements : les composantes principales ne font que les ranger par variance décroissante. Cette décomposition porte sur la matrice des prédicteurs de dss/moindres-carres-ordinaires, une ligne par observation de dss/apprentissage-supervise. [ajout]

## Exemple minimal
Sur les données de publicité du cours, la première composante est fortement liée à la population comme à la dépense publicitaire ; la seconde, faiblement à l'une et à l'autre. [slide 81, slide 82]

Sur les 20 clients, prédicteurs standardisés, la première composante porte environ 45 % de la dispersion des cinq prédicteurs, et elle les mêle tous les cinq, l'endettement comme les trois variables sans lien. [ajout]

## Geste de calcul type
Standardiser, décomposer $\mathbf{X}^T\mathbf{X}$, ordonner les valeurs propres, et garder les $M$ premières directions, $M$ choisi par validation croisée. [slide 61, slide 77, slide 85]

## Cesse d'être valide quand
Les directions sont choisies sur la seule variation des prédicteurs : rien ne garantit qu'elles soient liées à la réponse. [slide 86]

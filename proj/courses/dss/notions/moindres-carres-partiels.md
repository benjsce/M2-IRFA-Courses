---
id: dss/moindres-carres-partiels
nom: Moindres carrés partiels
type: notion
statut: source
cas_de: dss/reduction-de-dimension
valeur: 'oui : chaque direction est pondérée par sa liaison à la réponse'
construite_a_partir_de:
- dss/regression-composantes-principales
alias:
- PLS
- partial least squares
refs:
- slide 86
- slide 87
- slide 88
- slide 89
- slide 90
---

## Ce que c'est
La réduction de dimension où la réponse sert à choisir les directions. [slide 87]

## Forme
$$\hat\varphi_{mj}=\langle \mathbf{x}_j^{(m-1)},\mathbf{y}\rangle,\qquad \mathbf{z}_m=\sum_{j=1}^{p}\hat\varphi_{mj}\mathbf{x}_j^{(m-1)}$$ [slide 90]

## Ce que les symboles modélisent
$\hat\varphi_{mj}$ est le poids du prédicteur $j$ dans la direction $m$ : le même objet que le poids $\phi_{mj}$ de la réduction de dimension, que la slide 89 écrit $\phi_{1j}$ et l'algorithme de la slide 90 $\hat\varphi_{mj}$. Il est calculé à partir de la réponse $\mathbf{y}$, et c'est ce qui le sépare du poids d'une composante principale, qui ne regarde que les prédicteurs. Le produit scalaire $\langle\cdot,\cdot\rangle$ porte sur deux colonnes de données, prédicteurs standardisés : il mesure à quel point le prédicteur et la réponse varient ensemble sur les observations. [slide 89, slide 90, ajout]

$\mathbf{x}_j^{(m-1)}$ n'est pas le prédicteur $j$ d'origine, sauf à la première direction : c'est ce qui en reste une fois retiré ce que les directions déjà construites en expliquent. $\mathbf{z}_m$ est la direction obtenue, une colonne de valeurs, une par observation, et $p$ le nombre de prédicteurs. [slide 90]

## Ce qui la définit
Le poids d'un prédicteur mesure son lien avec la réponse : la méthode place le poids le plus fort sur les variables les plus liées, dans l'échantillon, à ce qu'on veut prédire. [slide 89]

Les directions suivantes s'obtiennent en orthogonalisant les prédicteurs par rapport à celles déjà construites, puis en recommençant sur les résidus. [slide 89, slide 90]

La réduction supervisée peut baisser le biais, mais elle a aussi le pouvoir d'augmenter la variance — le cours le dit, sans trancher. [slide 89]


## Le chemin jusqu'ici
Les moindres carrés partiels se définissent en changeant une seule chose à dss/regression-composantes-principales : l'usage de la réponse pour choisir les directions. [ajout]

Tout le reste en vient. Les directions restent des combinaisons des prédicteurs, comme les directions de dss/composante-principale que calcule dss/decomposition-en-valeurs-singulieres, et l'on finit par dss/moindres-carres-ordinaires sur ces directions. Ce qui change est que la réponse, observée avec les prédicteurs dans dss/apprentissage-supervise, sert dès la construction. [ajout]

## Exemple minimal
Sur les 20 clients, prédicteurs standardisés, les poids de la première direction valent 13,6 pour l'endettement, −6,9 pour le revenu, 14,8 pour x3, 1,0 pour x4 et −11,3 pour x5. x4, sans lien avec la perte, ne reçoit presque rien ; mais x3, sans lien lui aussi, reçoit le poids le plus fort, parce que le hasard l'a liée à la perte sur ces 20 clients. [ajout]

## Geste de calcul type
Standardiser, calculer les produits scalaires avec $\mathbf{y}$ pour la première direction, orthogonaliser, recommencer ; $M$ se choisit par validation croisée comme pour les composantes principales. [slide 89, slide 90]

## Cesse d'être valide quand
L'avantage sur la version non supervisée n'est pas garanti : le cours signale le risque d'augmentation de variance, sans donner de critère pour choisir entre les deux. [slide 89]

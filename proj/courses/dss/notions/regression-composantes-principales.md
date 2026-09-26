---
id: dss/regression-composantes-principales
nom: Régression sur composantes principales
type: notion
statut: source
cas_de: dss/reduction-de-dimension
valeur: 'non : les directions ne dépendent que des prédicteurs'
construite_a_partir_de:
- dss/composante-principale
alias:
- PCR
- principal components regression
refs:
- slide 75
- slide 76
- slide 77
- slide 78
- slide 85
---

## Ce que c'est
Construire les $M$ premières composantes principales, puis les utiliser comme prédicteurs d'une régression par moindres carrés. [slide 75]

## Forme
$$\hat{\mathbf{y}}^{\text{pcr}}_{(M)}=\bar y\mathbf{1}+\sum_{m=1}^{M}\hat\theta_m\mathbf{z}_m,\qquad \hat\theta_m=\frac{\langle \mathbf{z}_m,\mathbf{y}\rangle}{\langle \mathbf{z}_m,\mathbf{z}_m\rangle}$$ [slide 76]

## Ce que les symboles modélisent
$\mathbf{z}_m$ est la $m$-ième composante principale calculée sur les données, une colonne de valeurs, une par observation. $\hat\theta_m$ est le coefficient de la régression de $\mathbf{y}$ sur cette seule colonne ; les composantes étant orthogonales, il ne dépend pas des autres. [slide 76]

$M$ est le nombre de composantes retenues, le seul réglage de la méthode : au-delà, les composantes sont écartées, pas rétrécies. $\bar y\mathbf{1}$ est la moyenne de la réponse répétée sur toutes les observations, la prédiction qu'on ferait sans aucun prédicteur, et $\hat{\mathbf{y}}^{\text{pcr}}_{(M)}$ le vecteur des prédictions obtenues avec $M$ composantes. [slide 76, ajout]

## Ce qui la définit
Les composantes étant orthogonales, la régression se réduit à une somme de régressions univariées : chaque coefficient se calcule indépendamment des autres. [slide 76]

L'hypothèse de fond est explicite et n'est pas garantie : on suppose que les directions où les prédicteurs varient le plus sont celles qui sont liées à la réponse. [slide 75]

La parenté avec ridge est étroite, et la différence tient dans le facteur appliqué à la coordonnée de $\mathbf{y}$ sur la direction $j$ : ridge la multiplie par $d_j^2/(d_j^2+\lambda)$, qui rétrécit tout sans rien annuler ; la régression sur composantes principales, par 1 pour les $M$ premières directions et par 0 au-delà. [slide 77, slide 78]


## Le chemin jusqu'ici
Chaque étape est un changement de base, jamais un changement de méthode. dss/decomposition-en-valeurs-singulieres réécrit la matrice des prédicteurs, dss/composante-principale en range les directions par variance décroissante, et l'on revient pour finir à dss/moindres-carres-ordinaires, mais sur les composantes au lieu des prédicteurs observés dans dss/apprentissage-supervise. [ajout]

## Exemple minimal
Sur les 20 clients, deux composantes laissent une erreur mesurée sur 20 000 clients nouveaux de 3,73 ; il faut les cinq, c'est-à-dire ne rien réduire, pour retrouver 1,83, celle des moindres carrés. [ajout]

Sur les données de crédit du cours, l'erreur de validation croisée ne chute franchement qu'à la dixième composante, sur onze : presque aucune réduction, et la méthode n'y fait guère mieux que les moindres carrés. [slide 84]

## Geste de calcul type
Standardiser, construire les composantes, faire varier $M$ et lire la courbe d'erreur de validation croisée : le biais baisse et la variance monte avec $M$. [slide 85]

## Cesse d'être valide quand
Ce n'est pas une méthode de sélection de variables, le cours insiste. Et rien ne garantit que les premières composantes aient à voir avec la réponse. [slide 85, slide 86]

Sur les 20 clients, les quatre premières laissent une erreur de test de 3,89 ; c'est la cinquième, la moins étirée, qui la fait tomber à 1,83, parce qu'elle oppose l'endettement à x3, la variable sans lien que le hasard a liée à l'endettement sur ces 20 clients. [ajout]

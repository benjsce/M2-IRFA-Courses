---
id: dss/decomposition-en-valeurs-singulieres
nom: Décomposition en valeurs singulières
symbole: $\mathbf{X}=\mathbf{U}\mathbf{D}\mathbf{V}^T$, $d_j$
type: notion
statut: source
construite_a_partir_de:
- dss/moindres-carres-ordinaires
alias:
- SVD
- singular value decomposition
refs:
- slide 58
- slide 59
- slide 60
---

## Ce que c'est
L'écriture de la matrice centrée des prédicteurs comme produit de deux matrices orthogonales et d'une diagonale, base où l'effet de ridge se lit direction par direction. [slide 58, slide 60]

## Forme
$$\mathbf{X}=\mathbf{U}\mathbf{D}\mathbf{V}^T$$ [slide 58]

Dans cette base, l'ajustement des moindres carrés et celui de ridge s'écrivent : [slide 59]

$$\mathbf{X}\hat\beta^{\text{ls}}=\mathbf{U}\mathbf{U}^T\mathbf{y},\qquad \mathbf{X}\hat\beta^{\text{ridge}}=\sum_{j=1}^{p}\mathbf{u}_j\frac{d_j^2}{d_j^2+\lambda}\mathbf{u}_j^T\mathbf{y}$$ [slide 59]

## Ce que les symboles modélisent
Dans $\mathbf{X}=\mathbf{U}\mathbf{D}\mathbf{V}^T$, $\mathbf{X}$ est la matrice $n\times p$ des prédicteurs centrés. $\mathbf{V}$, $p\times p$ et orthogonale, donne $p$ directions de l'espace des prédicteurs ; $\mathbf{D}$, $p\times p$ et diagonale, dit de combien les données s'étirent le long de chacune ; $\mathbf{U}$, $n\times p$, a des colonnes $\mathbf{u}_j$ orthonormées, une par direction, qui forment une base où lire $\mathbf{y}$. [slide 58, slide 59]

$d_j$ est le $j$-ième terme de la diagonale, la valeur singulière de rang $j$ : $d_j^2/n$ est la variance des données le long de la direction $j$. [slide 59, slide 61, ajout]

L'exposant « ls » désigne les moindres carrés, « ridge » la régression ridge, dont $\lambda$ est la pénalité. [slide 59]

## Ce qui la définit
On connaît les coordonnées de $\mathbf{y}$ dans la base orthonormée $\mathbf{U}$. Les moindres carrés les gardent telles quelles ; ridge multiplie la $j$-ième par $d_j^2/(d_j^2+\lambda)$. Toute la différence entre les deux tient dans ce facteur. [slide 60]

Le rétrécissement est donc inégal : il est d'autant plus fort que $d_j^2$ est petit. Les directions de faible variance sont écrasées, celles de forte variance à peine touchées. [slide 60, slide 61]

On en tire aussi $\mathbf{X}^T\mathbf{X}=\mathbf{V}\mathbf{D}^2\mathbf{V}^T$, la décomposition en éléments propres de $\mathbf{X}^T\mathbf{X}$. [slide 61]

## Le chemin jusqu'ici
dss/moindres-carres-ordinaires fournit la matrice des prédicteurs, une ligne par observation de dss/apprentissage-supervise, et l'ajustement $\mathbf{X}\hat\beta^{\text{ls}}$ que la décomposition réécrit. Elle ne suppose rien de statistique : c'est une réécriture de cette matrice. [ajout]

## Exemple minimal
Sur les 20 clients, prédicteurs standardisés, les valeurs singulières vont de 6,70 pour la direction la plus étirée à 2,12 pour la moins étirée. Avec $\lambda=5$, ridge garde 0,90 de la coordonnée de $\mathbf{y}$ sur la première, 0,47 sur la dernière. [ajout]

![Les cinq directions des 20 clients, de la plus étirée à la moins étirée. Chaque cadre vaut 1 : la coordonnée de $\mathbf{y}$ que gardent les moindres carrés, entière. La barre est la part qu'en garde ridge avec $\lambda=5$, $d_j^2/(d_j^2+\lambda)$ : presque tout sur la première direction, moins de la moitié sur la dernière.](figures/decomposition-en-valeurs-singulieres.svg) [ajout]

## Geste de calcul type
Pour savoir ce que la pénalité fait réellement, ne pas regarder les coefficients mais les valeurs singulières : ce sont elles qui disent quelles directions disparaissent. [slide 60]

## Cesse d'être valide quand
C'est une relecture, pas une méthode : elle ne change aucun résultat, elle dit seulement quelles directions ridge rétrécit le plus. [ajout]

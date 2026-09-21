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
L'écriture de la matrice centrée des prédicteurs comme produit de deux matrices orthogonales et d'une matrice diagonale. [slide 58]

## Forme
$$\mathbf{X}=\mathbf{U}\mathbf{D}\mathbf{V}^T,\qquad \mathbf{X}\hat\beta^{\text{ls}}=\mathbf{U}\mathbf{U}^T\mathbf{y},\qquad \mathbf{X}\hat\beta^{\text{ridge}}=\sum_{j=1}^{p}\mathbf{u}_j\frac{d_j^2}{d_j^2+\lambda}\mathbf{u}_j^T\mathbf{y}$$ [slide 58, slide 59]

## Ce que les symboles modélisent
Dans $\mathbf{X}=\mathbf{U}\mathbf{D}\mathbf{V}^T$, les deux matrices orthogonales sont des changements de repère — elles tournent sans déformer — et la diagonale porte seule l'étirement. $d_j$ est cet étirement pour la direction de rang $j$ ; son carré dit la variance que la direction explique. [slide 58, slide 59]

## Ce qui la définit
Lue dans cette base, la différence entre moindres carrés et ridge tient en un facteur : les deux calculent les coordonnées de $\mathbf{y}$ dans la base orthonormée $\mathbf{U}$, mais ridge les rétrécit de $d_j^2/(d_j^2+\lambda)$. [slide 60]

Le rétrécissement est donc inégal : il est d'autant plus fort que $d_j^2$ est petit. Les directions de faible variance sont écrasées, celles de forte variance à peine touchées. [slide 60, slide 61]

On en tire aussi $\mathbf{X}^T\mathbf{X}=\mathbf{V}\mathbf{D}^2\mathbf{V}^T$, la décomposition en éléments propres. [slide 61]


## Le chemin jusqu'ici
dss/apprentissage-supervise, puis dss/moindres-carres-ordinaires, qui fournit la matrice des prédicteurs. [ajout]

La décomposition ne suppose rien de statistique : c'est une réécriture de cette matrice. Elle servira deux fois, pour relire ridge et pour définir les composantes principales. [ajout]

## Exemple minimal
Avec $\lambda=1$, une direction de valeur singulière $d_j=10$ est rétrécie d'un facteur $100/101$, une direction $d_j=0{,}1$ d'un facteur $0{,}01/1{,}01$. [ajout]

## Geste de calcul type
Pour savoir ce que la pénalité fait réellement, ne pas regarder les coefficients mais les valeurs singulières : ce sont elles qui disent quelles directions disparaissent. [slide 60]

## Cesse d'être valide quand
C'est une relecture, pas une méthode : elle éclaire ridge et prépare les composantes principales, elle ne change aucun résultat. [ajout]

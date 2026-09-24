---
id: pfo/matrice-de-correlation
nom: Matrice de corrélation
symbole: '$\mathbf{R}$, $\mathbf{D}$, $\rho_{ij}$, $\sigma_{ij}$'
type: notion
statut: source
construite_a_partir_de:
- pfo/matrice-de-covariance
alias:
- correlation matrix
- corrélation de Pearson
- Pearson correlation
- matrice des co-mouvements
refs:
- §1.5
- p. 17
- Listing 1.3
---

## Ce que c'est
La matrice des coefficients de corrélation de Pearson entre les rendements de chaque couple d'actifs, obtenue en divisant chaque covariance par le produit des deux écarts types. [§1.5, p. 17]

## Forme
$$\mathbf{R} = \mathbf{D}^{-1/2}\,\boldsymbol{\Sigma}\,\mathbf{D}^{-1/2}, \qquad \mathbf{D} = \mathrm{diag}\left(\sigma_1^2, \dots, \sigma_N^2\right), \qquad \rho_{ij} = \dfrac{\sigma_{ij}}{\sigma_i\,\sigma_j}$$ [p. 17]

## Ce que les symboles modélisent
$\sigma_{ij}$ est la covariance des rendements de $i$ et $j$, le terme courant de $\boldsymbol{\Sigma}$ ; $\rho_{ij}$ est la même information débarrassée de son unité. $\mathbf{D}$ ne contient que les variances, sur sa diagonale, et multiplier $\boldsymbol{\Sigma}$ des deux côtés par $\mathbf{D}^{-1/2}$ revient à diviser chaque terme par le produit des deux écarts types. [p. 17]

$\mathbf{R}$ a donc des 1 sur sa diagonale et des termes entre −1 et 1 ailleurs, que le listing affiche sur cette échelle. [Listing 1.3]

## Ce qui la définit
Le listing la calcule directement par `log_rets_filtered.corr()` et la visualise en carte de chaleur sous le titre de matrice des co-mouvements. [Listing 1.3]

Contrairement à la covariance, elle ne dépend pas de l'échelle : annualiser ou non les rendements ne la change pas, parce que le facteur 252 se simplifie entre le numérateur et le dénominateur. C'est pourquoi aucun facteur n'apparaît dans le calcul. [ajout]

## Le chemin jusqu'ici
pfo/matrice-de-covariance porte l'information ; la corrélation n'en retient que le sens et l'intensité du co-mouvement, une fois retirée la taille des mouvements. [ajout]

Derrière la covariance se trouvent pfo/rendement-logarithmique pour ses entrées, fpp/volatilite pour les écarts types qui servent ici de diviseurs, et fpp/echelonnement-de-la-variance pour le facteur 252 — qui disparaît justement dans le quotient. [ajout]

## Exemple minimal
Deux actifs de covariance annualisée 0,0252 et de variances 0,0252 et 0,1008 ont une corrélation de 0,5. [ajout]

## Geste de calcul type
$\rho_{12} = 0{,}0252 / \sqrt{0{,}0252 \times 0{,}1008} = 0{,}0252 / 0{,}0504 = 0{,}5$. [ajout]

## Cesse d'être valide quand
Calculée sur des places désynchronisées, elle est biaisée vers le bas : c'est l'effet Epps. [§1.3.1]

Elle ne mesure que la dépendance linéaire moyenne : deux actifs peu corrélés en temps normal peuvent chuter ensemble dans un krach. [ajout]

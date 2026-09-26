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
$$\rho_{ij} = \dfrac{\sigma_{ij}}{\sigma_i\,\sigma_j}, \qquad\text{soit, en matrice :}\qquad \mathbf{R} = \mathbf{D}^{-1/2}\,\boldsymbol{\Sigma}\,\mathbf{D}^{-1/2}, \qquad \mathbf{D} = \mathrm{diag}\left(\sigma_1^2, \dots, \sigma_N^2\right)$$ [p. 17]

## Ce que les symboles modélisent
$\sigma_{ij}$ est la covariance des rendements de $i$ et $j$, le terme courant de $\boldsymbol{\Sigma}$, et $\sigma_i=\sqrt{\sigma_{ii}}$ l'écart type de l'actif $i$ ; $\rho_{ij}$ est la même information que $\sigma_{ij}$, débarrassée de son unité. [p. 17, ajout]

$\mathbf{D}$ ne contient que les variances, sur sa diagonale, et multiplier $\boldsymbol{\Sigma}$ des deux côtés par $\mathbf{D}^{-1/2}$ revient à diviser chaque terme par le produit des deux écarts types. $\mathbf{R}$ a donc des 1 sur sa diagonale et des termes entre −1 et 1 ailleurs, que le listing affiche sur cette échelle. [p. 17, Listing 1.3]

## Ce qui la définit
Le listing la calcule directement par `log_rets_filtered.corr()` et la visualise en carte de chaleur sous le titre de matrice des co-mouvements. [Listing 1.3]

Contrairement à la covariance, elle ne dépend pas de l'échelle : annualiser ou non les rendements ne la change pas, parce que le facteur 252 se simplifie entre le numérateur et le dénominateur. C'est pourquoi aucun facteur n'apparaît dans le calcul. [ajout]

## Le chemin jusqu'ici
pfo/matrice-de-covariance porte l'information ; la corrélation n'en retient que le sens et l'intensité du co-mouvement, une fois retirée la taille des mouvements. [ajout]

Les écarts types qui servent de diviseurs sont ceux de fpp/volatilite, calculés sur les mêmes rendements de pfo/rendement-logarithmique que la covariance ; le facteur 252 de fpp/echelonnement-de-la-variance, présent en haut et en bas, disparaît dans le quotient. [ajout]

## Exemple minimal
Deux actifs de covariance annualisée $\sigma_{12}=0{,}0252$ et de variances $\sigma_1^2=0{,}0252$ et $\sigma_2^2=0{,}1008$ ont une corrélation de 0,5. [ajout]

## Geste de calcul type
Diviser le terme croisé par le produit des deux écarts types : $\sigma_1=\sqrt{0{,}0252}=0{,}159$, $\sigma_2=\sqrt{0{,}1008}=0{,}317$, dont le produit vaut 0,0504, d'où $\rho_{12}=\sigma_{12}/(\sigma_1\sigma_2)=0{,}0252/0{,}0504=0{,}5$. Que $\sigma_{12}$ et $\sigma_1^2$ valent tous deux 0,0252 est une coïncidence de l'exemple. [ajout]

## Cesse d'être valide quand
Calculée sur des places désynchronisées, elle est biaisée vers le bas : c'est l'effet Epps. [§1.3.1]

Elle ne mesure que la dépendance linéaire moyenne : deux actifs peu corrélés en temps normal peuvent chuter ensemble dans un krach. [ajout]

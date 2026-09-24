---
id: pfo/norme-de-frobenius
nom: Norme de Frobenius
symbole: '$\|\cdot\|_F$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- Frobenius norm
- distance de Frobenius
refs:
- §1.6.1
- éq. 1.12
- Listing 1.4
---

## Ce que c'est
La racine de la somme des carrés de tous les termes d'une matrice, employée comme distance globale entre deux matrices. [§1.6.1, éq. 1.12]

## Forme
$$\|\boldsymbol{\Sigma}_{\text{Daily}} - \boldsymbol{\Sigma}_{\text{Weekly}}\|_F = \sqrt{\sum_{i=1}^{N}\sum_{j=1}^{N} \left(\sigma_{ij,D} - \sigma_{ij,W}\right)^2}$$ [éq. 1.12]

## Ce que les symboles modélisent
$\|\cdot\|_F$ prend une matrice et rend un nombre positif, nul seulement pour la matrice nulle. Appliquée à la différence de deux matrices, elle agrège tous les écarts terme à terme en une seule distance, sans dire lesquels dominent. [éq. 1.12]

## Ce qui la définit
Le cours l'introduit comme mesure de la distance globale entre deux matrices, pour comparer une covariance estimée sur des rendements journaliers et une autre estimée sur des rendements hebdomadaires ; en Python, `np.linalg.norm(matrix_diff, ord='fro')`. [§1.6.1, Listing 1.4]

C'est la norme euclidienne ordinaire, appliquée à la matrice mise à plat en un seul vecteur de tous ses termes. [ajout]

## Exemple minimal
Une matrice d'écarts de termes diagonaux 0,001 et −0,003 et de terme hors diagonale 0,002 a une norme de Frobenius de 0,0042. [ajout]

## Geste de calcul type
$\sqrt{0{,}001^2 + 0{,}002^2 + 0{,}002^2 + 0{,}003^2} = \sqrt{18 \times 10^{-6}} = 0{,}0042$ : le terme hors diagonale compte deux fois, puisque la matrice est symétrique. [ajout]

## Cesse d'être valide quand
Elle n'a pas d'échelle propre : une distance de 0,004 est grande entre des covariances de l'ordre de 0,02, négligeable entre des covariances de l'ordre de 1. La rapporter à la norme de l'une des deux matrices en fait un écart relatif. [ajout]

Elle dit que deux matrices diffèrent, pas pourquoi : l'étude de cas laisse cette question aux questions de réflexion. [§1.6.2]

## Origine
- exercice pfo/ex-01 : la distance ne distingue pas un écart de calendrier, un écart de filtrage et un bruit d'estimation ; il faut les séparer à la main [ajout]

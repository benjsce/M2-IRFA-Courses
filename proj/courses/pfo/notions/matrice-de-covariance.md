---
id: pfo/matrice-de-covariance
nom: Matrice de variance-covariance
symbole: '$\boldsymbol{\Sigma}$, $\mathbf{r}_t$'
type: notion
statut: source
construite_a_partir_de:
- pfo/rendement-logarithmique
- fpp/echelonnement-de-la-variance
alias:
- covariance matrix
- matrice de covariance
- variance-covariance matrix
refs:
- §1.5
- éq. 1.11
- Listing 1.3
- §1.6
---

## Ce que c'est
La matrice carrée qui porte, pour chaque couple d'actifs, la covariance de leurs rendements, et sur sa diagonale leurs variances, ici annualisées. [§1.5, éq. 1.11]

## Forme
$$\boldsymbol{\Sigma} = 252 \times \dfrac{1}{T-1} \sum_{t=1}^{T} (\mathbf{r}_t - \mu)(\mathbf{r}_t - \mu)^{\top}$$ [éq. 1.11]

## Ce que les symboles modélisent
$\mathbf{r}_t$ est le vecteur colonne des rendements des $N$ actifs à la date $t$, et $\mu$ ici le vecteur de leurs rendements moyens. $\boldsymbol{\Sigma}$ est de dimension $N \times N$. [éq. 1.11]

Le terme $(i,j)$ de $\boldsymbol{\Sigma}$ dit si les actifs $i$ et $j$ montent et baissent ensemble, mais dans l'unité d'un rendement au carré, ce qui le rend difficile à lire seul : c'est le rôle de la corrélation. La matrice est symétrique, puisque la covariance de $i$ et $j$ est celle de $j$ et $i$. [ajout]

## Ce qui la définit
Le cours la présente comme l'espace des co-mouvements entre actifs. Le facteur 252 annualise des rendements journaliers ; en Python, `log_rets_filtered.cov() * 252`. Sur des rendements hebdomadaires, le facteur devient 52. [§1.5, éq. 1.11, Listing 1.3, Listing 1.4]

Le diviseur $T-1$ plutôt que $T$ est celui de l'estimateur sans biais, et c'est aussi celui qu'emploie pandas. [ajout]

## Le chemin jusqu'ici
Les entrées de la matrice sont des rendements de pfo/rendement-logarithmique, centrés sur leur moyenne. Sur la diagonale, on retrouve le carré de l'écart type que fpp/volatilite définit ; hors de la diagonale, sa généralisation à deux actifs. [ajout]

Le facteur 252 est une application directe de fpp/echelonnement-de-la-variance. Il n'est juste que si les rendements journaliers sont indépendants d'un jour à l'autre ; sinon l'estimation journalière annualisée et l'estimation hebdomadaire annualisée divergent. [ajout]

## Exemple minimal
Deux actifs de volatilités journalières 1 % et 2 % et de corrélation 0,5 ont une matrice annualisée de diagonale 0,0252 et 0,1008, et de terme croisé 0,0252. [ajout]

## Geste de calcul type
Multiplier chaque terme journalier par 252 : $0{,}01^2 \times 252 = 0{,}0252$, $0{,}02^2 \times 252 = 0{,}1008$, et $0{,}5 \times 0{,}01 \times 0{,}02 \times 252 = 0{,}0252$. [ajout]

## Ce qui reste libre
| fréquence des rendements | facteur d'annualisation |
|---|---|
| journalière | 252 |
| hebdomadaire | 52 |
[Listing 1.3, Listing 1.4]

L'étude de cas du cours pose précisément le choix entre les deux pour un portefeuille rééquilibré chaque mois. [§1.6]

## Cesse d'être valide quand
Sur des places qui ne cotent pas aux mêmes heures, les covariances journalières sont biaisées vers le bas par l'effet Epps. [§1.3.1]

Estimée sur peu d'observations au regard du nombre d'actifs, elle devient bruitée ; avec autant d'actifs que d'observations, ou davantage, elle n'est plus inversible. [ajout]

## Origine
- exercice pfo/ex-01 : le facteur 252 suppose 252 lignes par an ; avec le Bitcoin dans le tableau, il y en a environ 365, et les variances journalières annualisées sont sous-estimées face aux hebdomadaires [ajout]

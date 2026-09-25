---
id: pfo/frontiere-efficiente
nom: Frontière efficiente
symbole: '$\mu_0$, $\mu_p$'
type: notion
statut: source
cas_de: pfo/optimisation-de-portefeuille
valeur: minimiser la variance, le rendement espéré étant fixé à une cible
construite_a_partir_de:
- pfo/moments-du-portefeuille
alias:
- efficient frontier
- minimisation du risque sous contrainte de rendement cible
- formulation 1
- portefeuille de variance minimale globale
- GMV
refs:
- §3.0.2
- p. 39
- Fig. 3.1
- p. 52
---

## Ce que c'est
L'ensemble des portefeuilles de variance minimale pour chaque rendement cible, qui se trace comme une courbe dans le plan risque-rendement. [§3.0.2]

## Forme
$$\min_{W}\ \frac12W^T\boldsymbol{\Sigma}W\qquad\text{sous}\quad W^T\mu=\mu_0,\quad W^T\mathbf{1}=1,\quad W\ge0$$ [§3.0.2]

## Ce que les symboles modélisent
$\mu_0$ est le rendement cible, un niveau de rendement espéré qu'on impose au portefeuille avant de chercher le moins risqué de ceux qui l'atteignent. $\mu_p$ est le rendement espéré d'un portefeuille quelconque quand on le place dans le plan, en ordonnée, face à son risque $\sigma_p$ en abscisse. [§3.0.2, p. 39]

## Ce qui la définit
Chaque contrainte a une lecture économique : le portefeuille atteint exactement le rendement cible, tout le capital est investi, et la vente à découvert est interdite. Le facteur un demi ne change pas la solution ; il simplifie les dérivées. [§3.0.2]

Pour un rendement cible donné, le problème fournit le portefeuille de variance minimale parmi tous ceux qui l'atteignent. En faisant varier progressivement $\mu_0$, on obtient une suite de portefeuilles optimaux, chacun caractérisé par son couple $(\sigma_p,\mu_p)$ : leur tracé est la frontière efficiente. [§3.0.2, p. 39]

Graphiquement, la région des portefeuilles réalisables est un nuage dans le plan risque-rendement ; pour chaque cible, on retient le point réalisable le plus à gauche sur la droite horizontale $\mu_p=\mu_0$. [p. 39, Fig. 3.1]

![Deux actifs non corrélés, de rendements 6 % et 10 % et de volatilités 10 % et 20 %. En faisant varier le poids du premier de 0 à 1, le portefeuille décrit une courbe ; le point le plus à gauche est le portefeuille de variance minimale globale. Seule la branche au-dessus de lui est efficiente : sous lui, on peut obtenir plus de rendement pour moins de risque.](figures/frontiere-efficiente.svg) [ajout]

## Le chemin jusqu'ici
La frontière est tracée point par point, et chaque point est un calcul de pfo/moments-du-portefeuille : un rendement espéré imposé, une variance minimisée. [ajout]

La variance vient de pfo/matrice-de-covariance, estimée sur pfo/rendement-logarithmique et annualisée par fpp/echelonnement-de-la-variance, avec le carré de fpp/volatilite sur la diagonale ; le rendement espéré est une moyenne pondérée, parce que pfo/piege-d-agregation l'établit pour pfo/rendement-arithmetique. [ajout]

La forme de la courbe est celle de dup/diversification : quand on mélange, la variance tombe sous celle des composants, et la frontière se creuse vers la gauche. dup/moyenne-variance, en réduisant chaque dup/loterie à deux nombres, avait déjà dessiné le plan où elle se trace. [ajout]

## Exemple minimal
Avec les deux actifs non corrélés de rendements 6 % et 10 % et de volatilités 10 % et 20 %, le portefeuille de variance minimale globale place 80 % dans le premier : rendement 6,8 %, volatilité 8,94 %. [ajout]

## Geste de calcul type
Sans cible de rendement, pour deux actifs non corrélés, les poids de variance minimale sont proportionnels aux inverses des variances : $1/0{,}01=100$ et $1/0{,}04=25$, donc $W=(0{,}8;0{,}2)$. Alors $W^T\mu=0{,}8\times6\,\%+0{,}2\times10\,\%=6{,}8\,\%$ et $\sigma_p=\sqrt{0{,}64\times0{,}01+0{,}04\times0{,}04}=\sqrt{0{,}008}=8{,}94\,\%$. [ajout]

## Ce qui reste libre
| contrainte | cas | effet |
|---|---|---|
| rendement cible | $\mu_0$ fixé | un point de la frontière |
| rendement cible | aucune | le portefeuille de variance minimale globale, le point le plus à gauche |
[§3.0.2, p. 52]

## Cesse d'être valide quand
Faire varier $\mu_0$ sur toute sa plage trace la frontière de variance minimale entière, branche basse comprise. Seule la partie située au-dessus du portefeuille de variance minimale globale est efficiente : sous lui, un autre portefeuille offre à la fois plus de rendement et moins de risque. Le cours appelle « frontière efficiente » la courbe entière. [ajout]

Dans l'exemple, une cible de 6 % impose tout le capital dans le premier actif, pour une volatilité de 10 % : le portefeuille de variance minimale globale fait mieux sur les deux tableaux. [ajout]

La légende de la figure 3.1 du poly, « illustration d'une distribution à asymétrie négative », est celle d'une figure du chapitre 2 ; la figure montre bien la construction de la frontière. [Fig. 3.1]

## Origine
- exercice pfo/ex-02 : le portefeuille de variance minimale globale s'obtient en retirant la contrainte de rendement cible, et ne dépend pas des rendements espérés [p. 52]

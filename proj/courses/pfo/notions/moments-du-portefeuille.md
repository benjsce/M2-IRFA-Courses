---
id: pfo/moments-du-portefeuille
nom: Rendement espéré et variance d'un portefeuille
symbole: '$W$, $\mu$, $\mu_i$, $E(R_p)$, $\sigma_p$'
type: notion
statut: source
cas_de: pfo/paradigme-de-markowitz
construite_a_partir_de:
- pfo/matrice-de-covariance
- pfo/piege-d-agregation
- dup/diversification
alias:
- portfolio expected return and variance
- variance du portefeuille
- risque du portefeuille
- forme quadratique du risque
refs:
- §3.0.1
- p. 37
- p. 38
---

## Ce que c'est
Le rendement espéré d'un portefeuille est linéaire en ses poids, et sa variance en est une forme quadratique construite sur la matrice de covariance. [§3.0.1]

## Forme
$$E(R_p)=\sum_{i=1}^{N}w_iE(R_i)=W^T\mu,\qquad \sigma_p^2=\sum_{i=1}^{N}\sum_{j=1}^{N}w_iw_j\sigma_{ij}=W^T\boldsymbol{\Sigma}W,\qquad \sigma_p=\sqrt{W^T\boldsymbol{\Sigma}W}$$ [§3.0.1, p. 38]

## Ce que les symboles modélisent
$W$ est le vecteur colonne des poids : sa composante $w_i$ est la part du capital placée dans l'actif $i$, un nombre sans unité. $\mu$ est le vecteur colonne des rendements espérés des actifs : sa composante $\mu_i$ vaut $E(R_i)$. [§3.0.1]

$E(R_p)$ est le rendement espéré du portefeuille entier, et $\sigma_p$ son écart type, sa volatilité. Le second n'est pas la moyenne pondérée des volatilités des actifs : il dépend aussi de toutes leurs covariances. [§3.0.1, p. 38]

Au chapitre 2, $W$ désignait la statistique de Shapiro-Wilk, et $\mu$ une moyenne scalaire ; ici, les deux sont des vecteurs. [ajout]

## Ce qui la définit
Le rendement espéré est l'espérance de la somme pondérée des rendements ; la variance est une somme double sur tous les couples d'actifs, où le terme $\sigma_{ii}=\sigma_i^2$ est la variance de l'actif $i$, et les autres des covariances. [§3.0.1]

![La variance de l'exemple, lue comme une grille : chaque case vaut $w_iw_j\sigma_{ij}$, et son carré coloré a une aire proportionnelle. La diagonale porte les variances, le reste les covariances. À gauche, les deux actifs de l'exemple, sans corrélation : les cases hors diagonale sont vides, la somme vaut 0,0125 et σp 11,18 %. À droite, les mêmes actifs parfaitement corrélés : ces cases se remplissent, la somme monte à 0,0225 et σp à 15 %, la moyenne des volatilités.](figures/moments-du-portefeuille.svg) [ajout]

La moyenne pondérée des volatilités n'est la volatilité du portefeuille que si les actifs sont parfaitement corrélés. Dans l'exemple, $\sigma_{12}$ vaudrait alors $0{,}10\times0{,}20=0{,}02$, chaque case hors diagonale $0{,}25\times0{,}02=0{,}005$, et la somme $0{,}0225$ aurait pour racine 15 %. Toute corrélation plus faible vide en partie ces cases, et $\sigma_p$ tombe sous la moyenne. [ajout]

Les poids d'un portefeuille entièrement investi et sans vente à découvert somment à un et sont positifs ou nuls ; ces contraintes servent à l'optimisation, pas au calcul des deux moments. [§3.0.1]

## Le chemin jusqu'ici
Le rendement du portefeuille est d'abord une moyenne pondérée : pfo/piege-d-agregation l'établissait pour pfo/rendement-arithmetique, en prévenant que pfo/rendement-logarithmique ne s'agrège pas ainsi entre actifs. L'espérance hérite de cette linéarité. [ajout]

Le risque demande davantage. pfo/matrice-de-covariance range les covariances des actifs, estimées sur leurs rendements et portées à l'année par fpp/echelonnement-de-la-variance ; sa diagonale porte le carré de fpp/volatilite. La variance du portefeuille est cette matrice lue à travers les poids. [ajout]

Le cas de deux actifs était déjà écrit en décision : dup/loterie réduite par dup/moyenne-variance à deux nombres, puis dup/diversification, où l'écart type d'un mélange peut tomber sous celui de chacun de ses composants. La forme $W^T\boldsymbol{\Sigma}W$ généralise ce calcul à $N$ actifs. [ajout]

## Exemple minimal
Deux actifs non corrélés, de rendements espérés 6 % et 10 % et de volatilités 10 % et 20 %, à parts égales : $E(R_p)=8\,\%$ et $\sigma_p=11{,}18\,\%$, bien sous la moyenne des deux volatilités, 15 %. [ajout]

## Geste de calcul type
Avec $W=(0{,}5;0{,}5)$ : $W^T\mu=0{,}5\times6\,\%+0{,}5\times10\,\%=8\,\%$. La covariance étant nulle, $W^T\boldsymbol{\Sigma}W=0{,}25\times0{,}01+0{,}25\times0{,}04=0{,}0125$, d'où $\sigma_p=\sqrt{0{,}0125}=11{,}18\,\%$. [ajout]

## Cesse d'être valide quand
La linéarité de $E(R_p)$ vaut pour des rendements arithmétiques. Le script du cours estime $\mu$ sur des rendements logarithmiques et calcule pourtant $W^T\mu$ : c'est une approximation, bonne pour des rendements faibles, que le piège d'agrégation du chapitre 1 interdit en toute rigueur. [§3.0.8, §1.2.2]

Les deux moments supposent $\mu$ et $\boldsymbol{\Sigma}$ connus ; ils ne sont qu'estimés, et l'erreur d'estimation passe entière dans tout ce qu'on en déduit. [ajout]

---
id: pfo/slsqp
nom: Méthode SLSQP
symbole: '$f$, $g$, $h$, $x_k$, $d_k$, $H_k$, $\alpha_k$, $L(x, \lambda, \mu)$, $\lambda$, $\mu$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- SLSQP
- Sequential Least Squares Programming
- programmation quadratique séquentielle
- SQP
refs:
- §3.0.6
- éq. 3.1
- éq. 3.3
- éq. 3.4
- éq. 3.5
- éq. 3.6
- éq. 3.7
- éq. 3.11
---

## Ce que c'est
Une méthode d'optimisation sous contraintes qui, à chaque itération, remplace le problème par un sous-problème quadratique à contraintes linéarisées, et avance dans la direction qu'il fournit. [§3.0.6]

## Forme
$$d_k=\arg\min_d\ \nabla f(x_k)^Td+\tfrac12d^TH_kd\quad\text{sous}\quad g(x_k)+\nabla g(x_k)^Td=0,\quad h(x_k)+\nabla h(x_k)^Td\ge0$$
$$x_{k+1}=x_k+\alpha_kd_k$$ [éq. 3.4, éq. 3.5, éq. 3.11]

## Ce que les symboles modélisent
$f$ est la fonction à minimiser, $g$ les contraintes d'égalité, qui doivent s'annuler, et $h$ les contraintes d'inégalité, qui doivent rester positives ou nulles. $x_k$ est le point atteint à l'itération $k$, et $d_k$ le déplacement proposé depuis ce point. [éq. 3.1, éq. 3.2, éq. 3.5]

$H_k$ est une matrice qui tient lieu de courbure : une approximation du hessien du lagrangien $L(x, \lambda, \mu)$, où $\lambda$ et $\mu$ sont les multiplicateurs des contraintes d'égalité et d'inégalité. $\alpha_k$ est la longueur du pas, un nombre qui dit quelle fraction du déplacement on accepte. [éq. 3.3, éq. 3.5, éq. 3.6]

Dans ce chapitre, $\lambda$ et $\mu$ ne sont ni la persistance EWMA ni un rendement espéré, et $\alpha_k$ n'est pas la part $\alpha$ de la ligne de marché des capitaux. [ajout]

## Ce qui la définit
À chaque itération, **connus** : le point $x_k$, la pente $\nabla f(x_k)$ et une courbure approchée $H_k$. **Cherchés** : le déplacement $d_k$, puis la longueur du pas $\alpha_k$. [éq. 3.3, éq. 3.5]

On part d'un point initial $x_0$ choisi par l'utilisateur. À l'itération $k$, on ne cherche pas directement le nouveau point, mais un déplacement $d$ : l'objectif est approché par son développement de Taylor au second ordre, les contraintes par leur linéarisation autour de $x_k$. Le terme $f(x_k)$, constant en $d$, disparaît, et il reste un problème de programmation quadratique. [éq. 3.2, éq. 3.3, éq. 3.4]

Sa solution $d_k$ donne une direction ; une recherche linéaire fixe la longueur du pas $\alpha_k$. [éq. 3.5]

$H_k$ porte l'information de courbure locale du problème. On l'initialise souvent à l'identité, $H_0=I$, puis on la met à jour au fil des itérations par une méthode de quasi-Newton, typiquement BFGS. [éq. 3.6, éq. 3.7]

La descente de gradient, fondée sur une approximation du premier ordre, prend $d_k=-\nabla f(x_k)$, sans courbure ni contraintes ; SLSQP généralise cette idée aux problèmes contraints. [éq. 3.8, éq. 3.9, éq. 3.10, éq. 3.11]

## Exemple minimal
Pour minimiser $f(x)=(x-3)^2$ sous $x\ge0$ depuis $x_0=0$ avec $H_0=1$, le sous-problème propose le déplacement $d_0=6$ ; la recherche linéaire retient le pas $\alpha_0=\tfrac12$, qui mène à $x_1=3$, le minimum. [ajout]

![Une itération de l'exemple. En pointillé, le modèle quadratique du sous-problème, construit en $x_0=0$ avec $H_0=1$ : deux fois plus plat que $f$, il atteint son minimum en $d_0=6$. Le pas $\alpha_0=\tfrac12$ ramène à $x_1=3$, le minimum de $f$.](figures/slsqp.svg) [ajout]

## Geste de calcul type
En $x_0=0$, $\nabla f=2(0-3)=-6$ et la contrainte $x\ge0$ linéarisée devient $d\ge0$. Le sous-problème $\min_d\,-6d+\tfrac12d^2$ est minimal en $d_0=6$, qui la respecte. Avec la vraie courbure, $f''=2$, il aurait proposé $d_0=3$ : l'identité, deux fois trop plate ici, allonge le pas, et c'est la recherche linéaire qui le ramène. [ajout]

La recherche linéaire minimise $f$ le long de la direction : $f(0+6\alpha)=(6\alpha-3)^2$ est nul en $\alpha=\tfrac12$. Le pas entier, $\alpha=1$, mènerait à $x=6$, où $f$ vaut 9, comme au départ. [ajout]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| point de départ $x_0$ | script du cours | le portefeuille équipondéré, $w_i=1/N$ |
| contraintes | budget | $\sum w_i-1=0$, passée comme contrainte d'égalité |
| contraintes | vente à découvert interdite | bornes $0\le w_i\le1$ |
[§3.0.8]

## Cesse d'être valide quand
La méthode s'arrête sur un point stationnaire local, atteint depuis le point de départ. Pour la minimisation de la variance, problème convexe, c'est le minimum global ; pour un objectif quelconque, le résultat peut dépendre du point de départ. [ajout]

Linéariser les contraintes suppose qu'elles soient dérivables ; celles du cours, linéaires, le sont trivialement. [ajout]

---
id: ods/convex-set
nom: Convex set
symbole: '$C$, $\lambda$, $\Delta^{d-1}$, $\mathbb{R}^d_{\geq 0}$'
type: notion
statut: source
alias:
- convexity of a set
refs:
- Def. 2.1
- §2.1
- Ex. 2.1
---

## Ce que c'est
A set is convex when it contains the whole segment between any two of its points. [§2.1]

## Forme
$$\forall (x,y)\in C^2,\ \ \forall\lambda\in[0,1],\qquad \lambda x+(1-\lambda)y\in C$$ [Def. 2.1]

## Ce que les symboles modélisent
$C$ is a subset of a real vector space, usually $\mathbb{R}^p$ but possibly of infinite dimension: the definition only needs to add points and multiply them by numbers. [§2.1]

$\lambda$ slides a point along the segment: $\lambda=1$ gives $x$, $\lambda=0$ gives $y$, $\lambda=\tfrac12$ the midpoint. It is a mixing weight, not the regularization parameter that the same letter denotes elsewhere in the course. [Def. 2.1, ajout]

$\Delta^{d-1}$ is the unit simplex, the vectors of $\mathbb{R}^d$ with nonnegative entries summing to $1$ — for instance the weights of a fully invested portfolio without short sales. $\mathbb{R}^d_{\geq 0}$ is the nonnegative orthant, the vectors with nonnegative entries. [Ex. 2.1, ajout]

## Ce qui la définit
![Two sets, two points in each, and the segment between them. In the convex set C the segment stays inside. In the crescent D, the two points sit in the two horns and the segment crosses the hollow, so D is not convex.](figures/convex-set.svg) [Fig. 2.2]

The basic convex sets are the intervals of $\mathbb{R}$ — exactly them —, the affine hyperplanes $\{\varphi(x)=\alpha\}$ and the half-spaces $\{\varphi(x)\leq\alpha\}$ defined by a linear functional $\varphi$, the simplex $\Delta^{d-1}$ and the orthant $\mathbb{R}^d_{\geq 0}$. [Ex. 2.1]

Asking the segment condition only for $\lambda$ in the open interval $(0,1)$ changes nothing, since $\lambda=0$ and $\lambda=1$ give back $y$ and $x$ (Exercise 1). [§2.1, Exercise 1]

## Exemple minimal
The interval $[-1,2]$ is convex; the set $\{-1\}\cup[1,2]$ is not, since the segment from $-1$ to $1$ leaves it at $0$. [Ex. 2.1, ajout]

## Geste de calcul type
To show that a half-space $\{x:\langle a,x\rangle\leq b\}$ is convex, mix two of its points: $\langle a,\lambda x+(1-\lambda)y\rangle=\lambda\langle a,x\rangle+(1-\lambda)\langle a,y\rangle\leq\lambda b+(1-\lambda)b=b$, since $\lambda$ and $1-\lambda$ are nonnegative. [Exercise 2, ajout]

## Cesse d'être valide quand
The definition needs segments, hence a real vector space: on a circle, or on a finite set of choices, "convex" has no meaning. A union of convex sets is in general not convex, as the example $\{-1\}\cup[1,2]$ shows. [§2.1, ajout]

## Origine
- exercise ods/ex-01: the endpoints of the segment carry no information, so the open interval (0, 1) may replace [0, 1] [Exercise 1]
- exercise ods/ex-02: orthant, hyperplane, half-space and unit ball are convex by the same argument — the two weights of a mix are nonnegative and sum to one [Exercise 2]

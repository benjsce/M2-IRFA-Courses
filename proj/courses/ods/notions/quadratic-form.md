---
id: ods/quadratic-form
nom: Quadratic form
symbole: '$q$, $A$, $b$, $c$'
type: notion
statut: source
construite_a_partir_de:
- ods/first-order-optimality-condition
- ods/strongly-convex-function
alias:
- quadratic function
- quadratic problem
refs:
- slide 3
---

## Ce que c'est
The simplest curved objective: a quadratic function of $x$, and minimizing it comes down to solving the linear system $Ax=b$. [slide 3]

## Forme
$$q(x)=\tfrac12x^\top Ax-b^\top x+c,\qquad \nabla q(x)=Ax-b,\qquad A\succ0\ \Longrightarrow\ x^\star=A^{-1}b$$ [slide 3, ajout]

## Ce que les symboles modélisent
$q$ takes a point of $\mathbb{R}^n$ and returns a number. $A$, an $n\times n$ matrix, carries all the curvature: it is the Hessian of $q$, the same at every point, and is taken symmetric. $b$, a vector of $\mathbb{R}^n$, tilts the bowl — it is not the vector of responses of least squares, nor the intercept of ridge regression. $c$, a number, shifts the values and moves nothing. [slide 3, ajout]

## Ce qui la définit
Known: $A$, $b$, $c$. Sought: the minimizer. The gradient $Ax-b$ vanishes exactly at the solutions of $Ax=b$: these are the stationary points. When $A\succ0$, $q$ is strongly convex with modulus the smallest eigenvalue of $A$, so the stationary point exists, is unique and is the global minimizer. [slide 3, ajout]

So a quadratic problem and a linear system with a positive definite matrix are the same problem, seen twice: every method for one is a method for the other. [slide 3, slide 15]

## Le chemin jusqu'ici
ods/first-order-optimality-condition turns "minimize" into "make the gradient vanish", which for $q$ is the linear system; ods/strongly-convex-function, with the modulus given by the smallest eigenvalue of $A$, guarantees that the system has exactly one solution and that it is the minimizer. The first rests on ods/first-order-characterization and ods/local-minima-are-global, for an ods/convex-function, whose ods/epigraph is an ods/convex-set; the second gets existence from ods/existence-under-coercivity, which confines the search as ods/coercive-function says and applies ods/existence-on-a-compact — the minimizer in the sense of ods/optimization-problem. [ajout]

## Exemple minimal
The penalized least squares of the four observations is the quadratic form with $A=\begin{pmatrix}4&1\\1&3\end{pmatrix}$, $b=(1,2)$ and $c=1$; its minimizer is $(\tfrac1{11},\tfrac7{11})$, where $q=\tfrac7{22}$. [ajout]

## Geste de calcul type
Solve $4x_1+x_2=1$, $x_1+3x_2=2$: $x^\star=(\tfrac1{11},\tfrac7{11})$. The minimum is $q(x^\star)=c-\tfrac12b^\top x^\star=1-\tfrac12\cdot\tfrac{15}{11}=\tfrac7{22}\approx0.32$. [ajout]

## Cesse d'être valide quand
$A$ has a negative eigenvalue: $q$ is unbounded below along the corresponding eigenvector, and the stationary point is a saddle. $A$ is positive semidefinite but singular: a minimizer exists only if $b$ lies in the range of $A$, and then there is a whole affine set of them. A non-symmetric $A$ acts only through its symmetric part $\tfrac12(A+A^\top)$. [ajout]

## Origine
- exercise ods/ex-04: the slide leaves A unsymmetrized; in general the gradient is ½(A + Aᵀ)x − b [slide 3, ajout]

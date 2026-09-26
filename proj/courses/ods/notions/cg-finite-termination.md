---
id: ods/cg-finite-termination
nom: Convergence of conjugate gradient in n iterations
type: notion
statut: source
construite_a_partir_de:
- ods/conjugate-directions
alias:
- finite termination of conjugate gradient
refs:
- slide 15
- slide 18
---

## Ce que c'est
Conjugate gradient finds the minimizer of a positive definite quadratic form on $\mathbb{R}^n$, and so solves $Ax=b$, in at most $n$ iterations. [slide 15]

## Forme
$$A\succ0,\ A\in\mathbb{R}^{n\times n}\quad\Longrightarrow\quad g^n=0,\ \ x^n=x^\star=A^{-1}b$$ [slide 15, slide 23]

## Ce que les symboles modélisent
$n$ is the dimension of the space, the number of unknowns; $g^n$ is the gradient after $n$ iterations. If some earlier gradient vanishes, the algorithm stops there with the solution. [slide 15, slide 18]

## Retrouver la formule
Known: the gradients $g^0,g^1,\dots$ are pairwise orthogonal. Sought: why they must run out. On the four observations, $n=2$: $g^0=(-1,-2)$ and $g^1=(\tfrac12,-\tfrac14)$ are orthogonal and nonzero, so they fill the plane, and a third gradient, orthogonal to both, can only be $0$. [slide 23, ajout]

No step is wasted: $\langle g^k,d^k\rangle=\|g^k\|^2$, so $\beta_k$ vanishes only if $g^k=0$, and $\|d^k\|^2=\|g^k\|^2+\alpha_k^2\|d^{k-1}\|^2$, so $d^k\neq0$ as long as $g^k\neq0$. [slide 22]

Nonzero and pairwise orthogonal vectors are linearly independent, and $\mathbb{R}^n$ holds at most $n$ of them: if $g^0,\dots,g^{n-1}$ are all nonzero, the next one has nowhere to go. [slide 23]

$$g^0,\dots,g^{n-1}\neq0\ \text{pairwise orthogonal}\quad\Longrightarrow\quad g^n=0$$ [slide 23]

## Ce qui la définit
The result is exact and holds whatever the conditioning of $A$; it is what makes conjugate gradient a solver and not only a descent method. [slide 15]

## Le chemin jusqu'ici
ods/conjugate-directions supplies the two orthogonality properties that the counting argument uses; they belong to the directions of ods/conjugate-gradient, which only needs the product of ods/matrix-free-product, cheap for an ods/sparse-matrix. The problem is that of ods/quadratic-form, whose minimizer is where the gradient vanishes, by ods/first-order-optimality-condition — itself from ods/first-order-characterization and ods/local-minima-are-global, for an ods/convex-function, whose ods/epigraph is an ods/convex-set. It exists and is unique because $q$ is an ods/strongly-convex-function: ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact answer the question of ods/optimization-problem. [ajout]

## Exemple minimal
For the $2\times2$ system of the four observations, two iterations suffice: $x^2=(\tfrac1{11},\tfrac7{11})$. [ajout]

## Geste de calcul type
Count: $n$ unknowns, at most $n$ iterations, each costing one product with $A$. For the problem of the slides, $n=p=10^6$: at most a million products, each of about $4\times10^6$ operations. [slide 13, slide 24]

## Cesse d'être valide quand
"At most $n$ iterations" is of little help when $n=10^6$: what matters is the accuracy after $k\ll n$ iterations. The bound also assumes exact arithmetic; in floating point the gradients slowly lose their orthogonality. [slide 24, ajout]

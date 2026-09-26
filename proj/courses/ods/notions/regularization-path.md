---
id: ods/regularization-path
nom: Regularization path
type: notion
statut: source
construite_a_partir_de:
- ods/warm-start
- ods/conditioning-of-ridge
alias:
- path of solutions
- grid of λ
refs:
- slide 29
- slide 30
---

## Ce que c'est
The ridge solutions over a decreasing grid of penalties are computed from the largest $\lambda$ down, each solution warm-starting the next. [slide 30]

## Forme
$$\lambda_1>\lambda_2>\dots>\lambda_T:\qquad \hat{w}(\lambda_1)\ \text{from }x^0=0,\qquad \hat{w}(\lambda_{t+1})\ \text{from }x^0=\hat{w}(\lambda_t)$$ [slide 30]

## Ce que les symboles modélisent
$\lambda_1>\dots>\lambda_T$ is the grid, for instance the values tried by cross-validation; $\hat{w}(\lambda_t)$ is the ridge solution for the penalty $\lambda_t$. [slide 29, slide 30]

## Ce qui la définit
![In the plane of the weights, the ridge solutions of the four observations for λ = 100, 10, 3, 1, 0.3, 0.1 and 0. They start near the origin for λ large and end at the exact fit (0, 1) for λ = 0. The arrows give the order of solving: λ = 100 first, from zero, then each solution starts the next.](figures/regularization-path.svg) [ajout]

Start from the largest $\lambda$: $X^\top X+\lambda I$ is then dominated by $\lambda I$, well conditioned and easy to solve, and a crude $x^0$, say $0$, is already good enough, since the solution is close to $X^\top y/\lambda$. Then decrease $\lambda$, each solution warm-starting the next: consecutive problems differ little, so each solve takes few iterations. Going the other way, the first problem solved is the hardest one, and there is nothing to start it from. [slide 30]

Unlike the Lasso, ridge has no finite $\lambda$ for which $\hat{w}=0$: the path only tends to the origin as $\lambda\to\infty$. [slide 30]

## Le chemin jusqu'ici
ods/warm-start says why each solution should start the next, and ods/conditioning-of-ridge says why to begin at the large end: there $\kappa$ is close to $1$. Both lean on ods/cg-convergence-rate, in which the initial error and the ods/condition-number set the iteration count; the solver is ods/conjugate-gradient, with its ods/conjugate-directions and ods/cg-finite-termination, needing only an ods/matrix-free-product on an ods/sparse-matrix, and the comparison is with ods/gradient-descent, from ods/second-order-taylor-expansion and ods/quadratic-upper-bound for an ods/l-smooth-function. [ajout]

The problem is ods/ridge-regression — ods/structural-risk-minimization on the ods/empirical-risk that stands for the ods/expected-risk — whose singular values come from ods/singular-value-decomposition. It is solved as an ods/quadratic-form, minimized where ods/first-order-optimality-condition says, by ods/first-order-characterization and ods/local-minima-are-global for an ods/convex-function, an ods/epigraph that is an ods/convex-set; each point of the path is the unique minimizer of an ods/strongly-convex-function, which exists by ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact — one ods/optimization-problem per $\lambda$. [ajout]

## Exemple minimal
On the four observations: $\hat{w}(100)\approx(0.010,\,0.020)$, $\hat{w}(10)=(\tfrac2{31},\tfrac5{31})$, $\hat{w}(1)=(\tfrac1{11},\tfrac7{11})$, $\hat{w}(0)=(0,1)$. [ajout]

## Geste de calcul type
At $\lambda=100$, $\hat{w}\approx X^\top y/\lambda=(0.01,\,0.02)$, and the exact solution is $(0.0095,\,0.0195)$: zero is already a start within $0.02$ of it, on a system with $\kappa\approx1.02$. [slide 30, ajout]

## Cesse d'être valide quand
The solver is direct: then the order does not matter, and one factorization of $X$, reused for every $\lambda$, is the efficient route. [slide 29]

## Origine
- exercise ods/ex-12: conditioning and the availability of a good start both dictate the order [slide 30, ajout]

---
id: ods/conditioning-of-ridge
nom: Conditioning of ridge regression
symbole: '$\sigma_i$'
type: notion
statut: source
construite_a_partir_de:
- ods/cg-convergence-rate
- ods/singular-value-decomposition
- ods/ridge-regression
alias:
- what λ does to κ
refs:
- slide 26
---

## Ce que c'est
In ridge regression, the penalty $\lambda$ is added to every eigenvalue of $X^\top X$, so it sets the condition number of the system, and with it the cost of solving it. [slide 26]

## Forme
$$\kappa=\frac{\sigma_{\max}^2+\lambda}{\sigma_{\min}^2+\lambda}\qquad\text{for }A=X^\top X+\lambda I_p$$ [slide 26]

## Ce que les symboles modélisent
$\sigma_i$ are the singular values of $X$, and $\sigma_{\max}$, $\sigma_{\min}$ the largest and the smallest; their squares are the eigenvalues of $X^\top X$, each raised by $\lambda$ in $A$. When $n<p$, $X^\top X$ has at least $p-n$ zero eigenvalues, and $\sigma_{\min}=0$. [slide 26, slide 9]

## Ce qui la définit
![The condition number κ against λ, both on logarithmic scales. For the four observations, κ starts at 2.62 when λ = 0, is 1.94 at λ = 1 and falls towards 1. With the same largest singular value and σmin = 0, as when n < p, κ = (3.62 + λ)/λ blows up as λ goes to 0.](figures/conditioning-of-ridge.svg) [slide 26, ajout]

As $\lambda\to\infty$, $\kappa\to1$ and the problem becomes trivial: this is why a path of solutions is computed from the largest $\lambda$ down. When $n<p$, $\sigma_{\min}=0$ and $\kappa=(\sigma_{\max}^2+\lambda)/\lambda\approx\sigma_{\max}^2/\lambda$: the regularization is what makes the problem solvable, not only well posed. The same parameter therefore controls the statistics — bias against variance — and the cost of the optimization. [slide 26]

## Le chemin jusqu'ici
ods/cg-convergence-rate turns a condition number into a number of iterations; ods/singular-value-decomposition gives the eigenvalues of $X^\top X$ as squared singular values; ods/ridge-regression adds $\lambda$ to each of them. The rest of the chain is that of the solver and of the problem. [ajout]

On the solver side: the rate compares ods/conjugate-gradient, whose ods/conjugate-directions give ods/cg-finite-termination and which only needs an ods/matrix-free-product on an ods/sparse-matrix, with ods/gradient-descent, built from ods/second-order-taylor-expansion and ods/quadratic-upper-bound for an ods/l-smooth-function, through the ods/condition-number of the system. [ajout]

On the problem side: ridge has the shape of ods/structural-risk-minimization, on the ods/empirical-risk that replaces the ods/expected-risk, and is solved as an ods/quadratic-form. That form is minimized where ods/first-order-optimality-condition puts it, by ods/first-order-characterization and ods/local-minima-are-global for an ods/convex-function, an ods/epigraph that is an ods/convex-set; the minimizer is unique for an ods/strongly-convex-function and exists by ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact, as ods/optimization-problem requires. [ajout]

## Exemple minimal
For the four observations, $\sigma_{\max}^2\approx3.62$ and $\sigma_{\min}^2\approx1.38$: $\kappa\approx2.62$ at $\lambda=0$, $1.94$ at $\lambda=1$, $1.20$ at $\lambda=10$. [ajout]

## Geste de calcul type
At $\lambda=1$: $\kappa=(3.62+1)/(1.38+1)=4.62/2.38\approx1.94$, the condition number of $\begin{pmatrix}4&1\\1&3\end{pmatrix}$. With $\sigma_{\min}=0$ and $\lambda=0.01$ instead: $\kappa\approx3.62/0.01=362$, so conjugate gradient needs about $7.25\sqrt{362}\approx140$ iterations to gain a factor $10^6$. [slide 25, ajout]

## Cesse d'être valide quand
The formula is for the plain ridge matrix $X^\top X+\lambda I_p$. With an unpenalized intercept column, or a preconditioner, the eigenvalues change and $\kappa$ must be recomputed. [slide 26, ajout]

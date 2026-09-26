---
id: ods/warm-start
nom: Warm start
symbole: '$x^0$'
type: notion
statut: source
construite_a_partir_de:
- ods/cg-convergence-rate
alias:
- warm starting
refs:
- slide 29
- nb. 4
---

## Ce que c'est
To solve a problem close to one already solved, start the iterative solver from the previous solution rather than from zero. [slide 29]

## Forme
$$x^0_{\text{new}}=x^\star_{\text{previous}},\qquad\text{iterations}\ \propto\ \log\frac{\|x^0-x^\star\|_A}{\varepsilon}$$ [slide 29, ajout]

## Ce que les symboles modélisent
$x^0$ is the starting point of the iterative solver. The convergence bound multiplies $\|x^0-x^\star\|_A$ by a fixed factor at each iteration, so the number of iterations needed to reach the precision $\varepsilon$ grows like the logarithm of the initial error: starting closer removes iterations. [slide 24, slide 29, ajout]

## Ce qui la définit
Machine learning often solves a problem very similar to a previous one: a model retrained every day, or a hyperparameter scanned over a grid of values during cross-validation. A warm start is free to implement, and conjugate gradient only cares about how far $x^0$ is from $x^\star$. [slide 29]

It only helps iterative solvers: a direct solver pays the same factorization whatever the starting point. The counterpart for direct solvers on a path is to factorize once and reuse it — with the SVD of $X$ computed once, each new $\lambda$ is cheap. Notebook 4 times the two starts on a sparse ridge with $10^6$ features: from zero at $\lambda=0.01$, then from that solution at $\lambda=0.02$. [slide 29, nb. 4]

## Le chemin jusqu'ici
ods/cg-convergence-rate shows the initial error $\|x^0-x^\star\|_A$ as a factor of the bound: reduce it and fewer iterations reach the same precision. That rate belongs to ods/conjugate-gradient, with its ods/conjugate-directions and ods/cg-finite-termination, driven by an ods/matrix-free-product on an ods/sparse-matrix, and is compared with ods/gradient-descent — the step of ods/second-order-taylor-expansion kept safe by ods/quadratic-upper-bound for an ods/l-smooth-function — through the ods/condition-number. [ajout]

The system solved is that of an ods/quadratic-form, whose solution is its minimizer by ods/first-order-optimality-condition, from ods/first-order-characterization and ods/local-minima-are-global for an ods/convex-function, an ods/epigraph that is an ods/convex-set; the ods/strongly-convex-function guarantees one minimizer, via ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact, the answer to ods/optimization-problem. [ajout]

## Exemple minimal
Going from $\lambda=1$ to $\lambda=2$ on the four observations, the previous solution $(\tfrac1{11},\tfrac7{11})$ is $0.16$ away from the new one $(\tfrac2{19},\tfrac9{19})$, against $0.49$ for the origin. [ajout]

## Geste de calcul type
In the norm of $A=\begin{pmatrix}5&1\\1&4\end{pmatrix}$, the matrix at $\lambda=2$: the initial error is $1.03$ from the origin and $0.32$ from the warm start, about $3.2$ times smaller — the iterations that it takes to divide the error by $3.2$ are saved. [ajout]

## Cesse d'être valide quand
The new problem is not close to the old one: the previous solution may then be no better a start than zero. And for a direct solver a warm start brings nothing. [slide 29]

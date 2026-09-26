---
id: ods/condition-number
nom: Condition number
symbole: '$\kappa$'
type: notion
statut: source
construite_a_partir_de:
- ods/quadratic-form
alias:
- conditioning
refs:
- slide 24
---

## Ce que c'est
The ratio of the largest to the smallest eigenvalue of a positive definite matrix: how much more the quadratic form curves in its steepest direction than in its flattest. [slide 24]

## Forme
$$\kappa=\frac{\lambda_{\max}(A)}{\lambda_{\min}(A)}\ \geq1$$ [slide 24]

## Ce que les symboles modélisent
$\kappa$ is a pure number. $\lambda_{\max}(A)$ and $\lambda_{\min}(A)$ are the extreme eigenvalues of $A$, the curvatures of $q$ along its steepest and flattest directions — for $q$, the constants $L$ and $\mu$ of smoothness and strong convexity, so that $\kappa=L/\mu$. Geometrically, the level sets of $q$ are ellipses whose longest axis is $\sqrt\kappa$ times the shortest. [slide 24, ajout]

## Ce qui la définit
$\kappa=1$ means round level sets, where the gradient points straight at the minimizer; a large $\kappa$ means long thin valleys, where iterative methods slow down. How much they slow down is what the convergence rates measure. [slide 24, slide 26, ajout]

## Le chemin jusqu'ici
ods/quadratic-form puts all the curvature of the problem in the matrix $A$; its eigenvalues, the least of which is the modulus of the ods/strongly-convex-function $q$, give $\kappa$. The minimizer that the ratio makes hard or easy to reach is the one of ods/first-order-optimality-condition, obtained from ods/first-order-characterization and ods/local-minima-are-global for an ods/convex-function, whose ods/epigraph is an ods/convex-set; it exists by ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact, which answer ods/optimization-problem. [ajout]

## Exemple minimal
The system of the four observations, $A=\begin{pmatrix}4&1\\1&3\end{pmatrix}$, has $\kappa=\tfrac{7+\sqrt5}{7-\sqrt5}\approx1.94$: a well-conditioned problem. [ajout]

## Geste de calcul type
Eigenvalues of a symmetric $2\times2$ matrix: $\tfrac{\operatorname{tr}\pm\sqrt{\operatorname{tr}^2-4\det}}2$. Here the trace is $7$ and the determinant $11$: $\tfrac{7\pm\sqrt5}2\approx4.62$ and $2.38$, so $\kappa\approx1.94$. [ajout]

## Cesse d'être valide quand
$\lambda_{\min}(A)=0$: $A$ is singular, $\kappa$ is infinite, and the system may have no solution or infinitely many. For a non-symmetric matrix, the condition number is defined with singular values instead. [ajout]

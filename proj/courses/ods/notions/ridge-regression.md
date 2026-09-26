---
id: ods/ridge-regression
nom: Ridge regression
symbole: '$X$, $y$, $w$, $b$, $\mathbf{1}_n$'
type: notion
statut: source
cas_de: ods/optimization-problem
construite_a_partir_de:
- ods/structural-risk-minimization
- ods/quadratic-form
alias:
- ridge
refs:
- slide 5
- slide 7
---

## Ce que c'est
Least squares with a penalty on the size of the weights, the intercept being left unpenalized. [slide 5]

## Forme
$$\min_{w\in\mathbb{R}^p,\ b\in\mathbb{R}}\ \tfrac12\|y-Xw-b\mathbf{1}_n\|^2+\tfrac\lambda2\|w\|^2,\qquad\lambda>0$$ [slide 5]

## Ce que les symboles modélisent
The slides use the machine-learning notation: $n$ samples and $p$ features. $X\in\mathbb{R}^{n\times p}$ holds the samples as rows $x^i$, $y\in\mathbb{R}^n$ the targets, $w\in\mathbb{R}^p$ the weights. $b\in\mathbb{R}$ is the intercept, or bias, added to every prediction through the vector of ones $\mathbf{1}_n$; it is not penalized. [slide 5]

Compared with the notes, $X$ plays the role of $A$, $y$ of $b$ and $w$ of $x$. [§1.1.2, slide 5, ajout]

## Ce qui la définit
Known: $X$, $y$, $\lambda$. Sought: the weights, and the intercept. The problem has dimension $p+1$. Without intercept — the data being centered — it is the quadratic form of matrix $X^\top X+\lambda I_p$ and linear term $X^\top y$, so the weights solve a linear system. [slide 5, slide 7, ajout]

$$\hat{w}=(X^\top X+\lambda I_p)^{-1}X^\top y$$ [slide 11]

The objective is strongly convex, with constant $\lambda+\sigma_{\min}^2$, $\sigma_{\min}$ being the smallest singular value of $X$; when $n<p$, $\sigma_{\min}=0$ and the constant is $\lambda$ itself. [slide 7, ajout]

## Le chemin jusqu'ici
ods/structural-risk-minimization gives the shape — a fit term plus $\lambda$ times a penalty — with the squared loss of ods/empirical-risk, the stand-in for the ods/expected-risk, and $J(w)=\tfrac12\|w\|^2$. ods/quadratic-form says that such an objective is minimized by solving a linear system, since its gradient is affine: that step uses ods/first-order-optimality-condition, itself built on ods/first-order-characterization and ods/local-minima-are-global for an ods/convex-function — an ods/epigraph that is an ods/convex-set. The penalty makes the objective an ods/strongly-convex-function, so the minimizer exists and is unique, by ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact; ridge regression is one more instance of ods/optimization-problem. [ajout]

## Exemple minimal
On the four observations, without intercept and with $\lambda=1$, ridge gives $\hat{w}=(\tfrac1{11},\tfrac7{11})\approx(0.09,\,0.64)$, where least squares gave $(0,1)$. [ajout]

## Geste de calcul type
$X^\top X=\begin{pmatrix}3&1\\1&2\end{pmatrix}$, so $X^\top X+I=\begin{pmatrix}4&1\\1&3\end{pmatrix}$, and $X^\top y=(1,2)$; solving gives $\hat{w}=(\tfrac1{11},\tfrac7{11})$, whose norm, $0.64$, is smaller than that of $(0,1)$. [ajout]

## Cesse d'être valide quand
$\lambda=0$ and $X$ does not have full column rank: the penalty was what made the minimizer unique. And the closed form needs to store and factor $X^\top X+\lambda I_p$, a $p\times p$ matrix: with $p=10^6$ it takes 8 TB. [slide 12, ajout]

## Origine
- exercise ods/ex-07: when n < p the strong convexity constant is λ itself; the penalty alone makes the minimizer unique [slide 7, ajout]

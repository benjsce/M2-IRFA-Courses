---
id: ods/optimization-problem
nom: Optimization problem
symbole: '$f$, $\Omega$, $x^\star$'
type: principe
statut: source
alias:
- minimization problem
- unconstrained optimization problem
- objective function
refs:
- §1
- slide 2
---

## Ce que c'est
Many problems of modelling and machine learning are one question in disguise: among the admissible points, find one where a given function is as small as possible. [§1]

## Forme
$$\inf_{x}\ f(x)\quad\text{subject to}\quad x\in\Omega$$ [§1]

## Ce que les symboles modélisent
$f$ is the objective function: it takes a point and returns a number, the cost we want small. The slides let it take the value $+\infty$, which excludes a point without writing a constraint. [§1, slide 2]

$\Omega$ is the domain, the set of admissible points. When $\Omega$ is the whole space $\mathbb{R}^n$, the problem is called unconstrained. [§1, slide 2]

$x^\star$ is a minimizer: a point of $\Omega$ where the infimum is attained, and $f(x^\star)$ is then the minimum of $f$ over $\Omega$. [§1]

$\mu$ and $\Sigma$ only appear in the portfolio example: the vector of expected returns of the assets and the covariance matrix of their returns. [§1.1.4]

## Ce qui la définit
The infimum and the minimizer are two different objects. The infimum is a number, always defined, possibly $-\infty$; a minimizer is a point, and it may not exist. The first theorems of the course say when it does. [§1, §1.2]

The same template covers problems whose unknown is a vector, a prediction rule, a control or a transport map: only $f$ and $\Omega$ change (see the table below). [§1.1]

## Exemple minimal
Minimize $f(x)=x^2-\cos x$ over $\Omega=\mathbb{R}$: the infimum is $-1$, attained at the single minimizer $x^\star=0$. [ajout]

## Geste de calcul type
Name the unknown, the objective and the domain. For the portfolio of $n$ assets: the unknown is the vector of weights $x\in\mathbb{R}^n$, the objective is the variance $\langle\Sigma x,x\rangle$, and $\Omega$ holds the weights whose expected return $\langle x,\mu\rangle$ equals the target $r$ and which sum to one. [§1.1.4]

## Ce qui reste libre
| problem | unknown | objective | domain |
|---|---|---|---|
| least squares | weights $x\in\mathbb{R}^d$ | sum of squared residuals $\tfrac12\lVert Ax-b\rVert^2$ | all of $\mathbb{R}^d$ |
| risk minimization | a prediction rule $\phi$ | its expected or empirical risk | a class of prediction rules |
| portfolio | weights $x\in\mathbb{R}^n$ | the variance $\langle\Sigma x,x\rangle$ | target return, weights summing to one |
| optimal control | a control $u$ over $[0,T]$ | the integrated cost of the trajectory it drives | controls whose trajectory exists on $[0,T]$ |
| optimal transport | a map sending one distribution onto another | the total transport cost | maps that push the first distribution onto the second |
[§1.1.2, §1.1.3, §1.1.4, §1.1.5, §1.1.6]

## Cesse d'être valide quand
The formulation always makes sense, but it promises nothing: the infimum may be $-\infty$, as for $f(x)=x$ on $\mathbb{R}$, or finite and never reached, as for $f(x)=1/x$ on $x>0$, whose infimum $0$ no point attains. [§1.2]

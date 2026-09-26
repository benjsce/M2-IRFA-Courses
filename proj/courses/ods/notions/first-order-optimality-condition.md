---
id: ods/first-order-optimality-condition
nom: First-order optimality condition
type: notion
statut: source
construite_a_partir_de:
- ods/first-order-characterization
- ods/local-minima-are-global
alias:
- stationary point
- vanishing gradient
- variational inequality
refs:
- p. 9
---

## Ce que c'est
For a differentiable convex function, a point is a global minimizer exactly when no admissible direction goes downhill from it — on an open domain, when its gradient vanishes. [p. 9]

## Forme
$$\nabla f(x^\star)=0\quad\text{(open domain)},\qquad\big\langle\nabla f(x^\star),\,x-x^\star\big\rangle\geq0\ \ \forall x\in C\quad\text{(convex set } C)$$ [p. 9]

## Ce que les symboles modélisent
$x-x^\star$ is a direction that stays admissible, from $x^\star$ towards another point of $C$. The inner product with the gradient is the slope of $f$ in that direction: nonnegative means that $f$ does not decrease when one starts moving that way. [p. 9, ajout]

## Retrouver la formule
![Two minimizers. On the left, without constraint, f(x) = x² − cos x has a flat tangent at its minimizer x* = 0. On the right, the example of the notes: f(x) = x on the interval from 0 to 1 has its minimizer at 0, where the slope is 1, not 0; the only direction that goes downhill, to the left, leaves the interval.](figures/first-order-optimality-condition.svg) [p. 9, ajout]

Known: the tangent inequality $f(x)\geq f(x^\star)+\langle\nabla f(x^\star),x-x^\star\rangle$ of a convex function. Sought: a test at $x^\star$ alone. [p. 9]

On an open domain, a local minimizer has a flat tangent: moving a little in any direction and back cannot lower $f$, so every directional slope is zero and $\nabla f(x^\star)=0$. The tangent inequality then reads $f(x)\geq f(x^\star)$ for every $x$: the flat tangent is global. [p. 9]

On a convex set, only the directions towards other points of $C$ are allowed. A local minimizer has a nonnegative slope along each segment it can follow, $\langle\nabla f(x^\star),x-x^\star\rangle\geq0$; the tangent inequality again turns this into $f(x)\geq f(x^\star)$ on all of $C$. On the right of the figure, the slope is $1$ in the only allowed direction, and $0$ is the minimizer. [p. 9]

$$\big\langle\nabla f(x^\star),\,x-x^\star\big\rangle\geq0\ \ \forall x\in C\quad\Longrightarrow\quad f(x)\geq f(x^\star)\ \ \forall x\in C$$ [p. 9]

## Ce qui la définit
The condition is necessary for any local minimizer, convex or not; convexity is what makes it sufficient, and global. The gradient need not vanish at a constrained minimizer. [p. 9]

## Le chemin jusqu'ici
ods/first-order-characterization turns a flat or rising tangent at $x^\star$ into a bound on the whole domain, and ods/local-minima-are-global says that nothing better hides far away once $x^\star$ wins locally. Both rest on ods/convex-function, whose ods/epigraph is an ods/convex-set; the minimizer being certified is the one of ods/optimization-problem. [ajout]

## Exemple minimal
For the penalized least squares of the four observations, $\tfrac12\|Ax-b\|^2+\tfrac12\|x\|^2$, the gradient vanishes at $x^\star=(\tfrac1{11},\tfrac7{11})$, which is therefore the global minimizer. [ajout]

## Geste de calcul type
$\nabla f(x)=A^\top(Ax-b)+x=(A^\top A+I)x-A^\top b$. With $A^\top A+I=\begin{pmatrix}4&1\\1&3\end{pmatrix}$ and $A^\top b=(1,2)$: $4x_1+x_2=1$ and $x_1+3x_2=2$, so $x_1=\tfrac{3-2}{11}=\tfrac1{11}$ and $x_2=\tfrac{8-1}{11}=\tfrac7{11}$. [ajout]

## Cesse d'être valide quand
$f$ is not convex: the gradient also vanishes at local maxima, at saddle points and at local minima that are not global, so the condition is only necessary. On a constraint set, the gradient need not vanish: $f(x)=x$ on $[0,1]$ has $f'(0)=1$ at its minimizer. And $f$ must be differentiable at $x^\star$. [p. 9, ajout]

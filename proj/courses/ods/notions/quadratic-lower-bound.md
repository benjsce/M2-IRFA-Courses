---
id: ods/quadratic-lower-bound
nom: Quadratic lower bound
type: notion
statut: source
construite_a_partir_de:
- ods/strongly-convex-function
- ods/first-order-characterization
alias:
- strong convexity inequality
refs:
- Prop. 2.3
- eq. 2.4
- Fig. 2.4
---

## Ce que c'est
A differentiable $\mu$-strongly convex function lies above each of its tangents plus the parabola $\tfrac\mu2\|x-\bar{x}\|^2$, and not merely above the tangent. [Prop. 2.3]

## Forme
$$f(x)\geq f(\bar{x})+\big\langle\nabla f(\bar{x}),x-\bar{x}\big\rangle+\frac\mu2\|x-\bar{x}\|^2,\qquad f(x)\geq f(x^\star)+\frac\mu2\|x-x^\star\|^2$$ [Prop. 2.3, eq. 2.4]

## Ce que les symboles modélisent
The right-hand side of the first inequality is a parabola that touches $f$ at $\bar{x}$ from below. At the minimizer $x^\star$, the gradient vanishes and the bound becomes the second one: the value above the minimum is at least $\tfrac\mu2$ times the squared distance to the minimizer. [Prop. 2.3, eq. 2.4]

## Retrouver la formule
![The graph of f(x) = x² − cos x, its tangent at x̄ = 1, and the tangent plus the parabola ½(x − 1)², with μ = 1. The curve stays above the second one too: at x = −1 there is still about 3.68 of room.](figures/quadratic-lower-bound.svg) [Fig. 2.4, ajout]

Known: $h(x)=f(x)-\tfrac\mu2\|x\|^2$ is convex. Sought: what $f$ gains over its tangent. With $f(x)=x^2-\cos x$ and $\mu=1$: $h(x)=\tfrac12x^2-\cos x$. [§2.3, ajout]

$h$ is convex and differentiable, so it lies above its tangent at $\bar{x}$: $h(x)\geq h(\bar{x})+\langle\nabla h(\bar{x}),x-\bar{x}\rangle$, with $\nabla h(\bar{x})=\nabla f(\bar{x})-\mu\bar{x}$. [Prop. 2.3]

Add $\tfrac\mu2\|x\|^2$ back on both sides. The terms in $\mu$ collect into $\tfrac\mu2\|x\|^2-\tfrac\mu2\|\bar{x}\|^2-\mu\langle\bar{x},x-\bar{x}\rangle$, which is exactly $\tfrac\mu2\|x-\bar{x}\|^2$. At $\bar{x}=1$, $x=-1$: the tangent gives $-5.22$, the parabola adds $\tfrac12\cdot4=2$, and $-3.22\leq f(-1)\approx0.46$. [ajout]

$$f(x)\geq f(\bar{x})+\big\langle\nabla f(\bar{x}),x-\bar{x}\big\rangle+\frac\mu2\|x-\bar{x}\|^2$$ [Prop. 2.3]

## Ce qui la définit
What the bound buys: a small gap in value forces a small distance, $\|x-x^\star\|\leq\sqrt{2\big(f(x)-f(x^\star)\big)/\mu}$. It is the key property for lower bounds; for a differentiable function on a convex domain it is equivalent to strong convexity, with the same $\mu$ for all pairs of points. [p. 10, eq. 2.4]

## Le chemin jusqu'ici
ods/strongly-convex-function makes $f-\tfrac\mu2\|x\|^2$ convex, and ods/first-order-characterization puts that function above its tangent; adding the parabola back gives the bound. Behind them: ods/convex-function, the convexity of the ods/epigraph as an ods/convex-set; the existence of the minimizer $x^\star$ used in (2.4), which ods/existence-under-coercivity provides by making the search bounded (ods/coercive-function) and applying ods/existence-on-a-compact — a minimizer in the sense of ods/optimization-problem. [ajout]

## Exemple minimal
For $f(x)=x^2-\cos x$, with $\mu=1$: $f(x)\geq-1+\tfrac12x^2$, so a point where $f(x)\leq-0.98$ lies within $0.2$ of the minimizer. [ajout]

## Geste de calcul type
At $\bar{x}=1$: $f(1)\approx0.46$ and $f'(1)\approx2.84$, so $f(x)\geq0.46+2.84(x-1)+\tfrac12(x-1)^2$. At $x=-1$ the bound is $-3.22$, below $f(-1)\approx0.46$. [ajout]

## Cesse d'être valide quand
$f$ is only convex ($\mu=0$): the bound falls back to the tangent, and a small gap in value no longer forces a small distance — a flat-bottomed function has minimizers far apart. The inequality also needs $f$ differentiable at $\bar{x}$. [ajout]

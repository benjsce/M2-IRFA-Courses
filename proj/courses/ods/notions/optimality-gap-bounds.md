---
id: ods/optimality-gap-bounds
nom: Bounds on the optimality gap
type: notion
statut: source
construite_a_partir_de:
- ods/quadratic-upper-bound
- ods/first-order-optimality-condition
alias:
- optimality gap
- suboptimality bounds
refs:
- Prop. 2.5
---

## Ce que c'est
For an $L$-smooth function with a minimizer, the gap between $f(z)$ and the minimum is at least the squared gradient over $2L$ and at most $\tfrac L2$ times the squared distance to the minimizer. [Prop. 2.5]

## Forme
$$\frac1{2L}\|\nabla f(z)\|_*^2\ \leq\ f(z)-f(x^\star)\ \leq\ \frac L2\|z-x^\star\|^2\qquad\forall z\in\mathbb{R}^n$$ [Prop. 2.5]

## Ce que les symboles modélisent
$f(z)-f(x^\star)$ is the optimality gap: how much worse $z$ is than the best point. The left bound uses the gradient at $z$, which one can compute; the right one uses the distance to $x^\star$, which one does not know. [Prop. 2.5, ajout]

## Retrouver la formule
![The graph of f(x) = x² − cos x, its minimizer x* = 0 where f = −1, and the point z = 1. Three vertical bars start from the minimum: the gap itself, about 1.46; on its left the bound from the slope at z, about 1.35; on its right the bound from the distance to x*, 1.50.](figures/optimality-gap-bounds.svg) [ajout]

Known: at $z=1$, $f(x)=x^2-\cos x$ has slope $\approx2.84$, and $L=3$; the minimizer is $x^\star=0$, with $f(x^\star)=-1$. Sought: bounds on the gap $f(1)-f(0)\approx1.46$. [ajout]

Right side. Write the quadratic upper bound at $x^\star$: its gradient vanishes there, so the tangent is flat and $f(z)\leq f(x^\star)+\tfrac L2\|z-x^\star\|^2$. At $z=1$: gap $\leq1.5$. [Prop. 2.5]

Left side. The minimum is below every value of $f$, in particular below the lowest point of the parabola that sits above $f$ at $z$. That parabola, $f(z)+\langle\nabla f(z),y-z\rangle+\tfrac L2\|y-z\|^2$, is lowest at $y=z-\nabla f(z)/L$, where it equals $f(z)-\tfrac1{2L}\|\nabla f(z)\|_*^2$. At $z=1$: $0.46-2.84^2/6\approx-0.89$, above $-1$, so gap $\geq1.35$. [Prop. 2.5, ajout]

$$\frac1{2L}\|\nabla f(z)\|_*^2\ \leq\ f(z)-f(x^\star)\ \leq\ \frac L2\|z-x^\star\|^2$$ [Prop. 2.5]

## Ce qui la définit
Read from left to right: a point whose gap is small must have a small gradient, and a point close to the minimizer must have a small gap. Neither side needs convexity, only smoothness, a minimizer and a full domain. [Prop. 2.5, ajout]

## Le chemin jusqu'ici
ods/quadratic-upper-bound, which ods/l-smooth-function yields, supplies the parabola used on both sides; ods/first-order-optimality-condition gives the flat gradient at $x^\star$ that the right side needs. That condition was proved with ods/first-order-characterization and ods/local-minima-are-global, from ods/convex-function, whose ods/epigraph is an ods/convex-set; $x^\star$ is a minimizer in the sense of ods/optimization-problem. [ajout]

## Exemple minimal
For $f(x)=x^2-\cos x$ at $z=1$: the gap $1.46$ lies between $1.35$ and $1.50$. [ajout]

## Geste de calcul type
$f'(1)=2+\sin1\approx2.84$, so the left bound is $2.84^2/(2\times3)\approx1.35$; the right bound is $\tfrac32\times1^2=1.5$; the gap is $1-\cos1+1\approx1.46$. [ajout]

## Cesse d'être valide quand
$f$ has no minimizer — the gap is then undefined. The proof of the left side minimizes the parabola over all of $\mathbb{R}^n$: with a restricted domain, the best $y$ may be inadmissible. [Prop. 2.5, ajout]

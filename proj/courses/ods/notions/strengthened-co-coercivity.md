---
id: ods/strengthened-co-coercivity
nom: Strengthened co-coercivity
type: notion
statut: source
construite_a_partir_de:
- ods/co-coercivity
- ods/strongly-convex-function
alias:
- co-coercivity of a smooth strongly convex function
refs:
- Prop. 2.9
---

## Ce que c'est
When $f$ is both $L$-smooth and $\mu$-strongly convex, co-coercivity gains a term in the squared distance, and both terms share the weight $\mu+L$. [Prop. 2.9]

## Forme
$$\big\langle\nabla f(x)-\nabla f(y),x-y\big\rangle\ \geq\ \frac{\mu L}{\mu+L}\|x-y\|^2+\frac1{\mu+L}\|\nabla f(x)-\nabla f(y)\|^2$$ [Prop. 2.9]

## Ce que les symboles modélisent
The first term on the right comes from strong convexity and grows with the distance between the points; the second comes from smoothness and grows with the change of the gradient. Here $0<\mu\leq L$ and every norm is Euclidean. [Prop. 2.9]

## Retrouver la formule
Known: co-coercivity of a convex smooth function. Sought: what strong convexity adds. With $f(x)=x^2-\cos x$, $\mu=1$, $L=3$, $x=1$, $y=0$: the left side is $\approx2.84$. [ajout]

Remove the guaranteed curvature: $\phi(x)=f(x)-\tfrac\mu2\|x\|^2$ is convex, and its gradient $\nabla f(x)-\mu x$ rises along a segment by at most $(L-\mu)$ per unit, so $\phi$ is $(L-\mu)$-smooth. [Prop. 2.9]

If $L>\mu$, co-coercivity of $\phi$ gives $\langle\nabla\phi(x)-\nabla\phi(y),x-y\rangle\geq\tfrac1{L-\mu}\|\nabla\phi(x)-\nabla\phi(y)\|^2$. Replace $\nabla\phi$ by $\nabla f-\mu\,\mathrm{Id}$ and gather the terms. If $L=\mu$, $\phi$ is affine and the inequality holds with equality. On the example: $\tfrac34\times1+\tfrac14\times2.84^2\approx2.77\leq2.84$. [Prop. 2.9, ajout]

$$\big\langle\nabla f(x)-\nabla f(y),x-y\big\rangle\ \geq\ \frac{\mu L}{\mu+L}\|x-y\|^2+\frac1{\mu+L}\|\nabla f(x)-\nabla f(y)\|^2$$ [Prop. 2.9]

## Ce qui la définit
The inequality is stronger than each of its ingredients: with $\mu=0$ it falls back to co-coercivity, and it carries the two curvature bounds at once in a single statement about the gradient. [Prop. 2.9, ajout]

## Le chemin jusqu'ici
ods/co-coercivity, applied to $f$ minus its guaranteed curvature, does the work; ods/strongly-convex-function is what makes that difference convex. Co-coercivity itself comes from ods/optimality-gap-bounds, built on ods/quadratic-upper-bound and ods/l-smooth-function, with the flat gradient of ods/first-order-optimality-condition, proved from ods/first-order-characterization and ods/local-minima-are-global for an ods/convex-function, whose ods/epigraph is an ods/convex-set. Strong convexity also gives the minimizer, through ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact, in the sense of ods/optimization-problem. [ajout]

## Exemple minimal
For $f(x)=x^2-\cos x$, $\mu=1$, $L=3$, $x=1$, $y=0$: $2.84\geq0.75+2.02\approx2.77$. [ajout]

## Geste de calcul type
The weights are $\tfrac{\mu L}{\mu+L}=\tfrac34$ and $\tfrac1{\mu+L}=\tfrac14$; the squared distance is $1$ and the squared gradient change $2.84^2\approx8.07$: the right side is $0.75+2.02=2.77$, below the left side $2.84$. [ajout]

## Cesse d'être valide quand
The proof and the constants are Euclidean: for another norm, the step from $\phi$ back to $f$ does not hold as written. The function must have full domain. [Prop. 2.9]

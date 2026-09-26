---
id: ods/co-coercivity
nom: Co-coercivity of the gradient
type: notion
statut: source
construite_a_partir_de:
- ods/optimality-gap-bounds
alias:
- co-coercivity
- 1/L-co-coercive gradient
- Baillon–Haddad theorem
refs:
- Prop. 2.6
- Prop. 2.7
- §2.4.2
---

## Ce que c'est
For a convex $L$-smooth function, the gradient is $1/L$-co-coercive: along any segment, the gradient turns towards the displacement by at least the square of its change, divided by $L$. [Prop. 2.6]

## Forme
$$\big\langle\nabla f(x)-\nabla f(y),\,x-y\big\rangle\ \geq\ \frac1L\,\|\nabla f(x)-\nabla f(y)\|_*^2\qquad\forall x,y\in\mathbb{R}^n$$ [Prop. 2.6]

## Ce que les symboles modélisent
The left side measures how much the gradient change points in the direction of the displacement; it is nonnegative for a convex function. The right side is the squared size of that change. The inequality ties the two: a gradient cannot change a lot without pointing along the move. [Prop. 2.6, ajout]

## Retrouver la formule
Known: the gap bounds of an $L$-smooth function with a minimizer. Sought: an inequality between two gradients. With $f(x)=x^2-\cos x$, $L=3$, $x=1$, $y=0$: the gradients are $\approx2.84$ and $0$. [ajout]

Tilt $f$ so that $x$ becomes its minimizer: $f_x(z)=f(z)-\langle\nabla f(x),z\rangle$ is convex, $L$-smooth, and its gradient vanishes at $z=x$, so $x$ minimizes it. [Prop. 2.6]

The left gap bound at $y$ gives $f_x(y)-f_x(x)\geq\tfrac1{2L}\|\nabla f(y)-\nabla f(x)\|_*^2$, that is $f(y)-f(x)-\langle\nabla f(x),y-x\rangle\geq\tfrac1{2L}\|\nabla f(y)-\nabla f(x)\|_*^2$. [Prop. 2.6]

Do the same with the roles of $x$ and $y$ swapped, and add: the values cancel, and the two gradient terms combine. On the example: $2.84\times1\geq2.84^2/3\approx2.69$. [Prop. 2.6, ajout]

$$\big\langle\nabla f(x)-\nabla f(y),\,x-y\big\rangle\ \geq\ \frac1L\,\|\nabla f(x)-\nabla f(y)\|_*^2$$ [Prop. 2.6]

## Ce qui la définit
For a differentiable convex function on all of $\mathbb{R}^n$, three properties are equivalent: $f$ is $L$-smooth; the quadratic upper bound (2.6) holds; $\nabla f$ is $1/L$-co-coercive. The result is sometimes called the Baillon–Haddad theorem, whose original statement is much more general. [Prop. 2.7, §2.4.2]

## Le chemin jusqu'ici
ods/optimality-gap-bounds gives, on its left side, the lower bound that the tilted function $f_x$ satisfies at $y$; that bound comes from ods/quadratic-upper-bound, hence from ods/l-smooth-function, and uses the flat gradient of ods/first-order-optimality-condition. Convexity enters because $x$ must minimize $f_x$: that is what ods/first-order-characterization and ods/local-minima-are-global guarantee for a convex function, ods/convex-function, whose ods/epigraph is an ods/convex-set — a minimizer of ods/optimization-problem. [ajout]

## Exemple minimal
For $f(x)=x^2-\cos x$ with $x=1$, $y=0$: the left side is $2.84$, the right side $2.84^2/3\approx2.69$. [ajout]

## Geste de calcul type
Compute both sides: $\nabla f(1)-\nabla f(0)=2+\sin1-0\approx2.84$, times $1-0=1$, gives $2.84$; the square over $L=3$ gives $8.07/3\approx2.69\leq2.84$. [ajout]

## Cesse d'être valide quand
$f$ is not convex: $f(x)=-\tfrac12x^2$ is $1$-smooth, but $\langle-x+y,x-y\rangle=-(x-y)^2<0$, below the nonnegative right side. The equivalences of Proposition 2.7 need the full domain $\mathbb{R}^n$. [Prop. 2.7, ajout]

---
id: ods/first-order-characterization
nom: First-order characterization of convexity
symbole: '$\nabla f$, $\bar{x}$'
type: notion
statut: source
construite_a_partir_de:
- ods/convex-function
alias:
- above its tangents
- tangent inequality
refs:
- Prop. 2.2
- eq. 2.3
- Fig. 2.4
---

## Ce que c'est
A differentiable function is convex exactly when it lies above each of its tangents. [Prop. 2.2]

## Forme
$$\forall x,\bar{x}\in C,\qquad f(x)\geq f(\bar{x})+\big\langle\nabla f(\bar{x}),\,x-\bar{x}\big\rangle$$ [eq. 2.3]

## Ce que les symboles modélisent
$\nabla f$ takes a point and returns a vector, the gradient: the partial derivatives of $f$, pointing where $f$ increases fastest. $\bar{x}$ is the point where the tangent is drawn; the right-hand side is the tangent at $\bar{x}$, an affine function of $x$. $f$ is differentiable on an open set $\Omega$ that contains the convex set $C$. [Prop. 2.2, ajout]

## Retrouver la formule
![The graph of f(x) = x² − cos x and its tangent at x̄ = 1, where f ≈ 0.46 and the slope is about 2.84. The tangent stays under the whole graph, not only near x̄: at x = −1 it is 5.68 below it.](figures/first-order-characterization.svg) [Fig. 2.4, ajout]

Known: $f$ is convex, so its chords pass above its graph. Sought: a bound on $f$ everywhere from what happens at one point. At $\bar{x}=1$, $f(x)=x^2-\cos x$ has value $0.46$ and slope $2+\sin1\approx2.84$. [ajout]

Take the chord from $\bar{x}$ to another point $x$ and shrink it. Convexity with weight $\lambda$ on $x$ says $f\big(\bar{x}+\lambda(x-\bar{x})\big)-f(\bar{x})\leq\lambda\big(f(x)-f(\bar{x})\big)$: the rise over a small step is at most $\lambda$ times the total rise of the chord. [Prop. 2.2]

Divide by $\lambda$ and let $\lambda\to0$: the left side becomes the slope of $f$ at $\bar{x}$ in the direction of $x$, which is $\langle\nabla f(\bar{x}),x-\bar{x}\rangle$. The slope at the start of the chord is at most the average slope of the chord. At $x=-1$: the tangent predicts $0.46-2\times2.84\approx-5.22$, and $f(-1)\approx0.46$ is above it. [Prop. 2.2, ajout]

$$f(x)\geq f(\bar{x})+\big\langle\nabla f(\bar{x}),\,x-\bar{x}\big\rangle$$ [eq. 2.3]

## Ce qui la définit
The converse holds too. For $z=\alpha x+(1-\alpha)y$, write (2.3) at $\bar{x}=z$ once towards $x$ and once towards $y$, and combine the two lines with weights $\alpha$ and $1-\alpha$: the gradient terms cancel, and what remains is the chord inequality (2.1). [Prop. 2.2]

What this gives: local information — a value and a gradient at one point — yields a bound that holds on the whole domain. Strict convexity has the same characterization with a strict inequality for $x\neq\bar{x}$ (Exercise 3). [Prop. 2.2, Exercise 3]

## Le chemin jusqu'ici
ods/convex-function gives the chord inequality, and the tangent inequality is its limit when the chord shrinks to a point. That chord inequality is the convexity of the ods/epigraph, a region that is an ods/convex-set exactly when $f$ is convex. [ajout]

## Exemple minimal
At $\bar{x}=0$, the tangent of $f(x)=x^2-\cos x$ is the horizontal line at $-1$, and indeed $f(x)\geq-1$ everywhere. [ajout]

## Geste de calcul type
Tangent at $\bar{x}=1$: $f(1)\approx0.46$, $f'(1)=2+\sin1\approx2.84$, so $T(x)=0.46+2.84(x-1)$. At $x=-1$: $T(-1)\approx-5.22\leq f(-1)\approx0.46$. [ajout]

## Cesse d'être valide quand
$f$ is not differentiable, or $C$ is not convex: the characterization needs segments in $C$ and a gradient at every point. For a non-convex $f$ the inequality fails: the tangent of $\cos$ at $0$ is the horizontal line at $1$, which lies above the graph everywhere else. [Prop. 2.2, ajout]

## Origine
- exercise ods/ex-03: the limit that proves the tangent inequality loses strictness; the strict version goes through the midpoint [Exercise 3, ajout]

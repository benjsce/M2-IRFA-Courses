---
id: ods/convex-function
nom: Convex function
symbole: '$\operatorname{dom} f$, $\operatorname{Conv}\mathbb{R}^p$'
type: notion
statut: source
construite_a_partir_de:
- ods/convex-set
- ods/epigraph
alias:
- convexity
refs:
- Def. 2.3
- eq. 2.1
- §2.2.1
---

## Ce que c'est
A function is convex when its epigraph is a convex set: the chord between two points of its graph never passes below the graph. [Def. 2.3, §2.2.1]

## Forme
$$\forall x,y\in\operatorname{dom} f,\ \ \forall\lambda\in[0,1],\qquad f\big(\lambda x+(1-\lambda)y\big)\leq\lambda f(x)+(1-\lambda)f(y)$$ [eq. 2.1]

## Ce que les symboles modélisent
$\operatorname{dom} f$ is the set of points where $f$ is finite; the inequality is only asked there. On the left, $f$ is evaluated at a point of the segment; on the right, the same mix is applied to the two values, which is the height of the chord. [eq. 2.1, ajout]

$\operatorname{Conv}\mathbb{R}^p$ denotes the set of convex functions on $\mathbb{R}^p$, and the same symbol with a bar the closed ones, whose epigraph is closed; the convention is that of Hiriart-Urruty and Lemaréchal. [§2.2.1]

## Retrouver la formule
![The graph of f(x) = x² − cos x between x = −1 and y = 2, with the chord joining its two points. At the midpoint, the chord is at about 2.44, the average of 0.46 and 4.42; the graph is far lower, at about −0.63.](figures/convex-function.svg) [ajout]

Take $f(x)=x^2-\cos x$ and the two points $x=-1$, $y=2$ of its graph: $\big(-1,\,0.46\big)$ and $\big(2,\,4.42\big)$, heights rounded. Both belong to the epigraph, since each lies on the graph. [ajout]

If the epigraph is convex, so is every mix of the two points: the midpoint $\big(0.5,\ \tfrac12\cdot0.46+\tfrac12\cdot4.42\big)=\big(0.5,\,2.44\big)$ belongs to it, which says $f(0.5)\leq2.44$. It holds: $f(0.5)\approx-0.63$. [Def. 2.3, ajout]

In general, mixing $(x,f(x))$ and $(y,f(y))$ with weights $\lambda$ and $1-\lambda$ gives the point $\big(\lambda x+(1-\lambda)y,\ \lambda f(x)+(1-\lambda)f(y)\big)$, and belonging to the epigraph means lying on or above the graph at that abscissa. [§2.2.1]

$$f\big(\lambda x+(1-\lambda)y\big)\leq\lambda f(x)+(1-\lambda)f(y)$$ [eq. 2.1]

## Ce qui la définit
Many problems of statistics and machine learning are not convex; convexity is studied because it describes the generic behaviour of an optimization procedure, and the local picture of many non-convex problems. [§2]

Adding the two inequalities written with the same $x$, $y$ and $\lambda$ shows that a sum of convex functions is convex. [ajout]

## Le chemin jusqu'ici
ods/epigraph turns the function into a set, the region above its graph; ods/convex-set says what it means for that region to be convex. The inequality (2.1) is nothing but the segment condition written for two points of the graph. [§2.2.1]

## Exemple minimal
For $f(x)=x^2-\cos x$, midway between $-1$ and $2$ the graph is at $-0.63$ and the chord at $2.44$. [ajout]

## Geste de calcul type
Convexity of the penalized least squares $\tfrac12\|Ax-b\|^2+\tfrac12\|x\|^2$: each term is a squared norm composed with an affine map, which is convex, and the sum of two convex functions is convex. [ajout]

## Cesse d'être valide quand
One pair $x,y$ and one $\lambda$ that violate (2.1) are enough to break convexity: for $\cos$ with $x=-\pi$, $y=\pi$ and $\lambda=\tfrac12$, the chord is at $-1$ and the graph at $\cos0=1$, above it. Convexity alone guarantees neither a minimizer ($e^x$ has none) nor a unique one (a constant has infinitely many). [§2, ajout]

---
id: ods/epigraph
nom: Epigraph
symbole: '$\operatorname{epi} f$'
type: notion
statut: source
alias:
- epi f
refs:
- Def. 2.2
- Fig. 2.3
---

## Ce que c'est
The epigraph of a function is the set of points lying on or above its graph. [Def. 2.2]

## Forme
$$\operatorname{epi} f=\big\{(x,t)\in\mathbb{R}^n\times\mathbb{R}\ :\ t\geq f(x)\big\}$$ [Def. 2.2]

## Ce que les symboles modélisent
$\operatorname{epi} f$ lives in one more dimension than the domain of $f$: a point $(x,t)$ belongs to it when the height $t$ is at least $f(x)$. The function may take the values $\pm\infty$ but is not identically $+\infty$; above a point where $f=+\infty$ there is nothing. [Def. 2.2]

## Ce qui la définit
![Two epigraphs, shaded. On the left, a function with a bump in the middle: the segment between two points of the epigraph passes under the bump, so the epigraph is not a convex set. On the right, f(x) = x² − cos x: every segment between two points of the shaded region stays in it.](figures/epigraph.svg) [Fig. 2.3, ajout]

The epigraph turns a question about a function into a question about a set: the shape of $f$ becomes the shape of $\operatorname{epi} f$. This is how the notes define a convex function. [§2.2.1]

## Exemple minimal
For $f(x)=x^2-\cos x$, the point $(0,0)$ is in the epigraph, since $0\geq f(0)=-1$; the point $(1,0)$ is not, since $f(1)\approx0.46$. [ajout]

## Geste de calcul type
To test whether $(x,t)$ belongs to $\operatorname{epi} f$, compute $f(x)$ and compare it with $t$. For $(2,4)$: $f(2)=4-\cos2\approx4.42>4$, so the point lies below the graph and is not in the epigraph. [ajout]

## Cesse d'être valide quand
For $f\equiv+\infty$ the epigraph is empty, which is why the definition excludes that function. [Def. 2.2]

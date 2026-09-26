---
id: ods/quadratic-upper-bound
nom: Quadratic upper bound
type: notion
statut: source
construite_a_partir_de:
- ods/l-smooth-function
alias:
- descent lemma
refs:
- Prop. 2.4
- eq. 2.5
- eq. 2.6
- §2.4.1
---

## Ce que c'est
An $L$-smooth function lies below each of its tangents plus the parabola $\tfrac L2\|y-x\|^2$: its graph is trapped under a parabola of curvature $L$ that touches it at any point we choose. [Prop. 2.4]

## Forme
$$f(y)\leq f(x)+\big\langle\nabla f(x),y-x\big\rangle+\frac L2\|y-x\|^2\qquad\forall x,y\in\operatorname{dom}f$$ [eq. 2.6]

## Ce que les symboles modélisent
$x$ is the point where the parabola touches $f$, $y$ any other point. The inequality (2.5), $\langle\nabla f(x)-\nabla f(y),x-y\rangle\leq L\|x-y\|^2$, says the same thing on the gradient: along a segment, the slope cannot rise faster than $L$. [eq. 2.5, eq. 2.6]

## Retrouver la formule
Known: along any segment, the slope of $f$ rises by at most $L$ per unit of distance. Sought: how high $f$ can climb. With $f(x)=x^2-\cos x$, $L=3$, from $x=1$ to $y=0$: $f(1)\approx0.46$, slope $\approx2.84$. [ajout]

Follow the segment: $g(t)=f\big(x+t(y-x)\big)$, so that $g(0)=f(x)$ and $g(1)=f(y)$. By (2.5), the slope $g'(t)$ exceeds the initial slope $g'(0)=\langle\nabla f(x),y-x\rangle$ by at most $tL\|y-x\|^2$. [Prop. 2.4]

Integrate from $0$ to $1$: $f(y)=g(0)+\int_0^1g'(t)\,dt\leq g(0)+g'(0)+\tfrac L2\|y-x\|^2$. On the example: $f(0)\leq0.46-2.84+1.5\approx-0.88$, and indeed $f(0)=-1$. [Prop. 2.4, ajout]

$$f(y)\leq f(x)+\big\langle\nabla f(x),y-x\big\rangle+\frac L2\|y-x\|^2$$ [eq. 2.6]

## Ce qui la définit
$L$-smoothness implies (2.5) by the Cauchy–Schwarz inequality. When the domain is convex, (2.5) and (2.6) are equivalent: conversely, writing (2.6) from $x$ to $y$ and from $y$ to $x$ and adding makes the values cancel and leaves (2.5). [Prop. 2.4]

The bound says how much $f$ can go up at most, hence how far one can step without risk: this is why smoothness matters in optimization. [§2.4.1]

## Le chemin jusqu'ici
ods/l-smooth-function bounds how fast the gradient changes; integrating that bound along a segment turns it into a bound on the values of $f$. [Prop. 2.4]

## Exemple minimal
For $f(x)=x^2-\cos x$, with $L=3$, from $x=1$: $f(y)\leq0.46+2.84(y-1)+1.5(y-1)^2$ for every $y$. [ajout]

## Geste de calcul type
At $y=0$: the bound is $0.46-2.84+1.5\approx-0.88$, above $f(0)=-1$. At $y=2$: $0.46+2.84+1.5=4.80$, above $f(2)\approx4.42$. [ajout]

## Cesse d'être valide quand
The domain is not convex: the segment from $x$ to $y$ may leave it, and (2.5) no longer gives (2.6). A constant smaller than the true $L$ makes the bound false. [Prop. 2.4, ajout]

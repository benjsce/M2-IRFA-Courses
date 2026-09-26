---
id: ods/existence-under-coercivity
nom: Existence of a minimizer for a coercive function
type: notion
statut: source
construite_a_partir_de:
- ods/existence-on-a-compact
- ods/coercive-function
alias:
- C0 + coercive ⇒ global minimizer
refs:
- Th. 1.2
---

## Ce que c'est
A continuous and coercive function on the whole of $\mathbb{R}^d$ reaches its infimum: it has at least one global minimizer, although no compact domain was given. [Th. 1.2]

## Forme
$$f:\mathbb{R}^d\to\mathbb{R}\ \text{continuous and coercive}\ \Longrightarrow\ \exists\,x^\star\in\mathbb{R}^d,\ \ \forall x\in\mathbb{R}^d,\ f(x)\geq f(x^\star)$$ [Th. 1.2]

## Ce que les symboles modélisent
$x^\star$ is sought in all of $\mathbb{R}^d$: the problem is unconstrained, and the bounded region that the compact theorem needs is not given but built from the growth of $f$. [Th. 1.2, ajout]

## Retrouver la formule
![The least-squares loss of the four observations. The dashed circle has radius M ≈ 2.41: outside it, the loss exceeds its value at the origin, f(0) = 1, so no point out there can be the best. The solid curve is the set where f equals 1; it passes through the origin and surrounds the minimizer x* = (0, 1), well inside the disk.](figures/existence-under-coercivity.svg) [ajout]

Known: on a closed and bounded set, a continuous function has a minimizer. Sought: a minimizer on the whole plane, which is not bounded. Take the four observations of the course, with loss $f(x)=\tfrac12\|Ax-b\|^2$; at the origin, $f(0)=\tfrac12\|b\|^2=1$. [Th. 1.2, ajout]

Coercivity gives a radius beyond which $f$ exceeds that value. Here, every vector is stretched by $A$ by a factor at least $c\approx1.176$, so $\|Ax-b\|\geq c\|x\|-\|b\|$, and $f(x)>1$ as soon as $\|x\|>2\sqrt2/c\approx2.41$: this is the dashed circle. [Ex. 1.1, ajout]

Inside, the closed disk of radius $M$ is compact, and the compact theorem gives a point $x^\star$ of the disk with $f(x^\star)\leq f(y)$ for every $y$ of the disk, in particular $f(x^\star)\leq f(0)=1$. [Th. 1.2]

Outside, every point has $f>1\geq f(x^\star)$. The point $x^\star$ therefore beats the whole plane, not only the disk. [Th. 1.2]

$$\forall x\in\mathbb{R}^d,\quad f(x)\geq f(x^\star)$$ [Th. 1.2]

## Ce qui la définit
The theorem trades the compact domain for a compact region made by $f$ itself: the points where $f$ does not exceed $f(0)$ lie in a ball. The notes add that continuity can be weakened to lower semicontinuity, and that both existence theorems extend, under extra hypotheses, to infinite-dimensional Hilbert spaces. [p. 5]

## Le chemin jusqu'ici
ods/coercive-function provides the radius beyond which $f$ exceeds $f(0)$, which is what makes a bounded search region; ods/existence-on-a-compact then finds a minimizer inside that ball, and the comparison with $f(0)$ carries it to the whole space. The distinction between the infimum and a point reaching it, which this theorem settles for unconstrained problems, is the one ods/optimization-problem makes. [ajout]

## Exemple minimal
$f(x)=x^2-\cos x$ is continuous and coercive on $\mathbb{R}$: it has a global minimizer, $x^\star=0$. [ajout]

## Geste de calcul type
Check continuity, then coercivity by a lower bound. For $\tfrac12\|Ax-b\|^2$ with $\operatorname{Ker}A=\{0\}$: $\|Ax-b\|\geq c\|x\|-\|b\|\to+\infty$, so a least-squares minimizer exists. [Ex. 1.1]

## Cesse d'être valide quand
$f$ is not coercive. The conclusion can still hold — a least-squares loss with a nonzero kernel has minimizers, but a whole unbounded set of them — or fail: the logistic loss of separable data is continuous and bounded below by $0$, yet has no minimizer, since scaling up a separating $w$ drives it to $0$ without reaching it (notebook 5, rerun here on the iris data). The theorem also says nothing about uniqueness. [Ex. 1.1, nb. 5, ajout]

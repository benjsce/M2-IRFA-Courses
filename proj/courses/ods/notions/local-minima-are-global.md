---
id: ods/local-minima-are-global
nom: Local minima of a convex function are global
type: notion
statut: source
construite_a_partir_de:
- ods/convex-function
- ods/optimization-problem
alias:
- local solution
- global solution
refs:
- Th. 2.1
- §2.2.2
---

## Ce que c'est
For a convex function on a closed convex set, every local minimizer is a global one, and the global minimizers form a convex set. [Th. 2.1]

## Forme
$$f\ \text{convex},\ C\ \text{convex and closed}:\qquad x^\star\ \text{local solution of}\ \min_{x\in C}f(x)\ \Longrightarrow\ x^\star\ \text{global solution}$$ [Th. 2.1]

## Ce que les symboles modélisent
A local solution $x^\star$ beats the points of $C$ in some neighbourhood $\mathcal{O}$ of it: $f(x)\geq f(x^\star)$ for all $x\in C\cap\mathcal{O}$. A global solution beats every point of $C$. $C$ is the set of admissible points, here convex and closed. [§2.2.2]

## Retrouver la formule
![On the left, a non-convex function with two hollows: a point walking downhill from the right stops in the higher hollow, a local minimum that is not the global one. On the right, f(x) = x² − cos x has a single hollow, and the point walking downhill ends at the global minimum.](figures/local-minima-are-global.svg) [ajout]

Known: $x^\star$ beats every admissible point close to it. Sought: that it beats all of them. Suppose it does not: some $z\in C$ has $f(z)<f(x^\star)$. [Th. 2.1]

With numbers: say $f(x)=x^2-\cos x$ had a local minimum at $x^\star=1$, where $f\approx0.46$, while $z=0$ gives $f(0)=-1$. The chord from $\big(1,\,0.46\big)$ to $\big(0,\,-1\big)$ is below $0.46$ as soon as it leaves $x^\star$: at $0.99$ it is at $0.99\cdot0.46+0.01\cdot(-1)\approx0.445$. [ajout]

A convex function lies under its chords, so $f(0.99)\leq0.445<0.46$: a point as close to $x^\star$ as we like does better than $x^\star$, and $x^\star$ was not a local minimum. In general, the points $(1-t)x^\star+tz$ of the segment are admissible because $C$ is convex, and they tend to $x^\star$ as $t\downarrow0$. [Th. 2.1]

$$f\big((1-t)x^\star+tz\big)\leq(1-t)f(x^\star)+tf(z)<f(x^\star)\qquad\forall t\in(0,1]$$ [Th. 2.1]

## Ce qui la définit
The second half of the theorem: if $x^\star$ and $z$ are two global solutions, every point of the segment between them has the same value, $f(x^\star)$, so the set of global solutions is convex — a single point, a segment, a whole face, but never two separate pieces. [Th. 2.1]

## Le chemin jusqu'ici
ods/convex-function supplies the chord inequality on which the proof rests, and ods/convex-set makes the segment from $x^\star$ to $z$ admissible; the chord inequality is the convexity of the ods/epigraph read on two points of the graph. The words local and global solution refine the minimizer of ods/optimization-problem. [ajout]

## Exemple minimal
$f(x)=x^2-\cos x$ has a single local minimum, at $0$, and it is the global one. [ajout]

## Geste de calcul type
To certify a candidate as a global minimizer, check that $f$ and $C$ are convex and that no nearby admissible point does better. For the penalized least squares of the four observations, $C=\mathbb{R}^2$ is convex and closed and the objective is convex, so the point where a descent method stops is the global minimizer. [ajout]

## Cesse d'être valide quand
$f$ is not convex: $h(x)=(x^2-1)^2+0.3x$ has a local minimum near $0.96$, where $h\approx0.29$, and its global minimum near $-1.04$, where $h\approx-0.31$ — a descent started on the right is trapped. $C$ is not convex: on $[-2,-1]\cup[1,2]$, $f(x)=x^2+0.1x$ has a local minimum at $1$ that is not the global one, at $-1$. The theorem also assumes that a local solution exists; it does not produce one. [Th. 2.1, ajout]

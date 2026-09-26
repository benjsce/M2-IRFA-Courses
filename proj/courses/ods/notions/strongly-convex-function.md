---
id: ods/strongly-convex-function
nom: Strongly convex function
symbole: '$\mu$'
type: notion
statut: source
construite_a_partir_de:
- ods/convex-function
- ods/existence-under-coercivity
alias:
- μ-strongly convex function
- strong convexity
refs:
- Def. 2.4
- §2.3
- p. 10
---

## Ce que c'est
A function is $\mu$-strongly convex when it stays convex after subtracting the parabola $\tfrac\mu2\|x\|^2$: it curves upwards at least as much as that parabola, everywhere. [Def. 2.4, §2.3]

## Forme
$$f\big(\lambda x+(1-\lambda)y\big)\leq\lambda f(x)+(1-\lambda)f(y)-\tfrac12\mu\lambda(1-\lambda)\|x-y\|^2\qquad\forall x,y\in\operatorname{dom}f,\ \lambda\in[0,1]$$ [Def. 2.4]

## Ce que les symboles modélisent
$\mu>0$ is the modulus: the least curvature of $f$. The last term says that the chord is not merely above the graph but above it by a margin that grows with the square of the distance between the two points. For a twice differentiable $f$, it means that every eigenvalue of the Hessian is at least $\mu$, $\nabla^2f\succeq\mu\,\mathrm{Id}$. This $\mu$ has nothing to do with the expected returns of the portfolio example. [Def. 2.4, p. 10, ajout]

## Ce qui la définit
Equivalently, $x\mapsto f(x)-\tfrac\mu2\|x\|^2$ is convex; the norm is Euclidean. [§2.3]

A finite-valued strongly convex function on $\mathbb{R}^d$ has exactly one minimizer. Existence: $h=f-\tfrac\mu2\|x\|^2$ is convex, so it lies above an affine function, $h(x)\geq h(0)+\langle p,x\rangle$; hence $f(x)\geq f(0)+\langle p,x\rangle+\tfrac\mu2\|x\|^2\to+\infty$, $f$ is continuous and coercive, and a minimizer exists. Uniqueness: strong convexity makes the chord inequality strict, and two distinct minimizers would have a better point between them. [p. 9, p. 10]

## Le chemin jusqu'ici
ods/convex-function gives the chord inequality, which strong convexity sharpens by a quadratic margin; that inequality is the convexity of the ods/epigraph as an ods/convex-set. The existence of the minimizer comes from ods/existence-under-coercivity: the margin makes $f$ coercive, which confines the search to a ball, as ods/coercive-function says, where ods/existence-on-a-compact applies — the minimizer of ods/optimization-problem is then reached. [p. 10, ajout]

## Exemple minimal
$f(x)=x^2-\cos x$ is $1$-strongly convex, since $f''(x)=2+\cos x\geq1$; its unique minimizer is $0$. [ajout]

## Geste de calcul type
Compute the smallest eigenvalue of the Hessian. For the penalized least squares of the four observations, the Hessian is $A^\top A+I=\begin{pmatrix}4&1\\1&3\end{pmatrix}$, whose eigenvalues are $\tfrac{7\pm\sqrt5}2$: $\mu=\tfrac{7-\sqrt5}2\approx2.38$. [p. 10, ajout]

## Cesse d'être valide quand
$f$ may take the value $+\infty$: strong convexity alone then does not give a minimizer — $f(x)=x^2$ on $x>0$, $+\infty$ elsewhere, has infimum $0$ and no minimizer; a proper, lower semicontinuous $f$ is needed. A convex function whose curvature vanishes somewhere, like $x^4$ at $0$, is not strongly convex. [p. 9, ajout]

## Origine
- exercise ods/ex-04: for a quadratic form, positive definiteness is strong convexity, with the smallest eigenvalue as modulus [slide 3, ajout]

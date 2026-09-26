---
id: ods/l-smooth-function
nom: L-smooth function
symbole: '$L$, $\|\cdot\|_*$'
type: notion
statut: source
alias:
- L-smoothness
- Lipschitz gradient
refs:
- Def. 2.5
- §2.4
- Prop. 2.8
---

## Ce que c'est
A differentiable function is $L$-smooth when its gradient never changes by more than $L$ times the distance travelled. [Def. 2.5]

## Forme
$$\|\nabla f(x)-\nabla f(y)\|_*\leq L\,\|x-y\|\qquad\forall x,y\in\operatorname{dom}f$$ [Def. 2.5]

## Ce que les symboles modélisent
$L>0$ bounds the curvature from above: for a twice differentiable convex function with full domain, it means that every eigenvalue of the Hessian is at most $L$. $\|\cdot\|_*$ is the dual norm, the one in which gradients are measured; for the Euclidean norm it is the Euclidean norm again. This $L$ is not a loss. [Def. 2.5, Prop. 2.8, ajout]

## Ce qui la définit
For a differentiable convex $f$ on $\mathbb{R}^n$, $L$-smooth for the Euclidean norm, three equivalent readings: $L\,\mathrm{Id}-\nabla f$ is monotone, $\langle\nabla f(x)-\nabla f(y),x-y\rangle\leq L\|x-y\|_2^2$; the function $\tfrac L2\|x\|_2^2-f(x)$ is convex; and, if $f$ is twice differentiable, $\lambda_{\max}\big(\nabla^2f(x)\big)\leq L$ everywhere. [Prop. 2.8]

It is the mirror of strong convexity: $\mu$ bounds the curvature from below, $L$ from above. [ajout]

## Exemple minimal
$f(x)=x^2-\cos x$ is $3$-smooth, since $f''(x)=2+\cos x\leq3$. [ajout]

## Geste de calcul type
Compute the largest eigenvalue of the Hessian. For the penalized least squares of the four observations, $A^\top A+I=\begin{pmatrix}4&1\\1&3\end{pmatrix}$ has eigenvalues $\tfrac{7\pm\sqrt5}2$: $L=\tfrac{7+\sqrt5}2\approx4.62$. [Prop. 2.8, ajout]

## Cesse d'être valide quand
The gradient changes without bound: $f(x)=x^4$ has $f''(x)=12x^2$, so it is $L$-smooth only on bounded sets. The Hessian criterion of Proposition 2.8 assumes a convex, twice differentiable function with full domain and the Euclidean norm. [Prop. 2.8, ajout]

---
id: ods/gradient-descent
nom: Gradient descent
type: notion
statut: source
construite_a_partir_de:
- ods/second-order-taylor-expansion
- ods/quadratic-upper-bound
alias:
- gradient step
refs:
- slide 4
- slide 24
---

## Ce que c'est
Move from the current point against the gradient by a step of $1/L$: it is what minimizing the second-order model does when the Hessian is replaced by $L$ times the identity. [slide 4]

## Forme
$$x^{k+1}=x^k-\frac1L\,\nabla f(x^k)$$ [slide 4, ajout]

## Ce que les symboles modélisent
$x^k$ is the point reached after $k$ steps. $\tfrac1L$ is the step size: the one that minimizes the parabola of curvature $L$ touching $f$ at $x^k$. [slide 4, ajout]

## Retrouver la formule
![At x = 1, the parabola of curvature L = 3 that touches f(x) = x² − cos x lies above the whole curve. Its bottom is at x ≈ 0.053, at height −0.89; the gradient step jumps there, and f at that point is even lower, −0.996.](figures/gradient-descent.svg) [ajout]

Known: at $x=1$, $f(x)=x^2-\cos x$ has value $0.46$ and slope $2.84$, and its curvature never exceeds $L=3$. Sought: where to go next. [ajout]

Take the second-order model and replace the Hessian by $L\,\mathrm{Id}$: $m(h)=f(x)+\nabla f(x)^\top h+\tfrac L2\|h\|^2$. Its gradient is $\nabla f(x)+Lh$, which vanishes at $h=-\nabla f(x)/L$. From $x=1$: $h=-2.84/3\approx-0.95$, and the new point is $0.053$. [slide 4, ajout]

This model is not only an approximation: by the quadratic upper bound it lies above $f$. So $f(x+h)\leq m(h)=f(x)-\tfrac1{2L}\|\nabla f(x)\|^2$: the step can only go down. Here $m\approx-0.89$ and $f(0.053)\approx-0.996$. [Prop. 2.4, ajout]

$$x^{k+1}=x^k-\frac1L\,\nabla f(x^k),\qquad f(x^{k+1})\leq f(x^k)-\frac1{2L}\|\nabla f(x^k)\|^2$$ [slide 4, ajout]

## Ce qui la définit
Each step costs one gradient and decreases $f$ by at least $\tfrac1{2L}\|\nabla f\|^2$. On a quadratic, the error in the $A$-norm shrinks at worst by the factor $\tfrac{\kappa-1}{\kappa+1}$ per step, where $\kappa$ is the ratio of the largest to the smallest curvature — the rate the slides compare with conjugate gradient. [slide 24]

## Le chemin jusqu'ici
ods/second-order-taylor-expansion provides the local quadratic model; ods/quadratic-upper-bound, which comes from ods/l-smooth-function, guarantees that the model with curvature $L$ stays above $f$, so jumping to its bottom never goes up. [ajout]

## Exemple minimal
On $f(x)=x^2-\cos x$ with $L=3$, one step from $x=1$ lands at $0.053$, and $f$ goes from $0.46$ to $-0.996$. [ajout]

## Geste de calcul type
Penalized least squares of the four observations, from $w=0$: the gradient is $(A^\top A+I)\cdot0-A^\top b=-(1,2)$ and $L\approx4.62$, so the first step goes to $(1,2)/4.62\approx(0.22,\,0.43)$, still far from the minimizer $(0.09,\,0.64)$. [ajout]

## Cesse d'être valide quand
A step larger than $2/L$ can make $f$ increase and the iterates diverge; $L$ must be known or estimated. When the curvatures differ a lot — $\kappa$ large — the iterates zigzag across a narrow valley and progress slowly. [slide 24, ajout]

## Origine
- exercise ods/ex-05: the step 1/L is the minimizer of the quadratic model whose Hessian is L I [slide 4]

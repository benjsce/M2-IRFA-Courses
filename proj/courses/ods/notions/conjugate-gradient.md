---
id: ods/conjugate-gradient
nom: Conjugate gradient
symbole: '$g^k$, $d^k$, $\alpha_k$, $\beta_k$'
type: notion
statut: source
construite_a_partir_de:
- ods/matrix-free-product
alias:
- CG
- conjugate gradient method
- scipy.sparse.linalg.cg
refs:
- slide 14
- slide 16
- slide 17
- slide 31
---

## Ce que c'est
An iterative solver for $Ax=b$ with $A\succ0$ that asks for one product with $A$ per iteration and keeps a single previous direction in memory. [slide 14]

## Forme
$$g^k=Ax^k-b,\quad d^k=g^k+\alpha_kd^{k-1},\quad\alpha_k=-\frac{\langle g^k,Ad^{k-1}\rangle}{\langle Ad^{k-1},d^{k-1}\rangle},\quad\beta_k=\frac{\langle g^k,d^k\rangle}{\langle Ad^k,d^k\rangle},\quad x^{k+1}=x^k-\beta_kd^k$$ [slide 16, slide 17]

## Ce que les symboles modélisent
$g^k$ is the gradient of $q(x)=\tfrac12x^\top Ax-b^\top x$ at the current point $x^k$, which is also the residual of the system. $d^k$ is the search direction: the gradient, corrected by a multiple of the previous direction. $\alpha_k$ is that multiple, the direction coefficient; it is $0$ at the first iteration. $\beta_k$ is the step size, the one that minimizes $q$ along $d^k$. Beware that Nocedal and Wright use $\alpha_k$ for the step and $\beta_k$ for the coefficient, the opposite of these slides. [slide 16, slide 27]

## Retrouver la formule
![The level lines of q for the matrix A with rows (4, 1) and (1, 3), and b = (1, 2). From w⁰ = 0, conjugate gradient goes to w¹ = (1/4, 1/2), then lands exactly on the minimizer w² = (1/11, 7/11). Gradient descent with step 1/L, from the same start, only approaches it in six steps.](figures/conjugate-gradient.svg) [ajout]

Known: products with $A=\begin{pmatrix}4&1\\1&3\end{pmatrix}$, the system of the four observations with $\lambda=1$, and $b=(1,2)$. Sought: $x^\star$. The wish of the slides: at each iteration, take the best step among all the gradients seen so far. [slide 14, ajout]

First iteration, from $x^0=0$: $g^0=-b=(-1,-2)$ and $d^0=g^0$. One product, $Ad^0=(-6,-7)$. The best step along $d^0$ minimizes $q(x^0-\beta d^0)$, a parabola in $\beta$: $\beta_0=\langle g^0,d^0\rangle/\langle Ad^0,d^0\rangle=5/20=\tfrac14$. So $x^1=(\tfrac14,\tfrac12)$ and $g^1=g^0-\beta_0Ad^0=(\tfrac12,-\tfrac14)$. [slide 17, ajout]

Second iteration. Going along $g^1$ alone would undo part of the first step; the correction $\alpha_1=-\langle g^1,Ad^0\rangle/\langle Ad^0,d^0\rangle=\tfrac1{16}$ makes the new direction $d^1=g^1+\tfrac1{16}d^0=(\tfrac7{16},-\tfrac38)$ conjugate to $d^0$. Then $\beta_1=\tfrac4{11}$ and $x^2=(\tfrac1{11},\tfrac7{11})$: the minimizer, in two iterations. [slide 16, ajout]

$$d^k=g^k+\alpha_kd^{k-1},\qquad x^{k+1}=x^k-\beta_kd^k$$ [slide 16, slide 17]

## Ce qui la définit
Minimizing over all the gathered gradients naively would require storing them and solving a least-squares problem of growing size at every iteration. Conjugate gradient does exactly that with a single vector of memory, $d^{k-1}$, and one product $q^k=Ad^k$, reused for $\beta_k$, for $g^{k+1}=g^k-\beta_kq^k$ and for $\alpha_{k+1}$: one product with $A$ and $\mathcal{O}(n)$ extra operations per iteration. [slide 14, slide 17]

It is implemented as `scipy.sparse.linalg.cg`, and scikit-learn's `Ridge` offers it as the solver `'sparse_cg'`; notebook 4 hands it a `LinearOperator` for $X^\top X+\lambda I$. [slide 31, nb. 4]

## Le chemin jusqu'ici
ods/matrix-free-product is the only thing the method asks for: a way to compute $Ax$, here $X^\top(Xw)+\lambda w$ at the cost of the non-zeros of an ods/sparse-matrix. The system it solves comes from ods/quadratic-form: minimizing $q$ and solving $Ax=b$ are the same task. [ajout]

That equivalence rests on ods/first-order-optimality-condition — from ods/first-order-characterization and ods/local-minima-are-global, for an ods/convex-function whose ods/epigraph is an ods/convex-set — and $A\succ0$ makes $q$ an ods/strongly-convex-function with a single minimizer, which exists by ods/existence-under-coercivity, via ods/coercive-function and ods/existence-on-a-compact, as for any ods/optimization-problem. [ajout]

## Exemple minimal
On $A=\begin{pmatrix}4&1\\1&3\end{pmatrix}$, $b=(1,2)$, from $0$: $x^1=(\tfrac14,\tfrac12)$, $x^2=(\tfrac1{11},\tfrac7{11})$, and $g^2=0$. [ajout]

## Geste de calcul type
One iteration: compute $q=Ad$ (the only product), then $\beta=\langle g,d\rangle/\langle d,q\rangle$, $x\leftarrow x-\beta d$, $g\leftarrow g-\beta q$, $\alpha=-\langle g,q\rangle/\langle d,q\rangle$, $d\leftarrow g+\alpha d$. Stop when $g=0$, or small. [slide 17]

## Cesse d'être valide quand
$A$ is not positive definite: $\langle Ad,d\rangle$ can vanish or be negative, and the step is meaningless. In floating point, conjugacy is slowly lost, so the exact termination is a property of exact arithmetic. For a non-quadratic $f$, $A$ is no longer available and the formulas must be rewritten. [slide 15, slide 27, ajout]

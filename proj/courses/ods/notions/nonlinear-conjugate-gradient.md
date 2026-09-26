---
id: ods/nonlinear-conjugate-gradient
nom: Nonlinear conjugate gradient
symbole: '$\varepsilon$'
type: notion
statut: source
construite_a_partir_de:
- ods/fletcher-reeves-formula
alias:
- conjugate gradient for a general smooth f
- fmin_cg
- line search
refs:
- slide 28
---

## Ce que c'est
Conjugate gradient for any smooth function: the gradient is recomputed at each point, the step is found by a line search, and the direction coefficient is that of Fletcher and Reeves. [slide 28]

## Forme
$$\beta_k\ \text{minimizes}\ \beta\mapsto f(x^k-\beta d^k),\quad x^{k+1}=x^k-\beta_kd^k,\quad g^{k+1}=\nabla f(x^{k+1}),\quad d^{k+1}=g^{k+1}+\frac{\|g^{k+1}\|^2}{\|g^k\|^2}\,d^k$$ [slide 28]

## Ce que les symboles modélisent
$\varepsilon$, a positive number, is the tolerance: the loop stops as soon as $\|g^k\|\leq\varepsilon$. The line search replaces the formula $\beta_k=\langle g^k,d^k\rangle/\langle Ad^k,d^k\rangle$, which needed $A$: it minimizes $f$ along the direction, a one-dimensional problem. Everything else only asks for values and gradients of $f$. [slide 28, ajout]

## Ce qui la définit
The algorithm starts from $g^0=\nabla f(x^0)$ and $d^0=g^0$, then loops: stop if $\|g^k\|\leq\varepsilon$; line search for $\beta_k$; step; new gradient; Fletcher–Reeves coefficient; new direction. On a quadratic with an exact line search, it is exactly the conjugate gradient of the linear system. [slide 28, ajout]

Finite termination is lost: $\nabla^2f$ is no longer constant, so there is no fixed $A$ for the directions to be conjugate to. [slide 28]

## Le chemin jusqu'ici
ods/fletcher-reeves-formula removed $A$ from the direction coefficient; the line search removes it from the step, and nothing of the matrix is left. The coefficient came from the orthogonality properties of ods/conjugate-directions, built by ods/conjugate-gradient with an ods/matrix-free-product on an ods/sparse-matrix to solve the system of an ods/quadratic-form. That system is the optimality condition of ods/first-order-optimality-condition, from ods/first-order-characterization and ods/local-minima-are-global for an ods/convex-function, whose ods/epigraph is an ods/convex-set; and its solution is unique for an ods/strongly-convex-function, which reaches its minimum by ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact — the question of ods/optimization-problem. [ajout]

## Exemple minimal
On the quadratic of the four observations, from $0$, with an exact line search: the same two steps as the linear method, $(\tfrac14,\tfrac12)$ then $(\tfrac1{11},\tfrac7{11})$. [ajout]

## Geste de calcul type
Line search on a quadratic, for checking: $\beta\mapsto q(x-\beta d)$ is a parabola in $\beta$, minimized at $\langle g,d\rangle/\langle Ad,d\rangle$; from $0$ along $d^0=(-1,-2)$ this is $5/20=\tfrac14$. For a general $f$, a numerical line search approximates this minimizer. [slide 17, slide 28, ajout]

## Cesse d'être valide quand
The function is not smooth, or the line search is too crude: the directions can then stop being descent directions and progress stalls — which is what the Polak–Ribière variant guards against. [slide 28]

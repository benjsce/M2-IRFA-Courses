---
id: ods/fletcher-reeves-formula
nom: Fletcher–Reeves formula
type: notion
statut: source
construite_a_partir_de:
- ods/conjugate-directions
alias:
- Fletcher-Reeves
refs:
- slide 27
---

## Ce que c'est
In conjugate gradient, the direction coefficient is only a ratio of squared gradient norms: the matrix $A$ disappears from it. [slide 27]

## Forme
$$\alpha_k=-\frac{\langle g^k,Ad^{k-1}\rangle}{\langle d^{k-1},Ad^{k-1}\rangle}=\frac{\|g^k\|^2}{\|g^{k-1}\|^2},\qquad\beta_k=\frac{\|g^k\|^2}{\langle d^k,Ad^k\rangle}$$ [slide 27]

## Ce que les symboles modélisent
$\alpha_k$ is the direction coefficient of conjugate gradient, $\beta_k$ its step; $g^k$ and $d^k$ are the gradient and the direction at iteration $k$. On the right, $\alpha_k$ needs only two gradients; $\beta_k$ still needs a product with $A$. [slide 27]

## Retrouver la formule
Known: three facts from conjugate gradient — $g^k=g^{k-1}-\beta_{k-1}Ad^{k-1}$, $\langle g^k,g^{k-1}\rangle=0$ and $\langle g^k,d^k\rangle=\|g^k\|^2$. Sought: $\alpha_k$ without $A$. On the four observations: $g^0=(-1,-2)$, $g^1=(\tfrac12,-\tfrac14)$, and conjugate gradient found $\alpha_1=\tfrac1{16}$. [slide 27, ajout]

The update gives $Ad^{k-1}=(g^{k-1}-g^k)/\beta_{k-1}$. In the numerator: $\langle g^k,Ad^{k-1}\rangle=\big(\langle g^k,g^{k-1}\rangle-\|g^k\|^2\big)/\beta_{k-1}=-\|g^k\|^2/\beta_{k-1}$, by orthogonality. [slide 27, ajout]

In the denominator: $\langle d^{k-1},Ad^{k-1}\rangle=\langle d^{k-1},g^{k-1}-g^k\rangle/\beta_{k-1}=\|g^{k-1}\|^2/\beta_{k-1}$, since $\langle g^k,d^{k-1}\rangle=0$ and $\langle g^{k-1},d^{k-1}\rangle=\|g^{k-1}\|^2$. The $\beta_{k-1}$ cancel. On the example: $\|g^1\|^2/\|g^0\|^2=\tfrac{5/16}{5}=\tfrac1{16}$, the same value. [slide 27, ajout]

$$\alpha_k=\frac{\|g^k\|^2}{\|g^{k-1}\|^2}$$ [slide 27]

## Ce qui la définit
Once $A$ has left the direction coefficient, only the step $\beta_k$ still involves it. Replace the step by a line search, and the recursion applies to any smooth $f$: that is the way from linear to nonlinear conjugate gradient. [slide 27]

## Le chemin jusqu'ici
ods/conjugate-directions provides the orthogonality of successive gradients and the identity $\langle g^k,d^k\rangle=\|g^k\|^2$, which are what let $A$ cancel. They are properties of ods/conjugate-gradient, a solver that only asks for an ods/matrix-free-product — cheap for an ods/sparse-matrix — to solve the system of ods/quadratic-form. That system is the optimality condition, ods/first-order-optimality-condition, derived from ods/first-order-characterization and ods/local-minima-are-global for an ods/convex-function, whose ods/epigraph is an ods/convex-set; it has one solution because $q$ is an ods/strongly-convex-function, which by ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact has a minimizer, as ods/optimization-problem asks. [ajout]

## Exemple minimal
For the system of the four observations, $\alpha_1=\|g^1\|^2/\|g^0\|^2=\tfrac{5/16}{5}=\tfrac1{16}$. [ajout]

## Geste de calcul type
$\|g^1\|^2=\tfrac14+\tfrac1{16}=\tfrac5{16}$ and $\|g^0\|^2=1+4=5$: $\alpha_1=\tfrac1{16}$. The step, $\beta_1=\|g^1\|^2/\langle d^1,Ad^1\rangle=\tfrac{5/16}{55/64}=\tfrac4{11}$, still uses $A$. [slide 27, ajout]

## Cesse d'être valide quand
The identity relies on the exact orthogonality of successive gradients, true for a quadratic with exact steps. For a general $f$ with an inexact line search, the two expressions of $\alpha_k$ differ, and the choice between them matters. [slide 27, slide 28, ajout]

## Origine
- exercise ods/ex-11: the derivation also needs ⟨gᵏ, dᵏ⁻¹⟩ = 0, a fact the hint does not list [slide 27, ajout]

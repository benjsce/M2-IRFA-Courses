---
id: ods/polak-ribiere
nom: Polak–Ribière formula
type: notion
statut: source
construite_a_partir_de:
- ods/nonlinear-conjugate-gradient
alias:
- Polak-Ribiere
- Polak–Ribière restart
refs:
- slide 28
---

## Ce que c'est
A variant of the direction coefficient that equals Fletcher–Reeves on a quadratic but restarts on its own when progress stalls. [slide 28]

## Forme
$$\alpha_{k+1}=\frac{\langle g^{k+1},\,g^{k+1}-g^k\rangle}{\|g^k\|^2}$$ [slide 28]

## Ce que les symboles modélisent
$g^{k+1}-g^k$ is how much the gradient has changed over the last step. The coefficient measures that change along the new gradient, instead of the new gradient's size alone. [slide 28, ajout]

## Ce qui la définit
On a quadratic with exact steps, successive gradients are orthogonal, $\langle g^{k+1},g^k\rangle=0$, and the formula gives back Fletcher–Reeves. Elsewhere it is more robust: if progress stalls, $g^{k+1}\approx g^k$, so $\alpha_{k+1}\approx0$ and the next direction is just the gradient — a gradient descent step, a restart that clears the stale direction. [slide 28]

It is the formula used by `scipy.optimize.fmin_cg`, the solver of notebook 5. [slide 28, nb. 5]

## Le chemin jusqu'ici
ods/nonlinear-conjugate-gradient runs with the coefficient of ods/fletcher-reeves-formula, which this formula replaces. That coefficient came from the orthogonality of ods/conjugate-directions in ods/conjugate-gradient, a solver of the system of an ods/quadratic-form that needs only an ods/matrix-free-product, cheap on an ods/sparse-matrix. The system is the vanishing gradient of ods/first-order-optimality-condition, obtained from ods/first-order-characterization and ods/local-minima-are-global for an ods/convex-function, an ods/epigraph that is an ods/convex-set; its solution is the unique minimizer of an ods/strongly-convex-function, which exists by ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact, as ods/optimization-problem asks. [ajout]

## Exemple minimal
On the system of the four observations: $\langle g^1,g^1-g^0\rangle/\|g^0\|^2=\big(\tfrac5{16}-0\big)/5=\tfrac1{16}$, the Fletcher–Reeves value, since $\langle g^1,g^0\rangle=0$. [ajout]

## Geste de calcul type
If a step barely moves, say $g^k=(0.50,-0.25)$ and $g^{k+1}=(0.49,-0.25)$, Fletcher–Reeves gives $\alpha=0.3026/0.3125\approx0.97$ and keeps the old direction, while Polak–Ribière gives $\big(0.49\times(-0.01)+0\big)/0.3125\approx-0.016$, almost $0$: a restart. [ajout]

## Cesse d'être valide quand
The coefficient can become negative; implementations often clip it at $0$. Like every nonlinear conjugate gradient, it gives no finite termination and needs a reasonable line search. [slide 28, ajout]

---
id: ods/logistic-regression
nom: Logistic regression
type: notion
statut: source
cas_de: ods/optimization-problem
construite_a_partir_de:
- ods/empirical-risk
alias:
- logistic loss
refs:
- nb. 5
---

## Ce que c'est
To classify with labels $\pm1$, choose the weights that minimize the logistic loss of the margins $y_i x_i^\top w$, a smooth loss that is no longer quadratic. [nb. 5]

## Forme
$$f(w)=\sum_{i=1}^{n}\log\big(1+e^{-y_ix_i^\top w}\big),\qquad\nabla f(w)=-\sum_{i=1}^{n}\frac{y_i\,x_i}{1+e^{\,y_ix_i^\top w}}$$ [nb. 5]

## Ce que les symboles modélisent
$y_i\in\{-1,+1\}$ is the label of example $i$ and $x_i$ its features, with a last entry equal to $1$ that carries the intercept. The margin $y_ix_i^\top w$ is positive when the sign of the score $x_i^\top w$ matches the label. Each term of $f$ is the loss of one example: close to $0$ for a large positive margin, close to the margin's absolute value for a large negative one. $\nabla f(w)$ is what the solver is given alongside $f$. [nb. 5, ajout]

## Ce qui la définit
![The loss of one example as a function of its margin, log(1 + e^(−m)). It decreases towards 0 without ever reaching it. Doubling w doubles every margin: margins 1, 2, 4 have losses 0.31, 0.13, 0.02.](figures/logistic-regression.svg) [ajout]

It is empirical risk minimization with the logistic loss and linear rules. Unlike least squares, setting the gradient to zero gives no linear system: the minimizer has no closed form, and an iterative method for a general smooth function is needed. Notebook 5 uses `scipy.optimize.fmin_cg`, given $f$ and its gradient. [nb. 5, ajout]

## Le chemin jusqu'ici
ods/empirical-risk supplies the objective: an average — here a sum — of a loss over the training pairs, a computable stand-in for the ods/expected-risk. The problem is one more instance of ods/optimization-problem, whose unknown is the weight vector. [ajout]

## Exemple minimal
Notebook 5 keeps the 100 iris flowers of two species, setosa labelled $-1$ and versicolor $+1$, described by sepal length, sepal width and a constant $1$. [nb. 5]

## Geste de calcul type
At $w=0$ every margin is $0$ and every loss is $\log2$: $f(0)=100\log2\approx69.3$, and the gradient is $-\tfrac12\sum_iy_ix_i$. Rerun here with SciPy 1.11, `fmin_cg` from $0$ stops after 23 iterations with $f\approx4.5\times10^{-6}$ and all 100 flowers on the right side. [nb. 5, ajout]

## Cesse d'être valide quand
The data are linearly separable — as these 100 flowers are, on the two sepal measurements: a separating $w$ can be scaled up forever, every margin grows, and $f$ goes to $0$ without reaching it. The infimum is $0$ and there is no minimizer; $f$ is not coercive. The solver stops only because its gradient tolerance is met, here at $\|w\|\approx275$. A penalty $\tfrac\lambda2\|w\|^2$ would restore a minimizer — the question the notebook ends on. [nb. 5, ajout]

## Origine
- exercise ods/ex-13: on separable data the unpenalized loss has no minimizer, and the solver's answer depends only on its tolerance [nb. 5, ajout]

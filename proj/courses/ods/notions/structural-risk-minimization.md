---
id: ods/structural-risk-minimization
nom: Structural risk minimization
symbole: '$J$, $\lambda$'
type: notion
statut: source
cas_de: ods/optimization-problem
construite_a_partir_de:
- ods/empirical-risk
alias:
- regularized empirical risk
- SRM
refs:
- p. 3
---

## Ce que c'est
Minimize the empirical risk plus a penalty that encodes a prior on the prediction rule, the two being weighed by a hyperparameter. [p. 3]

## Forme
$$\inf_{\phi\in\mathcal{F}}\ \hat{\mathcal{R}}(\phi)+\lambda\,J(\phi)$$ [p. 3]

## Ce que les symboles modélisent
$J$ takes a prediction rule and returns a number that is large for the rules we distrust a priori; for linear rules, $J(w)=\tfrac12\|w\|^2$ penalizes large weights. [p. 3, ajout]

$\lambda>0$ is the exchange rate between fit and prior: as $\lambda\to0$ the problem goes back to empirical risk minimization, and as $\lambda$ grows the penalty dominates and pulls the rule towards the minimizer of $J$. [p. 3, ajout]

## Ce qui la définit
The term goes back to Vapnik and Chervonenkis (1974). The problem is still an optimization problem over the class $\mathcal{F}$; only the objective has changed. [p. 2, p. 3]

Scaling matters: multiplying the objective by $n$ gives $\sum_i\ell+n\lambda J$. The slides write ridge regression without the $\tfrac1n$, so their $\lambda$ is $n$ times this one. [slide 5, ajout]

## Le chemin jusqu'ici
ods/empirical-risk supplies the fit term, the only computable one; ods/expected-risk explains why the fit alone is not the goal, since the target is the loss on the whole population. The penalty is the new ingredient, and the result is again an instance of ods/optimization-problem. [p. 3, ajout]

## Exemple minimal
On the four observations, with the squared loss, $J(x)=\tfrac12\|x\|^2$ and $\lambda=\tfrac14$, four times the objective is $\tfrac12\|Ax-b\|^2+\tfrac12\|x\|^2$. [ajout]

## Geste de calcul type
Compare two weight vectors on $\tfrac12\|Ax-b\|^2+\tfrac12\|x\|^2$. At $(0,1)$: the fit costs $0$ and the penalty $\tfrac12$, total $0.5$. At $(0,\tfrac12)$: the residuals are $(\tfrac12,0,0,\tfrac12)$, the fit costs $\tfrac14$ and the penalty $\tfrac18$, total $0.375$. Smaller weights win, although they fit worse. [ajout]

## Cesse d'être valide quand
The notes do not say how to choose $\lambda$, nor $J$; a prior that does not match the data biases the result. The slides later compute the solutions over a whole grid of $\lambda$, the regularization path. [p. 3, slide 29]

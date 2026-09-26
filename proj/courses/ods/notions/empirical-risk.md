---
id: ods/empirical-risk
nom: Empirical risk
symbole: '$\hat{\mathcal{R}}(\phi)$'
type: notion
statut: source
construite_a_partir_de:
- ods/expected-risk
alias:
- empirical risk minimization
- ERM
- training error
refs:
- §1.1.3
- p. 2
---

## Ce que c'est
The average loss of a prediction rule on the $n$ training pairs: the computable stand-in for the expected risk, whose distribution is unknown. [p. 2]

## Forme
$$\hat{\mathcal{R}}(\phi)=\frac1n\sum_{i=1}^{n}\ell\big(y_i,\phi(x_i)\big)$$ [p. 2]

## Ce que les symboles modélisent
$\hat{\mathcal{R}}(\phi)$ carries a hat because it is estimated from the sample: the pairs $(x_i,y_i)$, $i=1,\dots,n$, replace the whole population. [p. 2]

## Ce qui la définit
Known: the $n$ pairs and the loss. Sought: the rule of the class that minimizes the empirical risk. With the squared loss $\tfrac12(y-x^\top w)^2$ and linear rules, $n\,\hat{\mathcal{R}}$ is exactly the least-squares loss $\tfrac12\|Ax-b\|^2$: least squares is empirical risk minimization. [p. 2, §1.1.2, ajout]

## Le chemin jusqu'ici
ods/expected-risk is what we would like to minimize, but it needs the unknown distribution; averaging the same loss over the sample makes it computable. The unknown is still a function and the problem still has the form of ods/optimization-problem. [p. 2]

## Exemple minimal
On the four observations, with the squared loss, the weights $(0,1)$ have an empirical risk of $0$: they reproduce the four targets exactly. [ajout]

## Geste de calcul type
The weights $(\tfrac12,\tfrac12)$ predict $1,\tfrac12,\tfrac12,\tfrac12$ for the targets $1,0,0,1$; the halved squared errors are $0,\tfrac18,\tfrac18,\tfrac18$, and their average is $\hat{\mathcal{R}}=\tfrac{3}{32}\approx0.094$. [ajout]

## Cesse d'être valide quand
A small empirical risk proves nothing about the expected risk: on four points, the weights $(0,1)$ reach $0$, and a noisy future sample would still cost them. This is why the notes add a regularization term, in structural risk minimization. [p. 2, p. 3, ajout]

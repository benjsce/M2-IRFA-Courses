---
id: ods/intercept
nom: Intercept
symbole: '$\bar{y}$, $\overline{X}$, $\hat{w}$, $\hat{b}$'
type: notion
statut: source
construite_a_partir_de:
- ods/ridge-regression
alias:
- bias
- centering the data
- intercept scaling
refs:
- slide 6
- nb. 1
- nb. 2
- nb. 4
---

## Ce que c'est
Once the weights are known, the best unpenalized intercept is the mean of the targets minus the mean of the features weighted by those weights. [slide 6]

## Forme
$$\hat{b}=\bar{y}-\overline{X}^\top\hat{w}$$ [slide 6]

## Ce que les symboles modélisent
$\bar{y}$, a number, is the mean of the targets, and $\overline{X}$, a vector of $\mathbb{R}^p$, is the vector of the means of the columns of $X$. $\hat{w}$ and $\hat{b}$ are the fitted weights and intercept. The formula says that the fitted line passes through the point of means. [slide 6, ajout]

## Retrouver la formule
Known: the ridge objective, whose intercept $b$ is not penalized. Sought: the best $b$ for given weights. On the four observations, the means are $\overline{X}=(\tfrac34,\tfrac12)$ and $\bar{y}=\tfrac12$. [slide 6, ajout]

Only the fit term depends on $b$, through the residual $y-Xw-b\mathbf{1}_n$. Its derivative in $b$ is $-\mathbf{1}_n^\top(y-Xw-b\mathbf{1}_n)$: it vanishes when the residuals sum to zero, that is when $n\bar{y}-n\overline{X}^\top w-nb=0$. [slide 6, ajout]

So $b=\bar{y}-\overline{X}^\top w$. Put back in the objective, it replaces $y$ and $X$ by their centered versions, and the weights solve ridge without intercept on centered data. On the example: $\hat{w}=(-\tfrac2{13},\tfrac6{13})$, then $\hat{b}=\tfrac12-\big(\tfrac34\cdot(-\tfrac2{13})+\tfrac12\cdot\tfrac6{13}\big)=\tfrac5{13}\approx0.38$. [slide 6, ajout]

$$\hat{b}=\bar{y}-\overline{X}^\top\hat{w}$$ [slide 6]

## Ce qui la définit
The slides give two ways to deal with the intercept. Option 1, for dense data: center $y$ and every column of $X$, solve ridge without intercept, and recover $\hat{b}$ by the formula. Option 2, for sparse data: add a column of ones to $X$, and do not penalize it, or not too much. [slide 6, nb. 2]

Centering is not an option for sparse data, since subtracting the column means fills in all the zeros. Notebook 4 therefore adds a column equal to 100 and lets ridge penalize its coefficient: the intercept is $100$ times that coefficient, and its penalty is divided by $100^2$, so it is almost free. [nb. 4, ajout]

## Le chemin jusqu'ici
ods/ridge-regression penalizes $w$ but not $b$, which is what makes the intercept separable. Behind it: the penalized shape of ods/structural-risk-minimization, built on ods/empirical-risk and ods/expected-risk; the linear system of ods/quadratic-form, obtained from ods/first-order-optimality-condition, itself proved with ods/first-order-characterization and ods/local-minima-are-global for an ods/convex-function, whose ods/epigraph is an ods/convex-set; and the unique minimizer that the ods/strongly-convex-function brings, through ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact — all instances of ods/optimization-problem. [ajout]

## Exemple minimal
On the four observations with $\lambda=1$ and an unpenalized intercept: $\hat{w}=(-\tfrac2{13},\tfrac6{13})$ and $\hat{b}=\tfrac5{13}\approx0.38$. [ajout]

## Geste de calcul type
With the intercept-scaling trick of notebook 4 — a column equal to $100$, penalized like the others — the same data give $\hat{w}\approx(-0.1538,\,0.4616)$ and an intercept $\approx0.3846$: the exact answer to three decimals. [nb. 4, ajout]

## Cesse d'être valide quand
The intercept is penalized like the other weights: the formula no longer holds, and the fit depends on where the origin of $y$ is. Notebook 5 raises the question for logistic regression, where the column of ones is added but the objective carries no penalty at all. [slide 6, nb. 5, ajout]

## Origine
- exercise ods/ex-06: the formula follows from setting the derivative in b to zero, and holds only because b is not penalized [slide 6, ajout]
- exercise ods/ex-13: the same rule carries over to logistic regression, where the notebook's question only makes sense once a penalty is added [nb. 5, ajout]

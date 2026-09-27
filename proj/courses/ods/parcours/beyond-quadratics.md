---
id: ods/parcours-beyond-quadratics
ordre: 6
titre: When the loss is no longer quadratic
source: slides 27 and 28, notebook 5
---

## Point de départ
One hundred iris flowers of two species, setosa and versicolor, each described by its sepal length and width. We label them $-1$ and $+1$ and look for weights whose linear score has the sign of the label. How do we find them? [nb. 5]

## À savoir avant
- ods/empirical-risk : the objective is again an average of a loss over the training pairs; only the loss changes. [p. 2]
- ods/conjugate-directions : the orthogonality of successive gradients, proved for the linear method, is what lets the matrix disappear from the formulas. [slide 16]

## Étapes
1. ods/logistic-regression
   What should be minimized to make the score agree with the label? [nb. 5]
   Histoire : « whose linear score has the sign of the label » — With $x_i$ the two measurements of flower $i$ and a constant $1$ for the intercept, and $y_i$ its label, the logistic loss of the margins $y_ix_i^\top w$: small when the score has the sign of the label, large otherwise. At $w=0$ it is $100\log2\approx69.3$. [ajout]

2. ods/fletcher-reeves-formula
   Can the matrix be taken out of conjugate gradient? [slide 27]
   Suite : This loss is not quadratic: setting its gradient to zero gives no linear system, and conjugate gradient used the matrix in its direction coefficient and in its step. [ajout]
   Histoire : « in its direction coefficient » — From the direction coefficient, yes: $\alpha_k=\|g^k\|^2/\|g^{k-1}\|^2$, a ratio of gradient norms — $\tfrac1{16}$ on the four observations, as in the previous story. [ajout]

3. ods/nonlinear-conjugate-gradient
   And from the step? [slide 28]
   Histoire : « and in its step » — On the flowers no matrix gives the step: from the current weights, $\beta_k$ is found by trying steps along the direction and keeping the one that lowers the logistic loss most, and the gradient is recomputed at the new weights. Values and gradients of the loss are then enough — but with three weights, the method no longer surely stops after three iterations. [ajout]

4. ods/polak-ribiere
   Which coefficient does the solver of the notebook use, and what does it do on the flowers? [slide 28, nb. 5]
   Histoire : « How do we find them » — SciPy's `fmin_cg` uses $\alpha_{k+1}=\langle g^{k+1},g^{k+1}-g^k\rangle/\|g^k\|^2$, which restarts when progress stalls. Rerun here, it stops after 23 iterations with the loss at $4.5\times10^{-6}$ and every flower on the right side — but at $\|w\|\approx275$: the flowers are separable, the loss has no minimizer, and only the gradient tolerance stopped the loop. [ajout]

## Point d'arrivée
Conjugate gradient extends to smooth losses once the matrix is removed from its formulas. On the iris flowers it separates the two species in 23 iterations, but the unpenalized logistic loss has no minimizer: a penalty, as in ridge regression, would give it one. [ajout]

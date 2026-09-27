---
id: ods/parcours-too-big
ordre: 4
titre: When the data no longer fits
source: slides 3 to 13, notebooks 1 to 4
---

## Point de départ
The same penalized least squares, now on a real problem: $n=100\,000$ observations and $p=1\,000\,000$ features, stored in a matrix whose rows each hold ten non-zero entries. The best weights solve a linear system. Can we write it down and solve it? [slide 12]

## À savoir avant
- ods/first-order-optimality-condition : it is what makes the best weights the solution of a linear system — the gradient of a quadratic objective vanishes on a linear equation. [p. 9]
- ods/strongly-convex-function : the penalty makes the objective strongly convex, so the system has exactly one solution. [Def. 2.4]
- ods/structural-risk-minimization : ridge regression is its instance with the squared loss and the penalty $\tfrac12\|w\|^2$; the question here is only how to compute it. [p. 3]

## Étapes
1. ods/quadratic-form
   Before the size, the shape: what kind of problem is it? [slide 3]
   Histoire : « The best weights solve a linear system » — The objective is a quadratic form, $q(x)=\tfrac12x^\top Ax-b^\top x+c$; its gradient $Ax-b$ vanishes where $Ax=b$, and $A\succ0$ makes that point the unique minimizer. On the four observations it is the $2\times2$ system that ended the second story, $A=\begin{pmatrix}4&1\\1&3\end{pmatrix}$ and $b=(1,2)$ — this $b$ is no longer the targets but the data applied to them: minimizing and solving are one task. [ajout]

2. ods/ridge-regression
   What is that matrix for our data, and what of the intercept that a real model needs? [slide 5]
   Histoire : « The same penalized least squares » — In the slides' notation — $X$ for the data, $y$ for the targets, $w$ for the weights and an intercept $b$ — the problem is ridge regression. Without intercept its system is $(X^\top X+\lambda I_p)w=X^\top y$, with a million unknowns. [ajout]

3. ods/intercept
   The intercept is not penalized: how is it dealt with? [slide 6]
   Histoire : « whose rows each hold ten non-zero entries » — Centering the data would give it by $\hat{b}=\bar{y}-\overline{X}^\top\hat{w}$, but subtracting the column means fills in every zero. With a sparse matrix one adds a column of ones instead, and barely penalizes its coefficient. [ajout]

4. ods/singular-value-decomposition
   Could a factorization of the data give the weights at once? [slide 8]
   Histoire : « Can we write it down and solve it » — With $M=U\Sigma V^\top$ for $M$ the data matrix, ridge shrinks each singular direction by $\sigma_i^2/(\sigma_i^2+\lambda)$, $\sigma_i$ being the singular values, and the weights are explicit. But computing the SVD of a $10^5\times10^6$ matrix is out of reach. [ajout]

5. ods/woodbury-identity
   The system is $p\times p$, but there are ten times fewer observations than features: can the inverse be moved to the smaller side? [slide 10]
   Histoire : « $n=100\,000$ observations and $p=1\,000\,000$ features » — The matrix inversion lemma rewrites $(A+UCV)^{-1}$ with a $k\times k$ inverse; with $A=\lambda I_p$, $U=X^\top$, $C=I_n$ and $V=X$, the $p\times p$ inverse becomes an $n\times n$ one. [ajout]

6. ods/dual-ridge
   What does the smaller system look like, and does it fit in memory? [slide 11]
   Histoire : « Can we write it down » — $\hat{w}=X^\top(XX^\top+\lambda I_n)^{-1}y$ needs an $n\times n$ matrix: 80 GB in float64. The primal $X^\top X$ would take 8 TB. Neither fits. [ajout]

7. ods/sparse-matrix
   Is the data itself too big? [slide 12]
   Histoire : « ten non-zero entries » — No: a million non-zeros, stored with their positions, take about 12 MB. The problem is not the data but the matrices built from it. [ajout]

8. ods/sparse-storage-format
   How should those non-zeros be laid out in memory to compute with them? [nb. 3]
   Histoire : « stored in a matrix whose rows each hold ten non-zero entries » — Row by row, since each row holds its ten non-zeros together: the CSR format keeps the million values, their million column indices, and the $100\,001$ positions where the rows start. The product $Xw$ then reads each row's ten entries once, about two million operations. [ajout]

9. ods/matrix-free-product
   If the matrix of the system cannot be stored, what can still be done with it? [slide 13]
   Histoire : « Can we write it down and solve it » — We cannot write it down, and we do not need to: $Aw=X^\top(Xw)+\lambda w$ costs about $4\times10^6$ operations — milliseconds — and a few vectors of memory. [ajout]

## Point d'arrivée
The ridge weights solve a system whose matrix, $10^6\times10^6$, cannot even be stored, while its product with a vector costs milliseconds. What is missing is a solver that asks for nothing but such products. [ajout]

---
id: ods/parcours-conjugate-gradient
ordre: 5
titre: A solver that only multiplies
source: slides 14 to 30, notebook 4
---

## Point de départ
The ridge system of the large problem has a million unknowns; its matrix is never formed, but each product with a vector costs about 4 million operations. On the four observations, the same system is $2\times2$: $A=\begin{pmatrix}4&1\\1&3\end{pmatrix}$ and $b=(1,2)$. How few products does it take to solve it? [slide 13, ajout]

## À savoir avant
- ods/matrix-free-product : it is the only operation the solver may use — a product with the matrix, never its entries. [slide 13]
- ods/quadratic-form : solving the system and minimizing the quadratic form are the same task; the solver works on the second to do the first, and the shape of its level sets sets the difficulty. [slide 3]
- ods/gradient-descent : it is the method to beat, the one that follows the slope with a fixed step. [slide 4]
- ods/singular-value-decomposition : the eigenvalues of $X^\top X$ are the squared singular values of $X$, which is how the penalty acts on the difficulty. [slide 9]
- ods/ridge-regression : its penalty $\lambda$ is added to every eigenvalue of the system; the grid of penalties at the end is a grid of ridge problems. [slide 5]

## Étapes
1. ods/conjugate-gradient
   Which method asks for nothing but products with the matrix, and keeps almost nothing in memory? [slide 14]
   Histoire : « How few products does it take » — One per iteration. From $x^0=0$, the gradient is $g^0=Ax^0-b=(-1,-2)$, the best step along it is $\beta_0=\tfrac14$, and $x^1=(\tfrac14,\tfrac12)$; then $\alpha_1=\tfrac1{16}$, $\beta_1=\tfrac4{11}$ and $x^2=(\tfrac1{11},\tfrac7{11})$ — the solution, after two products. [ajout]

2. ods/conjugate-directions
   Two products gave the exact solution. [slide 16]
   Suite : Gradient descent only approaches the solution. Why did two steps suffice here? [ajout]
   Histoire : « Why did two steps suffice here » — The two directions, $d^0=(-1,-2)$ and $d^1=(\tfrac7{16},-\tfrac38)$, are conjugate: $\langle d^1,Ad^0\rangle=0$. The second step does not undo what the first achieved. [ajout]

3. ods/cg-finite-termination
   The two directions are conjugate. [slide 15]
   Suite : Is two a coincidence of this small example? [ajout]
   Histoire : « Is two a coincidence of this small example » — No: the gradients stay pairwise orthogonal and nonzero until the end, and a plane holds at most two of them. With $n$ unknowns, at most $n$ iterations. [ajout]

4. ods/condition-number
   At most $n$ iterations, and for the large problem $n$ is a million. [slide 24]
   Suite : What decides the speed long before that? [ajout]
   Histoire : « What decides the speed long before that » — The shape of the level sets, measured by $\kappa=\lambda_{\max}(A)/\lambda_{\min}(A)$. On the four observations, $\kappa\approx1.94$: nearly round. [ajout]

5. ods/cg-convergence-rate
   $\kappa$ measures the shape of the level sets. [slide 24]
   Suite : How many iterations does a given $\kappa$ cost? [ajout]
   Histoire : « How many iterations does a given $\kappa$ cost » — The worst-case bounds give about $7.25\sqrt\kappa$ iterations to divide the error by a million, against $6.9\,\kappa$ for gradient descent: for $\kappa=10^4$, $730$ products instead of $69\,000$. [ajout]

6. ods/conditioning-of-ridge
   Fewer iterations need a smaller $\kappa$. [slide 26]
   Suite : What sets $\kappa$ for the ridge system? [ajout]
   Histoire : « What sets $\kappa$ for the ridge system » — The penalty: $\kappa=(\sigma_{\max}^2+\lambda)/(\sigma_{\min}^2+\lambda)$. With fewer observations than features, $\sigma_{\min}=0$ and $\kappa\approx\sigma_{\max}^2/\lambda$: the penalty is what makes the large system solvable in few products. [ajout]

7. ods/warm-start
   Each solve is iterative. [slide 29]
   Suite : In practice $\lambda$ is not known in advance: cross-validation needs the solution for a whole grid of values. Can one solve help the next? [ajout]
   Histoire : « Can one solve help the next » — Start each solve from the previous solution. Going from $\lambda=1$ to $\lambda=2$ on the four observations, the old solution $(\tfrac1{11},\tfrac7{11})$ is $0.16$ away from the new one, $(\tfrac2{19},\tfrac9{19})$, where the origin is $0.49$ away. [ajout]

8. ods/regularization-path
   Warm starts need an order. [slide 30]
   Suite : In which order should the grid be solved? [ajout]
   Histoire : « In which order should the grid be solved » — Start at the large end: at $\lambda=100$ the four observations give $\kappa\approx1.02$ and a solution, about $(0.01,0.02)$, so close to $0$ that starting from the origin costs almost nothing. Then go down the grid, each solution starting the next: $(\tfrac2{19},\tfrac9{19})$, found at $\lambda=2$, starts the solve at $\lambda=1$. [ajout]

## Point d'arrivée
Conjugate gradient solves the ridge system with one product per iteration and about $\sqrt\kappa$ iterations; the penalty sets $\kappa$, and a path over $\lambda$ is solved from the easy end with warm starts. [ajout]

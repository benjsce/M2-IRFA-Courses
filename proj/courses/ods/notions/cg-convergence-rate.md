---
id: ods/cg-convergence-rate
nom: Convergence rate of conjugate gradient
symbole: '$\|u\|_A$'
type: notion
statut: source
construite_a_partir_de:
- ods/cg-finite-termination
- ods/condition-number
- ods/gradient-descent
alias:
- √κ versus κ
- energy norm
refs:
- slide 24
- slide 25
---

## Ce que c'est
After $k$ iterations, the error of conjugate gradient has shrunk at least like a factor that depends on $\sqrt\kappa$, where gradient descent's depends on $\kappa$ itself. [slide 24]

## Forme
$$\|x^k-x^\star\|_A\leq2\left(\frac{\sqrt\kappa-1}{\sqrt\kappa+1}\right)^{k}\|x^0-x^\star\|_A\quad\text{(CG)},\qquad \|x^k-x^\star\|_A\leq\left(\frac{\kappa-1}{\kappa+1}\right)^{k}\|x^0-x^\star\|_A\quad\text{(gradient descent)}$$ [slide 24]

## Ce que les symboles modélisent
$\|u\|_A$, equal to $\sqrt{\langle u,Au\rangle}$, is the norm in which the error is measured, the one of the inner product of $A$; for $u=x-x^\star$, $\tfrac12\|u\|_A^2$ is exactly how far $q(x)$ is above its minimum. $\kappa$ is the condition number of $A$. The factor in parentheses is what each iteration keeps of the error, at worst. [slide 24, ajout]

## Ce qui la définit
![Iterations needed to divide the error by a million, against the condition number, both on logarithmic scales. Conjugate gradient follows √κ: about 70, 730 and 7 300 iterations for κ = 100, 10 000 and 1 000 000. Gradient descent follows κ: about 700, 69 000 and 6 900 000. The gap widens as the conditioning worsens.](figures/cg-convergence-rate.svg) [slide 25]

Reaching a precision $\varepsilon$ costs $\mathcal{O}(\sqrt\kappa\log(1/\varepsilon))$ iterations for conjugate gradient against $\mathcal{O}(\kappa\log(1/\varepsilon))$ for gradient descent. Conjugate gradient is not better by a constant factor: the gap widens as the problem gets worse conditioned. The rates are admitted in the slides, from Nocedal and Wright, chapter 5. [slide 24, slide 25]

## Le chemin jusqu'ici
ods/cg-finite-termination says conjugate gradient ends after $n$ steps, and this card says what it has achieved long before that; ods/condition-number measures the difficulty, and ods/gradient-descent, the step of ods/second-order-taylor-expansion made safe by ods/quadratic-upper-bound for an ods/l-smooth-function, is the method it is compared with. [ajout]

Behind the finite termination stand the ods/conjugate-directions of ods/conjugate-gradient, the ods/matrix-free-product it asks for, cheap on an ods/sparse-matrix, and the system of ods/quadratic-form. That system comes from ods/first-order-optimality-condition — built on ods/first-order-characterization and ods/local-minima-are-global for an ods/convex-function, an ods/epigraph that is an ods/convex-set — and has a unique solution because $q$ is an ods/strongly-convex-function, through ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact: the minimizer of ods/optimization-problem. [ajout]

## Exemple minimal
For $\kappa=10^4$, dividing the error by a million takes about $730$ iterations of conjugate gradient and $69\,000$ of gradient descent. [slide 25]

## Geste de calcul type
For conjugate gradient, $2r^k\leq10^{-6}$ with $r=\tfrac{\sqrt\kappa-1}{\sqrt\kappa+1}\approx1-\tfrac2{\sqrt\kappa}$ gives $k\approx\tfrac{\sqrt\kappa}2\ln(2\times10^6)\approx7.25\sqrt\kappa$: $\approx725$ for $\kappa=10^4$. For gradient descent, $k\approx\tfrac\kappa2\ln10^6\approx6.9\,\kappa$: $\approx69\,000$. On the four observations, $\kappa\approx1.94$: the factors per iteration are $0.16$ and $0.32$. [slide 25, ajout]

## Cesse d'être valide quand
These are worst-case bounds: a matrix whose eigenvalues are clustered is solved much faster than $\sqrt\kappa$ suggests. They also assume exact arithmetic, and a quadratic objective. [slide 25, ajout]

## Origine
- exercise ods/ex-10: the exact bounds give 72, 725 and 7 254 iterations for conjugate gradient, rounded on the slide to 70, 730 and 7 300 [slide 25, ajout]

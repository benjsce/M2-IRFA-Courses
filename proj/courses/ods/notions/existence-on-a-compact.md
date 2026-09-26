---
id: ods/existence-on-a-compact
nom: Existence of a minimizer on a compact set
symbole: '$f^\star$'
type: notion
statut: source
construite_a_partir_de:
- ods/optimization-problem
alias:
- C0 + compact ⇒ global minimizer
- extreme value theorem
refs:
- Th. 1.1
- §1.2
---

## Ce que c'est
A continuous function on a non-empty, closed and bounded subset of $\mathbb{R}^d$ reaches its infimum: the problem has at least one global minimizer. [Th. 1.1]

## Forme
$$f\ \text{continuous},\ \ \Omega\subset\mathbb{R}^d\ \text{non-empty and compact}\ \Longrightarrow\ \exists\,x^\star\in\Omega,\quad f(x^\star)=f^\star=\inf_{x\in\Omega}f(x)$$ [Th. 1.1]

## Ce que les symboles modélisent
$f^\star$ is the infimum of $f$ over $\Omega$: a number that exists before we know whether any point reaches it. The theorem says that one does, and calls it $x^\star$. [Th. 1.1]

## Retrouver la formule
![Three domains for the same question. On all of the real line, f(x) = x goes down forever: no minimum. On the open half-line x > 0, 1/x comes as close to 0 as we like but never reaches it: the minimizing points escape to infinity. On the closed and bounded interval from 1 to 3, the same 1/x has a lowest point, at x = 3.](figures/existence-on-a-compact.svg) [§1.2, ajout]

What is known is the number $f^\star$, the infimum; what is sought is a point where $f$ equals it. Take points $x^{(1)},x^{(2)},\dots$ of $\Omega$ whose values $f(x^{(t)})$ come down to $f^\star$: a minimizing sequence always exists, by the definition of an infimum. [Th. 1.1]

On the half-line of the figure, such points run off to infinity and converge to nothing. On a bounded set they cannot run away: the Bolzano–Weierstrass theorem extracts from them a subsequence that converges, to some point $x^\star$. [Th. 1.1]

The limit stays in $\Omega$ because $\Omega$ is closed; on the interval $(0,1]$, the points $1/t$ would converge to $0$, which is not in the domain. [Th. 1.1, ajout]

Finally, continuity carries the limit through $f$: the values along the subsequence tend to $f(x^\star)$ and to $f^\star$ at once, so they are equal. [Th. 1.1]

$$f(x^\star)=\lim_{t\to\infty}f\big(x^{(\varphi(t))}\big)=f^\star$$ [Th. 1.1]

## Ce qui la définit
Each hypothesis blocks one way of failing: boundedness keeps the minimizing points from escaping, closedness keeps their limit inside the domain, continuity keeps the value from jumping at the limit. The theorem gives existence only; it says nothing about uniqueness, nor about how to find the point. [Th. 1.1, ajout]

## Le chemin jusqu'ici
ods/optimization-problem separates the infimum, a number that always exists, from a minimizer, a point that may not; this theorem is the first condition under which the number is reached by a point. [ajout]

## Exemple minimal
On $[1,3]$ the function $1/x$ attains its minimum $1/3$ at $x=3$; on $x>0$ its infimum $0$ is never attained. [§1.2, ajout]

## Geste de calcul type
Check the hypotheses one by one. $f(x)=x^2-\cos x$ on $\Omega=[-1,2]$: $f$ is continuous, $\Omega$ is non-empty, closed and bounded, so a global minimizer exists; here it is $x^\star=0$, with $f^\star=-1$. [ajout]

## Cesse d'être valide quand
The domain is unbounded — and $\mathbb{R}^d$ itself is — or not closed, or $f$ is not continuous: the minimizing points may then escape or converge outside $\Omega$. For unconstrained problems on $\mathbb{R}^d$, the notes replace the compact domain by the coercivity of $f$. [§1.2]

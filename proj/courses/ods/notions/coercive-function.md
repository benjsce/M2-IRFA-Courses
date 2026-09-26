---
id: ods/coercive-function
nom: Coercive function
type: notion
statut: source
alias:
- coercivity
- 0-coercive function
refs:
- p. 4
---

## Ce que c'est
A function on $\mathbb{R}^d$ is coercive when it tends to $+\infty$ as the point moves away to infinity, in whatever direction. [p. 4]

## Forme
$$\lim_{\|x\|\to+\infty}f(x)=+\infty$$ [p. 4]

## Ce que les symboles modélisent
$\|x\|$ is the distance from the point to the origin. The limit is taken over every way of going far, not along one line: $f$ must blow up in all directions at once. [p. 4, ajout]

## Ce qui la définit
What coercivity is used for: given any level, for instance $f(0)$, there is a radius $M$ beyond which $f$ exceeds that level. Every point outside the ball of radius $M$ is then worse than the origin, and the search can be confined to the ball. [p. 5]

## Exemple minimal
$f(x)=x^2-\cos x$ is coercive, since $f(x)\geq x^2-1$; $f(x)=e^x$ is not, since it tends to $0$ when $x\to-\infty$. [ajout]

## Geste de calcul type
Bound $f$ from below by a function of $\|x\|$ alone that tends to $+\infty$. For $f(x)=x^2-\cos x$: $-\cos x\geq-1$, so $f(x)\geq x^2-1$, and $x^2-1\to+\infty$. [ajout]

## Cesse d'être valide quand
The least-squares loss $\tfrac12\|Ax-b\|^2$ is coercive only if the kernel of $A$ is $\{0\}$: along a nonzero vector of the kernel it stays constant, however far one goes. Coercivity also says nothing about what happens at finite distance: a coercive function may have several minimizers and several local minima. [Ex. 1.1, ajout]

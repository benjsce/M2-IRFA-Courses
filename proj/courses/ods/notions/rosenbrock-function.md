---
id: ods/rosenbrock-function
nom: Rosenbrock function
symbole: '$a$'
type: notion
statut: source
cas_de: ods/optimization-problem
alias:
- banana function
refs:
- §1.1.1
- Fig. 1.1
---

## Ce que c'est
A test function of two variables whose minimizer lies at the bottom of a long, narrow and curved valley, used to watch how an optimization algorithm behaves. [§1.1.1]

## Forme
$$f(x,y)=(1-x)^2+a\,(y-x^2)^2$$ [§1.1.1]

## Ce que les symboles modélisent
$a$ is the weight of the valley term: it sets how steep the walls around the parabola $y=x^2$ are, and its sign decides whether a minimizer exists at all. The typical value is $a=100$. [§1.1.1]

The two squares are two wishes that pull against each other: $(1-x)^2$ wants $x=1$, and $(y-x^2)^2$ wants the point to sit on the parabola $y=x^2$. [ajout]

## Ce qui la définit
Functions from $\mathbb{R}^2$ to $\mathbb{R}$ are the usual test bench because their contour lines can be drawn, and their geometry is already rich; the Rosenbrock valley is bent and flat along its floor, so a method that only looks at the steepest slope zigzags from wall to wall. [§1.1.1, Fig. 1.1, ajout]

## Exemple minimal
With $a=100$: $f(0,0)=1$ and $f(1,1)=0$, and the minimizer is $(1,1)$. [§1.1.1]

## Geste de calcul type
Check a candidate. At $(1,1)$ both squares vanish, so $f(1,1)=0$; when $a\geq0$, $f$ is a sum of nonnegative terms, so $0$ is the minimum; when $a>0$, both squares vanish only if $x=1$ and $y=x^2=1$, so $(1,1)$ is the only minimizer. [§1.1.1, ajout]

## Ce qui reste libre
| $a$ | minimizers |
|---|---|
| $a>0$ | the single point $(1,1)$ |
| $a=0$ | every point $(1,y)$: a whole line |
| $a<0$ | none: $f$ is unbounded below |
[§1.1.1]

## Cesse d'être valide quand
"The minimizer is $(1,1)$" holds only for $a>0$. At $a=0$ the valley term disappears and every point of the line $x=1$ is a minimizer; for $a<0$, moving away from the parabola, along $x=1$ and $y\to\infty$, sends $f$ to $-\infty$. One parameter is enough to go from one answer to infinitely many and then to none. [§1.1.1, ajout]

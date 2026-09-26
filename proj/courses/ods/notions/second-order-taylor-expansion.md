---
id: ods/second-order-taylor-expansion
nom: Second-order Taylor expansion
symbole: '$\nabla^2 f(x)$, $h$'
type: notion
statut: source
alias:
- Taylor at order 2
- Hessian matrix
refs:
- slide 4
---

## Ce que c'est
Near a point, a twice differentiable function is close to a quadratic: its value, plus a gradient term, plus half a Hessian term. [slide 4]

## Forme
$$f(x+h)=f(x)+\nabla f(x)^\top h+\tfrac12\,h^\top\nabla^2f(x)\,h+o\big(\|h\|^2\big)\qquad\forall h\in\mathbb{R}^n$$ [slide 4]

## Ce que les symboles modélisent
$h$ is the displacement from $x$. $\nabla^2 f(x)$ is the Hessian matrix, $n\times n$: its entries are the second derivatives, and $h^\top\nabla^2f(x)h$ is the curvature of $f$ in the direction $h$. The gradient $\nabla f(x)\in\mathbb{R}^n$ gives the slope. The remainder $o(\|h\|^2)$ becomes negligible against $\|h\|^2$ when $h$ is small, and only then. [slide 4, ajout]

## Ce qui la définit
It gives a local quadratic model of $f$, the quadratic that the slides go on to minimize. The two curvature constants of the course are bounds on the Hessian that appears here: $\mu\,\mathrm{Id}\preceq\nabla^2f(x)\preceq L\,\mathrm{Id}$ when $f$ is $\mu$-strongly convex and $L$-smooth. [slide 4, p. 10, Prop. 2.8]

## Exemple minimal
For $f(x)=x^2-\cos x$ at $x=1$: $f(1+h)\approx0.46+2.84\,h+1.27\,h^2$. [ajout]

## Geste de calcul type
At $h=-0.1$ the model gives $0.46-0.284+0.0127\approx0.1883$, and $f(0.9)=0.81-\cos0.9\approx0.1884$. At $h=-1$ it gives $-1.11$ while $f(0)=-1$: far from the point, the remainder is no longer small. [ajout]

## Cesse d'être valide quand
The displacement is not small: the model is only local, and it is not a bound on either side. $f$ must be twice differentiable at $x$. [slide 4, ajout]

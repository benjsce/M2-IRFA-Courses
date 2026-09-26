---
id: ods/parcours-curvature
ordre: 3
titre: How curved is the bowl?
source: notes §2.3 to §2.4, slide 4
---

## Point de départ
The notes draw $f(x)=x^2-\cos x$. Its second derivative, $2+\cos x$, never leaves the interval from $1$ to $3$: the curve bends upwards everywhere, never less than a parabola of second derivative $1$, never more than one of second derivative $3$. What do these two numbers buy? [Fig. 2.4, ajout]

## À savoir avant
- ods/convex-function : the curve is convex, and strong convexity is the same chord inequality with a margin added. [Def. 2.3]
- ods/existence-under-coercivity : it will say that the curvature bounded below gives a minimizer, since it makes $f$ grow without bound. [Th. 1.2]
- ods/first-order-characterization : the tangent under the curve is the starting point of the lower bound; the curvature puts a parabola under the curve instead. [Prop. 2.2]
- ods/first-order-optimality-condition : at the minimizer the gradient vanishes, which is what turns the upper bound into a bound on the distance to the best value. [p. 9]

## Étapes
1. ods/strongly-convex-function
   What does a curvature bounded below say about $f$ as a whole? [§2.3]
   Histoire : « never less than a parabola of second derivative $1$ » — $f$ is $\mu$-strongly convex with $\mu=1$: $f(x)-\tfrac12x^2=\tfrac12x^2-\cos x$ is still convex. The margin makes $f$ coercive, so it has exactly one minimizer, $x^\star=0$, where $f=-1$. [ajout]

2. ods/quadratic-lower-bound
   Can that margin be used at a given point, and not only as a statement about the whole curve? [Prop. 2.3]
   Histoire : « What do these two numbers buy » — The first number buys a floor: $f$ lies above each tangent plus $\tfrac\mu2(x-\bar{x})^2$. At the minimizer, $f(x)\geq-1+\tfrac12x^2$, so a point whose value is within $0.02$ of the minimum lies within $0.2$ of $x^\star$. [ajout]

3. ods/l-smooth-function
   And what does the curvature bounded above say? [§2.4]
   Histoire : « never more than one of second derivative $3$ » — The slope $f'(x)=2x+\sin x$ never changes by more than $3$ times the distance travelled: $f$ is $L$-smooth with $L=3$. [ajout]

4. ods/quadratic-upper-bound
   Does it bound the values of $f$ too, not only its slope? [Prop. 2.4]
   Histoire : « What do these two numbers buy » — The second number buys a ceiling: from $x=1$, where $f=1-\cos1\approx0.46$ and the slope is $2+\sin1\approx2.84$, the curve stays below $0.46+2.84(y-1)+1.5(y-1)^2$. [ajout]

5. ods/optimality-gap-bounds
   Can floor and ceiling tell how far a point is from the best value, without knowing where the best point is? [Prop. 2.5]
   Histoire : « these two numbers » — At $z=1$ the gap to the minimum, $1.46$, lies between the bound given by the slope, $2.84^2/(2L)=2.84^2/6\approx1.35$, and the one given by the distance to $x^\star=0$, $\tfrac L2\times1^2=1.5$. [ajout]

6. ods/co-coercivity
   Does the upper curvature also constrain how the slope itself changes? [§2.4.2]
   Histoire : « never more than one of second derivative $3$ » — For a convex, $3$-smooth function, the slope rises along any move by at least the square of its change divided by $3$: between $0$ and $1$, $2.84\geq2.84^2/3\approx2.69$. [ajout]

7. ods/strengthened-co-coercivity
   And with both numbers at once? [Prop. 2.9]
   Histoire : « these two numbers » — They combine in one inequality, with weights $\tfrac{\mu L}{\mu+L}=\tfrac34$ and $\tfrac1{\mu+L}=\tfrac14$: $2.84\geq\tfrac34\times1+\tfrac14\times2.84^2\approx2.77$. [ajout]

8. ods/second-order-taylor-expansion
   How does a method turn these bounds into a step? [slide 4]
   Histoire : « the curve bends upwards everywhere » — Near $x=1$ the curve looks like the parabola $f(1)+f'(1)h+\tfrac12f''(1)h^2$, with $f''(1)=2+\cos1\approx2.54$. The true curvature varies from point to point, but never beyond $3$. [ajout]

9. ods/gradient-descent
   Which parabola can one trust enough to jump to its bottom? [slide 4]
   Histoire : « never more than one of second derivative $3$ » — The one of curvature $L=3$, which stays above the curve: its bottom is at $1-2.84/3\approx0.053$, and $f$ there is $-0.996$, below the parabola's bottom, $0.46-1.35\approx-0.89$. The step $x^{k+1}=x^k-\tfrac1L\nabla f(x^k)$ never goes up. [ajout]

## Point d'arrivée
The lower curvature $\mu=1$ turns a small gap in value into a small distance; the upper one, $L=3$, bounds the gap from above and fixes a safe step, $1/L$. From $x=1$, one step lands at $0.053$ — and the ratio $L/\mu$ will come back as the difficulty of the problem. [ajout]

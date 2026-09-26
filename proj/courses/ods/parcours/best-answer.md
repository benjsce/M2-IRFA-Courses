---
id: ods/parcours-best-answer
ordre: 1
titre: Is there a best answer?
source: notes §1 to §1.2
---

## Point de départ
We have four observations of two features, the rows $(1,1)$, $(1,0)$, $(1,0)$ and $(0,1)$, with targets $1$, $0$, $0$ and $1$. We want the weights that bring the predicted targets as close as possible to the observed ones. Is there a best choice of weights? [ajout]

## Étapes
1. ods/optimization-problem
   Before looking for the weights, we must say what "best" means, and among which candidates we look. [§1]
   Histoire : « Is there a best choice of weights » — Written as a problem, the candidates form the domain $\Omega=\mathbb{R}^2$, the distance to the targets is the objective $f$, and a best choice is a minimizer $x^\star$, a point where $f$ reaches its infimum. The infimum always exists; whether a point reaches it is the whole question. [ajout]

2. ods/rosenbrock-function
   Can we take it for granted that such a point exists, and that there is only one? [§1.1.1]
   Histoire : « Is there a best choice » — The standard test function of the notes says no: with $a>0$ it has one minimizer, $(1,1)$; with $a=0$ a whole line of them; with $a<0$ none at all. One parameter is enough to go from one answer to none, so the existence of our best weights has to be proved. [ajout]

3. ods/existence-on-a-compact
   What guarantees that the infimum is reached by some point? [§1.2]
   Histoire : « the weights » — A continuous objective on a closed and bounded set of weights always has a minimizer. But our weights may be any pair of real numbers: the plane is not bounded, and the theorem does not apply as it stands. [ajout]

4. ods/coercive-function
   Since the plane is not bounded, can the objective itself keep the search inside a bounded region? [p. 4]
   Histoire : « as close as possible to the observed ones » — If the distance to the targets grows without bound as the weights grow, then beyond some radius every choice is worse than the weights $(0,0)$, and only a disk is worth searching. [ajout]

5. ods/existence-under-coercivity
   Does such a region, made by the objective, do the work of a compact domain? [Th. 1.2]
   Histoire : « Is there a best choice of weights » — Yes: inside the disk the compact theorem finds a minimizer, and outside it every point is worse than the origin, so that minimizer beats the whole plane. It remains to check that our distance grows in this way. [ajout]

6. ods/ordinary-least-squares
   Does our distance to the targets grow in every direction, and what are the best weights? [§1.1.2, Ex. 1.1]
   Histoire : « as close as possible to the observed ones » — Measured by the sum of squared residuals, the distance is $\tfrac12\|Ax-b\|^2$, with $A$ the $4\times2$ matrix of the rows and $b=(1,0,0,1)$. Its two columns are independent, so the kernel of $A$ is $\{0\}$, the loss is coercive, and the best choice exists and is unique: $x^\star=(A^\top A)^{-1}A^\top b=(0,1)$. The fit is exact, since $b$ is the second column of $A$. [ajout]

7. ods/expected-risk
   An exact fit answers the question we asked; is it the question we care about? [§1.1.3]
   Suite : On these four observations, the weights $(0,1)$ make no error at all. Will they predict a fifth observation as well? [ajout]
   Histoire : « Will they predict a fifth observation as well » — What matters is the average loss on all the observations the same process will produce: the expected risk. If the target were the second feature plus a noise of variance $0.1$, the weights $(0,1)$ would still lose $0.05$ on average, however exact their fit on four points. [ajout]

8. ods/empirical-risk
   The distribution that produces the future observations is unknown: what can we compute instead? [p. 2]
   Histoire : « four observations » — The average of the loss over the observations we have: the empirical risk. With the squared loss it is a quarter of $\tfrac12\|Ax-b\|^2$, so least squares was empirical risk minimization all along, and the weights $(0,1)$ bring it to $0$. [ajout]

9. ods/structural-risk-minimization
   An empirical risk of zero on four points may only mean that the weights learned the noise: how can a preference for small weights enter the problem? [p. 3]
   Histoire : « the weights » — Add to the empirical risk $\lambda$ times a penalty $J$; with $J(x)=\tfrac12\|x\|^2$ and $\lambda=\tfrac14$, four times the objective — four for the four observations averaged by the empirical risk — reads $\tfrac12\|Ax-b\|^2+\tfrac12\|x\|^2$. The exact fit $(0,1)$ now costs $0.5$, all of it penalty, and the smaller weights $(0,\tfrac12)$, which fit worse, score better, $0.375$. [ajout]

## Point d'arrivée
For the four observations a best choice exists — the weights $(0,1)$, an exact fit — because the least-squares loss is coercive. But learning asks for weights that predict, not only fit: the problem becomes the penalized $\tfrac12\|Ax-b\|^2+\tfrac12\|x\|^2$, whose minimizer the rest of the course finds. [ajout]

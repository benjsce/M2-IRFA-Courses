---
id: ods/parcours-convexity
ordre: 2
titre: Can a descent be trapped?
source: notes §2 to §2.2.3
---

## Point de départ
Our four observations now call for the penalized problem: minimize $\tfrac12\|Ax-b\|^2+\tfrac12\|x\|^2$ over the weights $x$ in the plane. A numerical method starts from $x=(0,0)$, walks downhill, and stops where no small step lowers the objective. Can it stop at a point that is not the best one? [ajout]

## À savoir avant
- ods/optimization-problem : it says what "the best one" is — a minimizer, a point where the objective reaches its infimum; convexity will show that the stopping point is such a point. [§1]

## Étapes
1. ods/convex-set
   Whether a stopping point can be a trap depends on the shape of the objective, and shape is first defined for sets. [§2]
   Histoire : « over the weights $x$ in the plane » — The plane of weights is convex: the segment between two admissible weights is admissible, so the method can always move straight from one candidate towards another. [ajout]

2. ods/operations-on-convex-sets
   Checking segments one by one is tedious: can a convex set be recognized from the way it is built? [Prop. 2.1]
   Histoire : « the weights » — The plane of weights is built, not checked: it is the product $\mathbb{R}\times\mathbb{R}$ of two intervals, hence convex, and the predictions $Ax$ that these weights produce, its image by an affine map, form a convex set of $\mathbb{R}^4$ as well. [ajout]

3. ods/epigraph
   How does a function, rather than a set, get a shape? [§2.2.1]
   Histoire : « walks downhill » — The epigraph of the objective is everything on or above its graph, a bowl standing over the plane of weights; the walk happens on the floor of that bowl. [ajout]

4. ods/convex-function
   When is that floor free of bumps? [Def. 2.3]
   Histoire : « the penalized problem » — When the epigraph is a convex set: every chord lies above the graph. Both terms of the objective are squared norms of affine maps, each convex, and their sum is convex too. [ajout]

5. ods/local-minima-are-global
   Does convexity answer our question about the stopping point? [Th. 2.1]
   Histoire : « Can it stop at a point that is not the best one » — No: for a convex function on a closed convex set, every local minimizer is global. A point where no small step lowers the objective is the best point. [ajout]

6. ods/first-order-characterization
   The chords need pairs of points, and the method only sees where it stands: can one point say something about all the others? [Prop. 2.2]
   Histoire : « walks downhill » — At its start, $x=(0,0)$, the method reads a value, $1$, and a slope, the gradient $(-1,-2)$. For a convex objective these two readings bound every other weight: the objective is at least $1-x_1-2x_2$ everywhere in the plane. [ajout]

7. ods/first-order-optimality-condition
   So where exactly does the walk stop? [p. 9]
   Histoire : « stops where no small step lowers the objective » — Where the gradient of the objective $f$ vanishes: $\nabla f(x^\star)=(A^\top A+I)x^\star-A^\top b=0$, that is $4x_1+x_2=1$ and $x_1+3x_2=2$. Its solution $x^\star=(\tfrac1{11},\tfrac7{11})$ is therefore the global minimizer. [ajout]

## Point d'arrivée
For a convex objective, stopping where the gradient vanishes is never a trap. For the four observations, the best penalized weights are $(\tfrac1{11},\tfrac7{11})$, the solution of a $2\times2$ linear system. [ajout]

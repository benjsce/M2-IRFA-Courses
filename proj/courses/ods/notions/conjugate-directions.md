---
id: ods/conjugate-directions
nom: Conjugate directions
symbole: '$\langle u, v\rangle_A$'
type: notion
statut: source
construite_a_partir_de:
- ods/conjugate-gradient
alias:
- A-conjugate directions
- A-orthogonal directions
refs:
- slide 16
- slide 23
---

## Ce que c'est
Two directions are conjugate with respect to $A$ when they are perpendicular for the inner product that $A$ defines; the directions built by conjugate gradient are all pairwise conjugate. [slide 16]

## Forme
$$\forall\,l<k:\qquad \langle d^k,Ad^l\rangle=0,\qquad \langle g^k,g^l\rangle=0$$ [slide 16, slide 22]

## Ce que les symboles modélisent
$\langle u, v\rangle_A$ stands for $\langle u,Av\rangle$: an inner product, well defined because $A\succ0$. Being conjugate means $\langle d^k, d^l\rangle_A=0$. The gradients, on the other hand, are orthogonal for the usual inner product. [slide 16, slide 23]

## Ce qui la définit
![On the left, the two steps of conjugate gradient on the ellipses of q: they are not perpendicular. On the right, the same picture in the coordinates z = A^(1/2)w, where the ellipses become circles: the two steps meet at a right angle.](figures/conjugate-directions.svg) [ajout]

The change of coordinates $z=A^{1/2}w$ turns $\langle\cdot,\cdot\rangle_A$ into the usual inner product and the ellipses of $q$ into circles: conjugate directions are perpendicular directions seen through $A$. Minimizing along one of them then never spoils what the previous minimizations achieved, which is how a single stored direction can do the work of all the past gradients. [slide 16, ajout]

The slides prove the two properties together, by induction on $k$, from the update $g^{k+1}=g^k-\beta_kAd^k$ and the choice of $\alpha_{k+1}$. [slide 18, slide 22, slide 23]

## Le chemin jusqu'ici
ods/conjugate-gradient builds the directions; this card says what they have in common. The method only multiplies by $A$, which ods/matrix-free-product provides from an ods/sparse-matrix, to solve the system of ods/quadratic-form. That system is the optimality condition, ods/first-order-optimality-condition, proved from ods/first-order-characterization and ods/local-minima-are-global for an ods/convex-function, whose ods/epigraph is an ods/convex-set; with $A\succ0$, $q$ is an ods/strongly-convex-function whose minimizer exists by ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact — the question of ods/optimization-problem. [ajout]

## Exemple minimal
For the system of the four observations, $d^0=(-1,-2)$ and $d^1=(\tfrac7{16},-\tfrac38)$ are conjugate, and $g^0=(-1,-2)$, $g^1=(\tfrac12,-\tfrac14)$ are orthogonal. [ajout]

## Geste de calcul type
$Ad^0=(-6,-7)$, so $\langle d^1,Ad^0\rangle=\tfrac7{16}\cdot(-6)+(-\tfrac38)\cdot(-7)=-\tfrac{42}{16}+\tfrac{42}{16}=0$; and $\langle g^1,g^0\rangle=-\tfrac12+\tfrac12=0$. [ajout]

## Cesse d'être valide quand
$A$ is not positive definite: $\langle u,Av\rangle$ is no longer an inner product, and "perpendicular for $A$" loses its meaning. In floating point the conjugacy degrades over many iterations. [slide 23, ajout]

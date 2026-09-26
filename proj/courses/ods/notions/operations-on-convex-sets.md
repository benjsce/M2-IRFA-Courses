---
id: ods/operations-on-convex-sets
nom: Operations that preserve convex sets
type: notion
statut: source
construite_a_partir_de:
- ods/convex-set
alias:
- operations on convex sets
- intersection of convex sets
- Minkowski sum
refs:
- Prop. 2.1
---

## Ce que c'est
Intersections, Cartesian products, sums and affine images of convex sets are convex, so most convex sets are built from simple ones rather than checked by hand. [Prop. 2.1]

## Ce qui la définit
- Any intersection $\bigcap_{i\in I}C_i$ of convex sets is convex, whatever the index set $I$. [Prop. 2.1]
- A Cartesian product $C_1\times\dots\times C_n$ of convex sets is convex; conversely, if the product is convex and no factor is empty, every factor is convex. [Prop. 2.1]
- The Minkowski sum $C_1+C_2=\{x_1+x_2:x_1\in C_1,\ x_2\in C_2\}$ of two convex sets is convex. [Prop. 2.1]
- The image $A(C)$ of a convex set by an affine map $A:\mathbb{R}^n\to\mathbb{R}^m$ is convex. [Prop. 2.1]

The simplex is an example: it is the intersection of the $d$ half-spaces $\{x_i\geq0\}$ with the hyperplane $\{\sum_ix_i=1\}$, so it is convex without checking a single segment. [Ex. 2.1, ajout]

## Le chemin jusqu'ici
ods/convex-set gives the segment condition; each operation is proved by taking two points of the new set and following them back to the sets they come from, where the segment condition already holds. [ajout]

## Exemple minimal
The set of weights $w\in\mathbb{R}^2$ with $w_1\geq0$, $w_2\geq0$ and $w_1+w_2\leq1$ is the intersection of three half-spaces, hence convex. [ajout]

## Cesse d'être valide quand
A union is not on the list, and is not convex in general: $[-1,0]\cup[1,2]$. The converse for products fails when a factor is empty: the product is then empty, hence convex, whatever the other factors are. [Prop. 2.1, ajout]

## Origine
- exercise ods/ex-02: once half-spaces are convex, the orthant follows as an intersection [Exercise 2, ajout]

---
id: ods/matrix-free-product
nom: Matrix-free product
type: notion
statut: source
construite_a_partir_de:
- ods/quadratic-form
- ods/sparse-matrix
alias:
- never form the matrix
- LinearOperator
- matvec
- Hessian-vector product
refs:
- slide 13
- nb. 4
---

## Ce que c'est
To solve $Aw=X^\top y$ one never needs the matrix $A=X^\top X+\lambda I_p$ itself, only its action on a vector, which costs two sparse products. [slide 13]

## Forme
$$w\ \longmapsto\ Aw=X^\top(Xw)+\lambda w,\qquad\text{cost}\approx4\,\mathrm{nnz}(X)\ \text{operations}$$ [slide 13]

## Ce que les symboles modélisent
$w$ is any vector of $\mathbb{R}^p$. The product is computed from right to left: first $Xw$, a vector of $n$ numbers, then $X^\top$ times it, then $\lambda w$ is added. Each sparse product costs about two operations — a multiplication and an addition — per non-zero of $X$. [slide 13, ajout]

## Ce qui la définit
![The product Aw computed without A: w, a million numbers, goes through X to give Xw, a hundred thousand numbers, then through Xᵀ, and λw is added. Each product costs two million operations. The matrix A = XᵀX + λI, 10⁶ × 10⁶ and 8 TB, is never built.](figures/matrix-free-product.svg) [slide 13, ajout]

The cost is about $4\times10^6$ operations — milliseconds — and the memory a handful of vectors of size $p$. What is then needed is a solver that only ever asks for products $Aw$. The same situation arises whenever $Aw$ is cheap and $A$ is not available, for instance for Hessian-vector products obtained by automatic differentiation. [slide 13]

In SciPy, such an operator is a `LinearOperator` built from its `matvec` function, which a solver such as `scipy.sparse.linalg.cg` accepts in place of a matrix. [nb. 4]

## Le chemin jusqu'ici
ods/quadratic-form turns the ridge problem into the system $Aw=X^\top y$ and says what $A$ is; ods/sparse-matrix makes each product with $X$ or $X^\top$ cost only its non-zeros. The quadratic form owes its linear system to ods/first-order-optimality-condition — built on ods/first-order-characterization and ods/local-minima-are-global for an ods/convex-function, an ods/epigraph that is an ods/convex-set — and its unique solution to the ods/strongly-convex-function, via ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact, the minimizer of ods/optimization-problem. [ajout]

## Exemple minimal
For $n=10^5$, $p=10^6$ and $\mathrm{nnz}(X)=10^6$, one product $Aw$ costs about $4\times10^6$ operations, where storing $A$ would take 8 TB. [slide 12, slide 13]

## Geste de calcul type
On the four observations, with $\lambda=1$ and $w=(1,0)$: $Xw=(1,1,1,0)$, $X^\top(Xw)=(3,1)$, and adding $w$ gives $Aw=(4,1)$ — the first column of $\begin{pmatrix}4&1\\1&3\end{pmatrix}$, obtained without forming that matrix. [ajout]

## Cesse d'être valide quand
A solver needs more than products: a direct factorization — Cholesky, the SVD — needs the entries of $A$. And if $X$ is dense, the product costs $4np$ operations, which may make the matrix-free route no cheaper. [slide 13, slide 29, ajout]

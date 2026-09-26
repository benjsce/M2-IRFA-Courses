---
id: ods/sparse-matrix
nom: Sparse matrix
symbole: '$\mathrm{nnz}(X)$'
type: notion
statut: source
alias:
- number of non-zeros
- nnz
refs:
- nb. 3
- slide 12
---

## Ce que c'est
A matrix most of whose entries are zero, stored by its non-zero entries alone, so that its memory and the cost of its products grow with their number rather than with its size. [nb. 3]

## Forme
$$\text{memory}\approx\mathrm{nnz}(X)\times(\text{one value}+\text{one index}),\qquad\text{instead of}\ \ n\times p\times\text{one value}$$ [slide 12, ajout]

## Ce que les symboles modélisent
$\mathrm{nnz}(X)$ counts the non-zero entries of $X$. A value takes 8 bytes in float64 and an index 4: a stored non-zero costs about 12 bytes, a dense entry 8. [slide 12, ajout]

## Ce qui la définit
Sparse matrices arise whenever a large system is mostly empty: text, recommendations, simulations. SciPy supports the usual linear algebra on them — transpose, sum, product by a scalar, product with a vector through `A.dot(v)`, product of matrices — without ever converting them to a dense array, which `toarray()` does on request. [nb. 3]

The data then fits in memory; what does not is what we build from it. The product $X^\top X$ of a sparse matrix with itself is dense in general. [slide 12]

## Exemple minimal
The $3\times3$ matrix of notebook 3, with rows $(1,2,0)$, $(0,0,3)$, $(4,0,5)$, has $\mathrm{nnz}=5$. [nb. 3]

## Geste de calcul type
The data of the slides: $n=10^5$ rows with ten non-zeros each, $\mathrm{nnz}(X)=10^6$. Values $8\times10^6$ bytes, column indices $4\times10^6$, one pointer per row $4\times10^5$: about 12 MB. Dense, the same $X$ would take $8\times10^5\times10^6$ bytes, 800 GB. [slide 12, ajout]

## Cesse d'être valide quand
The matrix is not sparse enough: at 12 bytes per stored entry against 8 for a dense one, sparse storage costs more as soon as about two thirds of the entries are non-zero. Products of sparse matrices fill in, so the savings do not survive forming $X^\top X$. [slide 12, ajout]

## Origine
- exercise ods/ex-09: sparsity does not survive the products of the normal equations, since each row fills a 10 × 10 block of XᵀX [slide 12, ajout]

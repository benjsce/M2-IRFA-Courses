---
id: ods/sparse-storage-format
nom: Sparse storage formats
type: notion
statut: source
construite_a_partir_de:
- ods/sparse-matrix
alias:
- CSR
- CSC
- COO
- LIL
- compressed sparse row
refs:
- nb. 3
---

## Ce que c'est
A sparse matrix can be laid out in memory in several ways, some easy to fill and others fast to compute with; one builds in the first and converts to the second. [nb. 3]

## Ce qui la définit
![The 3 × 3 matrix of notebook 3 and its compressed-sparse-row form: the non-zeros read row by row (data), the column of each one (indices), and, for each row, where it starts in those two arrays (indptr = 0, 2, 3, 5).](figures/sparse-storage-format.svg) [nb. 3, ajout]

Most algorithms — solving systems, multiplying matrices — run efficiently on the compressed formats CSR and CSC, which are not easy to build entry by entry. The coordinate format COO and the list-of-lists format LIL accept new entries cheaply. So a matrix is usually created in COO or LIL and converted to CSR or CSC before computing; the conversions are cheap. [nb. 3]

## Le chemin jusqu'ici
ods/sparse-matrix says to store only the non-zeros; the formats say how, and the choice decides which operations are cheap. [ajout]

## Exemple minimal
In CSR, the notebook's matrix $(1,2,0)$, $(0,0,3)$, $(4,0,5)$ is `data = [1, 2, 3, 4, 5]`, `indices = [0, 1, 2, 0, 2]`, `indptr = [0, 2, 3, 5]`. [nb. 3, ajout]

## Geste de calcul type
Row $i$ of a CSR matrix sits in `data[indptr[i]:indptr[i+1]]`: row 2 is `data[3:5] = [4, 5]` in columns `[0, 2]`. A product with a vector goes row by row through these slices, touching each non-zero once. [ajout]

## Ce qui reste libre
| format | stores | good for | bad for |
|---|---|---|---|
| COO | three arrays: values, rows, columns | building from lists of entries | arithmetic, slicing |
| LIL | one list of (column, value) per row | inserting entries one by one | products |
| CSR | values, columns, and where each row starts | products with a vector, row slices | inserting entries |
| CSC | values, rows, and where each column starts | column slices, some solvers | inserting entries |
[nb. 3]

## Cesse d'être valide quand
Inserting entries one by one into a CSR or CSC matrix forces the arrays to be rebuilt at each insertion: notebook 3 does it on a $10\,000\times10\,000$ matrix to show the difference with LIL. Conversely, products on a LIL matrix are slow. [nb. 3]

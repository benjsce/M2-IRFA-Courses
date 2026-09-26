---
id: ods/singular-value-decomposition
nom: Singular value decomposition
symbole: '$U$, $\Sigma$, $V$'
type: notion
statut: source
alias:
- SVD
- singular values
- pseudo-inverse
refs:
- slide 8
- slide 9
---

## Ce que c'est
Every real matrix factors into a rotation, a stretch along the axes, and another rotation; the stretches are its singular values. [slide 8]

## Forme
$$M=U\Sigma V^\top,\qquad U^\top U=UU^\top=I_n,\quad V^\top V=VV^\top=I_p,\quad \Sigma\ \text{diagonal}$$ [slide 8]

## Ce que les symboles modélisent
$M\in\mathbb{R}^{n\times p}$ is the matrix being factored — in the course, the data matrix $X$. $U$, an $n\times n$ matrix, is orthogonal; its columns, the left-singular vectors, are eigenvectors of $MM^\top$. $V$, a $p\times p$ matrix, is orthogonal too; its columns, the right-singular vectors, are eigenvectors of $M^\top M$. $\Sigma$, an $n\times p$ matrix, is diagonal: its entries $\Sigma_{i,i}$ are the singular values, and their squares are the eigenvalues of both $MM^\top$ and $M^\top M$, with $\Sigma_{i,i}=0$ for $\min(n,p)<i\leq\max(n,p)$. [slide 8, slide 9]

## Ce qui la définit
Read in the basis of $V$ on the way in and of $U$ on the way out, the matrix only multiplies each coordinate by a singular value. This is why the SVD gives at once the rank (the number of nonzero singular values), the null space and the image of the matrix, and its pseudo-inverse, obtained by inverting the nonzero singular values: $M^\dagger=V\Sigma^\dagger U^\top$. [slide 9, ajout]

## Exemple minimal
The data matrix of the four observations has singular values $\sqrt{(5+\sqrt5)/2}\approx1.90$ and $\sqrt{(5-\sqrt5)/2}\approx1.18$; their squares, $3.62$ and $1.38$, are the eigenvalues of $X^\top X$. [ajout]

## Geste de calcul type
Ridge in the SVD basis: $\hat{w}=V\,\mathrm{diag}\big(\tfrac{\sigma_i}{\sigma_i^2+\lambda}\big)\,U^\top y$. Each direction is fitted as least squares would, $1/\sigma_i$, then shrunk by the factor $\sigma_i^2/(\sigma_i^2+\lambda)$: here $3.62/4.62\approx0.78$ and $1.38/2.38\approx0.58$ for $\lambda=1$. With $\lambda=0$ the same formula is the pseudo-inverse, and gives back $(0,1)$. [slide 11, ajout]

## Cesse d'être valide quand
Computing the SVD costs a dense factorization, of order $np\min(n,p)$ operations: for $n=10^5$ and $p=10^6$ it is out of reach, and the slides rule it out. Its value is for moderate sizes, or for solving many problems with the same $X$. [slide 12, slide 29, ajout]

## Origine
- exercise ods/ex-08: computed once, the SVD gives the ridge solution for every λ [slide 11, ajout]

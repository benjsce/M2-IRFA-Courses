---
id: ods/woodbury-identity
nom: Matrix inversion lemma
symbole: '$U$, $C$, $V$'
type: notion
statut: source
alias:
- Woodbury matrix identity
- Woodbury identity
refs:
- slide 10
---

## Ce que c'est
The inverse of a matrix plus a low-rank correction is the inverse of the matrix, corrected by the inverse of a small $k\times k$ matrix. [slide 10]

## Forme
$$(A+UCV)^{-1}=A^{-1}-A^{-1}U\big(C^{-1}+VA^{-1}U\big)^{-1}VA^{-1}$$ [slide 10]

## Ce que les symboles modélisent
$A\in\mathbb{R}^{n\times n}$ is the matrix whose inverse is known, or cheap. $U$ ($n\times k$), $C$ ($k\times k$) and $V$ ($k\times n$) build the correction $UCV$, of rank at most $k$. When $k$ is much smaller than $n$, the only new inverse to compute is $k\times k$. These $U$ and $V$ are not the factors of the singular value decomposition. [slide 10, ajout]

## Retrouver la formule
Known: a candidate for the inverse. Sought: to check that it is one. Try the smallest case: $A=I_2$, $U=(1,1)^\top$, $C=1$, $V=U^\top$, so that $A+UCV=\begin{pmatrix}2&1\\1&2\end{pmatrix}$. The right-hand side gives $I-\tfrac13\begin{pmatrix}1&1\\1&1\end{pmatrix}=\tfrac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$, and multiplying it by $\begin{pmatrix}2&1\\1&2\end{pmatrix}$ gives the identity. [ajout]

In general, multiply $A+UCV$ by the right-hand side. Expanding gives $I+UCVA^{-1}-(U+UCVA^{-1}U)(C^{-1}+VA^{-1}U)^{-1}VA^{-1}$. [slide 10]

Factor $U+UCVA^{-1}U=UC(C^{-1}+VA^{-1}U)$: it cancels the inverse that follows, and what remains is $I+UCVA^{-1}-UCVA^{-1}=I$. [slide 10]

$$(A+UCV)\Big[A^{-1}-A^{-1}U\big(C^{-1}+VA^{-1}U\big)^{-1}VA^{-1}\Big]=I$$ [slide 10]

## Ce qui la définit
Its use in the course: with $A=\lambda I_p$, $U=X^\top$, $C=I_n$ and $V=X$, the $p\times p$ inverse of ridge becomes an $n\times n$ one, which is what the dual formulation exploits. [slide 11, ajout]

## Exemple minimal
$\begin{pmatrix}2&1\\1&2\end{pmatrix}^{-1}=I-\tfrac13\begin{pmatrix}1&1\\1&1\end{pmatrix}$: a rank-one correction of the identity, inverted with a single division by $1+U^\top U=3$. [ajout]

## Geste de calcul type
For a rank-one correction $uv^\top$, the lemma reads $(A+uv^\top)^{-1}=A^{-1}-\dfrac{A^{-1}uv^\top A^{-1}}{1+v^\top A^{-1}u}$: one matrix-vector product and one scalar division update a known inverse. [ajout]

## Cesse d'être valide quand
$A$, $C$ or the small matrix $C^{-1}+VA^{-1}U$ is not invertible. The lemma saves work only when $k$ is small compared with $n$ and $A^{-1}$ is cheap to apply. [slide 10, ajout]

---
id: ods/dual-ridge
nom: Primal and dual formulations of ridge
type: notion
statut: source
construite_a_partir_de:
- ods/ridge-regression
- ods/woodbury-identity
- ods/singular-value-decomposition
alias:
- dual ridge
- primal-dual link
refs:
- slide 11
- slide 12
---

## Ce que c'est
The ridge weights can be computed either from a $p\times p$ system, the primal, or from an $n\times n$ one, the dual; one chooses the smaller. [slide 11]

## Forme
$$\hat{w}=(X^\top X+\lambda I_p)^{-1}X^\top y=X^\top(XX^\top+\lambda I_n)^{-1}y$$ [slide 11]

## Ce que les symboles modélisent
$I_p$ and $I_n$ are the identity matrices of sizes $p$ and $n$. On the left, the matrix to invert has one row per feature; on the right, one row per sample. The vector $(XX^\top+\lambda I_n)^{-1}y$ has one entry per sample, and $\hat{w}$ is $X^\top$ times it: the weights are a combination of the samples. [slide 11, ajout]

## Retrouver la formule
Known: the primal formula. Sought: one that inverts an $n\times n$ matrix. Start from a product that can be read in two ways: $X^\top(XX^\top+\lambda I_n)=X^\top XX^\top+\lambda X^\top=(X^\top X+\lambda I_p)X^\top$. [ajout]

Multiply on the left by $(X^\top X+\lambda I_p)^{-1}$ and on the right by $(XX^\top+\lambda I_n)^{-1}$: $(X^\top X+\lambda I_p)^{-1}X^\top=X^\top(XX^\top+\lambda I_n)^{-1}$. The slides reach the same identity through the matrix inversion lemma. [slide 11, ajout]

Apply both sides to $y$. On the four observations, $n=4$ and $p=2$: the primal system is $2\times2$ and the dual $4\times4$, and both give $(\tfrac1{11},\tfrac7{11})$. In the SVD basis, both equal $V\,\mathrm{diag}\big(\sigma_i/(\sigma_i^2+\lambda)\big)U^\top y$, which confirms the link. [slide 11, ajout]

$$(X^\top X+\lambda I_p)^{-1}X^\top y=X^\top(XX^\top+\lambda I_n)^{-1}y$$ [slide 11]

## Ce qui la définit
![Memory in float64, on a logarithmic scale, for n = 100 000 samples and p = 1 000 000 features with ten non-zeros per row. The sparse matrix X takes 12 MB. The dual matrix XXᵀ takes 80 GB, X stored dense 800 GB, and the primal matrix XᵀX 8 TB — all three beyond a laptop's 16 GB.](figures/dual-ridge.svg) [slide 12]

With $n=10^5$ samples and $p=10^6$ features, the dual is a hundred times smaller than the primal — and still out of reach. $X^\top X$ is dense in general even when $X$ is sparse, so the primal normal equations cannot even be stored, let alone solved; and the SVD is not an option either. [slide 12]

## Le chemin jusqu'ici
ods/ridge-regression gives the primal closed form; ods/woodbury-identity, or the push-through product above, moves the inverse to the $n\times n$ side; ods/singular-value-decomposition shows both formulas as the same shrinkage of each singular direction. The primal form itself comes from the shape of ods/structural-risk-minimization — on ods/empirical-risk, the stand-in for ods/expected-risk — and from the linear system of ods/quadratic-form, through ods/first-order-optimality-condition, ods/first-order-characterization and ods/local-minima-are-global for an ods/convex-function, whose ods/epigraph is an ods/convex-set; the unique minimizer comes from the ods/strongly-convex-function, via ods/existence-under-coercivity, ods/coercive-function and ods/existence-on-a-compact, as for any ods/optimization-problem. [ajout]

## Exemple minimal
For $n=10^5$ and $p=10^6$, the primal matrix takes 8 TB and the dual one 80 GB. [slide 12]

## Geste de calcul type
Memory of a dense $m\times m$ float64 matrix: $8m^2$ bytes. Dual: $8\times(10^5)^2=8\times10^{10}$ bytes, 80 GB; primal: $8\times(10^6)^2=8\times10^{12}$, 8 TB. [slide 12]

## Cesse d'être valide quand
Both sizes are large: then neither formula can be used directly, and the only way out is a solver that never forms either matrix. The dual gains only when $n<p$; with more samples than features, the primal is the smaller system. [slide 12, slide 13, ajout]

## Origine
- exercise ods/ex-08: the SVD shows both formulas as the same shrinkage of each singular direction [slide 11, ajout]
- exercise ods/ex-09: the memory of each matrix, computed from the size of a float64 and of an index [slide 12]

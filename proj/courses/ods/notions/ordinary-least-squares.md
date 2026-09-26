---
id: ods/ordinary-least-squares
nom: Ordinary least squares
symbole: '$A$, $b$, $A^\dagger$, $\varepsilon$'
type: notion
statut: source
cas_de: ods/optimization-problem
construite_a_partir_de:
- ods/existence-under-coercivity
alias:
- OLS
- least-squares problem
- least-square minimization
refs:
- §1.1.2
- Ex. 1.1
---

## Ce que c'est
Choose the weights $x$ that bring $Ax$ as close as possible to the observed responses $b$, closeness being measured by the sum of squared residuals. [§1.1.2]

## Forme
$$\min_{x\in\mathbb{R}^d}\ \tfrac12\|Ax-b\|^2,\qquad x^\star=(A^\top A)^{-1}A^\top b\quad\text{when } A \text{ has full column rank}$$ [§1.1.2]

## Ce que les symboles modélisent
$A$ is the $n\times d$ data matrix: one row per observation, one column per feature. $b$ is the vector of the $n$ observed responses, modeled as $b=Ax_0+\varepsilon$, where $x_0$ is the unknown true weight vector and $\varepsilon$ the noise, or model error. [§1.1.2]

$A^\dagger$ is the Moore–Penrose pseudoinverse of $A$: when $A$ is not of full rank, $A^\dagger b$ is the minimizer of smallest norm. [§1.1.2]

The unknown is $x$ in the notes; the slides call the same weights $w$, the data $X$ and the responses $y$. [§1.1.2, slide 5]

## Ce qui la définit
Known: the data $A$ and the responses $b$. Sought: the weights. A minimizer exists whenever the loss is coercive, which happens exactly when the kernel of $A$ is $\{0\}$; then it is unique and given by the formula. [§1.1.2, Ex. 1.1]

## Le chemin jusqu'ici
ods/existence-under-coercivity guarantees a minimizer as soon as the loss is coercive, and Example 1.1 shows that the least-squares loss is coercive exactly when $\operatorname{Ker}A=\{0\}$. That theorem works by confining the search to a ball, which ods/coercive-function provides, and by applying ods/existence-on-a-compact inside it. What is proved is that the infimum of ods/optimization-problem is reached by a point. [Ex. 1.1, ajout]

## Exemple minimal
With the four observations $(1,1)$, $(1,0)$, $(1,0)$, $(0,1)$ as rows of $A$ and $b=(1,0,0,1)$, the least-squares weights are $x^\star=(0,1)$, and the fit is exact. [ajout]

## Geste de calcul type
$A^\top A=\begin{pmatrix}3&1\\1&2\end{pmatrix}$ and $A^\top b=(1,2)$. Solving $3x_1+x_2=1$, $x_1+2x_2=2$ gives $x_2=1$, $x_1=0$: $x^\star=(0,1)$. The residual $b-Ax^\star$ is zero, since $b$ is exactly the second column of $A$. [ajout]

## Cesse d'être valide quand
$A$ does not have full column rank — more features than observations, or a repeated column. Then $A^\top A$ is not invertible and the formula breaks; the loss is constant along the kernel of $A$, so the minimizers form an unbounded set, and $A^\dagger b$ picks the one of smallest norm. [§1.1.2, Ex. 1.1]

Even with full rank, the formula needs the $d\times d$ matrix $A^\top A$, which cannot be stored when $d$ is a million. [slide 12]

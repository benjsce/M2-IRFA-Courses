---
id: cs/loi-gaussienne-multivariee
nom: Loi gaussienne multivariée
symbole: '$\Phi_X$, $m$, $\Sigma$, $\mathcal N(m,\Sigma)$'
type: notion
statut: source
construite_a_partir_de:
- cs/vecteur-gaussien
alias:
- loi normale multivariée
- multivariate normal distribution
- N(m, Σ)
- fonction caractéristique d'un vecteur gaussien
refs:
- Prop. 0.3.1
- Exercice 0.3.2
---

## Ce que c'est
La loi d'un vecteur gaussien est entièrement fixée par deux objets, le vecteur de ses moyennes et la matrice de ses covariances : on la note $\mathcal N(m,\Sigma)$. [Prop. 0.3.1]

## Forme
$$\Phi_X(x)=E\big[e^{i\langle x,X\rangle}\big]=e^{i\langle x,m\rangle}\,e^{-\frac{x^{t}\Sigma x}{2}}\qquad m=(E[X_1],\dots,E[X_n]),\quad \Sigma=\big[\mathrm{cov}(X_i,X_j)\big]_{1\le i,j\le n}$$ [Prop. 0.3.1]

## Ce que les symboles modélisent
$\Phi_X$ est la fonction caractéristique de $X$ : elle prend un vecteur fixe $x$ de $\mathbb R^n$ et rend un nombre complexe, $E[e^{i\langle x,X\rangle}]$. Elle caractérise la loi : deux vecteurs qui ont la même fonction caractéristique ont la même loi. Ce n'est pas la fonction $\Phi$ de deux variables de la Prop. 0.4.3, qui porte la même lettre. [Prop. 0.3.1, ajout]

$m$ est le vecteur des moyennes des composantes, et $\Sigma$ la matrice carrée de leurs covariances, avec les variances sur la diagonale. $\mathcal N(m,\Sigma)$ est le nom de la loi, ces deux objets donnés. [Prop. 0.3.1]

## Retrouver la formule
![La cloche de ⟨x,X⟩ pour le couple du cours et x = (1, 1) : son centre est ⟨x,m⟩ = 1, son écart type √(xᵗΣx) = √3. Sous la cloche, la Forme : Φ_X(x) = E(e^{i⟨x,X⟩}) = e^{i⟨x,m⟩} e^{−xᵗΣx/2}, le premier facteur porté par le centre, le second par la largeur.](figures/loi-gaussienne-multivariee.svg) [ajout]

Le couple du cours a pour moyennes $0$ et $1$, pour variances $1$ et $1$, et pour covariance ½. Prenons $x=(1,1)$. Par définition d'un vecteur gaussien, $\langle x,X\rangle=X_1+X_2$ est une gaussienne réelle ; il suffit de connaître sa moyenne et sa variance. [Déf. 0.3.1, ajout]

Sa moyenne est $0+1=1$, c'est-à-dire $\langle x,m\rangle$. Sa variance est $1+1+2\times\tfrac12=3$ : la variance d'une somme ajoute les variances et deux fois la covariance, ce qui s'écrit en général $x^{t}\Sigma x=\sum_{i,j}x_ix_j\,\mathrm{cov}(X_i,X_j)$. [ajout]

Une gaussienne réelle $Y$ de moyenne $\mu$ et de variance $v$ a pour fonction caractéristique $E[e^{iuY}]=e^{iu\mu}e^{-u^2v/2}$. On l'évalue en $u=1$, avec $Y=\langle x,X\rangle$, $\mu=\langle x,m\rangle$ et $v=x^{t}\Sigma x$ : [ajout]

$$\Phi_X(x)=E\big[e^{i\langle x,X\rangle}\big]=e^{i\langle x,m\rangle}\,e^{-\frac{x^{t}\Sigma x}{2}}$$ [ajout]

## Ce qui la définit
**On connaît** $m$ et $\Sigma$, soit $n$ moyennes et des covariances deux à deux. **On cherche** la loi du vecteur entier, avec toutes les dépendances entre ses composantes. Pour un vecteur gaussien, les deux premiers moments suffisent : la loi de chaque combinaison $\langle x,X\rangle$ ne dépend que de $\langle x,m\rangle$ et de $x^{t}\Sigma x$, et la fonction caractéristique, qui caractérise la loi, s'en déduit. [Prop. 0.3.1]

Pour un vecteur quelconque, $m$ et $\Sigma$ existent aussi, mais ne fixent pas la loi : deux vecteurs de mêmes moyennes et covariances peuvent avoir des lois très différentes. [ajout]

## Le chemin jusqu'ici
cs/vecteur-gaussien garantit que chaque combinaison $\langle x,X\rangle$ est une gaussienne réelle. C'est ce qui ramène la loi du vecteur à deux nombres par direction $x$, sa moyenne et sa variance, que $m$ et $\Sigma$ fournissent pour toutes les directions à la fois. [Déf. 0.3.1, Prop. 0.3.1]

## Exemple minimal
Le couple du cours suit $\mathcal N\big((0,1),\begin{pmatrix}1&\tfrac12\\\tfrac12&1\end{pmatrix}\big)$ ; en $x=(1,1)$, $\Phi_X(x)=e^{i}\,e^{-3/2}$. [ajout]

## Geste de calcul type
Simuler un $\mathcal N(m,\Sigma)$ : écrire $\Sigma=AA^{t}$, par exemple par la factorisation de Cholesky, tirer $n$ gaussiennes indépendantes $G=(G_1,\dots,G_n)$ de loi $\mathcal N(0,1)$, et rendre $m+AG$, qui suit $\mathcal N(m,AA^{t})$. Pour le couple du cours, $A=\begin{pmatrix}1&0\\\tfrac12&\tfrac{\sqrt3}{2}\end{pmatrix}$, et l'on retrouve $X_2=1+\tfrac12G_1+\tfrac{\sqrt3}{2}G_2$. [Exercice 0.3.2, ajout]

## Cesse d'être valide quand
Le vecteur n'est pas gaussien : $m$ et $\Sigma$ se calculent encore, mais la fonction caractéristique n'a plus cette forme et la loi n'est plus fixée par eux. [Prop. 0.3.1, ajout]

$\Sigma$ est singulière : la formule reste vraie, mais la loi n'a pas de densité (cs/densite-gaussienne). [Prop. 0.3.2]

## Origine
- exercice cs/ex-0-3-2 : toute matrice $\Sigma$ symétrique positive s'écrit $AA^{t}$, et $m+AG$ fabrique un $\mathcal N(m,\Sigma)$ à partir de gaussiennes indépendantes [ajout]

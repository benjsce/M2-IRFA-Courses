---
id: cs/densite-gaussienne
nom: Densité d'un vecteur gaussien
type: notion
statut: source
construite_a_partir_de:
- cs/loi-gaussienne-multivariee
alias:
- densité de la loi normale multivariée
- Gaussian density
- vecteur gaussien dégénéré
refs:
- Prop. 0.3.2
---

## Ce que c'est
Quand sa matrice de covariance est inversible, un vecteur gaussien a une densité ; quand elle ne l'est pas, une combinaison de ses composantes est constante et la densité n'existe pas. [Prop. 0.3.2]

## Forme
$$f(x)=\frac{1}{(2\pi)^{\frac n2}\,\det(\Sigma)^{\frac12}}\;e^{-\frac12(x-m)^{t}\Sigma^{-1}(x-m)}\qquad\text{si }\det\Sigma\neq0$$ [Prop. 0.3.2]

$$\text{si }\det\Sigma=0 :\quad\text{il existe }(c_1,\dots,c_n)\neq(0,\dots,0)\ \text{tel que}\ c_1X_1+\dots+c_nX_n=\text{cste avec probabilité un}$$ [Prop. 0.3.2]

## Ce que les symboles modélisent
$f$ prend un point $x$ de $\mathbb R^n$ et rend une densité de probabilité par rapport à la mesure de Lebesgue, pas une probabilité. $(x-m)^{t}\Sigma^{-1}(x-m)$ mesure l'éloignement de $x$ au centre $m$ en tenant compte des variances et des covariances : il est constant sur des ellipses, et la densité aussi. $\det\Sigma$ est le déterminant de la matrice de covariance, et $(c_1,\dots,c_n)$ les poids de la combinaison qui ne varie pas. [Prop. 0.3.2, ajout]

## Ce qui la définit
Tout se joue sur le déterminant de $\Sigma$. **S'il est non nul**, la masse s'étale dans tout $\mathbb R^n$ et se lit sur des ellipses de densité constante. **S'il est nul**, un vecteur $c$ annule $\Sigma$, la variance de $\langle c,X\rangle$, qui vaut $c^{t}\Sigma c$, est nulle, et toute la masse tient sur un hyperplan, de volume nul : il n'y a plus de densité, et le facteur $1/\det(\Sigma)^{1/2}$ de la formule le dit en explosant. [Prop. 0.3.2, ajout]

![À gauche, le couple du cours, det Σ = ¾ : la densité vaut c × e^{−½ (x−m)ᵗΣ⁻¹(x−m)}, constante sur chaque ellipse, où la forme quadratique vaut 1, puis 4. À droite, le même couple avec une covariance 1, det Σ = 0 : toute la masse est sur la droite X₁ − X₂ = −1, et le facteur 1 / det(Σ)^{1/2} n'existe plus.](figures/densite-gaussienne.svg) [ajout]

## Le chemin jusqu'ici
cs/vecteur-gaussien a fait de chaque combinaison $\langle x,X\rangle$ une gaussienne, de variance $x^{t}\Sigma x$, et cs/loi-gaussienne-multivariee en a tiré que la loi est fixée par $m$ et $\Sigma$. La densité en est l'écriture explicite, et elle n'a de sens que si $\Sigma$ s'inverse : une combinaison de variance nulle est une constante. La forme quadratique $x^{t}\Sigma x$ de la fonction caractéristique devient ici $(x-m)^{t}\Sigma^{-1}(x-m)$, avec l'inverse. [Prop. 0.3.1, Prop. 0.3.2]

## Exemple minimal
Pour le couple du cours, $\det\Sigma=1\times1-\tfrac12\times\tfrac12=\tfrac34$, et la densité au centre $(0,1)$ vaut $1/(2\pi\sqrt{3/4})=1/(\pi\sqrt3)\approx0{,}184$. Avec une covariance $1$ au lieu de ½, $\det\Sigma=0$ et $X_1-X_2=-1$ avec probabilité un. [ajout]

## Geste de calcul type
Calculer $\det\Sigma$. S'il est nul, chercher $c$ dans le noyau de $\Sigma$ ($\Sigma c=0$) : la combinaison $\langle c,X\rangle$ est constante, égale à $\langle c,m\rangle$. Ici $\Sigma=\begin{pmatrix}1&1\\1&1\end{pmatrix}$, $c=(1,-1)$, et la constante vaut $0-1=-1$. [Prop. 0.3.2, ajout]

## Cesse d'être valide quand
$\Sigma$ est singulière : la formule de densité ne s'applique pas, alors que la fonction caractéristique de cs/loi-gaussienne-multivariee reste vraie. Une constante, de variance nulle, est le cas extrême d'un vecteur gaussien sans densité. [Prop. 0.3.2, ajout]

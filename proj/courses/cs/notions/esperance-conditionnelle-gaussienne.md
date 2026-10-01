---
id: cs/esperance-conditionnelle-gaussienne
nom: Espérance conditionnelle d'un vecteur gaussien
symbole: '$(a,b_1,\dots,b_n)$'
type: notion
statut: source
construite_a_partir_de:
- cs/esperance-conditionnelle-sachant-une-variable
- cs/independance-gaussienne
- cs/role-de-l-independance
alias:
- conditional expectation and Gaussian vectors
- régression gaussienne
- espérance conditionnelle linéaire
refs:
- Prop. 0.4.4
---

## Ce que c'est
Dans un vecteur gaussien, la prévision d'une composante sachant les autres est une fonction affine de celles-ci. [Prop. 0.4.4]

## Forme
$$(Z,X_1,\dots,X_n)\ \text{vecteur gaussien}\ \Rightarrow\ E[Z|X_1,\dots,X_n]=a+\sum_{i=1}^nX_ib_i$$ [Prop. 0.4.4]

## Ce que les symboles modélisent
$(a,b_1,\dots,b_n)$ sont des réels, la constante et les coefficients de la régression de $Z$ sur les $X_i$ : $b_i$ dit de combien la prévision de $Z$ bouge quand $X_i$ augmente d'une unité, les autres fixées. $E[Z|X_1,\dots,X_n]$ est la prévision sachant l'information que portent ensemble $X_1,\dots,X_n$. [Prop. 0.4.4, ajout]

## Retrouver la formule
![Le couple du cours, m = (0, 1), variances 1, covariance ½. Sur trois coupes verticales de l'ellipse, en X₁ = −1,5, 0 et 1,5, le milieu de la coupe est marqué : les trois milieux sont alignés sur la droite E(X₂|X₁) = 1 + ½ X₁, qui n'est pas le grand axe de l'ellipse, de pente 1. a = E(X₂) − b E(X₁) = 1 et b = cov(X₁, X₂) / Var X₁ = ½.](figures/esperance-conditionnelle-gaussienne.svg) [ajout]

Le couple du cours, $Z=X_2$ et une seule variable $X_1$. On cherche $b$ tel que $X_2-bX_1$ ne soit pas corrélée à $X_1$ : $\mathrm{cov}(X_2-bX_1,X_1)=\tfrac12-b\times1=0$, d'où $b=\tfrac12$. [ajout]

Le couple $(X_1,\ X_2-\tfrac12X_1)$ est gaussien, et sa covariance est nulle : ses deux composantes sont indépendantes. Le reste $X_2-\tfrac12X_1$ n'apprend donc rien de $X_1$, et sa prévision sachant $X_1$ est sa moyenne, $1-\tfrac12\times0=1$. [Cor. 0.3.1, Prop. 0.4.2 d), ajout]

On écrit $X_2=\tfrac12X_1+(X_2-\tfrac12X_1)$ et l'on prévoit chaque morceau : $X_1$ est connue, le reste se prévoit par sa moyenne. Avec plusieurs variables, on choisit les $b_i$ pour que $Z-\sum X_ib_i$ ne soit corrélée à aucune, et le même argument vaut : [Exercice 0.3.1, ajout]

$$E[Z|X_1,\dots,X_n]=a+\sum_{i=1}^nX_ib_i$$ [Prop. 0.4.4]

## Ce qui la définit
**On connaît** les valeurs de $X_1,\dots,X_n$, et la loi jointe, gaussienne. **On cherche** la prévision de $Z$. En général, $E[Z|X_1,\dots,X_n]$ est une fonction quelconque des $X_i$ ; pour un vecteur gaussien, c'est une droite, ou un hyperplan, et il suffit de trouver ses coefficients. [Prop. 0.4.4]

Les coefficients se calculent avec les seules covariances : avec une variable, $b=\mathrm{cov}(Z,X_1)/\mathrm{Var}\,X_1$ et $a=E[Z]-b\,E[X_1]$. [ajout]

## Le chemin jusqu'ici
cs/esperance-conditionnelle définit la prévision sachant une information, et cs/esperance-conditionnelle-sachant-une-variable dit que, l'information étant celle des $X_i$, on cherche une fonction des $X_i$. [Déf. 0.4.1, Déf. 0.4.2]

Le vecteur étant gaussien (cs/vecteur-gaussien), toute combinaison de ses composantes l'est encore, et sa loi ne dépend que des moyennes et des covariances (cs/loi-gaussienne-multivariee). cs/independance-gaussienne permet alors de couper $Z$ en une combinaison des $X_i$ et un reste non corrélé aux $X_i$, donc indépendant d'eux. cs/role-de-l-independance prévoit ce reste par sa moyenne : ce qui reste de la prévision est affine. [Déf. 0.3.1, Prop. 0.3.1, Cor. 0.3.1, Prop. 0.4.2 d)]

## Exemple minimal
Pour le couple du cours, $E[X_2|X_1]=1+\tfrac12X_1$ : si l'on observe $X_1=2$, on prévoit $X_2=2$. [ajout]

## Geste de calcul type
Calculer $b=\mathrm{cov}(Z,X_1)/\mathrm{Var}\,X_1$, puis $a=E[Z]-b\,E[X_1]$ ; avec plusieurs variables, résoudre le système des covariances $\Sigma_{XX}\,b=\mathrm{cov}(X,Z)$ et poser $a=E[Z]-\sum b_iE[X_i]$. Ici $b=\tfrac12/1$ et $a=1-\tfrac12\times0=1$. [ajout]

## Cesse d'être valide quand
Le vecteur $(Z,X_1,\dots,X_n)$ n'est pas gaussien : la meilleure prévision affine existe toujours, mais l'espérance conditionnelle peut ne pas être affine. Pour $X$ de loi $\mathcal N(0,1)$, $E[X^2|X]=X^2$, qui n'est pas affine en $X$. [ajout]

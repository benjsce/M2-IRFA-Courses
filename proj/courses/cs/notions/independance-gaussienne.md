---
id: cs/independance-gaussienne
nom: Indépendance et covariance nulle
symbole: '$\perp$'
type: notion
statut: source
construite_a_partir_de:
- cs/loi-gaussienne-multivariee
alias:
- indépendance des composantes gaussiennes
- non-corrélation et indépendance
- uncorrelated Gaussian components
refs:
- Cor. 0.3.1
- Exercice 0.3.1
---

## Ce que c'est
Dans un vecteur gaussien, deux composantes sont indépendantes dès que leur covariance est nulle : pour elles, ne pas être corrélées et être indépendantes, c'est la même chose. [Cor. 0.3.1]

## Forme
$$X=(X_1,X_2)\ \text{vecteur gaussien de }\mathbb R^2 :\qquad X_1\perp X_2\iff\mathrm{cov}(X_1,X_2)=0$$ [Cor. 0.3.1]

## Ce que les symboles modélisent
$\perp$ se lit « est indépendant de ». Entre deux variables, il dit que connaître l'une ne change rien à la loi de l'autre ; le chapitre suivant l'emploie aussi entre une variable et une tribu, $\sigma(X)\perp\mathcal G$. [Cor. 0.3.1, Prop. 0.4.2 d)]

## Retrouver la formule
Le sens « indépendantes, donc covariance nulle » est vrai pour toutes les variables de carré intégrable. Tout le contenu est dans l'autre sens. [ajout]

Si $\mathrm{cov}(X_1,X_2)=0$, la matrice $\Sigma$ est diagonale, de diagonale $\sigma_1^2$ et $\sigma_2^2$, et la forme quadratique perd son terme croisé : $x^{t}\Sigma x=x_1^2\sigma_1^2+x_2^2\sigma_2^2$. [ajout]

La fonction caractéristique du couple se coupe alors en deux facteurs, chacun celui d'une composante :
$e^{i(x_1m_1+x_2m_2)}e^{-(x_1^2\sigma_1^2+x_2^2\sigma_2^2)/2}=\big(e^{ix_1m_1}e^{-x_1^2\sigma_1^2/2}\big)\big(e^{ix_2m_2}e^{-x_2^2\sigma_2^2/2}\big)$. [Prop. 0.3.1, ajout]

Une fonction caractéristique de couple qui est le produit de celles des composantes est celle de deux variables indépendantes : [ajout]

$$\Phi_X(x_1,x_2)=\Phi_{X_1}(x_1)\,\Phi_{X_2}(x_2)\iff X_1\perp X_2$$ [ajout]

## Ce qui la définit
**On connaît** un seul nombre, la covariance. **On cherche** une propriété de toute la loi jointe, l'indépendance. En général un nombre ne peut pas la porter ; pour un vecteur gaussien, si, parce que la loi jointe ne dépend que des moyennes et des covariances. [Cor. 0.3.1]

Le même argument vaut par blocs : si $(Z,X_1,\dots,X_n)$ est gaussien et que $Z$ est non corrélée à chaque $X_i$, alors $Z$ est indépendante du vecteur $(X_1,\dots,X_n)$ tout entier. [Exercice 0.3.1]

## Le chemin jusqu'ici
cs/vecteur-gaussien demande que toutes les combinaisons du couple soient gaussiennes, pas seulement ses deux composantes ; c'est cette exigence qui permet à cs/loi-gaussienne-multivariee de fixer la loi du couple par $m$ et $\Sigma$, à travers sa fonction caractéristique. Une covariance nulle efface le terme croisé de cette fonction, qui se coupe alors en produit : c'est la forme même de l'indépendance. [Prop. 0.3.1]

## Exemple minimal
Pour le couple du cours, $\mathrm{cov}(X_1,X_2)=\tfrac12$ : les composantes ne sont pas indépendantes. Mais $X_1$ et $X_2-\tfrac12X_1$, qui forment encore un vecteur gaussien, ont pour covariance $\tfrac12-\tfrac12\times1=0$ : elles sont indépendantes. [ajout]

## Geste de calcul type
Pour prouver une indépendance entre combinaisons d'un vecteur gaussien : vérifier que le nouveau vecteur est gaussien (une transformation linéaire d'un vecteur gaussien l'est), puis calculer la covariance et constater qu'elle est nulle. C'est ainsi qu'on isole, dans $X_2$, la part $X_2-\tfrac12X_1$ que $X_1$ n'explique pas. [Exercice 0.3.1, ajout]

## Cesse d'être valide quand
Les deux variables sont gaussiennes chacune, mais le couple n'est pas un vecteur gaussien : $X$ de loi $\mathcal N(0,1)$ et $\varepsilon X$, avec $\varepsilon=\pm1$ indépendant, ont une covariance nulle et ne sont pas indépendantes, puisque $|\varepsilon X|=|X|$. [ajout]

## Origine
- exercice cs/ex-0-3-1 : la non-corrélation de $Z$ avec chaque composante suffit, dans un vecteur gaussien, à l'indépendance avec le vecteur entier [ajout]

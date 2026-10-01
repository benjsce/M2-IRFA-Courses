---
id: cs/role-de-l-independance
nom: Rôle de l'indépendance
type: notion
statut: source
construite_a_partir_de:
- cs/esperance-conditionnelle
alias:
- role of independence
- conditionner par une information indépendante
refs:
- Prop. 0.4.2 d)
---

## Ce que c'est
Une information indépendante de $X$ n'apprend rien sur $X$ : la prévision de $X$ sachant cette information est son espérance, un nombre. [Prop. 0.4.2 d)]

## Forme
$$\sigma(X)\perp\mathcal G\ \Rightarrow\ E[X|\mathcal G]=E[X]\quad P\text{-p.s.}$$ [Prop. 0.4.2 d)]

## Ce que les symboles modélisent
$\sigma(X)\perp\mathcal G$ dit que tout événement lu sur $X$ est indépendant de tout événement de $\mathcal G$ : ce qu'on apprend de $\mathcal G$ ne change pas la loi de $X$. $E[X]$ est une constante, donc une variable $\mathcal G$-mesurable comme il se doit. [Prop. 0.4.2 d), ajout]

## Ce qui la définit
**On connaît** l'information $\mathcal G$, mais elle ne dit rien de $X$. **On cherche** la prévision de $X$. Faute de rien apprendre, on prévoit comme si l'on ne savait rien : par la moyenne $E[X]$. [Prop. 0.4.2 d)]

## Le chemin jusqu'ici
cs/esperance-conditionnelle demande de vérifier $E[XU]=E[X]\,E[U]$ pour toute $U$ $\mathcal G$-mesurable et bornée ; c'est exactement ce que donne l'indépendance de $X$ et de $U$, puisque l'espérance d'un produit de variables indépendantes est le produit des espérances. [Déf. 0.4.1, ajout]

## Exemple minimal
Deux lancers, $\mathcal G$ le premier, $X'$ égal à $1$ si le second lancer donne pile et $0$ sinon : le second lancer est indépendant du premier, et $E[X'|\mathcal G]=E[X']=\tfrac12$, quel que soit le premier lancer. [ajout]

## Geste de calcul type
Écrire la variable comme une somme d'une part connue et d'une part indépendante, puis traiter chacune par sa règle : pour le nombre de piles $X=Y+X'$, $E[X|\mathcal G]=Y+E[X']=Y+\tfrac12$, ce qui redonne $1{,}5$ si pile et $0{,}5$ si face. [ajout]

## Cesse d'être valide quand
$X$ est seulement non corrélée à l'information, sans en être indépendante : $E[X|\mathcal G]$ peut alors dépendre de ce que $\mathcal G$ révèle. Pour un vecteur gaussien, la non-corrélation suffit, parce qu'elle y entraîne l'indépendance. [ajout]

---
id: cs/vecteur-gaussien
nom: Vecteur gaussien
symbole: '$\langle x,X\rangle$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- Gaussian vector
- vecteur aléatoire gaussien
refs:
- Déf. 0.3.1
- §0.3 slide 2
---

## Ce que c'est
Un vecteur aléatoire dont toutes les combinaisons linéaires des composantes sont des variables gaussiennes, et pas seulement chaque composante prise seule. [Déf. 0.3.1]

## Forme
$$X=(X_1,\dots,X_n)\ \text{est gaussien}\iff\text{pour tout }x\in\mathbb R^n,\ \ \langle x,X\rangle=x_1X_1+\dots+x_nX_n\ \text{est une variable gaussienne}$$ [Déf. 0.3.1]

## Ce que les symboles modélisent
$\langle x,X\rangle$ est le produit scalaire d'un vecteur fixe $x$ et du vecteur aléatoire $X$ : une variable aléatoire réelle, la somme des composantes pondérées par $x_1,\dots,x_n$. Le vecteur $x$ n'a rien d'aléatoire ; c'est lui qu'on fait parcourir tout $\mathbb R^n$. [Déf. 0.3.1]

## Ce qui la définit
La définition demande beaucoup : une infinité de combinaisons, une par $x$. Les composantes elles-mêmes en font partie — $x=(1,0,\dots,0)$ donne $X_1$ —, donc chacune est gaussienne, mais la réciproque est fausse. [Déf. 0.3.1, ajout]

Le contre-exemple tient en deux variables. $X$ suit une $\mathcal N(0,1)$, et $\varepsilon$, indépendant de $X$, vaut $1$ ou $-1$ avec probabilité ½ chacun. Alors $\varepsilon X$ suit encore une $\mathcal N(0,1)$, par symétrie ; mais $X+\varepsilon X$ vaut $0$ dès que $\varepsilon=-1$, donc avec probabilité ½, et $2X$ sinon. Une variable qui a une masse en un point sans y être constante n'est pas gaussienne : le couple $(X,\varepsilon X)$ n'est pas un vecteur gaussien. [ajout]

![En haut, deux couples dont chaque composante suit une loi gaussienne : le couple du cours, aux lignes de niveau elliptiques, et (X, εX), qui vit sur les deux diagonales. En bas, la loi de la combinaison x = (1, 1), la somme des composantes. Pour le couple du cours, une N(1, 3) : gaussienne. Pour (X, εX), une masse ½ en 0 et une demi-cloche ½ N(0, 4) : pas gaussienne, et le couple n'est pas un vecteur gaussien.](figures/vecteur-gaussien.svg) [ajout]

Dans l'autre sens, le cas le plus simple : des variables gaussiennes indépendantes forment toujours un vecteur gaussien. [§0.3 slide 2]

## Exemple minimal
Avec $G_1$ et $G_2$ indépendantes de loi $\mathcal N(0,1)$, le couple $(X_1,X_2)=\big(G_1,\ 1+\tfrac12G_1+\tfrac{\sqrt3}{2}G_2\big)$ est gaussien ; sa somme $X_1+X_2$ suit une $\mathcal N(1,3)$. [ajout]

## Geste de calcul type
Pour montrer qu'un vecteur est gaussien, l'écrire comme $m+AG$, avec $G$ un vecteur de gaussiennes indépendantes : $\langle x,m+AG\rangle=\langle x,m\rangle+\langle A^{t}x,G\rangle$ est une constante plus une combinaison de gaussiennes indépendantes, donc une gaussienne. Pour montrer qu'il ne l'est pas, exhiber une seule combinaison qui ne l'est pas, comme $X+\varepsilon X$ et sa masse en $0$. [Exercice 0.3.2, §0.3 slide 2, ajout]

## Cesse d'être valide quand
La définition compte une constante comme une gaussienne de variance nulle : sans cette convention, $x=0$ donnerait la variable nulle, et aucun vecteur ne serait gaussien. Les slides ne le disent pas ; la Prop. 0.3.2 le suppose, puisqu'elle admet le cas où une combinaison est constante. [Prop. 0.3.2, ajout]

Des composantes gaussiennes, même deux à deux non corrélées, ne suffisent pas : c'est le couple $(X,\varepsilon X)$, de covariance $E[\varepsilon X^2]=E[\varepsilon]\,E[X^2]=0$. [ajout]

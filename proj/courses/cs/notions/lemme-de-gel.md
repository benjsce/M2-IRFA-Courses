---
id: cs/lemme-de-gel
nom: Lemme de gel
symbole: '$\Phi$, $\psi$'
type: notion
statut: source
construite_a_partir_de:
- cs/sortir-ce-qui-est-connu
- cs/role-de-l-independance
alias:
- freezing lemma
- lemme de substitution
- An important result
refs:
- Prop. 0.4.3
---

## Ce que c'est
Pour prévoir une fonction d'une variable connue et d'une variable indépendante de l'information, on fige la variable connue à sa valeur et l'on prend l'espérance sur l'autre seule. [Prop. 0.4.3]

## Forme
$$\sigma(X)\perp\mathcal G,\ \ Y\ \mathcal G\text{-mesurable}\ \Rightarrow\ E[\Phi(X,Y)|\mathcal G]=\psi(Y),\qquad\psi(y)=E[\Phi(X,y)]$$ [Prop. 0.4.3]

## Ce que les symboles modélisent
$\Phi$ est une fonction borélienne de deux variables réelles, telle que $E[|\Phi(X,Y)|]<\infty$ ; elle combine la variable indépendante $X$ et la variable connue $Y$. Ce n'est pas la fonction caractéristique $\Phi_X$ des vecteurs gaussiens. [Prop. 0.4.3]

$\psi$ est la fonction gelée : elle prend un nombre $y$, fixé, et rend l'espérance de $\Phi(X,y)$, où seule $X$ reste aléatoire. Ce n'est pas la fonction convexe $\psi$ de l'inégalité de Jensen. Les slides ne donnent pas de nom à ce résultat, qu'elles intitulent « An important result » ; « lemme de gel » est le nom qu'il porte souvent ailleurs. [Prop. 0.4.3, ajout]

## Retrouver la formule
![Les deux lancers, avec Φ(x, y) = (x + y)², le carré du nombre de piles. À gauche, Y = 1 est gelée : les deux valeurs de X, de probabilité ½, donnent Φ = 4 et 1, de moyenne ψ(1) = 2,5. À droite, Y = 0 : Φ = 1 et 0, ψ(0) = 0,5. E(Φ(X,Y)|𝒢) = ψ(Y), avec ψ(y) = E(Φ(X,y)).](figures/lemme-de-gel.svg) [ajout]

Deux lancers ; $Y$ vaut $1$ si le premier donne pile, $0$ sinon, et elle est connue dans $\mathcal G$ ; $X$ vaut $1$ si le second donne pile, et elle est indépendante de $\mathcal G$. Ce $X$ est la variable indépendante de la Forme, et non le nombre de piles ; le parcours de la prévision, où $X$ compte les piles, l'écrit $X-Y$. On cherche la prévision du carré du nombre de piles, $\Phi(X,Y)=(X+Y)^2$. [ajout]

Si le premier lancer a donné pile, $Y=1$ et il reste $\Phi(X,1)=(X+1)^2$, qui vaut $4$ ou $1$ avec probabilité ½ : sa moyenne est $\psi(1)=2{,}5$. Si face, $\Phi(X,0)=X^2$ vaut $1$ ou $0$ : $\psi(0)=0{,}5$. [ajout]

La prévision est donc $2{,}5$ quand $Y=1$, $0{,}5$ quand $Y=0$ : c'est la fonction $\psi$ évaluée en $Y$. Dans le cas général, on vérifie la définition sur les produits $\Phi(x,y)=f(x)g(y)$, où sortir $g(Y)$, qui est connue, et moyenner $f(X)$, qui est indépendante, donne $E[f(X)]\,g(Y)=\psi(Y)$ ; les slides admettent le passage aux fonctions quelconques. [Prop. 0.4.3, ajout]

$$E[\Phi(X,Y)|\mathcal G]=\psi(Y),\qquad\psi(y)=E[\Phi(X,y)]$$ [Prop. 0.4.3]

## Ce qui la définit
**On connaît** $Y$, puisque l'information $\mathcal G$ la contient, et la loi de $X$, que l'information ne modifie pas. **On cherche** la prévision de $\Phi(X,Y)$, où les deux variables sont mêlées dans une même fonction et ne se séparent pas par un produit. Le lemme dit qu'on peut traiter $Y$ comme une constante pendant le calcul, et ne la remettre qu'à la fin. [Prop. 0.4.3]

## Le chemin jusqu'ici
Tout se vérifie sur la définition de cs/esperance-conditionnelle, avec deux règles qui en découlent. cs/sortir-ce-qui-est-connu traite le facteur connu quand il est en produit ; cs/role-de-l-independance traite la variable indépendante quand elle est seule. Le lemme de gel réunit les deux cas dans une même fonction quelconque : la part connue est figée comme un facteur qui sort, et la part indépendante est moyennée. [Prop. 0.4.2 c), Prop. 0.4.2 d), Prop. 0.4.3]

## Exemple minimal
Deux lancers, $\Phi(x,y)=(x+y)^2$ : $\psi(y)=\tfrac12(1+y)^2+\tfrac12y^2$, donc $E[(X+Y)^2|\mathcal G]=2{,}5$ si le premier lancer donne pile, $0{,}5$ sinon. [ajout]

## Geste de calcul type
Repérer, dans la quantité à prévoir, ce qui est connu et ce qui est indépendant de l'information. Remplacer le connu par une lettre muette $y$, calculer l'espérance en $y$ fixé, puis remettre la variable connue à la place de $y$. [Prop. 0.4.3]

## Cesse d'être valide quand
$X$ n'est pas indépendante de $\mathcal G$ : figer $Y$ ne suffit plus, puisque l'information modifie aussi la loi de $X$, et $E[\Phi(X,y)]$ n'est plus la bonne moyenne. Il faut aussi $E[|\Phi(X,Y)|]<\infty$. [Prop. 0.4.3]

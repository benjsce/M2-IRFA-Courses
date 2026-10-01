---
id: cs/sortir-ce-qui-est-connu
nom: Sortir ce qui est connu
type: notion
statut: source
construite_a_partir_de:
- cs/esperance-conditionnelle
alias:
- taking out what is known
- sortir le connu
refs:
- Prop. 0.4.2 b)
- Prop. 0.4.2 c)
---

## Ce que c'est
Un facteur que l'information $\mathcal G$ connaît se comporte, dans l'espérance conditionnelle, comme une constante : il sort. [Prop. 0.4.2 c)]

## Forme
$$Y\ \mathcal G\text{-mesurable et bornée}\ \Rightarrow\ E[XY|\mathcal G]=Y\,E[X|\mathcal G]\quad P\text{-p.s.}$$ [Prop. 0.4.2 c)]

$$X\ \mathcal G\text{-mesurable}\ \Rightarrow\ E[X|\mathcal G]=X\quad P\text{-p.s.}$$ [Prop. 0.4.2 b)]

## Ce que les symboles modélisent
$Y$ est ici un facteur dont la valeur est connue dès qu'on dispose de $\mathcal G$, et $X$ une variable intégrable quelconque. Ce n'est pas la variable $Y$ par laquelle on conditionne dans $E[X|Y]$. [Prop. 0.4.2 c), ajout]

## Ce qui la définit
**On connaît** l'information $\mathcal G$, et avec elle la valeur de $Y$. **On cherche** la prévision du produit $XY$. Puisque $Y$ est fixée par l'information, prévoir $XY$ revient à prévoir $X$ et à multiplier par la valeur connue de $Y$. [Prop. 0.4.2 c)]

La seconde forme est le cas $X$ connu tout entier : la prévision d'une quantité qu'on connaît est cette quantité. Elle se déduit de la première en prenant $1$ pour $X$ et la variable connue pour $Y$. [Prop. 0.4.2 b), ajout]

## Le chemin jusqu'ici
cs/esperance-conditionnelle demande de vérifier $E[XYU]=E[\,Y E[X|\mathcal G]\,U]$ pour toute $U$ mesurable et bornée ; or $YU$ est encore $\mathcal G$-mesurable et bornée, et l'égalité est celle de la définition appliquée au pari $YU$. [Déf. 0.4.1, ajout]

## Exemple minimal
Deux lancers, $X$ le nombre de piles, $\mathcal G$ le premier lancer, $Y$ égal à $1$ si le premier lancer donne pile et $0$ sinon : $E[XY|\mathcal G]=Y\times E[X|\mathcal G]$, qui vaut $1\times1{,}5=1{,}5$ si pile et $0$ si face. [ajout]

## Geste de calcul type
Dans un produit sous l'espérance conditionnelle, repérer les facteurs mesurables par rapport à l'information, les sortir, et ne garder dedans que ce qui est encore aléatoire. Pour $(Y+X')^2$, avec $Y$ connue : $E[(Y+X')^2|\mathcal G]=Y^2+2Y\,E[X'|\mathcal G]+E[X'^2|\mathcal G]$. [Prop. 0.4.2 c), ajout]

## Cesse d'être valide quand
Le facteur n'est pas $\mathcal G$-mesurable : $E[XY|\mathcal G]$ n'a alors aucune raison de valoir $Y\,E[X|\mathcal G]$, qui n'est même plus $\mathcal G$-mesurable. L'énoncé demande aussi $Y$ bornée, pour que $XY$ reste intégrable. [Prop. 0.4.2 c)]

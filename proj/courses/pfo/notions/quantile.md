---
id: pfo/quantile
nom: Quantile
symbole: '$F$'
type: notion
statut: ajout
construite_a_partir_de: []
alias:
- fonction quantile
- quantile function
- percentile
- centile
- percent point function
refs:
- Déf. 2.5.1
- p. 32
- p. 33
- p. 34
---

## Ce que c'est
La valeur sous laquelle tombe une proportion donnée des réalisations d'une variable aléatoire : le quantile d'ordre $\alpha$ laisse une probabilité $\alpha$ à sa gauche. [ajout]

## Forme
$$F(q_\alpha) = \alpha, \qquad\text{et quand } F \text{ avance par paliers :}\quad q_\alpha = F^{-1}(\alpha) = \inf\{x : F(x) \geq \alpha\}$$ [p. 34, ajout]

## Ce que les symboles modélisent
$F$ est la fonction de répartition : elle prend un niveau et rend une probabilité, celle de tomber en dessous. Le poly la note ainsi dans la relation $F(q_\alpha) = \alpha$ qui définit le quantile que cherche le développement de Cornish-Fisher. Ce n'est ni le prix forward du cours fpp, ni l'ensemble des actes du cours dup. [p. 34, ajout]

$\alpha$ est l'ordre du quantile, une probabilité, et $q_\alpha$ le quantile lui-même, un niveau : le trajet inverse de $F$. [p. 34]

## Ce qui la définit
**On connaît** une probabilité, 5 %, et la loi des rendements. **On cherche** le niveau qui laisse exactement 5 % des rendements à sa gauche. La fonction de répartition fait l'aller, du niveau à la probabilité ; le quantile fait le retour. [ajout]

![Le bas de la fonction de répartition des rendements de l'exemple, grossi. On part du connu, 5 % sur l'axe vertical, on rejoint la courbe, puis on descend sur l'axe des rendements : le quantile cherché vaut −3,24 %.](figures/quantile.svg) [ajout]

Le poly emploie le mot sans le définir : la VaR y est un quantile de la loi des pertes, `stats.norm.ppf` la fonction quantile, inverse de la fonction de répartition de la loi normale, et le développement de Cornish-Fisher une approximation de quantile. [Déf. 2.5.1, p. 33, p. 34]

Un centile est un quantile exprimé en pour cent : le 5e centile est le quantile d'ordre 0,05. `np.percentile` attend donc 5 et non 0,05, d'où le `alpha * 100` du listing. [p. 32, Listing 2.2]

## Exemple minimal
Le quantile d'ordre 5 % de la loi normale centrée réduite vaut −1,6449 ; pour des rendements normaux de moyenne 0,05 % et d'écart type 2 %, il vaut −3,24 %. [ajout]

## Geste de calcul type
Sur un échantillon, trier et lire le rang voulu : sur 1 000 rendements, `np.percentile(r, 5)` interpole entre la 50e et la 51e plus petite valeur. Sur une loi connue, inverser la fonction de répartition : `stats.norm.ppf(0.05)` rend −1,6449, et $0{,}0005 - 1{,}6449 \times 0{,}02 = -3{,}24\,\%$. [ajout]

## Cesse d'être valide quand
Sur un échantillon, $F$ avance par paliers : aucune valeur ne vérifie exactement $F(x) = \alpha$, ou bien plusieurs. La définition par l'infimum prend la plus petite, `np.percentile` interpole, et sur un petit échantillon les deux conventions divergent. [ajout]

Le sens compte : le quantile d'ordre $\alpha$ des rendements, négatif, est l'opposé du quantile d'ordre $1-\alpha$ des pertes. [ajout]

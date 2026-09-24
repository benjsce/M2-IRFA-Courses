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
$$F^{-1}(\alpha) = \inf\{x : F(x) \geq \alpha\}$$ [ajout]

## Ce que les symboles modélisent
Le poly note $F$ la fonction de répartition, dans la relation $F(q_\alpha) = \alpha$ qui définit le quantile que cherche le développement de Cornish-Fisher. [p. 34]

$F$ prend un niveau et rend une probabilité, celle de tomber en dessous. Le quantile fait le trajet inverse : il prend une probabilité et rend un niveau. Ce n'est ni le prix forward du cours fpp, ni l'ensemble des actes du cours dup. [ajout]

## Ce qui la définit
Le poly emploie le mot sans le définir : la VaR y est un quantile de la loi des pertes, `stats.norm.ppf` la fonction quantile, inverse de la fonction de répartition de la loi normale, et le développement de Cornish-Fisher une approximation de quantile. [Déf. 2.5.1, p. 33, §2.5.1]

Un centile est un quantile exprimé en pour cent : le 5e centile est le quantile d'ordre 0,05. `np.percentile` attend donc 5 et non 0,05, d'où le `alpha * 100` du listing. [p. 32, Listing 2.2]

Le quantile est le seuil qu'on retrouve dans tout le chapitre 2 : pfo/valeur-a-risque en est un, pfo/var-historique le lit sur l'échantillon, pfo/var-gaussienne le prend à la loi normale sous le nom $z_\alpha$, et pfo/developpement-de-cornish-fisher le corrige en $q_\alpha$. [ajout]

## Exemple minimal
Le quantile d'ordre 5 % de la loi normale centrée réduite vaut −1,6449 ; pour des rendements normaux de moyenne 0,05 % et d'écart type 2 %, il vaut −3,24 %. [ajout]

## Geste de calcul type
Sur un échantillon, trier et lire le rang voulu : sur 1 000 rendements, `np.percentile(r, 5)` interpole entre la 50e et la 51e plus petite valeur. Sur une loi connue, inverser la fonction de répartition : `stats.norm.ppf(0.05)` rend −1,6449, et $0{,}0005 - 1{,}6449 \times 0{,}02 = -3{,}24\,\%$. [ajout]

## Cesse d'être valide quand
Sur un échantillon, $F$ avance par paliers : aucune valeur ne vérifie exactement $F(x) = \alpha$, ou bien plusieurs. La définition par l'infimum prend la plus petite, `np.percentile` interpole, et sur un petit échantillon les deux conventions divergent. [ajout]

Le sens compte : le quantile d'ordre $\alpha$ des rendements, négatif, est l'opposé du quantile d'ordre $1-\alpha$ des pertes. C'est ce qui brouille la définition de la VaR du poly, qui parle d'« $\alpha$-quantile » de la perte tout en posant $P(L > \mathrm{VaR}_\alpha) = \alpha$. [ajout]

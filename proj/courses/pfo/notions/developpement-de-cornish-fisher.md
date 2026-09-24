---
id: pfo/developpement-de-cornish-fisher
nom: Développement de Cornish-Fisher
symbole: '$q_\alpha$, $\delta$'
type: notion
statut: source
construite_a_partir_de:
- pfo/coefficient-d-asymetrie
- pfo/kurtosis
alias:
- Cornish-Fisher expansion
- quantile de Cornish-Fisher
- Cornish-Fisher
refs:
- p. 34
- éq. 2.25
- éq. 2.26
- éq. 2.27
- éq. 2.28
---

## Ce que c'est
Une correction du quantile de la loi normale qui tient compte de l'asymétrie et de l'excès de kurtosis de la loi réelle. [p. 34, éq. 2.25]

## Forme
$$q_\alpha \approx z_\alpha + \dfrac{S}{6}\left(z_\alpha^2 - 1\right) + \dfrac{K}{24}\left(z_\alpha^3 - 3z_\alpha\right) - \dfrac{S^2}{36}\left(2z_\alpha^3 - 5z_\alpha\right)$$ [éq. 2.25, Listing 2.2]

## Ce que les symboles modélisent
$q_\alpha$ est le quantile d'ordre $\alpha$ corrigé, exprimé en écarts types comme $z_\alpha$ : il ne devient un rendement qu'une fois multiplié par l'écart type et ajouté à la moyenne. $\delta$ est la correction apportée par la non-normalité, l'écart $q_\alpha - z_\alpha$, et elle s'annule quand $S = 0$ et $K = 0$. [p. 34, éq. 2.27, éq. 2.28]

Dans cette formule, $K$ désigne l'excès de kurtosis et non la kurtosis de Pearson. [éq. 2.26]

## Ce qui la définit
La formule dérive du développement d'Edgeworth, qui approche la fonction de répartition d'une loi non normale à partir de la loi normale : on développe autour de $z_\alpha$, puis on inverse approximativement la relation. Les polynômes $z^2 - 1$ et $z^3 - 3z$ qui y apparaissent sont des polynômes d'Hermite associés à la loi normale. [p. 34]

Le terme en $S$ corrige l'asymétrie de la loi, le terme en $K$ l'épaisseur de ses queues. [p. 34]

Le terme en $S^2$ est une correction de second ordre de l'asymétrie. [ajout]

## Le chemin jusqu'ici
pfo/coefficient-d-asymetrie et pfo/kurtosis sont les deux seules informations sur la loi réelle que le développement utilise : de la non-normalité, il ne connaît que ces deux nombres. [ajout]

Tous deux sont réduits par l'écart type de fpp/volatilite, ce qui permet d'ajouter leurs corrections à un quantile lui-même exprimé en écarts types. [ajout]

## Exemple minimal
Pour un seuil de 5 %, une asymétrie de −0,5 et un excès de kurtosis de 3, le quantile passe de $z_\alpha = -1{,}645$ à $q_\alpha = -1{,}722$. [ajout]

## Geste de calcul type
Ajouter les trois termes à $z_\alpha = -1{,}6449$ : $\tfrac{-0{,}5}{6}(2{,}7055 - 1) = -0{,}1421$, puis $\tfrac{3}{24}(-4{,}4502 + 4{,}9346) = +0{,}0605$, puis $-\tfrac{0{,}25}{36}(-8{,}9004 + 8{,}2243) = +0{,}0047$, d'où $q_\alpha = -1{,}7217$. [ajout]

## Cesse d'être valide quand
L'équation 2.25 du poly omet le signe moins devant le terme en $S^2$ ; le listing 2.2 le porte, et c'est lui que suit cette fiche. [éq. 2.25, Listing 2.2]

Avec le signe du poly, l'exemple ci-dessus donnerait −1,731 au lieu de −1,722. [ajout]

Le poly présente $F$ comme la fonction de répartition d'une loi normale standard. [p. 34]

C'est en réalité celle de la loi réelle, centrée et réduite : si $F$ était normale, le quantile cherché serait $z_\alpha$ lui-même, et il n'y aurait rien à corriger. [ajout]

C'est une approximation, bonne pour de petits écarts à la normale : pour une asymétrie ou une kurtosis fortes, le quantile corrigé peut cesser de croître avec $\alpha$, et la formule ne définit plus une fonction quantile. [ajout]

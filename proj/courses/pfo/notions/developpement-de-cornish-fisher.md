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
Le quantile d'une loi non normale, obtenu en corrigeant celui de la loi normale par l'asymétrie et l'excès de kurtosis de la loi réelle. [p. 34, éq. 2.25]

## Forme
$$q_\alpha\approx z_\alpha+\delta,\qquad \delta=\dfrac{S}{6}\left(z_\alpha^2-1\right)+\dfrac{K}{24}\left(z_\alpha^3-3z_\alpha\right)-\dfrac{S^2}{36}\left(2z_\alpha^3-5z_\alpha\right)$$ [p. 34, éq. 2.25, Listing 2.2]

## Ce que les symboles modélisent
$q_\alpha$ est le quantile d'ordre $\alpha$ de la loi réelle, centrée et réduite : le nombre qui vérifie $F(q_\alpha)=\alpha$, où $F$ est la fonction de répartition de cette loi réelle. Il s'exprime en écarts types, comme $z_\alpha$, et ne devient un rendement qu'une fois multiplié par l'écart type et ajouté à la moyenne. [p. 34, ajout]

Le poly présente $F$ comme la répartition d'une loi normale standard, à tort : le quantile cherché serait alors $z_\alpha$ lui-même, et il n'y aurait rien à corriger. [p. 34, ajout]

$\delta$ est la correction, l'écart $q_\alpha-z_\alpha$ ; elle s'annule quand $S=0$ et $K=0$. $z_\alpha$ est le quantile de la loi normale centrée réduite, $S$ l'asymétrie de la loi réelle, et $K$ son excès de kurtosis, non sa kurtosis de Pearson. [p. 34, éq. 2.26, éq. 2.27, éq. 2.28]

## Ce qui la définit
**Connu** : le quantile normal $z_\alpha$, et deux nombres de la loi réelle, son asymétrie $S$ et son excès de kurtosis $K$. **Cherché** : le quantile $q_\alpha$ de cette loi réelle, dont on ne connaît pas la fonction de répartition. Le développement bouche ce trou par une correction $\delta$, somme de trois termes, qu'on ajoute à $z_\alpha$. [p. 34]

![L'exemple, au seuil de 5 %, avec une asymétrie de −0,5 et un excès de kurtosis de 3. On part du quantile normal, connu. Chaque ligne ajoute un terme de la correction : l'asymétrie pousse vers les pertes, la kurtosis ramène un peu vers la moyenne, le terme en S² compte à peine. On arrive au quantile cherché ; le trou entre les deux est δ.](figures/developpement-de-cornish-fisher.svg) [ajout]

Le terme en $S$ déplace le quantile du côté de la queue la plus longue : avec une asymétrie négative, vers les pertes. [p. 34, ajout]

Le terme en $K$ surprend : au seuil de 5 %, il est positif, et rapproche le quantile de la moyenne. Une loi à queues épaisses a aussi des flancs plus minces que la loi normale de même écart type ; à 1,645 écart type, on est encore sur le flanc, et le polynôme $z^3-3z$ ne change de signe qu'en $\pm\sqrt3\approx\pm1{,}73$. Plus loin dans la queue, ce terme pousse vers les pertes. [ajout]

Le terme en $S^2$ est une correction de second ordre de l'asymétrie. [ajout]

La formule vient du développement d'Edgeworth, qui approche la répartition d'une loi non normale à partir de la normale, et qu'on inverse approximativement autour de $z_\alpha$ ; $z^2-1$ et $z^3-3z$ sont des polynômes d'Hermite. [p. 34]

## Le chemin jusqu'ici
pfo/coefficient-d-asymetrie et pfo/kurtosis sont les deux seules informations sur la loi réelle que le développement utilise : de la non-normalité, il ne connaît que ces deux nombres. [ajout]

Tous deux sont réduits par l'écart type de fpp/volatilite, ce qui permet d'ajouter leurs corrections à un quantile lui-même exprimé en écarts types. [ajout]

## Exemple minimal
Pour un seuil de 5 %, une asymétrie de −0,5 et un excès de kurtosis de 3, le quantile passe de $z_\alpha = -1{,}645$ à $q_\alpha = -1{,}722$. [ajout]

## Geste de calcul type
Ajouter les trois termes à $z_\alpha = -1{,}6449$ : $\tfrac{-0{,}5}{6}(2{,}7055 - 1) = -0{,}1421$, puis $\tfrac{3}{24}(-4{,}4502 + 4{,}9346) = +0{,}0605$, puis $-\tfrac{0{,}25}{36}(-8{,}9004 + 8{,}2243) = +0{,}0047$ ; la correction vaut $\delta=-0{,}0769$, d'où $q_\alpha = -1{,}7217$. [ajout]

## Cesse d'être valide quand
L'équation 2.25 du poly omet le signe moins devant le terme en $S^2$ ; le listing 2.2 le porte, et cette fiche le suit. Avec le signe du poly, l'exemple donnerait −1,731. [éq. 2.25, Listing 2.2, ajout]

C'est une approximation, bonne pour de petits écarts à la normale : pour une asymétrie ou une kurtosis fortes, le quantile corrigé peut cesser de croître avec $\alpha$, et la formule ne définit plus une fonction quantile. [ajout]

---
id: pfo/facteur-statistique
nom: Facteur statistique
symbole: '$PC_k$, $PC_{k,t}$, $v_{ik}$, $R$'
type: notion
statut: source
cas_de: pfo/facteur-de-risque
valeur: combiner les rendements selon un vecteur propre de leur covariance, extrait des données
construite_a_partir_de:
- pfo/analyse-en-composantes-principales
alias:
- statistical factor
- composante principale des rendements
- principal component factor
- loadings
- facteur ACP
refs:
- p. 60
- p. 61
- p. 63
- p. 64
- p. 65
- p. 66
---

## Ce que c'est
La combinaison des rendements des actifs selon un vecteur propre de leur covariance : une série datée, dont les coefficients, les loadings, restent fixes. [p. 60, p. 61, p. 65]

## Forme
$$PC_k=V_k^{\top}R,\qquad PC_{1,t}=v_{11}R_{1,t}+v_{21}R_{2,t}+\dots+v_{N1}R_{N,t}$$ [p. 60, p. 61]

## Ce que les symboles modélisent
$R$ est le vecteur des rendements des $N$ actifs à une date ; $PC_k$ la composante $k$, et $PC_{k,t}$ sa valeur à la date $t$. $v_{ik}$, le loading, est le coefficient de l'actif $i$ dans la composante $k$, la $i$-ième coordonnée de $V_k$ : il dit comment l'actif contribue au facteur, pas ce qu'il rapporte. [p. 61, p. 65]

## Ce qui la définit
**Connus** : les loadings, fixés une fois pour toutes par l'analyse, et les rendements de chaque jour. **Cherchée** : la valeur du facteur ce jour-là. Les loadings ne changent pas d'une date à l'autre ; le facteur, si, parce que les rendements changent. [p. 64, p. 65]

![Les deux actifs de l'exemple, de loadings 0,29 et 0,96 sur le premier facteur. Chaque jour est une barre : la part de l'actif 1, v_11 R_1,t, et celle de l'actif 2, v_21 R_2,t ; leur somme est PC_1,t : 2,20 %, puis −0,77 %, puis −0,81 %. Dessous, la Forme : PC_1,t = v_11 R_1,t + v_21 R_2,t.](figures/facteur-statistique.svg) [ajout]

Le cours donne une règle de lecture des loadings. Des coefficients de même signe : les actifs contribuent au facteur dans le même sens. De signes opposés : le facteur oppose leurs mouvements. Proche de zéro : l'actif y contribue peu. Quand les loadings de la première composante sont de même signe et de grandeur comparable sur beaucoup d'actifs, elle se lit comme un mouvement commun du marché. [p. 61, p. 65]

Ce facteur n'est pas le portefeuille de marché : l'analyse ignore les poids économiques des entreprises et ne construit pas le marché ; elle cherche seulement les directions de plus grande variance. [p. 61, p. 72]

En Python, `pca.components_` range les loadings, une ligne par composante, une colonne par actif ; `pca.transform(returns)` donne les valeurs du facteur, une ligne par date. Le premier répond à « comment les actifs se combinent-ils ? », le second à « que vaut le facteur à chaque date ? ». [p. 63, p. 65, p. 66]

## Le chemin jusqu'ici
Les loadings sont les coordonnées d'un vecteur propre que pfo/analyse-en-composantes-principales tire de pfo/matrice-de-covariance. Les rendements qu'ils combinent sont, dans l'exemple, ceux de pfo/rendement-logarithmique, de variances données par le carré de fpp/volatilite et annualisées par fpp/echelonnement-de-la-variance. [ajout]

## Exemple minimal
Un jour où le premier actif fait 1 % et le second 2 %, le premier facteur vaut $0{,}29\times1+0{,}96\times2=2{,}20\,\%$. [ajout]

## Geste de calcul type
Le cours prend trois actions et des loadings $(0{,}60\,;0{,}55\,;0{,}58)$ : le jour où elles font 1,0 %, 0,8 % et 1,2 %, $PC_{1,1}=0{,}60\times1{,}0+0{,}55\times0{,}8+0{,}58\times1{,}2=1{,}74\,\%$. Sa seconde composante, $(-0{,}70\,;0{,}10\,;0{,}70)$, oppose la première action à la troisième. [p. 64, p. 65, ajout]

## Cesse d'être valide quand
Les loadings ne restent fixes que si l'analyse est estimée une seule fois sur tout l'échantillon. Réestimée chaque année, ou sur une fenêtre glissante, elle en donne de nouveaux, et c'est ainsi qu'on vérifie si la structure des facteurs change. [p. 66]

`pca.transform` applique les loadings aux rendements centrés, diminués de leur moyenne : ses valeurs diffèrent de la combinaison des rendements bruts d'une constante. [p. 70, ajout]

Un vecteur propre est défini au signe près : un logiciel peut rendre tous les loadings négatifs, et le facteur change alors de signe sans changer de sens. [ajout]

## Origine
- exercice pfo/ex-09 : construire les séries des trois premiers facteurs sur huit actions [p. 88]

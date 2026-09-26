---
id: pfo/piege-d-agregation
nom: Piège d'agrégation
symbole: '$R_p$, $r_p$, $w_i$'
type: notion
statut: source
construite_a_partir_de:
- pfo/rendement-arithmetique
- pfo/rendement-logarithmique
alias:
- asset aggregation trap
- rendement de portefeuille
refs:
- §1.2.2
- éq. 1.7
- éq. 1.8
---

## Ce que c'est
Le rendement logarithmique d'un portefeuille n'est pas la moyenne pondérée des rendements logarithmiques de ses actifs, alors que c'est vrai du rendement arithmétique. [§1.2.2]

## Forme
$$R_p = \sum_{i=1}^{N} w_i R_i, \qquad r_p = \ln(1+R_p) \;\neq\; \sum_{i=1}^{N} w_i r_i$$ [éq. 1.7, éq. 1.8, ajout]

## Ce que les symboles modélisent
$R_p$ est le rendement arithmétique du portefeuille entier, $r_p$ son rendement logarithmique ; $R_i$ et $r_i$ sont ceux de l'actif $i$, et $w_i$ son poids. [éq. 1.7, éq. 1.8]

Le poids $w_i$ est la part de la valeur du portefeuille placée dans l'actif $i$ en début de période, et les poids somment à un. C'est parce que la valeur du portefeuille est une somme de valeurs que $R_p$ se décompose et que $r_p$ ne le fait pas. [ajout]

## Ce qui la définit
**Connu** : le rendement de chaque actif et son poids. **Cherché** : le rendement logarithmique $r_p$ du portefeuille. La moyenne pondérée des $r_i$, qui vient spontanément, est fausse ; la bonne route passe par l'arithmétique : $R_p$ d'abord, puis son logarithme. [éq. 1.7, éq. 1.8, ajout]

La raison, que donne le cours, est la non-linéarité du logarithme ; ici, précisément, le logarithme d'une moyenne n'est pas la moyenne des logarithmes. Pour des poids positifs, le logarithme étant concave, la moyenne des $r_i$ tombe sous le vrai $r_p$, sauf si tous les actifs ont le même rendement. [§1.2.2, ajout]

Chaque rendement a donc son domaine d'agrégation : l'arithmétique s'agrège entre actifs, le logarithmique entre dates, et aucun des deux ne fait les deux. [ajout]

## Le chemin jusqu'ici
pfo/rendement-arithmetique s'agrège sans peine entre actifs mais se compose mal dans le temps ; pfo/rendement-logarithmique fait exactement l'inverse. [ajout]

Le piège naît de la tentation de garder le second pour tout, parce qu'il est commode dans le temps et que tous les listings du cours le calculent. [ajout]

## Exemple minimal
Un portefeuille placé pour moitié dans un actif qui fait +10 % et pour moitié dans un actif qui fait −10 % a un rendement nul, alors que la moyenne de leurs rendements logarithmiques vaut −0,50 %. [ajout]

![La courbe $r=\ln(1+R)$ et la corde qui joint les deux actifs de l'exemple, à $+10\,\%$ et $-10\,\%$. Le portefeuille fait $R_p=0$, donc $r_p=0$, sur la courbe ; la moyenne des deux logarithmes, $-0{,}50\,\%$, est le milieu de la corde, sous la courbe. À gauche l'écart se voit à peine ; à droite, le voisinage de zéro est agrandi.](figures/piege-d-agregation.svg) [ajout]

## Geste de calcul type
Agréger en arithmétique, puis passer au logarithme : $R_p = 0{,}5 \times 10\,\% + 0{,}5 \times (-10\,\%) = 0$, donc $r_p = \ln(1+R_p) = 0$. La moyenne pondérée $0{,}5 \times 0{,}0953 + 0{,}5 \times (-0{,}1054) = -0{,}0050$ est fausse. [ajout]

## Cesse d'être valide quand
L'écart est du second ordre : pour des rendements journaliers de l'ordre du pour cent, la moyenne pondérée des logarithmes est une bonne approximation, et le piège ne mord que sur de fortes variations ou de longues périodes. [ajout]

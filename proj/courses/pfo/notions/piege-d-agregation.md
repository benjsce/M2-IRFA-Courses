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
$$R_p = \sum_{i=1}^{N} w_i R_i \qquad\text{mais}\qquad r_p \neq \sum_{i=1}^{N} w_i r_i$$ [éq. 1.7, éq. 1.8]

## Ce que les symboles modélisent
$R_p$ est le rendement arithmétique du portefeuille entier, $r_p$ son rendement logarithmique, et $w_i$ le poids de l'actif $i$. [éq. 1.7, éq. 1.8]

Le poids $w_i$ est la part de la valeur du portefeuille placée dans l'actif $i$ en début de période, et les poids somment à un. C'est parce que la valeur du portefeuille est une somme de valeurs que $R_p$ se décompose et que $r_p$ ne le fait pas. [ajout]

## Ce qui la définit
La raison est la non-linéarité du logarithme : le logarithme d'une somme n'est pas la somme des logarithmes. [§1.2.2]

Chaque rendement a donc son domaine d'agrégation : l'arithmétique s'agrège entre actifs, le logarithmique entre dates, et aucun des deux ne fait les deux. [ajout]

## Le chemin jusqu'ici
pfo/rendement-arithmetique s'agrège sans peine entre actifs mais se compose mal dans le temps ; pfo/rendement-logarithmique fait exactement l'inverse. [ajout]

Le piège naît de la tentation de garder le second pour tout, parce qu'il est commode dans le temps et que tous les listings du cours le calculent. La fiche ne fait que croiser les deux propriétés : la linéarité en portefeuille du premier, la non-linéarité du logarithme qui définit le second. [ajout]

## Exemple minimal
Un portefeuille placé pour moitié dans un actif qui fait +10 % et pour moitié dans un actif qui fait −10 % a un rendement nul, alors que la moyenne de leurs rendements logarithmiques vaut −0,50 %. [ajout]

## Geste de calcul type
Agréger en arithmétique, puis passer au logarithme : $R_p = 0{,}5 \times 10\,\% + 0{,}5 \times (-10\,\%) = 0$, donc $r_p = \ln(1+R_p) = 0$. La moyenne pondérée $0{,}5 \times 0{,}0953 + 0{,}5 \times (-0{,}1054) = -0{,}0050$ est fausse. [ajout]

## Cesse d'être valide quand
L'écart est du second ordre : pour des rendements journaliers de l'ordre du pour cent, la moyenne pondérée des logarithmes est une bonne approximation, et le piège ne mord que sur de fortes variations ou de longues périodes. [ajout]

---
id: pfo/portefeuille-de-marche
nom: Portefeuille de marché
symbole: '$w_i^M$, $P_i$, $N_i$, $\mathrm{Capitalisation}_i$'
type: notion
statut: source
construite_a_partir_de:
- pfo/piege-d-agregation
alias:
- market portfolio
- capitalisation boursière
- market capitalization
- pondération par la capitalisation
refs:
- §4.1
- p. 57
- p. 58
---

## Ce que c'est
Le portefeuille qui contient tous les actifs du marché, chacun pesé par sa capitalisation boursière rapportée à celle du marché entier. [p. 57]

## Forme
$$w_i^M=\frac{\mathrm{Capitalisation}_i}{\sum_{j=1}^{n}\mathrm{Capitalisation}_j},\qquad \mathrm{Capitalisation}_i=P_i\times N_i,\qquad \sum_{i=1}^{n}w_i^M=1$$ [p. 57]

## Ce que les symboles modélisent
$P_i$ est le prix d'une seule action de l'entreprise $i$, $N_i$ le nombre total de ses actions en circulation ; leur produit, $\mathrm{Capitalisation}_i$, est ce que vaut l'entreprise entière en bourse. $w_i^M$ est la part de cette valeur dans celle de tout le marché, de $n$ entreprises : un poids de portefeuille, compris entre zéro et un. [p. 57]

## Ce qui la définit
**Connues** : les capitalisations de toutes les entreprises cotées. **Cherchés** : les poids d'un portefeuille qui reproduit le marché entier. Chaque poids est la part de l'entreprise dans la valeur totale du marché, et les poids font un. [p. 57]

![Le premier actif a 2 milliards d'actions à 10 €, le second 500 millions d'actions à 20 €. Prix fois nombre d'actions : 20 et 10 milliards. Le second a l'action la plus chère et le plus petit poids, un tiers ; le premier pèse deux tiers. Dessous, la Forme : w_i^M = Capitalisation_i / Σ_j Capitalisation_j = P_i N_i / Σ_j P_j N_j.](figures/portefeuille-de-marche.svg) [p. 57, ajout]

La capitalisation n'est pas le prix d'une action : une action chère peut appartenir à une petite entreprise. Les poids ne donnent pas non plus davantage aux actifs de rendement espéré élevé ; ils ne dépendent que de la taille relative des entreprises. [p. 57, p. 58]

Le portefeuille se construit donc sans rien optimiser, ce qui le distingue du portefeuille tangent du chapitre 3, obtenu en maximisant le ratio de Sharpe à partir de $\mu$, $\boldsymbol{\Sigma}$ et $R_f$ : ce sont en général deux portefeuilles différents. [p. 58]

## Le chemin jusqu'ici
Le portefeuille de marché est un portefeuille comme un autre, des poids qui font un ; ce qui lui est propre, c'est la règle qui fixe ces poids. Son rendement est la moyenne pondérée des rendements de ses actifs, et pfo/piege-d-agregation rappelle que cette moyenne n'est exacte qu'en pfo/rendement-arithmetique, et non en pfo/rendement-logarithmique. [ajout]

## Exemple minimal
Un marché de deux entreprises : 2 milliards d'actions à 10 €, soit 20 milliards, et 500 millions d'actions à 20 €, soit 10 milliards. Le marché vaut 30 milliards ; les poids sont deux tiers et un tiers. [ajout]

## Geste de calcul type
Multiplier, pour chaque entreprise, le prix de l'action par le nombre d'actions, sommer, puis diviser chaque capitalisation par la somme. Le cours le fait sur un marché de 10 milliards d'euros : une entreprise d'un milliard y pèse $1/10=10\,\%$. [p. 58]

## Cesse d'être valide quand
Le portefeuille de marché théorique contient tous les actifs de l'économie ; il n'est pas observable. En pratique, on le remplace par un indice d'actions, le S&P 500 ou le CAC 40, qui n'en est qu'une approximation. [p. 59, p. 67]

## Origine
- exercice pfo/ex-07 : le S&P 500 y tient lieu de portefeuille de marché [p. 75]

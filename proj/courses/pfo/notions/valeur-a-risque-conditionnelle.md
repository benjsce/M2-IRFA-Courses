---
id: pfo/valeur-a-risque-conditionnelle
nom: Valeur à risque conditionnelle
symbole: '$\mathrm{CVaR}_\alpha$'
type: notion
statut: source
construite_a_partir_de:
- pfo/valeur-a-risque
alias:
- CVaR
- Conditional Value-at-Risk
- Expected Shortfall
- ES
- perte moyenne au-delà de la VaR
refs:
- §2.5
- éq. 2.22
- éq. 2.24
- p. 32
---

## Ce que c'est
La perte moyenne d'un portefeuille dans les scénarios où elle dépasse la VaR. [§2.5, éq. 2.24]

## Forme
$$\mathrm{CVaR}_\alpha = E\big[L \mid L > \mathrm{VaR}_\alpha\big]$$ [éq. 2.24]

## Ce que les symboles modélisent
$\mathrm{CVaR}_\alpha$ est un montant de perte, comme la VaR, mais une moyenne et non un seuil : la moyenne des pertes de la queue de probabilité $\alpha$. Elle est donc toujours au moins égale à la VaR de même niveau. [éq. 2.22, éq. 2.24]

## Ce qui la définit
Elle répond à la question que la VaR laisse ouverte : quand la perte dépasse le seuil, quelle est son ampleur moyenne ? [p. 32]

Deux portefeuilles de même VaR peuvent avoir des CVaR très différentes, et celui dont la CVaR est la plus haute est exposé à des pertes extrêmes plus lourdes. [p. 32]

![La VaR est un seuil ; la CVaR est la moyenne des pertes qui le dépassent, plus loin dans la queue.](figures/valeur-a-risque-conditionnelle.svg) [ajout]

## Le chemin jusqu'ici
pfo/valeur-a-risque fournit le seuil qui délimite la queue ; la CVaR ne fait que moyenner ce qui se trouve au-delà. Elle hérite donc de toutes les conventions de la VaR : l'horizon, le niveau, et le signe de la perte. [ajout]

## Exemple minimal
Avec une VaR à 95 % sur un jour de 50 000 et une CVaR de 75 000, la perte moyenne des 5 % de jours les pires est de 75 000. [p. 32]

## Geste de calcul type
En historique, prendre la moyenne des rendements inférieurs ou égaux au quantile, `log_returns[log_returns <= var_hist_ret].mean()`, puis la changer de signe et la multiplier par le capital. [Listing 2.2, p. 33]

## Cesse d'être valide quand
Elle repose sur les quelques observations de la queue : avec 1 000 rendements et $\alpha = 5\,\%$, elle moyenne une cinquantaine de valeurs, et son estimation est plus bruitée que celle de la VaR. [ajout]

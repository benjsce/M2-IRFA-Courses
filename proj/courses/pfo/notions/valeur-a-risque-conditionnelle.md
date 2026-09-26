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
Elle répond à la question que la VaR laisse ouverte. **Connu** : le seuil, la VaR, que la perte ne dépasse que dans une proportion $\alpha$ des scénarios. **Cherché** : l'ampleur de la perte quand elle le dépasse. La CVaR est la moyenne de ces pertes-là. [p. 32]

![La VaR dit où commence la queue ; la CVaR dit combien on y perd en moyenne. Elle tombe au centre de gravité de la zone colorée, les 5 % de jours les pires, et donc plus loin que la VaR.](figures/valeur-a-risque-conditionnelle.svg) [ajout]

Deux portefeuilles de même VaR peuvent avoir des CVaR très différentes, et celui dont la CVaR est la plus haute est exposé à des pertes extrêmes plus lourdes. [p. 32]

## Le chemin jusqu'ici
pfo/valeur-a-risque fournit le seuil qui délimite la queue ; la CVaR ne fait que moyenner ce qui se trouve au-delà. Elle hérite donc de toutes les conventions de la VaR : l'horizon, le niveau, et le signe de la perte. [ajout]

## Exemple minimal
Sur 100 jours, les cinq pires pertes valent 52, 60, 70, 85 et 108 milliers, et les 95 autres restent sous 50 000 : la VaR à 95 % sur un jour vaut 50 000, la CVaR 75 000. [p. 32, ajout]

## Geste de calcul type
Garder les pertes qui dépassent la VaR, puis les moyenner : $(52+60+70+85+108)/5=75$ milliers. [ajout]

Sur un échantillon, le listing garde aussi une perte égale au seuil (`<=`), là où la Forme écrit $L>\mathrm{VaR}_\alpha$ ; pour une loi continue, cela ne change rien. [Listing 2.2, p. 33]

## Cesse d'être valide quand
Elle repose sur les quelques observations de la queue : avec 1 000 rendements et $\alpha = 5\,\%$, elle moyenne une cinquantaine de valeurs, et son estimation est plus bruitée que celle de la VaR. [ajout]

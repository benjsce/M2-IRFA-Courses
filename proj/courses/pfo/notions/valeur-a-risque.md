---
id: pfo/valeur-a-risque
nom: Valeur à risque
symbole: '$L$, $\alpha$, $\mathrm{VaR}_\alpha$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- Value-at-Risk
- VaR
- quantile de perte
- loss quantile
refs:
- §2.5
- éq. 2.18
- éq. 2.20
- éq. 2.21
- Déf. 2.5.1
- éq. 2.23
---

## Ce que c'est
Le seuil de perte qu'un portefeuille ne dépasse, sur un horizon donné, qu'avec une probabilité donnée. [§2.5, Déf. 2.5.1]

## Forme
$$P(L > \mathrm{VaR}_\alpha) = \alpha$$ [éq. 2.23]

## Ce que les symboles modélisent
$L$ est la perte du portefeuille sur l'horizon, comptée positivement : une perte de 50 000 s'écrit $L = 50\,000$. [Déf. 2.5.1, éq. 2.18]

$\alpha$ est ici la probabilité de dépassement, 5 % pour une VaR dite à 95 % : c'est la valeur que prend `alpha` dans les listings, et celle qu'impose l'équation de la définition. La définition du cours l'appelle pourtant « niveau de confiance », qui serait 95 %. [éq. 2.20, éq. 2.23, Déf. 2.5.1, Listing 2.2]

$\mathrm{VaR}_\alpha$ est un montant de perte, positif, et non un rendement : les listings changent le signe du quantile de rendement et le multiplient par le capital. [Listing 2.2]

## Ce qui la définit
La VaR répond à une question : quel niveau de perte le portefeuille ne dépasse-t-il qu'avec une probabilité donnée, sur un horizon donné ? Elle se fixe par trois éléments, l'horizon, le niveau de confiance et la probabilité de dépassement, qui en est le complément. [§2.5, éq. 2.20]

Elle ne fournit qu'un seuil : elle sépare les scénarios ordinaires des scénarios extrêmes, mais ne dit rien de l'ampleur de la perte une fois le seuil franchi. [éq. 2.21, p. 32]

Le cours la range parmi les indicateurs de risque exigés par les cadres réglementaires de Bâle III et de Solvabilité II. [p. 19, §2.5]

## Exemple minimal
Une VaR à 95 % sur un jour de 50 000 signifie que la perte d'une journée dépasse 50 000 avec une probabilité de 5 %. [p. 32, éq. 2.18]

## Geste de calcul type
Lire la VaR comme un quantile : sur 1 000 rendements journaliers, `np.percentile(returns, 5)` renvoie le rendement que seules une cinquantaine d'observations, les pires, dépassent vers le bas ; changé de signe et multiplié par le capital, il rend la VaR en montant. [Listing 2.2, p. 32]

## Cesse d'être valide quand
Deux portefeuilles peuvent avoir la même VaR et des pertes extrêmes très différentes : la VaR est aveugle à ce qui se passe au-delà du seuil. [p. 32]

Elle n'est pas sous-additive : la VaR d'un portefeuille peut dépasser la somme des VaR de ses composantes, ce qui revient à pénaliser la diversification. [ajout]

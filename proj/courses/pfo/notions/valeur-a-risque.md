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

$\alpha$ est ici la probabilité de dépassement, 5 % pour une VaR dite à 95 %. La Déf. 2.5.1 l'appelle « niveau de confiance », qui serait plutôt 95 % ; les listings et l'équation de la définition la prennent à 5 %. [éq. 2.20, éq. 2.23, Déf. 2.5.1, Listing 2.2]

$\mathrm{VaR}_\alpha$ est un montant de perte, positif, et non un rendement. [Listing 2.2]

## Ce qui la définit
**On connaît** la loi des pertes sur l'horizon, ou à défaut un historique de rendements, et la probabilité qu'on accepte de voir dépassée, 5 %. **On cherche** un montant : le seuil de perte qui n'est dépassé qu'avec cette probabilité. [§2.5, éq. 2.23, ajout]

Deux choix la fixent : l'horizon, et le niveau, 95 %, ou, ce qui revient au même, 5 % de probabilité de dépassement. [éq. 2.20]

Elle ne fournit qu'un seuil : elle sépare les scénarios ordinaires des scénarios extrêmes, mais ne dit rien de l'ampleur de la perte une fois le seuil franchi. [éq. 2.21, p. 32]

## Exemple minimal
Une VaR à 95 % sur un jour de 50 000 signifie que la perte d'une journée dépasse 50 000 avec une probabilité de 5 %. [p. 32, éq. 2.18]

## Geste de calcul type
Lire le quantile à 5 % des rendements, puis changer son signe et le multiplier par le capital. Pour des rendements journaliers de moyenne 0,05 % et d'écart type 2 %, supposés normaux, ce quantile vaut −3,24 % ; sur un capital de 1 000 000, $\mathrm{VaR} = -(-0{,}032397) \times 1\,000\,000 \approx 32\,397$. [Listing 2.2, ajout]

![Mille rendements journaliers répartis comme la loi normale de l'exemple, un trait par jour, sur l'axe des rendements en haut. Les cinquante pires, 5 % des jours, sont en couleur ; le quantile à 5 %, −3,24 %, est leur bord. L'axe du bas lit les mêmes jours en pertes sur un capital de 1 000 000 : il va dans l'autre sens, et le bord devient la VaR, 32 397.](figures/valeur-a-risque.svg) [ajout]

Sur un historique, `np.percentile(returns, 5)` fournit ce quantile : sur 1 000 rendements, une cinquantaine d'observations, les pires, sont en dessous. [Listing 2.2, p. 32]

## Cesse d'être valide quand
Deux portefeuilles peuvent avoir la même VaR et des pertes extrêmes très différentes : la VaR est aveugle à ce qui se passe au-delà du seuil. [p. 32]

Elle n'est pas sous-additive : la VaR d'un portefeuille peut dépasser la somme des VaR de ses composantes, ce qui revient à pénaliser la diversification. [ajout]

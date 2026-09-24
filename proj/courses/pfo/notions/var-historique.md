---
id: pfo/var-historique
nom: VaR historique
type: notion
statut: source
cas_de: pfo/modele-de-risque
valeur: 'aucune hypothèse : la loi empirique de l''échantillon'
construite_a_partir_de:
- pfo/valeur-a-risque-conditionnelle
alias:
- historical VaR
- VaR non paramétrique
- CVaR historique
- historical simulation
refs:
- p. 32
- Listing 2.2
---

## Ce que c'est
La VaR et la CVaR lues directement sur les rendements passés, sans hypothèse sur leur loi : le quantile empirique, puis la moyenne des rendements qui lui sont inférieurs. [Listing 2.2, p. 32]

## Ce qui la définit
`np.percentile(log_returns, alpha * 100)` extrait le 5e centile des rendements, que l'on change de signe et multiplie par le capital. La CVaR historique est la moyenne des rendements inférieurs ou égaux à ce centile, traitée de la même façon. [Listing 2.2, p. 32, p. 33]

C'est la méthode qui ne suppose rien : les queues épaisses et l'asymétrie de l'échantillon sont dans ses quantiles telles qu'elles ont été observées. [ajout]

## Le chemin jusqu'ici
pfo/valeur-a-risque définit le quantile à lire, pfo/valeur-a-risque-conditionnelle la moyenne à prendre au-delà. La méthode historique les lit sur l'échantillon tel quel, avec l'outil le plus simple qui soit, un tri. [ajout]

## Exemple minimal
Sur 1 000 rendements journaliers dont le 5e centile vaut −3,2 % et dont la moyenne des rendements inférieurs vaut −4,5 %, un capital de 1 000 000 porte une VaR de 32 000 et une CVaR de 45 000. [ajout]

## Cesse d'être valide quand
Elle ne connaît que les pertes déjà vues : un krach plus fort que tout ce que contient la fenêtre est hors de sa portée, et le choix de la fenêtre change le résultat. [ajout]

`np.percentile` interpole entre deux observations voisines : sur un petit échantillon, la VaR dépend de cette convention. [ajout]

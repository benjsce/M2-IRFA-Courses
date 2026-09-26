---
id: fpp/option
nom: Option
type: notion
statut: source
construite_a_partir_de:
- fpp/payoff
alias:
- call
- put
- option d'achat
- option de vente
- strike
- prix d'exercice
- option européenne
- European option
refs:
- Déf. 9
- Déf. 10
- §6.1
---

## Ce que c'est
Le droit, et non l'obligation, d'acheter (call) ou de vendre (put) une action à une date T, au prix K fixé d'avance. [Déf. 9]

## Ce qui la définit
Le prix $K$ s'appelle le strike, la date $T$ la maturité. Une option européenne ne paie qu'à la date $T$, sans exercice ni paiement intermédiaire. [Déf. 9, Déf. 10]

À la différence d'un contrat à terme, l'option laisse le choix à son détenteur : il n'achète au prix $K$ que si cela l'arrange, c'est-à-dire si l'action vaut alors plus que $K$. D'où son payoff $(S_T-K)^+$. [§6.1, Déf. 11]

Ce droit a une valeur : l'option se paie à la signature, alors qu'un contrat à terme ne coûte rien. Ce qui est **connu** : le strike, la maturité, le prix de l'action. Ce qu'on **cherche** : ce prix, appelé prime, qui est la question de tout le chapitre 6. [§6.1, ajout]

![Un call de strike K à maturité T, dans deux scénarios. Si S_T > K, le détenteur exerce et gagne S_T − K. Si S_T < K, il n'exerce pas et ne reçoit rien : il reçoit (S_T − K)⁺.](figures/option.svg) [ajout]

## Le chemin jusqu'ici
fpp/payoff décrit un contrat par ce qu'il paie ; l'option est le contrat dont le payoff est coudé, parce que son détenteur choisit d'exercer ou non. [ajout]

## Exemple minimal
Un call de strike 100 à un an sur l'action qui cote 100. [ajout]

## Cesse d'être valide quand
Une option américaine peut s'exercer avant l'échéance, et ce droit supplémentaire peut valoir quelque chose. Les dividendes versés pendant la vie de l'option ne reviennent pas à son détenteur. [Déf. 10, §6.2]

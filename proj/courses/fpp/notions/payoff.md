---
id: fpp/payoff
nom: Payoff
symbole: $G$
type: notion
statut: source
construite_a_partir_de: []
alias:
- payoff
- flux terminal
refs:
- Déf. 11
- §9.1
---

## Ce que c'est
La fonction qui dit combien le contrat paie, en fonction de ce qu’on a observé. [Déf. 11]

## Forme
$$\mathrm{Call}(S_T,K)=(S_T-K)^+,\qquad \mathrm{Put}(S_T,K)=(K-S_T)^+,\qquad x^+=\max(x,0)$$ [Déf. 11]

## Ce qui la définit
C’est une fonction de plusieurs observables : valeur finale, maximum, minimum, moyenne, franchissement d’une barrière. Le payoff est le contrat ; tout le reste est valorisation. [Déf. 11]

Les payoffs élémentaires se combinent : call spread, option digitale, straddle s’obtiennent par sommes et différences de calls et de puts. [§9.1]

## Exemple minimal
Un call de strike 100 sur un sous-jacent qui finit à 104,08 paie 4,08. [ajout]

## Geste de calcul type
Tracer le payoff par morceaux avant de valoriser : le nombre de points de rupture donne le nombre de calls ou de puts nécessaires pour le répliquer. [§9.1]

## Cesse d'être valide quand
La forme $(S_T-K)^+$ suppose un payoff qui ne dépend que de la valeur terminale ; dès qu’il dépend du chemin, il faut le dire dans $G$. [Déf. 11]

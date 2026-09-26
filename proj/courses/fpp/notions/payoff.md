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
$$\text{flux payé en }T=G(\text{ce qu'on a observé jusqu'en }T),\qquad\text{par exemple, pour un call : }G=(S_T-K)^+,\quad x^+=\max(x,0)$$ [Déf. 11]

## Ce que les symboles modélisent
$G$ est une fonction et non un montant : elle prend ce qui a été observé et rend ce que le contrat paie. Tout le contenu d'un contrat tient en elle ; le prix et la couverture s'en déduisent, ils ne s'ajoutent pas à elle. [Déf. 11]

$S_T$ est le prix du sous-jacent à la date $T$, et $K$ un prix écrit au contrat ; $x^+$, la partie positive, vaut $x$ s'il est positif et zéro sinon. [Déf. 9, Déf. 11]

## Ce qui la définit
Ce qu'on observe n'est pas seulement la valeur finale : le maximum, le minimum, la moyenne, le franchissement d’une barrière le sont aussi, et chaque contrat choisit ce qu'il lit. [Déf. 11]

![Une seule trajectoire du sous-jacent, de $t$ à $T$, choisie pour le dessin : elle part de 100 et finit à 104,08. Cinq contrats la lisent, chacun à sa façon : la valeur finale, le maximum, le minimum, la moyenne, le franchissement de la barrière 115. Même trajectoire, cinq montants différents : le contrat, c'est la fonction $G$.](figures/payoff.svg) [ajout]

Les payoffs élémentaires se combinent : un call spread et un straddle sont des sommes et différences de calls et de puts, et une option digitale est la limite d'un call spread de plus en plus serré. [§9.1, ajout]

## Exemple minimal
Un call de strike 100 sur un sous-jacent qui finit à 104,08 paie 4,08. [ajout]

## Geste de calcul type
Pour un payoff qui ne dépend que de $S_T$, le tracer par morceaux avant de valoriser : chaque coude, au point $K$, se reproduit par des calls de strike $K$, en nombre égal au changement de pente, vendus si la pente baisse ; la partie linéaire qui reste se fait avec le sous-jacent et un zéro-coupon. [ajout]

## Cesse d'être valide quand
La forme $(S_T-K)^+$ suppose un payoff qui ne dépend que de la valeur terminale ; dès qu’il dépend du chemin, il faut le dire dans $G$. [Déf. 11]

---
id: fpp/payoff
nom: Payoff
symbole: '$G$, $x^+$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- profil de paiement
- fonction de paiement
refs:
- Déf. 11
---

## Ce que c'est
La fonction qui donne le montant payé à partir de grandeurs observées, comme la valeur finale d'un actif, son maximum, sa moyenne ou le franchissement d'une barrière. [Déf. 11]

## Forme
$$\mathrm{Call}(S_T,K)=(S_T-K)^+,\qquad \mathrm{Put}(S_T,K)=(K-S_T)^+,\qquad x^+=\max(x,0)$$ [Déf. 11]

## Ce que les symboles modélisent
$G$ est le payoff en général : il prend des observables et rend un montant. $x^+$ est la partie positive, $x$ s'il est positif et 0 sinon ; c'est elle qui plie la droite en coude. $S_T$ est la valeur finale de l'actif, $K$ un montant fixé dans le contrat. [Déf. 11]

## Ce qui la définit
Un payoff décrit un contrat par ce qu'il paie, indépendamment de son prix. Celui d'un achat à terme est la droite $S_T-K$, qui peut être négative ; ceux du call et du put sont coudés en $K$ et jamais négatifs. [Déf. 11, ajout]

![Le payoff du call (S_T − K)⁺ et celui du put (K − S_T)⁺ : le call paie au-dessus de K, le put en dessous, et aucun ne paie jamais de montant négatif.](figures/payoff.svg) [Déf. 11, ajout]

## Exemple minimal
L'action finit à 120 et le strike vaut 100 : le call paie 20, le put 0. [ajout]

## Geste de calcul type
Évaluer le payoff dans chaque scénario de l'observable, avant de se demander ce qu'il vaut aujourd'hui : à 80, le call paie 0 et le put 20. [ajout]

## Cesse d'être valide quand
Un payoff qui dépend du maximum, de la moyenne ou d'une barrière dépend de toute la trajectoire, pas seulement de $S_T$ ; les formules du chapitre 6 portent sur les payoffs européens fonctions de la seule valeur finale. [Déf. 11, §6.2]

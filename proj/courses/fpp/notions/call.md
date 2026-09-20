---
id: fpp/call
nom: Call
symbole: $C$
type: notion
statut: source
cas_de: fpp/option
valeur: le droit d’acheter
construite_a_partir_de:
- fpp/payoff
alias:
- call option
- option d'achat
refs:
- Déf. 9
- Déf. 11
---

## Ce que c'est
Le droit d’acheter le sous-jacent au prix $K$ à la date $T$. [Déf. 9]

## Forme
$$\mathrm{Call}(S_T,K)=(S_T-K)^+$$ [Déf. 11]

## Ce qui la définit
Le détenteur n’exerce que si $S_T>K$ : le payoff est nul en dessous, linéaire de pente 1 au-dessus. [Déf. 11]

## Exemple minimal
Strike 100, sous-jacent à 104,08 à l’échéance : le call paie 4,08. [ajout]

## Geste de calcul type
Pour valoriser, ne jamais actualiser le payoff moyen sous $\mathbb{P}$ : passer sous $\mathbb{Q}$, où $\mathbb{E}^{\mathbb{Q}}(S_T)=F(t,T)$, puis actualiser par $P(t,T)$. [Prop. 6]

## Cesse d'être valide quand
Le prix du call n’a de forme fermée que sous les hypothèses de Black et Scholes ; hors de là il reste une espérance à calculer. [§6.4]

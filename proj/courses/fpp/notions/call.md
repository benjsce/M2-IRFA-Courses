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

## Ce que les symboles modélisent
$C$ est le prix du droit, et non le gain qu'il procurera : ce qu'on paie aujourd'hui pour pouvoir acheter plus tard. Il ne se confond pas avec le strike, qui est fixé au contrat et n'est payé qu'en $T$, et seulement si l'on exerce. [§6.4, ajout]

La Forme donne ce que le call paie en $T$ ; $C$, lui, est ce que vaut aujourd'hui ce paiement, et le Geste dit comment l'obtenir. [§6.4, ajout]

## Ce qui la définit
Le détenteur n’exerce que si $S_T>K$ : le payoff est nul en dessous, linéaire de pente 1 au-dessus. [Déf. 11]

## Le chemin jusqu'ici
Tout part de fpp/payoff, qui dit comment se calcule ce que paie un contrat en fonction de ce qu'on aura observé. [ajout]

Le call n'est qu'un payoff particulier, $(S_T-K)^+$ : à ce stade on n'a fait que décrire le contrat. [ajout]

## Exemple minimal
Strike 100, sous-jacent à 104,08 à l’échéance : le call paie 4,08. [ajout]

## Geste de calcul type
Pour valoriser : prendre l'espérance du payoff $(S_T-K)^+$ sous $\mathbb{Q}$, puis actualiser par $P(t,T)$. [Prop. 6]

Deux raccourcis sont faux. Prendre l'espérance sous $\mathbb{P}$ fait entrer une dérive que le prix ignore. Appliquer le payoff à l'espérance, le prix forward $F(t,T)$, ne donne que la valeur intrinsèque : $0{,}9608\times(104{,}08-100)=3{,}92$, quand le call vaut 9,93. [Prop. 6, Déf. 12, ajout]

## Cesse d'être valide quand
Le prix du call n’a de forme fermée que sous les hypothèses de Black et Scholes ; hors de là il reste une espérance à calculer. [§6.4]

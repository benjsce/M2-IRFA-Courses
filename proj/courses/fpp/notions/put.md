---
id: fpp/put
nom: Put
symbole: $P$
type: notion
statut: source
cas_de: fpp/option
valeur: le droit de vendre
construite_a_partir_de:
- fpp/payoff
alias:
- put option
- option de vente
refs:
- Déf. 9
- Déf. 11
---

## Ce que c'est
Le droit de vendre le sous-jacent au prix $K$ à la date $T$. [Déf. 9]

## Forme
$$\mathrm{Put}(S_T,K)=(K-S_T)^+$$ [Déf. 11]

## Ce que les symboles modélisent
$P$ est le prix du droit de vendre : un montant payé aujourd'hui. La lettre est aussi celle du zéro-coupon $P(t,T)$, et seuls les arguments les distinguent — un prix d'option n'en porte pas. Une exception : le livre d'exercices note $P(T,F_T)$, avec deux arguments, un prix de put sur la valeur d'une firme. [§6.4, exo. 16]

## Ce qui la définit
Symétrique du call par rapport au strike : le détenteur n’exerce que si $S_T<K$, et le payoff est borné par $K$. [Déf. 11]

## Le chemin jusqu'ici
Le socle s'arrête à fpp/payoff. Le put est le payoff $(K-S_T)^+$, le symétrique du call. [ajout]

Il n'est pas *construit* sur le call : les deux sont deux payoffs élémentaires, définis en parallèle, et ce qui les relie est un résultat, pas une définition. [ajout]

## Exemple minimal
Strike 100, sous-jacent à 96 à l’échéance : le put paie 4. [ajout]

## Geste de calcul type
Plutôt que de refaire le calcul, déduire le put du call par la parité : $P=C-S_0+KP(0,T)$, où le premier $P$ est le put et le second le zéro-coupon. [Prop. 7]

## Cesse d'être valide quand
Comme celui du call, le prix du put n'a de forme fermée que sous les hypothèses de Black et Scholes ; hors de là il reste une espérance à calculer. [§6.4]

## Origine
- exercice fpp/ex-18 : le put est l'instrument naturel d'un exportateur exposé à la baisse d'une devise ; le §9 ne traite que les stratégies sur actions [exo. 18]

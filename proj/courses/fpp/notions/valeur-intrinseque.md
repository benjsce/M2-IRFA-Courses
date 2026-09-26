---
id: fpp/valeur-intrinseque
nom: Valeur intrinsèque
symbole: $IV$
type: notion
statut: source
construite_a_partir_de:
- fpp/option
- fpp/probabilite-risque-neutre
alias:
- intrinsic value
refs:
- Déf. 12
- §6.2
- exo. 9
---

## Ce que c'est
Le prix qu'aurait un payoff si le sous-jacent valait à coup sûr, à l'échéance, son espérance risque-neutre, c'est-à-dire son prix forward. [Déf. 12]

## Forme
$$IV=e^{-rT}\,g\big(E(S_T)\big)$$ [Déf. 12]

## Ce que les symboles modélisent
$IV$ est un prix. $g$ est le payoff, $E(S_T)$ l'espérance du prix final sous la probabilité qui sert à fixer les prix, c'est-à-dire le prix forward. [Déf. 12, §6.1]

## Ce qui la définit
Ce qui est **connu** : le prix forward de l'action, 104,08, et le payoff. Ce qu'on **cherche** : ce que vaudrait l'option si l'avenir était certain. On paie le payoff au prix forward, $104{,}08-100=4{,}08$, et on l'actualise : 3,92. C'est aussi le prix du payoff dans un modèle sans aléa. [Déf. 12]

Au sens du poly, un call dont le strike égale le prix comptant n'a pas une valeur intrinsèque nulle : elle se calcule sur le prix forward, pas sur le prix comptant. Le livre d'exercices la compare au gain d'un exercice immédiat. [Déf. 12, exo. 9, ajout]

![La valeur intrinsèque d'un call de strike K : dans un monde sans aléa, l'action vaudrait à coup sûr son prix forward F = E(S_T) ; le call paierait F − K en T, et ce paiement vaut IV = e^(−rT) (F − K)⁺ aujourd'hui.](figures/valeur-intrinseque.svg) [ajout]

## Le chemin jusqu'ici
fpp/option fournit le payoff à évaluer, fpp/payoff sa forme coudée. fpp/probabilite-risque-neutre dit quelle espérance prendre, celle qui tombe sur fpp/prix-forward, et qu'il faut l'actualiser comme fpp/valeur-actuelle-nette le fait d'un flux certain. [ajout]

Le prix forward sortait de fpp/cash-and-carry, et l'actualisation de fpp/zero-coupon, dans la convention continue de fpp/capitalisation, sous la contrainte de fpp/absence-d-arbitrage. [ajout]

## Exemple minimal
L'action à 100, un taux de 4 %, un call de strike 100 à un an : sa valeur intrinsèque vaut 3,92 ; celle du put de même strike vaut 0. [ajout]

## Geste de calcul type
Calculer le prix forward, y appliquer le payoff, actualiser : $e^{-0,04}\times(104{,}08-100)^+=3{,}92$. [Déf. 12]

## Cesse d'être valide quand
Sur les marchés, on parle souvent de valeur intrinsèque pour $S_0-K$, calculée sur le prix comptant ; ce n'est pas la définition du poly, et les deux diffèrent dès que les taux ne sont pas nuls. [ajout]

---
id: fpp/valeur-intrinseque
nom: Valeur intrinsèque
symbole: $\mathrm{IV}$
type: notion
statut: source
construite_a_partir_de:
- fpp/mesure-risque-neutre
- fpp/payoff
alias:
- intrinsic value
refs:
- Déf. 12
- §6.2
---

## Ce que c'est
Le payoff appliqué au prix forward, puis actualisé : ce que vaudrait l'option si le sous-jacent valait à coup sûr son prix forward. [Déf. 12]

## Forme
$$\mathrm{IV}=e^{-rT}\,g\big(\mathbb{E}(S_T)\big)$$ [Déf. 12]

## Ce que les symboles modélisent
$\mathrm{IV}$ est un montant d'aujourd'hui : la part du prix qui se calcule sans volatilité. [Déf. 12]

$g$ est un payoff qui ne dépend que de $S_T$, un cas du $G$ général ; pour le call, $g(x)=(x-K)^+$. L'espérance est prise sous $\mathbb{Q}$, si bien que $\mathbb{E}(S_T)$ est le prix forward. [§6.2, Prop. 6]

Ce n'est pas la « valeur intrinsèque » des salles de marché, $(S_0-K)^+$, le gain d'un exercice immédiat, qui est nulle pour le call à la monnaie de l'exemple ; celle du cours lit le payoff au forward et vaut 3,92. [ajout]

## Ce qui la définit
Le prix d'une option se coupe en deux : une part **connue sans modèle**, lue sur le prix forward, la valeur intrinsèque ; et un reste qui demande toute la loi de $S_T$, donc la volatilité. [Déf. 12, Déf. 13]

Le prix est l'espérance du payoff, actualisée ; la valeur intrinsèque, le payoff de l'espérance. Pour un payoff coudé comme le call, la moyenne des payoffs dépasse le payoff de la moyenne : c'est l'inégalité de Jensen. [§6.2, Déf. 13]

![Le payoff du call, lu de deux façons. Pour que l'écart se voie, la loi de $S_T$ est réduite à deux états équiprobables, 87,50 et 120,66, choisis pour le dessin : leur moyenne est le prix forward, 104,08, et le call y vaut 9,93 comme dans le modèle de Black et Scholes. Lu au forward, le payoff vaut 4,08, soit 3,92 actualisé : la valeur intrinsèque, qui ne demande que le forward. La moyenne des payoffs, sur la corde, vaut 10,33, soit 9,93 actualisé : le prix, qui demande la loi.](figures/valeur-intrinseque.svg) [ajout]

## Le chemin jusqu'ici
Deux fils y mènent. L'un va de fpp/replication-statique, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) à fpp/prix-a-terme, puis à fpp/mesure-risque-neutre, sous laquelle le prix forward est la moyenne de $S_T$ : c'est le point où l'on lit le payoff. L'autre est fpp/payoff, ce qu'on lit en ce point. [ajout]

## Exemple minimal
Call de strike 100, $\mathbb{E}^{\mathbb{Q}}(S_1)=104{,}08$, $P(0,1)=0{,}9608$ : $\mathrm{IV}=3{,}92$. [ajout]

## Geste de calcul type
Calculer d’abord le forward, y appliquer le payoff, puis actualiser — trois opérations, sans volatilité : $0{,}9608\times(104{,}08-100)=3{,}92$. Tout ce que la volatilité ajoute est la valeur temps. [Déf. 12, Déf. 13]

## Cesse d'être valide quand
Ce n’est un prix que dans un modèle sans aléa ; dès qu’il y a de la volatilité, il manque la valeur temps. [Déf. 13]

## Origine
- exercice fpp/ex-09 : la convexité donne prix ≥ valeur intrinsèque, mais l'écart n'est pas toujours strictement positif une fois le portage retiré — c'est la porte de l'exercice anticipé sur le change [exo. 9]

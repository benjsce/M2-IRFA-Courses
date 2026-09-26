---
id: pfo/passage-aux-rendements
nom: Passage aux rendements
type: principe
statut: source
construite_a_partir_de: []
alias:
- stationnarité des rendements
- from prices to returns
- formalisation des rendements
refs:
- §1.2
---

## Ce que c'est
On modélise les rendements et non les prix, parce que le prix suit un processus non stationnaire alors que ses rendements ont des propriétés statistiques stables dans le temps. [§1.2]

## Ce qui la définit
Non stationnaire veut dire que les propriétés statistiques du prix changent avec le temps. [§1.2]

Un prix qui passe de 100 à 1 000 en quelques années n'a ni le même niveau ni la même amplitude de variation au début et à la fin : une variation de 1 % y vaut 1 au départ et 10 à l'arrivée. Ses rendements du jour, eux, restent de l'ordre de quelques pour cent du premier au dernier jour : leurs propriétés restent invariantes, et c'est eux qu'on modélise. [§1.2, ajout]

![Un prix simulé sur 750 jours, de 100 à 1 000, et ses rendements du jour. À gauche, le niveau monte et les variations grandissent avec lui ; à droite, les rendements restent dans la même bande de quelques pour cent, du premier au dernier jour.](figures/passage-aux-rendements.svg) [ajout]

Deux façons de passer du prix au rendement coexistent, l'arithmétique et la logarithmique. Elles ne se comportent pas de la même façon quand on agrège, dans le temps ou entre actifs, et c'est ce qui les distingue. [§1.2.1, §1.2.2]

Tout ce que calcule ensuite le cours, moyennes, écarts types, corrélations, tests et mesures de risque, porte sur des rendements. [ajout]

## Cesse d'être valide quand
Le cours constate lui-même que la volatilité des rendements n'est pas constante et se regroupe par épisodes. [§1.4, §2.1.1]

Des rendements stationnaires en moyenne ne le sont donc pas forcément en variance : le passage aux rendements retire la tendance du prix, pas l'instabilité de sa dispersion. [ajout]

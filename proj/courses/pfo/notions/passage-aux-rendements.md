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
Le cours pose ce passage en ouverture de sa formalisation : l'évolution d'un prix est un processus stochastique non stationnaire, et c'est en passant aux rendements qu'on obtient des séries dont les propriétés statistiques restent invariantes dans le temps. [§1.2]

Deux façons de passer du prix au rendement coexistent, l'arithmétique et la logarithmique. Elles ne se comportent pas de la même façon quand on agrège, dans le temps ou entre actifs, et c'est là tout l'enjeu des deux premières sous-sections. [§1.2.1, §1.2.2]

Tout ce que calcule ensuite le cours, moyennes, écarts types, corrélations, tests et mesures de risque, porte sur des rendements. [ajout]

## Cesse d'être valide quand
Le cours constate lui-même que la volatilité des rendements n'est pas constante et se regroupe par épisodes. [§1.4, §2.1.1]

Des rendements stationnaires en moyenne ne le sont donc pas forcément en variance : le passage aux rendements retire la tendance du prix, pas l'instabilité de sa dispersion, et c'est ce que l'estimateur EWMA vient traiter. [ajout]

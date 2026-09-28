---
id: dup/sophistication
nom: Sophistication
type: notion
statut: source
construite_a_partir_de:
- dup/coherence-dynamique
- dup/actualisation-quasi-hyperbolique
alias:
- sophistication
- agent sophistiqué
- naïveté
- naivete
refs:
- L5 slide 25
---

## Ce que c'est
L'agent sait qu'il sera biaisé pour le présent demain aussi, et prévoit exactement ce que ses moi futurs feront. [L5 slide 25]

## Ce qui la définit
Aujourd'hui, l'agent de l'exemple compte attendre les 110 de la semaine 30 ; sophistiqué, il sait qu'à la semaine 26 il prendra les 100. Il ne fait donc pas de plan que ses moi futurs défont : il choisit en tenant leurs choix pour acquis. [L5 slide 20, L5 slide 25]

Ses choix se calculent par récurrence à rebours : on résout d'abord la dernière période, puis la précédente sachant la dernière, et ainsi jusqu'à aujourd'hui. [L5 slide 25]

L'agent **naïf**, au contraire, sous-estime le biais de ses moi futurs ; la source en réserve l'étude à un cours ultérieur, et suppose d'ici là la sophistication. [L5 slide 25]

## Le chemin jusqu'ici
dup/coherence-dynamique établit que l'agent changera d'avis, parce que le poids du présent qu'impose dup/biais-pour-le-present n'est pas celui de dup/actualisation-exponentielle. Les choix en cause restent ceux de dup/inversion-des-preferences-dans-le-temps, jugés par la stationnarité, dup/stationnarite, et par dup/invariance-temporelle. [L5 slide 22]

dup/actualisation-quasi-hyperbolique donne à ce changement une forme calculable, posée sur dup/utilite-actualisee avec des utilités de dup/fonction-utilite : chaque moi décote de $\beta$ tout ce qui n'est pas son présent. La sophistication dit ce que l'agent en sait. [L5 slide 25]

## Cesse d'être valide quand
L'agent se trompe sur son biais futur : ses moi futurs ne font pas ce qu'il avait prévu, et la récurrence à rebours ne décrit plus ses choix. [L5 slide 25]

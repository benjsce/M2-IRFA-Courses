---
id: dup/inversion-des-preferences-dans-le-temps
nom: Inversion des préférences dans le temps
type: notion
statut: source
construite_a_partir_de:
- dup/actualisation-exponentielle
alias:
- inversion temporelle des préférences
- money now or later
refs:
- L5 slide 2
- L5 slide 5
- L5 slide 7
- L5 slide 8
---

## Ce que c'est
Préférer le plus tôt de deux gains quand le plus tôt est immédiat, et le plus tard quand on recule les deux dates d'autant. [L5 slide 2]

## Ce qui la définit
Le choix typique : 100 aujourd'hui plutôt que 110 dans quatre semaines, mais 110 dans trente semaines plutôt que 100 dans vingt-six. Les deux choix offrent le même échange, quatre semaines d'attente contre 10 de plus ; seul l'éloignement change. [L5 slide 2]

Le même renversement vaut pour une peine : on repousse sept heures de travail pénible à huit heures la semaine prochaine, mais entre sept heures dans dix semaines et huit dans onze, on prend les sept. Et pour un plaisir : une pomme plutôt qu'une barre chocolatée si on la mange la semaine prochaine, la barre si on la mange tout de suite. [L5 slide 2, L5 slide 5]

Ces choix sont incompatibles avec l'actualisation exponentielle. En normalisant $u(0)=0$, le premier choix dit $u(100)>\delta^4u(110)$ ; multiplier par $\delta^{26}$ donne $\delta^{26}u(100)>\delta^{30}u(110)$, c'est-à-dire le choix inverse du second. [L5 slide 7, L5 slide 8]

## Le chemin jusqu'ici
dup/actualisation-exponentielle est le modèle mis à l'épreuve : il pèse une attente de quatre semaines par $\delta^4$, où qu'elle tombe, et ne peut donc pas trancher deux fois différemment le même échange. C'est ce que dup/fonction-utilite, qui évalue 100 et 110 de la même façon aux deux dates, laisse seul responsable du renversement : le poids des dates. [L5 slide 7, ajout]

## Cesse d'être valide quand
L'argument suppose qu'on ne peut ni emprunter ni prêter, qu'on croit au paiement futur, et qu'aucune autre consommation ne fait varier l'utilité marginale d'un euro d'une période à l'autre. La source juge ces hypothèses fortes, mais note que des expériences plus prudentes, sur des coûts et des gains datés, concluent de même. [L5 slide 2, L5 slide 7]

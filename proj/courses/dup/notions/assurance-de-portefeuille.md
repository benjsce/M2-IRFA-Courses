---
id: dup/assurance-de-portefeuille
nom: Assurance de portefeuille
type: notion
statut: source
construite_a_partir_de:
- dup/regroupement-des-etats
alias:
- portfolio insurance
- exposition à la hausse
- upside exposure
refs:
- L4 slide 32
---

## Ce que c'est
La forme que prend le paiement optimal quand les rangs extrêmes sont surpondérés : un plancher plat en bas, et davantage de richesse dans le meilleur état. [L4 slide 32]

## Ce qui la définit
Comparé à l'investisseur qui raisonne en utilité espérée, celui qui pondère par le rang relève sa richesse dans le pire état et dans le meilleur, et abaisse celle du milieu pour financer les deux mouvements. Le segment bas devenu plat ressemble à une assurance de portefeuille : une protection à la baisse. [L4 slide 32]

Ce qui mérite d'être retenu, c'est que les deux effets sont simultanés. La surpondération des queues produit la protection à la baisse et l'appétit pour les grands gains dans le même portefeuille, sans qu'il faille invoquer deux agents ni deux motifs. [L4 slide 32]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite portent dup/utilite-esperee, que dup/rdu déforme par le rang ; dup/poids-de-decision en donne le poids d'un état, dup/portefeuille-rdu le programme d'allocation, dup/prix-par-unite-de-poids sa condition du premier ordre, et dup/regroupement-des-etats la solution effective quand l'ordre se dérobe. [ajout]

Cette fiche ne calcule rien de plus : elle lit la solution obtenue. C'est sa raison d'exister — le résultat économique n'est pas dans la condition du premier ordre mais dans la forme du profil qu'elle dessine, et cette forme ne se voit qu'une fois le problème résolu jusqu'au bout. [ajout]

## Exemple minimal
Sur le marché du cours, $x^{\mathrm{EU}}=(0{,}328;0{,}903;1{,}577)$ devient $x^{\mathrm{RDU}}=(0{,}437;0{,}437;1{,}845)$ : plus haut dans le pire état et dans le meilleur, plus bas au milieu. [L4 slide 32]

![Les deux profils de richesse sur les trois états. En pointillé celui de l'utilité espérée, qui monte régulièrement ; en trait plein celui de la pondération par rang, dont le bas est plat et le haut plus élevé.](figures/assurance-de-portefeuille.svg) [ajout]

## Cesse d'être valide quand
La forme précise dépend des probabilités et des prix : le cours en montre un cas, pas une règle, et un autre marché pourrait donner un profil tout différent avec la même déformation. [L4 slide 32]

---
id: fpp/parcours-options
ordre: 6
titre: Ce que vaut le droit d'acheter
source: §6
---

## Point de départ
Un investisseur veut s'assurer le droit, mais pas l'obligation, d'acheter dans un an à 100 l'action qui vaut aujourd'hui 100. Combien doit-il payer ce droit ? [ajout]

## À savoir avant
- fpp/zero-coupon : il actualise le prix d'achat de 100 payé dans un an, ce qui relie le droit d'acheter au droit de vendre. [Déf. 3]
- fpp/probabilite-risque-neutre : elle dit quelle moyenne de l'action prendre, le prix forward, et qu'il faut l'actualiser pour obtenir un prix. [Prop. 6]
- fpp/modele-black-scholes : il fournit la loi du prix dans un an, contre laquelle on intègre le paiement du droit. [§5.4]
- fpp/prix-a-terme : tout sous-jacent a un prix à terme, et c'est lui qu'une seule formule prend en entrée. [§2, §3]

## Étapes
1. fpp/payoff
   Avant de lui donner un prix, que paie exactement ce droit dans un an, selon ce que vaudra l'action ? [Déf. 11]
   Histoire : « le droit, mais pas l'obligation » — Il paie $(S_T-100)^+$ : 20 si l'action finit à 120, rien si elle finit à 80, jamais un montant négatif, puisque l'investisseur n'achète que si cela l'arrange. [ajout]

2. fpp/option
   Comment s'appelle ce contrat, et qu'a-t-il de différent d'un achat à terme ? [Déf. 9]
   Histoire : « d'acheter dans un an à 100 » — C'est un call européen de strike 100 et de maturité un an ; à la différence d'un contrat à terme, il se paie à la signature. [ajout]

3. fpp/parite-call-put
   Si quelqu'un veut au contraire le droit de vendre au même prix, les deux droits sont-ils liés par une relation que personne ne peut contester ? [Prop. 7]
   Suite : Un autre investisseur veut, lui, le droit de vendre l'action à 100 dans un an. [ajout]
   Histoire : « le droit de vendre l'action à 100 dans un an » — Le call moins ce put vaut l'action moins le strike actualisé, $100-100\times0{,}9608=3{,}92$, quel que soit le modèle. [ajout]

4. fpp/valeur-intrinseque
   Si l'avenir était certain, combien vaudrait le droit d'acheter ? [Déf. 12]
   Histoire : « Combien doit-il payer ce droit » — Dans un monde sans aléa, l'action vaudrait à coup sûr son prix forward, 104,08 : le droit paierait 4,08 dans un an, soit 3,92 aujourd'hui. [ajout]

5. fpp/formule-black-scholes
   Quand l'action peut monter ou baisser, quel prix exact ? [§6.4]
   Suite : La volatilité de l'action est de 20 % par an, et le taux de 4 %. [ajout]
   Histoire : « La volatilité de l'action est de 20 % par an » — $d_1=0{,}30$ et $d_2=0{,}10$ ; le droit vaut $C=100\,N(0{,}30)-96{,}08\,N(0{,}10)=61{,}79-51{,}87=9{,}93$. [ajout]

6. fpp/valeur-temps
   D'où vient l'écart entre ce prix et ce que vaudrait le droit sans aléa ? [Déf. 13]
   Histoire : « Combien doit-il payer ce droit » — 9,93, dont 3,92 de valeur intrinsèque et 6,00 de valeur temps : ce que vaut l'aléa, positif parce que le paiement est convexe. [ajout]

7. fpp/option-americaine
   Pouvoir exercer avant l'échéance vaut-il un supplément ? [Déf. 10]
   Suite : Un vendeur lui propose le même droit, mais exerçable à tout moment pendant l'année. [ajout]
   Histoire : « exerçable à tout moment pendant l'année » — Pas sur cette action, qui ne verse pas de dividende : garder le call vaut toujours plus que l'exercer, et le droit américain vaut 9,93, comme l'européen. [ajout]

8. fpp/formule-de-black
   Faut-il une nouvelle formule pour chaque sous-jacent ? [§6.5]
   Suite : L'investisseur cherche enfin le même droit sur un contrat future dont le prix est 104,08. [ajout]
   Histoire : « un contrat future dont le prix est 104,08 » — Non : avec le prix à terme $F=104{,}08$ et le zéro-coupon, la formule de Black redonne 9,93 ; le taux est passé dans $F$. [ajout]

## Point d'arrivée
Le droit d'acheter l'action à 100 dans un an vaut 9,93 : 3,92 de valeur intrinsèque, 6,00 de valeur temps. Écrite sur le prix à terme, la même formule vaut pour tout sous-jacent. [ajout]

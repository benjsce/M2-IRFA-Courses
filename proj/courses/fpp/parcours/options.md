---
id: fpp/parcours-options
ordre: 6
titre: Ce que vaut le droit d'acheter
source: §6
---

## Point de départ
Un investisseur veut s'assurer le droit, mais pas l'obligation, d'acheter dans un an à 100 l'action qui vaut aujourd'hui 100. Dans un an, l'action vaudra peut-être 120, peut-être 80, et le droit lui rapportera un montant qui dépend de ce cours. La volatilité de l'action est de 20 % par an, et le taux de 4 %. Combien doit-il payer ce droit ? [ajout]

## À savoir avant
- fpp/zero-coupon : il actualise le prix d'achat de 100 payé dans un an, ce qui relie le droit d'acheter au droit de vendre. [Déf. 3]
- fpp/probabilite-risque-neutre : elle dit quelle moyenne de l'action prendre, le prix forward, et qu'il faut l'actualiser pour obtenir un prix. [Prop. 6]
- fpp/modele-black-scholes : il fournit la loi du prix dans un an, contre laquelle on intègre le paiement du droit. [§5.4]
- fpp/prix-a-terme : tout sous-jacent a un prix à terme, et c'est lui qu'une seule formule prend en entrée. [§2, §3]

## Étapes
1. fpp/payoff
   Avant de lui donner un prix, que paie exactement ce droit dans un an, selon ce que vaudra l'action ? [Déf. 11]
   Histoire : « un montant qui dépend de ce cours » — C'est le payoff du droit, $(S_T-100)^+$ : 20 si l'action finit à 120, rien si elle finit à 80, jamais un montant négatif, puisque l'investisseur n'achète que si cela l'arrange. [ajout]

2. fpp/option
   Comment s'appelle ce contrat, et qu'a-t-il de différent d'un achat à terme ? [Déf. 9]
   Histoire : « s'assurer le droit, mais pas l'obligation » — Un droit sans obligation, c'est une option ; celui d'acheter à 100 dans un an est un call européen de strike 100 et de maturité un an. À la différence d'un contrat à terme, qui oblige, il se paie à la signature. [ajout]

3. fpp/parite-call-put
   Le droit d'acheter a un symétrique : le droit de vendre au même prix. [Prop. 7]
   Suite : Un autre investisseur veut, lui, le droit de vendre l'action à 100 dans un an. Une banque achète le premier droit et vend le second : que détient-elle ? [ajout]
   Histoire : « achète le premier droit et vend le second » — Un achat à terme à 100 : si l'action finit au-dessus de 100, elle exerce son call ; en dessous, on exerce contre elle le put qu'elle a vendu. Dans les deux cas, elle achète l'action à 100 dans un an. Le call moins le put vaut donc l'action moins le strike actualisé, $100-100\times0{,}9608=3{,}92$, quel que soit le modèle. [ajout]

4. fpp/valeur-intrinseque
   Avant d'intégrer l'aléa, on peut regarder le cas où il n'y en aurait pas. [Déf. 12]
   Suite : Supposons un instant que l'action finisse à coup sûr à son prix forward, 104,08. Que vaudrait alors le droit aujourd'hui ? [ajout]
   Histoire : « Que vaudrait alors le droit aujourd'hui » — Il paierait 4,08 dans un an, puisqu'on achèterait à 100 une action valant 104,08, soit $4{,}08\times0{,}9608=3{,}92$ aujourd'hui : c'est sa valeur intrinsèque. Elle n'est pas nulle, bien que le strike égale le prix du jour, parce que le strike se compare au prix forward. [ajout]

5. fpp/formule-black-scholes
   Quand l'action peut monter ou baisser, quel prix exact ? [§6.4]
   Histoire : « Combien doit-il payer ce droit » — Avec 20 % de volatilité et 4 % de taux, $d_1=0{,}30$ et $d_2=0{,}10$ ; le droit vaut $C=100\,N(0{,}30)-96{,}08\,N(0{,}10)=61{,}79-51{,}87=9{,}93$. [ajout]

6. fpp/valeur-temps
   Le prix exact dépasse ce que vaudrait le droit sans aléa. [Déf. 13]
   Suite : L'investisseur paie 9,93, et non les 3,92 d'un avenir certain. Que paie-t-il en plus ? [ajout]
   Histoire : « Que paie-t-il en plus » — 6,00, l'écart entre 9,93 et 3,92 avant arrondi : la valeur temps du droit. Il la paie parce que l'action ne finira pas à coup sûr à 104,08 : plus haut, il gagne davantage ; plus bas, il n'exerce pas. Le droit profite des hausses sans subir les baisses, et cet aléa vaut quelque chose. [ajout]

7. fpp/option-americaine
   Pouvoir exercer avant l'échéance vaut-il un supplément ? [Déf. 10]
   Suite : Un vendeur lui propose le même droit, mais exerçable à tout moment pendant l'année. [ajout]
   Histoire : « exerçable à tout moment pendant l'année » — Pas sur cette action, qui ne verse pas de dividende : garder le call vaut toujours plus que l'exercer, et le droit américain vaut 9,93, comme l'européen. [ajout]

8. fpp/formule-de-black
   Chaque sous-jacent semblait demander sa propre formule. [§6.5]
   Suite : L'investisseur cherche enfin le même droit sur un contrat future dont le prix est 104,08. Peut-il le calculer avec le seul prix de ce future et le zéro-coupon ? [ajout]
   Histoire : « avec le seul prix de ce future et le zéro-coupon » — Oui : avec le prix à terme $F=104{,}08$ et le zéro-coupon, la formule de Black redonne 9,93 ; le taux est passé dans $F$. [ajout]

## Point d'arrivée
Le droit d'acheter l'action à 100 dans un an vaut 9,93 : 3,92 de valeur intrinsèque, 6,00 de valeur temps. Écrite sur le prix à terme, la même formule vaut pour tout sous-jacent. [ajout]

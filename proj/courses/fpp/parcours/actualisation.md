---
id: fpp/parcours-actualisation
ordre: 2
titre: Ce que vaut aujourd'hui une somme promise plus tard
source: §2.1, §2.2, §2.3
---

## Point de départ
Un épargnant place 1 euro à 5 % par an pendant deux ans. Une banque lui promet 1,10 à l'échéance, une autre 1,1025. Laquelle se trompe ? [ajout]

## Étapes
1. fpp/capitalisation
   Un taux annoncé suffit-il à dire ce que devient une somme placée ? [§2.1]
   Histoire : « place 1 euro à 5 % par an pendant deux ans » — Ce qu'il devient dépend du facteur de capitalisation, donc de la fréquence des intérêts : versés une fois au bout de deux ans, l'euro devient 1,10 ; versés chaque année, 1,1025. Aucune banque ne se trompe. Capitalisé en continu, l'euro deviendrait $e^{0,1}\approx1{,}1052$ ; c'est la convention que le cours retient. [ajout]

2. fpp/zero-coupon
   Quand chaque échéance a son propre prix, que vaut aujourd'hui un euro promis à une date donnée ? [Déf. 3]
   Suite : Sur le marché, un titre qui paie 1 dans un an coûte 0,9608 aujourd'hui, un titre qui paie 1 dans deux ans 0,9048. [ajout]
   Histoire : « un titre qui paie 1 dans deux ans 0,9048 » — C'est un zéro-coupon : $P(t,t+2)=0{,}9048$. Le marché ne donne pas un taux, il donne directement le prix de 1 à chaque date. [ajout]

3. fpp/taux-zero-coupon
   Comment relire un prix de zéro-coupon comme un taux qu'on puisse comparer à un autre ? [§2.3]
   Suite : L'épargnant voudrait comparer ces prix au 5 % de sa banque. [ajout]
   Histoire : « comparer ces prix au 5 % de sa banque » — $R=-\ln0{,}9048/2=5\,\%$ à deux ans, $-\ln0{,}9608=4\,\%$ à un an : sur deux ans, le marché paie les 5 % de sa banque, mais en capitalisation continue ; sur un an, il paie moins. [ajout]

4. fpp/courbe-des-taux
   Que dit l'ensemble de ces taux, rangés par échéance ? [Déf. 6]
   Suite : Chaque échéance a ainsi son taux. Comment les voir tous d'un coup ? [ajout]
   Histoire : « Comment les voir tous d'un coup » — En les portant en fonction de l'échéance : 4 % à un an et 5 % à deux ans sont deux points de la courbe des taux, ici croissante : immobiliser son argent plus longtemps rapporte davantage par an. [ajout]

5. fpp/valeur-actuelle-nette
   Un titre qui paie à plusieurs dates vaut-il la somme de ses paiements ? [Déf. 4]
   Suite : On propose à l'épargnant un titre qui paie 5 dans un an et 105 dans deux ans. Combien le payer ? [ajout]
   Histoire : « Combien le payer » — Chaque paiement au prix de son zéro-coupon, puis la somme : $5\times0{,}9608+105\times0{,}9048=4{,}80+95{,}01=99{,}81$. [ajout]

6. fpp/obligation-in-fine
   Pourquoi le prix d'une obligation s'écarte-t-il de ce qu'elle rembourse ? [Ex. 1]
   Suite : Ce titre est une obligation : un coupon de 5 % par an, un capital de 100 rendu à la fin. Si le marché était à 4 % actuariel pour toutes les durées, elle vaudrait 101,89. Pourquoi plus que ce qu'elle rembourse ? [ajout]
   Histoire : « un coupon de 5 % par an, un capital de 100 rendu à la fin » — C'est une obligation in fine. Son coupon, 5 %, paie davantage que le marché, 4 % : elle vaut plus que ce qu'elle rembourse, au-dessus du pair, $B(5\,\%,4\,\%)=1{,}0189$ pour 1 de nominal. [ajout]

7. fpp/duration
   De combien un prix bouge-t-il quand le taux bouge un peu ? [Déf. 5]
   Suite : Le lendemain, le taux à deux ans monte d'un point de base. Combien perd le zéro-coupon à deux ans ? [ajout]
   Histoire : « Combien perd le zéro-coupon à deux ans » — Environ $2\times0{,}9048\times0{,}0001\approx0{,}00018$, soit 0,02 % de son prix : deux fois la hausse du taux, parce qu'il reste deux ans jusqu'au paiement. [ajout]

## Point d'arrivée
Une somme future vaut son montant fois le zéro-coupon de sa date ; un titre, la somme de ses flux ainsi actualisés. Et plus un flux est lointain, plus son prix réagit à une variation de taux. [ajout]

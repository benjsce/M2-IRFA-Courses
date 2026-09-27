---
id: fpp/parcours-terme-action
ordre: 4
titre: Fixer aujourd'hui le prix d'une action livrée plus tard
source: §3, §4
---

## Point de départ
Un investisseur veut acheter dans un an une action qui cote aujourd'hui 100. Le zéro-coupon à un an vaut 0,9608. Un vendeur accepte de s'engager dès aujourd'hui sur un prix de livraison : lequel peut-il proposer sans perdre ? [ajout]

## À savoir avant
- fpp/zero-coupon : il donne le coût de l'argent emprunté pour acheter l'action aujourd'hui et la garder un an. [Déf. 3]
- fpp/absence-d-arbitrage : c'est lui qui interdit au vendeur comme à l'acheteur de s'assurer un gain certain sans mise, et qui fixe ainsi le prix. [Prop. 5]

## Étapes
1. fpp/cash-and-carry
   Comment le vendeur peut-il être sûr d'avoir l'action à livrer dans un an, et à quel coût ? [§3.1]
   Histoire : « lequel peut-il proposer sans perdre » — Le vendeur, lui, emprunte 100, achète l'action et la garde : dans un an, il livre l'action et doit 104,08. Tout prix au-dessus lui rapporterait un gain certain, tout prix en dessous une perte certaine. [ajout]

2. fpp/prix-forward
   Du côté de l'acheteur, quel prix de livraison est alors le seul possible ? [Déf. 8]
   Histoire : « un prix de livraison » — Un seul, ce que coûte au vendeur le cash-and-carry : $F(t,T)=100/0{,}9608=104{,}08$ ; l'écart de 4,08 avec le prix d'aujourd'hui, la base, est le coût du portage. [ajout]

3. fpp/dividendes-intermediaires
   Qui touche un dividende versé avant la livraison, et que devient le prix ? [§3.2]
   Suite : L'action versera dans six mois un dividende de 2 % de sa valeur forward. [ajout]
   Histoire : « un dividende de 2 % de sa valeur forward » — Le vendeur, qui porte l'action, le touche : 2,04 dans six mois, 2,08 une fois placés jusqu'à l'échéance. Le prix de livraison tombe à 102,00. [ajout]

4. fpp/prix-a-terme
   Le taux forward, le change à terme, le prix forward : trois réponses, ou un seul geste ? [§2, §3]
   Suite : L'investisseur se souvient des contrats du parcours précédent : le FRA à 6 %, le change à 1,1111. [ajout]
   Histoire : « le FRA à 6 %, le change à 1,1111 » — Pour l'action, $K$ payé dans un an vaut aujourd'hui $K\times0{,}9608$ et l'action reçue vaut 100 : les égaler, parce que le contrat ne coûte rien, redonne le prix forward, 104,08. Le FRA à 6 % et le change à 1,1111 sortaient du même geste, chaque jambe ramenée en t par le zéro-coupon de sa devise. [ajout]

5. fpp/contrat-future
   Qu'est-ce qui change quand le contrat se règle tous les jours plutôt qu'une fois ? [§4.1]
   Suite : En bourse, l'investisseur ne trouve pas de contrat forward sur l'action, mais un contrat future, dont le prix cote 104,08 et se règle chaque jour. [ajout]
   Histoire : « se règle chaque jour » — Si le prix future passe à 105,00 le lendemain, l'investisseur reçoit 0,92 tout de suite, au lieu d'attendre l'échéance. [ajout]

6. fpp/compte-capitalise
   Que devient une somme replacée période après période, quand on ne connaît que le taux de la première ? [§4.2.2]
   Suite : Chaque flux reçu doit être replacé jusqu'à l'échéance, aux taux courts qui seront ceux de chaque jour. [ajout]
   Histoire : « aux taux courts qui seront ceux de chaque jour » — Le facteur de ce replacement est le produit des zéro-coupons courts successifs : seul celui du premier jour est connu aujourd'hui. [ajout]

7. fpp/prix-future
   Le prix future est-il alors le même que le prix forward ? [Prop. 3]
   Histoire : « un contrat future, dont le prix cote 104,08 » — Tant que les taux sont connus d'avance, oui : le replacement n'a rien d'aléatoire, et le future vaut le forward, 104,08. Sinon, le future est le prix d'un paiement divisé par le compte capitalisé, et non par le zéro-coupon. [ajout]

## Point d'arrivée
Le prix de livraison d'une action est son prix comptant porté jusqu'à l'échéance, net des dividendes : 104,08, ou 102,00 avec le dividende. C'est le même geste que pour un taux ou un change, et un future ne s'en écarte que si les taux sont aléatoires. [ajout]

---
id: fpp/parcours-flux
ordre: 2
titre: Comparer des flux séparés par le temps ou la devise
source: poly, §2
---

## Point de départ
Vaut-il mieux recevoir 100 euros aujourd'hui, 104 dans un an, ou 100 dollars dans six mois ? Ces trois flux ne se comparent pas tels quels. [ajout]

## Étapes
1. fpp/coordonnees-flux
   Pourquoi ne se comparent-ils pas ? Parce qu'un flux n'est pas seulement un montant. [§2.1]
   Histoire : « Ces trois flux ne se comparent pas tels quels » — Chacun a trois coordonnées : 100, en euros, aujourd'hui ; 104, en euros, dans un an ; 100, en dollars, dans six mois. Deux flux ne se comparent qu'une fois ramenés à la même date et à la même devise. [ajout]

2. fpp/facteur-conversion
   Qu'est-ce qui permet alors de les mettre côte à côte ? Un même outil sert pour le temps et pour la devise. [§2.1, §2.4]
   Histoire : « Vaut-il mieux recevoir » — Pour mettre les 104 à côté des 100, on les multiplie par un nombre qui les ramène à aujourd'hui ; pour les dollars, par un nombre qui les convertit en euros. Le même outil, un facteur, sert aux deux passages. [ajout]

3. fpp/convention-capitalisation
   Pour le passage entre deux dates, ce nombre peut s'écrire de plusieurs façons, qu'il faut savoir traduire l'une dans l'autre. [§2.1]
   Suite : Le marché annonce un taux de 4 % par an pour placer un euro pendant un an. Quel facteur cette annonce donne-t-elle, puisqu'un taux peut s'entendre de plusieurs façons ? [ajout]
   Histoire : « un taux peut s'entendre de plusieurs façons » — En capitalisation linéaire, 4 % sur un an font d'un euro 1,04 ; en capitalisation continue, $e^{0{,}04}\approx1{,}0408$. Pour ramener les 104, il faut savoir laquelle le marché emploie. [ajout]

4. fpp/facteur-actualisation
   Quelle que soit l'écriture, l'objet est le même, et il a un prix de marché. [§2.1, Déf. 3]
   Histoire : « 104 dans un an » — Au taux continu de 4 %, un euro payé dans un an vaut aujourd'hui $P(t,t+1)=e^{-0{,}04}\approx0{,}9608$. Les 104 valent donc $104\times0{,}9608\approx99{,}92$ aujourd'hui, un peu moins que 100. [ajout]

5. fpp/valeur-actuelle-nette
   Avec ce prix, tout un échéancier de flux certains se ramène à un seul nombre. [Déf. 4]
   Suite : Un placement promet 100 dans un an et 100 dans deux ans ; le marché cote aujourd'hui 0,9608 un euro payé dans un an, et 0,9048 un euro payé dans deux ans. Que vaut le placement ? [ajout]
   Histoire : « Que vaut le placement » — Chaque flux est ramené par son propre facteur, puis on additionne : $100\times0{,}9608+100\times0{,}9048=186{,}56$. [ajout]

6. fpp/duration
   Cette valeur n'est pas figée : un gérant d'obligations veut savoir à quel point elle est exposée à un mouvement de la courbe. [Déf. 5]
   Histoire : « 100 dans deux ans » — Si le taux à deux ans monte d'un point, ce flux perd environ 2 % de sa valeur : sa sensibilité au taux est sa maturité, deux ans. Celui d'un an ne perd qu'environ 1 %. [ajout]

7. fpp/taux-zero-coupon
   Pour comparer des maturités différentes, le marché affiche ce prix sous une autre forme. [§2.3]
   Histoire : « 0,9048 un euro payé dans deux ans » — Des prix à un an et à deux ans se comparent mal. Réécrits en taux annualisés, ils deviennent $R(t,t+1)=4\,\%$ et $R(t,t+2)=-\ln(0{,}9048)/2\approx5\,\%$ : une courbe qui monte. [ajout]

8. fpp/taux-forward
   Cette courbe contient davantage que ce qu'elle affiche : on peut y lire le coût d'un emprunt qui ne commencera que plus tard. [§2.3]
   Suite : Une entreprise sait qu'elle devra emprunter dans un an, pour un an. Peut-elle fixer dès aujourd'hui le taux de cet emprunt ? [ajout]
   Histoire : « Peut-elle fixer dès aujourd'hui le taux de cet emprunt » — Oui : acheter un zéro-coupon à un an et vendre $0{,}9608/0{,}9048\approx1{,}0619$ zéro-coupons à deux ans ne coûte rien aujourd'hui, fait recevoir 1 dans un an et payer 1,0619 dans deux ans. Le taux ainsi verrouillé est $F(t,t+1,t+2)=\ln(0{,}9608/0{,}9048)\approx6\,\%$. [ajout]

9. fpp/taux-de-change
   Reste l'autre coordonnée, la devise, et le nombre qui fait passer de l'une à l'autre. [§2.4]
   Histoire : « 100 dollars dans six mois » — Pour les dollars, il faut une seconde conversion : le taux de change dit combien de dollars vaut un euro. Ramenés à aujourd'hui en dollars, puis divisés par ce taux, les 100 dollars deviennent des euros d'aujourd'hui, comparables aux deux autres flux. [ajout]

## Point d'arrivée
Deux flux se comparent une fois ramenés à la même date et à la même devise, par des facteurs que le marché cote : le facteur d'actualisation et le taux de change. [§2.1, §2.4]

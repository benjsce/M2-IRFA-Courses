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
   Histoire : « un taux peut s'entendre de plusieurs façons » — En capitalisation linéaire, où l'intérêt est versé une seule fois en fin de période, 4 % sur un an font d'un euro 1,04 ; en capitalisation continue, où l'intérêt est réinvesti à chaque instant, ils en font $e^{0{,}04}\approx1{,}0408$. Pour ramener les 104, il faut savoir laquelle le marché emploie. [ajout]

4. fpp/facteur-actualisation
   Quelle que soit l'écriture, l'objet est le même, et il a un prix de marché. [§2.1, Déf. 3]
   Histoire : « 104 dans un an » — Un euro payé dans un an vaut aujourd'hui ce qu'il faut placer pour l'obtenir : au taux continu de 4 %, l'inverse de $e^{0{,}04}$, soit $P(t,t+1)=e^{-0{,}04}\approx0{,}9608$. C'est le facteur d'actualisation. Les 104 valent donc $104\times0{,}9608\approx99{,}92$ aujourd'hui, un peu moins que 100. [ajout]

5. fpp/valeur-actuelle-nette
   Avec ce prix, tout un échéancier de flux certains se ramène à un seul nombre. [Déf. 4]
   Suite : Un placement promet 100 dans un an et 100 dans deux ans ; le marché cote aujourd'hui 0,9608 un euro payé dans un an, et 0,9048 un euro payé dans deux ans. Que vaut le placement ? [ajout]
   Histoire : « Que vaut le placement » — Chaque flux est ramené par son propre facteur, puis on additionne : $100\times0{,}9608+100\times0{,}9048=186{,}56$. [ajout]

6. fpp/duration
   Cette valeur n'est pas figée : un gérant d'obligations veut savoir à quel point elle est exposée à un mouvement de la courbe. [Déf. 5]
   Histoire : « 100 dans deux ans » — Ce flux est actualisé sur deux années, au même taux chaque année ; si ce taux monte d'un point, l'actualisation prend deux points de plus et le flux perd environ 2 % de sa valeur. Sa sensibilité au taux est donc sa maturité, deux ans ; celui d'un an ne perd qu'environ 1 %. [ajout]

7. fpp/taux-zero-coupon
   Pour comparer des maturités différentes, le marché affiche ce prix sous une autre forme. [§2.3]
   Histoire : « 0,9048 un euro payé dans deux ans » — Un titre qui verse un seul flux, 1 à une date fixée, s'appelle un zéro-coupon, et ces prix sont les siens. Des prix à un an et à deux ans se comparent mal ; on les réécrit en taux annualisé, le taux continu qui redonne le prix : $0{,}9048=e^{-2R}$ donne $R(t,t+2)=-\ln(0{,}9048)/2\approx5\,\%$, et de même $R(t,t+1)=4\,\%$. C'est le taux zéro-coupon, et sa courbe monte. [ajout]

8. fpp/taux-forward
   Cette courbe contient davantage que ce qu'elle affiche : on peut y lire le coût d'un emprunt qui ne commencera que plus tard. [§2.3]
   Suite : Une entreprise sait qu'elle devra emprunter dans un an, pour un an. Peut-elle fixer dès aujourd'hui le taux de cet emprunt ? [ajout]
   Histoire : « Peut-elle fixer dès aujourd'hui le taux de cet emprunt » — Oui. Un taux *forward*, « à terme » en français, est exactement cela : un taux convenu aujourd'hui pour une période qui ne commence que plus tard. La courbe de l'étape précédente suffit à le trouver. Placer pour deux ans d'un coup rapporte 5 % par an, soit 10 % sur les deux ans, puisqu'en capitalisation continue les taux s'ajoutent d'une année à l'autre. Placer un an à 4 %, puis un an au taux fixé aujourd'hui, doit rapporter autant, sinon on gagnerait sans risque à faire l'un et à défaire l'autre. Ce taux vaut donc $10\,\%-4\,\%=6\,\%$ : c'est le taux forward $F(t,t+1,t+2)$. Pour le verrouiller, l'entreprise achète aujourd'hui le zéro-coupon à un an, qui lui versera 1 dans un an, et paie ses 0,9608 en vendant des zéro-coupons à deux ans à 0,9048 pièce : il lui en faut $0{,}9608/0{,}9048\approx1{,}0619$, qu'elle remboursera dans deux ans. Elle reçoit 1 dans un an, rend 1,0619 un an plus tard, et $\ln1{,}0619\approx6\,\%$. [ajout]

9. fpp/taux-de-change
   Reste l'autre coordonnée, la devise, et le nombre qui fait passer de l'une à l'autre. [§2.4]
   Histoire : « 100 dollars dans six mois » — Pour les dollars, il faut une seconde conversion : le taux de change dit combien de dollars vaut un euro. Ramenés à aujourd'hui en dollars, puis divisés par ce taux, les 100 dollars deviennent des euros d'aujourd'hui, comparables aux deux autres flux. [ajout]

## Point d'arrivée
Deux flux se comparent une fois ramenés à la même date et à la même devise, par des facteurs que le marché cote : le facteur d'actualisation et le taux de change. [§2.1, §2.4]

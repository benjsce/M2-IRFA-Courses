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
   Commençons par le temps : quel nombre ramène les 104 à aujourd'hui ? Le marché ne le donne pas directement : il annonce un taux. [§2.1]
   Suite : Le marché annonce un taux de 4 % par an pour placer un euro pendant un an. Quel facteur cette annonce donne-t-elle, puisqu'un taux peut s'entendre de plusieurs façons ? [ajout]
   Histoire : « un taux peut s'entendre de plusieurs façons » — En capitalisation linéaire, où l'intérêt est versé une seule fois en fin de période, 4 % sur un an font d'un euro 1,04 ; en capitalisation continue, où l'intérêt est réinvesti à chaque instant, ils en font $e^{0{,}04}\approx1{,}0408$. Pour ramener les 104, il faut savoir laquelle le marché emploie. [ajout]

4. fpp/facteur-actualisation
   De ce taux, on tire enfin ce que valent aujourd'hui les 104. [§2.1, Déf. 3]
   Histoire : « 104 dans un an » — Un euro payé dans un an vaut aujourd'hui ce qu'il faut placer pour l'obtenir : au taux continu de 4 %, l'inverse de $e^{0{,}04}$, soit, en notant $t$ aujourd'hui, $P(t,t+1)=e^{-0{,}04}\approx0{,}9608$. C'est le facteur d'actualisation. Les 104 valent donc $104\times0{,}9608\approx99{,}92$ aujourd'hui, un peu moins que 100. [ajout]

5. fpp/valeur-actuelle-nette
   Et si l'on reçoit non pas un flux, mais plusieurs, à des dates différentes ? [Déf. 4]
   Suite : Un placement promet 100 dans un an et 100 dans deux ans ; le marché cote aujourd'hui 0,9608 un euro payé dans un an, et 0,9048 un euro payé dans deux ans. Que vaut le placement ? [ajout]
   Histoire : « Que vaut le placement » — Chaque flux est ramené par son propre facteur, puis on additionne : $100\times0{,}9608+100\times0{,}9048=186{,}56$. [ajout]

6. fpp/duration
   Cette valeur n'est pas figée : que perd le placement si les taux d'intérêt montent ? [Déf. 5]
   Histoire : « 100 dans deux ans » — Ce flux est actualisé sur deux années, au même taux chaque année ; si ce taux monte d'un point, l'actualisation prend deux points de plus et le flux perd environ 2 % de sa valeur. Sa sensibilité au taux est donc sa maturité, deux ans ; celui d'un an ne perd qu'environ 1 %, et le placement, qui les contient tous deux, entre 1 et 2 %. [ajout]

7. fpp/taux-zero-coupon
   0,9608 à un an, 0,9048 à deux ans : lequel de ces deux placements rapporte le plus, par an ? [§2.3]
   Histoire : « 0,9048 un euro payé dans deux ans » — Un titre qui verse un seul flux, 1 à une date fixée, s'appelle un zéro-coupon, et ces prix sont les siens. Des prix à un an et à deux ans se comparent mal ; on les réécrit en taux annualisé, le taux continu qui redonne le prix : $0{,}9048=e^{-2R}$ donne $R(t,t+2)=-\ln(0{,}9048)/2\approx5\,\%$, et de même $R(t,t+1)=4\,\%$. C'est le taux zéro-coupon, et sa courbe, tracée selon la maturité, monte. [ajout]

8. fpp/taux-forward
   Cette courbe contient davantage que ce qu'elle affiche : que dit-elle d'une année qui ne commence que dans un an ? [§2.3]
   Suite : Pour placer un euro pendant deux ans, on peut le placer d'un coup à 5 % par an, ou le placer un an à 4 % et le replacer pour la seconde année. Quel taux la seconde année devrait-elle offrir pour que les deux façons se valent ? [ajout]
   Histoire : « Quel taux la seconde année devrait-elle offrir » — En capitalisation continue, les taux s'ajoutent d'une année à l'autre : d'un coup, 5 % par an font 10 % sur les deux ans ; en deux temps, la première année apporte 4 %. La seconde doit donc apporter $10\,\%-4\,\%=6\,\%$. Ce taux s'appelle le taux *forward* de la seconde année, « à terme » en français, noté $F(t,t+1,t+2)$ : un taux qui porte sur une période future, mais qu'on calcule dès aujourd'hui, avec les seuls prix de l'étape précédente, $\ln(0{,}9608/0{,}9048)\approx6\,\%$. Ce n'est qu'un nombre lu dans la courbe : personne ne s'est encore engagé à le payer. [ajout]

9. fpp/taux-de-change
   Reste l'autre coordonnée, la devise, et le nombre qui fait passer de l'une à l'autre. [§2.4]
   Suite : Le dollar se place à 2 % par an, et un euro s'échange aujourd'hui contre 1,10 dollar. Que valent, en euros d'aujourd'hui, les 100 dollars dans six mois ? [ajout]
   Histoire : « Que valent, en euros d'aujourd'hui, les 100 dollars dans six mois » — Deux conversions, dans cet ordre. D'abord la date, dans la devise du flux : au taux dollar de 2 % continu, un dollar payé dans six mois vaut aujourd'hui $e^{-0{,}02\times0{,}5}\approx0{,}990$ dollar, donc les 100 dollars en valent 99,0 aujourd'hui. Ensuite la devise, au taux de change du jour, $X_t=1{,}10$ dollar pour un euro : $99{,}0/1{,}10=90{,}0$ euros. Le taux de change ne convertit que des montants de la même date ; celui qui s'appliquera dans six mois n'est pas connu aujourd'hui, c'est pourquoi on ramène d'abord les dollars à aujourd'hui. La question du départ est tranchée : 100 euros aujourd'hui, 99,92 pour les 104 dans un an, 90,0 pour les dollars. [ajout]

## Point d'arrivée
Deux flux se comparent une fois ramenés à la même date et à la même devise, par des facteurs que le marché cote : le facteur d'actualisation et le taux de change. [§2.1, §2.4]

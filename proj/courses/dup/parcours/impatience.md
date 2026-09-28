---
id: dup/parcours-impatience
ordre: 8
titre: Choisir entre aujourd'hui et plus tard
source: L5 slides 2–25
---

## Point de départ
On propose à quelqu'un 100 € tout de suite ou 110 € dans quatre semaines : il prend les 100. On lui propose aussi 100 € dans vingt-six semaines ou 110 € dans trente : il prend les 110. Les deux propositions offrent le même échange, quatre semaines d'attente contre 10 € de plus, et il les tranche en sens opposés. Comment la théorie standard pèse-t-elle des sommes reçues à des dates différentes, et que dit-elle de ces deux choix ? [L5 slide 2]

## À savoir avant
- dup/fonction-utilite : elle traduit chaque somme en utilité, la même à toutes les dates ; ici $u(x)=x$, et tout ce qui distingue les dates passe par leur poids. [L5 slide 6, L5 slide 14]

## Étapes
1. dup/actualisation-exponentielle
   Le modèle de référence pèse chaque date par un seul facteur, répété autant de fois qu'il y a de semaines d'attente. [L5 slide 6]
   Histoire : « Comment la théorie standard pèse-t-elle des sommes reçues à des dates différentes » — Elle multiplie l'utilité d'une somme reçue dans $t$ semaines par $\delta^t$ : 110 € dans quatre semaines valent $\delta^4\times110$ aujourd'hui. Prendre les 100 € tout de suite, c'est dire $100>\delta^4\times110$, donc $\delta^4<100/110\approx0{,}909$. [L5 slide 7]

2. dup/inversion-des-preferences-dans-le-temps
   Reste à confronter ce facteur au second choix. [L5 slide 7]
   Histoire : « il les tranche en sens opposés » — Pour le modèle, les deux propositions ne diffèrent que par un facteur $\delta^{26}$ qui multiplie les deux côtés : $100>\delta^4\times110$ entraîne $\delta^{26}\times100>\delta^{30}\times110$, et il devrait prendre les 100 € de la semaine 26. Il prend les 110 : aucun $\delta$ ne produit les deux choix à la fois. [L5 slide 7]

3. dup/utilite-actualisee
   Il faut desserrer le modèle, sans rien supposer d'abord de la forme des poids. [L5 slide 10]
   Suite : Laissons à chaque date son propre poids, quel qu'il soit. Comment s'écrivent alors les deux choix ? [ajout]
   Histoire : « Laissons à chaque date son propre poids » — 110 € dans quatre semaines valent $D(4)\times110$, 100 € tout de suite valent $D(0)\times100=100$. Le premier choix dit $100>D(4)\times110$, le second $D(26)\times100<D(30)\times110$ : deux inégalités sur quatre poids, que rien ne relie encore. [L5 slide 11]

4. dup/biais-pour-le-present
   Les deux inégalités portent sur des dates différentes, mais sur le même rapport $110/100$. [L5 slide 11]
   Suite : Que faut-il exiger de ces poids pour que les deux choix tiennent ensemble ? [ajout]
   Histoire : « Que faut-il exiger de ces poids » — En divisant, $D(0)/D(4)>1{,}1>D(26)/D(30)$ : les quatre semaines d'attente doivent coûter plus quand elles commencent aujourd'hui que quand elles commencent à la semaine 26. [L5 slide 11, L5 slide 12]

5. dup/actualisation-quasi-hyperbolique
   Beaucoup de poids satisfont cette condition ; le cours cherche le plus simple. [L5 slide 13]
   Suite : Quel modèle, le plus proche possible de l'exponentiel, reproduit les deux choix ? [ajout]
   Histoire : « le plus proche possible de l'exponentiel » — Il garde $\delta$, ici $\delta=1$, et décote de $\beta=\tfrac12$ tout ce qui n'est pas aujourd'hui. Tout de suite, $100>\tfrac12\times110=55$ : il prend les 100 €. À vingt-six semaines, $\tfrac12\times100=50<55$ : il prend les 110. Les deux choix sont reproduits. [L5 slide 14]

6. dup/actualisation-hyperbolique
   Ce modèle décote d'un coup tout le futur, puis plus rien. [L5 slide 15]
   Suite : Une autre personne préfère 100 € dans une semaine à 110 € dans cinq, mais 110 € dans trente semaines à 100 € dans vingt-six. Son impatience ne tombe pas seulement au premier pas : quelle actualisation lui faut-il ? [ajout]
   Histoire : « Son impatience ne tombe pas seulement au premier pas » — Le modèle quasi-hyperbolique pèse tout le futur du même $\tfrac12$ et lui ferait attendre les 110 € de la semaine 5. Avec $D(\tau)=1/(1+0{,}05\,\tau)$, où $\alpha=\gamma=0{,}05$ : $100/1{,}05=95{,}2$ contre $110/1{,}25=88{,}0$, elle prend les 100 € de la semaine 1 ; $100/2{,}3=43{,}5$ contre $110/2{,}5=44{,}0$, elle attend les 110 de la semaine 30. Le prix de l'attente baisse encore entre la semaine 1 et la semaine 26. [L5 slide 15, ajout]

7. dup/stationnarite
   Ces modèles expliquent les choix par des poids ; il reste à dire, sans aucun poids, ce que les choix eux-mêmes violent. [L5 slide 17]
   Histoire : « le même échange » — $(100,0)\succ_0(110,4)$ et $(100,26)\prec_0(110,30)$ : le même échange, reculé de 26 semaines et jugé le même jour, reçoit la réponse inverse. La stationnarité tombe, et avec elle tout modèle qui ne pèse que les délais. [L5 slide 17]

8. dup/invariance-temporelle
   La stationnarité ne compare que des choix faits le même jour. [L5 slide 18]
   Suite : Vingt-six semaines passent, et l'on repose la question telle qu'elle se présente alors : 100 € tout de suite ou 110 € dans quatre semaines. Répond-il comme il l'aurait fait aujourd'hui ? [ajout]
   Histoire : « Répond-il comme il l'aurait fait aujourd'hui » — Oui : il prend les 100. La décision et les deux gains ont reculé ensemble de 26 semaines, $(100,0)\succ_0(110,4)$ et $(100,26)\succ_{26}(110,30)$ : ses choix sont les mêmes à la même distance du présent. [L5 slide 18, L5 slide 20]

9. dup/coherence-dynamique
   Or, ce jour-là, les 100 € tout de suite sont les 100 € de la semaine 26 qu'il avait refusés. [L5 slide 20]
   Suite : Aujourd'hui, il comptait attendre les 110 € de la semaine 30. Arrivé à la semaine 26, il prend les 100 : que devient le plan qu'il avait fait ? [ajout]
   Histoire : « que devient le plan qu'il avait fait » — Il est renversé : $(100,26)\prec_0(110,30)$, mais $(100,26)\succ_{26}(110,30)$. C'était forcé : garder l'invariance temporelle et la cohérence dynamique ensemble rendrait ses choix stationnaires, et ils ne le sont pas. Ce qui cède, c'est la cohérence, et le biais pour le présent en est la cause. [L5 slide 21, L5 slide 22]

10. dup/sophistication
   Le moi de la semaine 26 défait ce que le moi d'aujourd'hui avait prévu. [L5 slide 25]
   Suite : Supposons qu'il se connaisse bien. Comment choisit quelqu'un qui sait qu'il changera d'avis ? [ajout]
   Histoire : « qui sait qu'il changera d'avis » — Il ne compte plus sur les 110 € : il sait qu'à la semaine 26 il prendra les 100, et fait ses plans en partant de ce que fera ce moi-là, en remontant le temps. Le cours suppose désormais cet agent sophistiqué ; l'agent naïf, qui se croit plus patient demain qu'il ne le sera, attend un cours ultérieur. [L5 slide 25]

## Point d'arrivée
Des choix ordinaires, prendre l'argent tout de suite mais attendre quand tout est lointain, écartent l'actualisation exponentielle et imposent un biais pour le présent. Ce biais fait de l'agent une suite de moi qui ne s'accordent pas, et qu'un agent sophistiqué prend pour tels en choisissant. [ajout]

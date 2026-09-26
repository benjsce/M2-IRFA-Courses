---
id: fpp/parcours-couverture
ordre: 6
titre: Couvrir une option en continu
source: poly, §7–§8
---

## Point de départ
Une banque vend à l'investisseur le call à un an de strike 100 sur l'action à 100 : elle encaisse 9,93. Si l'action monte, elle devra la lui vendre à 100, quel que soit son prix ; or elle ne veut pas parier sur l'action. Comment neutraliser ce risque, et combien cela lui coûte-t-il ? [ajout]

## À savoir avant
- fpp/modele-black-scholes : c'est la dynamique du sous-jacent sur laquelle on écrit la variation du prix de l'option. [§7.1]
- fpp/replication-dynamique : c'est le principe de la couverture : réajuster le portefeuille à chaque pas pour reproduire le payoff. [§7.1]
- fpp/formule-black-scholes : c'est le prix qu'on dérive pour obtenir chaque sensibilité. [§8.2]

## Étapes
1. fpp/couverture
   La banque perd si l'action monte. Que peut-elle faire contre ? [§8]
   Histoire : « Comment neutraliser ce risque » — Prendre la position opposée. Le call vendu lui fait perdre quand l'action monte ; elle achète donc des actions, qui lui font gagner quand l'action monte. Reste à savoir combien. [ajout]

2. fpp/sensibilite
   Combien d'actions ? Cela dépend de la façon dont le call réagit à chacun de ses ingrédients. [§8.1]
   Histoire : « elle ne veut pas parier sur l'action » — Le prix du call dépend du cours de l'action, de sa volatilité, du temps qui reste et du taux. Chaque dépendance se mesure par une dérivée : de combien le prix bouge quand ce paramètre bouge un peu, les autres restant fixes. C'est une sensibilité, et la banque en aura une à surveiller par risque. [ajout]

3. fpp/delta
   La première, et la plus importante : celle au cours de l'action, qui dit combien d'actions acheter. [§8.2]
   Histoire : « Si l'action monte » — Le delta dit de combien le prix du call bouge quand l'action monte d'un euro. La formule de Black et Scholes le donne, $\delta=N(d_1)$, où $N$ est la fonction de répartition de la loi normale et $d_1$ la quantité qui apparaît dans la formule du prix, ici $d_1=\big(\ln(100/100)+0{,}04+0{,}2^2/2\big)/0{,}2=0{,}3$ : $\delta\approx0{,}618$. La banque achète donc 0,618 action par call vendu : si l'action monte d'un euro, le call vendu lui coûte environ 0,618 de plus, et ses actions lui rapportent autant. [ajout]

4. fpp/gamma
   Cette quantité d'actions ne reste pas juste longtemps. À quelle vitesse faut-il la corriger ? [§8.2]
   Suite : Le lendemain, l'action passe de 100 à 101. La couverture est-elle toujours juste ? [ajout]
   Histoire : « La couverture est-elle toujours juste » — Non : le delta passe de 0,618 à 0,637, et la banque doit acheter environ 0,019 action de plus. Ce rythme de correction est le gamma ; plus il est grand, plus il faut réajuster souvent. [ajout]

5. fpp/vega
   L'action n'est pas le seul risque : l'incertitude elle-même peut changer. [§8.2]
   Suite : Le marché devient plus nerveux : la volatilité passe de 20 % à 21 %. Que perd la banque, qui a vendu le call ? [ajout]
   Histoire : « Que perd la banque, qui a vendu le call » — Le call passe de 9,93 à environ 10,31 : la banque perd environ 0,38 par point de volatilité, et ses actions n'y changent rien. Seule une autre option peut couvrir ce risque. [ajout]

6. fpp/theta
   Même si rien ne change, l'échéance approche, et la position en est affectée. [§8.2]
   Suite : Supposons que rien ne bouge jusqu'à l'échéance : l'action reste à 100. Que devient le call vendu ? [ajout]
   Histoire : « Que devient le call vendu » — Il ne vaut plus rien à l'échéance, puisque l'action finit au strike : jour après jour, le seul passage du temps a fait baisser son prix. C'est le theta, et la banque, qui a vendu le call, en profite. [ajout]

7. fpp/rho
   Reste le financement : le taux d'intérêt entre dans le prix par l'actualisation du strike. [§8.2]
   Suite : La banque centrale baisse les taux de 4 % à 3 %. Qu'y perd ou qu'y gagne la banque ? [ajout]
   Histoire : « Qu'y perd ou qu'y gagne la banque » — Le strike actualisé passe de 96,08 à 97,04 : payer 100 dans un an coûte plus cher aujourd'hui, et le call perd de sa valeur. La banque, qui l'a vendu, y gagne. [ajout]

8. fpp/edp-black-scholes
   Si la banque réajuste sa couverture à chaque instant, que cela dit-il du prix du call ? [§7.1]
   Histoire : « combien cela lui coûte-t-il » — Couverte en continu, sa position ne dépend plus de l'action : elle est sans risque, et doit donc rapporter exactement le taux sans risque, sinon on gagnerait sans risque. Écrite à chaque instant et pour chaque cours, cette exigence devient une équation que le prix du call, fonction du temps et du cours, doit satisfaire, avec au bout le paiement $(S_T-100)^+$ : l'équation aux dérivées partielles de Black et Scholes. [ajout]

9. fpp/feynman-kac
   Le prix du call avait été obtenu autrement, comme une moyenne sous la probabilité risque-neutre. Les deux méthodes s'accordent-elles ? [§7.2.1]
   Histoire : « elle encaisse 9,93 » — Oui : le théorème de Feynman et Kac dit que l'espérance risque-neutre actualisée du paiement est la solution de cette équation. Les 9,93 encaissés sont donc exactement ce que coûte la couverture continue : c'est la réponse à la seconde question de la banque. [ajout]

10. fpp/equation-de-la-chaleur
    Reste à résoudre l'équation elle-même. [§7.2.2]
    Histoire : « le call à un an de strike 100 » — On change de variables : le logarithme du cours à la place du cours, et l'on retire l'actualisation en multipliant par $e^{r(T-t)}$, qui vaut 1,0408 à un an et 4 %. L'équation devient celle de la chaleur, que les physiciens savent résoudre, et sa solution redonne la formule de Black et Scholes. [ajout]

## Point d'arrivée
Le prix d'une option est le coût de sa couverture continue, et chaque sensibilité dit une position à tenir en sens inverse pour neutraliser un risque. [§7.1, §8.2]

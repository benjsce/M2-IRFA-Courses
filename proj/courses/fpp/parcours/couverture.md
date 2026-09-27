---
id: fpp/parcours-couverture
ordre: 7
titre: Vendre une option sans parier sur l'action
source: §7, §8
---

## Point de départ
Une banque a vendu 100 calls de strike 100 à un an sur l'action qui vaut 100, au prix de 9,93 chacun. Si l'action monte, elle perd. Comment se protéger sans renoncer à la vente ? [ajout]

## À savoir avant
- fpp/valeur-temps : elle décompose le prix de 9,93 en valeur intrinsèque et valeur temps ; les sensibilités que la banque va surveiller portent sur ces deux parts. [Déf. 13, §8.2]
- fpp/modele-black-scholes : il dit comment l'action bouge d'un instant à l'autre, et c'est cette dynamique que la banque propage au prix de ses calls. [§5.4]

## Étapes
1. fpp/couverture
   Que faut-il détenir à côté de ce qu'on a vendu pour que les deux variations s'annulent ? [§8]
   Histoire : « Comment se protéger » — En détenant des actions : quand l'action monte, leur gain compense la perte sur les calls vendus. [ajout]

2. fpp/delta
   Combien d'actions exactement ? [§8.2]
   Histoire : « Une banque a vendu 100 calls » — Autant que la pente du prix du call : $\delta=N(0{,}30)=0{,}618$ par call, soit 61,8 actions pour les 100 calls. [ajout]

3. fpp/grecque
   Le prix de l'action est-il le seul risque de la banque ? [§8.2]
   Histoire : « Si l'action monte, elle perd » — Pas seulement : vendeuse de 100 calls, la banque perd aussi si le marché anticipe une volatilité plus forte ou si le taux monte, et gagne à chaque jour qui passe. Chacun de ces risques se mesure, comme celui de l'action par le delta, par une dérivée du prix du call. [ajout]

4. fpp/gamma
   Les actions achetées la veille suffisent-elles encore quand l'action a bougé ? [§8.2]
   Suite : Le lendemain, l'action vaut 101. [ajout]
   Histoire : « Le lendemain, l'action vaut 101 » — Le delta est passé d'environ 0,618 à 0,637, parce que $\gamma=0{,}019$ : la banque doit racheter 1,9 action. [ajout]

5. fpp/vega
   Que coûte à la banque une erreur sur la volatilité ? [§8.2]
   Suite : Le marché se met à anticiper une volatilité de 21 % au lieu de 20 %. [ajout]
   Histoire : « une volatilité de 21 % au lieu de 20 % » — Chaque call vaut environ 0,38 de plus : la banque, vendeuse, perd 38 sur ses 100 calls, et les actions n'y changent rien. [ajout]

6. fpp/theta
   Le temps qui passe, à lui seul, change-t-il la valeur de ce qui a été vendu ? [§8.2]
   Suite : Une journée passe sans que rien d'autre ne bouge. [ajout]
   Histoire : « Une journée passe sans que rien d'autre ne bouge » — Chaque call perd environ 0,023 ; pour la banque, qui les a vendus, c'est un gain de 2,3. [ajout]

7. fpp/rho
   Et si c'est le taux qui bouge ? [§8.2]
   Suite : La banque centrale relève le taux d'un point, de 4 % à 5 %. [ajout]
   Histoire : « de 4 % à 5 % » — Chaque call gagne environ 0,52 : la banque perd 52 sur ses 100 calls. [ajout]

8. fpp/formule-d-ito
   Comment écrire la variation d'une fonction du prix de l'action, qui est aléatoire ? [§7.1]
   Suite : La banque veut savoir comment le prix d'un call varie d'un instant à l'autre, quand l'action suit le modèle de Black et Scholes. [ajout]
   Histoire : « comment le prix d'un call varie d'un instant à l'autre » — Par la formule d'Itô : une dérive, où la courbure apporte $\tfrac12\sigma^2S^2\gamma$, et un bruit proportionnel au delta, celui-là même que les actions compensent. [ajout]

9. fpp/edp-black-scholes
   Couverte à chaque instant, la position porte-t-elle encore un risque, et que doit-elle rapporter ? [§7.1]
   Histoire : « sans renoncer à la vente » — La banque garde ses calls vendus ; couverte en continu, sa position n'a plus de bruit : elle doit rapporter le taux sans risque, et le prix du call vérifie une équation : son thêta, $-5{,}89$, plus $rS\delta=2{,}47$, plus le terme de courbure $\tfrac12\sigma^2S^2\gamma=3{,}81$, donne $0{,}40=4\,\%\times9{,}93$. [ajout]

10. fpp/feynman-kac
    Cette équation redonne-t-elle le prix de 9,93, obtenu jusqu'ici par une espérance ? [§7.2]
    Histoire : « au prix de 9,93 chacun » — Oui : sa solution est l'espérance risque-neutre actualisée du paiement, 9,93. La couverture et l'espérance mènent au même prix. [ajout]

## Point d'arrivée
La banque couvre ses calls avec 61,8 actions, qu'elle ajuste à mesure que l'action bouge ; restent à surveiller la volatilité, le temps et le taux. Couverte en continu, sa position ne rapporte que le taux sans risque, et c'est ce qui justifie le prix de 9,93. [ajout]

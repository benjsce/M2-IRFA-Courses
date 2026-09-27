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
   Détenir des actions, soit ; reste à dire combien. [§8.2]
   Suite : Combien d'actions doit-elle détenir pour ses 100 calls ? [ajout]
   Histoire : « Combien d'actions doit-elle détenir » — Autant que la pente du prix du call : $\delta=N(0{,}30)=0{,}618$ par call, soit 61,8 actions pour les 100 calls. [ajout]

3. fpp/grecque
   L'action n'est pas le seul paramètre du prix d'un call. [§8.2]
   Suite : Mais l'action n'est pas seule à faire bouger le prix des calls vendus. Comment mesurer ce que chacun de ces paramètres coûte à la banque ? [ajout]
   Histoire : « ce que chacun de ces paramètres coûte à la banque » — Par une dérivée du prix du call, une par paramètre, comme le delta pour l'action. Vendeuse de 100 calls, la banque perd si le marché anticipe une volatilité plus forte ou si le taux monte, et gagne à chaque jour qui passe. [ajout]

4. fpp/gamma
   La couverture est calculée pour le prix du jour ; le prix, lui, bouge. [§8.2]
   Suite : Le lendemain, l'action vaut 101. De combien sa couverture doit-elle bouger ? [ajout]
   Histoire : « De combien sa couverture doit-elle bouger » — Le delta est passé d'environ 0,618 à 0,637, parce que $\gamma=0{,}019$ : la banque doit racheter 1,9 action. [ajout]

5. fpp/vega
   La volatilité n'est pas observée : le marché l'anticipe, et peut changer d'avis. [§8.2]
   Suite : Le marché se met à anticiper une volatilité de 21 % au lieu de 20 %. Que coûte ce point de volatilité à la banque ? [ajout]
   Histoire : « Que coûte ce point de volatilité à la banque » — Chaque call vaut environ 0,38 de plus : la banque, vendeuse, perd 38 sur ses 100 calls, et les actions n'y changent rien. [ajout]

6. fpp/theta
   Même sans aucun mouvement de marché, le temps passe. [§8.2]
   Suite : Une journée passe sans que rien d'autre ne bouge. Que rapporte ce jour à la banque ? [ajout]
   Histoire : « Que rapporte ce jour à la banque » — Chaque call perd environ 0,023 ; pour la banque, qui les a vendus, c'est un gain de 2,3. [ajout]

7. fpp/rho
   Dernier paramètre du prix : le taux. [§8.2]
   Suite : La banque centrale relève le taux d'un point, de 4 % à 5 %. Que coûte ce point de taux à la banque ? [ajout]
   Histoire : « Que coûte ce point de taux à la banque » — Chaque call gagne environ 0,52 : la banque perd 52 sur ses 100 calls. [ajout]

8. fpp/formule-d-ito
   Comment écrire la variation d'une fonction du prix de l'action, qui est aléatoire ? [§7.1]
   Suite : La banque veut savoir comment le prix d'un call varie d'un instant à l'autre, quand l'action suit le modèle de Black et Scholes. [ajout]
   Histoire : « comment le prix d'un call varie d'un instant à l'autre » — Par la formule d'Itô : une dérive, où la courbure apporte $\tfrac12\sigma^2S^2\gamma$, et un bruit proportionnel au delta, celui-là même que les actions compensent. [ajout]

9. fpp/edp-black-scholes
   La banque se couvre maintenant à chaque instant. [§7.1]
   Suite : Couverte en continu, la position de la banque ne porte plus de risque. Quelle équation le prix du call doit-il alors vérifier ? [ajout]
   Histoire : « Quelle équation le prix du call doit-il alors vérifier » — Sans bruit, la position doit rapporter le taux sans risque ; le prix du call vérifie donc une équation : son thêta, $-5{,}89$, plus $rS\delta=2{,}47$, plus le terme de courbure $\tfrac12\sigma^2S^2\gamma=3{,}81$, donne $0{,}40=4\,\%\times9{,}93$. [ajout]

10. fpp/feynman-kac
    Le prix de 9,93 venait jusqu'ici d'une espérance, pas d'une équation. [§7.2]
    Suite : La banque a vendu ses calls à 9,93, le prix que donne l'espérance risque-neutre. L'équation donne-t-elle le même prix ? [ajout]
    Histoire : « L'équation donne-t-elle le même prix » — Oui : sa solution est l'espérance risque-neutre actualisée du paiement, 9,93. La couverture et l'espérance mènent au même prix. [ajout]

## Point d'arrivée
La banque couvre ses calls avec 61,8 actions, qu'elle ajuste à mesure que l'action bouge ; restent à surveiller la volatilité, le temps et le taux. Couverte en continu, sa position ne rapporte que le taux sans risque, et c'est ce qui justifie le prix de 9,93. [ajout]

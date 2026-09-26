---
id: fpp/parcours-couverture
ordre: 6
titre: Couvrir une option en continu
source: poly, §7–§8
---

## Point de départ
Une banque vend un call à un an de strike 100 sur l'action à 100 : elle encaisse 9,93 et ne veut pas parier sur l'action. Comment neutraliser son risque, et combien cela lui coûte-t-il de le faire à chaque instant ? [ajout]

## À savoir avant
- fpp/modele-black-scholes : c'est la dynamique du sous-jacent sur laquelle on écrit la variation du prix de l'option. [§7.1]
- fpp/replication-dynamique : c'est le principe de la couverture : réajuster le portefeuille à chaque pas pour reproduire le payoff. [§7.1]
- fpp/mesure-risque-neutre : c'est l'autre façon de trouver le prix, par une espérance, que le parcours relie à l'équation. [§7.2.1]
- fpp/formule-black-scholes : c'est le prix qu'on dérive pour obtenir chaque sensibilité. [§8.2]

## Étapes
1. fpp/edp-black-scholes
   Si la banque peut réajuster sa couverture en continu, le prix de l'option doit obéir à une contrainte précise. [§7.1]
   Histoire : « de le faire à chaque instant » — Si la banque détient à chaque instant la bonne quantité d'actions, et la réajuste en continu, son portefeuille devient sans risque et doit rapporter le taux sans risque. Cette contrainte s'écrit comme une équation que le prix du call, fonction du temps et du cours, doit satisfaire, avec au bout le paiement $(S_T-100)^+$. [ajout]

2. fpp/feynman-kac
   Cette contrainte et l'espérance risque-neutre sont-elles deux réponses différentes ? Non, et un théorème le montre. [§7.2.1]
   Histoire : « elle encaisse 9,93 » — Ce prix avait été obtenu comme une espérance risque-neutre actualisée. Le théorème de Feynman et Kac dit que cette espérance est aussi la solution de l'équation : les deux chemins mènent au même 9,93. [ajout]

3. fpp/equation-de-la-chaleur
   Par quelques changements de variables, l'équation devient un objet que les physiciens savent résoudre. [§7.2.2]
   Histoire : « un call à un an de strike 100 » — Pour résoudre l'équation, on change de variables : le logarithme du cours à la place du cours, et l'on retire l'actualisation par le facteur $e^{r(T-t)}$, qui vaut 1,0408 à un an et 4 %. L'équation devient celle de la chaleur, dont on connaît la solution. [ajout]

4. fpp/couverture
   Revenons à la banque : le principe général de la neutralisation d'un risque. [§8]
   Histoire : « Comment neutraliser son risque » — Se couvrir, c'est prendre la position opposée à ce qui expose : la banque a vendu le call, qui gagne quand l'action monte ; elle achète donc de l'action, dans la quantité qui annule cette dépendance. [ajout]

5. fpp/sensibilite
   Neutraliser un risque demande de mesurer à quel point la position y est exposée, paramètre par paramètre. [§8.1]
   Histoire : « ne veut pas parier » — Le prix du call dépend de plusieurs paramètres : le cours de l'action, sa volatilité, le temps qui reste, le taux. Pour ne parier sur aucun, la banque mesure, paramètre par paramètre, de combien le prix bouge quand il bouge. [ajout]

6. fpp/delta
   Le paramètre qui compte le plus est le cours de l'action : c'est lui qui dit combien d'actions détenir. [§8.2]
   Histoire : « ne veut pas parier sur l'action » — Pour ne plus dépendre du cours, la banque achète $\delta=N(0{,}3)\approx0{,}618$ action par call vendu : si l'action monte d'un euro, le call vendu lui coûte environ 0,618 de plus, et les actions lui rapportent autant. [ajout]

7. fpp/gamma
   Cette quantité d'actions ne reste pas juste longtemps. À quelle vitesse faut-il la corriger ? [§8.2]
   Suite : Le lendemain, l'action passe de 100 à 101. La couverture est-elle toujours juste ? [ajout]
   Histoire : « La couverture est-elle toujours juste » — Non : le delta passe de 0,618 à 0,637, et la banque doit acheter environ 0,019 action de plus. Ce rythme de correction est le gamma ; plus il est grand, plus il faut réajuster souvent. [ajout]

8. fpp/vega
   L'action n'est pas le seul risque : l'incertitude elle-même peut changer. [§8.2]
   Suite : Le marché devient plus nerveux : la volatilité passe de 20 % à 21 %. Que perd la banque, qui a vendu le call ? [ajout]
   Histoire : « Que perd la banque, qui a vendu le call » — Le call passe de 9,93 à environ 10,31 : la banque perd environ 0,38 par point de volatilité, et ses actions n'y changent rien. Seule une autre option peut couvrir ce risque. [ajout]

9. fpp/theta
   Même si rien ne change, l'échéance approche, et la position en est affectée. [§8.2]
   Suite : Supposons que rien ne bouge jusqu'à l'échéance : l'action reste à 100. Que devient le call vendu ? [ajout]
   Histoire : « Que devient le call vendu » — Il ne vaut plus rien à l'échéance, puisque l'action finit au strike : jour après jour, le seul passage du temps a fait baisser son prix. C'est le theta, et la banque, qui a vendu le call, en profite. [ajout]

10. fpp/rho
    Reste le financement : le taux d'intérêt entre dans le prix par l'actualisation du strike. [§8.2]
    Suite : La banque centrale baisse les taux de 4 % à 3 %. Qu'y perd ou qu'y gagne la banque ? [ajout]
    Histoire : « Qu'y perd ou qu'y gagne la banque » — Le strike actualisé passe de 96,08 à 97,04 : payer 100 dans un an coûte plus cher aujourd'hui, et le call perd de sa valeur. La banque, qui l'a vendu, y gagne. [ajout]

## Point d'arrivée
Le prix d'une option est le coût de sa couverture continue, et chaque sensibilité dit une position à tenir en sens inverse pour neutraliser un risque. [§7.1, §8.2]

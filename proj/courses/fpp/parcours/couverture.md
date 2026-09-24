---
id: fpp/parcours-couverture
ordre: 6
titre: Couvrir une option en continu
source: poly, §7–§8
---

## Point de départ
Une banque vend un call et ne veut pas parier sur l'action. Comment neutraliser son risque, et combien cela lui coûte-t-il de le faire à chaque instant ? [ajout]

## À savoir avant
- fpp/modele-black-scholes : c'est la dynamique du sous-jacent sur laquelle on écrit la variation du prix de l'option. [§7.1]
- fpp/replication-dynamique : c'est le principe de la couverture : réajuster le portefeuille à chaque pas pour reproduire le payoff. [§7.1]
- fpp/mesure-risque-neutre : c'est l'autre façon de trouver le prix, par une espérance, que le parcours relie à l'équation. [§7.2.1]
- fpp/formule-black-scholes : c'est le prix qu'on dérive pour obtenir chaque sensibilité. [§8.2]

## Étapes
1. fpp/edp-black-scholes
   Si la banque peut réajuster sa couverture en continu, le prix de l'option doit obéir à une contrainte précise. [§7.1]

2. fpp/feynman-kac
   Cette contrainte et l'espérance risque-neutre sont-elles deux réponses différentes ? Non, et un théorème le montre. [§7.2.1]

3. fpp/equation-de-la-chaleur
   Par quelques changements de variables, l'équation devient un objet que les physiciens savent résoudre. [§7.2.2]

4. fpp/couverture
   Revenons à la banque : le principe général de la neutralisation d'un risque. [§8]

5. fpp/sensibilite
   Neutraliser un risque demande de mesurer à quel point la position y est exposée, paramètre par paramètre. [§8.1]

6. fpp/delta
   Le paramètre qui compte le plus est le cours de l'action : c'est lui qui dit combien d'actions détenir. [§8.2]

7. fpp/gamma
   Cette quantité d'actions ne reste pas juste longtemps. À quelle vitesse faut-il la corriger ? [§8.2]

8. fpp/vega
   L'action n'est pas le seul risque : l'incertitude elle-même peut changer. [§8.2]

9. fpp/theta
   Même si rien ne change, l'échéance approche, et la position en est affectée. [§8.2]

10. fpp/rho
    Reste le financement : le taux d'intérêt entre dans le prix par l'actualisation du strike. [§8.2]

## Point d'arrivée
Le prix d'une option est le coût de sa couverture continue, et chaque sensibilité dit une position à tenir en sens inverse pour neutraliser un risque. [§7.1, §8.2]

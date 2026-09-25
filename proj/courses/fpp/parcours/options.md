---
id: fpp/parcours-options
ordre: 5
titre: Évaluer un droit sans obligation
source: poly, §6
---

## Point de départ
Payer quelque chose aujourd'hui pour avoir le droit, et non l'obligation, d'acheter l'action à 100 dans un an. L'engagement ferme d'acheter au prix à terme se signait gratuitement ; combien vaut ce droit ? [ajout]

## À savoir avant
- fpp/mesure-risque-neutre : c'est le moteur de valorisation du parcours ; la valeur d'une option y est l'espérance actualisée de son paiement. [Prop. 6, §6.2]
- fpp/replication-dynamique : c'est elle qui garantit qu'un contrat à prime se réplique, même quand son paiement n'est pas linéaire. [§4.2.2]
- fpp/facteur-actualisation : il actualise le strike dans la parité call-put. [Prop. 7]
- fpp/modele-black-scholes : c'est l'hypothèse sur le sous-jacent qui rend le prix d'une option calculable en forme fermée. [§6.4]
- fpp/responsabilite-limitee : c'est le plancher de l'actionnaire, posé à la fin du premier parcours, que la dernière étape évalue enfin. [§1.4, exo. 16]

## Étapes
1. fpp/payoff
   Pour parler d'un contrat, il faut d'abord dire ce qu'il verse, en fonction de ce qu'on observera. [Déf. 11]

2. fpp/contrat-a-prime
   Le contrat du point de départ se paie à la signature. Qu'est-ce que cela change à ce qu'on cherche ? [§6]

3. fpp/option
   La famille la plus importante de ces contrats laisse à son détenteur le choix d'exercer ou non. [Déf. 9]

4. fpp/call
   Premier droit élémentaire : celui du point de départ, du côté de l'acheteur. [Déf. 9]

5. fpp/put
   Second droit élémentaire, symétrique du premier. [Déf. 9]

6. fpp/parite-call-put
   Ces deux droits sont-ils indépendants l'un de l'autre ? L'absence d'arbitrage les lie, sans aucun modèle. [Prop. 7]

7. fpp/valeur-intrinseque
   Pour comprendre ce que coûte le droit de choisir, on compare son prix à ce que vaudrait le contrat si rien n'était aléatoire. [Déf. 12]

8. fpp/valeur-temps
   L'écart entre les deux est ce que l'incertitude ajoute, et son signe dépend de la forme du paiement. [Déf. 13]

9. fpp/formule-black-scholes
   Sous le modèle de référence, tout cela se calcule en une formule fermée. [§6.4, §6.5]

10. fpp/modele-de-merton
   Le premier parcours laissait l'actionnaire d'une entreprise endettée avec une perte bornée en bas. Que vaut ce qu'il détient, et que coûte à l'entreprise le risque qu'elle fasse faillite ? [exos §2.1]

## Point d'arrivée
Le droit d'acheter vaut plus que l'engagement ferme au même prix, parce qu'il n'oblige à rien quand l'action baisse : l'écart entre les deux est exactement un put. [Prop. 7]

Son prix dépasse aussi sa valeur intrinsèque, parce que son paiement est convexe ; cette valeur temps, la formule de Black et Scholes la chiffre. [Déf. 13, §6.4]

Le même outil évalue un bilan : les fonds propres d'une entreprise endettée sont un call sur sa valeur, et son spread de crédit est le prix d'un put. [exo. 16]

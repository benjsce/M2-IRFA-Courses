---
id: fpp/parcours-risque-neutre
ordre: 4
titre: Une probabilité pour calculer les prix
source: poly, §5
---

## Point de départ
L'investisseur sait maintenant fixer le prix d'un engagement ferme : pour l'action, qui ne verse pas de dividende et vaut 100, c'est 104,08 à un an. Mais un contrat qui ne lui verserait que la hausse de l'action au-delà de 100, et rien si elle baisse, ne se fabrique pas en achetant l'action et en attendant. Comment calculer le prix de n'importe quel paiement futur qui dépend de l'action ? [ajout]

## À savoir avant
- fpp/prix-a-terme : c'est ce que le marché cote, et c'est lui qui contraint la probabilité cherchée : sous elle, l'espérance du sous-jacent doit valoir son prix à terme. [Prop. 5, Prop. 6]
- fpp/volatilite : c'est le seul paramètre du modèle de Black et Scholes que le passage à la nouvelle probabilité ne change pas. [§5.4]

## Étapes
1. fpp/operateur-de-prix
   Avant de choisir une méthode, que doit respecter toute façon raisonnable de donner un prix à un paiement futur ? [§5.1]
   Histoire : « le prix de n'importe quel paiement futur » — Elle associe à chaque paiement futur un prix d'aujourd'hui. Pour qu'on ne puisse pas gagner sans risque, deux paiements détenus ensemble doivent coûter la somme de leurs prix, et un paiement qui ne peut être que positif doit avoir un prix positif. Une règle qui respecte cela s'appelle un opérateur de prix. [ajout]

2. fpp/mesure-risque-neutre
   Ces deux exigences suffisent à donner à toute règle de prix une forme très simple. Laquelle ? [Prop. 5, Prop. 6]
   Histoire : « c'est 104,08 à un an » — Une moyenne : le prix d'un paiement $g(S_T)$ versé en $T$ est sa moyenne sous une certaine probabilité $\mathbb{Q}$, ramenée à aujourd'hui par le zéro-coupon, $\Pi_t\big(g(S_T)\big)=P(t,T)\,\mathbb{E}^{\mathbb{Q}}\big[g(S_T)\big]$. Cette probabilité n'est pas une prévision : elle est choisie pour redonner les prix du marché, et c'est pourquoi on la dit risque-neutre. Pour l'action, elle doit redonner 100 : $0{,}9608\times\mathbb{E}^{\mathbb{Q}}(S_T)=100$, donc sous $\mathbb{Q}$ l'action vaut en moyenne 104,08 dans un an, son prix à terme, quoi que chacun croie de son rendement. [ajout]

3. fpp/contrat-derive
   Le contrat de l'investisseur, qui ne verse que la hausse, se calcule-t-il de la même façon ? [Prop. 6]
   Histoire : « que la hausse de l'action au-delà de 100, et rien si elle baisse » — Oui : tout contrat dont le paiement dépend de l'action se valorise par cette même moyenne, qu'il suive l'action en ligne droite, comme l'engagement ferme, ou non, comme celui-ci. Seule change l'inconnue : le prix écrit dans le contrat quand il ne coûte rien à la signature, ce qu'on paie aujourd'hui quand il se paie. [ajout]

4. fpp/transformee-de-laplace-gaussienne
   Pour calculer cette moyenne, il faut dire comment le prix de l'action dans un an est distribué. [Th. 1]
   Suite : Supposons que le logarithme du prix de l'action dans un an suive une loi normale. Que vaut alors la moyenne de l'action, qui est l'exponentielle de ce logarithme ? [ajout]
   Histoire : « Que vaut alors la moyenne de l'action » — Si $X\sim\mathcal{N}(\mu,\sigma^2)$, $\mathbb{E}(e^{X})=e^{\mu+\sigma^2/2}$ : la moyenne de l'exponentielle dépasse l'exponentielle de la moyenne d'un facteur $e^{\sigma^2/2}$. Pour que la moyenne de l'action vaille 104,08, il faudra donc retirer $\sigma^2/2$ à la moyenne de son logarithme. [ajout]

5. fpp/echelonnement-de-la-variance
   Il faut aussi savoir de combien ce logarithme se disperse, selon l'horizon. [§5.3]
   Suite : L'action a une volatilité de 20 % par an. Quelle dispersion cela lui donne-t-il à trois mois, ou à deux ans ? [ajout]
   Histoire : « Quelle dispersion cela lui donne-t-il à trois mois, ou à deux ans » — La variance grandit comme le temps, et l'écart type comme sa racine : $20\sqrt{0{,}25}=10\,\%$ à trois mois, $20\sqrt2\approx28{,}3\,\%$ à deux ans, et 20 % à un an. [ajout]

6. fpp/modele-black-scholes
   Tout est prêt pour écrire la loi de l'action dans un an. [§5.4]
   Histoire : « Comment calculer le prix de n'importe quel paiement futur qui dépend de l'action » — Un logarithme gaussien, une variance qui grandit comme le temps et un taux constant forment le modèle de Black et Scholes. Sous $\mathbb{Q}$, l'action y croît au taux sans risque : sa moyenne dans un an, $100\,e^{0{,}04}\approx104{,}08$, ne dépend pas de sa volatilité, qui ne règle que la dispersion autour. Tout paiement qui dépend de l'action a désormais un prix calculable ; le parcours suivant le fait pour le contrat de l'investisseur. [ajout]

## Point d'arrivée
Un prix est une moyenne actualisée sous la probabilité risque-neutre ; avec un logarithme gaussien pour l'action, cette moyenne se calcule. [ajout]

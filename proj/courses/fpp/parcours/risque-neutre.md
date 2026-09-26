---
id: fpp/parcours-risque-neutre
ordre: 4
titre: Une probabilité pour calculer les prix
source: poly, §5
---

## Point de départ
L'action vaut 100 et le zéro-coupon à un an 0,9608 : son prix à terme à un an vaut 104,08, et il se lit sur le marché. Peut-on en tirer une façon de calculer le prix de n'importe quel flux futur, même non linéaire ? [ajout]

## À savoir avant
- fpp/prix-a-terme : c'est ce que le marché cote, et c'est lui qui contraint la probabilité cherchée : sous elle, l'espérance du sous-jacent doit valoir son prix à terme. [Prop. 5, Prop. 6]
- fpp/volatilite : c'est le seul paramètre du modèle de Black et Scholes que le passage à la nouvelle probabilité ne change pas. [§5.4]

## Étapes
1. fpp/operateur-de-prix
   Première question : si l'on interdit l'arbitrage, que peut-on dire de toute règle de valorisation, avant même d'en choisir une ? [§5.1]
   Histoire : « le prix de n'importe quel flux futur » — Avant de choisir une règle, on peut dire ce que toute règle sans arbitrage respecte : elle associe à chaque flux futur un prix d'aujourd'hui ; deux flux détenus ensemble coûtent la somme de leurs prix ; un flux qui ne peut être que positif a un prix positif. [ajout]

2. fpp/mesure-risque-neutre
   Ces propriétés ont une conséquence inattendue : tout se calcule comme une moyenne, pourvu qu'on choisisse bien les poids, et le marché à terme les fixe. [Prop. 5, Prop. 6]
   Histoire : « son prix à terme à un an vaut 104,08 » — Tout prix s'écrit comme une moyenne actualisée, $\Pi\big(g(S_T)\big)=P(t,T)\,\mathbb{E}^{\mathbb{Q}}\big[g(S_T)\big]$, sous des poids $\mathbb{Q}$ que le marché à terme contraint : sous eux, l'action vaut en moyenne 104,08 dans un an, quoi que chacun croie de sa dérive. [ajout]

3. fpp/contrat-derive
   Tous les contrats de ce cours se valorisent alors par le même moteur ; seule change l'inconnue qu'on y cherche. [Prop. 6]
   Histoire : « même non linéaire » — Un flux qui dépend de l'action, linéaire comme le forward ou non comme une option, se valorise par cette même moyenne. Seule change l'inconnue : un prix $K$ pour un contrat qui ne coûte rien à la signature, une prime pour un contrat qui se paie. [ajout]

4. fpp/transformee-de-laplace-gaussienne
   Pour calculer ces espérances en forme fermée, il faut un résultat technique sur les gaussiennes. [Th. 1]
   Suite : Pour calculer ces moyennes, il faut une loi pour l'action dans un an. Supposons que son logarithme soit gaussien. Que vaut alors la moyenne de l'action, qui en est l'exponentielle ? [ajout]
   Histoire : « Que vaut alors la moyenne de l'action, qui en est l'exponentielle » — Si $X\sim\mathcal{N}(\mu,\sigma^2)$, $\mathbb{E}(e^{X})=e^{\mu+\sigma^2/2}$ : la moyenne de l'exponentielle dépasse l'exponentielle de la moyenne d'un facteur $e^{\sigma^2/2}$. C'est ce facteur qu'il faudra compenser pour que la moyenne vaille 104,08. [ajout]

5. fpp/echelonnement-de-la-variance
   Il faut aussi savoir comment la dispersion d'un prix grandit avec l'horizon. [§5.3]
   Suite : L'action a une volatilité de 20 % par an. Quelle dispersion cela lui donne-t-il à trois mois, ou à deux ans ? [ajout]
   Histoire : « Quelle dispersion cela lui donne-t-il à trois mois, ou à deux ans » — La variance grandit comme le temps, et l'écart type comme sa racine : $20\sqrt{0{,}25}=10\,\%$ à trois mois, $20\sqrt2\approx28{,}3\,\%$ à deux ans. [ajout]

6. fpp/modele-black-scholes
   Réunis, ces deux résultats donnent le modèle de référence du cours pour le sous-jacent. [§5.4]
   Histoire : « Peut-on en tirer une façon de calculer le prix de n'importe quel flux futur » — Un logarithme gaussien, une variance qui grandit comme le temps et un taux constant donnent le modèle de Black et Scholes. Sous $\mathbb{Q}$, l'action y croît au taux sans risque : $\mathbb{E}^{\mathbb{Q}}(S_{t+1})=100\,e^{0{,}04}\approx104{,}08$, quelle que soit sa volatilité. [ajout]

## Point d'arrivée
Un prix est une espérance actualisée sous la mesure risque-neutre ; avec une diffusion log-normale, cette espérance se calcule. Il reste à l'appliquer aux options. [ajout]

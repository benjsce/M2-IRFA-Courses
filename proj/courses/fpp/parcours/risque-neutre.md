---
id: fpp/parcours-risque-neutre
ordre: 4
titre: Une probabilité pour calculer les prix
source: poly, §5
---

## Point de départ
Les prix à terme se lisent sur le marché. Peut-on en tirer une façon de calculer le prix de n'importe quel flux futur, même non linéaire ? [ajout]

## À savoir avant
- fpp/prix-a-terme : c'est ce que le marché cote, et c'est lui qui contraint la probabilité cherchée : sous elle, l'espérance du sous-jacent doit valoir son prix à terme. [Prop. 5, Prop. 6]
- fpp/volatilite : c'est le seul paramètre du modèle de Black et Scholes que le passage à la nouvelle probabilité ne change pas. [§5.4]

## Étapes
1. fpp/operateur-de-prix
   Première question : si l'on interdit l'arbitrage, que peut-on dire de toute règle de valorisation, avant même d'en choisir une ? [§5.1]

2. fpp/mesure-risque-neutre
   Ces propriétés ont une conséquence inattendue : tout se calcule comme une moyenne, pourvu qu'on choisisse bien les poids, et le marché à terme les fixe. [Prop. 5, Prop. 6]

3. fpp/contrat-derive
   Tous les contrats de ce cours se valorisent alors par le même moteur ; seule change l'inconnue qu'on y cherche. [Prop. 6]

4. fpp/transformee-de-laplace-gaussienne
   Pour calculer ces espérances en forme fermée, il faut un résultat technique sur les gaussiennes. [Th. 1]

5. fpp/echelonnement-de-la-variance
   Il faut aussi savoir comment la dispersion d'un prix grandit avec l'horizon. [§5.3]

6. fpp/modele-black-scholes
   Réunis, ces deux résultats donnent le modèle de référence du cours pour le sous-jacent. [§5.4]

## Point d'arrivée
Un prix est une espérance actualisée sous la mesure risque-neutre ; avec une diffusion log-normale, cette espérance se calcule. Il reste à l'appliquer aux options. [ajout]

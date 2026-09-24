---
id: pfo/parcours-risque
ordre: 5
titre: Mesurer le risque quand la loi n'est pas normale
source: poly, §2.5, Listing 2.2
---

## Point de départ
Un portefeuille de 1 000 000 affiche des rendements journaliers de moyenne 0,05 % et d'écart type 2 %, avec une asymétrie de −0,5 et un excès de kurtosis de 3. Combien peut-il perdre en une mauvaise journée ? [ajout]

## À savoir avant
- pfo/coefficient-d-asymetrie : c'est l'une des deux corrections que la méthode de Cornish-Fisher apporte au calcul gaussien. Dans l'exemple, une asymétrie de −0,5 déplace le quantile vers les pertes. [p. 34]
- pfo/kurtosis : c'est l'autre correction, celle de l'épaisseur des queues. Dans cette formule, le cours la prend en excès, nulle pour une loi normale. [éq. 2.26]

## Étapes
1. pfo/quantile
   Toutes les mesures de ce parcours reposent sur un même objet, que le poly emploie partout sans jamais le définir. [ajout]

2. pfo/valeur-a-risque
   La réglementation pose une question précise : quelle perte ne sera dépassée qu'une fois sur vingt ? [§2.5]

3. pfo/valeur-a-risque-conditionnelle
   Ce seuil ne dit rien de ce qui se passe au-delà : deux portefeuilles de même VaR peuvent perdre très différemment les mauvais jours. [p. 32]

4. pfo/modele-de-risque
   Pour chiffrer l'une et l'autre, il faut supposer quelque chose de la loi des rendements. Le cours compare trois hypothèses. [p. 32, Listing 2.2]

5. pfo/var-historique
   Première hypothèse : n'en faire aucune, et lire directement les rendements passés. [Listing 2.2]

6. pfo/var-gaussienne
   Deuxième hypothèse, la plus simple à calculer : celle que le parcours précédent vient de réfuter. [Listing 2.2]

7. pfo/developpement-de-cornish-fisher
   Plutôt que d'abandonner le calcul gaussien, peut-on corriger son quantile avec les deux moments du parcours précédent ? [p. 34]

8. pfo/var-de-cornish-fisher
   Comment ce quantile corrigé devient-il un montant de perte ? Pour la VaR, c'est immédiat ; pour la CVaR, qui moyenne toute la queue, il faut davantage. [§2.5.1, Listing 2.2]

## Point d'arrivée
Sur l'exemple de départ, la VaR à 95 % passe de 32 397 en gaussien à 33 935 avec Cornish-Fisher, et la CVaR de 40 754 à 53 511 : la correction pèse surtout sur ce qui se passe au-delà du seuil. [ajout]

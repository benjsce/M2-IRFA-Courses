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
   Histoire : « Combien peut-il perdre en une mauvaise journée » — Une « mauvaise journée » doit se chiffrer : une des 5 % pires, par exemple. Le rendement qui sépare ces 5 % du reste est un quantile. Pour une loi normale, il se trouve toujours à 1,6449 écarts types sous la moyenne, valeur que donne la table de la loi normale ; pour des rendements de moyenne 0,05 % et d'écart type 2 %, il vaut $0{,}05\,\%-1{,}6449\times2\,\%\approx-3{,}24\,\%$. [ajout]

2. pfo/valeur-a-risque
   La réglementation pose une question précise : quelle perte ne sera dépassée qu'une fois sur vingt ? [§2.5]
   Histoire : « Un portefeuille de 1 000 000 » — Rapporté au capital, ce quantile, $-3{,}2397\,\%$ avant arrondi, devient une perte : si ses rendements étaient normaux, le portefeuille ne perdrait plus de $0{,}032397\times1\,000\,000\approx32\,397$ qu'une journée sur vingt. C'est sa valeur à risque, ou VaR, à 95 % sur un jour. [ajout]

3. pfo/valeur-a-risque-conditionnelle
   Ce seuil ne dit rien de ce qui se passe au-delà : deux portefeuilles de même VaR peuvent perdre très différemment les mauvais jours. [p. 32]
   Suite : Et les jours où la perte dépasse ce seuil, combien perd-il en moyenne ? [ajout]
   Histoire : « combien perd-il en moyenne » — C'est la CVaR, ou valeur à risque conditionnelle, la perte moyenne sur les 5 % de jours les pires. Si les rendements étaient normaux, la moyenne de ces pires rendements se trouverait à $\varphi(1{,}645)/0{,}05\approx2{,}063$ écarts types sous la moyenne, $\varphi$ étant la densité de la loi normale, plus loin que le seuil à 1,645 : $0{,}05\,\%-2{,}063\times2\,\%\approx-4{,}08\,\%$, soit une perte de 40 754, bien au-delà des 32 397 du seuil. [ajout]

4. pfo/modele-de-risque
   Pour chiffrer l'une et l'autre, il faut supposer quelque chose de la loi des rendements. Le cours compare trois hypothèses. [p. 32, Listing 2.2]
   Histoire : « avec une asymétrie de −0,5 et un excès de kurtosis de 3 » — Ces deux chiffres disent que la loi n'est pas normale : les montants précédents dépendent de l'hypothèse faite sur elle. Le cours compare trois hypothèses : aucune, la loi normale, et une loi normale corrigée. [ajout]

5. pfo/var-historique
   Première hypothèse : n'en faire aucune, et lire directement les rendements passés. [Listing 2.2]
   Suite : Sur ses 1 000 derniers jours, le 5e centile des rendements du portefeuille vaut −3,2 %, et les rendements qui lui sont inférieurs valent en moyenne −4,5 %. Que disent-ils, sans aucune hypothèse sur la loi ? [ajout]
   Histoire : « Que disent-ils, sans aucune hypothèse sur la loi » — Lus tels quels, ils donnent une VaR de 32 000 et une CVaR de 45 000. Aucune hypothèse, mais le passé seul : un krach absent de ces mille jours n'y compte pas. [ajout]

6. pfo/var-gaussienne
   Deuxième hypothèse, la plus simple à calculer : celle que le parcours précédent vient de réfuter. [Listing 2.2]
   Histoire : « de moyenne 0,05 % et d'écart type 2 % » — Deuxième hypothèse : ne garder que ces deux nombres et supposer la loi normale. On retrouve la VaR de 32 397 et la CVaR de 40 754 ; mais l'asymétrie et la kurtosis du portefeuille disent que cette hypothèse est fausse. [ajout]

7. pfo/developpement-de-cornish-fisher
   Plutôt que d'abandonner le calcul gaussien, peut-on corriger son quantile avec les deux moments du parcours précédent ? [p. 34]
   Histoire : « une asymétrie de −0,5 » — Le quantile gaussien, $z_\alpha=-1{,}645$, se corrige avec l'asymétrie $S=-0{,}5$ et l'excès de kurtosis $K=3$ : $q_\alpha\approx z_\alpha+\tfrac{S}{6}(z_\alpha^2-1)+\tfrac{K}{24}(z_\alpha^3-3z_\alpha)-\tfrac{S^2}{36}(2z_\alpha^3-5z_\alpha)$. L'asymétrie négative le pousse vers les pertes de $-0{,}142$ ; à ce seuil, la kurtosis le ramène de $+0{,}061$ et le dernier terme de $+0{,}005$ : il arrive à $-1{,}7217$. [ajout]

8. pfo/var-de-cornish-fisher
   Comment ce quantile corrigé devient-il un montant de perte ? Pour la VaR, c'est immédiat ; pour la CVaR, qui moyenne toute la queue, il faut davantage. [§2.5.1, Listing 2.2]
   Histoire : « un excès de kurtosis de 3 » — Avec le quantile corrigé, la VaR passe de 32 397 à $-(0{,}05\,\%-1{,}7217\times2\,\%)\times1\,000\,000\approx33\,935$. La CVaR, qui moyenne toute la queue, doit corriger chacun de ses quantiles avant d'en faire la moyenne, et bouge bien davantage, de 40 754 à 53 511 : plus d'environ 1,73 écart type sous la moyenne, le terme de kurtosis change de signe et pousse fort vers les pertes. [ajout]

## Point d'arrivée
Sur l'exemple de départ, la VaR à 95 % passe de 32 397 en gaussien à 33 935 avec Cornish-Fisher, et la CVaR de 40 754 à 53 511 : la correction pèse surtout sur ce qui se passe au-delà du seuil. [ajout]

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
   Avant de chiffrer, il faut dire ce qu'est une mauvaise journée. [ajout]
   Histoire : « en une mauvaise journée » — Une mauvaise journée doit se chiffrer : une des 5 % pires, par exemple, soit une journée sur vingt. Le rendement qui sépare ces 5 % du reste est le quantile à 5 % de la loi des rendements. La moyenne et l'écart type ne suffisent pas à le situer : il dépend de toute la forme de la loi, et c'est lui qu'il va falloir trouver. [ajout]

2. pfo/valeur-a-risque
   La réglementation pose une question précise : quelle perte ne sera dépassée qu'une fois sur vingt ? [§2.5]
   Histoire : « Combien peut-il perdre » — Rapporté au capital, ce quantile devient une perte : la valeur à risque, ou VaR, à 95 % sur un jour, est la perte que le portefeuille ne dépasse qu'une journée sur vingt. Si le quantile valait −3,24 %, par exemple, elle serait de $0{,}0324\times1\,000\,000=32\,400$. [ajout]

3. pfo/valeur-a-risque-conditionnelle
   Ce seuil ne dit rien de ce qui se passe au-delà : deux portefeuilles de même VaR peuvent perdre très différemment les mauvais jours. [p. 32]
   Suite : Et les jours où la perte dépasse ce seuil, combien perd-il en moyenne ? [ajout]
   Histoire : « combien perd-il en moyenne » — Au-delà du seuil de 32 400 de l'exemple, la VaR ne dit plus rien : le portefeuille y perd plus, sans qu'on sache de combien. La CVaR répond en faisant la moyenne des pertes de ces jours-là, les 5 % les pires : si le rendement y valait en moyenne −4,08 %, elle serait de $0{,}0408\times1\,000\,000=40\,800$, plus que la VaR. Elle dépend donc de toute la queue de la loi, pas du seul quantile. [ajout]

4. pfo/modele-de-risque
   Pour chiffrer l'une et l'autre, il faut supposer quelque chose de la loi des rendements. Le cours compare trois hypothèses. [p. 32, Listing 2.2]
   Suite : Pour chiffrer la VaR et la CVaR, que faut-il supposer de la loi de ses rendements ? [ajout]
   Histoire : « que faut-il supposer de la loi de ses rendements » — Une loi entière, puisque la VaR et la CVaR en dépendent, pas seulement de sa moyenne et de son écart type ; et l'asymétrie de −0,5 et l'excès de kurtosis de 3 disent qu'elle n'est pas normale. Chaque hypothèse donne un modèle de risque ; le cours en compare trois : aucune, la loi normale, et une loi normale corrigée. [ajout]

5. pfo/var-historique
   Première hypothèse : n'en faire aucune, et lire directement les rendements passés. [Listing 2.2]
   Suite : Sur ses 1 000 derniers jours, le 5e centile des rendements du portefeuille vaut −3,2 %, et les rendements qui lui sont inférieurs valent en moyenne −4,5 %. Que disent-ils, sans aucune hypothèse sur la loi ? [ajout]
   Histoire : « Que disent-ils, sans aucune hypothèse sur la loi » — Lus tels quels, ils donnent une VaR de 32 000 et une CVaR de 45 000. Aucune hypothèse, mais le passé seul : un krach absent de ces mille jours n'y compte pas. [ajout]

6. pfo/var-gaussienne
   Deuxième hypothèse, la plus simple à calculer : celle que le parcours précédent vient de réfuter. [Listing 2.2]
   Suite : Et si l'on supposait la loi normale, de moyenne 0,05 % et d'écart type 2 % ? [ajout]
   Histoire : « Et si l'on supposait la loi normale » — On ne garde que ces deux nombres et l'on suppose la loi normale. Son quantile à 5 % est toujours à 1,6449 écarts types sous la moyenne, valeur que donne la table : $0{,}05\,\%-1{,}6449\times2\,\%\approx-3{,}24\,\%$, soit une VaR de 32 397. La moyenne des 5 % pires jours est plus loin : pour une loi normale, elle se trouve à $\varphi(1{,}6449)/0{,}05\approx2{,}063$ écarts types sous la moyenne, $\varphi$ étant la densité de la loi normale ; cette formule fermée vient de ce que la dérivée de $\varphi$ en $x$ vaut $-x\varphi(x)$. D'où $0{,}05\,\%-2{,}063\times2\,\%\approx-4{,}08\,\%$ et une CVaR de 40 754. Mais l'asymétrie et la kurtosis du portefeuille disent que cette hypothèse est fausse. [ajout]

7. pfo/developpement-de-cornish-fisher
   Plutôt que d'abandonner le calcul gaussien, on peut le corriger avec les deux moments du parcours précédent. [p. 34]
   Suite : La loi n'est pas normale : peut-on corriger son quantile par l'asymétrie et l'excès de kurtosis ? [ajout]
   Histoire : « peut-on corriger son quantile » — Le quantile gaussien, $z_\alpha=-1{,}645$, se corrige avec l'asymétrie $S=-0{,}5$ et l'excès de kurtosis $K=3$ : $q_\alpha\approx z_\alpha+\tfrac{S}{6}(z_\alpha^2-1)+\tfrac{K}{24}(z_\alpha^3-3z_\alpha)-\tfrac{S^2}{36}(2z_\alpha^3-5z_\alpha)$. L'asymétrie négative le pousse vers les pertes de $-0{,}142$. La kurtosis, elle, le ramène de $+0{,}061$ : une loi à queues épaisses a aussi des flancs plus minces que la loi normale, et à 1,645 écarts types on est encore sur le flanc ; son terme, $z_\alpha^3-3z_\alpha$, ne change de signe qu'à $\sqrt3\approx1{,}73$ écarts types. Avec le dernier terme, $+0{,}005$, le quantile arrive à $-1{,}7217$. [ajout]

8. pfo/var-de-cornish-fisher
   Le quantile corrigé doit encore devenir un montant de perte. Pour la VaR, c'est immédiat ; pour la CVaR, qui moyenne toute la queue, il faut davantage. [§2.5.1, Listing 2.2]
   Suite : Que deviennent alors la VaR et la CVaR ? [ajout]
   Histoire : « Que deviennent alors la VaR et la CVaR » — Avec le quantile corrigé, la VaR passe de 32 397 à $-(0{,}05\,\%-1{,}7217\times2\,\%)\times1\,000\,000\approx33\,935$. La CVaR, elle, corrige chacun des quantiles de la queue, du niveau 5 % jusqu'au niveau 0,01 %, puis en fait la moyenne. Or au-delà de 1,73 écarts types, le terme de kurtosis change de signe et pousse fort vers les pertes : la CVaR passe de 40 754 à 53 511. Aller jusqu'au tout bout de la queue ajouterait encore environ 430. [ajout]

## Point d'arrivée
Sur l'exemple de départ, la VaR à 95 % passe de 32 397 en gaussien à 33 935 avec Cornish-Fisher, et la CVaR de 40 754 à 53 511 : la correction pèse surtout sur ce qui se passe au-delà du seuil. [ajout]

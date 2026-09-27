---
id: pfo/parcours-portefeuille
ordre: 6
titre: Répartir un capital entre plusieurs actifs
source: poly, chapitre 3
---

## Point de départ
Un investisseur hésite entre deux actifs : l'un rapporte 6 % par an avec une volatilité de 10 %, l'autre 10 % avec une volatilité de 20 %, et ils ne sont pas corrélés. Un placement sans risque rapporte 2 %. Combien mettre dans chacun, et faut-il garder une part sans risque ? [ajout]

## À savoir avant
- pfo/matrice-de-covariance : c'est elle qui porte tout le risque du récit ; chaque portefeuille la lit à travers ses poids. [§1.5, §3.0.1]
- pfo/piege-d-agregation : il justifie qu'on écrive le rendement du portefeuille comme une moyenne pondérée, et rappelle que ce n'est exact qu'en rendements arithmétiques. [§1.2.2]
- dup/diversification : le cours de décision en incertain y montrait, pour deux actifs, que mélanger peut réduire le risque sous celui de chacun ; ce récit en fait une règle d'allocation. [ajout]
- pfo/rendement-logarithmique : les données du récit sont des rendements logarithmiques journaliers, qu'il faut porter à l'année. [§3.0.7, §3.0.8]
- fpp/echelonnement-de-la-variance : c'est l'hypothèse qui autorise à multiplier une variance journalière par le nombre de séances. [§3.0.7]
- dup/frontiere-actif-sans-risque : elle fournit la géométrie de la dernière étape, où l'on mélange un portefeuille risqué avec le placement sans risque. [ajout]

## Étapes
1. pfo/paradigme-de-markowitz
   Faut-il choisir le meilleur des deux actifs, ou regarder ce que chacun change à l'ensemble ? [§3.0.1]
   Histoire : « hésite entre deux actifs » — Pris seul, le second rapporte plus et le premier risque moins : aucun des deux ne l'emporte sur l'autre sur les deux tableaux. La question n'est pas lequel choisir, mais ce que chacun apporte au mélange. [ajout]

2. pfo/moments-du-portefeuille
   Pour comparer des répartitions, il faut chiffrer chacune. [§3.0.1]
   Suite : Que rapporte, et combien fluctue, un mélange des deux ? [ajout]
   Histoire : « Que rapporte, et combien fluctue, un mélange des deux » — À parts égales, le mélange rapporte la moyenne pondérée $\tfrac12\times6+\tfrac12\times10=8\,\%$. Sa variance est la somme des variances pondérées par le carré des poids, sans terme croisé puisque la corrélation est nulle : $0{,}5^2\times0{,}10^2+0{,}5^2\times0{,}20^2=0{,}0125$, d'où une volatilité de $\sqrt{0{,}0125}\approx11{,}18\,\%$ : moins que la moyenne des deux, 15 %, parce que les actifs ne bougent pas ensemble. [ajout]

3. pfo/annualisation
   Les prix arrivent jour par jour, les objectifs se fixent sur un an, et passer de l'un à l'autre ne doit pas fausser le risque. [§3.0.7]
   Suite : Ces chiffres annuels, l'investisseur ne les observe pas : ses données sont des rendements journaliers, par exemple, pour le second actif, de moyenne 0,0397 % et d'écart type 1,26 %. Comment les porter à l'année ? [ajout]
   Histoire : « Comment les porter à l'année » — La moyenne et la variance se multiplient par les 252 séances de l'année, l'écart type par leur racine : $252\times0{,}0397\,\%\approx10\,\%$ et $1{,}26\,\%\times\sqrt{252}\approx20\,\%$ par an, les chiffres du départ ; à l'inverse, $10\,\%/252$ et $20\,\%/\sqrt{252}$ redonnent les chiffres journaliers. [ajout]

4. pfo/optimisation-de-portefeuille
   On sait désormais noter une répartition ; reste à choisir, et selon quel critère. [p. 38]
   Suite : Chaque répartition a maintenant son rendement et sa volatilité. Comment choisir entre elles ? [ajout]
   Histoire : « Comment choisir entre elles » — En résolvant un problème d'optimisation : choisir le vecteur de poids $W$, positifs et de somme 1. À parts égales, 8 % pour 11,18 % de volatilité ; tout dans le premier actif, 6 % pour 10 % : aucun choix ne gagne sur les deux tableaux, et choisir revient à résoudre un problème qui arbitre entre $W^T\mu$ et $\sqrt{W^T\boldsymbol{\Sigma}W}$. [ajout]

5. pfo/frontiere-efficiente
   Premier critère : se fixer un rendement et ne rien risquer de plus que nécessaire pour l'obtenir. [§3.0.2]
   Suite : Pour chaque rendement visé, quelle répartition risque le moins ? [ajout]
   Histoire : « Pour chaque rendement visé, quelle répartition risque le moins » — Ces répartitions forment la frontière efficiente. La moins risquée de toutes, les actifs n'étant pas corrélés, répartit les poids en raison inverse des variances : $0{,}04/(0{,}01+0{,}04)=80\,\%$ dans ce premier actif, pour $0{,}8\times6+0{,}2\times10=6{,}8\,\%$ de rendement et $\sqrt{0{,}8^2\times0{,}01+0{,}2^2\times0{,}04}\approx8{,}94\,\%$ de volatilité, moins que chacun des deux. Les autres cibles tracent une courbe à partir de ce point. [ajout]

6. pfo/ratio-de-sharpe
   Sur cette courbe, tous les points semblent défendables, et un placement sans risque rapporte 2 %. [§3.0.3]
   Suite : Au-delà des 2 % du placement sans risque, combien rapporte chaque point de volatilité ? [ajout]
   Histoire : « combien rapporte chaque point de volatilité » — Au-delà de ces 2 %, chaque actif rapporte 0,40 par unité de volatilité, $(6-2)/10$ et $(10-2)/20$. Le mélange à parts égales atteint $(8-2)/11{,}18\approx0{,}54$ : il paie mieux le risque que chacun des deux. [ajout]

7. pfo/portefeuille-tangent
   Second critère : chercher directement le portefeuille dont le ratio de Sharpe est le plus élevé. Où tombe-t-il par rapport à la courbe ? [p. 40, §3.0.4]
   Histoire : « Combien mettre dans chacun » — Le mélange qui paie le mieux le risque donne à chaque actif, les deux n'étant pas corrélés, un poids proportionnel à son rendement au-delà des 2 % divisé par sa variance : $4/0{,}01=400$ contre $8/0{,}04=200$, soit deux tiers dans le premier actif et un tiers dans le second. Il rapporte 7,33 % pour 9,43 % de volatilité, soit 0,566 de rendement au-delà des 2 % par unité de volatilité. C'est le point où la droite partie des 2 % touche la courbe. [ajout]

8. pfo/ligne-de-marche-des-capitaux
   Reste la question du départ : faut-il garder une part sans risque, et que devient alors le compromis ? [p. 41]
   Histoire : « et faut-il garder une part sans risque » — Oui, s'il veut moins de risque que ce portefeuille : il le dose avec le placement sans risque, le long d'une droite de pente 0,566. Moitié chacun donne 4,67 % de rendement pour 4,71 % de volatilité. [ajout]

9. pfo/slsqp
   Avec deux actifs, tout se fait à la main. Avec des dizaines, et des bornes sur chaque poids, plus aucune formule ne donne la solution. [§3.0.6]
   Suite : L'investisseur élargit son choix à des dizaines d'actifs, avec une borne sur chaque poids. Comment l'ordinateur trouve-t-il alors la meilleure répartition ? [ajout]
   Histoire : « Comment l'ordinateur trouve-t-il alors la meilleure répartition » — Il part d'une répartition, à parts égales par exemple entre ces dizaines d'actifs. Autour d'elle, il remplace le ratio de Sharpe à rendre maximal par une approximation quadratique en les poids, garde la somme 1 et la borne sur chaque poids, résout ce problème approché et déplace les poids dans le sens indiqué. Il recommence depuis la nouvelle répartition, jusqu'à ce qu'aucun déplacement n'améliore plus le ratio. [ajout]

## Point d'arrivée
L'investisseur ne choisit pas un actif mais un mélange : deux tiers dans le premier, un tiers dans le second, le portefeuille dont le rendement excédentaire par unité de risque est le plus élevé. Il règle ensuite son risque en dosant ce mélange avec le placement sans risque, le long d'une droite de pente constante. [ajout]

Tout repose sur des rendements espérés et des covariances estimés, et le récit s'arrête là où commence la question de leur stabilité : si ces estimations bougent, la répartition bouge-t-elle avec elles ? [p. 54]

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

2. pfo/moments-du-portefeuille
   Pour comparer des répartitions, il faut chiffrer chacune : que rapporte-t-elle en moyenne, et combien fluctue-t-elle ? [§3.0.1]

3. pfo/annualisation
   Les prix arrivent jour par jour, les objectifs se fixent sur un an. Comment passer de l'un à l'autre sans fausser le risque ? [§3.0.7]

4. pfo/optimisation-de-portefeuille
   On sait désormais noter une répartition. Comment chercher la meilleure, et meilleure selon quel critère ? [p. 38]

5. pfo/frontiere-efficiente
   Premier critère : se fixer un rendement et ne rien risquer de plus que nécessaire pour l'obtenir. Que dessinent ces choix quand la cible varie ? [§3.0.2]

6. pfo/ratio-de-sharpe
   Sur cette courbe, tous les points semblent défendables. Avec un placement sans risque à 2 %, comment dire lequel paie le mieux le risque pris ? [§3.0.3]

7. pfo/portefeuille-tangent
   Second critère : chercher directement le portefeuille qui obtient le meilleur score. Où tombe-t-il par rapport à la courbe ? [p. 40, §3.0.4]

8. pfo/ligne-de-marche-des-capitaux
   Reste la question du départ : faut-il garder une part sans risque, et que devient alors le compromis ? [p. 41]

9. pfo/slsqp
   Avec deux actifs, tout se fait à la main. Avec des dizaines et des bornes sur chaque poids, comment l'ordinateur trouve-t-il la solution ? [§3.0.6]

## Point d'arrivée
L'investisseur ne choisit pas un actif mais un mélange : deux tiers dans le premier, un tiers dans le second, le portefeuille dont le rendement excédentaire par unité de risque est le plus élevé. Il règle ensuite son risque en dosant ce mélange avec le placement sans risque, le long d'une droite de pente constante. [ajout]

Tout repose sur des rendements espérés et des covariances estimés : le récit s'arrête là où commence la question de leur stabilité, que pose l'exercice 3. [p. 54]

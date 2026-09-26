---
id: pfo/parcours-volatilite
ordre: 3
titre: Mesurer la volatilité et les co-mouvements
source: poly, §1.4–§1.6
---

## Point de départ
Les rendements sont propres. Il faut maintenant dire combien ils bougent et s'ils bougent ensemble : un actif varie de 1 % par jour, un autre de 2 %, avec une corrélation de 0,5. Une fois ces chiffres rangés, deux difficultés apparaissent, l'une dans le temps, l'autre entre les places. [ajout]

## À savoir avant
- fpp/volatilite : c'est la grandeur qu'on cherche à estimer. Ce parcours montre qu'un seul nombre fixe ne suffit pas à la décrire. [§1.4]
- pfo/rendement-logarithmique : c'est la matière première de chaque estimation du parcours, variances comme covariances. [Listing 1.2, Listing 1.3]
- fpp/echelonnement-de-la-variance : c'est lui qui justifie de multiplier une variance journalière par 252 pour la porter à l'année, et une variance hebdomadaire par 52 ; c'est ce qui permet, à la fin, de comparer deux estimations faites à des fréquences différentes. [éq. 1.11, Listing 1.4]

## Étapes
1. pfo/matrice-de-covariance
   Comment ranger ces chiffres pour les deux actifs ensemble ? Il faut une variance pour chacun, et un terme pour le couple. [§1.5]
   Histoire : « un actif varie de 1 % par jour, un autre de 2 % » — On range dans une matrice les variances et la covariance, qui vaut la corrélation fois le produit des écarts types. Portées à l'année en multipliant par ses 252 séances : $0{,}01^2\times252=0{,}0252$ et $0{,}02^2\times252=0{,}1008$ sur la diagonale, $0{,}5\times0{,}01\times0{,}02\times252=0{,}0252$ hors de la diagonale. [ajout]

2. pfo/matrice-de-correlation
   Ces termes croisés sont dans l'unité d'un rendement au carré, donc illisibles seuls. Comment les rendre comparables d'un couple à l'autre ? [§1.5, p. 17]
   Histoire : « s'ils bougent ensemble » — Le terme croisé, 0,0252, ne dit pas à lui seul si les actifs sont liés : si le second actif variait de 4 % par jour au lieu de 2 %, il doublerait, à 0,0504, sans que leur lien change. Divisé par le produit des écarts types, $0{,}0252/\sqrt{0{,}0252\times0{,}1008}=0{,}5$, il ne garde que le lien. Ici on connaissait la corrélation et l'on retombe sur 0,5 ; en pratique, c'est l'inverse : on estime les covariances sur les rendements, et c'est cette division qui donne les corrélations. [ajout]

3. pfo/regroupement-de-volatilite
   Première difficulté : la dispersion des rendements ne reste pas au même niveau d'une semaine à l'autre. [§1.4]
   Histoire : « combien ils bougent » — Ce 1 % par jour, rangé dans la matrice, n'est qu'une moyenne sur la période : l'actif varie moins en temps calme, bien plus en crise, et les journées agitées se suivent. Un seul nombre fixe ne décrit pas cette alternance. [ajout]

4. pfo/ewma
   Comment estimer une volatilité qui change, sans attendre des années de données à chaque fois ? [§1.4]
   Suite : Hier, le premier actif a fait 2 %, deux fois son écart type habituel. Que faut-il croire de sa volatilité aujourd'hui ? [ajout]
   Histoire : « Que faut-il croire de sa volatilité aujourd'hui » — L'EWMA, moyenne mobile à pondération exponentielle, mélange la variance de la veille, $0{,}01^2=0{,}0001$ pour 1 % par jour, et le carré du dernier rendement, en donnant au passé le poids $\lambda=0{,}94$ usuel pour des données journalières : $0{,}94\times0{,}0001+0{,}06\times0{,}02^2=0{,}000118$, soit une volatilité de $\sqrt{0{,}000118}\approx1{,}09\,\%$. Elle monte, sans oublier le passé : ce jour-là, c'est 1,09 % et non 1 % qu'il faudrait mettre dans la matrice. [ajout]

5. pfo/effet-epps
   Seconde difficulté : Tokyo ferme avant que Paris ouvre. Une corrélation calculée jour par jour sur ces places est-elle fiable ? [§1.3.1, ajout]
   Suite : Supposons que le premier actif cote à Tokyo et le second à Paris. Calculée sur leurs rendements journaliers, leur corrélation ne sort qu'à 0,4 ; sur leurs rendements hebdomadaires, à 0,5. Laquelle croire ? [ajout]
   Histoire : « Laquelle croire » — La seconde. Une nouvelle tombée l'après-midi à Paris ne touche Tokyo que le lendemain : les deux rendements d'un même jour ne portent pas les mêmes nouvelles, et la corrélation journalière tombe sous sa vraie valeur. Sur une semaine, ce décalage d'un jour ne pèse presque plus. [ajout]

6. pfo/norme-de-frobenius
   Les deux fréquences donnent donc deux matrices de covariance différentes pour les mêmes actifs. De combien diffèrent-elles, en un seul nombre ? [§1.6, §1.6.1]
   Suite : Portées à l'année, par 252 pour l'une et par 52 pour l'autre, les deux estimations ont les mêmes variances ; seul le terme croisé change : $0{,}4\times0{,}01\times0{,}02\times252=0{,}02016$ en journalier, contre 0,0252 en hebdomadaire. Quelle distance sépare les deux matrices ? [ajout]
   Histoire : « Quelle distance sépare les deux matrices » — On additionne les carrés de tous les écarts terme à terme, le terme croisé comptant deux fois puisqu'il figure deux fois dans la matrice, et l'on prend la racine. Seul l'écart du terme croisé, $0{,}0252-0{,}02016=0{,}00504$, n'est pas nul : $\sqrt{2\times0{,}00504^2}\approx0{,}0071$. Toute la distance vient ici de l'effet Epps, qui ôte un cinquième au terme croisé. [ajout]

## Point d'arrivée
La volatilité change dans le temps, les corrélations dépendent de la fréquence et des fuseaux horaires, et deux estimations raisonnables d'une même matrice ne coïncident pas. [ajout]

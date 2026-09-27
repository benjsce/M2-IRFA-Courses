---
id: pfo/parcours-rendements
ordre: 1
titre: Du prix affiché au rendement qu'on modélise
source: poly, §1.1–§1.2
---

## Point de départ
Une action est affichée à deux prix : 99,90 pour qui la vend, 100,10 pour qui l'achète. Quel est son prix ? Et quand ce prix passe de 100 à 110 puis à 99, de combien a-t-elle monté ? Les deux questions ont plusieurs réponses. [ajout]

## Étapes
1. pfo/fourchette-bid-ask
   Sur un marché professionnel, la question « quel est le prix ? » n'a pas de réponse unique : le carnet d'ordres en affiche deux à chaque instant. [§1.1]
   Histoire : « 99,90 pour qui la vend, 100,10 pour qui l'achète » — Ces deux prix forment la fourchette, le bid à 99,90 et l'ask à 100,10, et l'écart de 0,20 est ce que coûte un aller-retour immédiat. [ajout]

2. pfo/prix-milieu
   Un modèle, lui, veut un seul nombre. Comment passer des deux prix affichés à un prix unique ? [§1.1.1]
   Histoire : « Quel est son prix ? » — On retient le milieu de la fourchette, $(99{,}90+100{,}10)/2=100{,}00$, à égale distance du prix auquel on peut vendre et de celui auquel on peut acheter. [ajout]

3. pfo/vwap
   Le prix milieu sert au modèle. Celui qui achète vraiment, et en quantité, a un autre souci : ses propres achats font bouger le prix, et ni le prix affiché ni le prix milieu ne disent ce qu'il a payé. Il faut tenir compte des quantités échangées. [§1.1.2]
   Suite : Un fonds achète 400 titres dans la journée : 300 à 100, puis 100 à 101, le prix ayant monté sous l'effet de ses propres achats. Quel prix a-t-il payé ? [ajout]
   Histoire : « Quel prix a-t-il payé » — Ni 100 ni 101 : chaque exécution pèse pour son volume, $(300\times100+100\times101)/400=100{,}25$. [ajout]

4. pfo/passage-aux-rendements
   Une fois le prix choisi, que faut-il modéliser : le prix lui-même, ou ses variations ? [§1.2]
   Suite : Pour modéliser cette action, faut-il décrire ses prix, ou leurs variations ? [ajout]
   Histoire : « faut-il décrire ses prix, ou leurs variations » — Ses variations. Le niveau ne se répète pas : 100, puis 110, puis 99, et rien ne le ramène à une valeur fixe. Les écarts en prix non plus, puisqu'ils grandissent avec le niveau : +10, puis −11. Rapportée au prix de la veille, en revanche, chaque variation garde la même allure d'une période à l'autre, et c'est elle qu'on modélise. [ajout]

5. pfo/rendement-arithmetique
   Première façon de mesurer une variation : la plus intuitive, celle d'un pourcentage. Que se passe-t-il quand on enchaîne deux périodes ? [§1.2.1]
   Histoire : « de combien a-t-elle monté » — Première réponse : +10 %, puis −10 %. Mais ces pourcentages ne s'additionnent pas, ils se composent en se multipliant : 100 devient $100\times1{,}1\times0{,}9=99$, si bien que sur l'ensemble la variation n'est pas nulle, elle vaut $99/100-1=-1\,\%$. [ajout]

6. pfo/rendement-logarithmique
   Existe-t-il une mesure qui s'enchaîne en s'additionnant ? La seconde façon règle ce problème, et c'est elle qu'on emploiera dans toute la suite. [§1.2.1, p. 11]
   Suite : Sur les deux périodes, +10 % puis −10 % ne font pas 0 %. Existe-t-il une mesure de la variation qui s'additionne d'une période à l'autre ? [ajout]
   Histoire : « une mesure de la variation qui s'additionne d'une période à l'autre » — Oui, le rendement logarithmique, seconde réponse à la question du départ : le logarithme du rapport des deux prix, $\ln(110/100)\approx+9{,}53\,\%$, puis $\ln(99/110)\approx-10{,}54\,\%$. Le logarithme changeant le produit des rapports en somme, leur somme, $-1{,}01\,\%$, est exactement le rendement logarithmique sur l'ensemble, $\ln(99/100)$. [ajout]

7. pfo/piege-d-agregation
   Mais ce qui s'enchaîne bien dans le temps s'agrège-t-il aussi bien entre les actifs d'un portefeuille ? [§1.2.2]
   Suite : Un portefeuille place la moitié de son capital dans cette action, qui fait +10 % sur la première période, et l'autre moitié dans une action qui fait −10 %. Son rendement est-il la moyenne de ceux des deux actions ? [ajout]
   Histoire : « Son rendement est-il la moyenne de ceux des deux actions » — En rendements arithmétiques, oui : $\tfrac12\times10\,\%+\tfrac12\times(-10\,\%)=0$, et le portefeuille n'a ni gagné ni perdu. En rendements logarithmiques, non : +10 % et −10 % valent, comme à l'étape précédente, $+9{,}53\,\%$ et $-10{,}54\,\%$, dont la moyenne, $-0{,}50\,\%$, annonce une perte qui n'a pas eu lieu. C'est le piège d'agrégation : les rendements logarithmiques s'additionnent entre dates, pas entre actifs. [ajout]

## Point d'arrivée
Le prix est un choix, le rendement logarithmique est celui du cours, et il a un domaine d'emploi : il s'additionne entre dates, pas entre actifs. [ajout]

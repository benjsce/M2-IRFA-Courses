---
id: pfo/parcours-rendements
ordre: 1
titre: Du prix affiché au rendement qu'on modélise
source: poly, §1.1–§1.2
---

## Point de départ
Une action est affichée à 99,90 à l'achat et à 100,10 à la vente. Quel est son prix ? Et quand ce prix passe de 100 à 110 puis à 99, de combien a-t-elle monté ? Les deux questions ont plusieurs réponses, et le chapitre 1 commence par les trier. [ajout]

## Étapes
1. pfo/fourchette-bid-ask
   Sur un marché professionnel, la question « quel est le prix ? » n'a pas de réponse unique : le carnet d'ordres en affiche deux à chaque instant. [§1.1]
   Histoire : « affichée à 99,90 à l'achat et à 100,10 à la vente » — Ces deux prix forment la fourchette : on peut vendre à 99,90 et acheter à 100,10, et l'écart de 0,20 est ce que coûte un aller-retour immédiat. [ajout]

2. pfo/prix-milieu
   Un modèle, lui, veut un seul nombre. Comment passer des deux prix affichés à un prix unique ? [§1.1.1]
   Histoire : « Quel est son prix ? » — Un modèle veut un seul nombre. On retient le milieu de la fourchette, $(99{,}90+100{,}10)/2=100{,}00$. [ajout]

3. pfo/vwap
   Pour un gros ordre, ni le prix affiché ni la clôture ne disent ce qu'on a vraiment payé : il faut tenir compte des quantités échangées. [§1.1.2]
   Suite : Un fonds achète 400 titres dans la journée : 300 à 100, puis 100 à 101, le prix ayant monté sous l'effet de ses propres achats. Quel prix a-t-il payé ? [ajout]
   Histoire : « Quel prix a-t-il payé » — Ni 100 ni 101 : chaque exécution pèse pour son volume, $(300\times100+100\times101)/400=100{,}25$. [ajout]

4. pfo/passage-aux-rendements
   Une fois le prix choisi, le cours cesse de le modéliser directement, pour une raison statistique. [§1.2]
   Histoire : « quand ce prix passe de 100 à 110 puis à 99 » — Le cours ne modélise pas ces prix eux-mêmes, qui n'ont pas de niveau stable dans le temps, mais leurs variations d'une période à l'autre, dont la loi, elle, reste stable. [ajout]

5. pfo/rendement-arithmetique
   Première façon de mesurer une variation : la plus intuitive, celle d'un pourcentage. Que se passe-t-il quand on enchaîne deux périodes ? [§1.2.1]
   Histoire : « de combien a-t-elle monté » — Première réponse : +10 %, puis −10 %. Mais ces pourcentages ne s'additionnent pas : sur l'ensemble, la variation n'est pas nulle, elle vaut $1{,}1\times0{,}9-1=-1\,\%$. [ajout]

6. pfo/rendement-logarithmique
   La seconde façon règle ce problème d'enchaînement, et c'est elle que tous les listings du cours emploieront. [§1.2.1, p. 11]
   Histoire : « Les deux questions ont plusieurs réponses » — Seconde réponse : $\ln(110/100)\approx+9{,}53\,\%$, puis $\ln(99/110)\approx-10{,}54\,\%$. Leur somme, $-1{,}01\,\%$, est exactement le rendement logarithmique sur l'ensemble, $\ln(99/100)$. [ajout]

7. pfo/piege-d-agregation
   Mais ce qui s'enchaîne bien dans le temps s'agrège-t-il aussi bien entre les actifs d'un portefeuille ? [§1.2.2]
   Suite : Un portefeuille place la moitié de son capital dans cette action, qui fait +10 % sur la première période, et l'autre moitié dans une action qui fait −10 %. Quel est son rendement ? [ajout]
   Histoire : « Quel est son rendement » — Arithmétiquement, $\tfrac12\times10\,\%+\tfrac12\times(-10\,\%)=0$ : le portefeuille n'a ni gagné ni perdu. La moyenne des rendements logarithmiques donne pourtant $-0{,}50\,\%$ : ils s'additionnent entre dates, pas entre actifs. [ajout]

## Point d'arrivée
Le prix est un choix, le rendement logarithmique est celui du cours, et il a un domaine d'emploi : il s'additionne entre dates, pas entre actifs. [ajout]

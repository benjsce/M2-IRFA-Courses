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

2. pfo/prix-milieu
   Un modèle, lui, veut un seul nombre. Comment passer des deux prix affichés à un prix unique ? [§1.1.1]

3. pfo/vwap
   Pour un gros ordre, ni le prix affiché ni la clôture ne disent ce qu'on a vraiment payé : il faut tenir compte des quantités échangées. [§1.1.2]

4. pfo/passage-aux-rendements
   Une fois le prix choisi, le cours cesse de le modéliser directement, pour une raison statistique. [§1.2]

5. pfo/rendement-arithmetique
   Première façon de mesurer une variation : la plus intuitive, celle d'un pourcentage. Que se passe-t-il quand on enchaîne deux périodes ? [§1.2.1]

6. pfo/rendement-logarithmique
   La seconde façon règle ce problème d'enchaînement, et c'est elle que tous les listings du cours emploieront. [§1.2.1, p. 11]

7. pfo/piege-d-agregation
   Mais ce qui s'enchaîne bien dans le temps s'agrège-t-il aussi bien entre les actifs d'un portefeuille ? [§1.2.2]

## Point d'arrivée
Le prix est un choix, le rendement logarithmique est celui du cours, et il a un domaine d'emploi : il s'additionne entre dates, pas entre actifs. [ajout]

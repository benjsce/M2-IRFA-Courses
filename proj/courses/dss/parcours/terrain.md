---
id: dss/parcours-terrain
ordre: 7
titre: Les modèles face aux données réelles
source: slides 203–237
---

## Point de départ
La banque sait maintenant apprendre à prévoir le défaut de plusieurs façons : modèles linéaires contraints, forêts d'arbres, boosting, réseaux de neurones. Le cours les met toutes en concurrence sur un même jeu de crédit, 12 544 entreprises du périmètre européen décrites par 343 variables, dont on sait si elles ont fait défaut. Laquelle choisir ? [slide 204, slide 205]

## À savoir avant
- dss/scoring-de-credit : c'est le problème sur lequel les modèles sont comparés. [slide 204]
- dss/courbe-roc : c'est l'étalon de la comparaison ; l'article superpose les courbes des modèles pour les départager. [slide 213]
- dss/lasso : c'est le représentant des modèles linéaires contraints dans la comparaison. [slide 204]
- dss/foret-aleatoire : c'est l'un des deux ensembles d'arbres mis en concurrence. [slide 204]
- dss/boosting : c'est l'autre. [slide 204]
- dss/retropropagation : elle représente les réseaux de neurones dans la comparaison. [slide 204]
- dss/preparation-des-donnees : elle précède le rééquilibrage des classes, qui en est une forme. [slide 229]
- dss/importance-des-variables : c'est par elle qu'on voit quelles variables portent le biais. [slide 220]

## Étapes
1. dss/comparaison-de-modeles
   Tous sont jugés à la même mesure : le GINI, lu sur leurs courbes ROC superposées. [slide 204, slide 205]
   Histoire : « Laquelle choisir » — Pas celle qu'on attend. La forêt aléatoire l'emporte avec 57,84, contre 51,36 pour la régression logistique, le modèle classique qui change une combinaison linéaire des variables en probabilité de défaut : 6,48 points de mieux. Mais le boosting tombe à 44,16, l'apprentissage profond à 44,92, et le séparateur à vaste marge, ou SVM, qui sépare les deux classes par la frontière la plus éloignée des exemples de chacune, à 28,38, soit 22,98 points sous la régression logistique. Plusieurs méthodes réputées avancées font moins bien que le modèle classique. [ajout]

2. dss/smote
   Bien classer les demandeurs ne dit pas ce qu'un modèle a appris d'autre que le risque. Le cours se termine sur une seconde étude qui le cherche, et bute d'abord sur une difficulté de données. [slide 229]
   Suite : Elle veut savoir si les autres variables d'un client permettent de prédire son genre, ce qu'un modèle de crédit pourrait alors apprendre sans qu'on le lui donne. Mais les groupes à comparer sont de tailles très inégales : comment apprendre une classe bien plus rare que l'autre ? [slide 227, ajout]
   Histoire : « comment apprendre une classe bien plus rare que l'autre » — Entraîné tel quel sur ces groupes inégaux, un classifieur apprendrait surtout à répondre le genre le plus nombreux, sans rien lire dans les autres variables. SMOTE complète d'abord le groupe rare : chaque client synthétique est pris entre un client de ce groupe et l'un de ses voisins du même groupe, sur le segment qui les joint ; aucun n'est recopié, c'est ce qui le sépare d'un simple sur-échantillonnage, et les deux genres se comparent à nombre égal. [slide 229, ajout]

3. dss/biais-societal
   Les groupes rendus comparables, le genre du client se lit-il dans ses autres variables ? [slide 218]
   Histoire : « si les autres variables d'un client permettent de prédire son genre » — Oui : on peut prédire le genre à partir d'elles, si bien qu'un modèle entraîné sans la variable de genre peut reproduire le traitement inégal selon le genre que reflètent les défauts passés. Le cours en conclut que l'apprentissage fait prospérer les biais sociaux en répliquant les motifs qu'il apprend, et qu'un biais social devient sociétal quand il devient la norme. [slide 218, slide 233, slide 235, ajout]

## Point d'arrivée
Un modèle se juge sur des données réelles et contre les autres modèles ; et bien prédire n'est pas tout, puisqu'il reproduit fidèlement les biais de ce qu'il apprend. [ajout]

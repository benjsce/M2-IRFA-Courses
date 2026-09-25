---
id: dss/parcours-terrain
ordre: 7
titre: Les modèles face aux données réelles
source: slides 203–237
---

## Point de départ
Sur 1 000 demandes de crédit, 30 finissent en défaut : un modèle qui prédit toujours « pas de défaut » a raison dans 97 % des cas, et ne détecte aucun défaut. [ajout]

Le cours se termine sur deux articles qui mettent ses méthodes à l'épreuve : l'un compare tous les modèles sur un même problème de crédit, l'autre montre ce qu'ils apprennent quand les données sont biaisées. [slide 204, slide 218]

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
   Sur un même jeu de risque de crédit, quel modèle du cours fait le mieux ? [slide 204, slide 205]

2. dss/smote
   Dans les données de crédit, les défauts sont rares. Comment apprendre une classe presque absente ? [slide 229]

3. dss/biais-societal
   Même bien entraîné, un modèle apprend ce que ses données contiennent, y compris ce qu'on ne voudrait pas qu'il reproduise. [slide 218]

## Point d'arrivée
Un modèle se juge sur des données réelles et contre les autres modèles ; et bien prédire n'est pas tout, puisqu'il reproduit fidèlement les biais de ce qu'il apprend. [ajout]

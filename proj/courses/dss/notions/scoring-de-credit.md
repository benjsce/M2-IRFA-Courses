---
id: dss/scoring-de-credit
nom: Scoring de crédit
type: notion
statut: source
construite_a_partir_de:
- dss/apprentissage-supervise
alias:
- credit scoring
refs:
- slide 17
- slide 204
- slide 205
---

## Ce que c'est
Prédire le défaut d'une contrepartie à partir de ses caractéristiques, pour décider d'un octroi, d'un suivi ou d'un recouvrement. [slide 17]

## Ce qui la définit
L'étiquette est un binaire — l'entité a fait défaut ou non — et les variables explicatives décrivent l'entité. Sur le jeu du cours : 12 544 entreprises du périmètre européen, 343 variables de chiffre d'affaires, de marge et autres, un facteur binaire de défaut. [slide 205]

La mesure d'usage n'est pas l'exactitude mais le GINI, lu sur la courbe ROC. C'est ce qui rend les modèles comparables d'une étude à l'autre. [slide 12, slide 17]


## Le chemin jusqu'ici
Tout repose sur dss/apprentissage-supervise : l'étiquette de défaut est connue, et c'est ce qui rend le problème traitable. [ajout]

Le scoring apparaît tôt comme une application parmi d'autres, et revient à la fin comme le terrain des deux articles. C'est la seule application du cours à faire ce trajet complet. [ajout]

## Exemple minimal
Sur le jeu du cours, la régression logistique donne un GINI de 51,36 et la forêt aléatoire 57,84. [slide 17]

## Cesse d'être valide quand
Le cours conclut que seuls des cadres dynamiques sont viables, et que la gouvernance du risque de modèle y est aujourd'hui inadaptée. [slide 214]

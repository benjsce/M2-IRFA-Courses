---
id: dss/moindres-carres-ordinaires
nom: Moindres carrés ordinaires
type: notion
statut: source
construite_a_partir_de:
- dss/apprentissage-supervise
alias:
- OLS
- ordinary least squares
refs:
- slide 25
- slide 26
- slide 48
---

## Ce que c'est
L'ajustement d'un modèle linéaire par minimisation de la somme des carrés des résidus. [slide 48]

## Forme
$$\mathrm{RSS}=\sum_{i=1}^{n}\Big(y_i-\beta_0-\sum_{j=1}^{p}\beta_jx_{ij}\Big)^2$$ [slide 48]

## Ce qui la définit
L'estimateur a un biais faible et une variabilité faible tant que la relation est linéaire et que $n\gg p$. Tout le chapitre tient dans ce que devient cette phrase quand l'inégalité se referme. [slide 26]

Si $n$ n'est pas beaucoup plus grand que $p$, l'ajustement devient très variable ; si $p>n$, la variance des estimateurs est infinie et la solution n'est même plus unique. [slide 26, slide 56]


## Le chemin jusqu'ici
dss/apprentissage-supervise suffit : il donne les couples de prédicteurs et de réponse que l'ajustement consomme. [ajout]

Les moindres carrés ne sont pas une méthode parmi d'autres mais le point de départ que tout le chapitre cherche à améliorer. C'est pourquoi leur socle est aussi court. [ajout]

## Exemple minimal
Avec $p=3$ prédicteurs et $n=1000$ observations, l'ajustement est stable ; avec $n=4$, il passe exactement par les points et ne dit plus rien. [ajout]

## Geste de calcul type
Avant toute chose, comparer $n$ et $p$ : c'est ce rapport, et non la qualité de l'ajustement observée, qui dit si l'estimateur est utilisable. [slide 26]

## Cesse d'être valide quand
Échoue complètement dès que $p>n$. C'est exactement le domaine où la régularisation et la réduction de dimension deviennent nécessaires. [slide 56, slide 91]

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

## Ce que les symboles modélisent
$n$ compte les observations et $p$ les prédicteurs ; c'est leur rapport qui décide de tout, un modèle où $p$ approche $n$ s'ajustant parfaitement sans rien avoir appris. RSS est ce qu'on minimise : une somme de carrés, donc un montant d'erreur et non un taux. [slide 26, slide 48]

$x_{ij}$ est la valeur du prédicteur $j$ pour l'observation $i$, et $y_i$ la réponse observée. $\beta_j$ est le coefficient du prédicteur $j$ : de combien la prédiction bouge quand ce prédicteur augmente d'une unité, les autres restant fixes ; $\beta_0$ est la constante. [ajout]

## Ce qui la définit
L'estimateur a un biais faible et une variabilité faible tant que la relation est linéaire et que $n\gg p$. Tout le chapitre tient dans ce que devient cette phrase quand l'inégalité se referme. [slide 26]

Si $n$ n'est pas beaucoup plus grand que $p$, l'ajustement devient très variable ; si $p>n$, la variance des estimateurs est infinie et la solution n'est même plus unique. [slide 26, slide 56]


## Le chemin jusqu'ici
dss/apprentissage-supervise suffit : il donne les couples de prédicteurs et de réponse que l'ajustement consomme. [ajout]

Les moindres carrés ne sont pas une méthode parmi d'autres mais le point de départ que tout le chapitre cherche à améliorer. C'est pourquoi leur socle est aussi court. [ajout]

## Exemple minimal
Sur les 20 clients, la régression de la perte sur l'endettement $x_1$ et le revenu $x_2$ donne $\hat y=3{,}30+0{,}076\,x_1-0{,}060\,x_2$ et une RSS de 22,43, quand la règle qui a servi à simuler les données est $y=2+0{,}10\,x_1-0{,}05\,x_2$ plus un bruit. [ajout]

## Geste de calcul type
Avant toute chose, comparer $n$ et $p$ : c'est ce rapport, et non la qualité de l'ajustement observée, qui dit si l'estimateur est utilisable. [slide 26]

Ici $n=20$ et $p=2$ : l'ajustement est utilisable. Avec 19 prédicteurs pour ces 20 clients, il passerait exactement par les points, avec une RSS nulle, et ne dirait plus rien. [ajout]

## Cesse d'être valide quand
Échoue complètement dès que $p>n$. C'est exactement le domaine où la régularisation et la réduction de dimension deviennent nécessaires. [slide 56, slide 91]

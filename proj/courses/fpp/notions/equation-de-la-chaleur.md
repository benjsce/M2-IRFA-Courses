---
id: fpp/equation-de-la-chaleur
nom: Réduction à l’équation de la chaleur
type: notion
statut: source
construite_a_partir_de:
- fpp/feynman-kac
alias:
- heat equation
refs:
- §7.2.2
- éq. 20
- éq. 21
---

## Ce que c'est
Deux changements de variables ramènent l’équation de Black et Scholes à l’équation de la chaleur. [§7.2.2]

## Forme
$$\dfrac{\partial C}{\partial t}+\tfrac12\sigma^2\dfrac{\partial^2C}{\partial x^2}=0,\qquad C(T,x)=(e^x-K)^+$$ [éq. 20, éq. 21]

## Ce qui la définit
Trois gestes successifs : multiplier par $e^{r(T-t)}$ pour passer au prix forward, ce qui fait disparaître le terme $rC$ ; prendre le prix forward du sous-jacent au lieu du comptant ; prendre le logarithme du prix au lieu du prix. [§7.2.2]

Le passage au forward est possible parce que les dérivées en espace de $F$ et de $C$ sont proportionnelles, alors que les dérivées en temps diffèrent exactement du terme d’actualisation. [§7.2.2]

## Le chemin jusqu'ici
C'est le socle le plus long du cours, et il n'est long que parce que cette fiche est la dernière. [ajout]

**Le prix.** fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre. [ajout]

**L'aléa.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes. [ajout]

**L'équation.** fpp/compte-capitalise donne fpp/replication-dynamique, d'où fpp/edp-black-scholes, dont fpp/feynman-kac donne la lecture probabiliste. [ajout]

Rien n'est ajouté ici sur le plan financier : deux changements de variables, et l'équation devient l'équation de la chaleur. Il a fallu tout construire pour y arriver ; cette fiche, elle, ne fait que la réécrire. C'est la seule étape purement mathématique. [ajout]

## Exemple minimal
Le facteur du changement de variable est $e^{r(T-t)}$ : à un an et 4 %, il vaut 1,0408. [ajout]

## Geste de calcul type
Pour reconnaître un problème de Black et Scholes déguisé : chercher si un passage au forward et un passage au logarithme annulent le terme d’ordre zéro et le terme de dérive. [§7.2.2]

## Cesse d'être valide quand
La réduction suppose $r$ et $\sigma$ constants. Avec des coefficients dépendant du temps il reste une équation de la chaleur à temps changé ; avec des coefficients dépendant du niveau, elle ne tient plus. [ajout]

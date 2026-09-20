---
id: fpp/vega
nom: Vega
symbole: $\mathcal{V}$
type: notion
statut: source
cas_de: fpp/sensibilite
valeur: la volatilité
construite_a_partir_de:
- fpp/formule-black-scholes
alias:
- vega de Black et Scholes
refs:
- §8.2
---

## Ce que c'est
De combien le prix bouge quand la volatilité bouge. [§8.2]

## Forme
$$\mathcal{V}=\dfrac{\partial P}{\partial\sigma}$$ [§8.2]

## Ce qui la définit
Positif pour le call comme pour le put : plus d’incertitude vaut plus cher des deux côtés, parce que le payoff est convexe. [§8.2]

La table écrit $SN(d_1)\sqrt{\tau}$ avec la fonction de répartition ; c’est la densité qu’il faut, $S\,n(d_1)\sqrt{\tau}$. Sur l’exemple courant la première donnerait 61,79, la seconde 38,14, et l’effet mesuré est 38,17 par unité de volatilité. [ajout]

## Le chemin jusqu'ici
Le socle est celui de fpp/formule-black-scholes, la formule elle-même en plus : tout y sert à l'écrire, et cette fiche ne fait que la dériver. Trois fils y mènent. [ajout]

**Le prix.** fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre : à ce stade, un prix est une espérance actualisée. [ajout]

**L'aléa.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes. [ajout]

**Le contrat.** fpp/payoff puis fpp/option disent ce qu'on évalue, et les trois se nouent dans fpp/formule-black-scholes. [ajout]

Ce qui distingue les grecques entre elles, c'est la variable dérivée, pas le chemin — celui-ci est le même pour toutes et ne vaut la peine d'être lu qu'une fois. Le véga est la dérivée par rapport à la **volatilité** — seule grecque à dériver par rapport à un paramètre que le modèle suppose constant, et c'est ce paradoxe qui en fait la plus employée. [ajout]

## Exemple minimal
Passer la volatilité de 20 % à 21 % fait passer le call de 9,93 à 10,30 : le vega vaut 0,38 par point de volatilité. [ajout]

## Geste de calcul type
Multiplier le vega par la variation de volatilité exprimée en points : c’est ainsi qu’on lit une position en volatilité. [§8.2]

## Cesse d'être valide quand
Le paramètre dérivé est justement celui que le modèle suppose constant : dériver par rapport à lui, c’est déjà sortir du modèle. [ajout]

## Origine
- exercice fpp/ex-15 : pour choisir une stratégie de volatilité, on ne regarde pas le profil de gain mais le signe du véga — le profil ne distingue pas l'achat de straddle de la vente de butterfly [ajout]

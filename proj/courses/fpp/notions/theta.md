---
id: fpp/theta
nom: Theta
symbole: $\Theta$
type: notion
statut: source
cas_de: fpp/sensibilite
valeur: le temps qui passe
construite_a_partir_de:
- fpp/formule-black-scholes
alias:
- theta de Black et Scholes
refs:
- §8.2
---

## Ce que c'est
De combien le prix bouge quand le temps passe. [§8.2]

## Forme
$$\Theta=\dfrac{\partial P}{\partial t}$$ [§8.2]

## Ce que les symboles modélisent
$\Theta$ mesure ce que le seul passage du temps fait au prix, tout le reste étant tenu fixe. C'est la seule des sensibilités dont la variable ne soit pas un aléa : le temps passe à coup sûr. [§8.2]

## Ce qui la définit
Négatif pour l’acheteur d’option dans presque tous les cas : la valeur temps s’érode à mesure que l’échéance approche. [§8.2]

## Le chemin jusqu'ici
Le socle est celui de fpp/formule-black-scholes, la formule elle-même en plus : tout y sert à l'écrire, et cette fiche ne fait que la dériver. Trois fils y mènent. [ajout]

**Le prix.** fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre : à ce stade, un prix est une espérance actualisée. [ajout]

**L'aléa.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes. [ajout]

**Le contrat.** fpp/payoff puis fpp/option disent ce qu'on évalue, et les trois se nouent dans fpp/formule-black-scholes. [ajout]

Ce qui distingue les grecques entre elles, c'est la variable dérivée, pas le chemin — celui-ci est le même pour toutes et ne vaut la peine d'être lu qu'une fois. Le thêta est la dérivée par rapport au **temps** : ce que coûte l'attente. Il est le pendant du gamma, l'équation de Black et Scholes les liant terme à terme. [ajout]

## Exemple minimal
Le call à la monnaie de l’exemple courant porte 6,00 de valeur temps, qui s’annule entièrement à l’échéance. [ajout]

## Geste de calcul type
Le theta est le loyer du gamma : ce qu’on paie chaque jour pour détenir de la convexité. [ajout]

## Cesse d'être valide quand
La table marque ce signe d’un astérisque, « presque toujours vrai » : les exceptions existent, notamment pour un put très en dedans. [§8.2]

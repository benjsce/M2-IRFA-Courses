---
id: fpp/sensibilite
nom: Sensibilité
type: abstraite
statut: source
cas_de: fpp/couverture
parametre: la variable par rapport à laquelle on dérive le prix
construite_a_partir_de: []
alias:
- greeks
- grecques
- sensitivities
refs:
- §8.1
- §8.2
---

## Ce que c'est
La dérivée d’un prix par rapport à l’un des paramètres dont il dépend. [§8.1]

## Ce que les membres partagent
Toutes répondent à la même question posée sur une variable différente : de combien bouge le prix si ce paramètre bouge d’une unité. [§8.1, §8.2]

Chacune se couvre en prenant la position opposée dans un instrument qui a la même sensibilité : de l'action pour le delta, une autre option pour le vega, un autre titre de taux pour la duration. Seul le theta n'a rien à couvrir, car le temps n'est pas un aléa : il passe à coup sûr. [ajout]

## Pourquoi ce niveau existe
Le cours présente ces dérivées dans une seule table ; elles ne diffèrent que par la variable dérivée. Les séparer sans les réunir ferait perdre que, pour chaque risque, couvrir est le même geste. [§8.2]

## Exemple minimal
Le call de strike 100 à un an, sur une action à 100, avec un taux de 4 % et une volatilité de 20 %, vaut 9,93. Ses sensibilités : delta 0,618 par unité d'action, gamma 0,019, vega 0,38 par point de volatilité, theta −5,89 par an (−0,016 par jour), rho 0,52 par point de taux. [ajout]

## Cesse d'être valide quand
Une sensibilité est locale : elle vaut au point où elle est calculée et se périme dès que le paramètre bouge. Le gamma mesure précisément cette péremption pour le delta. [ajout]

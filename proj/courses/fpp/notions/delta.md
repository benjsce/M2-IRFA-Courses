---
id: fpp/delta
nom: Delta
symbole: $\delta$
type: notion
statut: source
cas_de: fpp/sensibilite
valeur: le sous-jacent, au premier ordre
construite_a_partir_de:
- fpp/formule-black-scholes
alias:
- delta de Black et Scholes
refs:
- §8.2
---

## Ce que c'est
De combien le prix de l’option bouge quand le sous-jacent bouge d’une unité. [§8.2]

## Forme
$$\delta=\dfrac{\partial P}{\partial S}=N(d_1)$$ [§8.2]

## Ce qui la définit
C’est exactement la quantité de sous-jacent à détenir en sens inverse pour annuler le risque au premier ordre : le delta *est* la couverture, c’est le $\delta$ du §7.1. [§7.1, §8.2]

## Exemple minimal
Pour le call à la monnaie de l’exemple courant : $\delta=N(0{,}3)=0{,}618$, soit 0,618 action à vendre par call acheté. [ajout]

## Geste de calcul type
Lire $N(d_1)$. Il tend vers 0 très en dehors de la monnaie et vers 1 très en dedans : le delta est aussi, sous $\mathbb{Q}$, la probabilité approchée d’exercer. [§8.2]

## Cesse d'être valide quand
Ne vaut qu’au premier ordre et qu’à l’instant présent ; le gamma dit à quelle vitesse il se périme. [§8.2]

## Origine
- exercice fpp/ex-08 : un dividende de 0,988 au comptant ne coûte que 0,654 au call. La lecture « dividende × delta » donne 0,652 : le delta est l'outil de première approximation [exo. 8]

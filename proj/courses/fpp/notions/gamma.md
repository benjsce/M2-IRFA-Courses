---
id: fpp/gamma
nom: Gamma
symbole: $\gamma$
type: notion
statut: source
cas_de: fpp/sensibilite
valeur: le sous-jacent, au second ordre
construite_a_partir_de:
- fpp/formule-black-scholes
alias:
- gamma de Black et Scholes
refs:
- §8.2
---

## Ce que c'est
De combien le delta bouge quand le sous-jacent bouge. [§8.2]

## Forme
$$\gamma=\dfrac{\partial^2P}{\partial S^2}$$ [§8.2]

## Ce qui la définit
Il mesure la courbure du prix en le sous-jacent, donc la fréquence à laquelle il faut refaire la couverture en delta. [§8.2]

La table écrit $n(d_1)$ ; l’expression complète est $n(d_1)/(S\sigma\sqrt{\tau})$, la table ne donnant que le facteur qui dépend de $d_1$. [ajout]

## Exemple minimal
Passer le sous-jacent de 100 à 101 fait passer le delta de 0,618 à 0,637 : le gamma vaut environ 0,019. [ajout]

## Geste de calcul type
Un gamma élevé signale qu’une couverture en delta se dégradera vite ; c’est ce qui rend la couverture coûteuse près de la monnaie et près de l’échéance. [§8.2]

## Cesse d'être valide quand
Calculé dans le modèle de Black et Scholes : une volatilité non constante le déplace. [ajout]

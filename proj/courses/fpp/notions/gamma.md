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

## Ce que les symboles modélisent
$\gamma$ est la dérivée du delta, donc la dérivée seconde du prix : elle dit de combien la couverture doit être réajustée quand le sous-jacent bouge. Une couverture qui ne regarde que le delta suppose implicitement qu'elle est petite. [§8.2]

## Ce qui la définit
Il mesure la courbure du prix en le sous-jacent, donc la fréquence à laquelle il faut refaire la couverture en delta. [§8.2]

La table écrit $n(d_1)$ ; l’expression complète est $n(d_1)/(S\sigma\sqrt{\tau})$, la table ne donnant que le facteur qui dépend de $d_1$. [ajout]

## Le chemin jusqu'ici
Le socle est celui de fpp/formule-black-scholes, la formule elle-même en plus : tout y sert à l'écrire, et cette fiche ne fait que la dériver. Trois fils y mènent. [ajout]

**Le prix.** fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre : à ce stade, un prix est une espérance actualisée. [ajout]

**L'aléa.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes. [ajout]

**Le contrat.** fpp/payoff puis fpp/option disent ce qu'on évalue, et les trois se nouent dans fpp/formule-black-scholes. [ajout]

Ce qui distingue les grecques entre elles, c'est la variable dérivée, pas le chemin — celui-ci est le même pour toutes et ne vaut la peine d'être lu qu'une fois. Le gamma est la dérivée **seconde** par rapport au comptant : il mesure à quelle vitesse la couverture se périme, donc à quelle fréquence rééquilibrer. [ajout]

## Exemple minimal
Passer le sous-jacent de 100 à 101 fait passer le delta de 0,618 à 0,637 : le gamma vaut environ 0,019. [ajout]

## Geste de calcul type
Un gamma élevé signale qu’une couverture en delta se dégradera vite ; c’est ce qui rend la couverture coûteuse près de la monnaie et près de l’échéance. [§8.2]

## Cesse d'être valide quand
Calculé dans le modèle de Black et Scholes : une volatilité non constante le déplace. [ajout]

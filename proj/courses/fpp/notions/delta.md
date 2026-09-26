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

## Ce que les symboles modélisent
$\delta$ est une dérivée : de combien le prix bouge pour une unité de sous-jacent. C'est un rapport de deux prix, donc un nombre sans unité, et c'est ce qui permet de le lire directement comme une quantité de sous-jacent à détenir. [§8.2]

## Ce qui la définit
C’est exactement la quantité de sous-jacent à détenir en sens inverse pour annuler le risque au premier ordre : le delta *est* la couverture, c’est le $\delta$ du §7.1. [§7.1, §8.2]

## Le chemin jusqu'ici
Le socle est long, mais il ne raconte qu'une seule histoire, en trois temps. [ajout]

**Poser le prix.** fpp/replication-statique, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) se combinent en fpp/prix-a-terme, d'où sort fpp/mesure-risque-neutre : à ce stade, un prix est une espérance actualisée. [ajout]

**Poser l'aléa.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent de combien le sous-jacent bouge et comment cela grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes. [ajout]

**Poser le contrat.** fpp/payoff puis fpp/option disent ce qu'on évalue. Les trois fils se nouent dans fpp/formule-black-scholes — et le delta en est simplement la dérivée par rapport au comptant. [ajout]

C'est pourquoi ce socle est long sans être difficile : presque tout sert à écrire la formule, et le delta n'en est que la dérivée. [ajout]

## Exemple minimal
Pour le call à la monnaie de l’exemple courant : $\delta=N(0{,}3)=0{,}618$, soit 0,618 action à vendre par call acheté. [ajout]

![Le prix du call de l'exemple selon le sous-jacent, et sa tangente en 100, de pente 0,618. Au voisinage de 100, le call se comporte comme 0,618 action, ce qui est la couverture ; plus loin, la courbe s'écarte de la tangente.](figures/delta.svg) [ajout]

## Geste de calcul type
Lire $N(d_1)$. Il tend vers 0 très en dehors de la monnaie et vers 1 très en dedans : le delta est aussi, sous $\mathbb{Q}$, la probabilité approchée d’exercer. [§8.2]

## Cesse d'être valide quand
Ne vaut qu’au premier ordre et qu’à l’instant présent ; le gamma dit à quelle vitesse il se périme. [§8.2]

## Origine
- exercice fpp/ex-08 : un dividende de 0,988 au comptant ne coûte que 0,654 au call. La lecture « dividende × delta » donne 0,652 : le delta est l'outil de première approximation [exo. 8]

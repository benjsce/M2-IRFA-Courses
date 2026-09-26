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
$$\delta=\dfrac{\partial P}{\partial S},\qquad\text{pour un call : }\delta=N(d_1),\qquad\text{pour un put : }\delta=N(d_1)-1$$ [§8.2, ajout]

## Ce que les symboles modélisent
$\delta$ est une dérivée : de combien le prix bouge pour une unité de sous-jacent. C'est un rapport de deux prix, donc un nombre sans unité, et c'est ce qui permet de le lire directement comme une quantité de sous-jacent. [§8.2]

$P$ est ici le prix d'une option quelconque, call ou put, comme dans la table du §8.2 : la même lettre y désigne ailleurs le put seul, et $N(d_1)$ n'est le delta que du call. [§8.2, ajout]

Au §7.1, la même lettre $\delta$ désigne autre chose : la quantité d'actions *détenue* contre une option achetée, qui est l'opposé de cette dérivée. Pour le call de l'exemple, le delta de cette fiche vaut $+0{,}618$ et le $\delta$ du §7.1 vaut $-0{,}618$ action. Les deux notations sont celles du poly ; il ne les distingue pas. [§7.1, §8.2, ajout]

## Ce qui la définit
**On connaît** la courbe du prix du call selon le cours de l'action. **On cherche** combien d'actions bougent comme lui au voisinage du cours d'aujourd'hui. Le delta est la pente qui répond : la tangente à la courbe est la valeur d'un portefeuille de 0,618 action, complété par un emprunt. [ajout]

C’est donc la quantité de sous-jacent à détenir en sens inverse pour annuler le risque au premier ordre : le delta *est* la couverture. [§7.1, §8.2]

## Le chemin jusqu'ici
Le socle est long, mais il ne raconte qu'une seule histoire, en trois temps : presque tout sert à écrire la formule, et le delta n'en est que la dérivée. [ajout]

**Poser le prix.** fpp/replication-statique, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) se combinent en fpp/prix-a-terme, d'où sort fpp/mesure-risque-neutre : à ce stade, un prix est une espérance actualisée. [ajout]

**Poser l'aléa.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent de combien le sous-jacent bouge et comment cela grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes. [ajout]

**Poser le contrat.** fpp/payoff puis fpp/option disent ce qu'on évalue. Les trois fils se nouent dans fpp/formule-black-scholes — et le delta en est simplement la dérivée par rapport au comptant. [ajout]

## Exemple minimal
Le call de l'exemple courant : action à 100, strike 100, taux 4 %, volatilité 20 %, un an ; il vaut 9,93. Son delta vaut $N(0{,}3)=0{,}618$ : 0,618 action à vendre par call acheté. Le put de mêmes caractéristiques a pour delta $-0{,}382$. [ajout]

![Le prix du call de l'exemple selon le sous-jacent, et sa tangente en 100, de pente 0,618. Au voisinage de 100, le call se comporte comme 0,618 action, ce qui est la couverture ; plus loin, la courbe s'écarte de la tangente.](figures/delta.svg) [ajout]

## Geste de calcul type
Lire $N(d_1)$, avec $d_1=\big(\ln(S/K)+(r+\sigma^2/2)\,\tau\big)/(\sigma\sqrt{\tau})$ : ici $d_1=(0+0{,}04+0{,}02)/0{,}2=0{,}3$ et $N(0{,}3)=0{,}618$. Il tend vers 0 très en dehors de la monnaie et vers 1 très en dedans. [§8.2, ajout]

Ce n'est pas la probabilité d'exercer : sous $\mathbb{Q}$, celle-ci vaut $N(d_2)=N(0{,}1)=0{,}540$ ; $N(d_1)$ en est proche sans l'être. [ajout]

## Cesse d'être valide quand
Ne vaut qu’au premier ordre et qu’à l’instant présent ; le gamma dit à quelle vitesse il se périme. [§8.2]

## Origine
- exercice fpp/ex-08 : un dividende de 0,988 au comptant ne coûte que 0,654 au call. La lecture « dividende × delta » donne 0,652 : le delta est l'outil de première approximation [exo. 8]

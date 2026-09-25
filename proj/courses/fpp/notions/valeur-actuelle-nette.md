---
id: fpp/valeur-actuelle-nette
nom: Valeur actuelle nette
symbole: $\mathrm{NPV}$
type: notion
statut: source
cas_de: fpp/operateur-de-prix
valeur: flux certains
construite_a_partir_de:
- fpp/facteur-actualisation
alias:
- NPV
- net present value
refs:
- Déf. 4
---

## Ce que c'est
La somme d’un échéancier de flux certains, ramenés à une même date. [Déf. 4]

## Forme
$$\mathrm{NPV}(t)=\sum_i P(t,t_i)X_i$$ [Déf. 4]

## Ce que les symboles modélisent
$\mathrm{NPV}$ est un montant rapporté à une date, obtenu en y ramenant des flux échelonnés. Elle suppose ces flux **certains** : l'actualisation y fait tout le travail, et aucune probabilité n'intervient. [Déf. 4]

## Retrouver la formule
![Chaque flux revient en $t$ par le facteur de sa propre date, puis les valeurs ramenées s'additionnent. Trois flux comme dans l'exemple minimal, sans ses nombres.](figures/valeur-actuelle-nette.svg) [ajout]

Un flux certain $X_i$ payé en $t_i$, ce sont $X_i$ zéro-coupons d'échéance $t_i$ : chacun vaut $P(t,t_i)$ aujourd'hui, le flux vaut donc $P(t,t_i)X_i$. [ajout]

L'échéancier est la somme de ces flux, et les prix s'additionnent : si l'ensemble valait plus que la somme de ses morceaux, on achèterait les morceaux pour revendre l'ensemble. [ajout]

$$\mathrm{NPV}(t)=\sum_i P(t,t_i)X_i$$ [Déf. 4]

## Ce qui la définit
Elle se transporte à n’importe quelle date par une division : $\mathrm{NPV}(t_k)=\mathrm{NPV}(t)/P(t,t_k)$. [Déf. 4]

## Le chemin jusqu'ici
fpp/convention-capitalisation puis fpp/facteur-actualisation donnent le prix d'un flux unique. [ajout]

La valeur actuelle nette est l'étape où l'on passe d'un flux à un échéancier, et elle ne demande qu'une chose de plus : que les prix s'additionnent. C'est cette linéarité, et non une hypothèse nouvelle, qui autorise à sommer. [ajout]

## Exemple minimal
Trois flux de 100 en 1, 2 et 3 ans, courbe plate à 4 % : $\mathrm{NPV}(0)=277{,}08$. [ajout]

## Geste de calcul type
Actualiser flux par flux, puis sommer : trois flux de 100 à un, deux et trois ans sur une courbe plate à 4 % valent 277,08. Pour transporter la valeur en $t_k$, diviser par $P(t,t_k)$. [Déf. 4]

## Cesse d'être valide quand
Elle ne vaut que pour des flux certains. [Déf. 4]

Dès qu’ils sont aléatoires, il faut passer sous $\mathbb{Q}$. [§5.1]

## Origine
- exercice fpp/ex-19 : la NPV d'une stratégie de refinancement ne dépend que du rapport $P(0,T)/\big(P(0,t)P(t,T)\big)$ ; les notionnels disparaissent [exo. 19]

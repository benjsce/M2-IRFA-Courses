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
$\mathrm{NPV}$ est un montant rapporté à une date, obtenu en y ramenant des flux échelonnés. $X_i$ est le flux payé à la date $t_i$, et $P(t,t_i)$ le prix en $t$ d'un euro payé à cette date. Les flux sont supposés **certains** : l'actualisation y fait tout le travail, et aucune probabilité n'intervient. [Déf. 4]

## Retrouver la formule
![Deux flux de 100, dans un an et dans deux ans. Chacun revient en $t$ par le prix du zéro-coupon de sa propre date, 0,9608 et 0,9048, et vaut 96,08 et 90,48 ; l'échéancier vaut leur somme, 186,56.](figures/valeur-actuelle-nette.svg) [ajout]

**Connu** : un placement qui paie 100 dans un an et 100 dans deux ans, et le prix aujourd'hui d'un euro payé à chacune de ces dates, $P(t,t+1)=0{,}9608$ et $P(t,t+2)=0{,}9048$. **Cherché** : ce que vaut le placement aujourd'hui. [ajout]

Un flux de 100 payé dans un an, ce sont 100 zéro-coupons d'échéance un an : il vaut $100\times0{,}9608=96{,}08$. De même, le flux de deux ans vaut $100\times0{,}9048=90{,}48$. Chaque flux a son propre prix, celui de sa date. [Déf. 3, ajout]

Le placement est la somme de ces deux flux, et les prix s'additionnent : si l'ensemble valait plus que la somme de ses morceaux, on achèterait les morceaux pour revendre l'ensemble. Il vaut $96{,}08+90{,}48=186{,}56$. [ajout]

$$\mathrm{NPV}(t)=\sum_i P(t,t_i)X_i$$ [Déf. 4]

## Ce qui la définit
Des flux certains, chacun évalué au prix du zéro-coupon de sa date, puis additionnés. [Déf. 4]

Elle s'exprime à n'importe quelle autre date $t_k$ en la divisant par $P(t,t_k)$ : diviser par ce prix, c'est capitaliser de $t$ à $t_k$, comme pour un seul euro. [Déf. 4, ajout]

## Le chemin jusqu'ici
fpp/convention-capitalisation relie un taux affiché à ce que devient un euro placé, et fpp/facteur-actualisation en tire le prix d'un flux unique. [ajout]

La valeur actuelle nette est l'étape où l'on passe d'un flux à un échéancier, et elle ne demande qu'une chose de plus : que les prix s'additionnent. C'est cette linéarité, et non une hypothèse nouvelle, qui autorise à sommer. [ajout]

## Exemple minimal
100 dans un an et 100 dans deux ans, avec $P(t,t+1)=0{,}9608$ et $P(t,t+2)=0{,}9048$ : $\mathrm{NPV}(t)=186{,}56$. [ajout]

## Geste de calcul type
Actualiser flux par flux, puis sommer : $100\times0{,}9608+100\times0{,}9048=186{,}56$. Pour exprimer la même valeur dans un an, diviser par $P(t,t+1)$ : $186{,}56/0{,}9608=194{,}17$, soit les 100 reçus ce jour-là plus 94,17 pour le flux qui reste. [Déf. 4, ajout]

## Cesse d'être valide quand
Elle ne vaut que pour des flux certains. [Déf. 4]

Dès qu’ils sont aléatoires, il faut calculer l'espérance des flux sous la probabilité risque-neutre $\mathbb{Q}$. [§5.1]

## Origine
- exercice fpp/ex-19 : la NPV d'une stratégie de refinancement ne dépend que du rapport $P(0,T)/\big(P(0,t)P(t,T)\big)$ ; les notionnels disparaissent [exo. 19]

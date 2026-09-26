---
id: fpp/facteur-actualisation
nom: Facteur d’actualisation
symbole: $P(t,T)$
type: notion
statut: source
cas_de: fpp/facteur-conversion
valeur: la date
construite_a_partir_de:
- fpp/convention-capitalisation
alias:
- zéro-coupon
- zero-coupon bond
- discount factor
refs:
- §2.1
- Déf. 3
---

## Ce que c'est
Le prix aujourd’hui d’un euro payé en $T$, c’est-à-dire le prix d’un zéro-coupon : un titre qui paie 1 à une date et rien d’autre. [§2.1, Déf. 3]

## Forme
$$P(t,T)=e^{-r\tau},\qquad \tau=T-t$$ [§2.1, Déf. 3]

## Ce que les symboles modélisent
$P(t,T)$ prend deux dates et rend un **prix** : celui, en $t$, d'une unité payée en $T$. Ce n'est pas un taux, c'est un nombre positif, qu'on lit sur un titre échangé. Il est d'ordinaire inférieur à un, parce que les dépôts rapportent un intérêt. [Déf. 3, §2.1]

$\tau$ est la durée qui sépare les deux dates, $T-t$, comptée en années. $r$ est le taux d'intérêt, en capitalisation continue, supposé constant entre $t$ et $T$. [§2.1, §3.1]

## Retrouver la formule
![À 4 % continu sur un an. En haut, un euro payé en $T$, connu ; ce qu'il vaut en $t$, $P(t,T)$, est cherché. En bas, placer 0,9608 en $t$ rapporte exactement 1 en $T$, puisque $0{,}9608\times e^{0{,}04}=1$ : l'euro futur vaut donc 0,9608 aujourd'hui. Actualiser multiplie par $P(t,T)$, capitaliser divise par lui.](figures/facteur-actualisation.svg) [ajout]

**Connu** : un euro, payé en $T$. **Cherché** : ce qu'il vaut aujourd'hui, en $t$. [Déf. 3]

Un euro placé aujourd'hui au taux continu $r$ devient $e^{r\tau}$ en $T$ : c'est le facteur de capitalisation. À 4 % sur un an, $e^{0{,}04}=1{,}0408$. [§2.1]

Pour obtenir exactement un euro en $T$, il suffit donc de placer aujourd'hui $1/e^{r\tau}$ : à 4 % sur un an, 0,9608. Ce placement et l'euro futur rapportent la même chose, au même moment et sans risque ; ils ont donc le même prix. [ajout]

$$P(t,T)=\dfrac{1}{e^{r\tau}}=e^{-r\tau}$$ [§2.1]

## Ce qui la définit
On capitalise en avançant dans le temps et l’on actualise en reculant : le facteur est un taux de change entre deux dates. [§2.1, Déf. 3]

$P(t,T)$ est un prix, et ne dépend d'aucune convention ; c'est pour le calculer à partir d'un taux affiché qu'il faut en fixer une. [§2.1, ajout]

## Le chemin jusqu'ici
fpp/convention-capitalisation dit ce que devient un euro placé à un taux affiché. Le facteur d'actualisation fait le chemin inverse : ce qu'il faut placer aujourd'hui pour obtenir un euro plus tard. [§2.1]

## Exemple minimal
Taux continu de 4 % sur un an : $P(t,t+1)=0{,}9608$. [ajout]

## Geste de calcul type
Pour reculer, multiplier par $P(t,T)$ ; pour avancer, diviser par lui. À 4 % continu, un flux de 100 payé dans un an vaut $100\times0{,}9608=96{,}08$ aujourd’hui, et 96,08 placés un an redonnent $96{,}08/0{,}9608=100$. [§2.1]

## Ce qui reste libre
| paramètre | cas | $P(t,T)$ |
|---|---|---|
| convention de capitalisation | linéaire | $(1+r\tau)^{-1}$ |
| convention de capitalisation | $n$ fois par période | $(1+r\tau/n)^{-n}$ |
| convention de capitalisation | continue | $e^{-r\tau}$ |
| convention de capitalisation | actuarielle | $(1+r_a)^{-\tau}$, $r_a=e^r-1$ |
[§2.1, Déf. 3]

## Cesse d'être valide quand
La Forme suppose le taux constant jusqu'en $T$. Si les taux sont aléatoires, $P(t,T)$ reste le prix coté du zéro-coupon, mais il ne se confond plus avec le compte capitalisé $B(t,T)$, le produit des facteurs d'une période qu'on rencontrera en replaçant l'argent de période en période, et qu'on ne connaîtra qu'en $T$ ; les deux coïncident quand les taux sont déterministes. [§2.1, §4.2.2, Prop. 4]

## Origine
- exercice fpp/ex-03 : « le taux à six mois est de 4 % » ne dit ni l'unité ni la convention ; le défaut du cours est continu, annuel [ajout]
- exercice fpp/ex-10 : taux nul ne veut pas dire « pas d'actualisation à écrire », mais $P(0,T)=1$ ; la formule ne change pas de forme [ajout]

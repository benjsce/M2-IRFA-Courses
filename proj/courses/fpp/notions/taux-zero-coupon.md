---
id: fpp/taux-zero-coupon
nom: Taux zéro-coupon
symbole: $R(t,T)$, $L(t,S)$
type: notion
statut: source
construite_a_partir_de:
- fpp/facteur-actualisation
refs:
- §2.3
- Déf. 6
---

## Ce que c'est
Le prix d’un zéro-coupon réécrit en taux annuel, pour que des maturités différentes se comparent. [§2.3]

## Forme
$$R(t,T)=-\dfrac{\ln P(t,T)}{T-t},\qquad P(t,S)=\dfrac{1}{1+(S-t)\,L(t,S)}$$ [§2.3]

## Ce que les symboles modélisent
$R(t,T)$ et $L(t,S)$ disent le même prix en taux, de deux façons : la première en capitalisation continue, la seconde linéairement, comme le fait le marché court. Ce sont deux conventions de lecture, pas deux marchés. [§2.3]

$S$ est une échéance, comme $T$ ; la lettre suit le poly. Le poly imprime $S-T$ au dénominateur de $L$ : c'est une coquille, puisque la seule autre date de la formule est $t$. [§2.3, ajout]

## Ce qui la définit
**Connu** : le prix $P(t,T)$, coté pour chaque maturité. **Cherché** : le taux annuel constant qui, appliqué pendant $T-t$, redonne ce prix. [§2.3]

On en a besoin parce qu'un prix ne se compare pas d'une maturité à l'autre. Un euro dans un an coûte 0,9608, un euro dans deux ans 0,9048 : le second est moins cher, mais il immobilise l'argent deux fois plus longtemps. Rapporte-t-il plus par an ? En taux : 4 % contre 5 %, oui. [ajout]

La courbe des taux zéro-coupon s'affiche en taux linéaire $L$ jusqu'à un an et en taux continu $R$ au-delà : une convention d'affichage, les prix restent les mêmes. [Déf. 6]

## Le chemin jusqu'ici
fpp/convention-capitalisation fixe la règle qui relie un taux à un facteur ; fpp/facteur-actualisation fournit les prix $P(t,T)$, un par maturité. Le taux zéro-coupon relit chacun de ces prix avec une convention choisie, continue ou linéaire : aucune information nouvelle, seulement une échelle commune. [ajout]

## Exemple minimal
$P(t,t+2)=0{,}9048$ : $R(t,t+2)=5\,\%$. [ajout]

## Geste de calcul type
Passer des prix aux taux : $-\ln(0{,}9608)/1=4\,\%$ et $-\ln(0{,}9048)/2=5\,\%$. Le même prix à un an lu linéairement : $(1/0{,}9608-1)/1=4{,}08\,\%$, un peu plus que le taux continu, pour le même placement. [§2.3, ajout]

## Cesse d'être valide quand
rien dans le périmètre du cours ; le taux ne contient rien de plus que le prix [ajout]

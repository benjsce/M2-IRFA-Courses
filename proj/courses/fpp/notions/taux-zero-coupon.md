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
Le facteur d’actualisation réécrit en rendement annualisé, pour être comparable d’une maturité à l’autre. [§2.3]

## Forme
$$R(t,T)=-\dfrac{\ln P(t,T)}{T-t}$$ [§2.3]

## Ce qui la définit
Court terme en taux linéaire $L$, long terme en taux continu $R$ : pure convention d’affichage de la courbe. [Déf. 6]

## Exemple minimal
$P(0,2)=0{,}9048$ : $R(0,2)=5\%$. [ajout]

## Geste de calcul type
Pour comparer deux maturités, passer des prix aux taux : $P(0,1)=0{,}9608$ et $P(0,2)=0{,}9048$ donnent 4 % et 5 %. La courbe monte, ce qui se lira dans le forward. [§2.3]

## Cesse d'être valide quand
Ne contient rien de plus que $P$ : c’est une coordonnée, pas une notion nouvelle. [ajout]

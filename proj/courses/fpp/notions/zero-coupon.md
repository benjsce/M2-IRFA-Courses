---
id: fpp/zero-coupon
nom: Zéro-coupon
symbole: $P(t,T)$
type: notion
statut: source
construite_a_partir_de:
- fpp/capitalisation
alias:
- zero-coupon bond
- obligation zéro-coupon
- ZC
- prix zéro-coupon
refs:
- Déf. 3
- §2.2
---

## Ce que c'est
Le titre qui paie 1 à une date T et rien d'autre ; son prix en t, noté P(t,T), est ce que vaut aujourd'hui 1 reçu en T. [Déf. 3]

## Forme
$$P(t,T)=\text{valeur en }t\text{ de }1\text{ payé en }T,\qquad P(t,T)=e^{-r(T-t)}\ \text{si le taux est constant}$$ [Déf. 3, §2.1]

## Ce que les symboles modélisent
$P(t,T)$ prend deux dates, celle où l'on regarde et celle du paiement ; c'est un prix, inférieur à 1 dès que les taux sont positifs. Ce n'est pas le prix d'un put, que le poly note aussi $P$. [Déf. 3, éq. 4]

## Ce qui la définit
On connaît le flux, 1 en $T$ ; on cherche son prix aujourd'hui. Quand le taux n'est pas constant, aucune formule ne le donne : c'est le marché qui le fixe, échéance par échéance. Le zéro-coupon est le facteur d'actualisation sous sa forme la plus générale. [Déf. 3, ajout]

Tout flux certain de montant $X$ payé en $T$ vaut donc $X\,P(t,T)$ en $t$ : c'est $X$ zéro-coupons. [Déf. 4]

![Deux zéro-coupons du cours : 1 payé dans un an vaut 0,9608 aujourd'hui, 1 payé dans deux ans vaut 0,9048. Plus le paiement est loin, moins il vaut.](figures/zero-coupon.svg) [ajout]

## Le chemin jusqu'ici
fpp/capitalisation transporte une somme entre deux dates avec un taux unique. Le zéro-coupon garde le transport et abandonne le taux unique : il donne un prix par échéance, que la courbe des taux traduira ensuite en taux. [ajout]

## Exemple minimal
Le zéro-coupon à un an cote 0,9608, celui à deux ans 0,9048. [ajout]

## Geste de calcul type
Multiplier un flux certain par le zéro-coupon de sa date : 100 payés dans deux ans valent $100\times0{,}9048=90{,}48$ aujourd'hui. [ajout]

## Cesse d'être valide quand
Le zéro-coupon suppose que le paiement aura lieu. Un emprunteur qui peut faire défaut vaut moins : le livre d'exercices valorise le zéro-coupon risqué d'une entreprise à $De^{-(r+s)T}$, avec un spread $s$. Et le zéro-coupon est propre à une devise : l'étranger a le sien, $P^f(t,T)$. [exo. 16, §2.4]

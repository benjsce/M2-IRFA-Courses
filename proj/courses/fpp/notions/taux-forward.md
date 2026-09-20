---
id: fpp/taux-forward
nom: Taux forward
symbole: $F(t,T,S)$, $f(t,T)$
type: notion
statut: source
construite_a_partir_de:
- fpp/taux-zero-coupon
alias:
- forward rate
- taux instantané
refs:
- §2.3
---

## Ce que c'est
Le taux sur $[T,S]$ qu’on peut verrouiller dès aujourd’hui. [§2.3]

## Forme
$$F(t,T,S)=\dfrac{1}{S-T}\ln\dfrac{P(t,T)}{P(t,S)}$$ [§2.3]

## Ce qui la définit
Un taux long est une moyenne pondérée de forwards : $R(t,S)(S-t)=R(t,T)(T-t)+F(t,T,S)(S-T)$. À la limite, $f(t,T)=-\partial\ln P/\partial T$ et $P(t,T)=\exp\left(-\int_t^T f(t,u)du\right)$ — la courbe entière est l’accumulation de ses forwards. [§2.3]

## Exemple minimal
à venir [ajout]

## Geste de calcul type
à venir [ajout]

## Cesse d'être valide quand
Verrouillable seulement si l’on peut prêter et emprunter aux deux maturités. [ajout]

## Origine
- exercice fpp/ex-04 : un rapport de deux prix à terme de change est un rapport de facteurs d'actualisation forward [ajout]

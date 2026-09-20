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

## Le chemin jusqu'ici
fpp/convention-capitalisation, fpp/facteur-actualisation, puis fpp/taux-zero-coupon qui met les maturités dans une coordonnée comparable. [ajout]

Le taux forward est ce que la courbe implique pour une période future : il se lit dans le rapport de deux zéro-coupons, sans aucune hypothèse sur l'avenir. C'est une conséquence de l'absence d'arbitrage, pas une prévision — distinction que l'exercice 19 rend très concrète. [ajout]

## Exemple minimal
$P(0,1)=0{,}9608$ et $P(0,2)=0{,}9048$ : $F(0,1,2)=6\%$. [ajout]

## Geste de calcul type
Le forward est un rapport de zéro-coupons : $\ln(0{,}9608/0{,}9048)=6\,\%$ sur $[1,2]$. Vérifier par la moyenne pondérée du cours : $5\%\times2=4\%\times1+6\%\times1$. [§2.3]

## Cesse d'être valide quand
Verrouillable seulement si l’on peut prêter et emprunter aux deux maturités. [ajout]

## Origine
- exercice fpp/ex-04 : un rapport de deux prix à terme de change est un rapport de facteurs d'actualisation forward [ajout]
- exercice fpp/ex-19 : la matrice complète des forwards se remplit avec une seule formule, $\big(r(T)T-r(t)t\big)/(T-t)$, et se lit comme le taux qu'il faudra réaliser pour qu'un refinancement soit neutre [exo. 19]

---
id: fpp/courbe-des-taux
nom: Courbe des taux
type: notion
statut: source
construite_a_partir_de:
- fpp/taux-zero-coupon
alias:
- yield curve
- courbe zéro-coupon
- zero-coupon curve
- structure par terme des taux
refs:
- Déf. 6
---

## Ce que c'est
Le graphe, à une date t, du taux zéro-coupon en fonction de l'échéance, cité en linéaire jusqu'à un an et en continu au-delà. [Déf. 6]

## Forme
$$T\longmapsto\begin{cases}L(t,T) & t<T\le t+1\ \text{(court terme)}\\ R(t,T) & T>t+1\ \text{(long terme)}\end{cases}$$ [Déf. 6]

## Ce que les symboles modélisent
$t$ est fixé : c'est la date où l'on regarde. $T$ parcourt les échéances. $L$ et $R$ sont les taux zéro-coupon linéaire et continu. [Déf. 6]

## Ce qui la définit
La courbe résume en taux les prix de tous les zéro-coupons du jour. Le taux constant $r$ de la capitalisation correspond à une courbe plate ; une courbe croissante dit que les échéances longues rapportent davantage par an que les courtes. [Déf. 6, ajout]

Le livre d'exercices en donne une à quatre points, de 3 % à un an à 3,7 % à quatre ans, et demande d'en tirer les taux forward. [exo. 19]

## Le chemin jusqu'ici
fpp/taux-zero-coupon donne un taux par échéance ; la courbe les met bout à bout. Derrière chaque point se trouve un prix de fpp/zero-coupon, et le passage du prix au taux emploie l'une des deux conventions de fpp/capitalisation, que la courbe mélange en changeant de convention à un an. [ajout]

## Exemple minimal
Un taux de 4 % à un an et de 5 % à deux ans : la courbe du jour est croissante. [ajout]

## Geste de calcul type
Lire un prix sur la courbe : au-delà d'un an, $P(t,T)=e^{-R(t,T)(T-t)}$ ; en deçà, $P(t,T)=1/(1+(T-t)L(t,T))$. [Déf. 6, §2.3]

## Cesse d'être valide quand
La courbe est celle d'un jour : demain elle aura bougé. Elle ne prévoit pas les taux futurs ; elle dit seulement ce qu'on peut garantir dès aujourd'hui, ce que le taux forward lira entre deux de ses points. [Déf. 6, §2.3]

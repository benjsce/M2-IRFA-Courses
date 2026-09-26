---
id: fpp/taux-forward
nom: Taux forward
symbole: $F(t,T,S)$
type: notion
statut: source
cas_de: fpp/prix-a-terme
valeur: un taux, celui d'un emprunt entre deux dates futures
construite_a_partir_de:
- fpp/fra
- fpp/courbe-des-taux
alias:
- forward rate
- taux à terme
- taux forward continu
refs:
- §2.3
- Ex. 2
- exo. 19
---

## Ce que c'est
Le taux K qui rend un FRA gratuit à la signature ; il se lit dans la courbe d'aujourd'hui, entre les échéances T et S. [§2.3]

## Forme
$$F(t,T,S)=\frac{R(t,S)(S-t)-R(t,T)(T-t)}{S-T}=\frac{1}{S-T}\ln\frac{P(t,T)}{P(t,S)}$$ [§2.3]

## Ce que les symboles modélisent
$F(t,T,S)$ prend trois dates : celle où on le lit, puis le début et la fin de l'emprunt. C'est un taux continu par an. Ce n'est ni le prix forward $F(t,T)$ d'une action, qui n'a que deux dates et est un prix, ni le $F$ de la formule de Black. [§2.3, §3.1, éq. 11]

## Retrouver la formule
![Deux façons de placer 1 de t à S. En haut, ① en une fois, au taux R(t,S) : 1 devient e^(R(t,S)(S−t)). En bas, ② en deux temps : jusqu'à T au taux R(t,T), 1 devient e^(R(t,T)(T−t)), puis de T à S au taux K fixé aujourd'hui par le FRA, × e^(K(S−T)). ③ Les deux résultats sont connus dès aujourd'hui pour la même mise : ils sont égaux, et les exposants s'ajoutent, R(t,T)(T − t) + K(S − T) = R(t,S)(S − t).](figures/taux-forward.svg) [ajout]

Prenons la courbe du cours : 4 % à un an, 5 % à deux ans, avec $T$ dans un an et $S$ dans deux ans. [ajout]

① Placer 1 euro de $t$ à $S$ en une fois, au taux zéro-coupon $R(t,S)=5\,\%$ : il devient $e^{R(t,S)(S-t)}=e^{0,05\times2}=e^{0,10}=1{,}1052$. Ce montant est connu aujourd'hui. [§2.3]

② Le placer en deux temps : d'abord jusqu'à $T$ au taux $R(t,T)=4\,\%$, il devient $e^{R(t,T)(T-t)}=e^{0,04}=1{,}0408$ ; puis, de $T$ à $S$, au taux $K$ que le FRA fixe dès aujourd'hui, il devient $1{,}0408\times e^{K(S-T)}$. Ce montant aussi est connu aujourd'hui, puisque $K$ est écrit au contrat et que le FRA ne coûte rien. [Déf. 7, ajout]

③ Même mise, même date d'arrivée, deux résultats certains : ils sont égaux, sinon on emprunterait par le trajet le moins cher pour placer par l'autre, et l'on gagnerait sans risque. $e^{0,04}\times e^{K}=e^{0,10}$ : les exposants s'ajoutent, $0{,}04+K=0{,}10$, et $K=6\,\%$. [§2.3, ajout]

En lettres, $R(t,T)(T-t)+K(S-T)=R(t,S)(S-t)$ : c'est l'égalité du poly entre taux long, taux court et taux forward. Comme $e^{-R(t,T)(T-t)}=P(t,T)$, elle s'écrit aussi avec les zéro-coupons : [§2.3]

$$F(t,T,S)\equiv K=\frac{R(t,S)(S-t)-R(t,T)(T-t)}{S-T}=\frac{1}{S-T}\ln\frac{P(t,T)}{P(t,S)}$$ [§2.3]

## Ce qui la définit
Ce qui est **connu** : la courbe d'aujourd'hui, 4 % sur la première année, 5 % en moyenne sur les deux. Ce qu'on **cherche** : le taux de la seconde année. Sur deux ans, les intérêts continus totalisent 10 points ; la première année en porte 4 ; la seconde doit porter les 6 qui restent. C'est la première écriture de la Forme : le total moins la partie connue, divisé par la durée du trou. [§2.3, ajout]

Le taux forward est un nombre lu dans la courbe ; le FRA est le contrat qui l'obtient. Le poly l'écrit aussi comme une moyenne : le taux zéro-coupon long est la moyenne, pondérée par les durées, du taux court et du taux forward. Sur une courbe plate, tous trois sont égaux. [§2.3, Ex. 2]

Le livre d'exercices en tire une lecture : emprunter court puis renouveler coûte autant qu'emprunter long si le taux futur égale le taux forward, et moins s'il reste en dessous. Le taux forward est le point mort du renouvellement. [exo. 19]

## Le chemin jusqu'ici
fpp/fra pose la question : quel taux fixe rend le contrat gratuit ? fpp/courbe-des-taux fournit les deux points connus, et fpp/taux-zero-coupon les convertit en prix, ceux des deux fpp/zero-coupon qui servent à ramener chaque jambe en $t$. fpp/capitalisation fixe la convention continue qui permet de soustraire les intérêts comme des longueurs. [ajout]

## Exemple minimal
Avec 4 % à un an et 5 % à deux ans, le taux forward entre un et deux ans vaut 6 %. [ajout]

## Geste de calcul type
Remplir une matrice de taux forward à partir d'une courbe : avec 3 % à un an et 3,3 % à deux ans, le forward de la deuxième année vaut $2\times3{,}3-3=3{,}6\,\%$, comme dans le corrigé du livre d'exercices. [exo. 19]

## Cesse d'être valide quand
Le taux forward n'est pas une prévision : dans un an, le taux observé sera ce qu'il sera. Il est seulement ce qu'on peut garantir aujourd'hui, et le livre d'exercices montre que le renouvellement gagne ou perd selon que le taux futur tombe sous lui ou au-dessus. [exo. 19, ajout]

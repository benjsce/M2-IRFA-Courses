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
![Le FRA en trois étapes, avec la courbe du cours. En haut, ce qu'on reçoit : ① l'intérêt variable reçu en S est exactement ce que donne 1 reçu en T et placé jusqu'en S au taux du moment ; il vaut donc 1 en T, et ② 0,9608 aujourd'hui. En bas, ce qu'on paie : le montant fixé aujourd'hui, payé en S, vaut ② 0,9048 fois ce montant aujourd'hui. ③ Le contrat ne coûtant rien, les deux valeurs sont égales, ce qui donne K = 6 %.](figures/taux-forward.svg) [ajout]

Prenons la courbe du cours : 4 % à un an, 5 % à deux ans, donc $P(t,T)=0{,}9608$ et $P(t,S)=0{,}9048$ pour $T$ dans un an et $S$ dans deux ans. [ajout]

① La jambe variable rapporte en $S$ ce que rapporte 1 placé en $T$ au taux du moment : elle vaut 1 en $T$, quel que soit ce taux. ② Ramenée en $t$, elle vaut $P(t,T)=0{,}9608$. [Déf. 7, ajout]

② La jambe fixe paie $e^{K}$ en $S$, montant connu dès aujourd'hui : ramenée en $t$, elle vaut $P(t,S)\,e^{K}=0{,}9048\,e^{K}$. [§2.3]

③ Le contrat ne coûte rien, les deux valeurs sont égales : $e^{K}=0{,}9608/0{,}9048$, soit $K=6\,\%$. En lettres, $P(t,T)=P(t,S)\,e^{K(S-T)}$, et : [§2.3]

$$F(t,T,S)\equiv K=\frac{1}{S-T}\ln\frac{P(t,T)}{P(t,S)}$$ [§2.3]

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

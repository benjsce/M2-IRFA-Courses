---
id: fpp/taux-forward-instantane
nom: Taux forward instantané
symbole: $f(t,T)$
type: notion
statut: source
construite_a_partir_de:
- fpp/taux-forward
alias:
- instantaneous forward rate
- forward instantané
refs:
- §2.3
---

## Ce que c'est
Le taux forward d'un emprunt infiniment court commençant en T, dont l'accumulation de t à T redonne le prix du zéro-coupon. [§2.3]

## Forme
$$f(t,T)=\lim_{S\to T^+}F(t,T,S)=-\frac{\partial\ln P(t,T)}{\partial T},\qquad P(t,T)=\exp\Big(-\int_t^T f(t,u)\,du\Big)$$ [§2.3]

## Ce que les symboles modélisent
$f(t,T)$ est lu en $t$, pour un emprunt qui commence en $T$ et dure un instant ; $u$ parcourt les dates entre $t$ et $T$. Le livre d'exercices écrit $f(t,T)$ pour un autre objet, le taux forward d'un emprunt de $t$ à $T$ : même écriture, pas le même taux. [§2.3, exo. 19]

## Retrouver la formule
![Un taux forward instantané de 4 % la première année et de 6 % la seconde : l'aire sous la courbe sur deux ans vaut 0,04 + 0,06 = 0,10, et le zéro-coupon à deux ans vaut exp(−0,10).](figures/taux-forward-instantane.svg) [ajout]

Le taux forward entre $T$ et $S$ est une pente : $\big(\ln P(t,T)-\ln P(t,S)\big)/(S-T)$. Quand $S$ se rapproche de $T$, cette pente devient la dérivée de $-\ln P(t,T)$ par rapport à l'échéance. [§2.3]

Dans l'autre sens, $-\ln P(t,T)$ est l'accumulation de ces pentes depuis $t$, où il vaut 0 puisque $P(t,t)=1$ : l'aire sous $f$ entre $t$ et $T$. [§2.3]

Sur la figure, l'aire vaut $0{,}04\times1+0{,}06\times1=0{,}10$, et $e^{-0,10}=0{,}9048$ est bien le zéro-coupon à deux ans du cours : [ajout]

$$P(t,T)=\exp\Big(-\int_t^T f(t,u)\,du\Big)$$ [§2.3]

## Ce qui la définit
Ce qui est **connu** : les prix des zéro-coupons pour toutes les échéances. Ce qu'on **cherche** : le taux que l'on peut garantir aujourd'hui pour chaque instant futur. Le taux zéro-coupon $R(t,T)$ en est la moyenne de $t$ à $T$. [§2.3, ajout]

## Le chemin jusqu'ici
fpp/taux-forward donne le taux garanti sur une période ; on la réduit ici à un instant. Ce taux venait de fpp/fra, qui le rend échangeable, et de fpp/courbe-des-taux, dont il lit la pente. [ajout]

Remonter l'accumulation redonne les prix de fpp/zero-coupon, donc les taux de fpp/taux-zero-coupon, dans la convention continue de fpp/capitalisation, la seule où l'accumulation est une simple aire. [ajout]

## Exemple minimal
Si le taux forward du cours est constant par année, il vaut 4 % pendant la première année et 6 % pendant la seconde. [ajout]

## Geste de calcul type
Du forward instantané au prix : additionner les aires et prendre l'exponentielle de l'opposé, $e^{-(0,04+0,06)}=0{,}9048$. [§2.3]

## Cesse d'être valide quand
Il faut que le prix soit dérivable en l'échéance. Une courbe connue en quelques points seulement ne fixe pas $f$ entre eux : l'hypothèse d'un forward constant par année est un choix d'interpolation, pas une donnée. [§2.3, ajout]

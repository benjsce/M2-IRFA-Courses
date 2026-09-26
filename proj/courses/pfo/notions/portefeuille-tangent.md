---
id: pfo/portefeuille-tangent
nom: Portefeuille tangent
symbole: '$W^*$, $SR(\mu_0)$, $\mu_0^*$'
type: notion
statut: source
cas_de: pfo/optimisation-de-portefeuille
valeur: maximiser le ratio de Sharpe
construite_a_partir_de:
- pfo/frontiere-efficiente
- pfo/ratio-de-sharpe
alias:
- tangency portfolio
- portefeuille de Sharpe maximal
- maximum Sharpe portfolio
- max Sharpe
- formulation 2
refs:
- §3.0.3
- p. 40
- Fig. 3.2
- §3.0.4
- Fig. 3.3
- §3.0.8
- p. 53
- p. 54
---

## Ce que c'est
Le portefeuille risqué de ratio de Sharpe maximal, qui est aussi le point où une droite issue de l'actif sans risque touche la frontière efficiente. [p. 40]

## Forme
$$W^*=\arg\max_{W}\ \frac{W^T\mu-R_f}{\sqrt{W^T\boldsymbol{\Sigma}W}}\qquad\text{sous}\quad W^T\mathbf{1}=1,\quad W\ge0$$ [§3.0.3]

$$SR(\mu_0)=\frac{\mu_0-R_f}{\sigma_p(\mu_0)},\qquad \mu_0^*=\arg\max_{\mu_0}SR(\mu_0)$$ [§3.0.4]

## Ce que les symboles modélisent
$W^*$ est le vecteur des poids du portefeuille tangent. $SR(\mu_0)$ est une fonction du rendement cible : elle prend un niveau de rendement, cherche sur la frontière efficiente le portefeuille qui l'atteint avec le moins de risque, et rend son ratio de Sharpe. $\mu_0^*$ est le rendement cible où cette fonction culmine, celui du portefeuille tangent. [p. 40, §3.0.4]

## Ce qui la définit
**Connus** : le point de l'actif sans risque, $(0,R_f)$, et la frontière efficiente. **Cherchée** : la droite la plus pentue issue de ce point qui touche encore un portefeuille réalisable. Le portefeuille tangent est le point de contact. [p. 40, Fig. 3.2]

C'est bien le portefeuille de ratio de Sharpe maximal : le ratio d'un portefeuille est la pente de la droite qui le relie à l'actif sans risque, et maximiser le ratio revient à chercher la plus pentue de ces droites. [p. 40]

![Les deux actifs non corrélés de l'exemple, avec un taux sans risque de 2 %. La courbe est la frontière des portefeuilles ; de toutes les droites issues du point (0 ; 2 %), la plus pentue qui touche encore la courbe la touche en T, le portefeuille tangent, et sa pente est le ratio de Sharpe maximal.](figures/portefeuille-tangent.svg) [ajout]

Le même point se lit le long de la frontière : c'est le portefeuille efficient dont le ratio de Sharpe est le plus élevé, le maximum de $SR(\mu_0)$, atteint en $\mu_0^*$. [§3.0.4, Fig. 3.3]

Les algorithmes de `scipy.optimize` minimisent : le script du cours maximise donc le ratio en minimisant $-SR(W)$, par la méthode SLSQP, en partant du portefeuille équipondéré. [p. 40, §3.0.8]

## Le chemin jusqu'ici
Le portefeuille tangent est un point choisi sur une courbe par un critère. La courbe, c'est pfo/frontiere-efficiente ; le critère, c'est pfo/ratio-de-sharpe, la pente de la droite qui relie l'actif sans risque à chaque portefeuille. [ajout]

Les deux reposent sur pfo/moments-du-portefeuille. Le rendement espéré est une moyenne pondérée de pfo/rendement-arithmetique, ce que pfo/piege-d-agregation interdit de faire avec pfo/rendement-logarithmique ; la variance vient de pfo/matrice-de-covariance, annualisée par fpp/echelonnement-de-la-variance, dont la diagonale porte le carré de fpp/volatilite. [ajout]

Sans dup/diversification, il n'y aurait rien à choisir : mélanger n'améliorerait pas le compromis. C'est parce que dup/moyenne-variance réduit chaque dup/loterie à deux nombres que ce compromis se lit comme une pente. [ajout]

## Exemple minimal
Avec les deux actifs non corrélés de rendements 6 % et 10 %, de volatilités 10 % et 20 %, et un taux sans risque de 2 %, le portefeuille tangent place deux tiers dans le premier : rendement 7,33 %, volatilité 9,43 %, ratio 0,566. [ajout]

## Geste de calcul type
Quand la contrainte $W\ge0$ ne mord pas, les poids tangents sont proportionnels à $\boldsymbol{\Sigma}^{-1}(\mu-R_f\mathbf{1})$ : c'est ce que donne la condition du premier ordre du maximum de $SR(W)$. Pour $\boldsymbol{\Sigma}$ diagonale, chaque poids est donc proportionnel à la prime de l'actif, $\mu_i-R_f$, divisée par sa variance. [ajout]

Ici : $(0{,}04/0{,}01\,;\,0{,}08/0{,}04)=(4\,;2)$, soit $W^*=(\tfrac23\,;\tfrac13)$. Alors $W^{*T}\mu=7{,}33\,\%$, $\sigma_p=\sqrt{\tfrac49\times0{,}01+\tfrac19\times0{,}04}=9{,}43\,\%$ et $SR=5{,}33/9{,}43=0{,}566$. [ajout]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| bornes des poids | sans vente à découvert | $0\le w_i\le1$ |
| taux sans risque | script du cours | $R_f=0$ |
[§3.0.8]

## Cesse d'être valide quand
Les poids tangents dépendent des rendements espérés estimés, qui sont les paramètres les plus mal estimés : l'exercice 3 du cours demande de refaire l'optimisation sur des fenêtres de 12, 36 et 60 mois et d'en comparer les allocations. [p. 54, p. 55]

Dans l'exemple, porter le rendement espéré du second actif de 10 % à 11 % fait passer son poids de 33,3 % à 36 %. Le portefeuille de variance minimale globale, qui n'utilise pas $\mu$, n'en bouge pas. [ajout]

La formule proportionnelle à $\boldsymbol{\Sigma}^{-1}(\mu-R_f\mathbf{1})$ cesse de valoir dès qu'une borne est atteinte : il faut alors l'optimiseur. [ajout]

## Origine
- exercice pfo/ex-03 : des limites d'allocation déplacent le portefeuille tangent, et peuvent rendre le problème impossible [p. 53]
- exercice pfo/ex-04 : le portefeuille tangent change avec la fenêtre d'estimation, surtout par l'erreur sur $\mu$ [p. 54]

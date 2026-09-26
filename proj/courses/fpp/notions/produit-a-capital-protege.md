---
id: fpp/produit-a-capital-protege
nom: Produit à capital protégé
type: notion
statut: source
cas_de: fpp/strategie-optionnelle
valeur: on achète l’optionalité
construite_a_partir_de:
- fpp/call
- fpp/facteur-actualisation
alias:
- principal protected product
- PPP
refs:
- §9.2
---

## Ce que c'est
Un zéro-coupon qui rend la mise, plus les calls que le solde permet d'acheter, qui donnent une part de la hausse. [§9.2]

## Forme
$$\text{ZC}+k\,\text{Call},\qquad k=\dfrac{K-K\,P(t,T)}{C}$$ [§9.2, exo. 17]

$$\text{à }k=1\ :\qquad\text{ZC}+\text{Call}\;=\;\text{Spot}+\text{Put}$$ [§9.2, Prop. 7]

## Ce que les symboles modélisent
ZC, Call, Spot et Put désignent des positions, pas des prix. ZC est un zéro-coupon qui paie en $T$ le capital garanti ; Call est un call sur le sous-jacent, d'échéance $T$ ; Spot est le sous-jacent lui-même, acheté au comptant ; Put est un put de même échéance. [§9.2, ajout]

$K$ est la mise, celle que le produit rend à l'échéance ; on prend ici le strike des calls égal à la mise et au cours du jour, comme dans l'exercice 17. $K\,P(t,T)$ est ce qu'il faut en placer en $t$ pour la retrouver en $T$ : $P(t,T)$ y est le prix d'un zéro-coupon, et non celui d'un put. $C$ est le prix d'un call, et $k$ le nombre de calls achetés avec la mise ; comme la mise égale le cours du jour, c'est aussi la part de la hausse que touche l'épargnant : le taux de participation. [§9.2, exo. 17, ajout]

## Retrouver la formule
![Deux lignes sur le même axe du temps, une par brique. En haut, 96,08 placés en zéro-coupon en $t$ rendent la mise, 100, en $T$ : tout y est connu aujourd'hui. En bas, le solde, 3,92, achète des calls à 9,93 : le trou est le nombre de calls, 3,92 / 9,93 = 0,395. En $T$, ils paient 0,395 fois la hausse au-delà de 100, en pointillé parce qu'elle est aléatoire et peut être nulle.](figures/produit-a-capital-protege.svg) [ajout]

**Ce qui est connu aujourd'hui** : la mise, 100 ; le prix du zéro-coupon à un an, $P(t,t+1)=0{,}9608$ ; le prix du call à un an de strike 100, 9,93. **Ce qu'on cherche** : la part de la hausse qu'on peut s'offrir. [ajout]

Garantir la mise d'abord. Un zéro-coupon paie 1 en $T$ et coûte 0,9608 ; pour recevoir 100, il en faut 100, qui coûtent $100\times0{,}9608=96{,}08$. C'est le plancher : quoi qu'il arrive à l'action, ces 96,08 redeviennent 100. [§9.2, ajout]

Il reste $100-96{,}08=3{,}92$, le coussin. C'est tout ce qu'on peut dépenser en hausse sans toucher à la garantie. [exo. 17]

Un call coûte 9,93 et paie toute la hausse au-delà de 100. Avec 3,92, on n'en a pas les moyens : on en achète $3{,}92/9{,}93=0{,}395$, qui paient 0,395 fois cette hausse. C'est le taux de participation : 39,5 %. [exo. 17, ajout]

$$K\,P(t,T)+k\,C=K\quad\Longleftrightarrow\quad k=\dfrac{K-K\,P(t,T)}{C}$$ [exo. 17]

## Ce qui la définit
Protéger le capital, c'est acheter un put : la parité call-put le montre. À quantités unitaires, $96{,}08+9{,}93=106{,}00=100+6{,}00$ : un zéro-coupon et un call valent l'action et un put. Le put, 6,00, est le prix de la protection. Avec une mise de 100, on n'a pas les moyens des 106,00 : on réduit la part de call, d'où $k<1$. [§9.2, Prop. 7, ajout]

## Le chemin jusqu'ici
Deux fils y mènent. Le premier va de fpp/payoff à fpp/call : c'est lui qui donne la hausse. Le second va de fpp/convention-capitalisation à fpp/facteur-actualisation : c'est lui qui rend la mise. [ajout]

Le produit est exactement la somme des deux, et c'est tout le montage : un zéro-coupon garantit le capital, le solde achète l'optionalité. La fiche n'a besoin d'aucun modèle de prix, seulement de savoir que ces deux objets existent et s'additionnent. [ajout]

## Exemple minimal
96,08 placés en zéro-coupon à un an rendent 100 ; les 3,92 restants achètent 0,395 call de strike 100 : l'épargnant touche 39,5 % de la hausse au-delà de 100, et jamais moins que sa mise. [ajout]

## Geste de calcul type
Coussin sur prix du call : $k=(100-96{,}08)/9{,}93=0{,}395$. Si l'action finit à 120, le produit rend $100+0{,}395\times20=107{,}90$ ; si elle finit à 80, il rend 100. [exo. 17, ajout]

## Cesse d'être valide quand
La protection vaut à l’échéance seulement, et elle coûte exactement la prime du put : il n’y a pas de protection gratuite. [ajout]

## Origine
- exercice fpp/ex-17 : le taux de participation est un rapport, coussin sur prime du call à la monnaie. Il monte avec le taux et la maturité, il descend avec la volatilité ; le jeu de paramètres du corrigé ($r=4\,\%$, $T=4$, $\sigma=15\,\%$, $d=1{,}88\,\%$) est calibré pour donner exactement 100 % [exo. 17, ajout]

---
id: dup/euler-sans-engagement
nom: Équation d'Euler sans engagement
symbole: '$V(w)$, $c_2(w_2)$'
type: notion
statut: source
construite_a_partir_de:
- dup/engagement-complet
- dup/sophistication
alias:
- facteur d'actualisation effectif
- effective discount factor
- valeur de continuation
- continuation value
refs:
- L5 slide 27
- L5 slide 28
- L5 slide 29
---

## Ce que c'est
Quand chaque moi décide lui-même, le moi 1 actualise la période 2 par une moyenne de $\beta\delta$ et de $\delta$, pondérée par ce que le moi 2 consomme d'un euro de plus. [L5 slide 29]

## Forme
$$u'(c_1)=\Big[\,c_2'(w_2)\,\beta\delta+\big(1-c_2'(w_2)\big)\,\delta\,\Big]\,R\,u'(c_2),\qquad u'(c_2)=\beta\delta R\,u'(c_3)$$ [L5 slide 29]

## Ce que les symboles modélisent
$c_2(w_2)$ est la règle du moi 2 : ce qu'il consomme selon la richesse qu'il reçoit. Sa dérivée $c_2'(w_2)$ est la part d'un euro de plus qu'il consomme, le reste passant à la période 3. [L5 slide 27, L5 slide 29]

La valeur de continuation $V(w)$ s'écrit ici $V(w_2)=u(c_2(w_2))+\delta\,u\big(R(w_2-c_2(w_2))\big)$ : ce que vaut, **pour le moi 1**, la richesse $w_2$ qu'il transmet, sachant ce que le moi 2 en fera. Ce n'est pas ce que le moi 2 lui-même en pense. [L5 slide 28]

## Retrouver la formule
![Un euro de plus transmis au moi 2, découpé comme le moi 2 le découpe. La part c₂′ qu'il consomme a la hauteur βδ, le poids que le moi 1 donne à la période 2 ; la part 1 − c₂′ qu'il épargne a la hauteur δ. L'aire de la barre est le facteur effectif c₂′βδ + (1 − c₂′)δ, ici ⅔, entre βδ = ½ et δ = 1.](figures/euler-sans-engagement.svg) [ajout]

Avec $u=\ln$, $\beta=\tfrac12$, $\delta=R=1$ et 100 de richesse, on part de la fin. Le moi 3 consomme tout ce qu'il reçoit. [L5 slide 27]

Le moi 2 choisit $c_2$ en maximisant $\ln c_2+\beta\delta\ln(w_2-c_2)$ : il décote la période 3 de $\beta\delta$, puisqu'elle est son futur. Il consomme $c_2(w_2)=w_2/(1+\beta)=\tfrac23w_2$, d'où $u'(c_2)=\beta\delta R\,u'(c_3)$. [L5 slide 27]

Le moi 1, sophistiqué, choisit $c_1$ en maximisant $u(c_1)+\beta\delta V\big(R(w_1-c_1)\big)$, d'où $u'(c_1)=\beta\delta R\,V'(w_2)$. [L5 slide 28]

Un euro de plus en $w_2$ : le moi 2 en consomme $c_2'=\tfrac23$, qui vaut $u'(c_2)$ par euro, et en épargne $\tfrac13$, qui vaut $\delta R\,u'(c_3)=u'(c_2)/\beta$ par euro d'après l'équation du moi 2. Donc $V'(w_2)=u'(c_2)\,c_2'+\tfrac1\beta\,u'(c_2)\,(1-c_2')$. [L5 slide 28]

Multiplier par $\beta\delta R$ fait sortir le crochet : $\beta\delta\times c_2'$ pour la part consommée, $\beta\delta\times\tfrac1\beta=\delta$ pour la part épargnée. Ici $\tfrac23\times\tfrac12+\tfrac13\times1=\tfrac23$, et l'on retrouve $c_1=50$, $c_2=33{,}3$, $c_3=16{,}7$. [L5 slide 29, ajout]

$$u'(c_1)=\Big[\,c_2'(w_2)\,\beta\delta+\big(1-c_2'(w_2)\big)\,\delta\,\Big]\,R\,u'(c_2)$$ [L5 slide 29]

## Ce qui la définit
Le connu : les règles des moi suivants, qu'un agent sophistiqué prévoit. Le trou : ce que le moi 1 consomme. Le facteur effectif le bouche : il est plus proche de $\delta$ quand le moi 2 épargne l'euro marginal, plus proche de $\beta\delta$ quand il le consomme. [L5 slide 29]

## Le chemin jusqu'ici
dup/engagement-complet posait le programme du moi 1 et le plan $(50,25,25)$ qu'il voudrait imposer, avec les poids de dup/actualisation-quasi-hyperbolique. Sans engagement, le moi 2 s'en écarte, parce que dup/coherence-dynamique tombe sous dup/biais-pour-le-present ; dup/sophistication dit que le moi 1 le sait, et résout à rebours. [L5 slide 27, L5 slide 28]

Ces moi successifs partagent tous la même forme de dup/utilite-actualisee et les utilités de dup/fonction-utilite ; ce qui les oppose, c'est que chacun se place en 0. L'écart à dup/actualisation-exponentielle, que dup/inversion-des-preferences-dans-le-temps avait révélé et que dup/stationnarite et dup/invariance-temporelle ont nommé, devient ici un facteur d'actualisation qui dépend de la règle du moi suivant. [L5 slide 22, L5 slide 29]

## Exemple minimal
Avec $u=\ln$, $\beta=\tfrac12$, $\delta=R=1$ et 100 de richesse : le moi 1 consomme 50 et le moi 2, au lieu des 25 du plan, 33,3, laissant 16,7 à la période 3. [ajout]

## Geste de calcul type
Résoudre le moi 2 pour avoir $c_2(w_2)$ et $c_2'$, reporter dans le crochet, puis résoudre l'équation du moi 1 avec le budget $w_2=R(w_1-c_1)$. [L5 slide 27, L5 slide 29]

## Cesse d'être valide quand
La règle $c_2(w_2)$ n'est pas dérivable, ou $V$ n'est pas concave : la condition du premier ordre ne caractérise plus le choix du moi 1. [L5 slide 28, L5 slide 31]

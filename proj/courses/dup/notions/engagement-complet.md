---
id: dup/engagement-complet
nom: Consommation-épargne avec engagement complet
symbole: '$c_t$, $w_t$, $R$'
type: notion
statut: source
construite_a_partir_de:
- dup/actualisation-quasi-hyperbolique
alias:
- full commitment
- engagement
- équations d'Euler avec engagement
refs:
- L5 slide 25
- L5 slide 26
---

## Ce que c'est
Le plan de consommation que choisirait, pour trois périodes, un agent biaisé pour le présent s'il pouvait l'imposer à ses moi futurs. [L5 slide 26]

## Forme
$$\max_{c_1,c_2,c_3}\ u(c_1)+\beta\delta\,u(c_2)+\beta\delta^2u(c_3)\quad\text{avec}\quad w_2=R(w_1-c_1),\ \ c_3=w_3=R(w_2-c_2)$$ [L5 slide 25, L5 slide 26]
$$u'(c_1)=\beta\delta R\,u'(c_2),\qquad u'(c_2)=\delta R\,u'(c_3)$$ [L5 slide 26]

## Ce que les symboles modélisent
$w_t$ est la richesse au début de la période $t$, $c_t$ ce qu'on en consomme ; ce qui n'est pas consommé est placé et rapporte $R$ fois sa valeur à la période suivante. $R$ est un facteur brut, $1+r$, et non un taux. La dernière période consomme tout ce qui reste. [L5 slide 25]

## Retrouver la formule
![Les utilités marginales du plan de l'exemple, 0,02, 0,04 et 0,04. Déplacer un euro de la période 1 à la période 2 en rapporte R, que le moi 1 pèse βδ : la flèche courbe ramène u′(c₂) en période 1 multipliée par βδR, et tombe exactement sur u′(c₁). Entre 2 et 3, le moi 1 ne décote plus que de δ : u′(c₁) = βδR u′(c₂), u′(c₂) = δR u′(c₃).](figures/engagement-complet.svg) [ajout]

Avec $u=\ln$, $\beta=\tfrac12$, $\delta=R=1$ et $w_1=100$, le plan est $(50,25,25)$. Renoncer à un euro en période 1 coûte $u'(50)=0{,}02$. [ajout]

Cet euro placé rapporte $R=1$ en période 2, où il vaut $u'(25)=0{,}04$ ; le moi 1 ne le compte qu'à $\beta\delta=\tfrac12$, soit 0,02. Au plan optimal, le coût et le gain s'égalisent, sinon déplacer l'euro améliorerait le plan. [ajout]

Entre la période 2 et la période 3, les deux dates sont futures : le moi 1 ne les sépare que par $\delta$, et le plan égalise $u'(25)$ et $\delta R\,u'(25)$. [L5 slide 26]

$$u'(c_1)=\beta\delta R\,u'(c_2),\qquad u'(c_2)=\delta R\,u'(c_3)$$ [L5 slide 26]

## Ce qui la définit
Le connu : la richesse de départ, le rendement, les préférences du moi 1. Le trou : les trois consommations. L'engagement complet, c'est que le moi 1 les fixe toutes, et que les moi 2 et 3 n'ont rien à décider. [L5 slide 26]

## Le chemin jusqu'ici
dup/actualisation-quasi-hyperbolique fournit les poids du moi 1 : 1 pour aujourd'hui, $\beta\delta$ et $\beta\delta^2$ pour les deux périodes suivantes, sur des utilités de dup/fonction-utilite. C'est la forme de dup/utilite-actualisee que dup/biais-pour-le-present imposait, pour sortir de dup/actualisation-exponentielle que dup/inversion-des-preferences-dans-le-temps prenait en défaut ; le programme la maximise sous un budget. [L5 slide 25, L5 slide 26]

## Exemple minimal
Avec $u=\ln$, $\beta=\tfrac12$, $\delta=R=1$ et 100 de richesse, le moi 1 s'engage sur 50, 25 et 25. [ajout]

## Geste de calcul type
Avec $u=\ln$, les deux équations donnent $c_2=\beta\delta R\,c_1$ et $c_3=\delta R\,c_2$ ; les reporter dans le budget $c_1+c_2/R+c_3/R^2=w_1$ fixe $c_1$. [ajout]

## Cesse d'être valide quand
L'agent peut réviser son plan à chaque période : le moi 2, qui décote la période 3 de $\beta\delta$ et non de $\delta$, ne suit pas le plan du moi 1. [L5 slide 27]

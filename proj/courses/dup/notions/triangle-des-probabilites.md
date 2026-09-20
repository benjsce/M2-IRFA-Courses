---
id: dup/triangle-des-probabilites
nom: Triangle des probabilités
type: notion
statut: source
construite_a_partir_de:
- dup/utilite-esperee
alias:
- probability triangle
- simplexe de Marschak-Machina
refs:
- L1 slide 44
- L2 slide 4
---

## Ce que c'est
La représentation d’une loterie sur trois résultats comme un point d’un triangle, où l’indépendance devient une propriété visible. [L1 slide 44]

## Ce qui la définit
Les probabilités entrant linéairement, les courbes d’indifférence de l’utilité espérée sont des droites **parallèles**. Le parallélisme est l’indépendance, lue graphiquement. [L1 slide 44]

Les choix de type Allais imposent des pentes qui changent : le motif empirique le plus courant est l’éventail qui s’ouvre. [L1 slide 44]

## Le chemin jusqu'ici
Il faut dup/loterie et dup/fonction-utilite, puis dup/utilite-esperee qu'elles définissent. [ajout]

Le triangle est un outil de lecture, pas une théorie : trois résultats, deux degrés de liberté, donc un plan. Son intérêt tient entièrement à ce qu'il rend visible — sous utilité espérée les courbes d'indifférence y sont des **droites parallèles**. Sans l'utilité espérée au socle, la figure ne dirait rien. [ajout]

## Exemple minimal
Les quatre loteries d’Allais se placent avec $x=2400$, $\alpha=0{,}34$ et $P=\tfrac{33}{34}\delta_{2500}+\tfrac{1}{34}\delta_0$. [L2 slide 16]

## Geste de calcul type
Placer les quatre loteries, tracer les deux segments $A\to B$ et $C\to D$ : ils sont parallèles, donc l’indépendance impose le même classement aux deux paires. [L1 slide 44, L2 slide 16]

## Cesse d'être valide quand
Le triangle ne représente que trois résultats : au-delà, la lecture graphique de l’indépendance n’est plus disponible. [ajout]

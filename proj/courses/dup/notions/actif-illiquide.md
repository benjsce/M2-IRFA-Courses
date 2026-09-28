---
id: dup/actif-illiquide
nom: Actif illiquide
symbole: '$x_t$, $z_t$'
type: notion
statut: source
construite_a_partir_de:
- dup/engagement-complet
- dup/coherence-dynamique
alias:
- illiquid asset
- golden eggs
- œufs d'or
- actif liquide
refs:
- L5 slide 42
- L5 slide 43
- L5 slide 44
- L5 slide 52
---

## Ce que c'est
Un placement qu'on ne peut pas consommer dans la période où il rapporte, et qui engage donc les moi futurs contre leur propre impatience. [L5 slide 42]

## Forme
$$c_t\le y_t+R\,x_{t-1},\qquad c_t+x_t+z_t=y_t+R\,(z_{t-1}+x_{t-1}),\qquad x_t,\,z_t\ge0$$ [L5 slide 43]

## Ce que les symboles modélisent
$x_t$ est l'actif liquide choisi en $t$, $z_t$ l'actif illiquide ; tous deux rapportent le même $R$. $y_t$ est le revenu de la période. Seul ce que rend l'actif liquide peut être consommé tout de suite ; ce que rend l'actif illiquide doit être replacé, et ne devient consommable qu'une période plus tard. [L5 slide 43]

## Ce qui la définit
![Les ressources de la période t et où elles peuvent aller. Le revenu y_t et ce que rend l'actif liquide, R x_{t−1}, peuvent être consommés : c_t ≤ y_t + R x_{t−1}. Ce que rend l'actif illiquide, R z_{t−1}, ne peut qu'être replacé, en x_t ou en z_t : le moi t ne le consomme pas, il le transmet.](figures/actif-illiquide.svg) [ajout]

Le connu : la richesse et les revenus. Le trou : comment empêcher les moi futurs de tout consommer. L'actif illiquide le bouche en partie : ce qu'on y place échappe au moi suivant, qui ne peut que le transmettre au moi d'après. Les deux tiers des actifs des ménages sont de ce type — retraite, fonds de pension, sécurité sociale. [L5 slide 42]

L'hypothèse $x_t\ge0$ est décisive : si l'on pouvait emprunter sans garantie à court terme, sur une carte de crédit, contre l'actif illiquide, il ne lierait plus rien ; et sans elle, des contrats d'épargne forcée contrôleraient parfaitement la consommation future, ce que le droit ne permet pas d'imposer. Un crédit immobilier en est un contre-exemple partiel, trop rigide pour régler la consommation sur les variations du revenu. [L5 slide 44]

La source en tire, sans les développer, une propension à consommer qui dépend de l'actif, un échec de l'équivalence ricardienne même pour des ménages riches, et un effet des marchés du crédit sur la croissance et le bien-être. [L5 slide 52]

## Le chemin jusqu'ici
dup/engagement-complet montrait le plan que le moi 1 voudrait imposer ; dup/coherence-dynamique, qui tombe sous dup/biais-pour-le-present, dit pourquoi il ne le peut pas sans moyen d'engagement. L'actif illiquide est un tel moyen, partiel. [L5 slide 42]

Les poids du moi 1 sont ceux de dup/actualisation-quasi-hyperbolique, forme de dup/utilite-actualisee sur des utilités de dup/fonction-utilite. L'incohérence vient de ce que les choix de dup/inversion-des-preferences-dans-le-temps démentent dup/actualisation-exponentielle, et violent dup/stationnarite alors qu'ils respectent dup/invariance-temporelle. [L5 slide 21, L5 slide 22]

## Exemple minimal
Avec un revenu de 5, un rendement brut de 1,1, 3,82 en actif liquide et 18,18 en actif illiquide, le moi peut consommer au plus $5+1{,}1\times3{,}82=9{,}2$, alors que ses ressources font 29,2. [ajout]

## Geste de calcul type
Vérifier les deux contraintes : la consommation ne dépasse pas le revenu plus le liquide rendu, et les ressources se répartissent exactement entre consommation, liquide et illiquide. [L5 slide 43]

## Cesse d'être valide quand
L'agent peut emprunter contre l'actif illiquide sans délai, ou s'engager par contrat sur sa consommation future : le problème d'engagement disparaît. [L5 slide 44]

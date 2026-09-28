---
id: dup/actualisation-exponentielle
nom: Actualisation exponentielle
symbole: $\delta$
type: notion
statut: source
cas_de: dup/utilite-actualisee
construite_a_partir_de:
- dup/fonction-utilite
alias:
- exponential discounting
refs:
- L5 slide 6
- L5 slide 10
---

## Ce que c'est
Le modèle standard : chaque période d'attente de plus multiplie le poids d'une utilité par le même facteur $\delta$. [L5 slide 6]

## Forme
$$U=u_0+\delta\,u_1+\delta^2u_2+\delta^3u_3+\dots,\qquad D(t)=\delta^t$$ [L5 slide 6, L5 slide 10]

## Ce que les symboles modélisent
$\delta$ est un facteur entre 0 et 1 par période : ce que garde une utilité quand on la repousse d'une période. Il ne dépend pas de la date d'où l'on part, et c'est toute la notion. Ce n'est pas le delta d'une option du cours fpp. [L5 slide 6, ajout]

## Ce qui la définit
Le connu : les utilités instantanées $u_t$. Le trou : leur poids aujourd'hui. Le modèle le bouche d'un seul nombre, $\delta$, élevé à la puissance du délai. [L5 slide 6]

Comme le poids ne dépend que du délai, attendre quatre semaines coûte la même chose, $\delta^4$, qu'on parte d'aujourd'hui ou de la semaine 26 : $D(t)/D(t+\tau)=1/\delta^\tau$. [L5 slide 12]

## Le chemin jusqu'ici
dup/fonction-utilite traduit en utilité ce qui arrive à chaque date ; le modèle exponentiel n'ajoute que la façon de peser les dates. [L5 slide 6]

## Exemple minimal
Avec $\delta=0{,}9$ par semaine et $u(x)=x$, 110 dans quatre semaines vaut $0{,}9^4\times110\approx72{,}2$ aujourd'hui. [ajout]

## Geste de calcul type
Pour comparer $x$ en $t$ et $y$ en $s>t$, comparer $u(x)$ à $\delta^{s-t}u(y)$ : la date commune $t$ s'élimine. [L5 slide 7]

## Cesse d'être valide quand
Les choix observés dépendent de la date d'où l'on part et non du seul délai, comme lorsque l'on préfère 100 tout de suite à 110 dans quatre semaines, mais 110 dans trente semaines à 100 dans vingt-six. [L5 slide 7]

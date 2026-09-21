---
id: dup/theorie-des-perspectives
nom: Théorie des perspectives
symbole: $v(x)$
type: notion
statut: source
cas_de: dup/ponderation-des-probabilites
valeur: un poids appliqué à chaque probabilité séparément
construite_a_partir_de:
- dup/cadrage
alias:
- prospect theory
- Kahneman et Tversky
refs:
- L3 slide 20
- L3 slide 21
- L3 slide 22
---

## Ce que c'est
Une fonction de valeur définie sur les gains et les pertes relatifs à un point de référence, et une fonction de poids appliquée aux probabilités. [L3 slide 21]

## Forme
$$V(x,p;y,q)=\pi(p)v(x)+\pi(q)v(y),\qquad v(0)=0,\ \pi(0)=0,\ \pi(1)=1$$ [L3 slide 21]

## Ce qui la définit
Les deux ingrédients remplacent chacun une pièce de l’utilité espérée. $v$ prend la place de l’utilité de la richesse : elle n’évalue pas un état final mais un **écart** au point de référence, et vaut donc zéro en ce point. $\pi$ prend la place de la probabilité elle-même : ce n’est pas une croyance, c’est le poids que cette probabilité reçoit dans la décision, appliqué branche par branche. [L3 slide 20, L3 slide 21]

Markowitz le premier propose de définir l’utilité sur les écarts à la richesse courante, pour expliquer qu’on achète à la fois de l’assurance et des billets de loterie. [L3 slide 20]

L’aversion aux paris symétriques impose $v(x)<-v(-x)$ : la courbe est plus raide du côté des pertes. Une concavité marquée autour de zéro — un coude — explique les paradoxes d’échelle. [L3 slide 22]

![La courbe de valeur et, en pointillé, sa branche des pertes rabattue dans le quadrant des gains. Elle passe partout au-dessus : c’est toute l’inégalité. La courbe n’est pas graduée, la fiche ne donnant aucune échelle pour $v$.](figures/theorie-des-perspectives.svg) [ajout]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite se combinent en dup/utilite-esperee, dont dup/cadrage montre les limites. [ajout]

La dépendance au cadrage n'est pas anodine : la théorie des perspectives est la première du cours à faire du point de référence une **variable du modèle** plutôt qu'un artefact à éliminer. Elle transforme donc le cadrage d'anomalie en ingrédient. C'est pourquoi elle en dépend au lieu de le contredire. [ajout]

## Exemple minimal
Après avoir reçu 1 000, gagner 1 500 se code comme un gain de 500 ; après avoir reçu 2 000, la même richesse finale se code comme une perte de 500. [ajout]

## Geste de calcul type
Coder d’abord les résultats en écarts au point de référence, puis appliquer $v$ et $\pi$ séparément à chaque branche. [L3 slide 21]

## Cesse d'être valide quand
Appliquer $\pi$ branche par branche viole la dominance stochastique : $V(x,p;x-\epsilon,p;0,1-2p)>V(x,2p;0,1-2p)$ pour $\epsilon$ petit. La phase d’édition, censée y remédier, ne suffit pas. [L3 slide 26] Le point de référence, lui, est pris comme donné : c’est le cadre qui le fixe, et le modèle ne l’explique pas. [L3 slide 20]

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
Markowitz le premier propose de définir l’utilité sur les écarts à la richesse courante, pour expliquer qu’on achète à la fois de l’assurance et des billets de loterie. [L3 slide 20]

L’aversion aux paris symétriques impose $v(x)<-v(-x)$ : la courbe est plus raide du côté des pertes. Une concavité marquée autour de zéro — un coude — explique les paradoxes d’échelle. [L3 slide 22]

## Le chemin jusqu'ici
Le socle commun mène à dup/cadrage. [ajout]

La dépendance n'est pas anodine : la théorie des perspectives est la première du cours à faire du point de référence une **variable du modèle** plutôt qu'un artefact à éliminer. Elle transforme donc le cadrage d'anomalie en ingrédient. C'est pourquoi elle en dépend au lieu de le contredire. [ajout]

## Exemple minimal
Le point de référence est pris comme donné : c’est le cadre qui le fixe, et le modèle ne l’explique pas. [L3 slide 20]

## Geste de calcul type
Coder d’abord les résultats en écarts au point de référence, puis appliquer $v$ et $\pi$ séparément à chaque branche. [L3 slide 21]

## Cesse d'être valide quand
Appliquer $\pi$ branche par branche viole la dominance stochastique : $V(x,p;x-\epsilon,p;0,1-2p)>V(x,2p;0,1-2p)$ pour $\epsilon$ petit. La phase d’édition, censée y remédier, ne suffit pas. [L3 slide 26]

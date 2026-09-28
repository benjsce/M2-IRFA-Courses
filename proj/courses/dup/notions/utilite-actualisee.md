---
id: dup/utilite-actualisee
nom: Utilité actualisée
symbole: '$D(t)$, $u_t$'
type: principe
statut: source
construite_a_partir_de:
- dup/fonction-utilite
alias:
- fonction d'actualisation
- discount function
- discounted utility
refs:
- L5 slide 10
---

## Ce que c'est
Un flux d'utilités datées vaut la somme de chaque utilité instantanée, pesée par le poids $D(t)$ qu'a aujourd'hui une utilité reçue en $t$. [L5 slide 10]

## Forme
$$U=u_0+D(1)\,u_1+D(2)\,u_2+D(3)\,u_3+\dots,\qquad D(0)=1$$ [L5 slide 10]

## Ce que les symboles modélisent
$u_t$ est l'utilité instantanée de la période $t$, celle que procure ce qu'on consomme ou ce qu'on subit à ce moment, par exemple $u(x_t)$ pour un montant $x_t$. Elle ne dit rien de la date : c'est $D$ qui la porte. [L5 slide 6, L5 slide 10]

$D(t)$ prend une date et rend un poids : combien d'unités d'utilité d'aujourd'hui vaut une unité reçue en $t$. Ce n'est pas un prix de marché ni un taux d'intérêt, c'est un trait de l'agent, son impatience. $D(0)=1$ fixe l'unité : aujourd'hui compte pour lui-même. [L5 slide 10]

## Ce qui la définit
Toute l'attitude face au temps est dans la forme de $D$ : l'utilité instantanée est la même à toutes les dates, et seule la pondération des dates change d'un modèle à l'autre. Le cours la pose pour ne rien supposer encore de cette forme, et chercher celle qu'imposent les choix observés. [L5 slide 10, L5 slide 11]

![Un échéancier : l'utilité de chaque date monte au-dessus de l'axe, et une flèche courbe la ramène aujourd'hui en la multipliant par D(t). Arrivées en 0, les utilités s'empilent : U = u₀ + D(1)u₁ + D(2)u₂ + D(3)u₃.](figures/utilite-actualisee.svg) [ajout]

## Le chemin jusqu'ici
dup/fonction-utilite fournit l'utilité instantanée : $u_t=u(x_t)$ traduit ce qui arrive en $t$ en utilité, sans regarder la date. Le principe ajoute l'autre moitié, le poids de la date, et les multiplie. [L5 slide 6, ajout]

## Exemple minimal
Avec $D(t)=\tfrac12$ pour toute date future et $u(x)=x$, recevoir 110 dans quatre semaines vaut $\tfrac12\times110=55$ aujourd'hui. [L5 slide 14]

## Geste de calcul type
Pour comparer $x$ reçu en $t$ et $y$ reçu en $s$, comparer $D(t)\,u(x)$ et $D(s)\,u(y)$. [L5 slide 11]

## Cesse d'être valide quand
L'utilité d'une période dépend de ce qu'on a consommé aux autres, par l'habitude ou la satiété : la somme n'est plus séparable par date, et aucun $D$ ne représente ces préférences. La source ne traite pas ce cas. [ajout]

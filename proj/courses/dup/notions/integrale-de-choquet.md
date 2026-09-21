---
id: dup/integrale-de-choquet
nom: Intégrale de Choquet
symbole: $\int^{C}$
type: notion
statut: source
construite_a_partir_de:
- dup/capacite
alias:
- Choquet integral
refs:
- L4 slide 57
---

## Ce que c'est
L’intégrale d’une fonction par rapport à une capacité, obtenue en empilant les résultats du plus mauvais au meilleur. [L4 slide 57]

## Forme
$$\int^{C}_S z\,\mathrm{d}\mu=\sum_{i=1}^n\big[\mu(A_i)-\mu(A_{i+1})\big]z(s_i),\qquad A_i=\{s_i,\dots,s_n\},\ A_{n+1}=\varnothing$$ [L4 slide 57]

## Ce qui la définit
Les états sont d’abord rangés par valeur croissante, $z(s_1)\le\dots\le z(s_n)$, et les événements $A_i$ sont les queues « à partir de ce rang ». Le poids d’un état est alors la chute de capacité qu’on subit en sortant de sa queue. [L4 slide 57]

La forme équivalente $z(s_1)+\sum_{i\ge2}\big[z(s_i)-z(s_{i-1})\big]\mu(A_i)$ se lit comme un escalier : on part du pire résultat, acquis dans tous les états, et l’on paie chaque marche au prix de la capacité de l’événement où on la franchit. La définition générale, par les deux intégrales de survie, vaut aussi pour les paiements négatifs. [L4 slide 57]

## Le chemin jusqu'ici
dup/acte et dup/fonction-utilite se combinent en dup/utilite-esperee-subjective, que dup/principe-de-la-chose-sure rend possible et que dup/paradoxe-d-ellsberg met en défaut, d’où dup/aversion-a-l-ambiguite puis dup/capacite. [ajout]

Une capacité, à elle seule, ne permet pas encore d’évaluer un acte : l’espérance ordinaire suppose l’additivité, qui vient précisément d’être abandonnée. Cette fiche fournit l’opération de remplacement, et elle ne peut donc venir qu’après l’objet qu’elle intègre. [ajout]

## Exemple minimal
Avec $X(L)=1$, $X(H)=3$, $u(x)=x$ et $\mu(H)=0{,}4$, l’intégrale vaut $1+(3-1)\times0{,}4=1{,}8$. [L4 slide 62]

## Geste de calcul type
Ordonner les états par paiement croissant, écrire les événements emboîtés « à partir de ce rang », puis pondérer chaque marche par la capacité de l’événement correspondant. [L4 slide 57]

## Cesse d'être valide quand
L’ordre des états dépend de la fonction intégrée : changer de position change les événements emboîtés, et l’intégrale n’est donc pas linéaire — c’est ce qui sépare la position longue de la position courte. [L4 slide 57, L4 slide 62]

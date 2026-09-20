---
id: dup/rdu
nom: Utilité dépendante du rang
type: notion
statut: source
cas_de: dup/ponderation-des-probabilites
valeur: un poids appliqué aux probabilités cumulées, selon le rang du résultat
construite_a_partir_de:
- dup/utilite-esperee
alias:
- RDU
- rank-dependent utility
- Quiggin
refs:
- L3 slide 27
- L3 slide 32
- L3 slide 33
---

## Ce que c'est
Déformer non pas chaque probabilité mais la fonction de répartition, ce qui préserve la dominance. [L3 slide 27]

## Forme
$$U(P)=\sum_{i=1}^n\pi_iu(x_i),\qquad \pi_i=\varphi(p_1+\dots+p_i)-\varphi(p_1+\dots+p_{i-1}),\quad \pi_1=\varphi(p_1)$$ [L3 slide 27]

## Ce qui la définit
Les résultats sont d’abord ordonnés, $x_1<\dots<x_n$ ; le poids d’un résultat dépend donc de son rang, et la somme des poids vaut un par construction. C’est ce qui rétablit la dominance. [L3 slide 27]

Deux cas limites : $\varphi$ identité redonne l’utilité espérée, $u$ linéaire donne la théorie duale de Yaari. La concavité de $u$ et celle de $\varphi$ jouent toutes deux dans l’aversion au risque, et une préférence RDU est averse si et seulement si les deux sont concaves. [L3 slide 32]

$$U(F)=\int u(x)\,d\big(\varphi\circ F\big)(x)$$ [L3 slide 33]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite donnent dup/utilite-esperee — les notions que presque tout ce cours suppose acquises. [ajout]

RDU déforme la fonction de répartition et non chaque probabilité prise isolément. Cette différence-là est la raison d'être de la fiche : c'est ce qui lui permet de préserver la dominance stochastique, que la pondération naïve viole. Il fallait donc l'utilité espérée pour dire par rapport à quoi on déforme. [ajout]

## Exemple minimal
Avec $u(x)=x$ et $\varphi(p_1)>p_1$ : $U(x_1,p_1;x_2,p_2)<U(p_1x_1+p_2x_2,1)$, donc l’agent est averse par la seule déformation. [L3 slide 32]

## Geste de calcul type
Ordonner les résultats, cumuler les probabilités, appliquer $\varphi$ aux cumuls, différencier pour obtenir les poids, puis pondérer les utilités. [L3 slide 27]

## Cesse d'être valide quand
Résout les paradoxes d’Allais et, avec un $\varphi$ bien choisi, celui de Rabin — mais le risque de fond ramène ce dernier, sauf à invoquer un cadrage étroit. [L3 slide 34, L3 slide 36, L3 slide 37]

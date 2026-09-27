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
- L4 slide 14
---

## Ce que c'est
Déformer non pas chaque probabilité mais la fonction de répartition, ce qui préserve la dominance. [L3 slide 27]

## Forme
$$U(P)=\sum_{i=1}^n\pi_iu(x_i),\qquad \pi_i=\varphi(p_1+\dots+p_i)-\varphi(p_1+\dots+p_{i-1}),\quad \pi_1=\varphi(p_1)$$ [L3 slide 27]

## Ce que les symboles modélisent
$\varphi$ prend une probabilité **cumulée** — la chance de ne pas faire mieux qu'un résultat donné — et rend ce que cette chance pèse dans la décision. Ce n'est pas une croyance, puisque l'agent connaît ses probabilités, ni une utilité, puisqu'elle ne parle jamais de montants. [L3 slide 27]

Deux conséquences de cet argument-là. Le poids d'un résultat n'est pas $\varphi$ prise à son rang mais le saut qu'elle y fait ; et un même montant ne pèse pas pareil dans deux loteries différentes, puisque son cumul n'y est pas le même. [ajout]

## Ce qui la définit
Le problème est celui-ci. Pondérer chaque probabilité prise isolément peut faire préférer une loterie à une autre qui la domine pourtant résultat par résultat : c’est ce que fait dup/theorie-des-perspectives, et la phase d’édition n’y remédie pas. [L3 slide 26]

Les résultats sont d’abord ordonnés, $x_1<\dots<x_n$ ; le poids d’un résultat dépend donc de son rang, et la somme des poids vaut un par construction. C’est ce qui rétablit la dominance. [L3 slide 27]

$$U(F)=\int u(x)\,d\big(\varphi\circ F\big)(x)$$ [L3 slide 33]

Le modèle demande peu à ses deux ingrédients : $u$ évalue les résultats, et $\varphi$ va de $[0,1]$ dans lui-même, continue, croissante au sens large et surjective. Ce n’est que là où le cours dérive qu’il en exige davantage — $\varphi$ strictement croissante, et $u$ strictement croissante, strictement concave et dérivable. [L3 slide 27, L4 slide 26]

Les deux ne sont pas identifiés de la même façon : $u$ n’est définie qu’à une transformation affine croissante près, tandis que $\varphi$ est fixée. [ajout]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite définissent dup/utilite-esperee, et c'est par rapport à elle que la déformation se mesure. [ajout]

Il fallait l'utilité espérée pour dire par rapport à quoi on déforme : elle est la référence non déformée dont le modèle s'écarte, et non un ingrédient de son calcul. [ajout]

## Exemple minimal
Avec $u(x)=x$ et $\varphi(p_1)>p_1$ : $U(x_1,p_1;x_2,p_2)<U(p_1x_1+p_2x_2,1)$, donc l’agent est averse par la seule déformation. [L3 slide 32]

## Geste de calcul type
Ordonner les résultats, cumuler les probabilités, appliquer $\varphi$ aux cumuls, différencier pour obtenir les poids, puis pondérer les utilités. [L3 slide 27]

## Ce qui reste libre
Les deux objets libres ne portent pas la même chose : la courbure de $u$ mesure la sensibilité à la richesse, la déformation $\varphi$ change le poids accordé à chaque rang. [L4 slide 14]

| paramètre | cas | valeur |
|---|---|---|
| la forme de $u$ | linéaire, $u(x)=x$ | théorie duale de Yaari : toute l’attitude passe par $\varphi$ |
| la forme de $u$ | concave | sensibilité décroissante à la richesse |
| la forme de $\varphi$ | l’identité, $\varphi(p)=p$ | le modèle redonne l’utilité espérée |
| la forme de $\varphi$ | au-dessus de la diagonale, $\varphi(p)\ge p$ | pessimisme : poids cumulé supplémentaire sur les mauvais rangs |
| la forme de $\varphi$ | concave | pessimiste, et le poids marginal décroît avec le rang |
[L3 slide 32, L4 slide 14]

![À gauche, la déformation du cours, $\varphi$ avec $\beta=0{,}7$, sur les probabilités cumulées d'une loterie de trois résultats rangés, de probabilités 0,2, 0,3 et 0,5 : les sauts de $\varphi$ entre les cumuls sont les poids, $\pi_1=\varphi(p_1)$, $\pi_2=\varphi(p_1+p_2)-\varphi(p_1)$, $\pi_3=1-\varphi(p_1+p_2)$, soit 0,26, 0,20 et 0,54. À droite, chaque résultat est une barre de largeur $\pi_i$ et de hauteur $u(x_i)$ : leur aire est $U(P)=\sum\pi_iu(x_i)$.](figures/rdu.svg) [ajout]

## Cesse d'être valide quand
Résout les paradoxes d’Allais et, avec un $\varphi$ bien choisi, celui de Rabin — mais le risque de fond ramène ce dernier, sauf à invoquer un cadrage étroit. [L3 slide 34, L3 slide 36, L3 slide 37]

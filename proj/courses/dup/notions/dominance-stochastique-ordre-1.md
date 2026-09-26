---
id: dup/dominance-stochastique-ordre-1
nom: Dominance stochastique du premier ordre
symbole: $\succ_{FSD}$
type: notion
statut: source
cas_de: dup/principe-d-unanimite
valeur: l’unanimité des agents croissants
construite_a_partir_de:
- dup/utilite-esperee
alias:
- FOSD
- first-order stochastic dominance
refs:
- L1 slide 6
- L1 slide 16
---

## Ce que c'est
Déplacer de la probabilité d’un résultat bas vers un résultat haut augmente l’utilité espérée de tout agent qui préfère plus à moins. [L1 slide 6]

## Forme
$$\tilde x_2\succ_{FSD}\tilde x_1\ \implies\ \mathbb{E}[U(\tilde x_2)]>\mathbb{E}[U(\tilde x_1)]\quad\text{pour toute }U\text{ croissante}$$ [L1 slide 16]

## Ce que les symboles modélisent
$\succ_{FSD}$ relie deux loteries, pas deux nombres, et la relation est **partielle** : deux loteries peuvent n'être comparables ni dans un sens ni dans l'autre. Elle ne dit pas de combien l'une est meilleure, seulement que tout agent préférant plus à moins la préférera. [L1 slide 16]

## Ce qui la définit
Le critère ne demande rien de plus que la croissance de $U$ : c’est le plus large accord qu’on puisse obtenir entre agents. [L1 slide 6]

## Le chemin jusqu'ici
Il faut dup/loterie pour avoir l'objet du choix, dup/fonction-utilite pour l'évaluer, et dup/utilite-esperee qui assemble les deux. [ajout]

La dominance d'ordre 1 est le premier critère sur lequel **tous** les agents s'accordent, à condition seulement que $U$ soit croissante. C'est pourquoi l'utilité espérée doit être là : le critère porte sur les loteries, mais son sens est « tout agent la préfère ». [ajout]

## Exemple minimal
$(0,\tfrac12;100,\tfrac12)$ domine au premier ordre $(0,\tfrac34;100,\tfrac14)$ : même support, plus de poids sur le bon résultat. [ajout]

![Les deux fonctions de répartition de l'exemple. Entre 0 et 100, celle du pari dominant vaut ½ et l'autre ¾ ; ailleurs elles coïncident. Elle n'est donc jamais au-dessus, et l'écart d'un quart est la masse déplacée de 0 vers 100.](figures/dominance-stochastique-ordre-1.svg) [ajout]

## Geste de calcul type
Comparer les deux fonctions de répartition : si l’une est partout au-dessous de l’autre, elle domine, et tout agent croissant est d’accord. Si elles se croisent, le critère ne conclut pas et il faut passer au second ordre. [L1 slide 6, L1 slide 18]

## Cesse d'être valide quand
Elle ne classe pas deux distributions de même moyenne ; il faut alors un critère du second ordre. [L1 slide 18]

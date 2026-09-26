---
id: dss/apprentissage-en-ligne-ou-par-lot
nom: Apprentissage en ligne ou par lot
type: notion
statut: source
construite_a_partir_de:
- dss/retropropagation
alias:
- on-line vs batch
refs:
- slide 155
- slide 163
---

## Ce que c'est
Mettre à jour les poids après chaque motif, ou une seule fois après une passe complète sur les exemples. [slide 163]

## Forme
$$\text{en ligne : }E=\tfrac12\sum_j(t_j-o_j)^2\ \text{pour un motif}\qquad\text{par lot : }E=\tfrac12\sum_{\text{motifs}}\sum_j(t_j-o_j)^2$$ [slide 155, slide 163]

## Ce que les symboles modélisent
C'est la même erreur, sommée ou non sur les motifs. La somme intérieure parcourt les nœuds de sortie $j$ ; la somme extérieure, qui n'existe que par lot, parcourt les motifs présentés pendant une époque. Le cours écrit $E$ dans les deux cas. [slide 155, slide 163]

$t_j$ est la sortie que l'on attendait du nœud $j$ pour un motif donné, $o_j$ celle que le réseau a effectivement produite pour ce même motif. Les deux changent d'un motif à l'autre ; c'est leur écart qu'on cumule. [slide 163, ajout]

## Ce qui la définit
La méthode par lot parcourt un ensemble d'exemples appelé époque, calcule une erreur globale, et ne corrige les poids qu'une fois, sur ce signal cumulé. En ligne, on corrige après chaque motif, sur l'erreur de ce seul motif. [slide 163]

L'échange est énoncé sans détour : l'apprentissage en ligne est plus stochastique et typiquement un peu plus précis, celui par lot est plus efficace. [slide 163]

## Le chemin jusqu'ici
Ce que l'on met à jour, ce sont les corrections de dss/retropropagation : la notion ne change rien à leur calcul, seulement au moment où on les applique. [ajout]

Ces corrections sont des pas de dss/descente-de-gradient, qui déplace les poids là où l'erreur décroît le plus vite, comme la dss/regle-delta le faisait déjà pour un seul neurone ; c'est cette erreur, une somme de carrés, qui peut porter sur un motif ou sur toute l'époque. [ajout]

Le réseau corrigé est un dss/reseau-multicouche, rendu nécessaire par la dss/limite-du-perceptron et entraînable grâce à une dss/fonction-d-activation lisse ; chacun de ses nœuds reprend le dss/perceptron, un dss/reseau-de-neurones-artificiel réduit à un nœud qui calcule une dss/fonction-discriminante-lineaire. [ajout]

Les motifs, enfin, sont les exemples de dss/apprentissage-inductif, accompagnés de la sortie désirée $t_j$ qui fait de l'entraînement un dss/apprentissage-supervise. [ajout]

## Exemple minimal
Sur les quatre exemples du « ou exclusif », l'apprentissage en ligne fait quatre mises à jour par passage, celui par lot une seule, sur la somme des quatre erreurs. [ajout]

## Geste de calcul type
À qualité presque égale, on choisit sur le coût : une mise à jour par motif, ou une par époque. Le cours ne chiffre pas l'écart de précision entre les deux. [slide 163]

## Cesse d'être valide quand
Le cours ne traite pas les lots intermédiaires, qui sont pourtant l'usage courant. [ajout]

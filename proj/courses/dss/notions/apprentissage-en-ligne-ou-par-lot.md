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
- slide 163
---

## Ce que c'est
Mettre à jour les poids après chaque motif, ou après une passe complète sur les exemples. [slide 163]

## Forme
$$E=\tfrac12\sum_{\text{motifs}}\sum_j(t_j-o_j)^2$$ [slide 163]

## Ce que les symboles modélisent
$E$ est ici l'erreur de toute une époque et non celle d'un seul motif : la somme intérieure parcourt les nœuds de sortie $j$, la somme extérieure les motifs présentés. C'est ce second niveau de somme qui fait la méthode par lot ; en ligne, on corrige les poids après chaque motif, sur l'erreur de ce seul motif. [slide 163]

$t_j$ est la sortie que l'on attendait du nœud $j$ pour un motif donné, $o_j$ celle que le réseau a effectivement produite pour ce même motif. Les deux changent d'un motif à l'autre ; c'est leur écart qu'on cumule. [slide 163, ajout]

## Ce qui la définit
La méthode par lot parcourt un ensemble d'exemples appelé époque et calcule une erreur globale ; les mises à jour reposent sur ce signal cumulé. [slide 163]

L'échange est énoncé sans détour : l'apprentissage en ligne est plus stochastique et typiquement un peu plus précis, celui par lot est plus efficace. [slide 163]


## Le chemin jusqu'ici
Le socle est celui de la rétropropagation, la rétropropagation elle-même en plus : dss/apprentissage-supervise, dss/apprentissage-inductif, dss/fonction-discriminante-lineaire, dss/reseau-de-neurones-artificiel, dss/perceptron, dss/limite-du-perceptron, dss/fonction-d-activation, dss/reseau-multicouche, dss/regle-delta, dss/descente-de-gradient, puis dss/retropropagation. [ajout]

La distinction ne porte que sur le moment de la mise à jour, jamais sur son contenu : c'est un choix de cadence, ce qui explique qu'elle n'ajoute rien au socle. [ajout]

## Exemple minimal
Sur 1 000 exemples, l'apprentissage en ligne fait 1 000 mises à jour par époque, celui par lot une seule. [ajout]

## Geste de calcul type
Le choix se fait sur la contrainte de calcul, pas sur la qualité attendue : le cours ne donne pas d'écart de performance chiffré. [slide 163]

## Cesse d'être valide quand
Le cours ne traite pas les lots intermédiaires, qui sont pourtant l'usage courant. [ajout]

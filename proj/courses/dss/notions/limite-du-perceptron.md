---
id: dss/limite-du-perceptron
nom: Limite du perceptron
type: notion
statut: source
construite_a_partir_de:
- dss/perceptron
alias:
- limitations of simple neural networks
- XOR problem
refs:
- slide 148
- slide 149
- slide 150
---

## Ce que c'est
Un perceptron ne forme que des frontières linéaires, et la plupart des fonctions ne sont pas linéairement séparables. [slide 148]

## Ce qui la définit
La démonstration tient en un exemple : le OU exclusif. Les quatre points de sa table de vérité ne peuvent pas être séparés par une droite, et un seul neurone n'y arrive donc pas. [slide 149]

La raison tient en deux lignes. Un neurone de poids $w_0,w_1,w_2$ classerait juste les quatre points s'il avait $w_0\le0$ en $(0,0)$, $w_0+w_2>0$ en $(0,1)$, $w_0+w_1>0$ en $(1,0)$ et $w_0+w_1+w_2\le0$ en $(1,1)$. Les deux inégalités du milieu, additionnées, donnent $2w_0+w_1+w_2>0$ ; les deux autres, $2w_0+w_1+w_2\le0$ : c'est contradictoire. [ajout]

Deux neurones suffisent. Le premier répond 1 au-dessus de la droite basse $x_1+x_2=0{,}5$ : c'est le OU. Le second répond 1 au-dessus de la droite haute $x_1+x_2=1{,}5$ : c'est le ET. Le OU exclusif vaut 1 quand le premier dit oui et le second non, dans la bande entre les deux droites. [slide 149, ajout]

Le cours date l'effet de cette critique : publiée par Minsky et Papert en 1969, elle a paralysé la recherche sur les réseaux pendant quinze ans. [slide 148]

## Le chemin jusqu'ici
Une limite se démontre sur l'objet qu'elle limite : dss/perceptron, le neurone de dss/reseau-de-neurones-artificiel qui réalise une dss/fonction-discriminante-lineaire. Cette fonction est ici doublement nécessaire : elle dit ce que le perceptron sait faire, et donc ce qu'il ne sait pas. [ajout]

La limite porte sur la famille d'hypothèses que dss/apprentissage-inductif demandait de choisir avant de chercher, non sur les exemples de dss/apprentissage-supervise : aucun nombre d'exemples n'y changera rien. [ajout]

## Exemple minimal
Sur le OU exclusif, $(0,0)\mapsto 0$, $(0,1)\mapsto 1$, $(1,0)\mapsto 1$, $(1,1)\mapsto 0$ : les deux classes sont en diagonale et aucune droite ne les sépare. [slide 149]

![Les quatre points des deux tables de vérité, sorties 1 pleines et sorties 0 creuses. Pour le OU, une droite sépare $(0,0)$ des trois autres ; pour le OU exclusif, aucune droite n'y parvient, et il en faut deux, celles de deux neurones, entre lesquelles tombent les sorties 1.](figures/limite-du-perceptron.svg) [ajout]

## Cesse d'être valide quand
La limite porte sur un neurone unique, pas sur les réseaux : des réseaux multicouches plus complexes traitent des problèmes plus difficiles. [slide 150]

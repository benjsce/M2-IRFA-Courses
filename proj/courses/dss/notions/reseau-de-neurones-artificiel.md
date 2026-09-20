---
id: dss/reseau-de-neurones-artificiel
nom: Réseau de neurones artificiel
type: notion
statut: source
construite_a_partir_de:
- dss/apprentissage-supervise
alias:
- artificial neural network
- ANN
refs:
- slide 129
- slide 130
- slide 131
- slide 142
---

## Ce que c'est
Un calcul distribué sur des unités simples et sur les poids de leurs connexions. [slide 130]

## Ce qui la définit
L'inspiration est nommée : traitement et représentation distribués, d'où quatre propriétés recherchées — parallélisme, tolérance aux pannes, dégradation progressive, capacité à généraliser. [slide 130]

Le comportement du réseau sur une entrée dépend de trois choses seulement : la structure de chaque nœud, celle du réseau, et les poids des connexions. Et le cours ajoute aussitôt que ces poids doivent être appris. [slide 142]

L'histoire est celle d'un abandon et d'un retour : les premiers modèles mathématiques en 1943, le perceptron en 1958, la critique de Minsky et Papert en 1969, puis la rétropropagation en 1985. [slide 131]


## Le chemin jusqu'ici
En amont, dss/apprentissage-supervise et rien d'autre. [ajout]

Le cours ne traite qu'une famille de réseaux : entrées continues, propagation avant, erreur globale, apprentissage supervisé. Le réseau est donc posé d'emblée dans ce régime, et non comme un objet général. [ajout]

## Cesse d'être valide quand
Le cours ne traite qu'une seule famille : entrées continues, propagation avant, apprentissage supervisé, erreur globale. Les réseaux récurrents et auto-organisés sont seulement nommés. [slide 137, slide 202]

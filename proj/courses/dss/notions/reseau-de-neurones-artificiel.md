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
Une fonction calculée par des unités simples reliées entre elles, dont le comportement dépend des poids de leurs connexions, qu'on apprend. [slide 130, slide 142]

## Ce qui la définit
Le comportement du réseau sur une entrée dépend de trois choses seulement : la structure de chaque nœud, celle du réseau, et les poids des connexions. Et le cours ajoute aussitôt que ces poids doivent être appris. [slide 142]

L'inspiration est le cerveau, son traitement et sa représentation distribués, dont on attend le parallélisme, la tolérance aux pannes, une dégradation progressive et la capacité à généraliser. [slide 130]

L'histoire tient en une ligne : premiers modèles mathématiques en 1943, perceptron en 1958, critique de Minsky et Papert en 1969, retour en 1985 avec les réseaux multicouches entraînés par rétropropagation. La slide 154 date cette redécouverte de 1986 : la source se contredit d'un an. [slide 131, slide 154]

## Le chemin jusqu'ici
dss/apprentissage-supervise fixe le régime dans lequel le cours pose le réseau : des exemples dont on connaît la sortie désirée, et des poids qu'on ajuste pour la reproduire. [ajout]

## Cesse d'être valide quand
Le cours ne traite qu'une seule famille : entrées continues, propagation avant, apprentissage supervisé, erreur globale. Les réseaux récurrents et auto-organisés sont seulement nommés. [slide 137, slide 202]

---
id: dss/reseau-multicouche
nom: Réseau multicouche à propagation avant
type: notion
statut: source
construite_a_partir_de:
- dss/limite-du-perceptron
- dss/fonction-d-activation
alias:
- multi-layer feed-forward ANN
- MLP
refs:
- slide 141
- slide 151
- slide 152
---

## Ce que c'est
Un réseau où une couche cachée s'intercale entre entrées et sorties, et combine des fonctions linéaires. [slide 151]

## Ce qui la définit
Deux acquis des quinze années de traversée du désert : une couche cachée permet de combiner des fonctions linéaires, et une activation non linéaire dérivable rapproche le nœud d'un neurone réel. Ensemble, ils rendent possible un classifieur non linéaire. [slide 151]

Le comptage des couches du cours est celui des couches actives : un réseau à trois couches a deux couches actives, la cachée et celle de sortie. [slide 141]

Il restait un obstacle, et il a bloqué le domaine : aucun algorithme ne savait ajuster les poids sous la couche cachée, faute de sortie désirée pour ces nœuds. Les poids devaient être posés à la main. [slide 152]


## Le chemin jusqu'ici
Le chemin part de dss/apprentissage-supervise et dss/apprentissage-inductif, passe par dss/fonction-discriminante-lineaire et dss/reseau-de-neurones-artificiel qui donnent dss/perceptron, d'où sortent dss/limite-du-perceptron et dss/fonction-d-activation. [ajout]

Les deux dernières sont les deux moitiés de la réponse : la limite dit qu'il faut une couche cachée, l'activation non linéaire dit ce qu'il faut mettre dans les nœuds pour que cette couche serve à quelque chose. [ajout]

## Cesse d'être valide quand
La structure seule ne suffit pas : sans règle d'ajustement des poids cachés, le réseau n'apprend rien. [slide 152]

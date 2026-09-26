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
Un réseau où une couche cachée de nœuds à activation non linéaire s'intercale entre entrées et sorties, et combine plusieurs frontières linéaires en une frontière qui ne l'est pas. [slide 151]

## Ce qui la définit
Deux acquis des quinze années de traversée du désert : une couche cachée permet de combiner des fonctions linéaires, et une activation non linéaire dérivable rapproche le nœud d'un neurone réel. Ensemble, ils rendent possible un classifieur non linéaire. [slide 151]

Le comptage des couches du cours est celui des couches actives : un réseau à trois couches a deux couches actives, la cachée et celle de sortie. [slide 141]

## Le chemin jusqu'ici
dss/limite-du-perceptron et dss/fonction-d-activation sont les deux moitiés de la réponse : la limite dit qu'il faut plus d'une droite, donc une couche cachée ; l'activation non linéaire dit ce qu'il faut mettre dans ses nœuds pour que cette couche serve à quelque chose. [ajout]

Chaque nœud reste un dss/perceptron, le neurone de dss/reseau-de-neurones-artificiel qui trace une dss/fonction-discriminante-lineaire. Ce qui change, c'est la famille d'hypothèses, au sens de dss/apprentissage-inductif, que le réseau sait représenter ; on l'ajuste toujours sur les exemples de dss/apprentissage-supervise. [ajout]

## Exemple minimal
Le OU exclusif, avec une couche cachée de deux neurones à seuil : $h_1=\text{seuil}(x_1+x_2-0{,}5)$, qui calcule le OU, et $h_2=\text{seuil}(x_1+x_2-1{,}5)$, qui calcule le ET ; la sortie vaut $\text{seuil}(h_1-h_2-0{,}5)$. Les points $(0,1)$ et $(1,0)$ donnent $(h_1,h_2)=(1,0)$ et la sortie 1 ; $(0,0)$ donne $(0,0)$ et $(1,1)$ donne $(1,1)$, tous deux la sortie 0. [ajout]

![À gauche, les quatre points du OU exclusif dans le plan des entrées, sorties désirées 1 pleines et 0 creuses, et les droites des deux nœuds cachés ; à côté de chaque point, le couple $(h_1,h_2)$ qu'ils lui associent. À droite, le plan de ces sorties cachées : $(0,1)$ et $(1,0)$ y tombent au même endroit, et la seule droite $h_1-h_2=0{,}5$ sépare les classes. La couche cachée a rendu le problème linéaire.](figures/reseau-multicouche.svg) [ajout]

## Cesse d'être valide quand
La structure seule ne suffit pas : aucun algorithme ne savait ajuster les poids sous la couche cachée, faute de sortie désirée pour ces nœuds, et les poids devaient être posés à la main. [slide 152]

---
id: dss/perceptron
nom: Perceptron
type: notion
statut: source
construite_a_partir_de:
- dss/reseau-de-neurones-artificiel
- dss/fonction-discriminante-lineaire
alias:
- perceptron
- artificial neuron
refs:
- slide 138
- slide 139
- slide 140
- slide 143
- slide 147
---

## Ce que c'est
Un neurone artificiel qui somme ses entrées pondérées et produit une sortie si la somme dépasse un seuil. [slide 140]

## Forme
$$y=f\Big[\sum_{i=0}^{n}w_ix_i\Big],\qquad f(a)=1 \text{ si } a>0,\quad f(a)=0 \text{ sinon}$$ [slide 143]

## Ce qui la définit
Le calcul est en trois temps : multiplier chaque composante de l'entrée par le poids de sa connexion, sommer et retrancher le seuil, transformer ce total par la fonction d'activation. [slide 140]

Le seuil est traité comme un poids parmi les autres, avec une entrée constante $x_0=1$ : c'est ce qui permet de tout apprendre de la même façon. [slide 143]

La correspondance avec le neurone biologique est terme à terme : les connexions d'entrée sont les dendrites, le nœud le corps cellulaire, la sortie l'axone, les poids les synapses. L'apprentissage se fait par changement des poids. [slide 138, slide 139]

![Le calcul du neurone de gauche à droite : chaque entrée, dont la constante $x_0=1$ qui porte le seuil, est multipliée par son poids, les produits sont sommés, et la fonction seuil rend 0 ou 1.](figures/perceptron.svg) [ajout]

## Le chemin jusqu'ici
Deux fils se rejoignent. dss/apprentissage-supervise donne dss/reseau-de-neurones-artificiel, la machine ; dss/apprentissage-inductif donne dss/fonction-discriminante-lineaire, la forme de ce qu'on apprend. [ajout]

Le perceptron est leur rencontre : un nœud unique dont la sortie est le signe d'une combinaison linéaire, c'est-à-dire une fonction discriminante linéaire réalisée par un neurone. [ajout]

## Exemple minimal
Sur la fonction OU logique, un seul neurone suffit : la frontière $y=f(w_0+w_1x_1+w_2x_2)$ sépare le point $(0,0)$ des trois autres. [slide 147]

## Geste de calcul type
Écrire la table de vérité, placer les quatre points dans le plan, et chercher s'il existe une droite qui sépare les sorties 1 des sorties 0. Si oui, un perceptron suffit. [slide 147]

## Cesse d'être valide quand
L'espace d'hypothèses est celui des vecteurs de poids, $H=\{W\mid W\in\mathbb{R}^{(n+1)}\}$ : il ne contient que des frontières linéaires. [slide 143]

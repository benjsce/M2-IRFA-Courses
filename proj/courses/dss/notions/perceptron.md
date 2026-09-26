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
Un neurone artificiel qui somme ses entrées pondérées et rend 1 si la somme dépasse un seuil, 0 sinon. [slide 140, slide 143]

## Forme
$$y=f\Big[\sum_{i=0}^{n}w_ix_i\Big],\qquad f(a)=1 \text{ si } a>0,\quad f(a)=0 \text{ sinon}$$ [slide 143]

## Ce que les symboles modélisent
$w_i$ est le poids de la connexion qui porte l'entrée $x_i$ jusqu'au neurone, $n$ le nombre d'entrées réelles. L'indice commence à zéro parce que $x_0$ vaut toujours un et que $w_0$ est l'opposé du seuil : la somme contient donc déjà la soustraction du seuil, et le seuil s'apprend comme les autres poids. [slide 143]

La somme pondérée $a=w_0+w_1x_1+w_2x_2$ est exactement la fonction discriminante linéaire. Ici, $f$ ne désigne plus cette somme mais la fonction d'activation, un seuil qui en lit le signe : elle prend $a$, un nombre réel, et rend 1 ou 0. $y$ est la sortie du neurone, et non la classe réelle de l'exemple, que la règle d'apprentissage lui compare ensuite. [slide 143, ajout]

## Ce qui la définit
Le calcul est en trois temps : multiplier chaque composante de l'entrée par le poids de sa connexion, sommer et retrancher le seuil, transformer ce total par la fonction d'activation. [slide 140]

![Le calcul du neurone de gauche à droite : chaque entrée, dont la constante $x_0=1$ qui porte le seuil, est multipliée par son poids, les produits sont sommés, et la fonction seuil rend 0 ou 1.](figures/perceptron.svg) [ajout]

Le vocabulaire vient du neurone biologique : les connexions d'entrée sont les dendrites, le nœud le corps cellulaire, la sortie l'axone, les poids les synapses, et l'apprentissage se fait par changement des poids. [slide 138, slide 139]

## Le chemin jusqu'ici
dss/reseau-de-neurones-artificiel apporte la machine, des unités simples dont on apprend les poids sur les exemples étiquetés de dss/apprentissage-supervise. dss/fonction-discriminante-lineaire apporte la forme de ce qu'on apprend, la famille d'hypothèses la plus simple parmi celles que dss/apprentissage-inductif demande de se donner. [ajout]

Le perceptron est leur rencontre : un nœud unique dont la sortie est le signe d'une combinaison linéaire, c'est-à-dire une fonction discriminante linéaire réalisée par un neurone. [ajout]

## Exemple minimal
Sur la fonction OU logique, un seul neurone suffit, avec $w_0=-0{,}5$ et $w_1=w_2=1$ : le point $(0,0)$ donne une somme de $-0{,}5$, donc 0 ; $(0,1)$ et $(1,0)$ donnent $0{,}5$, donc 1 ; $(1,1)$ donne $1{,}5$, donc 1. [slide 147, ajout]

## Geste de calcul type
Écrire la table de vérité, placer les quatre points dans le plan, et chercher s'il existe une droite qui sépare les sorties 1 des sorties 0. Si oui, un perceptron suffit. [slide 147]

## Cesse d'être valide quand
L'espace d'hypothèses est celui des vecteurs de poids, $H=\{W\mid W\in\mathbb{R}^{(n+1)}\}$ : il ne contient que des frontières linéaires. [slide 143]

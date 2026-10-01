---
id: cs/filtration-naturelle
nom: Filtration naturelle
symbole: '$\mathcal F_t^X$'
type: notion
statut: source
construite_a_partir_de:
- cs/processus-adapte
alias:
- natural filtration
- filtration engendrée par un processus
refs:
- Rem. 0.5.4
---

## Ce que c'est
L'information que fournit l'observation d'un processus jusqu'à la date $t$ ; c'est la plus petite filtration à laquelle ce processus est adapté. [Rem. 0.5.4]

## Forme
$$\mathcal F_t^X=\sigma(X_s ;\ 0\le s\le t)$$ [Rem. 0.5.4]

## Ce que les symboles modélisent
$\mathcal F_t^X$ est la tribu engendrée par toutes les valeurs passées et présente du processus : les événements dont on sait s'ils se sont produits quand on a regardé la trajectoire de $0$ à $t$, et rien d'autre. L'exposant $X$ dit de quel processus vient l'information ; le chapitre suivant écrit $\mathcal F_s^B$ pour le mouvement brownien. [Rem. 0.5.4, ajout]

## Ce qui la définit
Un processus est toujours adapté à sa filtration naturelle, puisque $X_t$ fait partie des variables qui l'engendrent. Et toute filtration à laquelle $X$ est adapté contient $\mathcal F_t^X$ à chaque date : c'est la plus pauvre des informations qui permettent de connaître $X$ au fil du temps. [Rem. 0.5.4, ajout]

## Le chemin jusqu'ici
cs/filtration décrit une information qui grandit, sans dire d'où elle vient ; cs/processus-adapte demande qu'elle soit assez riche pour lire, à chaque date, la valeur d'un cs/processus-stochastique. La filtration naturelle répond à la question inverse, la filtration la plus pauvre qui convienne, et l'obtient en ne retenant que ce qu'on a observé du processus. [Déf. 0.5.8, Déf. 0.5.9, Rem. 0.5.4]

## Exemple minimal
Le joueur qui mise $1$ sur $[0,\tfrac12[$, puis $2$ ou $0$ selon le premier lancer : sa filtration naturelle ne sait rien avant $\tfrac12$ et connaît le premier lancer ensuite ; elle ignore le second lancer, dont la mise ne dépend pas. [ajout]

## Geste de calcul type
Lister ce que la trajectoire observée jusqu'à $t$ révèle, puis prendre la tribu engendrée ; sur un $\Omega$ fini, regrouper en un même bloc les issues dont les trajectoires coïncident sur $[0,t]$. [ajout]

## Cesse d'être valide quand
On veut tenir compte d'une information extérieure au processus : un prix observé en même temps, un autre aléa. La filtration du problème est alors plus grande que la filtration naturelle, et c'est elle qu'il faut nommer. [ajout]

---
id: cs/processus-mesurable
nom: Processus mesurable
symbole: '$\mathcal B([0,T])\otimes\mathcal A$, $T$'
type: notion
statut: source
construite_a_partir_de:
- cs/processus-stochastique
alias:
- measurable process
- mesurabilité jointe
refs:
- Déf. 0.5.6
- §0.5 slide 5
---

## Ce que c'est
Un processus est mesurable quand il l'est comme fonction des deux variables à la fois, le temps et l'aléa ; c'est ce qui permet de l'intégrer en temps et d'obtenir une variable aléatoire. [Déf. 0.5.6, §0.5 slide 5]

## Forme
$$\forall T\in\mathbb R_+,\ \forall E\in\mathcal B(\mathbb R) :\qquad\{(t,\omega) ;\ 0\le t\le T,\ X_t(\omega)\in E\}\in\mathcal B([0,T])\otimes\mathcal A$$ [Déf. 0.5.6]

## Ce que les symboles modélisent
$\mathcal B([0,T])\otimes\mathcal A$ est la tribu produit : celle des événements qui portent à la fois sur une date et sur un monde, engendrée par les rectangles $B\times A$. $T$ est ici une date finale quelconque, et non l'ensemble des indices ; $E$ est un borélien de $\mathbb R$, et non l'espace des valeurs du processus. [Déf. 0.5.6, ajout]

## Ce qui la définit
La définition d'un processus ne demandait la mesurabilité qu'à $t$ fixé, date par date. Celle-ci la demande pour le couple $(t,\omega)$, ce qui est plus fort, et c'est exactement l'hypothèse du théorème de Fubini : on peut alors intégrer en $t$ pour chaque $\omega$ et obtenir une variable aléatoire. Pour $f$ continue et bornée, $Y_t=\int_0^tf(X_s)\,ds$ est une variable aléatoire. [Déf. 0.5.6, §0.5 slide 5]

Un processus continu est mesurable : on l'approche par des processus constants par morceaux en temps, $X^n_t=X_{k/2^n}$ sur $[k/2^n,(k+1)/2^n[$, mesurables comme sommes de produits d'une indicatrice en $t$ et d'une variable aléatoire, et la limite simple de fonctions mesurables est mesurable. [§0.5 slide 5, ajout]

## Le chemin jusqu'ici
cs/processus-stochastique a présenté $(t,\omega)\mapsto X_t(\omega)$ comme une fonction de deux variables, mais n'en a demandé la mesurabilité qu'à $t$ fixé. Cette fiche la demande pour les deux variables ensemble, parce que c'est ce qu'il faut pour intégrer le long des trajectoires. [Déf. 0.5.1, Déf. 0.5.6]

## Exemple minimal
Sur $[0,1]$ avec la mesure de Lebesgue, $X_t(\omega)=\omega+t$ est continu, donc mesurable, et $Y_t=\int_0^tX_s\,ds=\omega t+\tfrac{t^2}{2}$ est une variable aléatoire pour chaque $t$ : pour $t=1$, $Y_1=\omega+\tfrac12$. [§0.5 slide 5, ajout]

## Geste de calcul type
Pour montrer qu'un processus est mesurable, l'écrire comme limite simple de processus étagés en temps, de la forme $\sum_k1_{[t_k,t_{k+1}[}(t)\,Z_k(\omega)$ avec chaque $Z_k$ variable aléatoire ; ou invoquer la continuité des trajectoires, qui fournit cette approximation. [§0.5 slide 5, ajout]

## Cesse d'être valide quand
Les trajectoires ne sont continues que presque sûrement : l'approximation ne converge que hors d'un ensemble négligeable, et il faut, pour conclure, que la tribu $\mathcal A$ contienne les ensembles négligeables, ou modifier le processus sur cet ensemble. Les slides ne le précisent pas. [§0.5 slide 5, ajout]

La mesurabilité jointe ne dit rien de l'information disponible : $\int_0^tf(X_s)\,ds$ est une variable aléatoire, mais rien ne dit encore qu'on la connaît à la date $t$. [§0.5 slide 5, ajout]

## Origine
- exercice cs/ex-0-5-2 : un processus continu est mesurable, par approximation dyadique ; l'ensemble négligeable où la continuité échoue demande une précaution que l'énoncé ne mentionne pas [ajout]

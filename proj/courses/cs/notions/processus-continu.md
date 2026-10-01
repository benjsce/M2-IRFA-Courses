---
id: cs/processus-continu
nom: Processus continu
type: notion
statut: source
construite_a_partir_de:
- cs/processus-stochastique
alias:
- continuous process
- processus à trajectoires continues
refs:
- Déf. 0.5.5
---

## Ce que c'est
Un processus est continu quand presque toutes ses trajectoires sont des fonctions continues du temps. [Déf. 0.5.5]

## Forme
$$\text{pour } P\text{-presque tout }\omega,\qquad t\in T\mapsto X_t(\omega)\ \text{ est continue}$$ [Déf. 0.5.5]

## Ce que les symboles modélisent
$t\mapsto X_t(\omega)$ est la trajectoire du processus dans le monde $\omega$. « Presque tout $\omega$ » autorise un ensemble négligeable de mondes où la trajectoire saute, sans que la définition en souffre. [Déf. 0.5.5, ajout]

## Ce qui la définit
La condition porte sur les trajectoires, c'est-à-dire sur la lecture à $\omega$ fixé. Elle est la seule de ce chapitre à regarder le temps de façon continue, et c'est ce qui lui donne sa force : une trajectoire continue est fixée par ses valeurs aux dates rationnelles, qui sont en nombre dénombrable. [Déf. 0.5.5, §0.5 slide 4, ajout]

## Le chemin jusqu'ici
cs/processus-stochastique a donné les deux lectures d'un processus ; la continuité est une exigence sur l'une d'elles, la trajectoire, et non sur la loi de chaque $X_t$. [Déf. 0.5.1, Déf. 0.5.5]

## Exemple minimal
Sur $[0,1]$, $X_t(\omega)=\omega+t$ est continu : chaque trajectoire est une droite. Le processus $Y$ qui vaut $X_t(\omega)$ sauf en $t=\omega$, où il vaut $0$, ne l'est pas : chacune de ses trajectoires a un trou. [§0.5 slide 4]

## Geste de calcul type
Fixer $\omega$ hors d'un ensemble négligeable, écrire la trajectoire comme une fonction de $t$, et vérifier sa continuité par les règles de l'analyse. [ajout]

## Cesse d'être valide quand
La continuité est une propriété des trajectoires, et deux versions d'un même processus n'ont pas les mêmes : $X$ est continu, sa version $Y$ ne l'est pas. Dire qu'un processus « est continu » demande donc de préciser laquelle de ses versions. [§0.5 slide 4, ajout]

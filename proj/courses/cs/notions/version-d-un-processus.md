---
id: cs/version-d-un-processus
nom: Version d'un processus
type: notion
statut: source
construite_a_partir_de:
- cs/processus-de-meme-loi
alias:
- version
- modification d'un processus
- modification
refs:
- Déf. 0.5.3
- §0.5 slide 3
---

## Ce que c'est
Un processus est une version d'un autre quand, à chaque date fixée, les deux sont égaux presque sûrement. [Déf. 0.5.3]

## Forme
$$\forall t\in T :\qquad X_t=Y_t\quad P\text{-p.s.}$$ [Déf. 0.5.3]

## Ce que les symboles modélisent
$X$ et $Y$ sont deux processus définis sur le même espace $(\Omega,\mathcal A,P)$ et indexés par le même $T$. L'ordre des quantificateurs est tout le sens de la définition : la date $t$ est choisie d'abord, et l'ensemble négligeable où $X_t$ et $Y_t$ diffèrent peut changer d'une date à l'autre. [Déf. 0.5.3, ajout]

## Ce qui la définit
Une version compare les deux processus dans le même monde $\omega$, ce que l'égalité en loi ne faisait pas, mais date par date. Elle entraîne l'égalité en loi : pour un nombre fini de dates, $P\big((X_{t_1},\dots,X_{t_n})\neq(Y_{t_1},\dots,Y_{t_n})\big)\le\sum_iP(X_{t_i}\neq Y_{t_i})=0$. [Déf. 0.5.3, §0.5 slide 3, ajout]

## Le chemin jusqu'ici
Deux processus au sens de cs/processus-stochastique, définis sur le même espace, peuvent se comparer de plusieurs façons. cs/processus-de-meme-loi ne compare que des lois, et laisse deux processus aussi différents que $\omega+t$ et $(1-\omega)+t$ se ressembler. La version exige davantage, l'égalité des valeurs presque sûrement à chaque date, et retrouve l'égalité en loi comme conséquence. [Déf. 0.5.1, Déf. 0.5.2, Déf. 0.5.3]

## Exemple minimal
Sur $[0,1]$ avec la mesure de Lebesgue, $X_t(\omega)=\omega+t$, et $Y_t(\omega)=X_t(\omega)$ sauf à l'instant $t=\omega$, où $Y_t(\omega)=0$ : à $t$ fixé, $X_t$ et $Y_t$ ne diffèrent que si $\omega=t$, ce qui arrive avec probabilité $0$. $Y$ est une version de $X$. [§0.5 slide 4]

## Geste de calcul type
Fixer $t$, écrire l'événement $\{X_t\neq Y_t\}$, et montrer qu'il est négligeable ; ici $\{X_t\neq Y_t\}=\{\omega=t\}$, un point, de mesure de Lebesgue nulle. [§0.5 slide 4, ajout]

## Cesse d'être valide quand
On veut comparer les trajectoires entières : les événements négligeables, un par date, sont en nombre non dénombrable, et leur réunion peut être tout $\Omega$. Il faut alors des processus indistinguables (cs/processus-indistinguables). [§0.5 slide 3, §0.5 slide 4]

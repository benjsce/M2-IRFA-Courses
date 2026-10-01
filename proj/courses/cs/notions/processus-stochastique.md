---
id: cs/processus-stochastique
nom: Processus stochastique
symbole: '$(X_t)_{t\in T}$, $T$, $E$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- stochastic process
- processus aléatoire
- trajectoire
refs:
- Déf. 0.5.1
---

## Ce que c'est
Une famille de variables aléatoires indexée par le temps, toutes définies sur le même espace probabilisé : une valeur aléatoire à chaque date. [Déf. 0.5.1]

## Forme
$$(X_t)_{t\in T},\qquad T\subset\mathbb R_+,\qquad X_t:(\Omega,\mathcal A,P)\to E\ \text{ variable aléatoire pour chaque } t\in T$$ [Déf. 0.5.1]

## Ce que les symboles modélisent
$T$ est l'ensemble des dates, une partie de $\mathbb R_+$ ; dans ce cours, un intervalle comme $[0,T]$ ou $\mathbb R_+$, où la même lettre désigne aussi la date finale. $E$ est l'espace où le processus prend ses valeurs, ici $\mathbb R$ ; ce n'est pas l'espérance, qui porte la même lettre. $(X_t)_{t\in T}$ est le processus entier, et $X_t$ sa valeur à la date $t$. [Déf. 0.5.1, ajout]

## Ce qui la définit
Un processus est une fonction de deux variables, $(t,\omega)\mapsto X_t(\omega)$, et il se lit de deux façons. **À $t$ fixé**, $\omega\mapsto X_t(\omega)$ est une variable aléatoire : ce que vaudra le processus à cette date. **À $\omega$ fixé**, $t\mapsto X_t(\omega)$ est une fonction du temps, une trajectoire : ce que l'on observe dans un monde donné. [Déf. 0.5.1, ajout]

![L'exemple des slides avec a = 1 : ω est tiré uniformément entre 0 et 1, et X_t(ω) = ω + t. Trois tirages, ω = 0,2, 0,5 et 0,9, donnent trois trajectoires, une par ω. La coupe verticale en t = 0,5 les rencontre en 0,7, 1 et 1,4 : X_{0,5} est une variable aléatoire, uniforme entre 0,5 et 1,5.](figures/processus-stochastique.svg) [§0.5 slide 4, ajout]

## Exemple minimal
Sur $\Omega=[0,1]$ muni de la mesure de Lebesgue, $X_t(\omega)=\omega+t$ pour $t\in[0,1]$ : pour $\omega=0{,}2$, la trajectoire va de $0{,}2$ à $1{,}2$ ; à $t=0{,}5$, $X_{0,5}$ suit une loi uniforme sur $[0{,}5\,;1{,}5]$. [§0.5 slide 4, ajout]

## Geste de calcul type
Pour décrire un processus, donner $X_t(\omega)$ comme une formule en $t$ et en $\omega$, puis lire les deux coupes : fixer $t$ pour obtenir la loi de $X_t$, fixer $\omega$ pour tracer une trajectoire. [ajout]

## Cesse d'être valide quand
La définition ne demande rien de plus que d'être une variable aléatoire à chaque date : ni régularité des trajectoires, ni mesurabilité jointe en $(t,\omega)$, ni lien avec l'information disponible. Ce sont les fiches suivantes du chapitre qui les ajoutent, une par une. [Déf. 0.5.1, ajout]

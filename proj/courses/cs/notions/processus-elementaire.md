---
id: cs/processus-elementaire
nom: Processus élémentaire
symbole: '$\mathcal E([0,T]\times\Omega)$, $F_{t_i}$'
type: notion
statut: source
construite_a_partir_de:
- cs/processus-progressivement-mesurable
alias:
- elementary process
- processus étagé
- simple process
- intégrande élémentaire
refs:
- §0.5 slide 11
- §0.5 éq. 1
---

## Ce que c'est
Un processus constant par morceaux en temps, dont la valeur sur chaque intervalle $[t_i,t_{i+1}[$ est une variable aléatoire connue au début de l'intervalle. [§0.5 slide 11]

## Forme
$$X_t=\sum_{i=1}^{n-1}F_{t_i}\,1_{[t_i,t_{i+1}[}(t),\qquad0\le t_1\le\dots\le t_n=T,\qquad F_{t_i}\in L^2(\mathcal F_{t_i})$$ [§0.5 éq. 1, §0.5 slide 11]

## Ce que les symboles modélisent
$F_{t_i}$ est la hauteur de la marche qui commence en $t_i$ : une variable aléatoire de carré intégrable, $\mathcal F_{t_i}$-mesurable, c'est-à-dire décidée avec l'information de la date $t_i$. $1_{[t_i,t_{i+1}[}(t)$ vaut $1$ quand $t$ est dans l'intervalle, $0$ sinon. $\mathcal E([0,T]\times\Omega)$ est l'ensemble de tous les processus de cette forme. [§0.5 slide 11, §0.5 éq. 1, ajout]

## Ce qui la définit
C'est la forme la plus simple d'un processus qui ne regarde pas l'avenir : une stratégie qu'on révise à des dates fixées, avec ce qu'on sait à ces dates, et qu'on tient jusqu'à la révision suivante. Chaque marche est fermée à gauche et ouverte à droite, et la somme s'arrête avant $T$, de sorte que $X_T=0$. [§0.5 slide 11, ajout]

![La mise d'un joueur entre les dates 0 et 1 : t₁ = 0, t₂ = ½, t₃ = T = 1. F_{t₁} = 1, connu en 0 ; en ½ une pièce est lancée, et F_{t₂} vaut 2 si pile, 0 si face, connu en t₂. Les deux trajectoires coïncident jusqu'à ½ puis se séparent ; chaque marche est fermée à gauche, ouverte à droite, et X_T = 0.](figures/processus-elementaire.svg) [ajout]

Un processus élémentaire est progressivement mesurable : restreint à $[0,u]$, il ne garde que les marches qui commencent avant $u$, dont chacune est le produit d'une indicatrice en temps et d'une variable $\mathcal F_{t_i}$-mesurable, donc $\mathcal F_u$-mesurable. [§0.5 slide 11]

## Le chemin jusqu'ici
Un processus élémentaire est un cs/processus-stochastique en escalier, dont chaque marche est lue avec l'information de cs/filtration à sa date de départ : il est adapté au sens de cs/processus-adapte, et mesurable en $(t,\omega)$ au sens de cs/processus-mesurable, puisqu'il est une somme finie de produits d'une indicatrice en temps et d'une variable aléatoire. [§0.5 slide 11]

cs/processus-progressivement-mesurable est la classe des processus qu'on saura intégrer, et dont cs/processus-continu donnait déjà un critère ; le processus élémentaire en est le cas le plus simple, sans continuité, celui sur lequel l'intégrale stochastique sera d'abord définie, par une somme finie. [Prop. 0.5.1, §0.5 slide 11]

## Exemple minimal
La mise du joueur : $X_t=1\cdot1_{[0,\frac12[}(t)+F_{\frac12}\,1_{[\frac12,1[}(t)$, avec $F_{\frac12}=2$ si le premier lancer donne pile et $0$ sinon. [ajout]

## Geste de calcul type
Pour un processus élémentaire, tout calcul se ramène à une somme finie sur les marches. Sa norme : $E\big[\int_0^TX_s^2\,ds\big]=\sum_iE[F_{t_i}^2]\,(t_{i+1}-t_i)$ ; pour la mise du joueur, $1\times\tfrac12+\big(\tfrac12\times4+\tfrac12\times0\big)\times\tfrac12=1{,}5$. [ajout]

## Cesse d'être valide quand
La hauteur d'une marche dépend d'une information postérieure à son début : le processus n'est plus adapté, et ce n'est plus un processus élémentaire au sens du cours. [§0.5 slide 11, ajout]

## Origine
- exercice cs/ex-0-5-3 : la forme (1) est progressivement mesurable ; l'énoncé renvoie à « la forme (2) » pour définir $\mathcal E([0,T]\times\Omega)$, alors que la formule est numérotée (1) [ajout]

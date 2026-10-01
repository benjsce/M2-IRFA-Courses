---
id: cs/esperance-conditionnelle
nom: Espérance conditionnelle
symbole: '$E[X|\mathcal G]$, $\mathcal G$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- conditional expectation
- espérance conditionnelle sachant une tribu
refs:
- Déf. 0.4.1
---

## Ce que c'est
La meilleure prévision de $X$ quand on ne dispose que de l'information $\mathcal G$ : une variable aléatoire qui ne dépend que de $\mathcal G$ et qui a, sur chaque événement de $\mathcal G$, la même moyenne que $X$. [Déf. 0.4.1, ajout]

## Forme
$$Z=E[X|\mathcal G]\iff\begin{cases}\text{i) } Z \text{ est } \mathcal G\text{-mesurable}\\\text{ii) } E[XU]=E[ZU]\ \text{ pour toute } U\ \mathcal G\text{-mesurable et bornée}\end{cases}$$ [Déf. 0.4.1]

## Ce que les symboles modélisent
$\mathcal G$ est une sous-tribu de $\mathcal A$ : l'ensemble des événements dont on saura, une fois l'expérience faite, s'ils se sont produits. C'est une information, pas un événement. [Déf. 0.4.1]

$E[X|\mathcal G]$ est une variable aléatoire et non un nombre : sa valeur dépend de ce que $\mathcal G$ a révélé. Les variables $U$ de la condition ii) sont les paris qu'on peut écrire avec la seule information $\mathcal G$, et ii) dit qu'aucun d'eux ne distingue $X$ de sa prévision. [Déf. 0.4.1, ajout]

## Ce qui la définit
**On connaît** $X$, intégrable, et une information $\mathcal G$ plus pauvre que celle qui fixe $X$. **On cherche** la variable qui résume $X$ avec ce que $\mathcal G$ permet de voir. Le théorème des slides dit qu'elle existe et qu'elle est unique, à une égalité presque sûre près. [Déf. 0.4.1]

Quand $\mathcal G$ découpe $\Omega$ en morceaux — ses atomes —, i) dit que $Z$ est constante sur chacun, et ii), avec $U$ l'indicatrice d'un morceau, que cette constante est la moyenne de $X$ sur le morceau. [ajout]

![Deux lancers de pièce : quatre issues de probabilité ¼, en barres de largeur ¼ et de hauteur X, le nombre de piles. 𝒢 est le premier lancer. Sur l'atome « premier lancer pile », Z = E(X|𝒢) vaut 1,5, et son aire, ½ × 1,5, égale celle de X, ¼ × 2 + ¼ × 1 = 0,75 ; sur « premier lancer face », 0,5 et 0,25. C'est E(XU) = E(ZU) pour U l'indicatrice de l'atome.](figures/esperance-conditionnelle.svg) [ajout]

## Exemple minimal
Deux lancers d'une pièce équilibrée, $X$ le nombre de piles, $\mathcal G$ l'information du premier lancer : $E[X|\mathcal G]=1{,}5$ si le premier lancer donne pile, $0{,}5$ sinon. [ajout]

## Geste de calcul type
Sur une information qui découpe $\Omega$ en atomes $A$ de probabilité non nulle : sur chaque atome, $E[X|\mathcal G]=E[X\,1_A]/P(A)$. Ici, sur $A=\{\text{premier pile}\}$, $E[X1_A]=\tfrac14\times2+\tfrac14\times1=\tfrac34$ et $P(A)=\tfrac12$, d'où $1{,}5$. [ajout]

## Cesse d'être valide quand
$X$ n'est pas intégrable : la définition demande $X\in L^1(\Omega,\mathcal A,P)$. [Déf. 0.4.1]

L'unicité n'est que presque sûre : deux versions de $E[X|\mathcal G]$ peuvent différer sur un événement de probabilité nulle, et toute égalité qui en découle s'entend $P$-p.s. [Déf. 0.4.1]

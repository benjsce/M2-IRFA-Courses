---
id: pfo/modele-factoriel
nom: Modèle factoriel
symbole: '$F_{k,t}$, $\beta_{ik}$, $K$, $N$'
type: principe
statut: source
construite_a_partir_de: []
alias:
- factor model
- modèle à facteurs
- facteurs communs
- common movements
refs:
- §4.1
- §4.2.4
- p. 61
- p. 62
---

## Ce que c'est
Les rendements de nombreux actifs bougent en grande partie ensemble : chacun s'explique par son exposition à quelques facteurs communs, plus une part qui lui est propre. [§4.2.4, p. 62]

## Forme
$$R_{i,t}=\alpha_i+\sum_{k=1}^{K}\beta_{ik}\,F_{k,t}+\varepsilon_{i,t},\qquad K\ll N$$ [p. 61, p. 62, ajout]

## Ce que les symboles modélisent
$F_{k,t}$ est la valeur à la date $t$ du facteur $k$, un mouvement commun à beaucoup d'actifs ; $\beta_{ik}$ est l'exposition de l'actif $i$ à ce facteur, de combien son rendement bouge quand le facteur bouge d'une unité. $\varepsilon_{i,t}$ est ce qui reste, propre à l'actif. $N$ compte les actifs observés, $K$ les facteurs retenus, beaucoup moins nombreux. Le cours écrit la somme sur des composantes principales ; la lettre $F$ pour un facteur quelconque est un ajout. [p. 61, p. 62, ajout]

Ce $K$ n'est pas la kurtosis du chapitre 2, que le cours note de la même lettre. [ajout]

## Ce qui la définit
Quand des actifs évoluent de façon semblable, leurs rendements sont fortement corrélés, et une grande partie de la variation des $N$ rendements s'explique par quelques mouvements communs. Le modèle factoriel passe de $N$ variables observées à $K$ facteurs. [§4.2.4, p. 61]

Le chapitre en tire deux familles. Dans le MEDAF et le modèle de Fama et French, les facteurs sont fixés **a priori** par une théorie économique : le marché ; le marché, la taille et la valeur. Dans l'analyse en composantes principales, ils sont **extraits des données**, à partir de la structure de covariance des rendements. Une fois les facteurs construits, une régression mesure l'exposition de chaque actif à chacun d'eux. [p. 62]

Les deux étapes répondent à deux questions distinctes : quels sont les principaux facteurs communs présents dans les données, et comment chaque actif y est-il exposé ? [p. 62]

## Exemple minimal
L'exercice 2 du cours fabrique quatre actifs qui suivent un même facteur commun, avec des expositions 0,8, 1,2, 0,5 et 1,0, plus un bruit propre à chacun : un facteur pour quatre actifs. [p. 74]

## Geste de calcul type
La variance d'un actif se partage entre le facteur et sa part propre, $\beta_{i1}^2\,\mathrm{Var}(F_1)+\mathrm{Var}(\varepsilon_i)$. Pour le deuxième actif de l'exercice, facteur d'écart type 2 % et bruit de 1 % : $1{,}2^2\times0{,}02^2=0{,}000576$ contre $0{,}01^2=0{,}0001$, soit 85 % de sa variance venue du facteur commun. [p. 74, ajout]

## Cesse d'être valide quand
Le modèle suppose que la part propre de chaque actif ne contient plus de mouvement commun ; si un facteur manque, il reste dans les résidus et y crée des corrélations. [ajout]

Les expositions sont estimées sur une période : si la structure des facteurs change, une estimation unique en donne une moyenne, et il faut la refaire sur des fenêtres glissantes. [p. 66]

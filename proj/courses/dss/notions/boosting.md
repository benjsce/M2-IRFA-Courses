---
id: dss/boosting
nom: Boosting
type: notion
statut: source
cas_de: dss/methode-d-ensemble
valeur: des arbres ajustés en séquence sur les résidus
construite_a_partir_de:
- dss/bagging
- dss/surapprentissage
alias:
- boosting
- gradient boosting
refs:
- slide 122
- slide 123
- slide 124
- slide 125
- slide 126
---

## Ce que c'est
Ajuster les arbres en séquence, chacun sur les résidus laissés par les précédents, c'est-à-dire sur ce que le modèle n'explique pas encore. [slide 123, slide 124]

## Forme
$$\hat f(x)=\sum_{b=1}^{B}\lambda\,\hat f^{\,b}(x)$$
$$\text{départ : }\hat f=0,\ \ r_i=y_i\,;\qquad\text{à chaque pas : }\ \hat f(x)\leftarrow \hat f(x)+\lambda\hat f^{\,b}(x),\quad r_i\leftarrow r_i-\lambda\hat f^{\,b}(x_i)$$ [slide 125]

## Ce que les symboles modélisent
$\hat f(x)$ prend un point $x$ de l'espace des prédicteurs et rend la prédiction de l'ensemble construit jusque-là. $\hat f^{\,b}$ est le seul arbre ajouté au pas $b$, ajusté non sur la réponse mais sur les résidus ; $B$ compte les arbres. $r_i$ est le résidu courant de l'observation $x_i$ : ce que le modèle actuel n'explique pas encore, et non l'erreur de l'arbre qu'on vient d'ajouter. La somme de la première ligne est ce que laissent les mises à jour de la seconde, répétées $B$ fois. [slide 124, slide 125, ajout]

$\lambda$ est le paramètre de rétrécissement, un petit nombre positif : la fraction de chaque arbre qu'on ajoute réellement. Il ne contrôle que la vitesse d'apprentissage. Ce n'est pas le $\lambda$ de ridge ou du lasso, qui pèse une pénalité dans un critère, ni celui de la décroissance des poids : le cours emploie la même lettre pour les trois sans le signaler. [slide 126, ajout]

## Ce qui la définit
À chaque pas, **connu** : la prédiction courante, donc le résidu $r_i$ de chaque observation. **Cherché** : ce qui reste à expliquer. L'arbre suivant est ajusté sur ce reste, et non plus sur $y$. [slide 124]

Le cours le situe face au bagging : pas de tirage bootstrap, des arbres construits en séquence à partir des précédents ; comme lui, il combine un grand nombre d'arbres. [slide 123]

## Le chemin jusqu'ici
Le boosting se définit contre dss/bagging, qui moyenne des arbres ajustés indépendamment sur des tirages de dss/bootstrap : ici, pas de tirage, et chaque arbre dépend des précédents. [slide 123, ajout]

Le bagging s'attaque à la variance, l'une des deux composantes que sépare dss/compromis-biais-variance. Le boosting, lui, fait baisser pas à pas l'erreur sur les clients de dss/apprentissage-supervise, et c'est dss/surapprentissage qui le guette : l'erreur d'apprentissage baisse toujours, dss/erreur-de-test non. [ajout]

## Exemple minimal
Avec $\lambda=0{,}01$ et des arbres à une seule coupure, chaque arbre n'ajoute qu'un centième de sa correction. Sur les 20 clients, dont la perte moyenne vaut 3,60 k€, la prédiction moyenne vaut 0,34 après 10 arbres, soit 10 % de la moyenne ; 2,28 après 100, soit 63 % ; 3,60 après 1 000. [slide 126, ajout]

![Les 20 clients, la perte selon l'endettement seul, et la prédiction du boosting après 10, 100 et 1 000 arbres à une coupure, avec $\lambda=0{,}01$. Chaque arbre n'ajoute qu'un centième de sa correction : après 10 arbres la prédiction a à peine bougé, après 1 000 elle suit les points en escalier.](figures/boosting.svg) [ajout]

## Geste de calcul type
Régler trois paramètres, et le premier par validation croisée : le nombre d'arbres $B$, le rétrécissement $\lambda$ — typiquement 0,01 ou 0,001 — et le nombre de coupures $d$, souvent 1. [slide 126]

Pour voir la lenteur : un arbre à une coupure a pour moyenne celle des résidus, si bien que chaque pas retire un centième de ce qui reste de la moyenne à expliquer. Il en reste $0{,}99^{10}\approx90\,\%$ après 10 arbres, $0{,}99^{100}\approx37\,\%$ après 100. [ajout]

## Cesse d'être valide quand
C'est la seule méthode du chapitre qui surajuste quand $B$ augmente. Le bagging et la forêt aléatoire ne le font pas ; le boosting, si, et il faut donc valider. [slide 126]

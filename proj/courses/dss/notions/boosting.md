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
Ajuster les arbres en séquence, chacun sur les résidus laissés par les précédents. [slide 123]

## Forme
$$\hat f(x)\leftarrow \hat f(x)+\lambda\hat f^{\,b}(x),\qquad r_i\leftarrow r_i-\lambda\hat f^{\,b}(x_i),\qquad \hat f(x)=\sum_{b=1}^{B}\lambda\hat f^{\,b}(x)$$ [slide 125]

## Ce que les symboles modélisent
$\hat f(x)$ prend un point $x$ de l'espace des prédicteurs et rend la prédiction de l'ensemble construit jusque-là. $\hat f^{\,b}$ est le seul arbre ajouté au pas $b$, ajusté non sur la réponse mais sur les résidus ; $B$ compte les arbres. $r_i$ est le résidu courant de l'observation $x_i$ : ce que le modèle actuel n'explique pas encore, et non l'erreur de l'arbre qu'on vient d'ajouter. [slide 124, slide 125]

$\lambda$ est le paramètre de rétrécissement, un petit nombre positif : la fraction de chaque arbre qu'on ajoute réellement. Il ne contrôle que la vitesse d'apprentissage. Ce n'est pas le $\lambda$ de ridge ou du lasso, qui pèse une pénalité dans un critère, ni celui de la décroissance des poids : le cours emploie la même lettre pour les trois sans le signaler. [slide 126, ajout]

## Ce qui la définit
Trois différences avec le bagging, et le cours les énumère : pas de tirage bootstrap, des arbres construits séquentiellement en utilisant l'information des précédents, et une combinaison d'un grand nombre d'arbres. [slide 123]

La variable de réponse change à chaque pas : ce n'est plus $y$ mais le résidu courant. Chaque arbre corrige ce que les précédents n'ont pas expliqué. [slide 124]

Le rétrécissement $\lambda$ ne fait rien d'autre que ralentir : il ne contrôle que le taux d'apprentissage. [slide 126]


## Le chemin jusqu'ici
Deux fils. dss/bootstrap, dss/apprentissage-supervise, dss/erreur-de-test et dss/compromis-biais-variance mènent à dss/bagging, dont le boosting se distingue point par point ; dss/surapprentissage donne ce qui le menace en propre. [ajout]

Le cours le définit entièrement par contraste : pas de tirage bootstrap, des arbres séquentiels, une réponse qui devient le résidu. Et c'est le seul de la famille qui puisse surajuster quand le nombre d'arbres augmente. [ajout]

## Exemple minimal
Avec $\lambda=0{,}01$ et des arbres à une seule coupure, chaque arbre ne corrige qu'un centième de ce qu'il aurait pu corriger. [slide 126]

![Les 20 clients, la perte selon l'endettement seul, et la prédiction du boosting après 10, 100 et 1 000 arbres à une coupure, avec $\lambda=0{,}01$. Chaque arbre n'ajoute qu'un centième de sa correction : après 10 arbres la prédiction a à peine bougé, après 1 000 elle suit les points en escalier.](figures/boosting.svg) [ajout]

## Geste de calcul type
Régler trois paramètres, et le premier par validation croisée : le nombre d'arbres $B$, le rétrécissement $\lambda$ — typiquement 0,01 ou 0,001 — et le nombre de coupures $d$, souvent 1. [slide 126]

## Cesse d'être valide quand
C'est la seule méthode du chapitre qui surajuste quand $B$ augmente. Le bagging et la forêt aléatoire ne le font pas ; le boosting, si, et il faut donc valider. [slide 126]

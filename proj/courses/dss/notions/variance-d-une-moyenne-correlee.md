---
id: dss/variance-d-une-moyenne-correlee
nom: Variance d'une moyenne corrélée
symbole: $\rho$
type: notion
statut: source
construite_a_partir_de:
- dss/bagging
refs:
- slide 108
- slide 109
---

## Ce que c'est
La variance de la moyenne de $B$ variables de même loi ne tombe pas à zéro si elles sont corrélées. [slide 109]

## Forme
$$\mathrm{Var}\Big(\frac{1}{B}\sum_{b=1}^{B}\hat f^{\,b}(x)\Big)=\rho\,\sigma^2+\frac{1-\rho}{B}\,\sigma^2$$ [slide 109]

## Ce que les symboles modélisent
$\rho$ est la corrélation entre deux arbres pris au hasard, et non entre deux prédicteurs. [slide 109]

$\sigma^2$ est la variance de la prédiction $\hat f^{\,b}(x)$ d'un arbre seul, en un point $x$ : pas la variance du bruit, que le $C_p$ de Mallows note $\hat\sigma^2$ avec la même lettre. $B$ est le nombre d'arbres moyennés. [slide 41, slide 109, ajout]

## Retrouver la formule
![La variance de la moyenne de $B$ arbres est la moyenne des cases du tableau de leurs covariances, ici avec $\rho=0{,}5$. Les cases foncées de la diagonale valent $\sigma^2$, les claires $\rho\sigma^2$. Avec 2 arbres, la moyenne des cases vaut $0{,}75\,\sigma^2$ ; avec 4, $0{,}625\,\sigma^2$ ; avec 10, $0{,}55\,\sigma^2$. Quand $B$ grandit, la diagonale ne pèse plus, et il reste $\rho\sigma^2$.](figures/variance-d-une-moyenne-correlee.svg) [ajout]

Deux arbres d'abord, chacun de variance $\sigma^2$, de corrélation $\rho=0{,}5$, donc de covariance $0{,}5\,\sigma^2$. La variance de leur somme additionne les deux variances et deux fois la covariance : $\sigma^2+\sigma^2+2\times0{,}5\,\sigma^2=3\,\sigma^2$. La moyenne divise la somme par 2, donc la variance par 4 : $0{,}75\,\sigma^2$. C'est le premier tableau : quatre cases, et leur moyenne. [ajout]

Avec $B$ arbres, le tableau a $B^2$ cases : les $B$ de la diagonale valent $\sigma^2$, les $B(B-1)$ autres $\rho\sigma^2$. La variance de la moyenne est leur somme divisée par $B^2$, soit $\sigma^2/B+(B-1)\rho\sigma^2/B$. Avec $\rho=0$, on retrouve le $\sigma^2/B$ d'arbres indépendants que rappelle le cours. [slide 109, ajout]

On regroupe les termes en $\sigma^2$ : le premier ne dépend pas de $B$, le second s'efface quand $B$ grandit. Avec $B=2$ et $\rho=0{,}5$, $0{,}5+0{,}25=0{,}75$ : le premier tableau. [ajout]

$$\mathrm{Var}\Big(\frac{1}{B}\sum_{b=1}^{B}\hat f^{\,b}(x)\Big)=\rho\,\sigma^2+\frac{1-\rho}{B}\,\sigma^2$$ [slide 109]

## Ce qui la définit
On connaît la variance $\sigma^2$ d'un arbre, la corrélation $\rho$ entre deux arbres et leur nombre $B$ ; on cherche la variance de leur moyenne. Le second terme disparaît quand $B$ croît, le premier reste : $\rho\sigma^2$ est un plancher qu'aucun nombre d'arbres ne franchit. [slide 109]

La conséquence est directive : pour aller plus bas, il faut faire baisser $\rho$, c'est-à-dire décorréler les arbres. Toute la suite du chapitre en découle. [slide 109, slide 112]

Le biais, lui, ne bouge pas : des arbres de même loi ont une moyenne de même espérance qu'un arbre seul. [slide 108]

## Le chemin jusqu'ici
Le calcul ne sert qu'à dss/bagging : il dit pourquoi la moyenne d'arbres tirés par dss/bootstrap dans les mêmes données ne réduit pas indéfiniment la variance. Ces arbres sont ajustés sur les couples observés de dss/apprentissage-supervise, et c'est leur variance que dss/compromis-biais-variance compte dans l'erreur que mesure dss/erreur-de-test. [ajout]

## Exemple minimal
Avec $\rho=0{,}5$, la variance de la moyenne vaut $0{,}75\,\sigma^2$ pour 2 arbres, $0{,}55\,\sigma^2$ pour 10, $0{,}505\,\sigma^2$ pour 100 et $0{,}501\,\sigma^2$ pour 500. [ajout]

## Geste de calcul type
Comparer les deux termes avant d'ajouter des arbres : à $B=10$ et $\rho=0{,}5$, le second ne vaut déjà plus que $0{,}05\,\sigma^2$, et seule une baisse de $\rho$ fera encore gagner. [slide 109, ajout]

## Cesse d'être valide quand
Le calcul suppose une corrélation de paire commune à tous les couples d'arbres. C'est une simplification que le cours ne discute pas. [ajout]

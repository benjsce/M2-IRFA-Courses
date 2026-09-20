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
$$\rho\,\sigma^2+\frac{1-\rho}{B}\,\sigma^2$$ [slide 109]

## Ce qui la définit
Les arbres d'un bagging sont de même loi mais pas indépendants. L'espérance de leur moyenne vaut donc celle d'un arbre isolé, et le biais du bagging est exactement celui d'un arbre unique. [slide 108]

Pour la variance, le second terme disparaît quand $B$ croît, le premier reste. C'est $\rho\sigma^2$ qui fixe le plancher, et aucun nombre d'arbres ne le franchit. [slide 109]

La conséquence est directive : pour aller plus bas, il faut faire baisser $\rho$, c'est-à-dire décorréler les arbres. Toute la suite du chapitre en découle. [slide 109, slide 112]


## Le chemin jusqu'ici
Le socle est celui du bagging : dss/bootstrap, et par ailleurs dss/apprentissage-supervise, dss/erreur-de-test et dss/compromis-biais-variance, tous réunis dans dss/bagging. [ajout]

Le calcul ne sert qu'à lui : il dit pourquoi la moyenne d'arbres bootstrap ne réduit pas indéfiniment la variance, et désigne la corrélation entre arbres comme le verrou à faire sauter. [ajout]

## Exemple minimal
Avec $\rho=0{,}5$, la variance de la moyenne ne descend jamais sous la moitié de celle d'un arbre isolé, quel que soit $B$. [ajout]

## Geste de calcul type
Quand ajouter des arbres n'améliore plus rien, ne pas en ajouter davantage : c'est le plancher $\rho\sigma^2$ qui est atteint, et il faut agir sur la corrélation. [slide 109]

## Cesse d'être valide quand
Le calcul suppose une corrélation de paire commune à tous les couples d'arbres. C'est une simplification que le cours ne discute pas. [ajout]

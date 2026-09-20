---
id: dup/approximation-arrow-pratt
nom: Approximation d’Arrow-Pratt
type: notion
statut: source
construite_a_partir_de:
- dup/aversion-absolue-arrow-pratt
- dup/prime-de-risque
alias:
- Arrow-Pratt approximation
refs:
- L1 slide 32
- L2 slide 22
- L2 slide 23
- L2 slide 24
---

## Ce que c'est
Pour un petit risque de moyenne nulle, la prime de risque vaut la moitié de la variance fois l’aversion absolue. [L1 slide 32]

## Forme
$$\pi(w_0,u,X)\approx\tfrac12\,\mathrm{Var}(X)\,A(w_0)$$ [L1 slide 32]

## Ce qui la définit
Le produit sépare exactement les deux ingrédients : $\mathrm{Var}(X)$ mesure le risque, $A(w_0)$ mesure l’aversion. Rien d’autre n’entre au premier ordre utile. [L1 slide 32]

La dérivation passe par un développement de Taylor à l’ordre deux de l’équivalent certain $f(t)$ de $w+t\tilde x$ : $f'(0)=\mu$ et $f''(0)=-A(w)\sigma^2$. [L2 slide 23]

$$f(t)\approx w+t\mu-\tfrac12t^2\sigma^2A(w)$$ [L2 éq. 1]

## Le chemin jusqu'ici
Deux fils. dup/fonction-utilite donne dup/aversion-absolue-arrow-pratt, la courbure. dup/utilite-esperee donne dup/equivalent-certain puis dup/prime-de-risque, le coût. [ajout]

L'approximation est le pont entre les deux : pour un petit risque de moyenne nulle, la prime vaut la moitié de la variance fois la courbure. C'est le résultat qui donne son sens à $A(z)$ — sans lui, la courbure ne serait qu'une formule. Et c'est un développement limité, donc valable seulement en petit : toute la suite du cours exploitera cette restriction. [ajout]

## Exemple minimal
Un pari de $\pm10$ à pile ou face, à richesse 100 sous utilité logarithmique : $\pi\approx\tfrac12\times100\times0{,}01=0{,}5$. [ajout]

## Geste de calcul type
Calculer la variance du pari, lire $A$ à la richesse initiale, multiplier, diviser par deux. Valable tant que le pari est petit devant la richesse. [L1 slide 32]

## Cesse d'être valide quand
La moyenne a un effet du premier ordre en $t$, l’écart type seulement du second : c’est ce qui fait qu’un agent à utilité espérée accepte toujours un petit pari actuariellement favorable, si grands que soient $\sigma^2$ et $A(w)$. [L2 slide 24]

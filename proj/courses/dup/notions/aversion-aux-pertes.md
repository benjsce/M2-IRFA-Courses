---
id: dup/aversion-aux-pertes
nom: Aversion aux pertes
symbole: $\lambda$
type: notion
statut: source
construite_a_partir_de:
- dup/theorie-des-perspectives
- dup/aversion-premier-ordre
alias:
- loss aversion
refs:
- L3 slide 39
---

## Ce que c'est
Une perte pèse plus lourd qu’un gain de même taille, avec un coude exactement au point de référence. [L3 slide 39]

## Forme
$$u(x)=\begin{cases}x^\beta&x\ge0\\ -\lambda(-x)^\beta&x\le0\end{cases},\qquad \lim_{x\to0^+}\dfrac{-u(-x)}{u(x)}=\lambda>1$$ [L3 slide 39]

## Ce qui la définit
La fonction est croissante, convexe pour les pertes, concave pour les gains, et concave au premier ordre en zéro. C’est ce coude qui produit l’aversion du premier ordre. [L3 slide 39]

## Le chemin jusqu'ici
Le socle est long parce que deux histoires distinctes s'y rejoignent, et c'est la fin du cours. [ajout]

**Le fil du risque.** La courbure de dup/fonction-utilite se mesure par dup/aversion-absolue-arrow-pratt ; cette même utilité, appliquée à dup/loterie, définit dup/utilite-esperee, puis dup/equivalent-certain et dup/prime-de-risque ; dup/approximation-arrow-pratt réunit les deux branches, ce qui permet de nommer dup/aversion-second-ordre, à quoi s'oppose dup/aversion-premier-ordre. Ce fil dit ce qu'il **faut** : une prime proportionnelle à l'écart type. [ajout]

**Le fil du comportement.** dup/cadrage conduit à dup/theorie-des-perspectives, et avec elle à un point de référence. Ce fil dit ce qu'on **observe** : un coude dans la fonction de valeur. [ajout]

L'aversion aux pertes est exactement le point où les deux se referment : un coude au point de référence produit une prime du premier ordre. C'est pourquoi elle est au niveau le plus profond du cours — non parce qu'elle est difficile, mais parce qu'elle est la conclusion. [ajout]

## Exemple minimal
Avec $\beta=1$ et $\lambda=2$ : gagner 100 vaut $+100$, perdre 100 vaut $-200$. La perte pèse deux fois le gain de même taille. [ajout]

![La pente double en franchissant zéro, et c'est là tout le coude. La droite pointillée est la même fonction avec $\lambda=1$, c'est-à-dire sans aversion aux pertes : elle ne vient pas de la source et sert seulement à rendre le coude visible.](figures/aversion-aux-pertes.svg) [ajout]

## Geste de calcul type
Chercher la limite du rapport $-u(-x)/u(x)$ quand $x\to0^+$ : si elle dépasse un, il y a un coude, donc aversion du premier ordre. [L3 slide 39]

## Cesse d'être valide quand
Le point de référence est donné de l’extérieur ; le modèle ne dit pas d’où il vient, et c’est la question ouverte que le cours renvoie aux modèles de formation endogène. [L3 slide 20]

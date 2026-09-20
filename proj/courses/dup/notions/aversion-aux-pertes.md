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

## Exemple minimal
Avec $\beta=1$ et $\lambda=2$, perdre 100 coûte autant que gagner 200 rapporte. [ajout]

## Geste de calcul type
Chercher la limite du rapport $-u(-x)/u(x)$ quand $x\to0^+$ : si elle dépasse un, il y a un coude, donc aversion du premier ordre. [L3 slide 39]

## Cesse d'être valide quand
Le point de référence est donné de l’extérieur ; le modèle ne dit pas d’où il vient, et c’est la question ouverte que le cours renvoie aux modèles de formation endogène. [L3 slide 20]

---
id: fpp/transformee-de-laplace-gaussienne
nom: Transformée de Laplace gaussienne
symbole: $\lambda$
type: notion
statut: source
construite_a_partir_de: []
alias:
- Gaussian Laplace transform
- moment exponentiel d'une gaussienne
refs:
- Th. 1
- §5.4
---

## Ce que c'est
L'espérance de l'exponentielle d'une variable gaussienne, qui dépasse l'exponentielle de sa moyenne d'un facteur qui ne dépend que de sa variance. [Th. 1]

## Forme
$$E\big(e^{\lambda X}\big)=e^{\lambda\mu+\frac{\lambda^2\sigma^2}{2}}\qquad\text{pour }X\sim\mathcal N(\mu,\sigma^2)$$ [Th. 1]

## Ce que les symboles modélisent
$\lambda$ est un réel quelconque. Ici, $\mu$ et $\sigma$ sont la moyenne et l'écart type de la variable $X$, et non la tendance et la volatilité d'une action ; ils le deviendront quand $X$ sera un log-rendement. [Th. 1]

## Ce qui la définit
Ce qui est **connu** : la moyenne et la variance de $X$. Ce qu'on **cherche** : la moyenne de $e^{X}$. Elle n'est pas $e^{\mu}$ : l'exponentielle est convexe, et ses valeurs hautes l'emportent sur ses valeurs basses. L'écart est le facteur $e^{\sigma^2/2}$. [Th. 1, ajout]

Le poly s'en sert aussitôt : pour que $E\big(S_0\,e^{Y(T)}\big)=S_0\,e^{rT}$, il faut donner au log-rendement la moyenne $rT-\sigma^2T/2$ et non $rT$. [§5.4]

![La courbe exponentielle et deux valeurs d'une variable, −0,2 et +0,2, de moyenne nulle : la moyenne des deux exponentielles, sur la corde, est au-dessus de exp(0) = 1.](figures/transformee-de-laplace-gaussienne.svg) [ajout]

## Exemple minimal
Pour $X$ gaussienne de moyenne nulle et d'écart type 0,2, $E(e^{X})=e^{0,02}\approx1{,}0202$ et non 1. [ajout]

## Geste de calcul type
Choisir la moyenne d'un log-rendement pour atteindre une espérance donnée : pour $E(e^{Y})=e^{rT}$ avec une variance $\sigma^2T$, prendre $\mu_Y=rT-\tfrac12\sigma^2T$. [§5.4]

## Cesse d'être valide quand
$X$ doit être gaussienne. Pour une loi à queues plus épaisses, le facteur de correction est plus grand, et il peut même être infini. [Th. 1, ajout]

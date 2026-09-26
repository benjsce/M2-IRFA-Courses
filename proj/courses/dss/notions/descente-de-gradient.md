---
id: dss/descente-de-gradient
nom: Descente de gradient
type: notion
statut: source
construite_a_partir_de:
- dss/regle-delta
alias:
- gradient descent
- steepest descent
refs:
- slide 160
- slide 162
---

## Ce que c'est
Se déplacer dans l'espace des poids dans la direction où l'erreur décroît le plus vite, à pas fixe. [slide 160]

## Forme
$$\Delta w_{ij}=-\eta\frac{\delta E}{\delta w_{ij}}$$ [slide 155]

## Ce qui la définit
Le gradient est le taux auquel l'erreur change quand les poids changent ; le taux d'apprentissage $\eta$ est la taille du pas, et il est fixe. [slide 160]

La descente la plus raide et la descente avec inertie n'utilisent que le gradient de la surface d'erreur. Des techniques plus avancées explorent l'espace des poids par des heuristiques, la plus courante étant de chercher devant soi dans la direction donnée par le gradient. [slide 162]


## Le chemin jusqu'ici
Le socle est celui de la règle delta : dss/apprentissage-supervise, dss/apprentissage-inductif, dss/fonction-discriminante-lineaire, dss/reseau-de-neurones-artificiel, dss/perceptron, puis dss/regle-delta. [ajout]

La descente de gradient est la lecture générale de cette règle : la correction $\eta d x_i$ est un pas dans la direction opposée au gradient de l'erreur. Nommer ce geste permet de l'appliquer là où la sortie désirée n'existe pas. [ajout]

## Exemple minimal
Avec $\eta=0{,}1$ et un gradient de $-2$, le poids augmente de 0,2. [ajout]

## Geste de calcul type
Si l'erreur oscille au lieu de descendre, réduire le taux d'apprentissage avant de toucher à autre chose. [slide 186]

![Une erreur quadratique choisie pour le dessin, et les pas de la règle $\Delta w=-\eta\,\partial E/\partial w$. Avec $\eta=0{,}1$ le poids glisse vers le minimum ; avec $\eta=0{,}9$ chaque pas franchit le minimum, et le poids oscille d'un bord à l'autre — c'est l'oscillation qu'on corrige en réduisant le taux.](figures/descente-de-gradient.svg) [ajout]

## Cesse d'être valide quand
Le pas est fixe : trop grand il fait osciller, trop petit il fait stagner, et rien dans la méthode ne l'adapte. [slide 162, slide 186]

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
Chercher les poids qui rendent l'erreur minimale en se déplaçant, à pas fixe, dans la direction où elle décroît le plus vite. [slide 160]

## Forme
$$\Delta w_{ij}=-\eta\frac{\delta E}{\delta w_{ij}}$$ [slide 155]

## Ce que les symboles modélisent
$\frac{\delta E}{\delta w_{ij}}$ est la dérivée de l'erreur par rapport à un seul poids : le taux auquel $E$ change quand $w_{ij}$ change, les autres poids restant fixes. Le cours l'écrit tantôt avec des $\delta$, tantôt avec des $\partial$ : c'est la même dérivée partielle, et non le signal d'erreur que la rétropropagation attache à chaque nœud. Le signe moins envoie le poids du côté où l'erreur baisse. [slide 155, slide 159, slide 160, ajout]

$\eta$ est le taux d'apprentissage, c'est-à-dire la taille du pas. $\Delta w_{ij}$ est la correction appliquée à un pas au poids de la connexion du nœud $i$ vers le nœud $j$, et non le poids lui-même. [slide 160, ajout]

## Ce qui la définit
**Cherché** : les poids qui rendent l'erreur minimale. **Connu** : pas la surface d'erreur entière, seulement sa pente au point où l'on est. La descente fait un pas du côté où la pente descend, d'autant plus grand que la pente est forte. [slide 160, ajout]

La règle delta en est un cas. Pour une sortie linéaire, $y=\sum_iw_ix_i$, et l'erreur $E=\tfrac12(t-y)^2$, la dérivée vaut $\partial E/\partial w_i=-(t-y)\,x_i$ : le pas $-\eta\,\partial E/\partial w_i$ est exactement la correction $\eta\,d\,x_i$. Avec le seuil du perceptron, la pente est nulle presque partout, et l'égalité ne tient plus. [ajout]

Des techniques plus avancées cherchent devant elles dans la direction du gradient, au lieu d'y faire un pas fixe. [slide 162, ajout]

## Le chemin jusqu'ici
dss/regle-delta corrige les poids d'un dss/perceptron en proportion de l'erreur et de l'entrée ; la descente de gradient en est la lecture générale, qui ne demande qu'une erreur dérivable, et plus une sortie désirée pour chaque nœud. [ajout]

Ce qu'on déplace, ce sont les poids du neurone de dss/reseau-de-neurones-artificiel, les coefficients d'une dss/fonction-discriminante-lineaire. La recherche dans la famille d'hypothèses que demandait dss/apprentissage-inductif devient une marche dans l'espace des poids, guidée par l'erreur sur les exemples de dss/apprentissage-supervise. [ajout]

## Exemple minimal
Avec l'erreur $E=w^2$ de la figure, au poids $w=4$, la pente vaut 8. Avec $\eta=0{,}1$, le pas vaut $-0{,}8$ et le poids passe à 3,2 ; avec $\eta=0{,}9$, le pas vaut $-7{,}2$ et le poids passe à $-3{,}2$, de l'autre côté du minimum. [ajout]

![Une erreur quadratique choisie pour le dessin, $E=w^2$, et les pas de la règle $\Delta w=-\eta\,\partial E/\partial w$ depuis $w=4$, où seule la pente, 8, est connue. Avec $\eta=0{,}1$ le poids glisse vers le minimum ; avec $\eta=0{,}9$ chaque pas franchit le minimum, et le poids oscille d'un bord à l'autre — c'est l'oscillation qu'on corrige en réduisant le taux.](figures/descente-de-gradient.svg) [ajout]

## Geste de calcul type
Si l'erreur oscille au lieu de descendre, réduire le taux d'apprentissage avant de toucher à autre chose. [slide 186]

## Cesse d'être valide quand
Le pas est fixe : trop grand il fait osciller, trop petit il fait stagner, et rien dans la méthode ne l'adapte. [slide 162, slide 186]

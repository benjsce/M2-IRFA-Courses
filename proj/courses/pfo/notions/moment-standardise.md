---
id: pfo/moment-standardise
nom: Moment d'ordre supérieur
type: abstraite
statut: source
cas_de: pfo/marches-non-gaussiens
parametre: l'ordre du moment centré réduit
construite_a_partir_de: []
alias:
- higher-order moments
- moment centré réduit
- moment standardisé
refs:
- §2.1.2
- §2.2.1
---

## Ce que c'est
L'espérance d'une puissance de l'écart à la moyenne réduit par l'écart type, pour un ordre supérieur à deux. [§2.1.2]

## Forme
$$E\!\left[\left(\dfrac{r-\mu}{\sigma}\right)^{k}\right], \qquad k = 3 \text{ pour l'asymétrie}, \quad k = 4 \text{ pour la kurtosis}$$ [éq. 2.1, éq. 2.2]

## Ce que les membres partagent
Tous deux centrent l'écart sur la moyenne et le réduisent par l'écart type : ils sont sans unité et ne dépendent ni du niveau ni de la dispersion des rendements. Ils décrivent la forme de la loi, là où la moyenne et la variance décrivent sa position et sa taille. [§2.1.2]

La puissance fait la différence. Impaire, elle garde le signe de l'écart et mesure l'asymétrie ; paire et élevée, elle efface le signe, amplifie les écarts lointains et mesure le poids des queues. [p. 21, p. 22, éq. 2.10, éq. 2.11]

## Pourquoi ce niveau existe
Le cours les introduit ensemble pour une seule raison, quantifier l'écart à la normalité, et les réutilise ensemble dans le test de Jarque-Bera et dans le développement de Cornish-Fisher. Ils ne diffèrent que par l'ordre de la puissance. [§2.1.2, §2.3, éq. 2.25]

## Exemple minimal
Pour une loi normale, le moment centré réduit d'ordre 3 vaut 0 et celui d'ordre 4 vaut 3. [§2.1.2]

## Geste de calcul type
En Python, `stats.skew(x)` calcule l'ordre 3 et `stats.kurtosis(x, fisher=True)` l'ordre 4 diminué de 3. [§2.2.1]

## Cesse d'être valide quand
Leurs estimations empiriques sont instables : une puissance 3 ou 4 donne à une poignée d'observations extrêmes l'essentiel du résultat, et le chiffre varie fortement d'un échantillon à l'autre. [ajout]

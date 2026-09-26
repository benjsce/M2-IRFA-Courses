---
id: pfo/score-z
nom: Score z
symbole: '$Z$, $\mu$, $\sigma$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- z-score
- standard score
- score standardisé
- règle empirique
refs:
- p. 9
- éq. 1.9
- p. 10
---

## Ce que c'est
Le nombre d'écarts types qui séparent une observation de la moyenne de son groupe. [p. 9, éq. 1.9]

## Forme
$$Z = \dfrac{x - \mu}{\sigma}$$ [éq. 1.9]

## Ce que les symboles modélisent
$Z$ est un nombre sans unité, positif au-dessus de la moyenne et négatif en dessous : c'est ce qui permet de comparer une note sur vingt à un rendement en pour cent. $\mu$ est la moyenne du groupe auquel on compare l'observation $x$, et $\sigma$ l'écart type qui mesure la dispersion du groupe autour de cette moyenne. [p. 9, p. 10]

Le groupe de référence n'est pas fixé par la formule. Dans le filtre du cours, $\mu$ et $\sigma$ sont une moyenne et un écart type glissants sur vingt jours, et non ceux de la série entière. [Listing 1.1]

## Ce qui la définit
Comparer un écart à la moyenne ne suffit pas : il faut le rapporter à la dispersion du groupe. Une note de 15 dans une classe de moyenne 13 et une note de 13 dans une classe de moyenne 10 ne se comparent qu'une fois divisées par les écarts types des deux classes. [p. 9]

Pour une loi normale, environ 68 % des observations ont un score entre −1 et +1, environ 95 % entre −2 et +2, et un score au-delà de 3 en valeur absolue est très rare, ce qui en fait un détecteur d'anomalies. [p. 10]

![La loi normale graduée en scores : la bande foncée contient environ 68 % des observations, la bande claire environ 95 %, et les verticales marquent le seuil de 3. Le rendement de l'exemple, $-4\,\%$ pour un écart type de 1 %, a un score de $-4$, hors du seuil.](figures/score-z.svg) [ajout]

## Exemple minimal
Un rendement journalier de −4 %, dans un groupe de moyenne nulle et d'écart type 1 %, a un score de −4. [ajout]

## Geste de calcul type
Soustraire la moyenne, diviser par l'écart type, lire la valeur absolue : $(-0{,}04 - 0)/0{,}01 = -4$, donc $|Z| = 4 > 3$ et l'observation est suspecte. [ajout]

## Cesse d'être valide quand
La règle des 68 % et 95 % est énoncée pour une loi normale seulement. [p. 10]

Sur des rendements à queues épaisses, un score au-delà de 3 est bien moins rare que ne le dit la loi normale, où sa probabilité est de 0,27 % : un seuil fixe à 3 prend alors des mouvements réels pour des anomalies. [ajout]

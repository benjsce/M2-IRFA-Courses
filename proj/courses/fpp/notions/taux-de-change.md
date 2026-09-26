---
id: fpp/taux-de-change
nom: Taux de change
symbole: $X_t$
type: notion
statut: source
cas_de: fpp/facteur-conversion
valeur: la devise
construite_a_partir_de: []
refs:
- §2.4
---

## Ce que c'est
Nombre d’unités de devise étrangère pour une unité de devise locale. [§2.4]

## Ce que les symboles modélisent
$X_t$ est un rapport entre deux monnaies, et son sens de lecture est une convention : ici, le nombre d'unités étrangères pour une unité locale. Inverser la convention inverse toutes les formules qui suivent. [§2.4]

## Ce qui la définit
Quand $X$ monte, la devise locale s’apprécie. C’est un facteur atomique : rien ne s’en décline. [§2.4]

Il ne convertit que des montants de la même date : $X_t$ est le taux d'aujourd'hui, et celui d'une date future, $X_T$, n'est pas connu en $t$. Un montant payé plus tard dans l'autre devise se ramène donc d'abord à aujourd'hui dans sa propre devise, puis se convertit au taux du jour. [ajout]

![Deux lignes de temps, dollars en haut, euros en bas. En $t$, passer des dollars aux euros, c'est diviser par $X_t$, connu. En $T$, il faudra diviser par $X_T$, que personne ne connaît aujourd'hui : d'où le pointillé.](figures/taux-de-change.svg) [ajout]

## Cesse d'être valide quand
rien dans le périmètre du cours [ajout]

## Origine
- exercices fpp/ex-09, fpp/ex-13, fpp/ex-18 : **le livre d'exercices emploie $X_t$ en sens inverse du poly.** Le §2.4 pose le nombre d'unités étrangères pour une unité locale ; le livre pose la valeur d'une unité étrangère en monnaie locale. Les deux formules de forward sont justes chacune dans sa convention et opposées terme à terme [exo. 9, exo. 13, exo. 18]

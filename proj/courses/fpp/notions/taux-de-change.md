---
id: fpp/taux-de-change
nom: Taux de change
symbole: $X_t$
type: notion
statut: source
construite_a_partir_de: []
alias:
- exchange rate
- cours de change
- change comptant
refs:
- §2.4
- §2.1
- exo. 13
- exo. 18
---

## Ce que c'est
Le nombre d'unités de devise étrangère que vaut, à la date t, une unité de devise locale. [§2.4]

## Ce que les symboles modélisent
$X_t$ est un prix relatif entre deux devises, lu à une date. Dans la convention du poly, s'il monte, la devise locale s'apprécie ; s'il baisse, elle se déprécie. [§2.4]

Le livre d'exercices prend souvent la convention inverse, la valeur d'une unité étrangère en devise locale : dans ses exercices 13 et 18, $X$ qui monte veut dire que la devise **étrangère** s'apprécie. Et au chapitre 7, le poly note $X(t)$ un processus de diffusion qui n'a rien d'un taux de change. [exo. 13, exo. 18, éq. 17]

## Ce qui la définit
Le change ajuste la valeur de deux unités de devises différentes, comme le taux d'intérêt ajuste celle de deux unités d'une même devise payées à des dates différentes. Un dollar ne vaut pas un euro, et un dollar aujourd'hui ne vaut pas un dollar demain. [§2.1]

## Exemple minimal
$X_t=1{,}10$ : un euro, devise locale, vaut 1,10 dollar ; un dollar vaut donc $1/1{,}10\approx0{,}909$ euro. [ajout]

## Cesse d'être valide quand
Une formule de change n'a de sens qu'avec sa convention : si $X_t$ est le prix de la devise étrangère en devise locale, les deux taux d'intérêt échangent leurs places dans le change à terme. Avant tout calcul, vérifier quelle devise est au numérateur. [exo. 13, §2.4]

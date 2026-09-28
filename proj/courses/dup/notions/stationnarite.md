---
id: dup/stationnarite
nom: Stationnarité
symbole: '$(x,t)$, $\succsim_0$'
type: notion
statut: source
construite_a_partir_de:
- dup/inversion-des-preferences-dans-le-temps
alias:
- stationarity
- gain daté
- dated reward
refs:
- L5 slide 17
---

## Ce que c'est
Décalé du même délai, un choix entre deux gains datés ne change pas, pour qui décide aujourd'hui. [L5 slide 17]

## Forme
$$(x,t)\succsim_0(y,s)\iff(x,t+\tau)\succsim_0(y,s+\tau)$$ [L5 slide 17]

## Ce que les symboles modélisent
$(x,t)$ est un gain daté : le résultat $x$ reçu à la date $t$, un montant, un effort pénible, ou tout autre résultat. $\succsim_0$ est la préférence de la période 0, celle de l'agent qui décide aujourd'hui ; l'indice rappelle qu'un agent peut avoir d'autres préférences à d'autres dates. [L5 slide 17]

## Ce qui la définit
Les deux choix de l'inversion la violent : $(100,0)\succ_0(110,4)$ mais $(100,26)\prec_0(110,30)$. Les deux problèmes sont posés le même jour ; seules les dates des gains ont reculé de 26 semaines. [L5 slide 17]

L'actualisation exponentielle est stationnaire, puisqu'elle pèse deux gains par le seul écart de leurs dates. [L5 slide 7, L5 slide 17]

## Le chemin jusqu'ici
dup/inversion-des-preferences-dans-le-temps fournit les choix, et avec eux dup/actualisation-exponentielle qu'ils contredisent, les utilités venant de dup/fonction-utilite. La stationnarité nomme la propriété qu'ils violent, sans passer par aucun $D$ : elle ne parle que des choix eux-mêmes. [L5 slide 17]

## Exemple minimal
$(100,0)\succ_0(110,4)$ et, décalés de 26 semaines, $(100,26)\succ_0(110,30)$ : un agent stationnaire tranche les deux problèmes de la même façon. [L5 slide 17, ajout]

## Geste de calcul type
Reculer les deux dates d'un même délai, reposer le choix à la même date de décision, et comparer les deux réponses. [L5 slide 17]

## Cesse d'être valide quand
Elle compare des choix faits à la même date, aujourd'hui. Elle ne dit rien de ce que choisira l'agent quand la date de la décision avance elle aussi. [L5 slide 17, L5 slide 18]

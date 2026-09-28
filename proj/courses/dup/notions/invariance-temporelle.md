---
id: dup/invariance-temporelle
nom: Invariance temporelle
symbole: $\succsim_\tau$
type: notion
statut: source
construite_a_partir_de:
- dup/stationnarite
alias:
- time invariance
refs:
- L5 slide 18
- L5 slide 20
---

## Ce que c'est
Reculer du même délai la décision et les deux gains ne change pas le choix. [L5 slide 20]

## Forme
$$(x,t)\succsim_0(y,s)\iff(x,t+\tau)\succsim_\tau(y,s+\tau)$$ [L5 slide 20]

## Ce que les symboles modélisent
$\succsim_\tau$ est la préférence de l'agent quand il décide à la période $\tau$ ; la comparer à $\succsim_0$, c'est comparer deux moments de décision et non plus deux dates de gains. [L5 slide 20]

## Ce qui la définit
Dans vingt-six semaines, on repose à l'agent le premier problème, tel qu'il se présente alors : 100 tout de suite ou 110 dans quatre semaines. Il prend les 100, comme il les avait pris aujourd'hui, $(100,0)\succ_0(110,4)$ et $(100,26)\succ_{26}(110,30)$ : les choix de l'exemple satisfont l'invariance temporelle. [L5 slide 18, L5 slide 20]

C'est une hypothèse naturelle : rien ne distingue la semaine 26 d'aujourd'hui une fois qu'on y est. [L5 slide 22]

## Le chemin jusqu'ici
dup/stationnarite décale les gains sous la même préférence $\succsim_0$, celle d'aujourd'hui ; elle est née des choix de dup/inversion-des-preferences-dans-le-temps, qui contredisent dup/actualisation-exponentielle sur des utilités de dup/fonction-utilite. L'invariance temporelle décale aussi le moment de la décision, et compare donc deux préférences. [L5 slide 17, L5 slide 20]

## Exemple minimal
$(100,0)\succ_0(110,4)$ aujourd'hui, et $(100,26)\succ_{26}(110,30)$ dans vingt-six semaines. [L5 slide 20]

## Geste de calcul type
Reculer du même délai les deux dates des gains et la date de la décision, puis comparer le choix fait alors à celui fait aujourd'hui. [L5 slide 20]

## Cesse d'être valide quand
L'agent n'est plus le même dans vingt-six semaines, par son revenu, sa santé ou ses besoins : la source suppose que seules les dates changent. [ajout]

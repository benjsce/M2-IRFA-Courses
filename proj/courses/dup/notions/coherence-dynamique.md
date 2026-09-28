---
id: dup/coherence-dynamique
nom: Cohérence dynamique
type: notion
statut: source
construite_a_partir_de:
- dup/invariance-temporelle
- dup/biais-pour-le-present
alias:
- dynamic consistency
- time consistency
- cohérence temporelle
- incohérence dynamique
refs:
- L5 slide 20
- L5 slide 21
- L5 slide 22
---

## Ce que c'est
Un plan fait aujourd'hui pour deux dates futures n'est pas renversé quand l'une d'elles approche. [L5 slide 20]

## Forme
$$(x,t)\succsim_0(y,s)\iff(x,t)\succsim_\tau(y,s)\qquad\forall\,\tau\le t,s$$ [L5 slide 20]

## Ce que les symboles modélisent
Les gains datés $(x,t)$ et $(y,s)$ ne bougent pas ; seule la date de la décision passe de 0 à $\tau$, qui ne dépasse aucune des deux dates des gains. [L5 slide 20]

## Ce qui la définit
Les choix de l'exemple la violent : aujourd'hui, $(100,26)\prec_0(110,30)$, l'agent compte attendre les 110 ; à la semaine 26, $(100,26)\succ_{26}(110,30)$, il prend les 100. [L5 slide 20]

De même pour le travail pénible : aujourd'hui, l'agent prévoit sept heures dans dix semaines plutôt que huit dans onze ; arrivé à la semaine 10, il repousse et choisit les huit heures de la semaine 11. [L5 slide 19]

![Les trois problèmes de l'exemple sur une grille : en abscisse la date du premier gain, en ordonnée la date de la décision. La stationnarité décale les gains sous la même décision, l'invariance temporelle décale tout en diagonale, la cohérence dynamique ne décale que la décision : (x,t) ≿₀ (y,s) ⟺ (x,t) ≿τ (y,s). La diagonale suivie de la descente refait le chemin horizontal.](figures/coherence-dynamique.svg) [ajout]

Invariance temporelle et cohérence dynamique ensemble impliquent la stationnarité : $(x,t)\succsim_0(y,s)\iff(x,t+\tau)\succsim_\tau(y,s+\tau)$ par l'invariance, $\iff(x,t+\tau)\succsim_0(y,s+\tau)$ par la cohérence. Des choix non stationnaires obligent donc à renoncer à l'une des deux ; si l'on garde l'invariance, comme l'exemple le fait, c'est la cohérence qui tombe. [L5 slide 21, L5 slide 22]

Le biais pour le présent est ainsi une source naturelle d'incohérence dynamique. [L5 slide 22]

## Le chemin jusqu'ici
dup/invariance-temporelle compare deux dates de décision, en reculant aussi les gains ; elle prolonge dup/stationnarite, qui ne reculait que les gains. La cohérence dynamique garde les gains en place et ne fait avancer que la décision : les trois conditions portent sur les mêmes choix de dup/inversion-des-preferences-dans-le-temps. [L5 slide 20, L5 slide 21]

dup/biais-pour-le-present, la condition que ces choix imposent au poids de dup/utilite-actualisee, est ce qui fait tomber la cohérence : dup/actualisation-exponentielle, stationnaire sur les utilités de dup/fonction-utilite, la gardait. [L5 slide 12, L5 slide 22]

## Exemple minimal
$(100,26)\prec_0(110,30)$ aujourd'hui, mais $(100,26)\succ_{26}(110,30)$ à la semaine 26 : le plan d'attendre les 110 est renversé. [L5 slide 20]

## Geste de calcul type
Garder les deux gains datés, faire avancer la date de la décision jusqu'au premier d'entre eux, et comparer le choix fait alors à celui fait aujourd'hui. [L5 slide 20]

## Cesse d'être valide quand
Elle ne dit pas ce que fait l'agent qui sait qu'il changera d'avis : c'est l'objet de la sophistication. [L5 slide 25]

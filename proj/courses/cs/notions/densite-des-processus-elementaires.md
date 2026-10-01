---
id: cs/densite-des-processus-elementaires
nom: Densité des processus élémentaires
type: notion
statut: source
construite_a_partir_de:
- cs/espace-l2-progressif
- cs/processus-elementaire
alias:
- density of elementary processes
- complétude de L²_prog
- approximation par des processus élémentaires
refs:
- Th. 0.5.2
---

## Ce que c'est
Tout processus progressivement mesurable de carré intégrable est limite, pour la norme de $L^2_{prog}$, de processus élémentaires ; et cet espace est complet. [Th. 0.5.2]

## Forme
$$L^2_{prog}(\Omega\times[0,T])\ \text{est complet, et}\ \ \forall X\in L^2_{prog},\ \exists\,(X^n)\subset\mathcal E([0,T]\times\Omega) :\ E\Big[\int_0^T(X_s-X^n_s)^2\,ds\Big]\xrightarrow[n\to\infty]{}0$$ [Th. 0.5.2]

## Ce que les symboles modélisent
$X^n$ est une suite de processus élémentaires, des escaliers dont chaque marche est décidée à son départ. $E\big[\int_0^T(X_s-X^n_s)^2\,ds\big]$ est le carré de la distance de $L^2_{prog}$ entre $X$ et son approximation. [Th. 0.5.2, ajout]

## Ce qui la définit
**On connaît** l'intégrale d'un processus élémentaire, une somme finie, à venir au chapitre de l'intégrale stochastique. **On cherche** à l'étendre à tout $L^2_{prog}$. Le théorème fournit les deux ingrédients : la densité, pour approcher n'importe quel intégrande par des escaliers ; la complétude, pour que la limite des intégrales existe dans le même espace. [Th. 0.5.2, ajout]

![X_t = t entre les dates 0 et 1, et l'escalier Xⁿ qui prend sur chaque marche la valeur de X à son départ : pour n = 2 puis n = 4, les triangles colorés sont l'écart X − Xⁿ, et E(∫(X_s − Xⁿ_s)² ds) = 1/(3n²) vaut 1/12 puis 1/48. Le pas se resserre, l'écart tend vers 0.](figures/densite-des-processus-elementaires.svg) [ajout]

## Le chemin jusqu'ici
cs/espace-l2-progressif est l'espace où vivront les intégrandes : la norme de cs/espace-l2-des-processus, restreinte aux processus de cs/processus-progressivement-mesurable, eux-mêmes un cs/processus-stochastique à la fois mesurable au sens de cs/processus-mesurable et adapté à une cs/filtration au sens de cs/processus-adapte. [Déf. 0.5.11]

cs/processus-elementaire est la classe simple où l'intégrale se définit d'abord. Le théorème relie les deux : la classe simple est dense dans l'espace, et l'espace est complet. Pour un processus continu (cs/processus-continu), l'approximation est explicite : l'escalier qui prend la valeur au départ de chaque marche. [§0.5 slide 11, Th. 0.5.2]

## Exemple minimal
Pour $X_t=t$ sur $[0,1]$ et l'escalier à $n$ marches égales qui prend la valeur de $X$ au départ de chacune, l'écart vaut $\tfrac{1}{3n^2}$ : $\tfrac1{12}$ pour $n=2$, $\tfrac1{48}$ pour $n=4$. [ajout]

## Geste de calcul type
Pour un processus continu, approcher par l'escalier qui prend, sur $[t_i,t_{i+1}[$, la valeur $X_{t_i}$ ; c'est un processus élémentaire, puisque $X_{t_i}$ est connue en $t_i$. Calculer l'écart marche par marche : pour $X_t=t$, $\int_{t_i}^{t_{i+1}}(s-t_i)^2\,ds=\tfrac{h^3}{3}$ avec $h=\tfrac1n$, et $n$ marches donnent $\tfrac{1}{3n^2}$. [ajout]

## Cesse d'être valide quand
L'escalier prend la valeur de $X$ à la fin de la marche plutôt qu'au début : il converge aussi, mais il regarde l'avenir et n'est pas un processus élémentaire. La valeur au départ de chaque marche est la seule qui respecte l'information. [ajout]

---
id: dup/intervalle-de-non-echange
nom: Intervalle de non-échange
type: notion
statut: source
construite_a_partir_de:
- dup/ceu
alias:
- no-trade interval
- zone d'abstention
refs:
- L4 slide 62
---

## Ce que c'est
Une plage de prix sur laquelle l’agent ambigu ne prend ni position longue ni position courte. [L4 slide 62]

## Forme
$$V(X)<p<-V(-X)\ \Longrightarrow\ \text{toute position non nulle est dominée par zéro}$$ [L4 slide 62]

## Ce que les symboles modélisent
$X$ est l'actif, décrit par son paiement dans chaque état, et $-X$ la position courte, qui paie l'opposé. $V$ prend une position et rend son intégrale de Choquet ; comme elle n'est pas linéaire, $-V(-X)$ ne coïncide pas avec $V(X)$. $p$ est le prix d'une unité de l'actif, le rendement brut sans risque étant normalisé à un. [L4 slide 62, ajout]

## Ce qui la définit
La position longue et la position courte s’évaluent séparément, parce que l’évaluation n’est pas linéaire : le pire état n’est pas le même selon le sens de la position. Avec $X(L)=1$, $X(H)=3$, $u(x)=x$, $\mu(L)=0{,}3$ et $\mu(H)=0{,}4$, on obtient $V(X)=1{,}8$ et $V(-X)=-2{,}4$. [L4 slide 62]

Au prix $p$, la position longue vaut alors $1{,}8-p$ et la position courte $p-2{,}4$ : les deux sont négatives tant que le prix reste entre les deux bornes. Aux bornes elles-mêmes l’agent est indifférent, de sorte que zéro est optimal sur l’intervalle fermé et strictement préféré à l’intérieur seulement. [L4 slide 62]

## Le chemin jusqu'ici
dup/acte et dup/fonction-utilite se combinent en dup/utilite-esperee-subjective, que dup/principe-de-la-chose-sure rend possible et que dup/paradoxe-d-ellsberg met en défaut, d’où dup/aversion-a-l-ambiguite puis dup/capacite et dup/integrale-de-choquet. Le cadre axiomatique arrive par l’autre côté : dup/acte et dup/loterie s’emboîtent dans dup/cadre-anscombe-aumann, où dup/independance-comonotone affaiblit l’axiome de mélange. Les deux fils se referment sur dup/ceu. [ajout]

L’intervalle n’est alors qu’un calcul, mais un calcul qui ne se pose pas avant : il faut une évaluation non linéaire pour que la valeur d’une position et celle de son opposé cessent d’être opposées. C’est cet écart, et lui seul, qui ouvre la plage de prix. [ajout]

## Exemple minimal
Au prix 2, ni acheter, qui vaut $-0{,}2$, ni vendre, qui vaut $-0{,}4$, ne bat l’abstention. [L4 slide 62]

![La valeur d'une unité achetée, $1{,}8-p$, et celle d'une unité vendue, $p-2{,}4$, selon le prix. Les deux sont négatives entre 1,8 et 2,4, sur la bande grisée ; au prix 2 elles valent $-0{,}2$ et $-0{,}4$.](figures/intervalle-de-non-echange.svg) [ajout]

## Geste de calcul type
Calculer l’intégrale de Choquet de la position longue et celle de la position courte, puis lire l’intervalle des prix où les deux sont négatives. [L4 slide 62]

## Cesse d'être valide quand
L’abstention n’est stricte qu’à l’intérieur de l’intervalle, et le résultat tient à la linéarité de l’utilité : avec une pénalité de variance strictement positive, zéro redevient l’unique optimum jusqu’aux bornes incluses. [L4 slide 62, L4 slide 65]

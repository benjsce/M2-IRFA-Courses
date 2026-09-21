---
id: dup/ensemble-de-priors
nom: Ensemble de priors
symbole: $K$
type: notion
statut: source
construite_a_partir_de:
- dup/cadre-anscombe-aumann
alias:
- set of priors
- ensemble de probabilités plausibles
- plausible priors
refs:
- L4 slide 39
- L4 slide 40
---

## Ce que c'est
Un ensemble de probabilités sur les états, non vide, compact et convexe, qui remplace la croyance ponctuelle. [L4 slide 38]

## Forme
$$K\subseteq\Delta(S),\qquad \Delta(S)=\Big\{p:\ p_s\ge0,\ \textstyle\sum_s p_s=1\Big\}$$ [L4 slide 38, L4 slide 39]

## Ce que les symboles modélisent
$\Delta(S)$ est l'ensemble de toutes les probabilités qu'on pourrait poser sur les états — pour trois états, un triangle. $K$ en est une partie : les compositions que l'agent juge plausibles. $K$ ne hiérarchise pas ses éléments, aucune probabilité n'y étant plus crédible qu'une autre, et c'est ce qui le sépare d'une loi portant sur les lois. [L4 slide 38, L4 slide 40]

$K$ est le même objet que le $\Pi$ de L1 slide 64, sous une autre lettre. [ajout]

## Ce qui la définit
Pour trois états, le simplexe se dessine comme un triangle dont les sommets sont les certitudes : un prior y est un point, un ensemble de priors une partie du triangle. C’est la même géométrie que le diagramme de Marschak-Machina, appliquée cette fois aux croyances et non aux loteries. [L4 slide 39]

L’ensemble dit l’étendue des compositions jugées plausibles, et rien de plus. Il n’attribue aucune probabilité du second ordre à ses éléments : aucun prior n’y est plus crédible qu’un autre, et c’est ce refus de hiérarchiser qui distingue cette représentation des modèles d’ambiguïté lisse. [L4 slide 40]

## Le chemin jusqu'ici
dup/acte et dup/loterie s’emboîtent dans dup/cadre-anscombe-aumann, qui fixe l’espace des états et le simplexe des probabilités qu’on peut poser dessus. [ajout]

L’ensemble de priors est une partie de ce simplexe, et ne se définit donc qu’une fois celui-ci en place. L’ordre compte : on ne peut renoncer à choisir une probabilité qu’après avoir dit parmi quoi on renonce à choisir. [ajout]

## Exemple minimal
$K=\{p:0{,}2\le p_R\le0{,}6\}$ est la bande du triangle comprise entre les deux droites $p_R=0{,}2$ et $p_R=0{,}6$. [L4 slide 40]

## Geste de calcul type
Traduire l’information disponible en contraintes linéaires sur les $p_s$, puis lire l’ensemble obtenu comme une partie du simplexe : plus l’information est mince, plus la partie est large. [L4 slide 40]

## Cesse d'être valide quand
L’ensemble décrit ce qui est plausible sans dire ce qui l’est le plus, et il ne dit pas non plus d’où il vient : le calibrer demande davantage d’observations qu’une probabilité unique. [L4 slide 40, L4 slide 37]

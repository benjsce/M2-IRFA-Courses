---
id: dup/ceu
nom: Utilité espérée de Choquet
type: notion
statut: source
cas_de: dup/reponse-a-l-ambiguite
valeur: une capacité non additive
construite_a_partir_de:
- dup/integrale-de-choquet
- dup/independance-comonotone
alias:
- Choquet expected utility
- CEU
refs:
- L1 slide 64
- L4 slide 60
---

## Ce que c'est
Remplacer la probabilité additive par une capacité, qui pondère les événements sans que les poids somment à un. [L1 slide 64]

## Forme
$$f\succsim g\iff\int^{C}_S u\big(f(s)\big)\,\mathrm{d}\mu\ \ge\ \int^{C}_S u\big(g(s)\big)\,\mathrm{d}\mu$$ [L4 slide 60]

## Ce qui la définit
Les poids de décision peuvent alors refléter la non-additivité des croyances et l’ambiguïté d’un événement, ce qu’une probabilité interdit par construction. [L1 slide 64]

Le théorème de Schmeidler donne l’axiomatique exacte : une préférence satisfait les quatre axiomes de base et l’indépendance comonotone si et seulement si elle s’écrit sous cette forme, pour une capacité et une utilité affine non constante. La capacité est unique, l’utilité l’est à une transformation affine croissante près. [L4 slide 60]

Quand la capacité est convexe, le modèle se relit comme un maxmin sur son cœur, $V(f)=\min_{p\in C(\mu)}\sum_s p(s)u(f(s))$. Les deux familles se recoupent donc sans se confondre : la forme générale n’exige pas la convexité, et un maxmin quelconque n’est pas une utilité de Choquet. [L4 slide 60]

## Le chemin jusqu'ici
Un premier fil apporte l'objet. dup/acte et dup/fonction-utilite se combinent en dup/utilite-esperee-subjective, que dup/principe-de-la-chose-sure rend possible et que dup/paradoxe-d-ellsberg met en défaut, d'où dup/aversion-a-l-ambiguite, à quoi répond dup/capacite, qu'on évalue par dup/integrale-de-choquet. [ajout]

Un second fil apporte l'axiome. dup/acte et dup/loterie s'emboîtent dans dup/cadre-anscombe-aumann, où dup/independance-comonotone restreint le mélange aux actes qui classent les états de la même façon. [ajout]

Ce qui est propre à cette fiche tient à leur rencontre : on garde une seule mesure mais on lui retire l'additivité, et c'est le silence de l'axiome sur les actes non comonotones qui autorise ce retrait. Une capacité peut attribuer aux deux moitiés d'un événement moins que le tout, et ce défaut d'additivité est exactement ce qui encode l'aversion à l'ambiguïté. [ajout]

## Exemple minimal
Une capacité qui donne $1/3$ au rouge et moins de $1/3$ au noir, alors que leurs complémentaires ne somment pas à un. [ajout]

## Geste de calcul type
Intégrer au sens de Choquet : ordonner les conséquences, puis pondérer par les différences de capacité des ensembles emboîtés — le même geste que l’utilité dépendante du rang, transposé aux événements. [ajout]

## Cesse d'être valide quand
Le modèle décrit l’ambiguïté sans dire d’où vient la capacité ; la calibrer demande davantage d’observations qu’une probabilité. [ajout]

---
id: dup/famille-hara
nom: Famille HARA
type: abstraite
statut: source
cas_de: dup/courbure-de-l-utilite
parametre: la forme donnée à la courbure
construite_a_partir_de: []
alias:
- HARA
- hyperbolic absolute risk aversion
refs:
- L1 slide 35
---

## Ce que c'est
La famille d’utilités dont l’aversion absolue est une fonction hyperbolique de la richesse. [L1 slide 35]

## Forme
$$u(z)=\zeta\Big(\eta+\dfrac{z}{\gamma}\Big)^{1-\gamma}\ \implies\ A(z)=\Big(\eta+\dfrac{z}{\gamma}\Big)^{-1}$$ [L1 slide 35]

## Ce que les membres partagent
Toutes les utilités classiques du cours en relèvent, et leur $A$ s’obtient en fixant $\eta$ et $\gamma$. Choisir une utilité, dans ce cours, c’est choisir un point de cette famille. [L1 slide 35]

## Pourquoi ce niveau existe
Quatre utilités que le cours énumère sur une seule slide, avec leur $A$ en regard, et dont il dit explicitement qu’elles appartiennent toutes à la même famille. Les traiter séparément ferait manquer que le choix porte sur deux paramètres, pas sur quatre objets. [L1 slide 35]

## Exemple minimal
Avec $\eta=0$ et $\gamma=4$ : $A(z)=4/z$, soit $0{,}04$ à une richesse de 100. [ajout]

## Geste de calcul type
Fixer $\eta$ et $\gamma$, puis lire $A(z)=(\eta+z/\gamma)^{-1}$ : $\eta=0$ donne CRRA, $\gamma\to\infty$ donne CARA. [L1 slide 35]

## Cesse d'être valide quand
La forme hyperbolique est une commodité analytique, pas un résultat : rien n’oblige une préférence à y appartenir. [ajout]

---
id: dup/cpt
nom: Théorie cumulative des perspectives
type: notion
statut: source
cas_de: dup/ponderation-des-probabilites
valeur: la pondération par rang, appliquée séparément aux gains et aux pertes
construite_a_partir_de:
- dup/rdu
- dup/theorie-des-perspectives
alias:
- CPT
- cumulative prospect theory
- Tversky et Kahneman 1992
refs:
- L3 slide 38
---

## Ce que c'est
La théorie des perspectives refaite avec la pondération par rang, appliquée de part et d’autre du point de référence. [L3 slide 38]

## Forme
$$\varphi(p)=\dfrac{p^\beta}{\big(p^\beta+(1-p)^\beta\big)^{1/\beta}},\qquad \beta\in(0,1)$$ [L3 slide 38]

## Ce qui la définit
La loterie est décomposée en gains et en pertes, et la formule dépendante du rang est appliquée séparément aux probabilités cumulées de chaque côté. [L3 slide 38]

La forme concave puis convexe surpondère à la fois les mauvais résultats peu probables — l’effet de certitude — et les bons résultats peu probables — l’effet de possibilité. [L3 slide 38]

## Le chemin jusqu'ici
Deux fils se rejoignent. dup/cadrage donne dup/theorie-des-perspectives — le point de référence, les gains et les pertes ; dup/utilite-esperee donne dup/rdu — la pondération par rang. [ajout]

CPT est littéralement leur composition : la théorie des perspectives refaite avec la pondération par rang, appliquée séparément aux gains et aux pertes. Elle ne peut donc exister qu'après les deux, et c'est ce qui en fait l'aboutissement de cette branche du cours. [ajout]

## Exemple minimal
Avec $\beta=0{,}7$ et $p=0{,}2$ : $\varphi(0{,}2)=0{,}2560$, soit une surpondération de plus d’un quart. [L3 slide 46]

## Geste de calcul type
Séparer gains et pertes, cumuler de part et d’autre du point de référence, appliquer $\varphi$ à chaque cumul, puis assembler. [L3 slide 38]

## Cesse d'être valide quand
La forme paramétrique est un ajustement empirique, pas un résultat : $\beta$ se calibre, il ne se déduit pas. [ajout]

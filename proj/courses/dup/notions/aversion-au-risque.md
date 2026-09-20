---
id: dup/aversion-au-risque
nom: Aversion au risque
type: notion
statut: source
cas_de: dup/courbure-de-l-utilite
valeur: la concavité, prise globalement
construite_a_partir_de:
- dup/utilite-esperee
alias:
- risk aversion
refs:
- L1 slide 7
- L1 slide 8
- L1 slide 10
---

## Ce que c'est
Préférer la moyenne certaine d’un pari au pari lui-même. [L1 slide 7]

## Forme
$$U(\mathbb{E}[\tilde x])\ \ge\ \mathbb{E}[U(\tilde x)]$$ [L1 slide 7]

## Ce qui la définit
Par l’inégalité de Jensen, l’aversion vaut pour tout pari si et seulement si $U$ est concave ; la concavité stricte donne une préférence stricte pour tout pari non dégénéré. [L1 slide 7]

## Exemple minimal
Avec $u(x)=\sqrt{x}$ et le pari $(0,\tfrac12;100,\tfrac12)$ : la moyenne certaine vaut $u(50)=7{,}07$ contre $5$ pour le pari. [ajout]

## Geste de calcul type
Comparer $U(\mathbb{E}\tilde x)$ et $\mathbb{E}U(\tilde x)$ ; si l’on ne veut pas calculer, le signe de $U''$ décide seul. [ajout]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| forme de $U$ | concave | $U(\mathbb{E}\tilde x)\ge\mathbb{E}U(\tilde x)$ : averse |
| forme de $U$ | linéaire | $U(\mathbb{E}\tilde x)=\mathbb{E}U(\tilde x)$ : neutre |
| forme de $U$ | convexe | $U(\mathbb{E}\tilde x)\le\mathbb{E}U(\tilde x)$ : amateur |
[L1 slide 10]

## Cesse d'être valide quand
Ces trois catégories comparent un pari à sa moyenne certaine ; elles ne classent pas deux distributions risquées l’une par rapport à l’autre. [L1 slide 10]

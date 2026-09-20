---
id: dup/prime-de-risque
nom: Prime de risque
symbole: $\pi$
type: notion
statut: source
construite_a_partir_de:
- dup/equivalent-certain
alias:
- risk premium
refs:
- L1 slide 9
- L1 slide 31
---

## Ce que c'est
Ce que l’agent accepte d’abandonner sur la moyenne pour se débarrasser du risque. [L1 slide 9]

## Forme
$$\pi(\tilde x)=\mathbb{E}[\tilde x]-c,\qquad \mathbb{E}u(w_0+X)=u(w_0-\pi)$$ [L1 slide 9, L1 slide 31]

## Ce qui la définit
Sous aversion au risque, $c\le\mathbb{E}[\tilde x]$ et donc $\pi\ge0$ ; plus d’aversion implique une prime plus grande. [L1 slide 9, L1 slide 31]

## Le chemin jusqu'ici
Le socle commun mène à dup/equivalent-certain. [ajout]

La prime de risque en est la simple différence à la moyenne. Elle n'ajoute aucun concept — mais elle change l'unité de mesure : on passe d'un montant équivalent à un **coût**, ce qui la rend comparable d'une loterie à l'autre et ouvre tout le chapitre des approximations. [ajout]

## Exemple minimal
Avec $u(x)=\sqrt{x}$ et le pari $(0,\tfrac12;100,\tfrac12)$ : $\pi=50-25=25$. [ajout]

## Geste de calcul type
Calculer l’équivalent certain, le retrancher de la moyenne. Pour un petit risque, l’approximation d’Arrow-Pratt évite l’inversion : $\pi\approx\tfrac12\mathrm{Var}(X)A(w_0)$. [L1 slide 9, L1 slide 32]

## Cesse d'être valide quand
Écrite sur un risque de moyenne nulle ajouté à une richesse initiale, elle dépend de $w_0$ autant que du risque. [L1 slide 31]

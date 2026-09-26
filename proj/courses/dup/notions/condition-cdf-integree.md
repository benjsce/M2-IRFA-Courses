---
id: dup/condition-cdf-integree
nom: Condition sur la répartition intégrée
type: notion
statut: source
cas_de: dup/accroissement-de-risque
valeur: la comparaison analytique des répartitions intégrées
construite_a_partir_de:
- dup/loterie
alias:
- integrated-CDF condition
refs:
- L1 slide 22
---

## Ce que c'est
Le critère analytique de l’accroissement de risque : l’aire sous la fonction de répartition de $F^*$ domine celle de $F$ en tout point. [L1 slide 22]

## Forme
$$\int_0^x\big[F^*(t)-F(t)\big]\,dt\ \ge\ 0\quad\forall x\in[0,M],\qquad\text{avec égalité en }x=M$$ [L1 slide 22]

## Ce qui la définit
C’est la seule des formulations équivalentes qui survive à une suite quelconque d’étalements, quel que soit le nombre de croisements des répartitions. [L1 slide 22]

## Le chemin jusqu'ici
Tout part de dup/loterie, et de rien d'autre. [ajout]

Le critère est purement analytique : il compare des aires sous des fonctions de répartition. Aucune utilité, aucun agent n'intervient — et c'est tout l'intérêt, puisqu'on cherche précisément un critère sur lequel tous les agents averses s'accorderont. [ajout]

## Exemple minimal
Pour $\tilde x$ uniforme sur $\{40,60\}$ et $\tilde y$ uniforme sur $\{20,40,60,80\}$, sur $[0,80]$ : l’intégrale est positive avant 80 et nulle en 80. [ajout]

## Geste de calcul type
Tracer les deux répartitions, intégrer la différence de gauche à droite, vérifier que l’intégrale reste positive et s’annule au bout. C’est la seule méthode qui survive à plusieurs croisements. [L1 slide 22]

![Le geste sur l'exemple. À gauche, la répartition $F$ de $\tilde x$ et la répartition $F^*$ de $\tilde y$ se croisent. À droite, l'intégrale de $F^*-F$ depuis 0 monte à 5 entre 20 et 40, reste à 5 jusqu'à 60, puis redescend et s'annule en 80 : positive avant, nulle au bout.](figures/condition-cdf-integree.svg) [ajout]

## Cesse d'être valide quand
Énoncée sur un support borné $[0,M]$, avec égalité au bout : c’est cette égalité qui encode l’égalité des moyennes. [L1 slide 22]

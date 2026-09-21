---
id: dup/portefeuille-rdu
nom: Portefeuille optimal sous RDU
symbole: $q_s$
type: notion
statut: source
construite_a_partir_de:
- dup/rdu
alias:
- RDU optimal portfolio
- pi-SPP
refs:
- L3 slide 42
- L3 slide 44
- L3 slide 46
---

## Ce que c'est
Le programme de choix de portefeuille quand les états sont pondérés par leur rang et non par leur probabilité. [L3 slide 42]

## Forme
$$\max_{x_s}\sum_{s=1}^n\pi_su(x_s)\quad\text{s.c.}\quad\sum_s x_sq_s=w,\ \ x_s\le x_{s+1}$$ [L3 éq. 1]

## Ce que les symboles modélisent
$q_s$ est le prix, aujourd'hui, d'un titre qui paie une unité dans le seul état $s$ et rien ailleurs. C'est un prix de marché, le même pour tous les agents — à la différence du poids de décision, qui dépend de l'investisseur et de son portefeuille. [L3 slide 42]

## Ce qui la définit
La contrainte de monotonie $x_s\le x_{s+1}$ n’est pas décorative : elle vient de ce que les poids $\pi_s$ dépendent du rang, donc de la solution elle-même. [L3 slide 42]

La condition du premier ordre s’inverse en $x_s^*=u'^{-1}\big((\eta q_s+\kappa_s-\kappa_{s-1})/\pi_s\big)$, et sur les plages où la contrainte n’est pas active elle se réduit à $u'^{-1}(\eta q_s/\pi_s)$. [L3 éq. 3]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite se combinent en dup/utilite-esperee, dont dup/rdu déforme les probabilités cumulées. [ajout]

La fiche applique la pondération par rang à un problème de portefeuille. Elle dépend donc de RDU et non l'inverse : le critère d'abord, le programme d'optimisation ensuite. Ce qui change par rapport au cas classique, c'est que les états sont pondérés par leur rang, donc que la première condition d'ordre ne se lit plus comme une espérance. [ajout]

## Exemple minimal
Avec $q=(0{,}3;0{,}3;0{,}4)$ et $p=(0{,}2;0{,}3;0{,}5)$, le rapport prix sur probabilité vaut 1,5 puis 1 puis 0,8. [L3 slide 45]

## Geste de calcul type
Classer les états par prix rapporté au poids, en déduire l’ordre des $x_s$, puis vérifier que l’ordre obtenu est bien celui qui a servi à calculer les poids. [L3 slide 46, L3 slide 47]

## Cesse d'être valide quand
La vérification est indispensable : sur l’exemple du cours, l’allocation trouvée impose un ordre des états incompatible avec les poids dont elle est issue, et la solution n’en est donc pas une. [L3 slide 47]

---
id: pfo/vwap
nom: Prix moyen pondéré par les volumes
symbole: '$P_{\mathrm{VWAP}}$, $V_i$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- VWAP
- volume weighted average price
- prix d'exécution
refs:
- §1.1.2
- éq. 1.3
---

## Ce que c'est
Le prix moyen des exécutions d'une période, chacune pesant pour le volume échangé. [§1.1.2, éq. 1.3]

## Forme
$$P_{\mathrm{VWAP}} = \dfrac{\sum_{i=1}^{M} P_i \times V_i}{\sum_{i=1}^{M} V_i}$$ [éq. 1.3]

## Ce que les symboles modélisent
$V_i$ est le nombre de titres échangés lors de la $i$-ème exécution de la période, $P_i$ son prix, et $M$ le nombre d'exécutions de la période ; c'est $V_i$ qui fait qu'une grosse transaction pèse plus qu'une petite. [éq. 1.3, ajout]

$P_{\mathrm{VWAP}}$ est un prix, pas un volume : le montant total échangé divisé par le nombre total de titres, c'est-à-dire le prix moyen payé par titre. [ajout]

## Ce qui la définit
**Connu** : le prix et le volume de chaque exécution de la période. **Cherché** : ce qu'un titre a coûté en moyenne. Chaque prix doit donc peser pour le nombre de titres qu'il a servis. [ajout]

Les bases de données quotidiennes, comme Yahoo Finance, fournissent un prix de clôture. Pour de gros volumes, les gérants de portefeuille lui préfèrent le VWAP, qui pondère chaque prix d'exécution par le volume échangé sur la période. [§1.1.2]

## Exemple minimal
300 titres échangés à 100 et 100 titres échangés à 101 font un VWAP de 100,25. [ajout]

![Les deux exécutions de l'exemple, chacune avec son volume. Le VWAP, 100,25, tombe près de la grosse exécution ; la moyenne simple des deux prix, 100,50, tombe au milieu, comme si les deux pesaient autant.](figures/vwap.svg) [ajout]

## Geste de calcul type
Le montant total échangé, divisé par le nombre total de titres : $(100 \times 300 + 101 \times 100)/400 = 40\,100/400 = 100{,}25$. La moyenne simple des deux prix, 100,50, surpondère la petite exécution. [ajout]

## Cesse d'être valide quand
Il ne dit rien de la dispersion des prix autour de lui, et il dépend de la période retenue : le VWAP d'une séance n'est pas celui de sa dernière heure. [ajout]

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
$V_i$ est le nombre de titres échangés lors de la $i$-ème exécution de la période, et $P_i$ son prix ; c'est $V_i$ qui fait qu'une grosse transaction pèse plus qu'une petite au même prix. [éq. 1.3]

$P_{\mathrm{VWAP}}$ est un prix, pas un volume : c'est le prix moyen qu'aurait payé celui qui aurait participé à chaque exécution de la période au prorata de sa taille. [ajout]

## Ce qui la définit
Les bases de données quotidiennes, comme Yahoo Finance, fournissent un prix de clôture. Pour de gros volumes, les gérants de portefeuille lui préfèrent le VWAP, qui pondère chaque prix d'exécution par le volume échangé sur la période. [§1.1.2]

## Exemple minimal
300 titres échangés à 100 et 100 titres échangés à 101 font un VWAP de 100,25. [ajout]

## Geste de calcul type
Multiplier chaque prix par son volume, sommer, diviser par le volume total : $(100 \times 300 + 101 \times 100)/400 = 40\,100/400 = 100{,}25$. La moyenne simple des deux prix, 100,50, surpondère la petite exécution. [ajout]

## Cesse d'être valide quand
Il ne dit rien de la dispersion des prix autour de lui, et il dépend de la période retenue : le VWAP d'une séance n'est pas celui de sa dernière heure. [ajout]

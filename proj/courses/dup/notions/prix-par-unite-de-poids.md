---
id: dup/prix-par-unite-de-poids
nom: Prix par unité de poids de décision
symbole: $q_s/\pi_s$
type: notion
statut: source
construite_a_partir_de:
- dup/poids-de-decision
- dup/portefeuille-rdu
alias:
- price per unit of decision weight
refs:
- L4 slide 28
---

## Ce que c'est
Le prix d'un état rapporté à son poids de décision, qui remplace le rapport du prix à la probabilité dès que les poids dépendent du rang. [L4 slide 28]

## Forme
$$u'(x_s)=\eta\,\frac{q_s}{\pi_s},\qquad x_s=(u')^{-1}\!\left(\eta\,\frac{q_s}{\pi_s}\right)$$ [L4 slide 28]

## Ce que les symboles modélisent
$q_s/\pi_s$ rapporte un prix de marché à un poids propre à l'agent : ce que coûte un paiement dans l'état $s$, divisé par l'importance que cet état a pour lui. Plus il est bas, meilleur marché est cet état pour cet investisseur-là — ce n'est donc pas une grandeur de marché, malgré son numérateur. [L4 slide 28]

## Ce qui la définit
Sous utilité espérée, le rapport qui commande l'allocation est $q_s/p_s$, le prix par unité de probabilité. Sous utilité dépendante du rang, la probabilité objective n'entre plus dans la condition du premier ordre : c'est $q_s/\pi_s$ qui la remplace, et le rang du paiement décide donc de ce qu'un état coûte. [L4 slide 28]

Un rapport plus bas rend le paiement de cet état meilleur marché par unité de poids, et l'investisseur y porte davantage de richesse. Les deux termes n'ont pourtant pas le même statut : $q_s$ est un prix de marché, le même pour tous, tandis que $\pi_s$ dépend de l'investisseur et de son portefeuille. Surpondérer un état augmente l'attrait de son paiement, à multiplicateur et à ordre fixés ; le budget, lui, couple tous les états. [L4 slide 28]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite se combinent en dup/utilite-esperee, que dup/rdu généralise en déformant les probabilités cumulées, et dup/poids-de-decision nomme le poids qui en résulte. [ajout]

dup/portefeuille-rdu apporte l'autre moitié : un budget, des prix d'état et une condition du premier ordre. Cette fiche est le rapport entre les deux — le prix vient du programme, le poids vient du rang —, et elle n'a de sens qu'une fois les deux écrits, puisqu'elle dit exactement ce que la pondération par rang change au critère d'arbitrage classique. [ajout]

## Exemple minimal
Sur le marché du cours, $q=(0{,}3;0{,}3;0{,}4)$ et $\pi=(0{,}2560;0{,}2013;0{,}5426)$ donnent $q_s/\pi_s=(1{,}17;1{,}49;0{,}74)$, là où $q_s/p_s$ valait $(1{,}5;1;0{,}8)$. [L4 slide 29, L4 slide 30]

## Geste de calcul type
Diviser chaque prix d'état par le poids de décision de son rang, classer les états par ce rapport croissant, et lire l'ordre des richesses que ce classement impose. [L4 slide 28]

## Cesse d'être valide quand
Le rapport n'est pas donné avant la solution : $\pi_s$ dépend du rang, donc de l'allocation cherchée. Sur l'exemple du cours, les deux rapports ne classent même pas les états dans le même ordre, et l'ordre supposé au départ se trouve renversé par la solution qu'il produit. [L4 slide 30]

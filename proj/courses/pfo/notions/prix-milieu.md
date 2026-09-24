---
id: pfo/prix-milieu
nom: Prix milieu
symbole: '$P_t^{\mathrm{mid}}$'
type: notion
statut: source
construite_a_partir_de:
- pfo/fourchette-bid-ask
alias:
- mid-price
- mid price
- prix moyen de la fourchette
refs:
- §1.1.1
- éq. 1.2
---

## Ce que c'est
La moyenne du meilleur prix acheteur et du meilleur prix vendeur, retenue comme prix unique quand un modèle en demande un. [§1.1.1, éq. 1.2]

## Forme
$$P_t^{\mathrm{mid}} = \dfrac{P_t^{\mathrm{ask}} + P_t^{\mathrm{bid}}}{2}$$ [éq. 1.2]

## Ce que les symboles modélisent
$P_t^{\mathrm{mid}}$ n'est le prix d'aucune transaction : personne ne peut acheter ni vendre au milieu de la fourchette. C'est une convention de modélisation, qui résume deux prix réels en un prix fictif placé à égale distance des deux. [ajout]

## Ce qui la définit
Le cours l'introduit pour les besoins de la modélisation : un modèle manipule un prix, le marché en affiche deux, et le prix milieu est le choix fréquent pour passer de l'un à l'autre. [§1.1.1]

## Le chemin jusqu'ici
pfo/fourchette-bid-ask fournit les deux prix affichés, le bid et l'ask, dont le prix milieu est la moyenne. [ajout]

Le prix milieu est ce qui reste de la fourchette quand on renonce à son écart : il garde le centre et jette la largeur, c'est-à-dire l'information sur l'illiquidité. [ajout]

## Exemple minimal
Avec 99,90 à l'achat et 100,10 à la vente, le prix milieu vaut 100,00. [ajout]

## Geste de calcul type
Pour chaque date, additionner les deux colonnes du carnet et diviser par deux : $(99{,}90 + 100{,}10)/2 = 100{,}00$. [ajout]

## Cesse d'être valide quand
Il cesse d'être un prix atteignable dès que la fourchette est large : sur un titre illiquide, acheter coûte l'ask et non le milieu, et un modèle calé sur le prix milieu sous-estime le coût de chaque transaction. [ajout]

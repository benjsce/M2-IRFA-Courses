---
id: pfo/fourchette-bid-ask
nom: Fourchette acheteur-vendeur
symbole: '$P_t^{\mathrm{bid}}$, $P_t^{\mathrm{ask}}$, $S_t$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- bid-ask spread
- fourchette bid-ask
- spread
- prix bid
- prix ask
refs:
- §1.1
- §1.1.1
- éq. 1.1
---

## Ce que c'est
L'écart, à un instant donné, entre le prix le plus bas auquel un vendeur accepte de céder l'actif et le prix le plus haut qu'un acheteur accepte de payer. [§1.1.1, éq. 1.1]

## Forme
$$S_t = P_t^{\mathrm{ask}} - P_t^{\mathrm{bid}}, \qquad P_t^{\mathrm{ask}} > P_t^{\mathrm{bid}}$$ [éq. 1.1, §1.1.1]

## Ce que les symboles modélisent
$P_t^{\mathrm{bid}}$ est le meilleur prix que les acheteurs affichent : si vous vendez tout de suite, c'est ce que vous touchez. $P_t^{\mathrm{ask}}$ est le meilleur prix que les vendeurs affichent : si vous achetez tout de suite, c'est ce que vous payez. Aucun des deux n'est « le prix » de l'actif : un prix unique n'existe pas sur un marché professionnel. [§1.1, §1.1.1, ajout]

![Le carnet affiche deux prix : l'ask, 100,10, en haut, et le bid, 99,90, en bas. Qui achète tout de suite paie l'ask ; qui vend tout de suite touche le bid ; la fourchette $S_t$, 0,20, est l'écart entre les deux.](figures/fourchette-bid-ask.svg) [ajout]

$S_t$ est un écart de prix, de quelques centimes sur une action liquide, et non un prix. Il n'a rien à voir avec le prix comptant que le même symbole désigne dans le cours fpp. [ajout]

## Ce qui la définit
À chaque instant, le marché présente deux flux de prix, et l'ask est toujours au-dessus du bid. La fourchette est leur différence, et le cours la lit comme un indicateur direct de l'illiquidité du marché. [§1.1.1]

Elle se lit aussi comme un coût : acheter à l'ask et revendre aussitôt au bid fait perdre exactement la fourchette. Plus elle est large, plus il coûte cher de traiter immédiatement. [ajout]

## Exemple minimal
Une action affichée avec un bid à 99,90 et un ask à 100,10 se vend tout de suite à 99,90 et s'achète tout de suite à 100,10 : sa fourchette vaut 0,20. [ajout]

## Geste de calcul type
Chiffrer un aller-retour immédiat : acheter à l'ask, 100,10, et revendre au bid, 99,90, coûte 0,20 par titre, soit 0,2 % du prix. [ajout]

## Cesse d'être valide quand
La fourchette affichée ne vaut que pour la quantité disponible au meilleur prix ; un ordre plus gros traverse plusieurs niveaux du carnet et paie davantage. [ajout]

Pour les gros volumes, le cours juge l'exécution au prix moyen pondéré par les volumes plutôt qu'à un prix affiché. [§1.1.2]

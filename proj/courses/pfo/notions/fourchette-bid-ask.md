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
$P_t^{\mathrm{bid}}$ est le meilleur prix d'achat affiché : c'est ce que l'on encaisse si l'on veut vendre tout de suite. $P_t^{\mathrm{ask}}$ est le meilleur prix de vente affiché : c'est ce que l'on paie si l'on veut acheter tout de suite. Aucun des deux n'est « le prix » de l'actif, et le cours insiste sur ce point : un prix unique n'existe pas sur un marché professionnel. [§1.1, §1.1.1]

$S_t$ est un écart de prix, de quelques centimes sur une action liquide, et non un prix. Il n'a rien à voir avec le prix comptant que le même symbole désigne dans le cours fpp. [ajout]

## Ce qui la définit
À chaque instant, le marché présente deux flux de prix, et l'ask est toujours au-dessus du bid. La fourchette est leur différence, et le cours la lit comme un indicateur direct de l'illiquidité du marché. [§1.1.1]

Elle se lit aussi comme un coût : acheter au prix vendeur et revendre aussitôt au prix acheteur fait perdre exactement la fourchette. Plus elle est large, plus il coûte cher de traiter immédiatement. [ajout]

## Exemple minimal
Une action affichée à 99,90 à l'achat et à 100,10 à la vente a une fourchette de 0,20. [ajout]

## Geste de calcul type
Chiffrer un aller-retour immédiat : acheter à 100,10 et revendre à 99,90 coûte 0,20 par titre, soit 0,2 % du prix. [ajout]

## Cesse d'être valide quand
La fourchette affichée ne vaut que pour la quantité disponible au meilleur prix ; un ordre plus gros traverse plusieurs niveaux du carnet et paie davantage. [ajout]

Pour les gros volumes, le cours juge l'exécution au prix moyen pondéré par les volumes plutôt qu'à un prix affiché. [§1.1.2]

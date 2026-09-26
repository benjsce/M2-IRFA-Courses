---
id: fpp/couverture
nom: Couverture
type: principe
statut: source
construite_a_partir_de: []
alias:
- hedging
- se couvrir
refs:
- §8
- §7.1
- exo. 18
---

## Ce que c'est
Tenir, face à un produit, une position dans un autre instrument choisie pour que leurs variations s'annulent, si bien que l'ensemble ne porte plus de risque. [§7.1, §8]

## Ce qui la définit
Le poly l'emploie au chapitre 7 : un portefeuille fait d'une option et de $\delta$ actions ne porte plus de risque entre $t$ et $t+dt$ quand $\delta$ est bien choisi, et il doit alors rapporter le taux sans risque. C'est de là qu'il tire l'équation du prix des options. [§7.1]

Le chapitre 8 en fait son titre : les sensibilités du prix aux paramètres, les grecques, disent combien de chaque instrument il faut tenir pour neutraliser chaque risque. [§8]

Le livre d'exercices oppose deux couvertures d'une entreprise qui attend des dollars : la vente à terme, qui supprime tout risque et tout gain possible, et l'achat d'un put, qui ne retire que le risque de baisse. [exo. 18]

![Le vendeur d'un call de strike 100, à un an, tient 0,618 action. Sa perte sur le call et son gain sur les actions se compensent autour de 100 : la somme reste presque plate tant que l'action bouge peu.](figures/couverture.svg) [ajout]

## Cesse d'être valide quand
La compensation n'est exacte que pour de petits mouvements : quand l'action s'écarte, la position doit être ajustée, et entre deux ajustements il reste un risque. [§7.1, §8.2, ajout]

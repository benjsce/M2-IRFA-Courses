---
id: fpp/replication
nom: Réplication
type: abstraite
statut: ajout
cas_de: fpp/absence-arbitrage
parametre: le rééquilibrage
construite_a_partir_de: []
refs:
- §3.1
- §4.2.2
---

## Ce que c'est
Trouver le prix d'un flux futur en le reconstruisant avec des actifs dont on connaît le prix : le flux coûte ce que coûte la reconstruction. [ajout]

## Ce que les membres partagent
**Connu** : le prix aujourd'hui des briques, l'action et le zéro-coupon. **Cherché** : le prix d'un flux futur. On assemble les briques pour qu'elles paient exactement ce flux, dans tous les états du monde ; deux flux identiques ayant le même prix, le flux coûte ce que coûtent les briques. [§3.1, §4.2.2]

## Pourquoi ce niveau existe
Le cours change deux fois de montage, pour deux raisons distinctes : une fois parce que le refinancement n'est plus connu d'avance (les futures), une fois parce que le payoff n'est plus linéaire (les options). Les deux fois, il faut retoucher le montage en route ; ce niveau montre que la méthode, elle, ne change pas. [§4.2.2, ajout]

## Cesse d'être valide quand
rien dans le périmètre du cours [ajout]

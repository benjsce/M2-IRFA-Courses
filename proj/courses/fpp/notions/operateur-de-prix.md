---
id: fpp/operateur-de-prix
nom: Opérateur de prix
type: abstraite
statut: ajout
cas_de: fpp/absence-arbitrage
parametre: la nature des flux
construite_a_partir_de: []
refs:
- §5.1
---

## Ce que c'est
L’application qui associe un prix d’aujourd’hui à un flux futur. [ajout]

## Ce que les membres partagent
Linéarité et positivité, toutes deux imposées par l’absence d’arbitrage : un flux positif a un prix positif, et le prix d’une somme est la somme des prix. [ajout]

## Pourquoi ce niveau existe
Le cours ne fait jamais le rapprochement, et c’est dommage : la NPV est le cas dégénéré du prix risque-neutre, celui où $\mathbb{E}^{\mathbb{Q}}$ n’a rien à moyenner. Un seul opérateur, deux régimes. [ajout]

## Cesse d'être valide quand
rien dans le périmètre du cours [ajout]

---
id: dss/apprentissage-par-renforcement
nom: Apprentissage par renforcement
type: notion
statut: source
cas_de: dss/apprentissage-automatique
valeur: une récompense, après action sur l'environnement
construite_a_partir_de: []
alias:
- reinforcement learning
- RL
refs:
- slide 7
- slide 9
---

## Ce que c'est
L'agent agit sur un environnement et n'apprend que d'une récompense, en cherchant à maximiser un cumul. [slide 7]

## Ce qui la définit
La boucle a quatre termes : l'agent choisit une action, l'environnement renvoie un état et une récompense, un interprète les traduit, l'état interne se met à jour. [slide 9]

Trois paramètres pilotent cet état interne : le taux d'apprentissage, la température inverse et le taux d'actualisation. Le cours les nomme sans les définir. [slide 9]

## Cesse d'être valide quand
Le cours s'arrête au schéma. Aucune méthode de renforcement n'est enseignée ensuite. [ajout]

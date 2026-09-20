---
id: fpp/contrat-prime-nulle
nom: Contrat à prime nulle
type: abstraite
statut: ajout
cas_de: fpp/contrat-derive
valeur: aucun flux à la signature
parametre: la nature du sous-jacent échangé
construite_a_partir_de:
- fpp/valeur-actuelle-nette
refs:
- §2.3
- §3.1
---

## Ce que c'est
Un échange qui ne coûte rien à la signature : forward, future, FRA, swap. [ajout]

## Ce que les membres partagent
La valeur du contrat est nulle en $t$, donc l’inconnue est le strike et non le prix : $0=\Pi_t(S_T-K)$ donne $K=\mathbb{E}^{\mathbb{Q}}[S_T]$. [ajout]

## Pourquoi ce niveau existe
Le seul contenu réel de ce niveau est le déplacement de l’inconnue. Tout le reste est hérité du dessus ou instancié en dessous. [ajout]

## Le chemin jusqu'ici
La chaîne est courte et droite : fpp/convention-capitalisation, fpp/facteur-actualisation, fpp/valeur-actuelle-nette. [ajout]

Un contrat à prime nulle est un échéancier dont la valeur actuelle nette est nulle à la signature. Il fallait donc savoir sommer des flux datés avant de pouvoir dire « cet échange ne coûte rien » — sinon la phrase n'a pas de sens. [ajout]

## Cesse d'être valide quand
Ne dit rien tant qu’on n’a pas dit ce qu’on échange ni comment on règle. [ajout]

## Origine
- exercice fpp/ex-11 : le strike qui annule la prime **est** le prix forward. Un forward est un call-put à strike bien choisi ; c'est la définition, lue depuis la parité [exo. 11]

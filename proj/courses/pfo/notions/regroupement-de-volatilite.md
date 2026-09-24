---
id: pfo/regroupement-de-volatilite
nom: Regroupement de volatilité
type: notion
statut: source
cas_de: pfo/fait-stylise
valeur: la constance de la volatilité dans le temps
construite_a_partir_de:
- fpp/volatilite
alias:
- volatility clustering
- grappes de volatilité
- clusters de volatilité
refs:
- §1.4
- §2.1.1
---

## Ce que c'est
Le fait que la volatilité des rendements n'est pas constante mais alterne des épisodes de forte et de faible agitation. [§1.4, §2.1.1]

## Ce qui la définit
La volatilité des rendements présente des grappes de forte et de faible instabilité au lieu de rester à un niveau fixe, et elle se propage par épisodes. Le cours le range parmi les faits stylisés de Mandelbrot et Fama, et en fait la raison d'être de l'estimateur EWMA. [§1.4, §2.1.1]

## Le chemin jusqu'ici
fpp/volatilite définit l'écart type du rendement comme un paramètre unique, fixe sur toute la période. Le regroupement de volatilité est le constat que ce paramètre bouge : il faudrait parler d'une volatilité à chaque date, et non d'une volatilité de l'actif. [ajout]

## Cesse d'être valide quand
Le cours le constate sans le mesurer : aucune statistique du cours ne teste qu'une série présente des grappes, et l'estimateur EWMA le suppose au lieu de le vérifier. [ajout]

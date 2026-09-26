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
Une forte variation, à la hausse comme à la baisse, tend à être suivie d'autres fortes variations, et une journée calme d'autres journées calmes. [§1.4, ajout]

Le cours le range parmi les faits stylisés relevés par Mandelbrot et Fama. [§2.1.1]

## Le chemin jusqu'ici
fpp/volatilite définit l'écart type du rendement comme un paramètre unique, fixe sur toute la période. Le regroupement de volatilité est le constat que ce paramètre bouge : il faudrait parler d'une volatilité à chaque date, et non d'une volatilité de l'actif. [ajout]

## Exemple minimal
Sur la série simulée de la figure, l'écart type de toute la période vaut 1 % par jour. Les 12 jours où le rendement sort de ± 2 écarts types tombent tous dans l'épisode agité, qui ne couvre qu'un jour sur cinq ; dans les épisodes calmes, ce même 1 % surestime la dispersion. [ajout]

![250 jours de rendements simulés : un épisode calme, un épisode agité, puis un nouvel épisode calme. La bande pointillée est ± 2 fois l'écart type calculé sur toute la période, un seul nombre fixe ; les rendements qui en sortent, en couleur, sont tous groupés dans l'épisode agité.](figures/regroupement-de-volatilite.svg) [ajout]

## Cesse d'être valide quand
Le cours le constate sans le mesurer : aucune statistique du cours ne teste qu'une série présente des grappes. [ajout]

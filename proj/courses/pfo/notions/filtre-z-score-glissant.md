---
id: pfo/filtre-z-score-glissant
nom: Filtre par score z glissant
type: notion
statut: source
construite_a_partir_de:
- pfo/score-z
- pfo/rendement-logarithmique
alias:
- rolling z-score filter
- bad tick filter
- filtre des bad ticks
- bad ticks
refs:
- §1.3.2
- Listing 1.1
---

## Ce que c'est
Un filtre qui remplace par zéro tout rendement dont le score z, calculé sur une fenêtre glissante, dépasse 3 en valeur absolue. [§1.3.2, Listing 1.1]

## Forme
$$\left|\dfrac{r_t - \mu}{\sigma}\right| > 3 \;\Longrightarrow\; r_t \leftarrow 0, \qquad \mu,\ \sigma \text{ calculés sur les vingt derniers rendements}$$ [Listing 1.1]

## Ce qui la définit
Les flux de données réels contiennent des bad ticks, erreurs de saisie ou sauts de prix anormaux dus à des bugs d'interface logicielle. Le filtre les repère comme des rendements qui s'écartent de plus de trois écarts types de la moyenne locale. [§1.3.2]

Dans le pipeline du cours, la moyenne et l'écart type sont glissants sur vingt jours, l'écart est pris en valeur absolue pour détecter les deux sens, et le rendement repéré est remplacé par 0, ce qui revient à supposer que le prix n'a pas bougé ce jour-là. [Listing 1.1, p. 11]

## Le chemin jusqu'ici
Le filtre applique pfo/score-z non pas à une série quelconque mais aux rendements de pfo/rendement-logarithmique : un prix n'a pas de moyenne locale stable, un rendement si. [ajout]

Ce que la fiche ajoute au score z est le choix du groupe de référence : non pas toute la série, mais les vingt derniers jours, pour que la moyenne et l'écart type suivent les changements de régime. [ajout]

## Exemple minimal
Dans une fenêtre qui, rendement testé compris, a une moyenne nulle et un écart type de 1 %, un rendement de −4 % a un score de 4 en valeur absolue et est remplacé par 0. [ajout]

## Geste de calcul type
Compter les rendements filtrés avec `(z_scores > 3).sum().sum()` : le premier `sum()` compte les `True` de chaque colonne, le second additionne les colonnes. Sur une `Series`, un seul `sum()` suffit. [p. 13, p. 14]

## Cesse d'être valide quand
La fenêtre de pandas contient le rendement testé lui-même : un saut isolé gonfle l'écart type qui sert à le juger. Sur une fenêtre de vingt rendements, le score d'une observation ne peut jamais dépasser $19/\sqrt{20} \approx 4{,}25$ ; un saut isolé reste détecté, mais deux sauts proches se masquent l'un l'autre. [ajout]

Les dix-neuf premiers rendements n'ont pas de fenêtre complète, donc pas de score, et ne sont jamais filtrés. [ajout]

Remplacer par zéro suppose que le mouvement était une erreur. Un vrai krach de plus de trois écarts types est effacé comme un bad tick, ce qui retire du jeu de données exactement les queues épaisses que le chapitre 2 veut mesurer. [ajout]

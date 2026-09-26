---
id: fpp/volatilite
nom: Volatilité
symbole: $\sigma$
type: notion
statut: source
construite_a_partir_de: []
alias:
- volatility
- écart type du rendement
refs:
- Déf. 2
- §1.3
- Rem. 1
---

## Ce que c'est
L'écart type du rendement d'un actif, qui mesure de combien ce rendement s'écarte d'ordinaire de sa moyenne. [Déf. 2]

## Forme
$$\sigma = \operatorname{stdev}(\text{rendement})$$ [Déf. 2, §1.3]

## Ce que les symboles modélisent
$\sigma$ mesure une amplitude, pas un sens : un actif très volatil peut monter ou baisser. C'est un écart type et non une variance, qui en est le carré. Comme les taux, elle s'exprime par an sauf mention contraire. [Déf. 2, Rem. 1]

Le poly l'écrit sur la prime, $\sigma_E = \operatorname{stdev}(\tilde\pi_E)$ ; quand le coût de la dette est connu d'avance, l'écart type de la prime et celui du rendement sont le même nombre. [§1.3, ajout]

## Ce qui la définit
On connaît une suite de rendements ; on cherche l'écart typique autour de leur moyenne. La volatilité le donne en un nombre, sans rien dire de la moyenne elle-même. [Déf. 2]

![Des rendements fictifs autour de leur moyenne : la plupart restent dans la bande de largeur σ de part et d'autre, la volatilité.](figures/volatilite.svg) [ajout]

## Exemple minimal
Des rendements annuels qui s'écartent d'ordinaire de 4 points de leur moyenne de 6 % : la volatilité vaut 4 %. [ajout]

## Geste de calcul type
Calculer l'écart type des rendements observés sur une période ; le porter à une autre durée, du jour à l'année par exemple, demande une hypothèse sur la façon dont les rendements s'enchaînent, celle de l'échelonnement de la variance. [Déf. 2, §5.3]

## Cesse d'être valide quand
Un seul $\sigma$ ne décrit l'actif que si ses rendements gardent la même loi d'une période à l'autre ; le poly le suppose. Quand la volatilité change dans le temps, il faut parler d'une volatilité à chaque date. [§1.3, §5.3]

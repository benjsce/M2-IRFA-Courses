---
id: pfo/p-valeur
nom: p-valeur
symbole: '$\alpha$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- p-value
- niveau de signification
- significance level
- seuil de signification
refs:
- éq. 2.15
- éq. 2.16
- éq. 2.17
- p. 26
- p. 29
---

## Ce que c'est
La probabilité, si l'hypothèse nulle est vraie, d'observer une statistique de test au moins aussi extrême que celle que donne l'échantillon. [p. 26, p. 28]

## Forme
$$p < \alpha = 0{,}05 \;\Longrightarrow\; H_0 \text{ est rejetée}, \qquad p \geq \alpha \;\Longrightarrow\; H_0 \text{ n'est pas rejetée}$$ [éq. 2.15, éq. 2.16, éq. 2.17, p. 29]

## Ce que les symboles modélisent
$\alpha$ est le niveau de signification du test, fixé par le cours à 5 % : c'est le seuil sous lequel une p-valeur conduit à rejeter l'hypothèse nulle. [éq. 2.15, éq. 2.16]

Il représente le risque, accepté à l'avance, de rejeter une hypothèse nulle qui est vraie. Ce n'est ni le paramètre de lissage de l'EWMA ni le seuil de la VaR, que le cours note de la même lettre. [ajout]

## Ce qui la définit
Une p-valeur inférieure au niveau choisi signifie que les données présentent des caractéristiques significativement différentes de celles qu'impose l'hypothèse nulle, qui est rejetée. Supérieure, elle signifie que les données n'apportent pas assez de preuves pour la rejeter. [p. 25, p. 29]

Ne pas rejeter n'est pas prouver : la formulation correcte est « on ne rejette pas l'hypothèse de normalité », jamais « les données sont normales ». [p. 29]

## Exemple minimal
Au niveau de 5 %, une p-valeur de 0,03 conduit à rejeter l'hypothèse nulle, une p-valeur de 0,40 ne le permet pas. [ajout]

## Geste de calcul type
Comparer la p-valeur au niveau, jamais la statistique brute : `if p_value < 0.05:` on rejette, sinon on ne rejette pas. [Listing 2.1, p. 27]

## Cesse d'être valide quand
Au niveau de 5 %, un test appliqué à vingt séries réellement normales en rejettera une en moyenne : multiplier les tests multiplie les rejets à tort. [ajout]

Sur de très longues séries, la moindre déviation devient significative : une p-valeur minuscule dit que l'écart existe, pas qu'il est grand. [ajout]

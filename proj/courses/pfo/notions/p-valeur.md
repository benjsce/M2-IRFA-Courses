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
$$p = P\big(\text{statistique au moins aussi extrême que celle observée} \mid H_0\big), \qquad p < \alpha = 0{,}05 \;\Longrightarrow\; H_0 \text{ est rejetée}$$ [p. 26, p. 28, éq. 2.15, éq. 2.16, éq. 2.17]

## Ce que les symboles modélisent
$p$ est la p-valeur, une probabilité calculée sous $H_0$, l'hypothèse nulle que le test éprouve. « Au moins aussi extrême » dépend du test : au moins aussi grande pour Jarque-Bera, au moins aussi petite pour Shapiro-Wilk. [p. 26, p. 28]

$\alpha$ est le niveau de signification, fixé par le cours à 5 % : le risque, accepté à l'avance, de rejeter une hypothèse nulle qui est vraie. Ce n'est ni le paramètre de lissage de l'EWMA ni le seuil de la VaR, que le cours note de la même lettre. [éq. 2.15, ajout]

## Ce qui la définit
**On connaît** la statistique calculée sur l'échantillon, et la loi qu'elle suivrait si $H_0$ était vraie. **On cherche** la probabilité de tomber au moins aussi loin : c'est l'aire de la queue de cette loi au-delà de la valeur observée. [ajout]

![La loi dessinée est celle du test de Jarque-Bera sous l'hypothèse nulle, $\chi^2(2)$, choisie pour l'illustration. L'aire colorée est la p-valeur, au-delà de la statistique observée ; l'aire grise est $\alpha=0{,}05$, au-delà du seuil 5,99. À gauche, statistique 1,83 : l'aire p = 0,40 contient l'aire α, on ne rejette pas. À droite, la queue grossie, statistique 7,01 : l'aire p = 0,03 tient dans l'aire α, on rejette.](figures/p-valeur.svg) [ajout]

Comparer $p$ à $\alpha$ revient donc à regarder si la statistique observée dépasse le seuil : $\alpha$ est l'aire au-delà du seuil, $p$ l'aire au-delà de l'observée, et la seconde est la plus petite exactement quand l'observée est plus loin que le seuil. [ajout]

Une p-valeur inférieure au niveau signifie que les données présentent des caractéristiques significativement différentes de celles qu'impose l'hypothèse nulle, qui est rejetée. Supérieure, elle signifie que les données n'apportent pas assez de preuves pour la rejeter. [p. 25, p. 29]

Ne pas rejeter n'est pas prouver : la formulation correcte est « on ne rejette pas l'hypothèse de normalité », jamais « les données sont normales ». [p. 29]

## Exemple minimal
Au niveau de 5 %, une p-valeur de 0,03 conduit à rejeter l'hypothèse nulle, une p-valeur de 0,40 ne le permet pas. [ajout]

## Geste de calcul type
Comparer la p-valeur au niveau, jamais la statistique brute : `if p_value < 0.05:` on rejette, sinon on ne rejette pas. [Listing 2.1, p. 27]

## Cesse d'être valide quand
Au niveau de 5 %, un test appliqué à vingt séries réellement normales en rejettera une en moyenne : multiplier les tests multiplie les rejets à tort. [ajout]

Sur de très longues séries, la moindre déviation devient significative : une p-valeur minuscule dit que l'écart existe, pas qu'il est grand. [ajout]

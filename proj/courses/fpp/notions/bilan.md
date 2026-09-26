---
id: fpp/bilan
nom: Bilan
type: notion
statut: source
construite_a_partir_de: []
alias:
- balance sheet
- double entry
refs:
- §1.2
- Prop. 1
---

## Ce que c'est
La photographie comptable d’une entité à une date : d’un côté ce qu’elle possède, l’actif ; de l’autre qui l’a financée, les actionnaires et les créanciers. [§1.2, ajout]

## Forme
$$A_t=E_t+D_t$$ [Prop. 1]

## Ce que les symboles modélisent
$A_t$, $E_t$ et $D_t$ sont trois montants pris à la même date, et non des taux. $A_t$ est l'actif, ce que l'entité possède. $E_t$ est la part de son financement apportée par les actionnaires, les capitaux propres : elle leur appartient. $D_t$ est la part apportée par les créanciers, la dette : elle leur est due. L'indice rappelle qu'ils bougent : un bilan est un instantané. [§1.3, ajout]

## Ce qui la définit
Toute transaction s’enregistre par au moins deux écritures, ce qui force l’égalité à tout instant : l’actif égale le passif, c’est-à-dire les capitaux propres plus la dette. C'est une identité comptable, vraie par construction et non par hypothèse économique. [§1.2, Prop. 1, §1.3]

![Le bilan de l'exemple. À gauche, ce que l'entité possède : un actif de 100. À droite, qui l'a financée : 30 de capitaux propres, qui appartiennent aux actionnaires, et 70 de dette, due aux créanciers. Les deux colonnes ont toujours la même hauteur.](figures/bilan.svg) [ajout]

## Exemple minimal
Un actif de 100 financé par 30 de capitaux propres et 70 de dette. [ajout]

## Geste de calcul type
L’identité tient aussi en variations : $\Delta A_t=\Delta E_t+\Delta D_t$. Si l’actif perd 10 et que la dette ne bouge pas, $-10=\Delta E_t+0$ : les capitaux propres perdent 10, de 30 à 20, et le bilan devient $90=20+70$. [§1.3, ajout]

## Cesse d'être valide quand
Jamais : c’est une identité comptable. Elle dit que les trois termes restent liés, pas comment chacun est évalué. [Prop. 1, ajout]

## Origine
- exercice fpp/ex-16 : l'identité force le payoff des créanciers à être le complément de celui des actionnaires [exo. 16]

---
id: fpp/bilan
nom: Bilan
symbole: '$A_t$, $E_t$, $D_t$'
type: principe
statut: source
construite_a_partir_de: []
alias:
- actif égale passif
- balance sheet
- comptabilité en partie double
- double-entry accounting
- loi fondamentale de la comptabilité
refs:
- Prop. 1
- §1.2
- §1.3
---

## Ce que c'est
À tout instant, l'actif d'un bilan égale son passif, c'est-à-dire les capitaux propres plus la dette. [Prop. 1, §1.2]

## Forme
$$A_t = E_t + D_t$$ [Prop. 1, §1.3]

## Ce que les symboles modélisent
$A_t$ est la valeur des actifs, ce que l'entreprise possède ; $D_t$ celle de sa dette, ce qu'elle doit à ses créanciers ; $E_t$ celle de ses capitaux propres (equity), ce qui revient aux actionnaires. Ce sont des stocks, mesurés à une date, et non des flux. [§1.3]

## Ce qui la définit
En comptabilité en partie double, chaque transaction s'enregistre par au moins deux écritures, si bien que l'égalité tient à chaque instant. [§1.2]

On connaît les actifs et la dette ; les capitaux propres sont **ce qui reste** : $E_t = A_t - D_t$. C'est pourquoi l'égalité vaut aussi pour les variations, $\Delta A_t = \Delta E_t + \Delta D_t$ : si la dette ne bouge pas, tout gain ou toute perte des actifs tombe sur les capitaux propres. [§1.3]

Le livre d'exercices l'appelle la loi fondamentale de la comptabilité et s'en sert pour valoriser la dette d'une entreprise une fois connue la valeur de ses capitaux propres. [exo. 16]

![Le bilan de l'entreprise du cours : 100 d'actifs à gauche, financés à droite par 20 de capitaux propres et 80 de dette.](figures/bilan.svg) [§1.2, ajout]

## Exemple minimal
Des actifs de 100, une dette de 80 : les capitaux propres valent 20. [ajout]

## Geste de calcul type
Des actifs et de la dette, déduire les capitaux propres par différence ; après un choc sur les actifs, dette inchangée, reporter le choc tel quel sur les capitaux propres : des actifs qui passent de 100 à 110 portent les capitaux propres de 20 à 30. [§1.3, ajout]

## Cesse d'être valide quand
L'égalité tient toujours. Ce qui change sous responsabilité limitée, c'est quel poste du passif absorbe une perte qui dépasse les capitaux propres : ceux-ci s'arrêtent à 0, et la dette encaisse le reste. [§1.4]

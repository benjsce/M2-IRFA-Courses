---
id: dss/compromis-biais-variance
nom: Compromis biais-variance
type: notion
statut: source
construite_a_partir_de:
- dss/erreur-de-test
alias:
- bias-variance trade-off
refs:
- slide 53
- slide 54
- slide 55
---

## Ce que c'est
Accepter du biais pour réduire la variance, quand la somme des deux diminue. [slide 53]

## Ce qui la définit
Les estimateurs des moindres carrés ont un biais faible mais peuvent être très variables, en particulier quand $n$ et $p$ sont du même ordre. Contraindre les coefficients les rend biaisés et réduit fortement leur variance. [slide 53]

L'erreur quadratique moyenne étant la somme du carré du biais et de la variance, il existe un réglage où l'échange est favorable — et c'est le seul argument qui justifie de dégrader volontairement l'ajustement. [slide 54]


## Le chemin jusqu'ici
dss/apprentissage-supervise, puis dss/erreur-de-test : il faut une erreur hors échantillon avant de pouvoir la décomposer. [ajout]

Le compromis n'a de sens que mesuré sur des données non vues. Sur les données d'apprentissage, la variance ne coûte rien et seul le biais se voit. [ajout]

## Exemple minimal
Quand le paramètre de pénalité augmente, le biais monte, la variance descend, et l'erreur quadratique moyenne passe par un minimum avant de remonter. [slide 54]

![Les deux erreurs varient en sens contraire, et c'est leur somme qui décide. La source ne chiffre ni l'une ni l'autre : la figure ne porte donc aucune graduation, seulement les formes et l'endroit où la somme est minimale.](figures/compromis-biais-variance.svg) [ajout]

## Cesse d'être valide quand
L'échange n'est favorable que si les moindres carrés sont effectivement très variables. Quand $n\gg p$, il n'y a presque rien à gagner. [slide 55]

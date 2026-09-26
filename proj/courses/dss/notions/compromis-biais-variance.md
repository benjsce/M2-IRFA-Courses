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
Accepter du biais pour réduire la variance, quand la somme du biais au carré et de la variance diminue. [slide 53]

## Ce qui la définit
Les estimateurs des moindres carrés ont un biais faible mais peuvent être très variables, en particulier quand $n$ et $p$ sont du même ordre. Contraindre les coefficients les rend biaisés et réduit fortement leur variance. [slide 53]

L'erreur quadratique moyenne d'un estimateur est la somme du carré de son biais et de sa variance ; l'erreur de test y ajoute une erreur irréductible, celle du bruit, que rien ne réduit. Il existe donc un réglage où l'échange est favorable — et c'est le seul argument qui justifie de dégrader volontairement l'ajustement. [slide 54, ajout]

Quand la contrainte sur les coefficients se resserre, le biais monte, la variance descend, et l'erreur quadratique moyenne passe par un minimum avant de remonter. [slide 54]

![Les deux erreurs varient en sens contraire, et c'est leur somme qui décide. La source ne chiffre ni l'une ni l'autre : la figure ne porte donc aucune graduation, seulement les formes et l'endroit où la somme est minimale.](figures/compromis-biais-variance.svg) [ajout]


## Le chemin jusqu'ici
dss/erreur-de-test fournit l'erreur hors échantillon qu'on décompose, et dss/apprentissage-supervise les exemples sur lesquels on ajuste. Le compromis n'a de sens que mesuré sur des données non vues : sur les données d'apprentissage, la variance ne coûte rien et seul le biais se voit. [ajout]

## Exemple minimal
Sur les 20 clients, les moindres carrés sur les cinq prédicteurs donnent aux trois variables sans lien avec la perte des coefficients de 0,37, −0,25 et −0,38, quand leur vrai coefficient est nul : sur 20 autres clients, ils seraient tout autres. C'est cette variance qu'une contrainte réduirait, au prix de tirer aussi vers zéro les coefficients de l'endettement et du revenu. [ajout]

## Cesse d'être valide quand
L'échange n'est favorable que si les moindres carrés sont effectivement très variables. Quand $n\gg p$, il n'y a presque rien à gagner. [slide 55]

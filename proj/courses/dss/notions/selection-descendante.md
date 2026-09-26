---
id: dss/selection-descendante
nom: Sélection descendante
type: notion
statut: source
cas_de: dss/selection-pas-a-pas
valeur: du modèle complet vers le modèle nul
construite_a_partir_de:
- dss/moindres-carres-ordinaires
alias:
- backward stepwise selection
refs:
- slide 33
- slide 35
- slide 36
---

## Ce que c'est
Partir du modèle contenant tous les prédicteurs et retirer à chaque pas le moins utile, celui dont le retrait fait le moins monter la RSS. [slide 33, slide 35]

## Ce qui la définit
Elle commence par ajuster le modèle complet, ce qui suppose $n>p$ : avec moins d'observations que de prédicteurs, les moindres carrés n'ont pas de solution unique. C'est la seule différence de fond avec le sens ascendant, qui s'en passe, et elle est décisive. [slide 36, ajout]

Le cours donne deux façons de s'arrêter : quand plus aucun retrait n'améliore le modèle, ou au bout du chemin, en choisissant par validation croisée, $C_p$, BIC ou $R^2$ ajusté parmi les modèles $\mathcal{M}_p,\dots,\mathcal{M}_0$ atteints à chaque pas. L'exemple suit la seconde. [slide 33, slide 35]


## Le chemin jusqu'ici
Le point de départ est un ajustement de dss/moindres-carres-ordinaires sur tous les prédicteurs à la fois, avec tous les exemples de dss/apprentissage-supervise ; chaque pas réajuste ensuite autant de modèles qu'il reste de variables. [ajout]

## Exemple minimal
Sur les 20 clients, elle retire tour à tour les trois variables sans lien avec la perte et retombe sur l'endettement et le revenu, que le $C_p$ retient ; là où la sélection ascendante s'est trompée, elle trouve le bon modèle. [ajout]

## Geste de calcul type
Comparer $n$ et $p$ avant de la lancer : avec $n=50$ observations et $p=80$ prédicteurs, elle ne peut pas démarrer, et il faut passer au sens ascendant. [slide 36, ajout]

## Cesse d'être valide quand
Exige $n>p$. [slide 36]

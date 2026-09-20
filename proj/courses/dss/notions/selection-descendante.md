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
Partir du modèle contenant tous les prédicteurs et retirer à chaque pas celui dont le retrait améliore le plus le modèle. [slide 33]

## Ce qui la définit
Elle commence par un ajustement complet, ce qui suppose que cet ajustement existe. C'est la seule différence de fond avec le sens ascendant, et elle est décisive. [slide 33, slide 36]


## Le chemin jusqu'ici
Même point de départ que le sens ascendant : dss/apprentissage-supervise, puis dss/moindres-carres-ordinaires. [ajout]

La dépendance est ici plus contraignante qu'elle n'en a l'air, car la procédure commence par ajuster le modèle complet — et il faut donc que cet ajustement existe. [ajout]

## Exemple minimal
Avec $n=50$ observations et $p=80$ prédicteurs, elle ne peut pas démarrer : le modèle complet n'a pas de solution unique. [ajout]

## Geste de calcul type
Vérifier $n>p$ avant de la lancer ; si l'inégalité ne tient pas, il faut passer au sens ascendant. [slide 36]

## Cesse d'être valide quand
Exige $n>p$, là où la sélection ascendante s'en passe. [slide 36]

---
id: dss/selection-ascendante
nom: Sélection ascendante
type: notion
statut: source
cas_de: dss/selection-pas-a-pas
valeur: du modèle nul vers le modèle complet
construite_a_partir_de:
- dss/moindres-carres-ordinaires
alias:
- forward stepwise selection
refs:
- slide 33
- slide 34
- slide 36
---

## Ce que c'est
Partir du modèle sans prédicteur et ajouter à chaque pas celui qui améliore le plus le modèle. [slide 33]

## Ce qui la définit
On s'arrête quand plus aucune addition n'améliore. Le chemin est déterminé par le point de départ : une variable écartée tôt peut ne jamais revenir, même si elle serait utile en présence d'une autre. [slide 33]


## Le chemin jusqu'ici
dss/apprentissage-supervise, puis dss/moindres-carres-ordinaires : chaque pas ajuste un modèle de plus. [ajout]

Ce qui distingue cette fiche dans sa famille tient à son abstraction et non à ses dépendances : le sens du parcours ne se construit sur rien, il se choisit. [ajout]

## Exemple minimal
Sur les 20 clients, elle fait entrer d'abord une variable sans lien avec la perte, la meilleure seule par hasard, puis une seconde, et n'atteint l'endettement qu'au quatrième pas ; le $C_p$ retient alors un modèle à quatre prédicteurs dont deux inutiles, d'erreur de test 1,77 contre 1,16. [ajout]

## Geste de calcul type
La préférer dès que $n<p$ : c'est le seul des deux sens qui reste calculable, puisqu'on n'a jamais besoin d'ajuster le modèle complet. [slide 36]

Avec $p=20$, elle ajuste 211 modèles là où le parcours exhaustif en demanderait plus d'un million. [ajout]

## Cesse d'être valide quand
Rien dans la procédure ne garantit d'atteindre le meilleur sous-ensemble ; elle atteint un optimum local du chemin. [slide 36]

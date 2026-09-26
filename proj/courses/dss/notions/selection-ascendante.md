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
Partir du modèle sans prédicteur et ajouter à chaque pas celui qui fait le plus baisser la RSS. [slide 33, slide 34]

## Ce qui la définit
Le cours donne deux façons de s'arrêter : quand plus aucune addition n'améliore le modèle, ou au bout du chemin. Dans la seconde, on va jusqu'au modèle complet, en appelant $\mathcal{M}_k$ le modèle atteint au $k$-ième pas, puis on choisit parmi $\mathcal{M}_0,\dots,\mathcal{M}_p$ par validation croisée, $C_p$, BIC ou $R^2$ ajusté ; c'est elle que suit l'exemple. [slide 33, slide 34]

Une variable entrée n'en ressort jamais, même quand celles qui suivent la rendent inutile : le chemin dépend de ses premiers pas. [slide 33, ajout]


## Le chemin jusqu'ici
Chaque pas ajuste par dss/moindres-carres-ordinaires un modèle par variable candidate, sur les exemples de dss/apprentissage-supervise, et garde celui dont la RSS est la plus basse. Rien d'autre n'est nécessaire : ce qui distingue ce sens de l'autre n'est pas un ingrédient, c'est le point de départ. [ajout]

## Exemple minimal
Sur les 20 clients, elle fait entrer d'abord une variable sans lien avec la perte, la meilleure seule par hasard, puis une seconde, puis le revenu, et l'endettement seulement au quatrième pas ; le $C_p$ retient alors ce modèle à quatre prédicteurs dont deux inutiles, d'erreur de test 1,77 contre 1,16 pour l'endettement et le revenu seuls. [ajout]

## Geste de calcul type
La préférer dès que $n<p$ : elle reste calculable, puisqu'elle n'a jamais besoin d'ajuster le modèle complet. [slide 36]

Avec $p=20$, elle ajuste 211 modèles là où le parcours exhaustif en demanderait plus d'un million. [ajout]

## Cesse d'être valide quand
Rien dans la procédure ne garantit d'atteindre le meilleur sous-ensemble ; elle atteint un optimum local du chemin. [slide 36]

---
id: dss/meilleur-sous-ensemble
nom: Meilleur sous-ensemble
type: notion
statut: source
cas_de: dss/selection-de-sous-ensemble
valeur: tous les sous-ensembles, exhaustivement
construite_a_partir_de:
- dss/critere-penalise
alias:
- best subset selection
refs:
- slide 29
- slide 30
- slide 31
---

## Ce que c'est
Ajuster une régression par moindres carrés pour chaque combinaison possible des prédicteurs, puis choisir. [slide 29]

## Ce qui la définit
La procédure est en trois temps. Le modèle nul $\mathcal{M}_0$ ne contient aucun prédicteur et prédit la moyenne. Pour chaque taille $k$, on ajuste les $\binom{p}{k}$ modèles et on retient celui de plus petite RSS, appelé $\mathcal{M}_k$. Puis on choisit parmi $\mathcal{M}_0,\dots,\mathcal{M}_p$ par $C_p$, BIC, $R^2$ ajusté ou erreur de validation croisée. [slide 29]

Le deuxième temps se fait sur la RSS parce qu'à taille fixée la comparaison est licite. Le troisième ne le peut pas, puisque la RSS décroît toujours avec la taille : il y faut un critère qui pénalise la taille ou une validation croisée, sans quoi on retiendrait toujours le modèle complet. [slide 30, slide 37]


## Le chemin jusqu'ici
Chacun des modèles essayés s'ajuste par dss/moindres-carres-ordinaires sur les exemples de dss/apprentissage-supervise, et sa RSS suffit à le comparer aux autres modèles de même taille. Pour trancher entre tailles, il faut viser dss/erreur-de-test, que dss/critere-penalise permet d'estimer sans données nouvelles. [ajout]

## Exemple minimal
Les 20 clients ont cinq prédicteurs : l'endettement $x_1$, le revenu $x_2$, et trois variables sans lien avec la perte, $x_3$, $x_4$, $x_5$. Il faut ajuster 32 modèles. Le meilleur à un prédicteur est, par hasard, $x_3$ ; le meilleur à deux est le bon, l'endettement et le revenu. Le $C_p$ choisit alors $\mathcal{M}_2$ : 1,40, le plus bas de $\mathcal{M}_0,\dots,\mathcal{M}_5$, contre 1,79 pour $\mathcal{M}_1$ et 1,68 pour le modèle complet. [ajout]

![Les 32 modèles des 20 clients, chacun à sa taille et à sa RSS d'apprentissage ; la ligne relie le plus bas de chaque taille. Le meilleur à un prédicteur est $x_3$, sans lien avec la perte, le meilleur à deux l'endettement $x_1$ et le revenu $x_2$, et la ligne descend toujours : la RSS ne départage pas des tailles différentes.](figures/meilleur-sous-ensemble.svg) [ajout]

## Geste de calcul type
Pour chaque taille, garder le modèle de plus petite RSS, le plus bas de sa colonne sur la figure ; puis calculer le $C_p$ de ces seuls modèles et retenir le plus petit. [slide 29, slide 40]

## Cesse d'être valide quand
Devient infaisable au-delà d'une quarantaine de prédicteurs. Et plus l'espace de recherche est grand, plus la chance de trouver un modèle qui a l'air bon sans pouvoir prédictif augmente. [slide 31, slide 32]

Avec $p=10$, il faut déjà ajuster 1 024 modèles ; avec $p=40$, plus de mille milliards. [ajout]

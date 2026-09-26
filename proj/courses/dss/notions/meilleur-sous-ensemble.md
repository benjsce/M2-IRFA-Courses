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

Le deuxième temps se fait sur la RSS parce qu'à taille fixée la comparaison est licite ; le troisième ne le peut pas, puisque la RSS décroît toujours avec la taille. [slide 30]


## Le chemin jusqu'ici
dss/apprentissage-supervise et dss/moindres-carres-ordinaires donnent l'ajustement ; dss/erreur-de-test et dss/critere-penalise donnent de quoi choisir entre les modèles obtenus. [ajout]

Les deux sont nécessaires, pour des raisons différentes : à taille fixée la RSS suffit à comparer, entre tailles différentes il faut une pénalité. La procédure fait les deux comparaisons l'une après l'autre, et les confondre reviendrait à toujours retenir le modèle complet. [ajout]

## Exemple minimal
Avec les cinq prédicteurs des 20 clients, il faut ajuster 32 modèles. Le meilleur à un prédicteur est, par hasard, une variable sans lien avec la perte ; le meilleur à deux est le bon, l'endettement et le revenu. [ajout]

![Les 32 modèles des 20 clients, chacun à sa taille et à sa RSS d'apprentissage ; la ligne relie le plus bas de chaque taille. Le meilleur à un prédicteur est une variable sans lien avec la perte, le meilleur à deux l'endettement et le revenu, et la ligne descend toujours : la RSS ne départage pas des tailles différentes.](figures/meilleur-sous-ensemble.svg) [ajout]

## Geste de calcul type
Séparer les deux comparaisons : à taille fixée la RSS suffit, entre tailles différentes il faut un critère qui pénalise. Confondre les deux revient à toujours retenir le modèle complet. [slide 30, slide 37]

## Cesse d'être valide quand
Devient infaisable au-delà d'une quarantaine de prédicteurs. Et plus l'espace de recherche est grand, plus la chance de trouver un modèle qui a l'air bon sans pouvoir prédictif augmente. [slide 31, slide 32]

Avec $p=10$, il faut déjà ajuster 1 024 modèles ; avec $p=40$, plus de mille milliards. [ajout]

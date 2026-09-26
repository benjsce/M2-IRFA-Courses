---
id: pfo/modele-de-risque
nom: Modèle de risque
type: abstraite
statut: source
cas_de: pfo/marches-non-gaussiens
parametre: la loi supposée des rendements
construite_a_partir_de:
- pfo/valeur-a-risque-conditionnelle
alias:
- risk model
- méthode de calcul de la VaR
- trois modèles de risque
refs:
- p. 32
- Listing 2.2
---

## Ce que c'est
Une méthode qui calcule la VaR et la CVaR d'un portefeuille à partir de ses rendements, sous une hypothèse sur leur loi. [p. 32, Listing 2.2]

## Ce que les membres partagent
Tous partent des mêmes rendements, du même seuil de 5 % et du même capital, et rendent une VaR et une CVaR en montant, sur un horizon d'un jour ; le listing 2.2 les calcule côte à côte pour qu'on les compare. [Listing 2.2]

Ils diffèrent par ce qu'ils supposent de la loi des rendements : rien pour la méthode historique, qui lit les quantiles de l'échantillon ; la loi normale pour la méthode paramétrique ; la loi normale corrigée de l'asymétrie et de l'excès de kurtosis pour Cornish-Fisher. [p. 32, Listing 2.2]

## Pourquoi ce niveau existe
Le cours les nomme ensemble, « nos trois modèles de risque », et les implémente dans un seul listing. [p. 32, Listing 2.2]

La question qu'ils posent ensemble est celle du chapitre : combien la non-normalité des rendements change le risque mesuré. Séparés, ils ne montreraient plus que l'écart entre leurs chiffres est précisément l'effet des queues et de l'asymétrie. [ajout]

Un exemple le fait voir. Pour des rendements journaliers de moyenne 0,05 %, d'écart type 2 %, d'asymétrie −0,5 et d'excès de kurtosis 3, sur un capital de 1 000 000, la VaR à 95 % vaut 32 397 sous l'hypothèse normale et 33 935 avec la correction de Cornish-Fisher ; la CVaR, 40 754 et 53 511. Le seuil bouge à peine, la moyenne de la queue de près d'un tiers. [ajout]

## Le chemin jusqu'ici
pfo/valeur-a-risque-conditionnelle et, derrière elle, pfo/valeur-a-risque définissent ce que chaque modèle doit rendre ; le modèle ne dit que comment l'estimer. [ajout]

## Cesse d'être valide quand
Tous supposent que la loi estimée sur l'échantillon vaudra pour l'horizon qui vient : aucun ne suit un changement de régime de volatilité, ce que l'estimateur EWMA permettrait. [ajout]

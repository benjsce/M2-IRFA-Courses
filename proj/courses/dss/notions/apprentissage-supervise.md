---
id: dss/apprentissage-supervise
nom: Apprentissage supervisé
type: notion
statut: source
cas_de: dss/apprentissage-automatique
valeur: une sortie désirée pour chaque entrée
construite_a_partir_de: []
alias:
- supervised learning
refs:
- slide 7
- slide 235
---

## Ce que c'est
L'algorithme apprend sur des couples formés d'un objet d'entrée et de la sortie désirée, qu'on appelle aussi l'étiquette. [slide 7]

## Ce qui la définit
La sortie désirée est fournie avec chaque entrée : il existe donc une réponse contre laquelle mesurer l'écart de la prédiction, et c'est cet écart que l'apprentissage cherche à réduire. Le but est ensuite de prédire la sortie d'une entrée nouvelle, dont on ne connaît que l'entrée. [slide 7, ajout]

En régression, les composantes de l'entrée s'appellent les prédicteurs — on dit aussi variables explicatives, ou régresseurs — et la sortie désirée s'appelle la réponse. [ajout]

C'est le seul régime que le cours développe : régression linéaire, arbres, réseaux de neurones et les deux études de cas sont tous supervisés. [ajout]

## Exemple minimal
Une banque dispose des dossiers de 20 anciens clients en défaut : pour chacun, l'endettement, le revenu et trois autres renseignements forment l'entrée, et la perte subie, en milliers d'euros, est la sortie désirée. D'un nouveau client, elle ne connaîtra que l'entrée : c'est sa perte qu'elle cherche. [ajout]

## Cesse d'être valide quand
Il suppose que les étiquettes existent, et il apprend les régularités des données telles qu'elles sont, biais compris : le dernier article du cours conclut que l'apprentissage automatique laisse ainsi prospérer les biais sociaux, en reproduisant les motifs qu'il apprend. [slide 235, ajout]

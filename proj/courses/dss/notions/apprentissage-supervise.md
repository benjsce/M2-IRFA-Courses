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
---

## Ce que c'est
L'algorithme reçoit des couples formés d'un objet d'entrée et de la sortie désirée. [slide 7]

## Ce qui la définit
L'étiquette est fournie avec l'exemple : il existe donc une réponse contre laquelle mesurer l'écart, et c'est cet écart qui pilote l'apprentissage. [slide 7]

En régression, les composantes de l'objet d'entrée s'appellent les prédicteurs — on dit aussi variables explicatives, ou régresseurs — et la sortie désirée s'appelle la réponse. [ajout]

C'est le seul régime que le cours développe : régression linéaire, arbres, réseaux de neurones et les deux études de cas sont tous supervisés. [ajout]

## Exemple minimal
Une banque dispose des dossiers de 20 anciens clients en défaut : pour chacun, l'endettement et le revenu sont l'entrée, et la perte subie, en milliers d'euros, est la sortie désirée. [ajout]

## Cesse d'être valide quand
Il suppose que les étiquettes existent et qu'elles sont justes. Le cours revient longuement sur ce que coûte une étiquette biaisée. [slide 218]

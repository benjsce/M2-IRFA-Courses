---
id: dss/analyse-post-entrainement
nom: Analyse post-entraînement
type: notion
statut: source
construite_a_partir_de:
- dss/retropropagation
- dss/interpretabilite
alias:
- post-training analysis
refs:
- slide 194
- slide 195
- slide 196
- slide 197
---

## Ce que c'est
Ce qu'on peut lire d'un réseau une fois qu'il est entraîné. [slide 194]

## Ce qui la définit
Deux voies séparées par le cours : examiner le modèle lui-même, ou mesurer la sensibilité de la sortie aux attributs d'entrée. [slide 194]

Examiner le modèle veut dire afficher la réponse quand on fait varier une entrée choisie, ou analyser le réseau en détail. La lecture manuelle des poids est jugée difficile et les outils graphiques très utiles ; la conversion en équation ou en code exécutable est mentionnée, et la traduction automatique vers de la logique symbolique donnée comme un sujet de recherche actif. [slide 195, slide 196]

La sensibilité se mesure analytiquement — analyse factorielle, analyse des poids — ou par élimination d'attributs, vers l'avant ou vers l'arrière. On retrouve ici les deux sens de la sélection pas à pas. [slide 197]


## Le chemin jusqu'ici
Deux fils. Le premier va de dss/apprentissage-supervise et dss/apprentissage-inductif à dss/fonction-discriminante-lineaire, dss/reseau-de-neurones-artificiel, dss/perceptron, dss/limite-du-perceptron, dss/fonction-d-activation et dss/reseau-multicouche, puis par dss/regle-delta et dss/descente-de-gradient jusqu'à dss/retropropagation : le réseau entraîné. Le second est dss/interpretabilite : la raison de l'ouvrir. [ajout]

L'analyse vient nécessairement après l'entraînement, et elle répond à la question posée au tout début du cours — celle de l'effet des variables sur la réponse. [ajout]

## Cesse d'être valide quand
Le cours revient à son constat de départ : le réseau reste une boîte noire dont on ne voit pas comment elle décide. Ces analyses en donnent des vues, pas la règle. [slide 200]

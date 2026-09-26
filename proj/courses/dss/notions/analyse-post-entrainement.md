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

La sensibilité se mesure analytiquement — analyse factorielle, analyse des poids — ou par élimination d'attributs, vers l'avant ou vers l'arrière : retirer ou ajouter les attributs un à un, et mesurer ce que le réseau perd ou gagne. [slide 197, ajout]

## Le chemin jusqu'ici
La raison d'ouvrir le réseau vient de dss/interpretabilite : pouvoir lire, dans un modèle ajusté, l'effet des variables qui comptent. C'est la question de départ, quel est l'effet de chaque variable sur la réponse, que le réseau rend difficile. [ajout]

L'analyse vient nécessairement après dss/retropropagation, qui a fixé les poids : ce sont eux qu'on examine, ou dont on mesure la sensibilité aux entrées. Chaque poids résulte de pas de dss/descente-de-gradient, qui suivent la pente de l'erreur comme la dss/regle-delta pour un seul neurone. [ajout]

Si les poids se lisent mal, c'est qu'ils sont ceux d'un dss/reseau-multicouche. Sa couche cachée, imposée par la dss/limite-du-perceptron, et sa dss/fonction-d-activation non linéaire forment une représentation interne qu'aucune variable ne porte seule ; un dss/perceptron isolé, lui, se lirait directement : l'unité d'un dss/reseau-de-neurones-artificiel qui calcule une dss/fonction-discriminante-lineaire a un poids par attribut. [ajout]

Ce que le réseau a appris, il l'a appris sur des exemples, au sens de dss/apprentissage-inductif, étiquetés, au sens de dss/apprentissage-supervise ; c'est la réponse apprise sur eux qu'on fait varier. [ajout]

## Cesse d'être valide quand
Le réseau reste une boîte noire : le cours le range parmi ses défauts, on ne voit pas comment il décide. Ces analyses en donnent des vues, pas la règle. [slide 200]

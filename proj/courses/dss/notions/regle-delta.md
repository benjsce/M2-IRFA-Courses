---
id: dss/regle-delta
nom: Règle delta
symbole: $\eta$
type: notion
statut: source
construite_a_partir_de:
- dss/perceptron
alias:
- delta rule
- Widrow-Hoff
refs:
- slide 144
- slide 145
---

## Ce que c'est
Corriger chaque poids proportionnellement à l'erreur commise et à l'entrée qui l'a produite. [slide 145]

## Forme
$$w_i(t+1)=w_i(t)+\Delta w_i,\qquad \Delta w_i=\eta\,d\,x_i(t),\qquad d=t-y$$ [slide 145]

## Ce que les symboles modélisent
$\eta$ est le taux d'apprentissage : la fraction de la correction qu'on applique réellement. Trop petit, l'apprentissage traîne ; trop grand, il oscille sans se poser. Ce n'est pas un paramètre du modèle mais un paramètre de la marche vers le modèle. [slide 145]

## Ce qui la définit
L'algorithme du perceptron tient en quatre pas répétés : initialiser les poids, présenter un motif et sa sortie désirée, calculer la sortie, mettre à jour les poids. On recommence jusqu'à un niveau d'erreur acceptable. [slide 144]

Le signal d'erreur $d$ est la différence entre la sortie désirée et la sortie obtenue. Le poids d'une entrée nulle ne bouge pas : seule une entrée active est tenue pour responsable. [slide 145]

Le taux d'apprentissage $\eta$ vit dans $]0,1]$ et vaut typiquement 0,1. [slide 145]


## Le chemin jusqu'ici
Le socle est celui du perceptron : dss/apprentissage-supervise et dss/apprentissage-inductif, puis dss/reseau-de-neurones-artificiel et dss/fonction-discriminante-lineaire, réunis dans dss/perceptron. [ajout]

La règle ne s'applique à rien d'autre : elle corrige les poids d'un neurone dont on connaît la sortie désirée. C'est cette restriction qui rendra la couche cachée problématique. [ajout]

## Exemple minimal
Avec $\eta=0{,}1$, une sortie désirée de 1, une sortie obtenue de 0 et une entrée $x_i=1$, le poids augmente de 0,1. [ajout]

## Geste de calcul type
Vérifier le signe avant tout : si la sortie est trop basse, $d>0$ et les poids des entrées actives montent. Une erreur de signe fait diverger l'apprentissage sans autre symptôme. [ajout]

## Cesse d'être valide quand
Elle ne s'applique qu'à un neurone dont on connaît la sortie désirée. Pour un nœud caché, cette sortie n'existe pas — c'est précisément le problème que la rétropropagation résout. [slide 152]

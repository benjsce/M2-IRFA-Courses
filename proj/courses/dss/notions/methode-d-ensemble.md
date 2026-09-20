---
id: dss/methode-d-ensemble
nom: Méthode d'ensemble
type: principe
statut: source
construite_a_partir_de:
- dss/compromis-biais-variance
alias:
- ensemble methods
refs:
- slide 97
---

## Ce que c'est
Apprendre plusieurs arbres plutôt qu'un seul, en s'assurant qu'ils n'apprennent pas tous la même chose. [slide 97]

## Ce qui la définit
Le point de départ est un constat et une contrainte : un arbre de décision isolé prédit mal, mais il est très rapide à ajuster. On peut donc se permettre d'en construire beaucoup. [slide 97]

La question qui organise tout le chapitre est posée telle quelle par le cours : comment faire pour qu'ils n'apprennent pas tous la même chose. Chaque méthode de la famille y répond différemment. [slide 97]


## Le chemin jusqu'ici
dss/apprentissage-supervise, dss/erreur-de-test, puis dss/compromis-biais-variance. [ajout]

Le compromis justifie la famille entière : un arbre isolé a une variance forte, et moyenner plusieurs estimations réduit cette variance sans toucher au biais. [ajout]

## Cesse d'être valide quand
Le gain se paie en interprétabilité : un ensemble d'arbres n'est plus lisible comme un arbre unique l'était. [slide 104]

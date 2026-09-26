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

Il prédit mal notamment parce qu'il varie beaucoup : découper les données autrement donne un autre arbre. Moyenner plusieurs arbres qui diffèrent réduit cette variance. [slide 98]

La question qui organise tout le chapitre est posée telle quelle par le cours : comment faire pour qu'ils n'apprennent pas tous la même chose. Chaque méthode de la famille y répond différemment. [slide 97]


## Le chemin jusqu'ici
dss/compromis-biais-variance fournit la raison de construire plusieurs arbres : l'erreur que mesure dss/erreur-de-test contient la variance du modèle, et un arbre ajusté sur les couples observés de dss/apprentissage-supervise en a beaucoup. [ajout]

C'est l'argument de la moyenne. Construire les arbres en séquence, chacun corrigeant ce que les précédents n'expliquent pas, est l'autre façon de les combiner, et elle n'en relève pas. [ajout]

## Cesse d'être valide quand
Le gain se paie en interprétabilité : un ensemble d'arbres n'est plus lisible comme un arbre unique l'était. [slide 104]

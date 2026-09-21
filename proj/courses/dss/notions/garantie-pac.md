---
id: dss/garantie-pac
nom: Garantie probabiliste de généralisation
symbole: $W$, $\varepsilon$
type: notion
statut: source
construite_a_partir_de:
- dss/generalisation
alias:
- probabilistic guarantee
- PAC theory
refs:
- slide 168
- slide 169
- slide 170
---

## Ce que c'est
Une borne qui lie le nombre d'exemples d'apprentissage au nombre de poids du réseau et à la tolérance d'erreur. [slide 168]

## Forme
$$m>O\Big(\frac{W}{\varepsilon}\log_2\frac{N}{\varepsilon}\Big)\ \approx\ m>\frac{W}{\varepsilon}$$ [slide 168]

## Ce que les symboles modélisent
$W$ compte les poids du réseau, c'est-à-dire sa capacité à retenir. $\varepsilon$ est la tolérance qu'on s'accorde sur l'erreur. La borne lie les deux au nombre d'exemples nécessaires : plus on veut d'exactitude, ou plus le réseau est gros, plus il en faut. [slide 168]

## Ce qui la définit
Deux conditions, et le cours donne les deux : l'erreur sur le jeu d'apprentissage doit être inférieure à $\varepsilon/2$, et le nombre d'exemples doit dépasser la borne. On obtient alors la généralisation avec 95 % de confiance, pour une tolérance $\varepsilon<1/8$. [slide 168]

La forme approchée $m>W/\varepsilon$ est celle que le cours retient comme règle de pratique : il faut à peu près autant d'exemples que de poids, divisé par la tolérance. [slide 168]

Elle donne aussi le sens du compromis sur la taille du réseau : trop de poids exige trop d'exemples, trop peu ne laisse pas la liberté de construire la fonction voulue. Entre les deux, un nombre optimal de nœuds cachés. [slide 170]


## Le chemin jusqu'ici
Le socle est celui de la généralisation, la généralisation elle-même en plus : dss/apprentissage-supervise, dss/apprentissage-inductif, dss/erreur-de-test, dss/fonction-discriminante-lineaire, dss/reseau-de-neurones-artificiel, dss/perceptron, dss/limite-du-perceptron, dss/fonction-d-activation, dss/reseau-multicouche, puis dss/generalisation. [ajout]

La borne ne fait que chiffrer la question précédente : combien d'exemples pour que la généralisation ait lieu. Il fallait donc l'avoir posée qualitativement avant de pouvoir la borner. [ajout]

## Exemple minimal
Un réseau 20-20-1 a 441 poids ; pour $\varepsilon=0{,}1$, il faut $m>4\,410$ exemples, à comparer aux $2^{20}=1\,048\,576$ cas possibles. [slide 169]

## Geste de calcul type
Compter les poids du réseau, diviser par la tolérance visée : c'est l'ordre de grandeur du jeu d'apprentissage nécessaire. [slide 168, slide 169]

## Cesse d'être valide quand
C'est une borne de théorie PAC, donnée comme règle de pratique et non comme garantie : elle est en ordre de grandeur, et la confiance est de 95 %, pas de 100 %. [slide 168]

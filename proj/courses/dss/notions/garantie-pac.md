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
Une borne qui dit combien d'exemples il faut pour qu'un réseau de $W$ poids généralise avec une tolérance $\varepsilon$ : un peu plus de $W/\varepsilon$. [slide 168]

## Forme
$$m>O\Big(\frac{W}{\varepsilon}\log_2\frac{N}{\varepsilon}\Big)\ \approx\ m>\frac{W}{\varepsilon}$$ [slide 168]

## Ce que les symboles modélisent
$W$ compte les poids du réseau, c'est-à-dire sa capacité à retenir. $\varepsilon$ est la tolérance qu'on s'accorde sur l'erreur, inférieure à 1/8. [slide 168]

$m$ est le nombre d'exemples d'apprentissage, la quantité que la borne fixe. $N$ est le nombre de nœuds cachés ; il n'intervient que dans le logarithme, que la forme approchée abandonne. [slide 168]

## Ce qui la définit
**Connu** : le réseau, donc son nombre de poids $W$, et la tolérance qu'on se fixe, $\varepsilon$. **Cherché** : le nombre d'exemples $m$. La borne bouche le trou : un peu plus de $W/\varepsilon$, soit $1/\varepsilon$ exemples par poids, dix par poids pour une tolérance de 10 %. [slide 168]

![Le réseau de la banque, 5 entrées, 20 nœuds cachés, une sortie, compte 141 poids : une colonne chacun. La tolérance ε = 0,1 demande 10 exemples par colonne. Le nombre d'exemples cherché est l'aire du rectangle, 1 410 ; les 20 clients de la banque n'en remplissent que deux colonnes.](figures/garantie-pac.svg) [ajout]

La garantie tient à deux conditions, que le cours donne ensemble : l'erreur sur le jeu d'apprentissage doit être inférieure à $\varepsilon/2$, et le nombre d'exemples doit dépasser la borne. Le réseau généralise alors avec 95 % de confiance. [slide 168]

Lue dans l'autre sens, la même borne fixe le nombre de poids qu'on peut se permettre avec les exemples dont on dispose. [slide 170]

## Le chemin jusqu'ici
La borne chiffre la question que pose dss/generalisation : combien d'exemples pour que le réseau réponde juste hors de ceux qu'il a vus. Il fallait l'avoir posée qualitativement, avec la régularité observée sur la parité, avant de pouvoir la borner. [ajout]

L'erreur que borne $\varepsilon$ est une dss/erreur-de-test, commise sur des cas qui n'ont pas servi à l'apprentissage. [ajout]

Les poids comptés par $W$ sont ceux d'un dss/reseau-multicouche : ses nœuds cachés, que la dss/limite-du-perceptron a rendus nécessaires, et leur dss/fonction-d-activation, en font une machine qui peut apprendre par cœur. Chaque nœud reprend le dss/perceptron, unité d'un dss/reseau-de-neurones-artificiel qui calcule une dss/fonction-discriminante-lineaire. [ajout]

Les exemples comptés par $m$ sont ceux de dss/apprentissage-inductif, étiquetés de la réponse attendue comme le veut dss/apprentissage-supervise. [ajout]

## Exemple minimal
Sur la parité à 20 bits, qui a $2^{20}=1\,048\,576$ entrées possibles, un réseau 20-20-1 a 441 poids ; pour $\varepsilon=0{,}1$, il lui faut $m>4\,410$ exemples, bien moins que tous les cas. [slide 169]

## Geste de calcul type
Compter les poids, puis diviser par la tolérance. Pour le réseau de la banque, 5 entrées, 20 nœuds cachés et une sortie : $20\times(5+1)=120$ poids vers la couche cachée, $20+1=21$ vers la sortie, soit $W=141$ ; à 10 %, $141/0{,}1=1\,410$ exemples, contre 20 clients. [ajout]

## Cesse d'être valide quand
C'est une borne de théorie PAC, donnée comme règle de pratique et non comme garantie : elle est en ordre de grandeur, et la confiance est de 95 %, pas de 100 %. [slide 168]

---
id: dup/paradoxe-d-ellsberg
nom: Paradoxe d’Ellsberg
type: notion
statut: source
construite_a_partir_de:
- dup/principe-de-la-chose-sure
alias:
- Ellsberg paradox
- urne d'Ellsberg
refs:
- L1 slide 62
- L1 slide 63
- L4 slide 61
---

## Ce que c'est
Les choix courants sur l’urne à composition partiellement inconnue ne peuvent être rationalisés par aucune probabilité additive. [L1 slide 62]

## Forme
$$f_1\succ f_2\Rightarrow\pi(R)>\pi(B),\qquad f_4\succ f_3\Rightarrow\pi(B)+\pi(J)>\pi(R)+\pi(J)\Rightarrow\pi(B)>\pi(R)$$ [L1 slide 63]

## Ce que les symboles modélisent
$f_1$, $f_2$, $f_3$ et $f_4$ sont les quatre paris sur l'urne, chacun payant 100 sur certaines couleurs et rien sur les autres. $\pi$ est la probabilité subjective que l'agent aurait s'il en avait une, additive par hypothèse ; ce n'est pas une fréquence connue. [L1 slide 62, L1 slide 63]

$\pi(R)$, $\pi(B)$ et $\pi(J)$ sont ses valeurs sur le rouge, le noir et le jaune : $B$ désigne ici le noir, et non le bleu de la version du quatrième cours. [L1 slide 62, ajout]

## Ce qui la définit
Les deux implications se contredisent, et la colonne jaune — commune aux deux actes de chaque paire — s’annule dans les deux cas. C’est donc bien le principe de la chose sûre qui casse. [L1 slide 63]

Le quatrième cours reprend la même urne en appelant ses couleurs rouge, bleu et vert, et l’écrit comme une table de quatre actes à trois colonnes : le raisonnement est mot pour mot celui de la première présentation. [L4 slide 35, L4 slide 36]

Il en donne aussi une seconde version, à deux urnes. L’une a une composition rouge-bleu connue à parts égales, l’autre une composition inconnue ; chaque état décrit un tirage dans chacune. Les choix aversifs à l’ambiguïté y consistent à préférer parier sur l’urne connue, quelle que soit la couleur — préférence qui, comme la première, ne se représente par aucune probabilité unique. [L4 slide 61]

## Le chemin jusqu'ici
Le chemin passe par dup/acte et dup/fonction-utilite, qui se combinent en dup/utilite-esperee-subjective, laquelle repose à son tour sur dup/principe-de-la-chose-sure. [ajout]

Le paradoxe frappe le dernier maillon, et c'est pour cela qu'il faut les précédents : les choix courants sur l'urne à composition inconnue violent le principe de la chose sûre, donc aucune probabilité subjective ne peut les représenter. Ce n'est pas l'utilité qui est en cause, c'est la croyance. [ajout]

## Exemple minimal
Une urne de 30 boules rouges et 60 noires ou jaunes en proportion inconnue : la plupart préfèrent parier sur rouge, puis sur noir-ou-jaune. [L1 slide 62]

## Geste de calcul type
Écrire la table des quatre actes en trois colonnes, rayer la colonne commune à chaque paire, et lire les deux inégalités sur les probabilités. [L1 slide 63]

## Cesse d'être valide quand
Le paradoxe ne dit pas quelle réparation adopter : capacité non additive ou ensemble de probabilités sont deux réponses différentes, aux comportements comparés différents. [L1 slide 64]

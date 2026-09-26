---
id: dss/fonction-d-activation
nom: Fonction d'activation
type: notion
statut: source
construite_a_partir_de:
- dss/perceptron
alias:
- activation function
- transfer function
refs:
- slide 151
- slide 178
---

## Ce que c'est
La transformation appliquée au total pondéré pour produire la sortie d'un nœud. [slide 178]

## Ce qui la définit
Le passage du seuil à une fonction non linéaire dérivable est ce qui a rendu possible l'apprentissage multicouche : la sortie varie continûment mais pas linéairement, et l'on peut la dériver. [slide 151]

Il faut dériver pour savoir dans quel sens corriger. Avec le seuil, bouger un peu un poids ne change presque jamais la sortie : sa pente est nulle partout sauf au saut, et rien n'indique la direction. Avec la sigmoïde, chaque petite correction se voit à la sortie, en proportion de la pente. [ajout]

La sigmoïde est celle sur laquelle repose la rétropropagation du cours. Pour un total pondéré $a$, que la slide 156 note $x_j$, elle rend la sortie du nœud $o=1/(1+e^{-a})$ ; sa pente vaut $o(1-o)$, soit 0,25 en $a=0$, où $o=0{,}5$. Les autres fonctions sont listées comme des choix de conception. [slide 155, slide 156, slide 178, ajout]

![Le seuil du perceptron saute de 0 à 1 et n'a de pente nulle part ailleurs ; la sigmoïde passe continûment de 0 à 1 et se dérive partout, sa pente valant $o(1-o)$. C'est ce remplacement qui permet de dériver l'erreur.](figures/fonction-d-activation.svg) [ajout]

Au même endroit, le cours laisse libre la façon d'intégrer les entrées — sommées, sommées après élévation au carré, ou multipliées —, qui précède la fonction d'activation et ne se confond pas avec elle. [slide 178]

## Le chemin jusqu'ici
dss/perceptron fournit la pièce qu'on remplace : le seuil qui lit le signe de la somme pondérée, c'est-à-dire d'une dss/fonction-discriminante-lineaire. [ajout]

Le neurone de dss/reseau-de-neurones-artificiel apprend ses poids sur les exemples de dss/apprentissage-supervise, dans la famille d'hypothèses que dss/apprentissage-inductif demandait de fixer ; changer la fonction d'activation, c'est changer cette famille, et rendre dérivable ce qu'on apprend. [ajout]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| fonction d'activation | sigmoïde (logistique) | $1/(1+e^{-a})$, celle de la rétropropagation |
| fonction d'activation | tangente hyperbolique | sortie centrée sur zéro |
| fonction d'activation | gaussienne | réponse locale |
| fonction d'activation | linéaire | pas de non-linéarité |
| fonction d'activation | soft-max | sortie lue comme une distribution |
[slide 178]

## Cesse d'être valide quand
La rétropropagation telle que le cours l'écrit repose sur la sigmoïde : les formules de $d_j$ portent le facteur $o_j(1-o_j)$, qui est sa dérivée. [slide 155, slide 159]

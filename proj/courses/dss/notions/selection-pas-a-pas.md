---
id: dss/selection-pas-a-pas
nom: Sélection pas à pas
type: abstraite
statut: source
cas_de: dss/selection-de-sous-ensemble
valeur: un seul chemin glouton, une variable à la fois
parametre: le sens dans lequel le chemin est parcouru
construite_a_partir_de:
- dss/meilleur-sous-ensemble
alias:
- stepwise selection
refs:
- slide 32
- slide 33
- slide 36
---

## Ce que c'est
Parcourir un seul chemin dans l'espace des sous-ensembles, en ajoutant ou en retirant une variable à la fois. [slide 33]

## Ce que les membres partagent
Un chemin ne visite que $1+p(p+1)/2$ modèles : le modèle de départ, puis, à chaque pas, un modèle par variable encore candidate, $p$ au premier pas, $p-1$ au deuxième, et ainsi de suite jusqu'à un seul. Avec cinq prédicteurs, $1+5+4+3+2+1=16$. C'est ce qui rend la méthode utilisable là où le parcours exhaustif ne l'est plus. [slide 36, ajout]

La méthode est gloutonne : à chaque pas on prend le meilleur mouvement immédiat, et l'on ne revient jamais dessus. Dans un sens comme dans l'autre, rien ne garantit d'atteindre le meilleur sous-ensemble. [slide 33, slide 36]

Le cours mentionne une version hybride qui combine les deux sens, sans la détailler. [slide 36]

## Pourquoi ce niveau existe
Le cours pose les deux sens côte à côte, sur la même slide, dans deux colonnes symétriques dont seul le sens du parcours change. Les séparer ferait manquer que c'est une seule idée lue dans les deux sens. [slide 33]


## Le chemin jusqu'ici
Chaque pas ajuste par dss/moindres-carres-ordinaires quelques modèles sur les exemples de dss/apprentissage-supervise, et garde celui dont la RSS est la plus basse. Au bout du chemin, le choix de la taille revient, comme dans dss/meilleur-sous-ensemble, à une estimation de dss/erreur-de-test, par dss/critere-penalise ou par validation. [ajout]

La dépendance au parcours exhaustif est d'abord logique : la sélection pas à pas existe parce que celui-ci devient infaisable au-delà d'une quarantaine de prédicteurs. [ajout]

## Exemple minimal
Avec les cinq prédicteurs des 20 clients, chaque sens ajuste 16 modèles, là où le parcours exhaustif en ajuste 32. Et les deux sens n'aboutissent pas au même modèle : le sens ascendant garde deux variables sans lien avec la perte, le sens descendant retrouve l'endettement et le revenu. [ajout]

![Les deux chemins sur les 20 clients : $x_1$ l'endettement, $x_2$ le revenu, $x_3$ à $x_5$ sans lien avec la perte. En haut, la sélection ascendante ajoute à chaque pas la variable qui fait le plus baisser la RSS ; elle commence par $x_3$ et n'atteint l'endettement qu'au quatrième pas. En bas, la sélection descendante retire à chaque pas celle dont le retrait fait le moins monter la RSS. À deux prédicteurs, les deux chemins ne passent pas par le même modèle. Sous chaque modèle, son $C_p$ ; la case colorée est le plus petit du chemin, le modèle retenu.](figures/selection-pas-a-pas.svg) [ajout]

## Cesse d'être valide quand
L'espace parcouru étant réduit, le modèle retenu peut être strictement moins bon que le meilleur sous-ensemble de même taille. C'est le prix explicitement payé pour la faisabilité. [slide 36]

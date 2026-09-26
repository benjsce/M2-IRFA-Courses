---
id: dss/decroissance-des-poids
nom: Décroissance des poids
type: notion
statut: source
construite_a_partir_de:
- dss/retropropagation
- dss/regularisation
alias:
- weight decay
refs:
- slide 49
- slide 62
- slide 171
- slide 174
- slide 184
---

## Ce que c'est
Pénaliser la croissance des poids inutiles en ajoutant leur somme des carrés à la fonction d'erreur. [slide 174]

## Forme
$$E=\tfrac12\sum_j(t_j-o_j)^2+\frac{\lambda}{2}\sum_i w_{ij}^2\ \Longrightarrow\ \Delta w_{ij}=\Delta w_{ij}-\lambda w_{ij}$$ [slide 174]

## Ce que les symboles modélisent
$\lambda$ est le paramètre de coût des poids : le prix, en erreur, de chaque unité de poids au carré. Le cours emploie la même lettre pour le $\lambda$ de ridge et pour le rétrécissement du boosting, qui sont d'autres nombres. [slide 174, ajout]

$w_{ij}$ est le poids de la connexion du nœud $i$ vers le nœud $j$ : la pénalité porte sur les poids, pas sur les sorties. $t_j$ et $o_j$ gardent leur sens, sortie désirée et sortie produite du nœud $j$. $\Delta w_{ij}$ est la correction que la rétropropagation calculait déjà ; dans la mise à jour, le signe égal se lit comme une affectation, et le terme retranché ne dépend que du poids lui-même, pas de l'erreur. [slide 174, ajout]

## Ce qui la définit
C'est la pénalité de ridge, appliquée aux poids d'un réseau. Le cours fait le rapprochement lui-même, dans le chapitre sur ridge : pénaliser par la somme des carrés des paramètres est aussi employé en réseaux de neurones, où cela s'appelle décroissance des poids. [slide 49]

L'effet sur la mise à jour est lisible : chaque poids est diminué d'une quantité proportionnelle à sa propre valeur. Ceux que l'apprentissage ne renforce pas tendent donc vers zéro. [slide 174]

![Un poids de départ 1, que rien ne renforce, avec λ = 0,1 : chaque mise à jour lui retire un dixième de sa valeur, soit une multiplication par 0,9. Il vaut 0,81 après deux mises à jour, 0,35 après dix, 0,12 après vingt, et n'atteint jamais zéro. Sans la pénalité, il resterait à 1.](figures/decroissance-des-poids.svg) [ajout]

C'est une méthode automatique pour contrôler le nombre de poids effectifs, ceux qui pèsent vraiment dans la réponse, là où le choix du nombre de nœuds cachés est manuel. [slide 171, slide 174]

## Le chemin jusqu'ici
La décroissance réunit deux chapitres du cours. De dss/regularisation, elle reprend l'idée de garder tous les paramètres en les rétrécissant vers zéro. Cette idée contraignait les dss/moindres-carres-ordinaires, au nom du dss/compromis-biais-variance : accepter un peu de biais quand la variance baisse davantage, ce que tranche dss/erreur-de-test, mesurée sur des données non vues. [ajout]

De dss/retropropagation, elle reprend la correction $\Delta w_{ij}$ de chaque poids, à laquelle elle retranche $\lambda w_{ij}$. Cette correction est un pas de dss/descente-de-gradient, qui suit la pente de l'erreur comme le faisait déjà la dss/regle-delta pour un seul neurone. [ajout]

Le réseau est un dss/reseau-multicouche : la dss/limite-du-perceptron a imposé sa couche cachée, et la dss/fonction-d-activation lisse de ses nœuds permet de les corriger par petites touches. Chaque nœud reprend le dss/perceptron, l'unité d'un dss/reseau-de-neurones-artificiel qui calcule une dss/fonction-discriminante-lineaire, et le tout apprend sur des exemples, au sens de dss/apprentissage-inductif, étiquetés, au sens de dss/apprentissage-supervise. [ajout]

## Exemple minimal
Avec $\lambda=0{,}1$, la valeur typique du cours, un poids de 1 que rien ne renforce vaut 0,9 après une mise à jour, 0,81 après deux, 0,35 après dix. [slide 174, slide 184, ajout]

## Geste de calcul type
Après chaque correction de la rétropropagation, retrancher $\lambda$ fois le poids ; régler $\lambda$ dans la plage donnée par le cours, de 0,001 à 0,5. [slide 174, slide 184]

## Cesse d'être valide quand
La pénalité rétrécit sans annuler, comme ridge : un poids que rien ne renforce est multiplié par 0,9 à chaque mise à jour, et n'est donc jamais mis exactement à zéro. La connexion reste. [slide 62, ajout]

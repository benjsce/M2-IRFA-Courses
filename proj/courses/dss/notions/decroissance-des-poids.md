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
- slide 174
---

## Ce que c'est
Pénaliser la croissance des poids inutiles en ajoutant leur somme des carrés à la fonction d'erreur. [slide 174]

## Forme
$$E=\tfrac12\sum_j(t_j-o_j)^2+\frac{\lambda}{2}\sum_i w_{ij}^2\ \Longrightarrow\ \Delta w_{ij}=\Delta w_{ij}-\lambda w_{ij}$$ [slide 174]

## Ce qui la définit
C'est la pénalité de ridge, appliquée aux poids d'un réseau. Le cours fait le rapprochement lui-même, dans le chapitre sur ridge : pénaliser par la somme des carrés des paramètres est aussi employé en réseaux de neurones, où cela s'appelle décroissance des poids. [slide 49]

L'effet sur la mise à jour est lisible : chaque poids est diminué d'une quantité proportionnelle à sa propre valeur. Ceux que l'apprentissage ne renforce pas tendent donc vers zéro. [slide 174]

C'est une méthode automatique de contrôle du nombre de poids effectifs, là où le choix du nombre de nœuds cachés est manuel. [slide 171, slide 174]


## Le chemin jusqu'ici
Deux chapitres se rejoignent ici, et c'est la seule fiche du cours dans ce cas. [ajout]

**Le réseau.** dss/apprentissage-supervise et dss/apprentissage-inductif donnent dss/fonction-discriminante-lineaire et dss/reseau-de-neurones-artificiel, puis dss/perceptron, dss/limite-du-perceptron et dss/fonction-d-activation, d'où sort dss/reseau-multicouche ; dss/regle-delta et dss/descente-de-gradient donnent dss/retropropagation. [ajout]

**La pénalité.** dss/moindres-carres-ordinaires d'un côté, dss/erreur-de-test puis dss/compromis-biais-variance de l'autre, donnent dss/regularisation. [ajout]

La décroissance des poids est littéralement la pénalité de ridge appliquée aux poids d'un réseau — et le rapprochement n'est pas de moi : le cours le fait lui-même, dès le chapitre sur ridge. [slide 49]

## Exemple minimal
Avec $\lambda=0{,}1$, un poids que rien ne renforce perd un dixième de sa valeur à chaque mise à jour. [slide 184]

## Geste de calcul type
Le régler dans la plage donnée par le cours, de 0,001 à 0,5, valeur typique 0,1 — et retenir que ce $\lambda$ n'est pas celui de ridge ni celui du boosting. [slide 184]

## Cesse d'être valide quand
La pénalité rétrécit sans annuler, exactement comme ridge : aucun poids n'est mis à zéro exactement, la connexion reste. [slide 62]

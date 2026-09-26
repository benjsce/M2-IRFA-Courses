---
id: dss/bic
nom: Critère d'information bayésien
symbole: BIC
type: notion
statut: source
cas_de: dss/critere-penalise
valeur: $\log(n)\,d\hat\sigma^2$ ajouté à la RSS
construite_a_partir_de:
- dss/moindres-carres-ordinaires
alias:
- BIC
- Bayesian information criterion
refs:
- slide 39
- slide 43
---

## Ce que c'est
Le critère pénalisé dont la pénalité croît avec la taille de l'échantillon. [slide 43]

## Forme
$$\mathrm{BIC}=\frac{1}{n}\big(\mathrm{RSS}+\log(n)\,d\hat\sigma^2\big)$$ [slide 43]

## Ce que les symboles modélisent
BIC se lit comme le $C_p$ : une erreur d'apprentissage plus une pénalité, et le plus petit l'emporte. Mais sa pénalité dépend de la taille de l'échantillon : à nombre de prédicteurs égal, il devient plus sévère à mesure que les données s'accumulent. [slide 43]

Comme dans le $C_p$, $d$ compte les prédicteurs du modèle et $\hat\sigma^2$ est la variance du bruit, estimée sur le modèle complet ; $n$ est le nombre d'observations. [slide 43, ajout]

## Ce qui la définit
Il remplace le terme $2d\hat\sigma^2$ du $C_p$ par $\log(n)d\hat\sigma^2$ : la seule différence est le facteur qui multiplie le nombre de variables. [slide 43]

Comme $\log n>2$ dès que $n\ge8$, la pénalité est plus lourde et le modèle retenu plus petit que celui du $C_p$. [slide 43]


## Le chemin jusqu'ici
dss/moindres-carres-ordinaires fournit la RSS du modèle jugé et celle du modèle complet, d'où l'on tire $\hat\sigma^2$, sur les exemples de dss/apprentissage-supervise. Il ne demande rien de plus que le $C_p$. [ajout]

## Exemple minimal
Sur les 20 clients, $\log 20\approx3{,}0$ : la pénalité par variable vaut une fois et demie celle du $C_p$, et le BIC retient lui aussi le modèle à deux prédicteurs, à 1,54 contre 2,03 pour le modèle complet. [ajout]

## Geste de calcul type
Le calculer à côté du $C_p$ : l'écart entre les deux modèles retenus mesure directement le poids que l'on accorde à la parcimonie. [slide 40, slide 43]

## Cesse d'être valide quand
Sur un petit échantillon, $n\le7$, sa pénalité est plus légère que celle du $C_p$ et le classement s'inverse. [ajout]

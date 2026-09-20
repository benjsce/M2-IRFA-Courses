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

## Ce qui la définit
Il remplace le terme $2d\hat\sigma^2$ du $C_p$ par $\log(n)d\hat\sigma^2$ : la seule différence est le facteur qui multiplie le nombre de variables. [slide 43]

Comme $\log n>2$ dès que $n>7$, la pénalité est plus lourde et le modèle retenu plus petit que celui du $C_p$. [slide 43]


## Le chemin jusqu'ici
Le socle est celui du Cp de Mallows : dss/apprentissage-supervise, puis dss/moindres-carres-ordinaires. [ajout]

Les deux critères ne diffèrent pas par ce qu'ils supposent mais par le facteur qui multiplie le nombre de variables. Il fallait donc exactement le même point de départ pour que la comparaison ait un sens. [ajout]

## Exemple minimal
À $n=1000$, $\log n\approx 6{,}9$ : la pénalité par variable est plus de trois fois celle du $C_p$. [ajout]

## Geste de calcul type
Le calculer à côté du $C_p$ : l'écart entre les deux modèles retenus mesure directement le poids que l'on accorde à la parcimonie. [slide 40, slide 43]

## Cesse d'être valide quand
Sur un petit échantillon, $n<8$, sa pénalité est plus légère que celle du $C_p$ et le classement s'inverse. [ajout]

---
id: dss/reduction-de-dimension
nom: Réduction de dimension
type: abstraite
statut: source
cas_de: dss/selection-de-variables
valeur: projeter les prédicteurs, puis ajuster sur les projections
parametre: la réponse sert-elle à choisir les directions
construite_a_partir_de:
- dss/moindres-carres-ordinaires
alias:
- dimension reduction
refs:
- slide 71
- slide 72
- slide 73
---

## Ce que c'est
Transformer les $p$ prédicteurs en $M<p$ combinaisons linéaires, puis ajuster les moindres carrés sur ces combinaisons. [slide 71]

## Forme
$$Z_m=\sum_{j=1}^{p}\phi_{mj}X_j,\qquad y_i=\theta_0+\sum_{m=1}^{M}\theta_m z_{im}+\epsilon_i$$ [slide 72]

## Ce que les symboles modélisent
$Z_m$ est une combinaison des prédicteurs, donc une variable construite et non observée. $\phi_{mj}$ et $\theta_m$ se ressemblent et ne font pas le même travail : le premier est le poids du prédicteur $j$ dans la direction $m$, il dit **comment la direction est faite** ; le second est le coefficient de régression sur cette direction, il dit **ce qu'elle vaut pour prédire**. $M$ est le nombre de directions retenues. [slide 72]

## Ce que les membres partagent
Tous ramènent l'estimation de $p+1$ coefficients à celle de $M+1$ coefficients, avec $M<p$. Le gain n'est pas de retirer des variables mais d'en estimer moins. [slide 73]

La contrainte imposée aux coefficients d'origine est explicite : $\beta_j=\sum_{m}\theta_m\phi_{mj}$. Toutes les méthodes de la famille sont donc des moindres carrés contraints, écrits autrement. [slide 73]

Dans tous les cas, les prédicteurs doivent être standardisés avant de construire les directions, et $M$ se choisit par validation croisée. [slide 75, slide 85, slide 89]

## Pourquoi ce niveau existe
Le cours construit la seconde méthode entièrement contre la première, en ne changeant qu'une chose : la réponse est-elle utilisée pour choisir les directions. Les séparer ferait perdre ce contraste, qui est tout le contenu de la slide d'ouverture des moindres carrés partiels. [slide 86]


## Le chemin jusqu'ici
dss/apprentissage-supervise, puis dss/moindres-carres-ordinaires sur lesquels la projection débouche. [ajout]

La famille ne remplace pas l'ajustement, elle change ce qu'on lui donne à ajuster. Les moindres carrés restent donc au socle, en aval de la projection et non en amont. [ajout]

## Exemple minimal
Avec $p=45$ prédicteurs et $M=5$ directions, on passe de 46 coefficients à estimer à 6. [ajout]

## Geste de calcul type
Standardiser, construire les $M$ directions, ajuster les moindres carrés dessus, puis revenir aux coefficients d'origine par $\beta_j=\sum_m\theta_m\phi_{mj}$ si l'on veut les lire. [slide 73]

## Cesse d'être valide quand
Ce n'est pas de la sélection de variables : chaque direction est une combinaison de tous les prédicteurs, donc aucun n'est écarté. Le modèle final reste illisible variable par variable. [slide 85]

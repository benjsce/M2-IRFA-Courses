---
id: dss/aic
nom: Critère d'information d'Akaike
symbole: AIC
type: notion
statut: source
cas_de: dss/critere-penalise
valeur: $2d$ ajouté à moins deux fois la log-vraisemblance
construite_a_partir_de:
- dss/moindres-carres-ordinaires
alias:
- AIC
- Akaike information criterion
refs:
- slide 39
- slide 42
---

## Ce que c'est
Le critère pénalisé défini pour toute la classe des modèles ajustés par maximum de vraisemblance. [slide 42]

## Forme
$$\mathrm{AIC}=-2\log L+2\cdot d$$ [slide 42]

## Ce que les symboles modélisent
AIC est un score qu'on compare, non une quantité qu'on interprète : sa valeur absolue ne dit rien, seul son classement entre modèles compte. $L$ est la vraisemblance **maximisée**, donc déjà optimisée sur les paramètres — c'est exactement pour cela qu'il faut la pénaliser. [slide 42]

## Ce qui la définit
Sa portée est plus large que celle du $C_p$ : il ne suppose pas un modèle linéaire, seulement une vraisemblance maximisable. [slide 42]

Dans le cas linéaire à erreurs gaussiennes, le maximum de vraisemblance et les moindres carrés coïncident, et l'AIC devient équivalent au $C_p$. [slide 42]


## Le chemin jusqu'ici
dss/apprentissage-supervise donne le cadre, dss/moindres-carres-ordinaires le modèle ajusté. [ajout]

L'AIC ne demande rien de plus, et c'est ce qui fait sa portée : il vaut pour toute vraisemblance maximisable, le cas linéaire n'étant que celui où il rejoint le Cp. [ajout]

## Exemple minimal
Pour une régression à erreurs gaussiennes, $-2\log L$ vaut $n\log(\mathrm{RSS}/n)$ à une constante près ; sur les 20 clients, l'AIC vaut 6,29 pour le modèle à deux prédicteurs et 9,59 pour le modèle complet. [ajout]

## Geste de calcul type
Reporter la log-vraisemblance maximisée, ajouter deux fois le nombre de paramètres, retenir la plus petite valeur. [slide 42]

## Cesse d'être valide quand
Sa pénalité ne dépend pas de $n$ : sur un grand échantillon, il retient des modèles plus grands que le BIC. [slide 43]

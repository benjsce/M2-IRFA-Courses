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

$d$ compte les prédicteurs du modèle, sans la constante. [ajout]

## Ce qui la définit
Sa portée est plus large que celle du $C_p$ : il ne suppose pas un modèle linéaire, seulement une vraisemblance maximisable. [slide 42]

Dans le cas linéaire à erreurs gaussiennes, le maximum de vraisemblance et les moindres carrés coïncident, et le cours dit l'AIC équivalent au $C_p$. [slide 42]

Équivalent veut dire : ils rangent les modèles dans le même ordre. C'est exact quand la variance du bruit est la même estimation $\hat\sigma^2$ pour tous les modèles : $-2\log L$ vaut alors $\mathrm{RSS}/\hat\sigma^2$ à une constante près, et l'AIC vaut $n\,C_p/\hat\sigma^2$ à la même constante près. [ajout]


## Le chemin jusqu'ici
L'AIC ne demande qu'un modèle ajusté sur les exemples de dss/apprentissage-supervise ; dss/moindres-carres-ordinaires en est le cas que le cours traite, celui où il rejoint le $C_p$. Il vaut pour toute vraisemblance maximisable, et c'est ce qui fait sa portée. [ajout]

## Exemple minimal
Sur les 20 clients, avec la variance du bruit estimée dans chaque modèle, l'AIC vaut 6,29 pour le modèle à l'endettement et au revenu et 9,59 pour le modèle complet : même choix que le $C_p$ (1,40 et 1,68), sans que les nombres soient proportionnels. Avec la même $\hat\sigma^2=1{,}40$ pour les deux, il vaudrait 20,03 et 24,00, soit $20\,C_p/\hat\sigma^2$. [ajout]

## Geste de calcul type
Reporter moins deux fois la log-vraisemblance maximisée, ajouter deux fois le nombre de prédicteurs $d$, retenir la plus petite valeur. Compter aussi la constante ajouterait la même quantité à tous les modèles, sans changer le classement. [slide 42, ajout]

Pour une régression à erreurs gaussiennes dont la variance est estimée dans chaque modèle, $-2\log L$ vaut $n\log(\mathrm{RSS}/n)$ à une constante près : $20\log(22{,}43/20)+2\times2=6{,}29$ et $20\log(19{,}59/20)+2\times5=9{,}59$. [ajout]

## Cesse d'être valide quand
Sa pénalité ne dépend pas de $n$ : sur un grand échantillon, il retient des modèles plus grands que le BIC. [slide 43]

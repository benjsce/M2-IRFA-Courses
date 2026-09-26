---
id: dss/r2-ajuste
nom: R2 ajusté
type: notion
statut: source
cas_de: dss/critere-penalise
valeur: un degré de liberté retiré au numérateur et au dénominateur
construite_a_partir_de:
- dss/moindres-carres-ordinaires
alias:
- adjusted R2
refs:
- slide 39
- slide 44
---

## Ce que c'est
Le $R^2$ corrigé du nombre de variables ; il se lit à la hausse : le plus grand l'emporte. [slide 44]

## Forme
$$R^2=1-\frac{\mathrm{RSS}}{\mathrm{TSS}}\qquad\longrightarrow\qquad R^2_{\text{ajusté}}=1-\frac{\mathrm{RSS}/(n-d-1)}{\mathrm{TSS}/(n-1)}$$ [slide 44, ajout]

## Ce que les symboles modélisent
TSS est la dispersion totale de la variable à expliquer : l'erreur qu'on ferait en ne prédisant jamais que la moyenne. C'est l'étalon de la comparaison — le $R^2$ rapporte l'erreur du modèle à celle-là, et non à zéro. [slide 44]

$n-d-1$ et $n-1$ sont les degrés de liberté : le nombre d'observations moins le nombre de coefficients estimés, $d$ prédicteurs et la constante pour la RSS, la seule moyenne pour la TSS. [ajout]

## Ce qui la définit
Le $R^2$ est un moins un rapport d'erreurs : d'autant plus grand que l'erreur du modèle est petite, d'où sa lecture à la hausse. Le $R^2$ ajusté divise chaque somme de carrés par ses degrés de liberté. Ajouter une variable fait baisser la RSS, mais aussi $n-d-1$ : le quotient $\mathrm{RSS}/(n-d-1)$ ne baisse, et le $R^2$ ajusté ne monte, que si la RSS baisse assez. [slide 44, ajout]

C'est ce qui lui fait payer un prix pour l'inclusion de variables inutiles, là où le $R^2$ ordinaire monte toujours. [slide 30, slide 44]


## Le chemin jusqu'ici
dss/moindres-carres-ordinaires fournit la RSS, et dss/apprentissage-supervise la réponse observée, dont la TSS mesure la dispersion autour de sa moyenne : le $R^2$ ajusté rapporte l'une à l'autre. [ajout]

## Exemple minimal
Sur les 20 clients, passer de deux à cinq prédicteurs fait baisser la RSS de 22,43 à 19,59, mais monter le quotient $\mathrm{RSS}/(n-d-1)$ de 1,32 à 1,40, puisque les degrés de liberté passent de 17 à 14. Le $R^2$ monte de 0,49 à 0,55 ; le $R^2$ ajusté descend de 0,43 à 0,40. [ajout]

## Geste de calcul type
Rapporter $\mathrm{RSS}/(n-d-1)$ de chaque modèle, ici $22{,}43/17=1{,}32$ et $19{,}59/14=1{,}40$, à $\mathrm{TSS}/(n-1)$, la même pour tous, $44{,}03/19=2{,}32$ ; d'où $1-1{,}32/2{,}32=0{,}43$ et $1-1{,}40/2{,}32=0{,}40$ ; le modèle à deux prédicteurs l'emporte. [slide 40, slide 44, ajout]

## Cesse d'être valide quand
Sa justification est plus faible que celle du $C_p$ ou du BIC. Le cours le range avec eux parce qu'il vise le même but, un modèle de faible erreur de test ; mais c'est un ajustement de degrés de liberté, pas une estimation de cette erreur. [slide 44, ajout]

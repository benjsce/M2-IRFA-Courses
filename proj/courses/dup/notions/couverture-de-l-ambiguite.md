---
id: dup/couverture-de-l-ambiguite
nom: Couverture de l’ambiguïté
type: notion
statut: source
construite_a_partir_de:
- dup/maxmin-eu
alias:
- hedging ambiguity
- superadditivité de la valeur
refs:
- L4 slide 41
- L4 slide 51
- L4 slide 52
---

## Ce que c'est
Le pire prior dépend de la position, de sorte que combiner deux actes peut valoir davantage que la somme de leurs valeurs prises séparément. [L4 slide 41]

## Forme
$$\widehat{I}(a+b)\ \ge\ \widehat{I}(a)+\widehat{I}(b)$$ [L4 slide 52]

## Ce qui la définit
Sur la bande $K=\{p:0{,}2\le p_R\le0{,}6\}$ et avec $u(x)=x$, parier 100 sur rouge vaut 20, parier 100 contre rouge vaut 40, et les deux paris détenus ensemble paient 100 à coup sûr. Chaque pari est jugé sous son pire prior, et ces deux priors ne sont pas le même : la valeur n’est donc pas additive, même avec une utilité linéaire en monnaie. [L4 slide 41]

La géométrie du mélange dit la même chose autrement. Avec les vecteurs d’utilité $f=(0,2)$ et $g=(2,0)$ et $K=\{(p,1-p):1/4\le p\le3/4\}$, chaque prior donne une droite en fonction du poids de mélange, et le maxmin en retient l’enveloppe inférieure, qui est concave. Les deux actes valent 0,5 chacun, et leur mélange à parts égales vaut 1. [L4 slide 51]

C’est l’étape de la démonstration où l’aversion à l’ambiguïté entre : combinée à l’homogénéité positive, elle donne la superadditivité, donc la concavité de la fonctionnelle — ce qui ouvre la voie aux fonctions affines de support. [L4 slide 52]

## Le chemin jusqu'ici
dup/acte et dup/loterie s’emboîtent dans dup/cadre-anscombe-aumann ; dup/ensemble-de-priors y découpe la croyance et dup/independance-de-certitude affaiblit l’axiome, ce qui donne dup/maxmin-eu. L’autre amont de ce modèle est le motif à expliquer : dup/utilite-esperee-subjective, construite sur dup/acte et dup/fonction-utilite et adossée à dup/principe-de-la-chose-sure, que dup/paradoxe-d-ellsberg met en défaut, d’où dup/aversion-a-l-ambiguite. [ajout]

Cette fiche lit une propriété du modèle qu’on ne voit pas dans sa formule : le minimum étant pris acte par acte, il ne commute pas avec l’addition. Elle vient donc après le maxmin, et non avant — il fallait l’opérateur pour découvrir ce qu’il fait aux sommes. [ajout]

## Exemple minimal
Les deux paris opposés de la bande $K$ valent 20 et 40 pris séparément, et 100 détenus ensemble. [L4 slide 41]

![Les deux priors extrêmes de l'ensemble donnent chacun une droite en fonction du poids du mélange ; le maxmin retient l'enveloppe inférieure, en trait plein. Le creux est aux extrémités : les deux actes valent 0,5 chacun, leur mélange à parts égales vaut 1.](figures/couverture-de-l-ambiguite.svg) [ajout]

## Geste de calcul type
Chercher le pire prior acte par acte, puis celui de la somme : s’il change d’un acte à l’autre, la valeur de la combinaison dépasse la somme des valeurs. [L4 slide 41]

## Cesse d'être valide quand
La superadditivité n’est pas une additivité manquée, c’est l’axiome d’aversion à l’ambiguïté lui-même : un agent attiré par l’ambiguïté donnerait l’inégalité inverse, et un agent neutre l’égalité. [L4 slide 45]

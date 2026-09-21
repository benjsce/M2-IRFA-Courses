---
id: dup/equilibre-sous-ambiguite
nom: Équilibre avec investisseurs ambigus
symbole: $\hat p$
type: notion
statut: source
construite_a_partir_de:
- dup/demande-sous-ambiguite
alias:
- equilibrium price and participation
- non-participation d'équilibre
refs:
- L4 slide 66
- L4 slide 67
---

## Ce que c'est
Le prix qui égalise l’offre de l’actif risqué et la somme des demandes de deux populations, l’une qui connaît la loi et l’autre qui l’ignore. [L4 slide 66]

## Forme
$$(1-\lambda)\,x_R^{*}(p)+\lambda\,x_A^{*}(p)=\bar x,\qquad \hat p=\hat v-\frac{\hat\sigma^2\bar x}{1-\lambda}$$ [L4 slide 66, L4 slide 67]

## Ce qui la définit
Tous les investisseurs ont la même utilité exponentielle et un accès illimité à l’emprunt ; une fraction $\lambda$ d’entre eux considère l’ensemble des modèles gaussiens, le reste un modèle unique. La demande agrégée est continue et strictement décroissante, et parcourt toute la droite réelle : le prix d’équilibre existe et il est unique. [L4 slide 66]

$\hat p$ est le prix qui prévaudrait si les investisseurs ambigus ne détenaient rien. Sa position par rapport à l’intervalle de non-participation décide du régime : au-dessous de $v_{\min}$ ils achètent, au-dessus de $v_{\max}$ ils vendent, et entre les deux ils s’abstiennent et le prix vaut $\hat p$. Avec une offre positive et une moyenne située dans l’intervalle, seuls les deux premiers régimes se présentent, et dans le régime participant les deux types détiennent des positions positives. [L4 slide 67]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite portent dup/utilite-esperee, que dup/equivalent-certain lit en monnaie et que dup/cara rend explicite : c’est dup/demande-cara-normale. Le critère de l’autre population vient de dup/acte et dup/loterie emboîtés dans dup/cadre-anscombe-aumann, où dup/ensemble-de-priors découpe la croyance et dup/independance-de-certitude affaiblit l’axiome, le motif venant de dup/utilite-esperee-subjective, adossée à dup/principe-de-la-chose-sure, que dup/paradoxe-d-ellsberg met en défaut, d’où dup/aversion-a-l-ambiguite puis dup/maxmin-eu. Les deux se rejoignent dans dup/demande-sous-ambiguite. [ajout]

Cette fiche fait le pas qui manque : jusqu’ici le prix était donné, ici il se forme. La non-participation cesse alors d’être un choix individuel pour devenir une propriété du marché, et c’est pourquoi elle exige d’abord la demande individuelle des deux types. [ajout]

## Exemple minimal
Avec $\hat v=110$, $\hat\sigma=20$, une offre de 0,005 par investisseur et la moitié d’investisseurs ambigus, le prix d’abstention vaut 106 : s’il tombe dans $[105;115]$, les ambigus ne détiennent rien et 106 est le prix d’équilibre. [ajout]

## Geste de calcul type
Calculer d’abord le prix d’abstention, puis le situer par rapport aux deux bornes de la moyenne ambiguë : le régime, et avec lui le prix, se lisent sur cette seule comparaison. [L4 slide 67]

## Cesse d'être valide quand
Le résultat suppose une population ambiguë homogène, la même utilité exponentielle pour tous et un emprunt illimité ; la non-participation y est un fait d’équilibre, non une friction ni un coût d’entrée. [L4 slide 66]

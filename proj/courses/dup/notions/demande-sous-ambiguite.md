---
id: dup/demande-sous-ambiguite
nom: Demande optimale sous ambiguïté
symbole: $x_A^{*}$
type: notion
statut: source
construite_a_partir_de:
- dup/demande-cara-normale
- dup/maxmin-eu
alias:
- optimal demand under ambiguity
- intervalle de non-participation
refs:
- L4 slide 64
- L4 slide 65
---

## Ce que c'est
Quand la moyenne du paiement n’est connue que dans un intervalle, la demande de l’actif risqué est nulle sur toute une plage de prix. [L4 slide 65]

## Forme
$$x_A^{*}(p)=\begin{cases}(v_{\min}-p)/\sigma_{\max}^2,&p<v_{\min}\\[2pt]0,&v_{\min}\le p\le v_{\max}\\[2pt](v_{\max}-p)/\sigma_{\max}^2,&p>v_{\max}\end{cases}$$ [L4 slide 65]

## Ce que les symboles modélisent
$v_{\min}$ et $v_{\max}$ bornent les moyennes que l'investisseur juge plausibles : l'écart entre les deux mesure son **ignorance**, et non le risque du titre. $\sigma_{\max}$ borne de la même façon les écarts types envisagés. Des quatre symboles, $x_A^{*}$ est le seul qui soit une décision ; les trois autres décrivent ce que l'agent ne sait pas. [L4 slide 64, L4 slide 65]

## Ce qui la définit
L’investisseur retient tous les modèles gaussiens dont la moyenne tombe entre $v_{\min}$ et $v_{\max}$ et l’écart type entre $\sigma_{\min}$ et $\sigma_{\max}$, puis maximise le plus mauvais équivalent certain. Le pire modèle change avec le signe de la position : une position longue est jugée sous la moyenne la plus basse, une position courte sous la plus haute, et toute position non nulle sous l’écart type le plus élevé. [L4 slide 64]

Les deux ambiguïtés ne jouent donc pas le même rôle. Celle qui porte sur la moyenne crée l’intervalle de non-participation, parce qu’elle fait basculer la borne retenue avec le sens de la position ; celle qui porte sur la variance ne fait que réduire la taille des positions. Aux bornes de l’intervalle, zéro reste l’unique optimum, la pénalité de variance étant strictement positive dès que la position ne l’est pas — ce qui diffère du cas à utilité linéaire. [L4 slide 65]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite portent dup/utilite-esperee, dont dup/equivalent-certain donne la lecture en monnaie ; avec dup/cara, cela donne dup/demande-cara-normale, la demande de référence quand la loi est connue. [ajout]

L’autre amont fournit le critère. dup/acte et dup/loterie s’emboîtent dans dup/cadre-anscombe-aumann, où dup/ensemble-de-priors découpe la croyance et dup/independance-de-certitude affaiblit l’axiome ; le motif à représenter vient de dup/utilite-esperee-subjective, adossée à dup/principe-de-la-chose-sure et à dup/acte, que dup/paradoxe-d-ellsberg met en défaut, d’où dup/aversion-a-l-ambiguite, puis dup/maxmin-eu. [ajout]

La fiche est l’application du second au premier : on garde le problème de portefeuille et l’on remplace l’espérance par le pire cas. C’est la conjonction qui produit le résultat — ni le programme seul, ni le critère seul ne donnent une plage de non-participation. [ajout]

## Exemple minimal
Avec $v_{\min}=105$, $v_{\max}=115$ et $\sigma_{\max}=20$, l’investisseur ambigu reste à l’écart tant que le prix est compris entre 105 et 115, et achète $5/400=0{,}0125$ au prix 100. [ajout]

## Geste de calcul type
Situer le prix par rapport aux deux bornes de la moyenne ; hors de l’intervalle, appliquer la formule de la demande sous risque avec la borne la plus défavorable et l’écart type le plus élevé. [L4 slide 65]

## Cesse d'être valide quand
L’intervalle ne vient que de l’ambiguïté sur la moyenne : une ambiguïté portant sur la seule variance laisse la participation intacte et n’en change que l’ampleur. [L4 slide 65]

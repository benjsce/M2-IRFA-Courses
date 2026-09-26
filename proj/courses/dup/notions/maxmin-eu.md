---
id: dup/maxmin-eu
nom: Utilité espérée maxmin
symbole: $\Pi$
type: notion
statut: source
cas_de: dup/reponse-a-l-ambiguite
valeur: un ensemble de probabilités a priori
construite_a_partir_de:
- dup/aversion-a-l-ambiguite
- dup/ensemble-de-priors
- dup/independance-de-certitude
alias:
- maxmin expected utility
- MEU
refs:
- L1 slide 64
- L4 slide 38
- L4 slide 46
---

## Ce que c'est
Évaluer un acte sous celle de ses probabilités plausibles qui lui est la moins favorable. [L1 slide 64]

## Forme
$$V(f)=\min_{\pi\in\Pi}\sum_s\pi(s)\,U\big(f(s)\big)$$ [L1 slide 64]

## Ce que les symboles modélisent
$\Pi$ est l'ensemble des probabilités que l'agent juge plausibles, et le modèle ne lui en fait choisir aucune : il retient pour chaque acte la plus défavorable. $\Pi$ n'est donc pas une croyance, c'est un aveu d'ignorance. [L1 slide 64]

$I$ associe une valeur à un vecteur d'utilités, un état par coordonnée : $I(u\circ f)=V(f)$, la valeur de l'acte lue sur ses seules utilités. C'est un intermédiaire de démonstration, sans lecture économique propre. [L4 slide 48]

## Ce qui la définit
La croyance n’est plus un point mais un ensemble $\Pi$, et l’attitude face à l’ambiguïté est portée par le seul opérateur $\min$. [L1 slide 64]

Le quatrième cours en donne la définition complète, sous une autre lettre : l’ensemble $K$ y est supposé non vide, compact et convexe, et l’utilité n’a pas besoin d’être linéaire en monnaie — seule son extension aux loteries est affine. [L4 slide 38]

$$V(f)=\min_{p\in K}\sum_{s\in S}p(s)\,u\big(f(s)\big)$$ [L4 slide 38]

Le théorème de représentation sépare ce modèle du précédent par un seul axiome. Les quatre axiomes de base joints à l’indépendance pleine donnent l’utilité espérée subjective ; joints à l’indépendance de certitude et à l’aversion à l’ambiguïté, ils donnent le maxmin. L’utilité est unique à une transformation affine croissante près, et l’ensemble fermé convexe de priors est unique lui aussi. [L4 slide 46]

La démonstration procède par étapes, toutes visibles dans l’énoncé final. On établit d’abord l’utilité sur les loteries constantes, puis l’équivalent certain de chaque acte, ce qui donne une fonctionnelle lue sur les vecteurs d’utilité ; l’indépendance de certitude en fait une fonctionnelle positivement homogène, qu’on étend à tout l’espace, puis invariante par translation, donc continue ; l’aversion à l’ambiguïté la rend concave, une fonction concave admet en chaque point une affine de support, et ces supports se révèlent être des probabilités. L’ensemble $K$ est enfin celui des probabilités qui majorent la fonctionnelle partout. [L4 slide 47, L4 slide 48, L4 slide 49, L4 slide 50, L4 slide 53, L4 slide 54, L4 slide 55]

Sur l’urne à composition partiellement connue, avec $u(x)=x$ et le seul $p_R=1/3$ imposé, parier sur rouge vaut $100/3$ contre zéro pour parier sur bleu, et parier sur bleu-ou-vert vaut $200/3$ contre $100/3$ pour rouge-ou-vert. Les quatre choix d’Ellsberg sont représentés, parce que chaque pari est jugé sous la composition qui lui est la plus défavorable. [L4 slide 42]

## Le chemin jusqu'ici
Le premier fil est celui du problème. dup/acte et dup/fonction-utilite se combinent en dup/utilite-esperee-subjective, que dup/principe-de-la-chose-sure rend possible et que dup/paradoxe-d-ellsberg met en défaut, d'où dup/aversion-a-l-ambiguite : voilà le comportement qu'il faut représenter. [ajout]

Le second fil est celui des moyens. dup/acte et dup/loterie s'emboîtent dans dup/cadre-anscombe-aumann, qui fournit le mélange entre actes ; dup/ensemble-de-priors y découpe la croyance en une partie du simplexe, et dup/independance-de-certitude restreint l'axiome de mélange aux loteries constantes. [ajout]

Les deux fils se referment ici, et l'ordre a un sens : on garde des probabilités additives, mais on en garde **plusieurs**, et l'on retient la pire. L'ambiguïté n'est plus dans la mesure, elle est dans le fait qu'on n'en choisit pas une — et c'est l'affaiblissement de l'axiome qui autorise ce refus de choisir. [ajout]

## Exemple minimal
Si $\pi(B)$ est seulement connu dans $[0,\,2/3]$, parier sur le noir vaut son évaluation en $\pi(B)=0$. [ajout]

## Geste de calcul type
Pour chaque acte, chercher la probabilité de $\Pi$ qui minimise son espérance d’utilité, puis comparer les minima. Le minimum change d’un acte à l’autre : c’est ce qui produit la non-additivité apparente. [L1 slide 64]

## Cesse d'être valide quand
Le pessimisme est total et non paramétré : le modèle ne distingue pas un agent prudent d’un agent extrêmement prudent. [ajout]

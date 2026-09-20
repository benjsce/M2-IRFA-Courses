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
alias:
- maxmin expected utility
- MEU
refs:
- L1 slide 64
---

## Ce que c'est
Évaluer un acte sous celle de ses probabilités plausibles qui lui est la moins favorable. [L1 slide 64]

## Forme
$$V(f)=\min_{\pi\in\Pi}\sum_s\pi(s)\,U\big(f(s)\big)$$ [L1 slide 64]

## Ce qui la définit
La croyance n’est plus un point mais un ensemble $\Pi$, et l’attitude face à l’ambiguïté est portée par le seul opérateur $\min$. [L1 slide 64]

## Le chemin jusqu'ici
Même chemin que l'utilité espérée de Choquet : dup/acte et dup/fonction-utilite donnent dup/utilite-esperee-subjective, que dup/principe-de-la-chose-sure rend possible et que dup/paradoxe-d-ellsberg met en défaut, d'où dup/aversion-a-l-ambiguite. [ajout]

La réponse est ici opposée dans sa forme : on garde des probabilités additives, mais on en garde **plusieurs**, et l'on retient la pire. L'ambiguïté n'est plus dans la mesure, elle est dans le fait qu'on n'en choisit pas une. Deux voies, même socle — c'est pourquoi le cours les range sous une famille. [ajout]

## Exemple minimal
Si $\pi(B)$ est seulement connu dans $[0,\,2/3]$, parier sur le noir vaut son évaluation en $\pi(B)=0$. [ajout]

## Geste de calcul type
Pour chaque acte, chercher la probabilité de $\Pi$ qui minimise son espérance d’utilité, puis comparer les minima. Le minimum change d’un acte à l’autre : c’est ce qui produit la non-additivité apparente. [L1 slide 64]

## Cesse d'être valide quand
Le pessimisme est total et non paramétré : le modèle ne distingue pas un agent prudent d’un agent extrêmement prudent. [ajout]

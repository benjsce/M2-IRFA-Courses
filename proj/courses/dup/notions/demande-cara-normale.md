---
id: dup/demande-cara-normale
nom: Demande d’actif risqué sous CARA-normale
symbole: $x_R^{*}$
type: notion
statut: source
construite_a_partir_de:
- dup/cara
- dup/equivalent-certain
alias:
- portfolio analysis under risk
- demande sous risque
refs:
- L4 slide 63
---

## Ce que c'est
Sous utilité exponentielle et paiement gaussien, la position optimale est l’écart entre la moyenne du paiement et son prix, divisé par la variance. [L4 slide 63]

## Forme
$$\mathrm{CE}(x)=w+(\hat v-p)x-\tfrac12\hat\sigma^2x^2,\qquad x_R^{*}(p)=\frac{\hat v-p}{\hat\sigma^{2}}$$ [L4 slide 63]

## Ce que les symboles modélisent
$p$ est le prix du titre aujourd'hui, $\hat v$ le paiement qu'il rendra en moyenne : leur écart est le gain espéré par unité détenue. $\hat\sigma$ est l'écart type de ce paiement, donc ce qu'une unité fait courir. $x_R^{*}$ est le nombre d'unités détenues à l'optimum — un nombre signé, négatif quand l'agent vend à découvert. [L4 slide 63]

$p$ est ici un prix, alors que la lettre désigne une probabilité partout ailleurs dans le cours. [ajout]

## Ce qui la définit
La monnaie a pour prix et pour paiement terminal l’unité ; le budget $w=m+px$ donne la richesse terminale $w+x(\tilde v-p)$, et la normalité jointe à l’exponentielle rend l’équivalent certain exactement quadratique. [L4 slide 63]

Deux conséquences suivent, et ce sont elles qu’on réutilise. La demande est linéaire en prix, donc strictement décroissante ; et elle ne dépend pas de la richesse initiale, puisque l’aversion absolue est constante. L’emprunt et la vente à découvert sont supposés sans limite. [L4 slide 63]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite se combinent en dup/utilite-esperee, dont dup/equivalent-certain donne la lecture en monnaie : le montant sûr qui vaut autant que le pari. [ajout]

dup/cara fixe la forme de l’utilité, et c’est cette forme précise, avec la loi normale, qui rend l’équivalent certain calculable en clôture — moyenne moins demi-variance pondérée. La position optimale se lit alors directement sur une parabole, sans espérance à évaluer. Il fallait donc les deux : la grandeur à maximiser, et l’utilité qui la rend explicite. [ajout]

## Exemple minimal
Avec $\hat v=110$, $p=100$ et $\hat\sigma=20$, la position optimale vaut $10/400=0{,}025$. [ajout]

## Geste de calcul type
Écrire l’équivalent certain comme une parabole en la position, puis la dériver et annuler : le sommet est la demande. [L4 slide 63]

![L'équivalent certain de l'exemple, moins la richesse initiale, comme parabole en la position : $10\,x-200\,x^2$. Le gain espéré seul, en pointillé, croît sans fin ; la pénalité de variance finit par l'emporter, et le sommet, en $x=10/400=0{,}025$, est la demande.](figures/demande-cara-normale.svg) [ajout]

## Cesse d'être valide quand
Le modèle suppose la loi connue — une seule moyenne, un seul écart type ; c’est cette unicité que l’ambiguïté lève. [L4 slide 64]

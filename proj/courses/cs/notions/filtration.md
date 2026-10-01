---
id: cs/filtration
nom: Filtration
symbole: '$(\mathcal F_t)_{t\in\mathbb R_+}$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- filtration
- flux d'information
refs:
- Déf. 0.5.8
---

## Ce que c'est
Une famille croissante de tribus indexée par le temps : à chaque date, l'information disponible, qui ne fait que s'enrichir. [Déf. 0.5.8]

## Forme
$$(\mathcal F_t)_{t\in\mathbb R_+},\qquad\mathcal F_t\subset\mathcal A,\qquad s\le t\ \Rightarrow\ \mathcal F_s\subset\mathcal F_t$$ [Déf. 0.5.8]

## Ce que les symboles modélisent
$\mathcal F_t$ est la tribu des événements dont on sait, à la date $t$, s'ils se sont produits ou non. L'inclusion $\mathcal F_s\subset\mathcal F_t$ dit qu'une information acquise ne se perd pas. $(\mathcal F_t)_{t\in\mathbb R_+}$ est la famille entière, une information qui évolue avec le temps. [Déf. 0.5.8, ajout]

## Ce qui la définit
Une tribu seule, comme $\mathcal G$ dans l'espérance conditionnelle, est une information figée. La filtration la fait dépendre de la date, avec une seule contrainte : on n'oublie rien. Quand $\Omega$ est fini, chaque $\mathcal F_t$ se lit comme un découpage de $\Omega$, et le découpage s'affine avec le temps. [Déf. 0.5.8, ajout]

![Deux lancers de pièce, en t = ½ et en t = 1 : Ω = {PP, PF, FP, FF}. Avant ½, rien n'est connu, un seul bloc : 𝓕_t = {∅, Ω}. Entre ½ et 1, le premier lancer est connu : deux blocs. En 1, les deux lancers : quatre blocs. Chaque découpage affine le précédent : 𝓕_s ⊂ 𝓕_t pour s ≤ t.](figures/filtration.svg) [ajout]

## Exemple minimal
Une pièce lancée en $t=\tfrac12$, une autre en $t=1$ : $\mathcal F_t=\{\varnothing,\Omega\}$ pour $t<\tfrac12$, $\mathcal F_t$ est engendrée par le premier lancer pour $\tfrac12\le t<1$, et par les deux à partir de $t=1$. [ajout]

## Geste de calcul type
Pour décrire une filtration sur un $\Omega$ fini, donner à chaque date le découpage de $\Omega$ en blocs que l'information ne sépare pas, et vérifier que chaque découpage est plus fin que le précédent. [ajout]

## Cesse d'être valide quand
L'information peut se perdre : une suite de tribus qui n'est pas croissante n'est pas une filtration. La définition ne dit pas non plus d'où vient l'information ; c'est la filtration naturelle d'un processus qui la tire de ce qu'on observe. [Déf. 0.5.8, Rem. 0.5.4, ajout]

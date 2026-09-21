---
id: dup/pessimisme
nom: Pessimisme
type: notion
statut: source
construite_a_partir_de:
- dup/rdu
alias:
- pessimism
- distorsion pessimiste
refs:
- L4 slide 14
---

## Ce que c'est
Une déformation des probabilités qui reste au-dessus de la diagonale, donc qui charge les rangs les plus bas. [L4 slide 14]

## Forme
$$\varphi(p)\ge p\ \ \forall p\qquad\Longrightarrow\qquad U(P)-\mathbb{E}[X]=\big[\varphi(p_1)-p_1\big](x_1-x_2)\le0$$ [L4 slide 14]

## Ce qui la définit
Avec la convention cumulative, $\varphi(p)\ge p$ signifie que le poids cumulé placé sur les mauvais résultats dépasse leur probabilité. Sur une loterie à deux résultats $x_1<x_2$ évaluée avec $u(x)=x$, la valeur tombe alors sous la moyenne : l'agent refuse le pari sans qu'aucune courbure de l'utilité y soit pour quelque chose. [L4 slide 14]

C'est la seconde source d'attitude face au risque que le cours isole. La courbure de $u$ mesure la sensibilité à la richesse ; la distorsion, elle, change le poids accordé selon le rang du résultat, et les deux agissent sur des objets différents. [L4 slide 14]

## Le chemin jusqu'ici
dup/loterie fournit l'objet à évaluer et dup/fonction-utilite la valeur d'un résultat ; leur combinaison est dup/utilite-esperee, où chaque résultat pèse sa probabilité. [ajout]

dup/rdu remplace ce poids par un saut de $\varphi$ sur les probabilités cumulées, et ouvre ainsi la question que cette fiche tranche : dans quel sens la déformation penche-t-elle. Le pessimisme est la réponse la plus simple — au-dessus de la diagonale — et il ne se formule qu'une fois la pondération par rang écrite. [ajout]

## Exemple minimal
Avec $\varphi(t)=\sqrt{t}$ et le pari $(0,\tfrac12;100,\tfrac12)$ évalué par $u(x)=x$ : $\varphi(0{,}5)=0{,}707$, la valeur vaut $100\times(1-0{,}707)=29{,}3$ pour une moyenne de 50. [ajout]

## Geste de calcul type
Comparer $\varphi(p)$ à $p$ sur tout l'intervalle : au-dessus de la diagonale l'agent alourdit les mauvais rangs, en dessous il les allège, et la courbe peut changer de côté en chemin. [L4 slide 14]

## Cesse d'être valide quand
Le pessimisme suffit à faire préférer la moyenne certaine à la loterie, mais pas à faire refuser tout étalement préservant la moyenne : celui-là demande en plus que $\varphi$ soit concave. [L4 slide 15]

---
id: dup/loterie
nom: Loterie
symbole: '$P$, $\Delta(X)$'
type: notion
statut: source
cas_de: dup/separation-gouts-croyances
construite_a_partir_de: []
alias:
- lottery
- risque objectif
refs:
- L1 slide 2
---

## Ce que c'est
Une distribution de probabilité sur les résultats, dont les probabilités font partie de l’énoncé. [L1 slide 2]

## Forme
$$\Delta(X)=\Big\{p:X\to[0,1]\ :\ \sum_{x\in X}p(x)=1\Big\},\qquad P=(x_1,p_1;\dots;x_n,p_n)$$ [L1 slide 2]

## Ce qui la définit
Le risque est dit objectif : rien n’est à inférer, les probabilités sont spécifiées avec l’objet. [L1 slide 2]

## Exemple minimal
$P=(0,\tfrac12;100,\tfrac12)$ : cent euros ou rien, à pile ou face. [ajout]

## Geste de calcul type
Un mélange $\alpha P+(1-\alpha)Q$ se calcule résultat par résultat : la probabilité de $x$ y vaut $\alpha P(x)+(1-\alpha)Q(x)$. [ajout]

## Cesse d'être valide quand
Dès que les probabilités ne sont pas données, l’objet n’est plus une loterie mais un acte. [L1 slide 2]

---
id: dup/poids-de-decision
nom: Poids de décision
symbole: $\pi_s$
type: notion
statut: source
construite_a_partir_de:
- dup/rdu
alias:
- decision weight
- poids de rang
refs:
- L4 slide 17
- L4 slide 26
---

## Ce que c'est
Le poids qu'une préférence dépendante du rang accorde à un état, lu sur le rang du paiement total et non sur la seule probabilité de cet état. [L4 slide 17]

## Forme
$$\pi_s=\varphi(P_s)-\varphi(P_{s-1}),\qquad P_s=\sum_{j\le s}p_j,\qquad P_0=0$$ [L4 slide 26]

## Ce qui la définit
$p_s$ dit la probabilité de l'état ; $\pi_s$ dit ce qu'il pèse dans l'évaluation, et ce poids dépend de l'endroit où le paiement total vient se ranger. Les deux nombres ne se confondent que si la déformation est l'identité. [L4 slide 17]

L'exemple du cours tient en deux lignes. Une action paie $S_L<S_H$ avec les probabilités $p$ et $1-p$ : détenue longue, elle fait de l'état bas son pire état, qui pèse alors $\varphi(p)$ ; vendue à découvert, le même état devient le meilleur et pèse $1-\varphi(1-p)$. La probabilité n'a pas bougé, le poids si. [L4 slide 17]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite se combinent en dup/utilite-esperee, où le poids d'un résultat est sa probabilité et rien d'autre. [ajout]

dup/rdu rompt cette identification en déformant les probabilités cumulées. Le poids devient alors un objet à part, qu'il faut nommer et calculer séparément — c'est l'objet de cette fiche —, et il cesse d'être une propriété de l'état seul pour devenir une propriété du couple état-portefeuille. [ajout]

## Exemple minimal
Avec $\varphi(t)=\sqrt{t}$ et $p=1/4$, l'état bas pèse $\varphi(0{,}25)=0{,}5$ en position longue et $1-\varphi(0{,}75)=0{,}134$ en position courte. [ajout]

## Geste de calcul type
Repérer d'abord le rang du paiement total dans chaque état, cumuler les probabilités dans cet ordre, puis prendre les sauts de $\varphi$ sur ces cumuls. [L4 slide 26]

## Cesse d'être valide quand
Un poids calculé pour un actif ou un portefeuille ne se réutilise pas après un changement de rang des paiements : ce n'est pas une croyance fixe sur les états, et c'est ce qui oblige à évaluer la distribution de la richesse totale. [L4 slide 17]

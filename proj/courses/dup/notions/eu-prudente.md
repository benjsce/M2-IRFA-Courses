---
id: dup/eu-prudente
nom: Utilité espérée prudente
symbole: $\mathcal{U}$
type: notion
statut: source
cas_de: dup/axiome-independance
valeur: une invariance de mélange à sens unique, face au certain
construite_a_partir_de:
- dup/equivalent-certain
- dup/effet-certitude
alias:
- cautious EU
- indépendance de certitude négative
- NCI
refs:
- L3 slide 15
- L3 slide 16
---

## Ce que c'est
L’agent envisage plusieurs fonctions d’utilité et retient, pour chaque loterie, le plus bas des équivalents certains. [L3 slide 16]

## Forme
$$c(P,u)=u^{-1}\Big(\sum_i p_iu(x_i)\Big),\qquad V(P)=\inf_{u\in\mathcal{U}}c(P,u)$$ [L3 slide 16]

## Ce qui la définit
L’axiome est l’indépendance de certitude négative : si un risqué bat un sûr, ajouter du risque commun ne peut pas renverser ce classement. La comparaison inverse, elle, reste libre. [L3 slide 15]

Pour un résultat sûr, toutes les évaluations coïncident : $c(\delta_x,u)=x$. Élargir $\mathcal{U}$ ne peut qu’abaisser $V(P)$ et laisse les résultats sûrs inchangés — d’où l’effet de certitude. [L3 slide 16]

## Le chemin jusqu'ici
Depuis dup/utilite-esperee, que définissent dup/loterie et dup/fonction-utilite, deux fils se séparent. L'un mène à dup/equivalent-certain, qui donne de quoi comparer les loteries ; l'autre à dup/effet-consequence-commune puis à dup/effet-certitude, qui donnent ce qu'il faut expliquer. [ajout]

L'agent prudent envisage plusieurs utilités et retient le plus bas équivalent certain. La construction est donc un minimum sur une famille — exactement la même forme que l'utilité espérée maxmin, mais sur les goûts au lieu des croyances. Le socle le montre : cette fiche vient du côté du risque, l'autre du côté de l'ambiguïté. [ajout]

## Exemple minimal
$\mathcal{U}$ réduit à un singleton redonne exactement l’utilité espérée. [L3 slide 16]

## Geste de calcul type
Calculer l’équivalent certain sous chaque $u$ envisagée, prendre le plus petit, puis classer les loteries par ces minima. [L3 slide 16]

## Cesse d'être valide quand
L’asymétrie est assumée : $\delta_x\succ P$ peut coexister avec $\lambda P+(1-\lambda)R\succ\lambda\delta_x+(1-\lambda)R$. Retirer la certitude peut renverser le choix. [L3 slide 15]

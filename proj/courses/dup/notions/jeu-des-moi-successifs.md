---
id: dup/jeu-des-moi-successifs
nom: Jeu entre les moi successifs
symbole: '$T$, $U_t$, $MRS^t_{t,t+1}$'
type: notion
statut: source
construite_a_partir_de:
- dup/sophistication
alias:
- consumption game
- jeu de consommation
- équilibre parfait en sous-jeux
- SPNE
refs:
- L5 slide 45
---

## Ce que c'est
Chaque période est un joueur, le moi de cette date, et les choix de consommation sont l'équilibre parfait en sous-jeux de leur jeu. [L5 slide 45]

## Forme
$$U_t=u(c_t)+\beta\sum_{\tau=t+1}^{T}\delta^{\tau-t}u(c_\tau)$$ [L5 slide 45]
$$MRS^t_{t,t+1}=\beta\delta\,\frac{u'(c_{t+1})}{u'(c_t)},\qquad MRS^t_{t+1,t+2}=\delta\,\frac{u'(c_{t+2})}{u'(c_{t+1})}$$ [L5 slide 45]

## Ce que les symboles modélisent
$T$ est le nombre de périodes, donc de joueurs. $U_t$ est l'objectif du moi $t$ : il pèse 1 son présent et $\beta\delta^{\tau-t}$ chaque date suivante. $MRS^t_{t,t+1}$ est le taux auquel le moi $t$ échange de la consommation de $t$ contre celle de $t+1$ ; l'exposant dit quel moi juge, les indices entre quelles dates. [L5 slide 45]

## Ce qui la définit
Le moi $t$ arbitre entre $t+1$ et $t+2$ au taux $\delta$ ; le moi $t+1$, pour qui $t+1$ est le présent, au taux $\beta\delta$. Ils ne s'accordent pas, et c'est pourquoi le problème est un jeu et non un programme. [L5 slide 45]

Avec un horizon fini, l'équilibre se trouve par récurrence à rebours. L'horizon compte : à horizon infini, les équilibres parfaits sont nombreux, comme dans un jeu répété, et l'on retient ceux qui ne dépendent que de l'état, dits markoviens ; admettre une dépendance à l'histoire donne des règles personnelles, qui peuvent mener à des trappes de pauvreté. [L5 slide 45]

## Le chemin jusqu'ici
dup/sophistication fournit la méthode : chaque moi prévoit ce que feront les suivants, et l'on résout à rebours. Le jeu en est la forme générale, à $T$ joueurs, avec les poids de dup/actualisation-quasi-hyperbolique pour chacun. [L5 slide 25, L5 slide 45]

Le désaccord entre deux moi voisins est dup/coherence-dynamique qui tombe sous dup/biais-pour-le-present, alors que dup/invariance-temporelle tient, dup/stationnarite étant violée par les choix de dup/inversion-des-preferences-dans-le-temps. Tous les moi partagent la même dup/utilite-actualisee, qui généralise dup/actualisation-exponentielle, et les mêmes utilités de dup/fonction-utilite. [L5 slide 21, L5 slide 45]

## Exemple minimal
Avec $u=\ln$, $\beta=\tfrac12$ et $\delta=1$, le moi 1 veut autant consommer en période 2 qu'en période 3 ; le moi 2 veut consommer deux fois plus en 2 qu'en 3. [ajout]

## Geste de calcul type
Écrire l'objectif du dernier moi, en déduire sa règle, la reporter dans l'objectif de l'avant-dernier, et remonter. [L5 slide 45]

## Cesse d'être valide quand
L'horizon est infini et l'on ne restreint pas les stratégies : la récurrence n'a plus de point de départ, et l'équilibre n'est plus unique. [L5 slide 45]

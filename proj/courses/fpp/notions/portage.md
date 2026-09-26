---
id: fpp/portage
nom: Portage
symbole: $\Phi$
type: notion
statut: source
construite_a_partir_de: []
alias:
- cost of carry
- carry
refs:
- §3.2
- §5.2.1
---

## Ce que c'est
La part du prix comptant qui paie le sous-jacent livré à l'échéance, une fois retiré ce que son détenteur touche d'ici là. [§3.2]

## Forme
$$\Phi=1-\sum_i d_i$$ [§3.2]

## Ce que les symboles modélisent
$\Phi$ est un facteur et non un montant : il prend le comptant $S_t$ et rend, en le multipliant, le prix aujourd'hui de l'action livrée en $T$ sans ses dividendes. Il vaut un quand le sous-jacent ne verse rien. C'est une lettre du dépôt ; le poly n'écrit que le résultat, $1-\sum_i d_i$. [§3.2, ajout]

$d_i$ est le dividende versé à la date $T_i$, exprimé en proportion : le poly le fixe à $d_iS_t/P(t,T_i)$, un montant connu dès aujourd'hui, qui vaut donc $d_iS_t$ en $t$. $q$ est un dividende versé en continu, comme un rendement par an, sur la durée $\tau=T-t$ ; le poly l'écrit $d$ au §5.2.1 et $q$ au §6.4. [§3.2, §5.2.1, §6.4]

$D_i$ est un dividende donné en montant, et non en proportion ; il ne sert qu'au cas particulier de la fin de la fiche. [ajout]

## Retrouver la formule
![Le détenteur d'une action reçoit un dividende en $T_1$, puis l'action en $T$. Ramenées en $t$, ces deux choses font le comptant, 100, connu. Le dividende, 2 % de la valeur, vaut 2 aujourd'hui, connu lui aussi. Le trou est la valeur aujourd'hui de l'action livrée en $T$ : ce qui reste, 98. Le portage est cette part, 0,98.](figures/portage.svg) [ajout]

Détenir une action de $t$ à $T$, c'est recevoir deux choses : le dividende en $T_1$, puis l'action elle-même en $T$. Ensemble, elles valent ce que coûte l'action aujourd'hui, le comptant $S_t=100$, **connu**. [ajout]

Le dividende est **connu** lui aussi. Le poly le fixe à $d_1S_t/P(t,T_1)$, payé en $T_1$ ; ramené en $t$ par le zéro-coupon de sa date, il vaut $d_1S_t$, soit $2\,\%\times100=2$. [§3.2]

Reste ce qu'on cherche, **le trou** : la valeur aujourd'hui de l'action livrée en $T$, sans son dividende. C'est ce qui reste du comptant, $100-2=98$. Le poly le dit ainsi : les dividendes touchés en route réduisent d'autant ce qu'il faut financer. [§3.2]

Rapportée au comptant, cette part est le portage : $\Phi=98/100=0{,}98$. Avec plusieurs dividendes, on retire chacun, ramené en $t$ : $d_1S_t$, $d_2S_t$, et ainsi de suite. [ajout]

$$\Phi\,S_t=S_t-\sum_i d_iS_t\quad\Longleftrightarrow\quad\Phi=1-\sum_i d_i$$ [§3.2]

## Ce qui la définit
Un sous-jacent qui verse quelque chose pendant qu'on le détient coûte moins cher à porter jusqu'à l'échéance : le portage retire du comptant ce que le détenteur touchera d'ici là. [§3.2, §5.2.1]

Comme $\Phi S_t$ est aussi le prix au comptant de $\Phi$ action, on lit $\Phi$ comme la fraction d'action à détenir aujourd'hui pour en avoir une à l'échéance. La lecture est exacte pour un rendement continu réinvesti en actions : $e^{-q\tau}$ action, grossie au rythme $q$, fait une action en $T$. [ajout]

## Exemple minimal
Une action qui vaut 100 verse avant l'échéance un dividende de 2 % de sa valeur : son portage vaut 0,98. [ajout]

## Geste de calcul type
Un moins la somme des dividendes en proportion : $1-0{,}02=0{,}98$. Pour un rendement continu de 2 % sur un an, $e^{-0{,}02}=0{,}9802$ : presque le même nombre. [ajout]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| ce que verse le sous-jacent | rien | $\Phi=1$ |
| ce que verse le sous-jacent | dividendes proportionnels aux dates $T_i$ | $\Phi=1-\sum_i d_i$ |
| ce que verse le sous-jacent | rendement continu $q$ | $\Phi=e^{-q\tau}$ |
| ce que verse le sous-jacent | taux d'intérêt de la devise livrée | $\Phi$ = le zéro-coupon de cette devise ; au §2.4, où l'on livre la devise locale, $P(t,T)$ |
[§3.2, §5.2.1, §2.4]

## Cesse d'être valide quand
Les dividendes sont donnés en montants $D_i$ et non en proportions : on retire toujours du comptant chacun, ramené en $t$, $\Phi S_t=S_t-\sum_i D_iP(t,T_i)$, mais $\Phi$ dépend alors du prix du jour et des dates de versement. $D_i$ est un montant, à ne pas confondre avec le facteur $D$ du prix à terme. [ajout]

## Origine
- exercices fpp/ex-01 (c) et fpp/ex-02 (c)(d) : un dividende « en pourcentage de la valeur de l'action à cette date » ne fixe pas la convention. $\Phi=1-d$ (cours, §3.2) donne 79,73 et 59,97 ; $\Phi=1/(1+d)$, un dividende réinvesti en actions, donne 79,86 et 59,59, les réponses du corrigé. Le livre d'exercices tient la seconde convention d'un exercice à l'autre [exo. 1, exo. 2, ajout]
- exercice fpp/ex-05 : un dividende versé juste avant l'échéance ne s'actualise pas ; sa date n'entre pas dans le calcul, au contraire d'un montant versé en cours de vie [exo. 5]
- exercice fpp/ex-07 : un future ne coûte rien à porter, ce qui s'écrit $\Phi=e^{-r\tau}$ ; c'est le sens du « dividende = taux » du corrigé [exo. 7]
- exercice fpp/ex-08 : avec un dividende en montant, le retirer du comptant **avant** d'entrer dans la formule, jamais après [ajout]
- exercice fpp/ex-13 : la devise étrangère y est le sous-jacent livré, et son zéro-coupon fait le portage, $\Phi=e^{-r_f\tau}$ ; c'est la même règle que dans la table, dans la convention inverse de celle du poly [exo. 13]

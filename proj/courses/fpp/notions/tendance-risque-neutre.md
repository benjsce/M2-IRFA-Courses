---
id: fpp/tendance-risque-neutre
nom: Tendance risque-neutre
symbole: $\mu$
type: notion
statut: source
construite_a_partir_de:
- fpp/probabilite-risque-neutre
- fpp/taux-de-dividende
alias:
- risk neutral trend
- dérive risque-neutre
- risk neutral drift
refs:
- §5.2
- §5.2.1
- §5.2.2
- exo. 14
---

## Ce que c'est
Sous la probabilité risque-neutre, un actif croît en moyenne au taux sans risque diminué de ce qu'il verse, quelle que soit sa tendance réelle. [§5.2.1]

## Forme
$$\mu=r-d\qquad\Longleftrightarrow\qquad E^{\mathbb Q}(S_t)=S_0\,e^{(r-d)t}$$ [§5.2.1]

## Ce que les symboles modélisent
$\mu$ est la tendance du prix, par an. Sous la probabilité historique, c'est ce que les investisseurs attendent et elle vaut ce qu'elle vaut ; sous $\mathbb Q$, elle n'a plus le choix et vaut $r-d$. Le poly emploie la même lettre dans les deux cas : il faut lire sous quelle probabilité on se place. [§3.1, §5.2.1, §5.4]

## Retrouver la formule
Détenir l'action rapporte deux choses : sa valeur finale et, en chemin, un dividende continu $d\,S_s$. Sous $\mathbb Q$, le prix d'aujourd'hui est l'espérance actualisée de ces deux flux. [§5.2.1]

Si le prix croît en moyenne au taux $\mu$, cela donne $S_0=S_0\Big(\frac{d}{\mu-r}\big(e^{(\mu-r)t}-1\big)+e^{(\mu-r)t}\Big)$. [§5.2.1]

Cette égalité doit tenir pour toute durée $t$. Elle se réécrit $\big(1+\frac{d}{\mu-r}\big)\big(e^{(\mu-r)t}-1\big)=0$ : pour que ce soit vrai quel que soit $t$, il faut que la première parenthèse soit nulle, $\frac{d}{\mu-r}=-1$. Avec $r=4\,\%$ et $d=2\,\%$, cela donne $\mu=2\,\%$ : [§5.2.1, ajout]

$$\mu=r-d$$ [§5.2.1]

## Ce qui la définit
Ce qui est **connu** : le taux et le dividende. Ce qu'on **cherche** : la tendance à donner au prix pour calculer des prix. La tendance réelle n'y entre pas : sous $\mathbb Q$, l'espérance d'un actif est son prix forward, et c'est ce prix qui fixe la tendance. [§5.2.1, Prop. 6]

Pour une devise, le poly trouve de même que l'espérance risque-neutre du change est le change à terme, et sa tendance l'écart entre le taux étranger et le taux local. Le livre d'exercices ajoute que le prix forward d'une action, lui, n'a aucune tendance sous $\mathbb Q$ : il y est une martingale. [§5.2.2, exo. 14]

![Trois trajectoires moyennes de l'action à 100. Sous la probabilité historique, elle monte à 8 % ; sous la probabilité risque-neutre, à 4 % sans dividende, à 2 % avec un dividende de 2 %. Seules les deux dernières servent à calculer des prix.](figures/tendance-risque-neutre.svg) [ajout]

## Le chemin jusqu'ici
fpp/probabilite-risque-neutre impose que l'espérance d'un actif soit son prix forward ; fpp/taux-de-dividende dit ce que l'actif verse en route, et fpp/dividendes-intermediaires en était la version datée. [ajout]

Le prix forward vient de fpp/prix-forward, donc de fpp/cash-and-carry, d'un emprunt évalué par fpp/zero-coupon et de fpp/absence-d-arbitrage ; l'actualisation des flux en chemin est celle de fpp/valeur-actuelle-nette, écrite dans la convention continue de fpp/capitalisation. [ajout]

## Exemple minimal
$r=4\,\%$, $d=2\,\%$ : sous $\mathbb Q$, l'action à 100 vaut en moyenne $100\,e^{0,02}=102{,}02$ dans un an, qu'on attende 8 % ou 20 % de hausse. [ajout]

## Geste de calcul type
Pour écrire un modèle sous $\mathbb Q$, remplacer la tendance réelle par $r-d$ ; pour une devise, par l'écart des deux taux, dans la convention de change qu'on emploie. [§5.2.1, §5.2.2]

## Cesse d'être valide quand
Le calcul suppose $r$ et $d$ constants. La tendance est une affirmation sur une moyenne : elle ne dit rien de la dispersion autour d'elle. [§5.2.1, ajout]

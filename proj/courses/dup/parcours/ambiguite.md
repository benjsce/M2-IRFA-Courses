---
id: dup/parcours-ambiguite
ordre: 6
titre: Quand on ne connaît même pas les probabilités
source: L1 slides 59–64, L4 slides 35–62
---

## Point de départ
Une urne contient 30 boules rouges et 60 boules noires ou jaunes, en proportion inconnue. La plupart des gens préfèrent parier sur le rouge plutôt que sur le noir, puis sur le noir-ou-jaune plutôt que sur le rouge-ou-jaune. [L1 slide 62]

Aucune probabilité ne rend compte de ces deux choix à la fois. Ce parcours suit ce que le cours en tire : la croyance d'un agent n'est pas toujours une probabilité, et cela se voit jusque sur les marchés. [ajout]

## À savoir avant
- dup/acte : c'est l'objet de tous les choix de ce parcours. Parier sur le rouge est un acte : il paie selon la couleur tirée, et aucune probabilité n'est donnée avec lui. [L1 slide 2]
- dup/loterie : c'est le hasard dont on connaît les probabilités, celui des boules rouges. Tout le parcours oppose ce hasard-là à celui des boules noires et jaunes, dont on ignore la proportion. [L1 slide 2]
- dup/fonction-utilite : elle traduit les gains en utilité, et c'est elle qui porte l'aversion au risque. Ici elle ne change jamais : toute l'histoire se joue du côté de la croyance, pas du côté des goûts. [ajout]

## Étapes
1. dup/separation-gouts-croyances
   Pour voir ce que l'urne met en cause, il faut d'abord savoir comment la théorie découpe une décision, et où elle range ce que l'agent croit. [ajout]
   Histoire : « en proportion inconnue » — Parier sur une couleur engage deux choses : ce qu'on aime, le gain, et ce qu'on croit, la chance de tirer cette couleur. La théorie range ces deux ingrédients séparément ; l'urne ne touche qu'au second, puisque le gain est le même d'un pari à l'autre. [ajout]

2. dup/utilite-esperee-subjective
   Chez Savage, la croyance n'est pas donnée : elle se déduit des choix, et elle prend la forme d'une probabilité unique. [L1 slide 59]
   Histoire : « préfèrent parier sur le rouge plutôt que sur le noir » — Chez Savage, ce choix révèle une croyance : préférer le rouge, c'est donner au noir une probabilité $\pi(N)$ plus petite que celle du rouge, un tiers. [ajout]

3. dup/principe-de-la-chose-sure
   L'axiome qui fait de la croyance une probabilité est l'analogue subjectif de l'indépendance : ce que deux actes donnent en commun ne compte pas dans leur comparaison. [L1 slide 60]
   Histoire : « puis sur le noir-ou-jaune plutôt que sur le rouge-ou-jaune » — Les deux paris de cette seconde paire ne diffèrent des deux premiers que par le jaune, ajouté des deux côtés. Le principe dit que ce qu'ils donnent en commun, gagner si la boule est jaune, ne doit pas compter dans la comparaison. [ajout]

4. dup/paradoxe-d-ellsberg
   L'urne du départ montre les choix que ce principe interdit : la colonne jaune, commune aux deux actes de chaque paire, devrait s'annuler, et pourtant le choix s'inverse quand on l'ajoute. [L1 slide 63]
   Histoire : « Aucune probabilité ne rend compte de ces deux choix à la fois » — Avec $R$, $N$ et $J$ pour rouge, noir et jaune, le premier choix exige $\pi(R)>\pi(N)$ ; le second exige $\pi(N)+\pi(J)>\pi(R)+\pi(J)$, donc $\pi(N)>\pi(R)$. Les deux ne peuvent pas tenir ensemble. [ajout]

5. dup/aversion-a-l-ambiguite
   Ce que les gens fuient ici n'est pas la dispersion du gain, c'est l'imprécision de la probabilité. Il faut donc un concept distinct de l'aversion au risque. [L1 slide 63]
   Histoire : « 30 boules rouges et 60 boules noires ou jaunes » — Le rouge a une chance connue, un tiers ; le noir, une chance qui peut aller de 0 à deux tiers. Les deux paris gagnent ou perdent la même somme : ce que les gens fuient, ce n'est pas le risque, c'est l'imprécision de la chance. [ajout]

6. dup/reponse-a-l-ambiguite
   Le cours renonce à la probabilité unique et propose deux façons de la remplacer. Les étapes suivantes prennent la première, puis la seconde, puis montrent où elles se rejoignent. [L1 slide 64]
   Histoire : « la croyance d'un agent n'est pas toujours une probabilité » — Le cours en tire la conséquence : il remplace la probabilité unique, soit par un ensemble de probabilités, soit par une mesure dont les poids ne s'ajoutent pas. [ajout]

7. dup/cadre-anscombe-aumann
   Pour dire exactement quelle part de l'indépendance on garde, il faut pouvoir mélanger deux actes, ce que le cadre de Savage ne permet pas. Le quatrième cours change donc de cadre. [ajout]
   Suite : Un joueur peut aussi lancer une pièce avant de parier : sur pile, il parie sur le noir ; sur face, sur le jaune. Ce mélange de deux paris est-il encore un pari au sens de Savage ? [ajout]
   Histoire : « Ce mélange de deux paris est-il encore un pari au sens de Savage » — Non : chez Savage, un acte donne un résultat par couleur. Ici, si la boule est noire, on gagne sur pile seulement : le résultat est lui-même une loterie. Le cadre d'Anscombe et Aumann donne à chaque couleur une loterie, et permet ainsi de mélanger deux actes couleur par couleur. [ajout]

8. dup/independance-restreinte
   Dans ce cadre, un mélange de deux paris peut couvrir l'ambiguïté. [L4 slide 45, L4 slide 59]
   Suite : Pour admettre les choix de l'urne, faut-il jeter l'axiome d'indépendance ? [ajout]
   Histoire : « faut-il jeter l'axiome d'indépendance » — Non. Le mélange du noir et du jaune efface l'ambiguïté : quand la boule n'est pas rouge, on gagne une fois sur deux, quelle que soit la composition. Les deux voies gardent donc l'indépendance, mais seulement pour des mélanges qui ne peuvent pas couvrir ainsi l'ambiguïté. [ajout]

9. dup/ensemble-de-priors
   Première voie : la croyance devient un ensemble de probabilités plausibles, sans qu'aucune soit jugée plus crédible que les autres. [L4 slide 40]
   Histoire : « 60 boules noires ou jaunes, en proportion inconnue » — La croyance devient l'ensemble des compositions possibles : $\pi(R)=\tfrac13$, et $\pi(N)$ n'importe où entre 0 et $\tfrac23$, sans qu'aucune soit jugée plus crédible que les autres. [ajout]

10. dup/independance-de-certitude
   Quel axiome faut-il affaiblir pour qu'une croyance puisse être un ensemble ? Pas l'indépendance entière, seulement la partie qui interdisait de se couvrir contre l'ambiguïté. [L4 slide 45]
   Histoire : « Ce mélange de deux paris » — L'axiome n'exige plus l'indépendance que pour un mélange avec un gain certain, qui n'ajoute ni n'ôte d'ambiguïté. Le mélange du noir et du jaune n'y est plus soumis : il peut valoir plus que chacun des deux paris. [ajout]

11. dup/maxmin-eu
    Reste à dire comment on juge un acte quand on hésite entre plusieurs probabilités. Le cours retient la plus pessimiste pour cet acte-là. [L1 slide 64, L4 slide 38]
    Histoire : « parier sur le rouge plutôt que sur le noir » — Le pari sur le noir est jugé sous la composition la pire pour lui, $\pi(N)=0$ : il ne gagne jamais, moins que le rouge et son tiers. Le noir-ou-jaune gagne toujours avec deux tiers ; le rouge-ou-jaune peut descendre à un tiers, et il est jugé là. Les deux choix de l'histoire deviennent cohérents. [ajout]

12. dup/couverture-de-l-ambiguite
    Ce critère a une conséquence qu'une probabilité unique n'a jamais : la valeur d'un ensemble de paris n'est plus la somme des valeurs de chaque pari. [L4 slide 41]
    Histoire : « sur pile, il parie sur le noir ; sur face, sur le jaune » — Jugés chacun sous leur pire composition, le pari sur le noir et le pari sur le jaune ne gagnent jamais. Leur mélange gagne avec une chance de $\tfrac12\times\tfrac23=\tfrac13$ quelle que soit la composition : il vaut plus que chacun des deux. [ajout]

13. dup/capacite
    Seconde voie : au lieu de multiplier les probabilités, on n'en garde qu'une, mais on renonce à ce qu'elle soit additive. [L4 slide 56]
    Histoire : « noir-ou-jaune » — Seconde voie : une seule mesure, mais dont les poids ne s'ajoutent pas. On peut donner un tiers au rouge, un sixième au noir et un sixième au jaune, mais deux tiers au noir-ou-jaune et la moitié au rouge-ou-jaune. Avec ces poids, le rouge bat le noir et le noir-ou-jaune bat le rouge-ou-jaune : ce sont les deux choix de l'histoire. [ajout]

14. dup/integrale-de-choquet
    Une mesure qui n'est pas additive demande une autre façon de faire la moyenne : on range les états du pire au meilleur, et chaque marche se paie au poids de l'événement où on la franchit. [L4 slide 57]
    Suite : Un acte paie désormais selon la couleur : 0 si la boule est rouge, 50 si elle est noire, 100 si elle est jaune. Comment le juger avec des poids qui ne s'ajoutent pas ? [ajout]
    Histoire : « Comment le juger avec des poids qui ne s'ajoutent pas » — On range les couleurs du pire au meilleur, et chaque marche se paie au poids de l'événement où on la franchit : on a au moins 50 sur le noir-ou-jaune, de poids $\tfrac23$, et 50 de plus sur le jaune, de poids $\tfrac16$. L'acte vaut $\tfrac23\times50+\tfrac16\times50\approx41{,}7$. [ajout]

15. dup/independance-comonotone
    La seconde voie a elle aussi son axiome. [L4 slide 59]
    Suite : Entre quels actes l'indépendance peut-elle encore être exigée sans rien coûter ? [ajout]
    Histoire : « Entre quels actes l'indépendance peut-elle encore être exigée » — Entre actes qui classent toujours les couleurs dans le même ordre, et qui ne se couvrent donc pas l'un l'autre. Le pari sur le rouge et le pari sur le noir classent les couleurs en sens opposés : les mélanger couvre une part de l'ambiguïté, et l'axiome ne leur impose rien. [ajout]

16. dup/ceu
    Schmeidler montre que cet axiome suffit : la préférence s'écrit comme une intégrale de Choquet. Et quand la capacité est convexe, le modèle se relit comme un maxmin : les deux voies se rejoignent. [L4 slide 60]
    Histoire : « des poids qui ne s'ajoutent pas » — Les poids de l'histoire forment une capacité convexe : une réunion d'événements pèse au moins la somme de ses morceaux, comme le noir-ou-jaune, deux tiers contre un sixième plus un sixième. Juger par l'intégrale de Choquet revient alors à juger par le maxmin, sur l'ensemble des probabilités qui donnent à chaque événement au moins son poids : ici $\pi(R)=\tfrac13$ et $\pi(N)$ entre $\tfrac16$ et $\tfrac12$. L'acte qui paie 0, 50 ou 100 y vaut au pire 41,7, sous $\pi(N)=\tfrac12$, comme par l'intégrale : les deux voies se rejoignent. [ajout]

17. dup/intervalle-de-non-echange
    Face à un actif qu'on peut acheter ou vendre à découvert, cet agent n'évalue pas les deux sens de la même façon, parce que le pire état change avec le sens de la position. [L4 slide 62]
    Suite : Un marché permet d'acheter, ou de vendre à découvert, au prix $p$, un titre qui paie 100 si la boule est noire et rien sinon. À quel prix l'agent aux poids qui ne s'ajoutent pas, celui qui donne un sixième au noir, l'achète-t-il, et à quel prix le vend-il ? [ajout]
    Histoire : « À quel prix l'agent aux poids qui ne s'ajoutent pas, celui qui donne un sixième au noir, l'achète-t-il » — Il juge comme un maxmin sur les compositions où $\pi(N)$ va de $\tfrac16$ à $\tfrac12$. Acheté, le titre est jugé sous la composition la pire pour l'acheteur, $\pi(N)=\tfrac16$ : il vaut environ 16,7. Vendu, il est jugé sous la pire pour le vendeur, $\pi(N)=\tfrac12$, où il paie une fois sur deux : il coûte 50. Entre 16,7 et 50, l'agent n'achète ni ne vend. [ajout]

## Point d'arrivée
L'ambiguïté ne change pas seulement des choix de laboratoire : elle crée des prix auxquels l'agent n'achète ni ne vend, ce qu'une probabilité unique ne produit jamais. [ajout]

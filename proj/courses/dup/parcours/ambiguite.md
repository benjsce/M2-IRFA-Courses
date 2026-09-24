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

2. dup/utilite-esperee-subjective
   Chez Savage, la croyance n'est pas donnée : elle se déduit des choix, et elle prend la forme d'une probabilité unique. [L1 slide 59]

3. dup/principe-de-la-chose-sure
   L'axiome qui fait de la croyance une probabilité est l'analogue subjectif de l'indépendance : ce que deux actes donnent en commun ne compte pas dans leur comparaison. [L1 slide 60]

4. dup/paradoxe-d-ellsberg
   L'urne du départ montre les choix que ce principe interdit : la colonne jaune, commune aux deux actes de chaque paire, devrait s'annuler, et pourtant le choix s'inverse quand on l'ajoute. [L1 slide 63]

5. dup/aversion-a-l-ambiguite
   Ce que les gens fuient ici n'est pas la dispersion du gain, c'est l'imprécision de la probabilité. Il faut donc un concept distinct de l'aversion au risque. [L1 slide 63]

6. dup/reponse-a-l-ambiguite
   Le cours renonce à la probabilité unique et propose deux façons de la remplacer. Les étapes suivantes prennent la première, puis la seconde, puis montrent où elles se rejoignent. [L1 slide 64]

7. dup/cadre-anscombe-aumann
   Pour dire exactement quelle part de l'indépendance on garde, il faut pouvoir mélanger deux actes, ce que le cadre de Savage ne permet pas. Le quatrième cours change donc de cadre. [ajout]

8. dup/independance-restreinte
   Les deux voies ne jettent pas l'indépendance : elles la gardent, en restreignant seulement les mélanges auxquels elle s'applique. [L4 slide 45, L4 slide 59]

9. dup/ensemble-de-priors
   Première voie : la croyance devient un ensemble de probabilités plausibles, sans qu'aucune soit jugée plus crédible que les autres. [L4 slide 40]

10. dup/independance-de-certitude
   Quel axiome faut-il affaiblir pour qu'une croyance puisse être un ensemble ? Pas l'indépendance entière, seulement la partie qui interdisait de se couvrir contre l'ambiguïté. [L4 slide 45]

11. dup/maxmin-eu
    Reste à dire comment on juge un acte quand on hésite entre plusieurs probabilités. Le cours retient la plus pessimiste pour cet acte-là. [L1 slide 64, L4 slide 38]

12. dup/couverture-de-l-ambiguite
    Ce critère a une conséquence qu'une probabilité unique n'a jamais : la valeur d'un ensemble de paris n'est plus la somme des valeurs de chaque pari. [L4 slide 41]

13. dup/capacite
    Seconde voie : au lieu de multiplier les probabilités, on n'en garde qu'une, mais on renonce à ce qu'elle soit additive. [L4 slide 56]

14. dup/integrale-de-choquet
    Une mesure qui n'est pas additive demande une autre façon de faire la moyenne : on range les états du pire au meilleur, et chaque marche se paie au poids de l'événement où on la franchit. [L4 slide 57]

15. dup/independance-comonotone
    L'axiome correspondant n'exige l'indépendance qu'entre actes qui ne se couvrent pas l'un l'autre, là où elle ne coûte rien. [L4 slide 59]

16. dup/ceu
    Schmeidler montre que cet axiome suffit : la préférence s'écrit comme une intégrale de Choquet. Et quand la capacité est convexe, le modèle se relit comme un maxmin : les deux voies se rejoignent. [L4 slide 60]

17. dup/intervalle-de-non-echange
    Que fait cet agent face à un actif qu'il peut acheter ou vendre à découvert ? Son évaluation n'est pas la même dans les deux sens, parce que le pire état change avec le sens de la position. [L4 slide 62]

## Point d'arrivée
L'ambiguïté ne change pas seulement des choix de laboratoire : elle crée des prix auxquels l'agent n'achète ni ne vend, ce qu'une probabilité unique ne produit jamais. [ajout]

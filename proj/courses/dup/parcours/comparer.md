---
id: dup/parcours-comparer
ordre: 2
titre: Dire qu'un risque est plus grand qu'un autre
source: L1 slides 6–28
---

## Point de départ
Deux placements ont la même moyenne de 50 : le pari $(0,\tfrac12;100,\tfrac12)$, d'écart type 50, et le pari $(25,\tfrac12;75,\tfrac12)$, d'écart type 25. Lequel est le plus risqué ? La réponse la plus courante, « celui dont l'écart type est le plus grand », est aussi celle que le cours met en doute. [ajout]

## À savoir avant
- dup/loterie : c'est l'objet que l'on compare tout au long du parcours, un pari dont les probabilités sont connues. [L1 slide 2]
- dup/fonction-utilite : elle apparaît quand on cherche le cas où moyenne et écart type suffisent vraiment, qui dépend d'une forme précise de l'utilité. [L1 slide 14]
- dup/utilite-esperee : c'est le juge de toutes les comparaisons. Un risque est plus grand qu'un autre si des agents qui évaluent les paris par l'utilité espérée le jugent ainsi. [L1 slide 6]
- dup/aversion-au-risque : c'est la classe d'agents dont on demande l'accord unanime dans la seconde moitié du parcours. [L1 slide 19]

## Étapes
1. dup/moyenne-variance
   La première idée, la plus répandue en finance, consiste à ne garder de chaque pari que ce qu'il rapporte en moyenne et combien il s'en écarte. [L1 slide 11]
   Histoire : « celui dont l'écart type est le plus grand » — Cette réponse résume chaque pari par deux nombres : sa moyenne, 50 pour les deux, et son écart type, 50 pour le premier et 25 pour le second. C'est ce résumé que le cours examine d'abord. [ajout]

2. dup/frontiere-actif-sans-risque
   Ce résumé est commode pour composer un portefeuille : avec un actif sans risque, tout se joue sur une droite. [L1 slide 12]
   Suite : Un épargnant peut aussi mêler un placement sûr, qui rend 50 à coup sûr, au premier pari. Moitié de l'un, moitié de l'autre, il reçoit $\tfrac12\times0+25$ ou $\tfrac12\times100+25$, soit 25 ou 75 : exactement le second pari. Que devient le résumé quand on mêle ainsi du sûr et du risqué ? [ajout]
   Histoire : « Que devient le résumé quand on mêle ainsi du sûr et du risqué » — La moyenne reste 50 et l'écart type est divisé par deux, de 50 à 25. Ici le sûr et le risqué ont la même moyenne : chaque dosage donne un point d'une même droite, horizontale, où l'écart type va de 50 à 0 à mesure qu'on garde plus de sûr. [ajout]

3. dup/diversification
   Avec deux actifs risqués, le résumé révèle quelque chose que les écarts types pris un à un ne montrent pas. [L1 slide 13]
   Suite : Prenons maintenant deux paris comme le premier, tirés chacun à pile ou face, indépendamment, et misons la moitié sur chacun. On reçoit 0, 50 ou 100, avec les probabilités $\tfrac14$, $\tfrac12$, $\tfrac14$. Ce mélange est-il moins risqué que chacun des deux ? [ajout]
   Histoire : « Ce mélange est-il moins risqué que chacun des deux » — Son écart type vaut $50/\sqrt2\approx35{,}4$, au-dessous des 50 de chaque pari, et sa moyenne reste 50 : la covariance nulle entre les deux tirages l'abaisse, ce que les écarts types pris un à un ne montraient pas. [ajout]

4. dup/utilite-quadratique
   Mais quand ces deux nombres suffisent-ils vraiment à classer des paris ? La réponse est très restrictive. [L1 slide 14]
   Histoire : « Deux placements ont la même moyenne de 50 » — Pour qu'un agent classe ces deux paris par leurs seuls moyenne et écart type, il faut que son utilité soit de la forme $U(x)=\alpha x+\beta x^2$. Avec $\alpha=1$ et $\beta=-0{,}005$, le premier pari vaut 25 et le second environ 34,4 : il préfère celui d'écart type le plus faible. [ajout]

5. dup/principe-d-unanimite
   Faute de résumé fiable, le cours change de méthode : n'appeler « meilleur » ou « plus risqué » que ce dont tous les agents d'une classe conviennent. [L1 slide 18]
   Histoire : « est aussi celle que le cours met en doute » — Faute d'un résumé qui vaille pour tous les agents, le cours ne dira « meilleur » ou « plus risqué » que ce dont tous les agents d'une classe conviennent : non plus un nombre, mais un accord. [ajout]

6. dup/dominance-stochastique-ordre-1
   Première classe, la plus large : tous ceux qui préfèrent plus à moins. Ce qu'ils jugent tous meilleur a une forme simple. [L1 slide 6]
   Suite : Comparons maintenant le premier pari à un troisième, qui rapporte encore 0 ou 100, mais 100 avec une chance sur quatre seulement. Tous ceux qui préfèrent plus à moins le jugent-ils moins bon ? [ajout]
   Histoire : « Tous ceux qui préfèrent plus à moins » — Oui : on a seulement déplacé un quart de probabilité de 100 vers 0. Pour toute utilité croissante, $\tfrac34U(0)+\tfrac14U(100)<\tfrac12U(0)+\tfrac12U(100)$. [ajout]

7. dup/critique-de-borch
   Ce critère permet de prendre la moyenne et l'écart type en défaut : ils peuvent déclarer équivalents deux paris dont l'un est meilleur pour tous. [L1 slide 16]
   Suite : Un agent juge chaque pari par sa moyenne moins son écart type. On lui propose, à la place du premier pari, un pari qui rapporte 0 ou 200 à pile ou face. Lequel choisit-il ? [ajout]
   Histoire : « Lequel choisit-il » — Aucun : $50-50=0$ pour le premier, $100-100=0$ pour le nouveau, il les déclare équivalents. Or le nouveau paie autant sur face et le double sur pile : il domine le premier au premier ordre, et tout agent qui préfère plus à moins le prend. [ajout]

8. dup/entropie
   Et si l'on mesurait l'incertitude sans regarder l'agent du tout ? L'entropie essaie, et montre ce qu'on perd. [L1 slide 17]
   Suite : Un dernier pari rapporte 49 ou 51 à pile ou face. Peut-on dire qu'il est moins incertain que le premier sans rien savoir de l'agent ? [ajout]
   Histoire : « sans rien savoir de l'agent » — L'entropie essaie, en ne regardant que les probabilités. Elle vaut $\log 2$ pour les deux paris, qui ont chacun deux résultats à une chance sur deux : elle ne voit aucune différence entre 49 ou 51 et 0 ou 100. [ajout]

9. dup/accroissement-de-risque
   Seconde classe : tous les agents averses au risque. Ce sur quoi ils s'accordent définit enfin ce qu'est « plus risqué » à moyenne égale. [L1 slide 18]
   Histoire : « Lequel est le plus risqué » — Voici enfin la réponse du cours, à moyenne égale : le premier pari est plus risqué que le second si tous les agents averses au risque préfèrent le second. [ajout]

10. dup/etalement-preservant-la-moyenne
    Comment fabrique-t-on un pari plus risqué à partir d'un autre ? La façon la plus concrète est de déplacer de la probabilité. [L1 slide 21]
    Histoire : « le pari $(25,\tfrac12;75,\tfrac12)$, d'écart type 25 » — On passe de ce pari au premier en déplaçant de la probabilité du centre vers les extrêmes, de 25 et 75 vers 0 et 100, sans que la moyenne quitte 50 : le premier pari est un étalement du second. [ajout]

11. dup/bruit-equitable
    Une autre façon consiste à ajouter du hasard sans changer la moyenne. [L1 slide 20]
    Histoire : « le pari $(0,\tfrac12;100,\tfrac12)$, d'écart type 50 » — Il s'obtient aussi en ajoutant du hasard au second : quand celui-ci donne 25, on tire 0 avec trois chances sur quatre et 100 sinon ; quand il donne 75, l'inverse. Ce hasard est de moyenne nulle à chaque tirage, et le résultat est exactement le premier pari. [ajout]

12. dup/ordre-concave
    Une troisième part directement des préférences, et c'est elle qui justifie le mot « unanime ». [L1 slide 19]
    Histoire : « La réponse la plus courante » — Elle désignait le bon pari, mais pour une mauvaise raison. Le premier est plus risqué parce que tout agent averse au risque préfère le second — avec $\sqrt{x}$, environ 6,83 contre 5 —, et non parce que son écart type est plus grand. [ajout]

13. dup/condition-cdf-integree
    Il faut enfin un test que l'on puisse faire sur deux distributions données, sans chercher l'étalement ni le bruit. [L1 slide 22]
    Histoire : « la même moyenne de 50 » — Sur les deux paris, l'écart des aires sous les fonctions de répartition monte jusqu'à 12,5 en 25, y reste jusqu'à 75, puis redescend à 0 en 100 : positif partout, nul au bout, parce que les moyennes sont égales. Le test confirme que le premier est plus risqué. [ajout]

14. dup/statique-comparative-risque-accru
    Reste la question pratique : un agent qui investit, assure ou épargne doit-il en faire moins quand son risque grandit en ce sens ? [L1 slide 26]
    Suite : Un agent place une part $a$ de sa richesse dans un placement risqué. Si ce placement devient plus risqué au sens du parcours, sans changer de moyenne, doit-il en placer moins ? [ajout]
    Histoire : « doit-il en placer moins » — Pas forcément : ce n'est pas la concavité de son utilité qui décide, mais le signe de $U_{xxa}$. S'il est négatif, il en place moins ; s'il est positif, il en place plus. [ajout]

## Point d'arrivée
« Plus risqué » n'est pas « plus d'écart type » : c'est ce que tous les agents averses au risque rejettent, et Rothschild et Stiglitz montrent que plusieurs définitions concrètes en donnent la même chose. [L1 slide 23]

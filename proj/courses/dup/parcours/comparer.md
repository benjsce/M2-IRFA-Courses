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

2. dup/frontiere-actif-sans-risque
   Ce résumé est commode pour composer un portefeuille : avec un actif sans risque, tout se joue sur une droite. [L1 slide 12]

3. dup/diversification
   Avec deux actifs risqués, le résumé révèle quelque chose que les écarts types pris un à un ne montrent pas. [L1 slide 13]

4. dup/utilite-quadratique
   Mais quand ces deux nombres suffisent-ils vraiment à classer des paris ? La réponse est très restrictive. [L1 slide 14]

5. dup/principe-d-unanimite
   Faute de résumé fiable, le cours change de méthode : n'appeler « meilleur » ou « plus risqué » que ce dont tous les agents d'une classe conviennent. [L1 slide 18]

6. dup/dominance-stochastique-ordre-1
   Première classe, la plus large : tous ceux qui préfèrent plus à moins. Ce qu'ils jugent tous meilleur a une forme simple. [L1 slide 6]

7. dup/critique-de-borch
   Ce critère permet de prendre la moyenne et l'écart type en défaut : ils peuvent déclarer équivalents deux paris dont l'un est meilleur pour tous. [L1 slide 16]

8. dup/entropie
   Et si l'on mesurait l'incertitude sans regarder l'agent du tout ? L'entropie essaie, et montre ce qu'on perd. [L1 slide 17]

9. dup/accroissement-de-risque
   Seconde classe : tous les agents averses au risque. Ce sur quoi ils s'accordent définit enfin ce qu'est « plus risqué » à moyenne égale. [L1 slide 18]

10. dup/etalement-preservant-la-moyenne
    Comment fabrique-t-on un pari plus risqué à partir d'un autre ? La façon la plus concrète est de déplacer de la probabilité. [L1 slide 21]

11. dup/bruit-equitable
    Une autre façon consiste à ajouter du hasard sans changer la moyenne. [L1 slide 20]

12. dup/ordre-concave
    Une troisième part directement des préférences, et c'est elle qui justifie le mot « unanime ». [L1 slide 19]

13. dup/condition-cdf-integree
    Il faut enfin un test que l'on puisse faire sur deux distributions données, sans chercher l'étalement ni le bruit. [L1 slide 22]

14. dup/statique-comparative-risque-accru
    Reste la question pratique : un agent qui investit, assure ou épargne doit-il en faire moins quand son risque grandit en ce sens ? [L1 slide 26]

## Point d'arrivée
« Plus risqué » n'est pas « plus d'écart type » : c'est ce que tous les agents averses au risque rejettent, et Rothschild et Stiglitz montrent que plusieurs définitions concrètes en donnent la même chose. [L1 slide 23]

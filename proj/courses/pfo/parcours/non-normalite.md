---
id: pfo/parcours-non-normalite
ordre: 4
titre: Les rendements ne sont pas gaussiens
source: poly, §2.1–§2.4
---

## Point de départ
Le 19 octobre 1987, le Dow Jones perd 22,6 % en une séance. Sous une loi normale, c'est un écart de plus de vingt écarts types, qui n'aurait jamais dû arriver. [p. 19]

## À savoir avant
- fpp/volatilite : c'est l'unité de mesure de tout le parcours. Asymétrie et kurtosis rapportent les écarts à la moyenne à cet écart type, pour ne décrire que la forme de la loi. [§2.1.2]

## Étapes
1. pfo/marches-non-gaussiens
   Le chapitre part de ce constat, et en fait un principe dont tout le reste découle. [p. 19, §2.1]

2. pfo/fait-stylise
   En quoi, précisément, les rendements réels s'écartent-ils de la loi normale ? Mandelbrot et Fama en ont dressé la liste. [§2.1.1]

3. pfo/moment-standardise
   Pour passer du constat à la mesure, le cours va au-delà de la moyenne et de la variance. [§2.1.2]

4. pfo/coefficient-d-asymetrie
   Premier outil : une puissance impaire, qui garde le signe des écarts et voit donc de quel côté penche la loi. [§2.1.2, p. 21]

5. pfo/kurtosis
   Second outil : une puissance paire et élevée, qui efface le signe et grossit démesurément les écarts lointains. [§2.1.2, p. 22]

6. pfo/asymetrie-negative
   Avec le premier outil, un des faits stylisés devient un chiffre qu'on peut lire sur une série. [§2.1.1, p. 21]

7. pfo/queues-epaisses
   Avec le second, un autre fait stylisé devient mesurable, celui des krachs trop fréquents. [p. 23]

8. pfo/p-valeur
   Mesurer un écart ne suffit pas : sur un échantillon fini, une asymétrie non nulle peut venir du hasard. Il faut une règle de décision. [p. 25]

9. pfo/test-de-normalite
   Appliquée à la question du chapitre, cette règle demande une hypothèse précise à éprouver. [éq. 2.13, éq. 2.14]

10. pfo/test-de-jarque-bera
    Premier test : il réemploie directement les deux moments calculés aux étapes 4 et 5. [§2.3]

11. pfo/test-de-shapiro-wilk
    Second test : il regarde l'échantillon trié tout entier, et peut rejeter là où le premier ne voit rien. [§2.4, p. 31]

## Point d'arrivée
L'écart à la normale se nomme, se mesure et se teste. Reste à savoir ce qu'il change à la mesure du risque. [ajout]

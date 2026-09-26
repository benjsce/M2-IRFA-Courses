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
   Histoire : « qui n'aurait jamais dû arriver » — Sous une loi normale, une baisse de plus de vingt écarts types a une probabilité de l'ordre de $10^{-89}$ ; elle est pourtant arrivée. Le cours en fait un principe : les rendements réels ne sont pas gaussiens, et un modèle qui le suppose sous-estime les pertes extrêmes. [ajout]

2. pfo/fait-stylise
   En quoi, précisément, les rendements réels s'écartent-ils de la loi normale ? Mandelbrot et Fama en ont dressé la liste. [§2.1.1]
   Histoire : « Le 19 octobre 1987 » — Ce krach n'est pas isolé : les rendements réels ont des pertes extrêmes trop fréquentes, des baisses plus violentes que les hausses, des périodes agitées qui se suivent. Mandelbrot et Fama ont dressé la liste de ces régularités, que la loi normale ne reproduit pas. [ajout]

3. pfo/moment-standardise
   Pour passer du constat à la mesure, le cours va au-delà de la moyenne et de la variance. [§2.1.2]
   Suite : Prenons une petite série de rendements : −2 %, −1 %, 0 %, 1 %, 2 %, et un jour de krach à −10 %. Sa moyenne et son écart type suffisent-ils à dire ce que ce krach a d'anormal ? [ajout]
   Histoire : « suffisent-ils à dire ce que ce krach a d'anormal » — Non : ils disent où se trouve la série et combien elle s'étale, pas sa forme. Les moyennes des puissances 3 et 4 de l'écart réduit, $\big((r-\mu)/\sigma\big)^k$, regardent précisément les écarts lointains ; elles vaudraient 0 et 3 pour une loi normale. [ajout]

4. pfo/coefficient-d-asymetrie
   Premier outil : une puissance impaire, qui garde le signe des écarts et voit donc de quel côté penche la loi. [§2.1.2, p. 21]
   Histoire : « un jour de krach à −10 % » — Élevé au cube, l'écart réduit garde son signe : le −10 %, très loin sous la moyenne, pèse lourd et négatif. La série a un coefficient d'asymétrie de −1,37 ; sans ce jour, elle est symétrique et le coefficient est nul. [ajout]

5. pfo/kurtosis
   Second outil : une puissance paire et élevée, qui efface le signe et grossit démesurément les écarts lointains. [§2.1.2, p. 22]
   Histoire : « Prenons une petite série de rendements » — À la puissance quatre, le signe s'efface et les écarts lointains dominent : la kurtosis de la série vaut environ 3,49, au-dessus des 3 d'une loi normale. Sans le jour de krach, elle ne vaudrait que 1,7. [ajout]

6. pfo/asymetrie-negative
   Avec le premier outil, un des faits stylisés devient un chiffre qu'on peut lire sur une série. [§2.1.1, p. 21]
   Histoire : « le Dow Jones perd 22,6 % » — Les krachs sont des baisses, pas des hausses : la queue des pertes est plus longue que celle des gains. Sur la petite série, cela se lit au signe du coefficient d'asymétrie, −1,37. [ajout]

7. pfo/queues-epaisses
   Avec le second, un autre fait stylisé devient mesurable, celui des krachs trop fréquents. [p. 23]
   Histoire : « un écart de plus de vingt écarts types » — Les écarts lointains arrivent bien plus souvent que la loi normale ne le dit : une loi de Laplace de même variance dépasse trois écarts types avec une probabilité de 1,4 %, contre 0,27 % pour la loi normale. C'est ce que la kurtosis mesure. [ajout]

8. pfo/p-valeur
   Mesurer un écart ne suffit pas : sur un échantillon fini, une asymétrie non nulle peut venir du hasard. Il faut une règle de décision. [p. 25]
   Suite : Six rendements, c'est peu. Une asymétrie de −1,37 peut-elle venir du seul hasard, même si la loi était normale ? [ajout]
   Histoire : « peut-elle venir du seul hasard » — On calcule la probabilité, si la loi était normale, d'obtenir un écart au moins aussi grand : c'est la p-valeur. Sous 5 %, on rejette la normalité ; au-dessus, on ne peut pas conclure. [ajout]

9. pfo/test-de-normalite
   Appliquée à la question du chapitre, cette règle demande une hypothèse précise à éprouver. [éq. 2.13, éq. 2.14]
   Histoire : « même si la loi était normale » — L'hypothèse éprouvée est précise, $H_0:X\sim\mathcal{N}(\mu,\sigma^2)$. Le test ne prouve jamais qu'elle est vraie ; il dit seulement si les données permettent de la rejeter. [ajout]

10. pfo/test-de-jarque-bera
    Premier test : il réemploie directement les deux moments calculés aux étapes 4 et 5. [§2.3]
    Suite : Sur 1 000 rendements réels, on mesure une asymétrie de −0,5 et un excès de kurtosis de 3. La normalité tient-elle ? [ajout]
    Histoire : « La normalité tient-elle » — Jarque-Bera combine les deux écarts : $JB=\tfrac{1000}{6}\big(0{,}25+\tfrac94\big)\approx416{,}7$, très au-delà du seuil de 5,99 qui correspond au niveau de 5 %. La normalité est rejetée. [ajout]

11. pfo/test-de-shapiro-wilk
    Second test : il regarde l'échantillon trié tout entier, et peut rejeter là où le premier ne voit rien. [§2.4, p. 31]
    Suite : Sur un autre échantillon, Jarque-Bera donne une p-valeur de 0,20. Faut-il en conclure que la loi est normale ? [ajout]
    Histoire : « Faut-il en conclure que la loi est normale » — Non : Shapiro-Wilk, qui compare l'échantillon trié aux positions qu'y occuperaient les observations d'une loi normale, peut rejeter là où Jarque-Bera ne voit rien, par exemple avec une p-valeur de 0,03 sur le même échantillon. [ajout]

## Point d'arrivée
L'écart à la normale se nomme, se mesure et se teste. Reste à savoir ce qu'il change à la mesure du risque. [ajout]

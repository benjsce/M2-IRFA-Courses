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
   Que faut-il conclure d'un jour pareil, que la loi normale déclarait impossible ? [p. 19, §2.1]
   Histoire : « qui n'aurait jamais dû arriver » — Sous une loi normale, une baisse de plus de vingt écarts types a une probabilité de l'ordre de $10^{-89}$ ; elle est pourtant arrivée. Ce n'est donc pas le marché qui s'est trompé, c'est la loi : les rendements réels ne sont pas gaussiens, et un modèle qui le suppose sous-estime les pertes extrêmes. [ajout]

2. pfo/fait-stylise
   En quoi, précisément, les rendements réels s'écartent-ils de la loi normale ? Mandelbrot et Fama en ont dressé la liste. [§2.1.1]
   Histoire : « Le 19 octobre 1987 » — Ce krach n'est pas isolé : les rendements réels ont des pertes extrêmes trop fréquentes, des baisses plus violentes que les hausses, des périodes agitées qui se suivent. Ce sont des régularités qu'on retrouve d'un marché à l'autre, et que la loi normale ne reproduit pas. [ajout]

3. pfo/moment-standardise
   Pour passer du constat à la mesure, il faut aller au-delà de la moyenne et de la variance. [§2.1.2]
   Suite : Prenons une petite série de rendements : −2 %, −1 %, 0 %, 1 %, 2 %, et un jour de krach à −10 %. Sa moyenne et son écart type suffisent-ils à dire ce que ce krach a d'anormal ? [ajout]
   Histoire : « suffisent-ils à dire ce que ce krach a d'anormal » — Non : ils disent où se trouve la série et combien elle s'étale, pas sa forme. Les moyennes des puissances 3 et 4 de l'écart réduit, $\big((r-\mu)/\sigma\big)^k$, regardent précisément les écarts lointains ; elles vaudraient 0 et 3 pour une loi normale. [ajout]

4. pfo/coefficient-d-asymetrie
   Premier outil : une puissance impaire, qui garde le signe des écarts et voit donc de quel côté penche la loi. [§2.1.2, p. 21]
   Histoire : « un jour de krach à −10 % » — Élevé au cube, l'écart réduit garde son signe : le −10 %, très loin sous la moyenne, pèse lourd et négatif. La série a un coefficient d'asymétrie de −1,37 ; sans ce jour, elle est symétrique et le coefficient est nul. [ajout]

5. pfo/asymetrie-negative
   Ce signe négatif est-il un accident de la petite série, ou un trait des marchés ? [§2.1.1, p. 21]
   Histoire : « le Dow Jones perd 22,6 % » — Un trait des marchés, et le premier fait stylisé qui devienne un chiffre : sur les actions, les baisses sont plus brutales que les hausses, et les krachs sont des baisses. La queue des pertes est plus longue que celle des gains, ce que la volatilité ne voit pas et que le signe du coefficient d'asymétrie lit aussitôt. [ajout]

6. pfo/kurtosis
   Le signe ne dit pas tout : le krach est aussi un écart trop lointain, dans quelque sens qu'il aille. Second outil : une puissance paire et élevée, qui efface le signe et grossit démesurément les écarts lointains. [§2.1.2, p. 22]
   Histoire : « Prenons une petite série de rendements » — À la puissance quatre, le signe s'efface et les écarts lointains dominent : la kurtosis de la série vaut environ 3,49, au-dessus des 3 d'une loi normale. Sans le jour de krach, elle ne vaudrait que 1,7. [ajout]

7. pfo/queues-epaisses
   Une kurtosis au-dessus de 3, à quoi cela ressemble-t-il sur la loi elle-même ? [p. 23]
   Suite : Comparons à la loi normale une loi de Laplace de même moyenne et de même variance, dont la densité décroît comme $e^{-|x|}$ et non comme $e^{-x^2/2}$ ; sa kurtosis vaut 6. Combien de fois plus souvent s'écarte-t-elle de plus de trois écarts types ? [ajout]
   Histoire : « Combien de fois plus souvent s'écarte-t-elle de plus de trois écarts types » — Plus de cinq fois : elle dépasse trois écarts types avec une probabilité de 1,4 %, contre 0,27 % pour la loi normale. C'est ce qu'on appelle des queues épaisses, et c'est le second fait stylisé devenu mesurable : les écarts lointains, comme celui de 1987, arrivent bien plus souvent que la loi normale ne le dit. [ajout]

8. pfo/p-valeur
   Reste une objection : mesurer un écart ne suffit pas, car sur un échantillon fini une asymétrie non nulle peut venir du hasard. [p. 25]
   Suite : Six rendements, c'est peu. Une asymétrie de −1,37 peut-elle venir du seul hasard, même si la loi était normale ? [ajout]
   Histoire : « peut-elle venir du seul hasard » — Pour le savoir, on suppose la loi normale et l'on calcule la probabilité d'obtenir un écart au moins aussi grand : c'est la p-valeur. En tirant un très grand nombre de séries de six rendements normaux, une asymétrie d'au moins 1,37, dans un sens ou dans l'autre, n'apparaît qu'environ trois fois sur cent : la p-valeur vaut à peu près 0,03. Le hasard l'explique mal, sans l'exclure. [ajout]

9. pfo/test-de-normalite
   Trois chances sur cent, est-ce assez peu pour abandonner la loi normale ? La réponse se fixe avant de regarder les données : l'hypothèse éprouvée, et le seuil. [éq. 2.13, éq. 2.14]
   Histoire : « même si la loi était normale » — L'hypothèse éprouvée est $H_0:X\sim\mathcal{N}(\mu,\sigma^2)$, rejetée quand la p-valeur passe sous 5 %. Avec 0,03, la petite série la rejette : le seul krach y suffit. Au-dessus de 5 %, on aurait seulement dit qu'on ne la rejette pas, jamais que la loi est normale. [ajout]

10. pfo/test-de-jarque-bera
    Ce calcul ne regardait que l'asymétrie, et il a fallu simuler sa loi. Un test usuel juge les deux écarts à la fois, avec une loi connue d'avance. [§2.3]
    Suite : Cette loi ne vaut que sur de longues séries. Sur 1 000 rendements réels, on mesure une asymétrie de −0,5 et un excès de kurtosis de 3, c'est-à-dire une kurtosis de 6, dépassant de 3 celle d'une loi normale. La normalité tient-elle ? [ajout]
    Histoire : « La normalité tient-elle » — Jarque-Bera combine les deux écarts à la loi normale, l'asymétrie $S$ et l'excès de kurtosis $K_{\mathrm{ex}}$, sur $T$ rendements : $JB=\tfrac{T}{6}\big(S^2+\tfrac{K_{\mathrm{ex}}^2}{4}\big)=\tfrac{1000}{6}\big((-0{,}5)^2+\tfrac{3^2}{4}\big)\approx416{,}7$. Si la loi était normale, $JB$ suivrait une loi du khi-deux à deux degrés de liberté, qui ne dépasse 5,99 qu'une fois sur vingt ; très au-delà, la normalité est rejetée. [ajout]

11. pfo/test-de-shapiro-wilk
    Jarque-Bera ne regarde que ces deux nombres. Une série peut-elle avoir l'asymétrie et la kurtosis d'une loi normale sans en suivre la loi ? [§2.4, p. 31]
    Suite : Prenons un titre peu échangé, dont le cours ne bouge que d'un cran : sur trente jours, cinq baisses de 1 %, vingt jours sans changement, cinq hausses de 1 %. Son asymétrie est nulle et sa kurtosis vaut exactement 3. Faut-il en conclure que la loi est normale ? [ajout]
    Histoire : « Faut-il en conclure que la loi est normale » — Jarque-Bera ne voit rien : $JB=0$, p-valeur 1. Shapiro-Wilk compare l'échantillon trié aux positions qu'y occuperaient trente observations normales, et y voit trois paliers là où la loi normale mettrait une pente régulière : $W\approx0{,}75$, p-valeur bien en dessous de 1 %, la normalité est rejetée. [ajout]

## Point d'arrivée
L'écart à la normale se nomme, se mesure et se teste. Reste à savoir ce qu'il change à la mesure du risque. [ajout]

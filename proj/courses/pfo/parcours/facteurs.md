---
id: pfo/parcours-facteurs
ordre: 8
titre: Les mouvements communs que le marché ne voit pas
source: poly, chapitre 4, §4.2.2 à §4.3, exercices 2, 4 et 5
---

## Point de départ
Régressé sur le marché pendant soixante mois, le second actif du récit précédent ne voit expliquer que 49 % de ses variations. L'investisseur se demande si le reste lui est vraiment propre, ou si d'autres mouvements, communs à beaucoup d'entreprises, s'y cachent. [ajout]

## À savoir avant
- pfo/regression-du-medaf : elle a laissé la moitié des variations du second actif sans explication ; le modèle de Fama et French lui ajoute deux colonnes. [p. 59]
- pfo/portefeuille-de-marche : il fournit la capitalisation, sur laquelle on trie les entreprises par taille et à laquelle on compare leurs comptes. [p. 57]
- fpp/bilan : il donne les capitaux propres comptables, actifs moins dettes, que le récit compare à la capitalisation. [ajout]
- pfo/matrice-de-covariance : c'est la seule donnée que l'analyse en composantes principales consulte ; le récit reprend celle de son exemple. [§1.5]
- dss/moindres-carres-ordinaires : c'est la méthode de la régression du récit précédent, appliquée à la fin à un facteur extrait des données. [ajout]

## Étapes
1. pfo/modele-factoriel
   Le MEDAF ne connaît qu'un mouvement commun, le marché. [§4.2.4]
   Histoire : « d'autres mouvements, communs à beaucoup d'entreprises, s'y cachent » — Si c'est le cas, son rendement s'écrit comme une somme d'expositions à quelques mouvements communs, dont le marché, plus une part qui lui est propre ; ce que le récit précédent appelait son risque propre n'était que ce que le marché seul n'expliquait pas. [ajout]

2. pfo/facteur-de-risque
   Encore faut-il dire ce que sont ces mouvements. [p. 62]
   Suite : Quels mouvements communs ajouter au marché, et qui les choisit ? [ajout]
   Histoire : « Quels mouvements communs ajouter au marché, et qui les choisit » — Des séries de rendements construites à partir des actifs eux-mêmes. On peut les choisir d'avance, sur une idée économique, en opposant deux groupes d'entreprises ; ou les extraire des données, sans rien supposer de leur sens. Le récit fait l'un, puis l'autre. [ajout]

3. pfo/facteur-smb
   Première idée économique : la taille des entreprises. [§4.2.2]
   Suite : Le second actif est la plus petite des deux entreprises, 10 milliards contre 20. Sur un marché plus large, un mois où les petites capitalisations font 3 % et les grandes 1 %, de combien les petites ont-elles battu les grandes ? [ajout]
   Histoire : « de combien les petites ont-elles battu les grandes » — De deux points, $3\,\%-1\,\%$ : c'est la valeur ce mois-là du facteur de taille. Une petite entreprise qui monte avec lui y est exposée positivement. [ajout]

4. pfo/facteur-hml
   Seconde idée : le prix que la bourse paie pour ce que disent les comptes. [§4.2.2]
   Suite : Deux entreprises ont le même bilan, 100 d'actifs et 80 de dette, et la bourse capitalise l'une à 25, l'autre à 100. Ce mois-là, les entreprises du premier genre font 0,5 %, celles du second 2,5 %. Qu'a rapporté l'écart entre celles que la bourse paie peu au regard de leurs comptes et celles qu'elle paie cher ? [ajout]
   Histoire : « l'écart entre celles que la bourse paie peu au regard de leurs comptes et celles qu'elle paie cher » — Leurs capitaux propres comptables valent $100-80=20$ : book-to-market de 0,8 pour la première, rangée Value, de 0,2 pour la seconde, rangée Growth. L'écart vaut $0{,}5\,\%-2{,}5\,\%=-2\,\%$ : ce mois-là, la croissance l'a emporté. [ajout]

5. pfo/modele-de-fama-french
   Le marché, la taille et la valeur forment maintenant trois mouvements communs. [§4.2.2]
   Suite : Ce même mois, le marché fait 4 % au-delà du taux sans risque. Vu comme une petite entreprise de croissance, le second actif a des expositions de 1,5 au marché, de 0,6 à la taille et de −0,4 à la valeur, et un alpha nul. Que doit-il rapporter au-delà du taux sans risque ? [ajout]
   Histoire : « Que doit-il rapporter au-delà du taux sans risque » — $1{,}5\times4+0{,}6\times2+(-0{,}4)\times(-2)=6+1{,}2+0{,}8=8\,\%$ : deux points de plus que le marché seul ne lui en donnait, venus de sa taille et de son style. [ajout]

6. pfo/analyse-en-composantes-principales
   Ces mouvements ont été choisis d'avance ; on peut aussi ne rien supposer. [§4.2.3]
   Suite : L'investisseur regarde maintenant deux autres actifs, de volatilités journalières 1 % et 2 % et corrélés à 0,5, sans aucune idée de ce qui les fait bouger. Dans quelle direction leurs rendements varient-ils le plus ensemble ? [ajout]
   Histoire : « Dans quelle direction leurs rendements varient-ils le plus ensemble » — Dans celle du vecteur propre de leur matrice de covariance qui a la plus grande valeur propre : $(0{,}29\,;0{,}96)$, de variance annualisée 0,108 sur un total de 0,126, soit 86 %. Elle penche vers le second actif, le plus volatil. [ajout]

7. pfo/facteur-statistique
   Cette direction n'est encore qu'un vecteur de deux nombres. [p. 65]
   Suite : Un jour où le premier actif fait 1 % et le second 2 %, que vaut ce mouvement commun ? [ajout]
   Histoire : « que vaut ce mouvement commun » — $0{,}29\times1+0{,}96\times2=2{,}20\,\%$. Les coefficients restent les mêmes chaque jour ; la valeur change avec les rendements, et forme ainsi une série, jour après jour. [ajout]

8. pfo/modele-factoriel-statistique
   Le mouvement commun est maintenant une série datée, comme l'était le marché au récit précédent. [p. 62]
   Suite : Combien chacun des deux actifs est-il exposé à cette série ? [ajout]
   Histoire : « Combien chacun des deux actifs est-il exposé à cette série » — Régressé sur elle, le second actif a une exposition de 0,96, et elle explique 98,5 % de ses variations ; le premier, 0,29 et 36 % seulement. Sans standardisation, le mouvement extrait est d'abord celui de l'actif le plus volatil. [ajout]

## Point d'arrivée
Il y a deux façons de trouver les mouvements communs qui se cachent dans un rendement : les choisir d'avance, comme Fama et French la taille et la valeur, ou les extraire des données, comme l'analyse en composantes principales. Les premiers ont un sens économique qu'il reste à démontrer ; les seconds expliquent le plus de variance possible et ne disent rien de leur sens. Dans les deux cas, une régression mesure ensuite l'exposition de chaque actif. [p. 62, ajout]

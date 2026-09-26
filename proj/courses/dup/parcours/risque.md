---
id: dup/parcours-risque
ordre: 1
titre: Mesurer l'attitude face au risque
source: L1 slides 2–40
---

## Point de départ
Un pari rapporte 0 ou 100 avec une chance sur deux : il vaut 50 en moyenne. Pour un agent dont l'utilité est $\sqrt{x}$, il ne vaut pourtant pas plus que 25 reçus à coup sûr. [ajout]

Donnons-lui 100 en poche avant de jouer : il n'abandonne plus qu'environ 4,3 sur la moyenne, et la richesse a changé le prix du risque. Un second agent, d'utilité $\ln x$, avec les mêmes 100 en poche, en abandonne deux fois plus, environ 8,6. [ajout]

Sur un pari plus petit, 10 gagnés ou perdus à pile ou face avec 100 en poche, les deux primes tombent à 0,25 et 0,50 environ. À 1000 en poche et sur 100 gagnés ou perdus, celle du second agent vaut environ 5 : toujours un demi pour cent de sa richesse. [ajout]

Ces deux agents sont-ils des cas isolés, et que dire d'une économie entière, dont la croissance est elle aussi un pari ? Ce parcours suit la façon dont le cours explique ces écarts, puis les chiffre. [ajout]

## Étapes
1. dup/loterie
   Le point de départ est l'objet le plus simple du cours : un pari dont les probabilités sont données avec l'énoncé. [L1 slide 2]
   Histoire : « Un pari rapporte 0 ou 100 avec une chance sur deux » — Avant de dire ce que vaut ce pari, il faut l'écrire comme un objet sur lequel on raisonne : deux résultats, 0 et 100, chacun avec sa probabilité, donnée par l'énoncé. [ajout]

2. dup/fonction-utilite
   Pour comparer des paris, il faut d'abord dire ce que vaut chaque montant pour la personne qui le reçoit, et ce n'est pas le montant lui-même. [L1 slide 3]
   Histoire : « dont l'utilité est $\sqrt{x}$ » — L'histoire ne demande pas ce que vaut le pari en général, mais ce qu'il vaut pour un agent précis, décrit par son utilité : pour lui, 100 euros valent $\sqrt{100}=10$, et non 100. [ajout]

3. dup/axiome-independance
   Quelle règle de cohérence impose-t-on aux choix entre paris ? Celle qui fait le cœur du modèle porte sur la façon de mélanger des paris. [L1 slide 4]
   Histoire : Rien dans l'histoire ne dit encore comment passer de ce que valent 0 et 100 pour l'agent à ce que vaut le pari qui les mélange. C'est cette règle de cohérence, au cœur du modèle, qui fixera la façon de le faire. [ajout]

4. dup/utilite-esperee
   Cette règle a une conséquence précise sur la façon dont un pari s'évalue : les probabilités y entrent comme de simples poids. [L1 slide 3, L1 slide 4]
   Histoire : « il ne vaut pourtant pas plus que 25 reçus à coup sûr » — Ici, « valoir » porte sur le pari entier, pour l'agent : il faut une valeur pour la loterie, et plus seulement pour un montant. Celle du pari de l'histoire est $\tfrac12\sqrt{0}+\tfrac12\sqrt{100}=5$, exactement l'utilité de 25 reçus à coup sûr, puisque $\sqrt{25}=5$. [ajout]

5. dup/courbure-de-l-utilite
   Si les probabilités sont de simples poids, où peut encore se loger une attitude face au risque ? Il ne reste qu'un endroit. [L1 slide 3]
   Histoire : « ces écarts » — Entre 50 et 25, entre 8,6 et 4,3 : puisque les probabilités n'entrent dans la valeur d'un pari que comme poids, ces écarts ne peuvent venir que de la forme de l'utilité de chaque agent. [ajout]

6. dup/aversion-au-risque
   Comment nommer ce que fait l'agent de l'exemple, et à quelle forme de $u$ cela correspond-il ? [L1 slide 7]
   Histoire : « il vaut 50 en moyenne » — Recevoir ces 50 à coup sûr vaudrait $\sqrt{50}\approx7{,}07$ à l'agent, plus que les 5 du pari : l'agent de l'histoire préfère la moyenne certaine au pari lui-même. [ajout]

7. dup/equivalent-certain
   Dire qu'on préfère le certain ne dit pas de combien. Il faut ramener le pari à un montant qu'on puisse comparer à sa moyenne. [L1 slide 9]
   Histoire : « 25 reçus à coup sûr » — Le 25 de l'histoire est ce montant : la somme certaine que l'agent juge exactement équivalente au pari. [ajout]

8. dup/prime-de-risque
   L'écart entre ce montant et la moyenne du pari est ce que l'agent paie pour ne pas courir le risque. [L1 slide 9]
   Histoire : « puis les chiffre » — Chiffrer l'écart, c'est dire ce que l'agent abandonne sur la moyenne : $50-25=25$ pour le premier pari, 4,3 et 8,6 pour les deux agents qui ont 100 en poche. [ajout]

9. dup/aversion-absolue-arrow-pratt
   Pour comparer l'aversion de deux personnes, il faut une mesure de la courbure qui ne change pas quand on change l'échelle de l'utilité. [L1 slide 33]
   Histoire : « Un second agent, d'utilité $\ln x$ » — Avec les mêmes 100 en poche, il abandonne deux fois plus que le premier. Pour le prévoir sans refaire le calcul, il faut mesurer la courbure de chaque utilité, rapportée à sa pente : à 100, elle vaut $1/200$ pour $\sqrt{x}$ et $1/100$ pour $\ln x$. [ajout]

10. dup/approximation-arrow-pratt
    Cette mesure et la prime se rejoignent pour les petits paris : on peut alors calculer la prime sans passer par l'utilité espérée. [L1 slide 32]
    Histoire : « Sur un pari plus petit » — La moitié de la variance du pari, 100, fois la mesure de courbure donne $\tfrac12\times100\times\tfrac{1}{200}=0{,}25$ et $\tfrac12\times100\times\tfrac{1}{100}=0{,}50$ : les deux primes de l'histoire, presque sans passer par l'utilité. Sur le premier pari, qui va de 0 à 100, elle donnerait 12,5 au lieu de 25. [ajout]

11. dup/aversion-relative
    Peut-on dire qu'une personne est plus averse qu'une autre sans rien calculer, en regardant seulement les paris qu'elle refuse ? [L1 slide 30]
    Histoire : « Un second agent » — Il abandonne plus que le premier sur le grand pari comme sur le petit. Le cours veut pouvoir dire qu'il est plus averse sans choisir un pari : il refuse tout pari qui laisse le premier indifférent. [ajout]

12. dup/dara
    Comment l'aversion devrait-elle évoluer quand on s'enrichit ? Le cours retient une hypothèse que presque tout le monde accepte. [L1 slide 34]
    Histoire : « Donnons-lui 100 en poche avant de jouer » — Plus riche, le premier agent n'abandonne plus qu'environ 4,3 au lieu de 25 pour le même pari. Sa mesure de courbure, $1/(2x)$, baisse quand la richesse monte. [ajout]

13. dup/famille-hara
    Il faut maintenant des formes d'utilité concrètes pour calculer. Le cours les range toutes dans une même famille, où chacune est un point. [L1 slide 35]
    Histoire : « Ces deux agents sont-ils des cas isolés » — $\sqrt{x}$ et $\ln x$ sont deux points d'une même famille de formes d'utilité, que le cours range ensemble. [ajout]

14. dup/cara
    Premier point de la famille : l'aversion absolue y est la même à tout niveau de richesse. [L1 slide 35]
    Histoire : « la richesse a changé le prix du risque » — Chez les deux agents de l'histoire, la richesse change la prime. Cette forme-ci est celle où elle ne la changerait pas : même prime pour le même pari, qu'on ait 0, 100 ou 1000 en poche. [ajout]

15. dup/crra
    Second point : c'est l'aversion relative qui reste constante, ce qui permet de parler de la prime en pourcentage de la richesse. [L1 slide 35]
    Histoire : « toujours un demi pour cent de sa richesse » — Richesse et pari décuplés, la prime du second agent est décuplée aussi : elle reste la même part de sa richesse. C'est ce que cette forme garde constant, et $\sqrt{x}$ en fait aussi partie, avec $\gamma=\tfrac12$. [ajout]

16. dup/utilite-logarithmique
    Un cas particulier de cette forme revient partout dans le cours, parce que sa prime se calcule à la main. [L1 slide 35]
    Histoire : « d'utilité $\ln x$ » — Le second agent a cette utilité, d'aversion relative 1 contre un demi pour le premier. Ses primes se calculent à la main : avec 100 en poche, son équivalent certain est $\sqrt{100\times200}\approx141{,}4$, d'où la prime de 8,6. [ajout]

17. dup/cout-social-du-risque
    À quoi tout cela sert-il hors du laboratoire ? Le cours l'applique au risque sur la croissance d'une économie entière. [L1 slide 38]
    Histoire : « une économie entière, dont la croissance est elle aussi un pari » — Le pari porte alors sur la croissance du PIB par tête, et la prime se mesure en points de croissance qu'une population céderait pour la rendre sûre. [ajout]

## Point d'arrivée
L'écart entre 25 et 50 est devenu un nombre, la prime de risque, que l'on sait relier à une propriété de l'utilité, calculer pour une forme donnée, et comparer d'un agent à l'autre et d'une richesse à l'autre. [ajout]

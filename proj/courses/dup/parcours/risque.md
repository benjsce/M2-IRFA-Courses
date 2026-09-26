---
id: dup/parcours-risque
ordre: 1
titre: Mesurer l'attitude face au risque
source: L1 slides 2–40
---

## Point de départ
Un pari rapporte 0 ou 100 avec une chance sur deux : il vaut 50 en moyenne. Pour un agent dont l'utilité est $\sqrt{x}$, il ne vaut pourtant pas plus que 25 reçus à coup sûr. Ce parcours suit la façon dont le cours explique cet écart, puis le chiffre. [ajout]

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
   Histoire : « cet écart » — L'écart entre 50 et 25 est ce que le parcours doit expliquer. Puisque les probabilités n'entrent dans la valeur du pari que comme poids, il ne peut venir que de la forme de $\sqrt{x}$, qui monte de moins en moins vite. [ajout]

6. dup/aversion-au-risque
   Comment nommer ce que fait l'agent de l'exemple, et à quelle forme de $u$ cela correspond-il ? [L1 slide 7]
   Histoire : « il vaut 50 en moyenne » — Recevoir ces 50 à coup sûr vaudrait $\sqrt{50}\approx7{,}07$ à l'agent, plus que les 5 du pari : l'agent de l'histoire préfère la moyenne certaine au pari lui-même. [ajout]

7. dup/equivalent-certain
   Dire qu'on préfère le certain ne dit pas de combien. Il faut ramener le pari à un montant qu'on puisse comparer à sa moyenne. [L1 slide 9]
   Histoire : « 25 reçus à coup sûr » — Le 25 de l'histoire est ce montant : la somme certaine que l'agent juge exactement équivalente au pari. [ajout]

8. dup/prime-de-risque
   L'écart entre ce montant et la moyenne du pari est ce que l'agent paie pour ne pas courir le risque. [L1 slide 9]
   Histoire : « puis le chiffre » — Le chiffre qu'annonce l'histoire est l'écart entre ses deux nombres : $50-25=25$. [ajout]

9. dup/aversion-absolue-arrow-pratt
   Pour comparer l'aversion de deux personnes, il faut une mesure de la courbure qui ne change pas quand on change l'échelle de l'utilité. [L1 slide 33]
   Histoire : « Pour un agent » — Un autre agent, d'utilité différente, donnerait au même pari un autre montant certain. Pour dire lequel des deux craint le plus le risque, il faut mesurer la courbure de chaque utilité, rapportée à sa pente ; pour $\sqrt{x}$, cette mesure vaut $1/(2x)$. [ajout]

10. dup/approximation-arrow-pratt
    Cette mesure et la prime se rejoignent pour les petits paris : on peut alors calculer la prime sans passer par l'utilité espérée. [L1 slide 32]
    Histoire : « puis le chiffre » — Le 25 de l'histoire se calcule en passant par $\sqrt{x}$. L'approximation, faite autour de la moyenne 50, donnerait $\tfrac12\times2500\times\tfrac{1}{100}=12{,}5$ : le pari de l'histoire, qui va de 0 à 100, est trop grand pour qu'elle s'applique. [ajout]

11. dup/aversion-relative
    Peut-on dire qu'une personne est plus averse qu'une autre sans rien calculer, en regardant seulement les paris qu'elle refuse ? [L1 slide 30]
    Histoire : « Pour un agent » — Un second agent qui préférerait 25 sûrs au pari, là où celui de l'histoire est indifférent, serait plus averse que lui. Le cours veut pouvoir le dire sans calcul, en comparant seulement les paris que chacun refuse. [ajout]

12. dup/dara
    Comment l'aversion devrait-elle évoluer quand on s'enrichit ? Le cours retient une hypothèse que presque tout le monde accepte. [L1 slide 34]
    Histoire : L'agent de l'histoire part de rien. Avec 100 déjà en poche, le même pari ne lui coûterait plus qu'une prime d'environ 4,3, au lieu de 25 : avec $\sqrt{x}$, l'aversion absolue $1/(2x)$ baisse quand la richesse monte. [ajout]

13. dup/famille-hara
    Il faut maintenant des formes d'utilité concrètes pour calculer. Le cours les range toutes dans une même famille, où chacune est un point. [L1 slide 35]
    Histoire : « $\sqrt{x}$ » — La racine de l'histoire n'est qu'une forme d'utilité parmi d'autres, et le cours les range dans une seule famille, dont $\sqrt{x}$ est un point. [ajout]

14. dup/cara
    Premier point de la famille : l'aversion absolue y est la même à tout niveau de richesse. [L1 slide 35]
    Histoire : L'aversion absolue de l'agent de l'histoire, $1/(2x)$, dépend de sa richesse : $\sqrt{x}$ n'est pas de cette forme. Celle-ci sert de premier repère, où la prime d'un pari ne dépend pas de ce qu'on possède déjà. [ajout]

15. dup/crra
    Second point : c'est l'aversion relative qui reste constante, ce qui permet de parler de la prime en pourcentage de la richesse. [L1 slide 35]
    Histoire : « dont l'utilité est $\sqrt{x}$ » — L'agent de l'histoire est de ce type, avec $\gamma=\tfrac12$ : son aversion relative, $x\times\tfrac{1}{2x}$, vaut un demi à toute richesse. [ajout]

16. dup/utilite-logarithmique
    Un cas particulier de cette forme revient partout dans le cours, parce que sa prime se calcule à la main. [L1 slide 35]
    Histoire : « $\sqrt{x}$ » — Le logarithme est le voisin de la racine dans la même famille, un peu plus averse : une aversion relative de 1 contre un demi. Face au pari de l'histoire, qui peut ne rien rapporter, il préférerait n'importe quel montant certain positif, car $\ln 0$ vaut $-\infty$. [ajout]

17. dup/cout-social-du-risque
    À quoi tout cela sert-il hors du laboratoire ? Le cours l'applique au risque sur la croissance d'une économie entière. [L1 slide 38]
    Histoire : « Un pari » — Un pari n'a pas besoin d'être un jeu : la croissance d'une économie est incertaine, et la prime de risque mesure alors ce que sa population céderait pour qu'elle soit sûre. [ajout]

## Point d'arrivée
L'écart entre 25 et 50 est devenu un nombre, la prime de risque, que l'on sait relier à une propriété de l'utilité et calculer pour une forme donnée. [ajout]

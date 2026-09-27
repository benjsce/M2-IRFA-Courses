---
id: dup/parcours-poids
ordre: 5
titre: Déformer les probabilités
source: L1 slide 55, L2 slides 21–27, L3 slides 20–41, L4 slides 14–15
---

## Point de départ
Un billet verse 100 avec une probabilité de 1 %, et rien sinon. Avec $u(x)=\sqrt{x}$, l'utilité espérée ne lui accorde qu'un équivalent certain de 0,01, et pourtant beaucoup le paient plus que son espérance, 1. [ajout]

Une seconde famille de modèles laisse l'utilité des résultats tranquille et agit sur les probabilités : un événement rare peut compter plus que sa probabilité, un événement presque certain moins. [L1 slide 55]

## À savoir avant
- dup/utilite-esperee : c'est le modèle dont on garde l'utilité et dont on déforme les probabilités. Chaque étape y revient quand la déformation disparaît. [L1 slide 55]
- dup/cadrage : il fonde le point de référence de la théorie des perspectives, où les résultats se lisent en gains et en pertes. [L3 slide 20]
- dup/accroissement-de-risque : il définit la forme forte de l'aversion au risque, qui refuse tout étalement préservant la moyenne. [L4 slide 15]
- dup/approximation-arrow-pratt : elle donne la taille de la prime pour un petit pari sous utilité espérée, ce qui sert d'étalon aux deux ordres de l'aversion. [L2 slide 21]

## Étapes
1. dup/ponderation-des-probabilites
   Le cours sépare ce qu'un modèle de choix peut changer, et isole la famille qui ne touche qu'à la façon dont les probabilités entrent. [L1 slide 55]
   Histoire : « un événement rare peut compter plus que sa probabilité » — Le billet de l'histoire est payé plus que son espérance : si son 1 % comptait comme 5 %, il vaudrait 5 même avec une utilité linéaire. Cette famille garde $u$ telle quelle et change seulement le poids avec lequel chaque probabilité entre. [ajout]

2. dup/theorie-des-perspectives
   La version la plus connue ajoute un point de référence et lit les résultats comme des gains et des pertes. [L3 slide 20, L3 slide 21]
   Suite : Celui qui achète le billet au prix de 2, plus que son espérance, ne le vit pas en richesses finales : il gagne 98 une fois sur cent, et perd 2 le reste du temps. Comment un modèle tient-il compte de ce point de référence, le prix payé ? [ajout]
   Histoire : « Comment un modèle tient-il compte de ce point de référence » — La théorie des perspectives code chaque résultat comme un gain ou une perte par rapport à ce point, lui donne une valeur $v$, nulle au point de référence, et pondère chaque probabilité par $\pi$ : le billet vaut $\pi(0{,}01)v(98)+\pi(0{,}99)v(-2)$. [ajout]

3. dup/rdu
   Ce modèle a pourtant un défaut grave : il peut faire choisir un pari moins bon qu'un autre dans tous les cas. [L3 slide 26]
   Suite : Coupons le gain du billet en deux : 100 avec 0,5 % de chances, 99 avec 0,5 %, rien sinon. Ce nouveau billet est moins bon que le premier dans tous les cas. Un modèle qui pondère chaque probabilité séparément le juge-t-il ainsi ? [ajout]
   Histoire : « Un modèle qui pondère chaque probabilité séparément le juge-t-il ainsi » — Pas forcément : si les petites probabilités sont surpondérées, deux fois $\pi(0{,}005)$ peut dépasser nettement $\pi(0{,}01)$, et le billet coupé en deux valoir plus que l'autre. La pondération par le rang déforme la fonction de répartition plutôt que chaque probabilité : les deux chances de gain comptent alors ensemble autant que l'unique chance du premier billet, et la dominance est préservée. [ajout]

4. dup/cpt
   La théorie des perspectives peut alors être refaite sur cette base, séparément du côté des gains et du côté des pertes. [L3 slide 38]
   Histoire : « il gagne 98 une fois sur cent, et perd 2 le reste du temps » — Refaite par le rang, la théorie des perspectives pondère séparément le côté des gains et celui des pertes ; du côté des gains, les chances se cumulent depuis le meilleur résultat, la chance d'avoir au moins ce gain, et se déforment par la fonction du cours, $\varphi(p)=p^\beta/\big(p^\beta+(1-p)^\beta\big)^{1/\beta}$, où $\beta$ règle l'écart à la diagonale. Avec $\beta=0{,}7$, la chance de gagner 98 compte pour $\varphi(0{,}01)\approx3{,}8\,\%$ au lieu de 1 % : c'est ce qui fait payer le billet plus que son espérance. [L3 slide 38, ajout]

5. dup/pessimisme
   Reste à voir ce que la déformation des probabilités fait au risque, même avec une utilité linéaire. [L4 slide 14]
   Suite : Revenons au pari à pile ou face qui rapporte 0 ou 100, et jugeons-le avec une utilité linéaire. Peut-on le refuser contre sa moyenne, 50, sans aucune courbure de l'utilité ? [ajout]
   Histoire : « sans aucune courbure de l'utilité » — Oui, si la déformation charge le mauvais résultat. Revenue à la pondération par le rang, elle s'applique aux chances cumulées depuis le pire résultat : avec $\varphi(t)=\sqrt t$, le 0 compte pour $\varphi(0{,}5)\approx0{,}707$ au lieu d'une chance sur deux, et le pari vaut $100\times(1-0{,}707)\approx29{,}3$, moins que 50. [ajout]

6. dup/aversion-forte-au-risque
   Le pessimisme suffit à refuser un pari contre sa moyenne. Refuser tout étalement du risque demande une condition plus forte. [L4 slide 15]
   Suite : Refuser le pari contre sa moyenne, est-ce refuser aussi tout pari simplement plus étalé, à moyenne égale ? [ajout]
   Histoire : « refuser aussi tout pari simplement plus étalé » — Pas toujours. Avec $u(x)=x$, le cours prend la déformation $\varphi(t)=2t$ jusqu'à $\tfrac14$, $\tfrac38+\tfrac t2$ de $\tfrac14$ à $\tfrac34$, puis $t$ : pessimiste, puisqu'elle reste au-dessus de la diagonale, mais pas concave. $X=(10;0{,}4\,|\,20;0{,}6)$ vaut alors $10\,\varphi(0{,}4)+20\,\big(1-\varphi(0{,}4)\big)=10\times0{,}575+20\times0{,}425=14{,}250$ ; $Y$, où 20 est remplacé par 15 ou 25 à parts égales, vaut $10\times0{,}575+15\,\big(\varphi(0{,}7)-\varphi(0{,}4)\big)+25\,\big(1-\varphi(0{,}7)\big)=5{,}75+15\times0{,}15+25\times0{,}275=14{,}875$. $Y$ est plus étalé, de même moyenne 16, et pourtant préféré. Refuser tout étalement demande une condition plus forte sur $\varphi$. [L4 slide 34, ajout]

7. dup/aversion-second-ordre
   Pour distinguer ces modèles de l'utilité espérée, le cours regarde comment la prime se comporte quand le pari devient très petit. [L2 slide 21, L2 slide 24]
   Suite : Réduisons le pari : gagner ou perdre 10 à pile ou face, avec une richesse de 100. Sous l'utilité espérée, que devient la prime quand le pari rapetisse ? [ajout]
   Histoire : « que devient la prime quand le pari rapetisse » — Elle s'évanouit comme le carré de sa taille. Pour un agent dont l'aversion absolue à 100 vaut $\rho=0{,}01$, comme l'agent d'utilité $\ln x$, elle vaut environ la moitié de $\rho$ fois la variance : $\tfrac{0{,}01}{2}\times10^2=0{,}5$ pour un pari de ±10, et $\tfrac{0{,}01}{2}\times1^2=0{,}005$ pour un pari de ±1 ; dix fois plus petit, le pari coûte cent fois moins. [ajout]

8. dup/paradoxe-rabin
   Cette propriété a une conséquence que Rabin rend absurde à partir d'un choix d'apparence anodine. [L2 slide 25]
   Suite : Un agent refuse, quelle que soit sa richesse, de perdre 100 ou gagner 105 à pile ou face. Est-ce un choix anodin ? [L2 slide 27]
   Histoire : « Est-ce un choix anodin » — Non : sous l'utilité espérée, il doit alors refuser de perdre 945 ou gagner 1 680, et refuser toute perte de plus de 1 575, quel que soit le gain. Une prime qui s'évanouit aussi vite oblige, pour refuser un petit pari, à une courbure absurde. [L2 slide 27, ajout]

9. dup/aversion-premier-ordre
   Les modèles de ce parcours y échappent parce que leur prime ne s'évanouit pas aussi vite. [L2 slide 21, L3 slide 41]
   Histoire : « gagner ou perdre 10 à pile ou face » — Pour refuser ce pari sans l'absurde de Rabin, il faut une prime proportionnelle à sa taille, et non à son carré. C'est le cas si une perte pèse $\lambda=2$ fois un gain de même taille, sans autre courbure : $\gamma$, qui règle la courbure de l'utilité de part et d'autre du point de référence, vaut 0, et l'utilité est linéaire de chaque côté. Pour que l'agent accepte le pari, il faut y ajouter une somme $r$ telle que $\tfrac12(10+r)=\tfrac12\times2\times(10-r)$, soit $r=10/3\approx3{,}33$, un tiers de la taille, contre 0,5 sous l'utilité espérée ; et elle reste un tiers quand le pari rapetisse. [ajout]

10. dup/aversion-aux-pertes
    D'où vient, dans la théorie des perspectives, cette prime qui ne s'évanouit pas ? D'une asymétrie au point de référence. [L3 slide 39]
    Histoire : « perd 2 le reste du temps » — La prime qui ne s'évanouit pas vient d'un coude au point de référence : une perte pèse $\lambda$ fois un gain de même taille. Avec $\lambda=2$ et $\beta=1$, ici l'exposant de la fonction de valeur et non celui de la déformation, qui la laisse linéaire de chaque côté, la perte de 2 du billet vaut $-4$ ; perdre 10 vaut $-20$ et gagner 10 vaut $+10$, de sorte que le pari de ±10 vaut $\tfrac12\times10-\tfrac12\times20=-5$ : il est refusé. [ajout]

## Point d'arrivée
Déformer les probabilités par le rang explique ce que l'utilité espérée ne peut pas expliquer, le refus des petits paris favorables, sans perdre la dominance. C'est ce modèle que le cours emporte vers le choix de portefeuille. [ajout]

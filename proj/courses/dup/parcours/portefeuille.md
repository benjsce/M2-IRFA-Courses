---
id: dup/parcours-portefeuille
ordre: 7
titre: Choisir un portefeuille avec ces modèles
source: L3 slides 42–46, L4 slides 17–34, L4 slides 63–67
---

## Point de départ
Un marché compte trois états, de probabilités 0,2, 0,3 et 0,5 ; le titre qui paie 1 dans un seul de ces états coûte 0,3, 0,3 et 0,4. Un investisseur qui a 1 à placer choisit combien recevoir dans chaque état. Que change à son choix le fait qu'il pondère les états par leur rang, ou qu'il doute de la loi elle-même ? Le cours pose la question pour ces deux modèles, et pour le prix auquel un marché s'équilibre. [ajout]

## À savoir avant
- dup/rdu : c'est le modèle de préférence de la première moitié du parcours, où les états comptent selon le rang de leur paiement. [L3 slide 42]
- dup/cara : c'est l'utilité de tous les investisseurs de la seconde moitié, choisie parce qu'elle rend la demande calculable. [L4 slide 63]
- dup/equivalent-certain : c'est ce que l'investisseur de la seconde moitié maximise, et qui devient une expression simple sous paiement gaussien. [L4 slide 63]
- dup/maxmin-eu : c'est le critère de l'investisseur ambigu, qui juge chaque position sous le modèle le plus défavorable. [L4 slide 64]

## Étapes
1. dup/portefeuille-rdu
   Le premier problème est d'écrire le programme de l'investisseur quand ses poids dépendent du rang de ses propres paiements. [L3 slide 42]
   Histoire : « choisit combien recevoir dans chaque état » — Son programme : choisir $x_1$, $x_2$ et $x_3$ sous le budget $0{,}3x_1+0{,}3x_2+0{,}4x_3=1$, en pondérant chaque état par son rang et non par sa probabilité. Ces poids dépendent de l'ordre des $x_s$, qu'il faut supposer pour écrire le programme. [ajout]

2. dup/poids-de-decision
   Ce que pèse un état ne se lit plus sur sa probabilité, mais sur l'endroit où tombe son paiement dans le classement. [L4 slide 17]
   Histoire : « il pondère les états par leur rang » — Si le premier état paie le moins et le troisième le plus, les probabilités cumulées valent 0,2, 0,5 et 1, et chaque état pèse le saut qu'y fait la déformation de la théorie cumulative des perspectives, $\varphi$ avec $\beta=0{,}7$, appliquée ici comme dans la pondération par le rang, aux chances cumulées depuis le pire état : $\varphi(0{,}2)=0{,}2560$, $\varphi(0{,}5)-\varphi(0{,}2)=0{,}2013$ et $1-\varphi(0{,}5)=0{,}5426$, au lieu de 0,2, 0,3 et 0,5. Le pire et le meilleur état pèsent plus que leur probabilité, celui du milieu moins. [ajout]

3. dup/prix-par-unite-de-poids
   Qu'est-ce qui décide alors de l'allocation entre les états, à la place du prix rapporté à la probabilité ? [L4 slide 28]
   Histoire : « coûte 0,3, 0,3 et 0,4 » — Rapportés aux probabilités, ces prix valent 1,5, 1 et 0,8 ; rapportés aux poids, 1,17, 1,49 et 0,74. C'est ce second rapport qui décide de l'allocation : l'état du milieu devient le plus cher. [ajout]

4. dup/regroupement-des-etats
   La solution peut ne pas respecter l'ordre qu'on avait supposé pour calculer les poids. [L4 slide 31, L4 slide 33]
   Suite : Avec ces rapports, l'investisseur voudrait recevoir moins dans l'état du milieu que dans le premier, contre l'ordre supposé pour calculer les poids. Que faire ? [ajout]
   Histoire : « contre l'ordre supposé pour calculer les poids » — On donne le même paiement $a$ aux deux états qui se disputent le rang, et l'on traite le bloc comme un seul résultat : de probabilité 0,5, il coûte 0,6 et pèse $\varphi(0{,}5)\approx0{,}457$. Avec l'utilité du cours, $u(x)=x^{0{,}6}$, et le budget $0{,}6a+0{,}4b=1$, les deux mauvais états reçoivent 0,437 chacun, et le meilleur 1,845. Cette solution vaut 1,0618, plus que les meilleures solutions des autres ordres, à 1,0405 et 1,0021. [ajout]

5. dup/assurance-de-portefeuille
   Ce qui en résulte ressemble à un produit que l'on connaît : un plancher de protection en bas, et plus de richesse dans le meilleur état. [L4 slide 32]
   Histoire : « qu'il pondère les états par leur rang » — Sous l'utilité espérée, il recevrait 0,328, 0,903 et 1,577 ; en pondérant par le rang, 0,437, 0,437 et 1,845. Plus dans le pire état et dans le meilleur, moins au milieu : un plancher plat, comme une assurance de portefeuille. [ajout]

6. dup/demande-cara-normale
   Seconde moitié, sur un marché : il faut d'abord la demande d'un investisseur ordinaire qui connaît la loi du paiement. [L4 slide 63]
   Suite : Passons à un marché plus simple : un actif risqué coûte 100 et paie en moyenne 110, avec un écart type de 20, selon une loi gaussienne. Combien en achète un investisseur qui connaît cette loi ? [ajout]
   Histoire : « Combien en achète un investisseur qui connaît cette loi » — Avec l'utilité exponentielle du cours, $u(W)=-e^{-W}$, dont l'aversion absolue vaut 1 à toute richesse, son équivalent certain se calcule à la main, et la position optimale est l'écart entre la moyenne et le prix, divisé par la variance fois cette aversion : $10/(1\times400)=0{,}025$. [L4 slide 63, ajout]

7. dup/demande-sous-ambiguite
   Jusqu'ici, l'investisseur connaît la loi du paiement. [L4 slide 64, L4 slide 65]
   Suite : Un second investisseur ne connaît la moyenne du paiement qu'à 5 près : entre 105 et 115. Combien achète-t-il ? [ajout]
   Histoire : « Combien achète-t-il » — Il juge un achat sous la moyenne la plus basse, 105, et une vente sous la plus haute, 115. Au prix 100, il achète $5/400=0{,}0125$, deux fois moins que le premier ; entre 105 et 115, il ne fait rien. [ajout]

8. dup/equilibre-sous-ambiguite
   Reste le prix que fixe le marché. [L4 slide 66]
   Suite : Le marché réunit pour moitié des investisseurs de chaque sorte, et chacun doit en moyenne absorber 0,005 unité de l'actif. À quel prix le marché s'équilibre-t-il ? [ajout]
   Histoire : « À quel prix le marché s'équilibre-t-il » — Si les ambigus ne détiennent rien, les autres, qui sont la moitié du marché, doivent tout absorber : $\tfrac12(110-p)/400=0{,}005$ donne $p=106$. Ce prix est compris entre 105 et 115 : les ambigus restent bien à l'écart, et 106 est le prix d'équilibre. [ajout]

## Point d'arrivée
La pondération par rang produit une assurance de portefeuille que l'utilité espérée ne produit pas. L'ambiguïté produit des plages de prix où l'on n'échange pas, et elle déplace l'équilibre du marché. [ajout]

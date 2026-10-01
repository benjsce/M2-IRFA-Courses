---
id: cs/parcours-prevision
ordre: 2
titre: Prévoir avec une information partielle
source: slides, §0.4 Conditional expectation (slides 1–7)
---

## Point de départ
On lance deux fois une pièce équilibrée et l'on compte les piles, $X$ : $2$, $1$, $1$ ou $0$ selon les quatre résultats PP, PF, FP, FF, chacun de probabilité ¼. On a vu le premier lancer, pas encore le second. Quelle prévision faire de $X$ avec ce qu'on sait ? [ajout]

## À savoir avant
- cs/independance-gaussienne : elle sert à la dernière étape, quand le récit revient au couple gaussien du parcours précédent ; c'est elle qui permet de couper $X_2$ en une part proportionnelle à $X_1$ et une part indépendante de $X_1$. [Cor. 0.3.1]

## Étapes
1. cs/esperance-conditionnelle
   Avant le second lancer, $X$ n'est pas connu ; la prévision ne peut utiliser que le premier. [Déf. 0.4.1]
   Histoire : « Quelle prévision faire de $X$ avec ce qu'on sait » — L'information est le premier lancer. La prévision ne peut dépendre que de lui, et sur chacun de ses deux cas elle doit avoir la même moyenne que $X$ : si le premier lancer a donné pile, $X$ vaut $2$ ou $1$, et la prévision vaut $1{,}5$ ; s'il a donné face, $X$ vaut $1$ ou $0$, et elle vaut $0{,}5$. [Déf. 0.4.1, ajout]

2. cs/esperance-conditionnelle-sachant-une-variable
   Toute l'information tient ici dans le résultat d'un seul lancer. [Déf. 0.4.2]
   Suite : Notons $Y$ ce résultat, $1$ pour pile et $0$ pour face. Peut-on écrire la prévision comme une formule en $Y$ ? [ajout]
   Histoire : « une formule en $Y$ » — Oui : conditionner par le premier lancer, c'est conditionner par l'information que porte $Y$, et la prévision est une fonction de $Y$, $E[X|Y]=\tfrac12+Y$, qui redonne $1{,}5$ pour $Y=1$ et $0{,}5$ pour $Y=0$. [Déf. 0.4.2, Rem. 0.4.3, ajout]

3. cs/proprietes-heritees-de-l-esperance
   Faire un tableau des cas pour chaque nouvelle quantité deviendra vite impraticable. [Prop. 0.4.1]
   Suite : On voudra prévoir d'autres quantités que $X$, son carré par exemple. Peut-on calculer avec la prévision comme avec une espérance ordinaire ? [ajout]
   Histoire : « calculer avec la prévision comme avec une espérance ordinaire » — Oui, à un ensemble négligeable près : elle est linéaire, croissante, passe aux limites et vérifie Jensen. Si le premier lancer a donné pile, $X^2$ vaut $4$ ou $1$ et se prévoit par $2{,}5$, tandis que le carré de la prévision de $X$ vaut $1{,}5^2=2{,}25$ : Jensen le garantissait, $2{,}25\le2{,}5$. [Prop. 0.4.1, ajout]

4. cs/sortir-ce-qui-est-connu
   La linéarité permet de couper $X$ en morceaux et de prévoir chacun. [Prop. 0.4.1 b)]
   Suite : Le nombre de piles se coupe en deux, $X=Y+(X-Y)$ : la part du premier lancer, déjà vue, et celle du second. Que devient, dans la prévision, la part déjà vue ? [ajout]
   Histoire : « la part déjà vue » — Elle sort telle quelle : $Y$ est connue de l'information, donc sa prévision est elle-même, $E[Y|Y]=Y$. Il en va de même d'un facteur connu dans un produit : $E[YX|Y]=Y\,E[X|Y]$, qui vaut $1{,}5$ si pile et $0$ si face. [Prop. 0.4.2 b), Prop. 0.4.2 c), ajout]

5. cs/role-de-l-independance
   Reste l'autre morceau, que le premier lancer n'annonce en rien. [Prop. 0.4.2 d)]
   Histoire : « celle du second » — Le second lancer est indépendant du premier : voir $Y$ ne change rien à sa loi, et sa prévision est sa moyenne, $E[X-Y|Y]=\tfrac12$. Les deux morceaux réunis redonnent $E[X|Y]=Y+\tfrac12$, sans tableau. [Prop. 0.4.2 d), ajout]

6. cs/lemme-de-gel
   Couper en morceaux ne marche que si les lancers sont séparés dans la quantité à prévoir. [Prop. 0.4.3]
   Suite : Dans le carré du nombre de piles, $X^2=\big((X-Y)+Y\big)^2$, les deux lancers sont mêlés. Comment le prévoir sans tableau ? [ajout]
   Histoire : « les deux lancers sont mêlés » — On fige le premier lancer à sa valeur $y$ et l'on moyenne sur le second seul : avec $\Phi(x,y)=(x+y)^2$, $\psi(y)=E[\Phi(X-Y,y)]$ vaut $\tfrac12\times4+\tfrac12\times1=2{,}5$ pour $y=1$ et $\tfrac12\times1+\tfrac12\times0=0{,}5$ pour $y=0$. La prévision de $X^2$ est $\psi(Y)$, et l'on retrouve le $2{,}5$ du tableau. [Prop. 0.4.3, ajout]

7. cs/propriete-de-la-tour
   Toutes ces prévisions sont faites après le premier lancer. [Prop. 0.4.2 e)]
   Suite : Avant le premier lancer, on ne savait rien. Si l'on moyenne la prévision d'après le premier lancer avec cette information vide, que trouve-t-on ? [ajout]
   Histoire : « Si l'on moyenne la prévision d'après le premier lancer avec cette information vide » — On trouve la prévision qu'on aurait faite avant tout lancer : $\tfrac12\times1{,}5+\tfrac12\times0{,}5=1$, qui est $E[X]=\tfrac14(2+1+1+0)$. Prévoir en deux temps ou directement avec l'information la plus pauvre donne le même résultat. [Prop. 0.4.2 a), Prop. 0.4.2 e), ajout]

8. cs/esperance-conditionnelle-gaussienne
   Avec la pièce, la prévision se lisait dans un tableau de cas ; avec des variables continues, il n'y a plus de tableau. [Prop. 0.4.4]
   Suite : On revient au couple gaussien du récit précédent, $X_1$ de moyenne $0$, $X_2$ de moyenne $1$, toutes deux de variance $1$, de covariance ½. On a vu $X_1$ ; quelle prévision faire de $X_2$ ? [ajout]
   Histoire : « quelle prévision faire de $X_2$ » — $X_2=\tfrac12X_1+\big(X_2-\tfrac12X_1\big)$ : la première part est connue et sort, la seconde est indépendante de $X_1$ et se prévoit par sa moyenne, $1$. Donc $E[X_2|X_1]=1+\tfrac12X_1$ : si l'on voit $X_1=2$, on prévoit $X_2=2$. Dans un vecteur gaussien, la prévision est affine. [Prop. 0.4.4, ajout]

## Point d'arrivée
Prévoir avec une information, c'est moyenner sur ce que l'information ne distingue pas. On le calcule sans tableau : ce qui est connu sort, ce qui est indépendant se prévoit par sa moyenne, et quand les deux sont mêlés on fige l'un pour moyenner l'autre. Dans un monde gaussien, la prévision est une fonction affine de ce qu'on a vu. [ajout]

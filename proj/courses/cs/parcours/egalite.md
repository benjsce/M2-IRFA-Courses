---
id: cs/parcours-egalite
ordre: 3
titre: Quand deux processus sont-ils le même ?
source: slides, §0.5 Stochastic processes (slides 1–4)
---

## Point de départ
On tire au hasard un nombre $\omega$ entre $0$ et $1$, uniformément, et l'on note, à chaque instant $t$ entre $0$ et $1$, la valeur $\omega+t$ : pour $\omega=0{,}3$, on note $0{,}3$ au départ et $1{,}3$ à la fin. Qu'est-ce, mathématiquement, que cette valeur aléatoire à chaque instant ? [§0.5 slide 4, ajout]

## Étapes
1. cs/processus-stochastique
   Il faut un objet qui soit à la fois aléatoire et fonction du temps. [Déf. 0.5.1]
   Histoire : « cette valeur aléatoire à chaque instant » — C'est un processus stochastique, $X_t(\omega)=\omega+t$. À $t$ fixé, c'est une variable aléatoire : $X_{0,5}$ est uniforme entre $0{,}5$ et $1{,}5$. À $\omega$ fixé, c'est une trajectoire : pour $\omega=0{,}3$, la droite qui va de $0{,}3$ à $1{,}3$. [Déf. 0.5.1, §0.5 slide 4, ajout]

2. cs/processus-de-meme-loi
   Un processus ne se dit pas seulement ; il se compare à d'autres. [Déf. 0.5.2]
   Suite : Un deuxième observateur part du même tirage mais note $(1-\omega)+t$ : pour $\omega=0{,}3$, il note $0{,}7$ au départ. Ses relevés ont-ils, à toutes dates, les mêmes probabilités que ceux du premier ? [ajout]
   Histoire : « Ses relevés ont-ils, à toutes dates, les mêmes probabilités que ceux du premier » — Oui : $1-\omega$ est uniforme comme $\omega$, et à toutes dates $t_1,\dots,t_n$ les relevés des deux observateurs ont la même loi jointe. Les deux processus ont même loi, et pourtant, pour $\omega=0{,}3$, l'un part de $0{,}3$ et l'autre de $0{,}7$. [Déf. 0.5.2, ajout]

3. cs/version-d-un-processus
   Avoir les mêmes probabilités ne dit pas que les relevés coïncident dans un même tirage. [Déf. 0.5.3]
   Suite : Un troisième observateur note $\omega+t$ comme le premier, mais à l'instant $t=\omega$, distrait, il écrit $0$. À un instant donné, ses relevés coïncident-ils avec ceux du premier ? [§0.5 slide 4, ajout]
   Histoire : « À un instant donné, ses relevés coïncident-ils avec ceux du premier » — Presque sûrement : à $t$ fixé, il n'écrit $0$ que si le tirage $\omega$ tombe exactement sur $t$, ce qui arrive avec probabilité nulle. Son processus $Y$ est une version de $X$. [Déf. 0.5.3, §0.5 slide 4]

4. cs/processus-continu
   Les deux relevés se ressemblent instant par instant ; on regarde maintenant leur dessin. [Déf. 0.5.5]
   Suite : Le relevé du premier observateur se trace sans lever le crayon. Celui du troisième aussi ? [ajout]
   Histoire : « se trace sans lever le crayon » — Pour le premier, oui : chaque trajectoire de $X$ est une droite, et $X$ est un processus continu. Pour le troisième, non : sa trajectoire tombe à $0$ en $t=\omega$ puis revient, et $Y$ n'est pas continu. [Déf. 0.5.5, §0.5 slide 4]

5. cs/processus-indistinguables
   Une version compare les relevés instant par instant, jamais sur toute la durée à la fois. [Déf. 0.5.4]
   Suite : Sur toute la durée, le relevé du troisième est-il, presque sûrement, celui du premier ? [ajout]
   Histoire : « Sur toute la durée, le relevé du troisième est-il, presque sûrement, celui du premier » — Non : chaque trajectoire de $Y$ a son trou, en $t=\omega$, et ne coïncide avec celle de $X$ que pour $\omega=0$ ; la probabilité qu'elles coïncident partout est nulle, et $X$ et $Y$ ne sont pas indistinguables. Si les deux relevés étaient continus, coïncider à chaque instant suffirait : ils coïncideraient aux instants rationnels, puis partout. [Déf. 0.5.4, §0.5 slide 4]

## Point d'arrivée
Deux processus peuvent être « le même » de trois façons, de plus en plus fortes : avoir même loi, être une version l'un de l'autre, être indistinguables. La différence entre les deux dernières est celle d'un ensemble négligeable par instant ou d'un seul pour tous les instants, et la continuité des trajectoires l'efface. [§0.5 slide 3, §0.5 slide 4]

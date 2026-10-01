---
id: cs/parcours-integrer
ordre: 4
titre: Les mises qu'on saura intégrer
source: slides, §0.5 Stochastic processes (slides 5–12)
---

## Point de départ
Un joueur fixe sa mise à chaque instant $t$ entre $0$ et $1$. Une pièce est lancée en $t=\tfrac12$, une autre en $t=1$. Il mise $1$ jusqu'à $\tfrac12$, puis $2$ si la première pièce tombe sur pile et $0$ si elle tombe sur face. À chaque instant, que sait-il ? [ajout]

## À savoir avant
- cs/processus-stochastique : la mise du joueur en est un, une valeur aléatoire à chaque instant ; c'est sur lui que portent toutes les exigences du récit. [Déf. 0.5.1]
- cs/version-d-un-processus : elle sert à l'étape de la filtration complète, pour un joueur dont la mise ne diffère de celle du premier que sur un événement de probabilité nulle. [Déf. 0.5.3]
- cs/processus-continu : il fournit le critère pratique de la mesurabilité progressive, continu et adapté ; la mise du joueur, qui saute en $\tfrac12$, n'en profite pas. [Prop. 0.5.1]

## Étapes
1. cs/filtration
   Avant de juger une mise, il faut dire ce que le joueur sait à chaque instant. [Déf. 0.5.8]
   Histoire : « À chaque instant, que sait-il » — Avant $\tfrac12$, rien ; entre $\tfrac12$ et $1$, le résultat de la première pièce ; en $1$, celui des deux. L'information grandit sans rien perdre : sur les quatre résultats PP, PF, FP, FF, elle forme un bloc, puis deux, puis quatre. C'est la filtration $(\mathcal F_t)$. [Déf. 0.5.8, ajout]

2. cs/processus-adapte
   On peut maintenant confronter chaque mise à cette information. [Déf. 0.5.9]
   Suite : Un autre joueur misait $2$ dès le début lorsque la première pièce allait tomber sur pile. Sa mise se décide-t-elle avec ce qu'il sait ? [ajout]
   Histoire : « Sa mise se décide-t-elle avec ce qu'il sait » — Non : avant $\tfrac12$, sa mise dépend de la première pièce, que $\mathcal F_t$ ignore encore. Celle du premier joueur, au contraire, se lit à chaque instant sur l'information de cet instant : elle est adaptée. [Déf. 0.5.9, ajout]

3. cs/filtration-naturelle
   L'information du joueur vient des pièces ; on peut aussi la tirer de la mise elle-même. [Rem. 0.5.4]
   Suite : Un spectateur ne voit pas les pièces, seulement la mise du premier joueur. Que sait-il à chaque instant ? [ajout]
   Histoire : « Que sait-il à chaque instant » — Rien avant $\tfrac12$, puis le résultat de la première pièce, qu'il lit sur le passage de la mise à $2$ ou à $0$ ; jamais celui de la seconde, dont la mise ne dépend pas. C'est la filtration naturelle de la mise, la plus pauvre à laquelle elle soit adaptée. [Rem. 0.5.4, ajout]

4. cs/filtration-complete
   Reste un cas limite, celui d'un avenir qui n'arrive jamais. [Rem. 0.5.3]
   Suite : Un dernier joueur mise comme le premier, sauf qu'il mise $5$ jusqu'à $\tfrac12$ si la première pièce va retomber sur la tranche, ce qui a une probabilité nulle. Faut-il le compter comme un joueur qui regarde l'avenir ? [ajout]
   Histoire : « Faut-il le compter comme un joueur qui regarde l'avenir » — Non, si l'on complète la filtration : sa mise ne diffère de celle du premier que sur un événement négligeable, c'en est une version. Une fois les événements négligeables ajoutés à chaque $\mathcal F_t$, toute version d'une mise adaptée est adaptée. [Rem. 0.5.5, ajout]

5. cs/processus-mesurable
   Le gain du joueur sera une intégrale de sa mise ; il faut d'abord pouvoir intégrer. [Déf. 0.5.6]
   Suite : Commençons par la mise cumulée, $\int_0^tX_s\,ds$. Est-ce bien une variable aléatoire ? [§0.5 slide 5, ajout]
   Histoire : « Est-ce bien une variable aléatoire » — Oui, si la mise est mesurable en $(t,\omega)$ ensemble : on intègre alors chaque trajectoire, et le résultat dépend de $\omega$ de façon mesurable. Ici la mise cumulée vaut $t$ avant $\tfrac12$, puis $\tfrac12+2\big(t-\tfrac12\big)$ ou $\tfrac12$ selon la première pièce. [Déf. 0.5.6, §0.5 slide 5, ajout]

6. cs/espace-l2-des-processus
   Pour comparer deux mises, ou en approcher une par une autre, il faut une distance. [Déf. 0.5.7]
   Suite : Quelle taille donner à une mise, sur toute la partie et dans tous les cas ? [ajout]
   Histoire : « Quelle taille donner à une mise » — Le carré de la mise, intégré sur la partie puis moyenné sur les cas : $E\big[\int_0^1X_s^2\,ds\big]=\tfrac12\times1+\tfrac12\times\big(\tfrac12\times4+\tfrac12\times0\big)=1{,}5$. Il est fini : la mise est dans $L^2(\Omega\times[0,1])$. [Déf. 0.5.7, ajout]

7. cs/processus-progressivement-mesurable
   Être une variable aléatoire ne suffit pas au joueur : il doit savoir où il en est. [Déf. 0.5.10]
   Suite : La mise cumulée doit être connue du joueur à chaque instant. Que faut-il demander à la mise pour cela ? [§0.5 slide 11, ajout]
   Histoire : « La mise cumulée doit être connue du joueur à chaque instant » — Qu'elle soit mesurable en $(t,\omega)$ sur chaque intervalle $[0,u]$ avec la seule information de la date $u$ : c'est la mesurabilité progressive, et elle rend $\int_0^tX_s\,ds$ connue en $t$, par Fubini. La mesurabilité seule ignorait l'information, l'adaptation seule ne regardait qu'un instant à la fois : il faut les deux ensemble, sur tout le passé. [Déf. 0.5.10, §0.5 slide 11, ajout]

8. cs/processus-elementaire
   La mise du joueur a une forme particulière, qui rend toutes ces vérifications faciles. [§0.5 slide 11]
   Suite : Elle est constante entre deux dates de révision, et révisée avec ce que le joueur sait à ces dates. Comment s'écrit une telle mise ? [ajout]
   Histoire : « Comment s'écrit une telle mise » — Comme une somme de marches : $X_t=F_{t_1}1_{[0,\frac12[}(t)+F_{t_2}1_{[\frac12,1[}(t)$, avec $F_{t_1}=1$, connue en $0$, et $F_{t_2}$ égale à $2$ ou $0$, connue en $\tfrac12$. C'est un processus élémentaire, progressivement mesurable marche par marche. [§0.5 éq. 1, §0.5 slide 11, ajout]

9. cs/espace-l2-progressif
   Les deux exigences du récit, la taille finie et le respect de l'information, se réunissent. [Déf. 0.5.11]
   Suite : Les mises qu'on voudra autoriser sont celles qui ne regardent pas l'avenir et dont la taille est finie. Comment appeler leur ensemble ? [ajout]
   Histoire : « celles qui ne regardent pas l'avenir et dont la taille est finie » — $L^2_{prog}(\Omega\times[0,1])$ : les processus progressivement mesurables de taille finie. La mise du joueur en fait partie, avec une taille de $1{,}5$. [Déf. 0.5.11, ajout]

10. cs/densite-des-processus-elementaires
   Les mises élémentaires sont commodes ; toutes les mises ne le sont pas. [Th. 0.5.2]
   Suite : Un joueur pourrait réviser sa mise à chaque instant, par exemple miser $t$ à l'instant $t$. Une telle mise se laisse-t-elle approcher par des mises révisées à quelques dates seulement ? [ajout]
   Histoire : « se laisse-t-elle approcher par des mises révisées à quelques dates seulement » — Oui : en misant, sur chaque période de longueur $\tfrac1n$, la valeur du début de la période, l'écart $E\big[\int_0^1(X_s-X^n_s)^2\,ds\big]$ vaut $\tfrac1{3n^2}$, soit $\tfrac1{12}$ pour deux périodes et $\tfrac1{48}$ pour quatre. Toute mise de $L^2_{prog}$ s'approche ainsi par des processus élémentaires, et l'espace est complet : le gain, défini d'abord pour les mises élémentaires, s'étendra à toutes par passage à la limite. [Th. 0.5.2, ajout]

## Point d'arrivée
Une mise qu'on saura intégrer est un processus progressivement mesurable de carré intégrable : elle ne regarde pas l'avenir, et sa taille est finie. Les mises élémentaires, révisées à des dates fixes avec l'information de ces dates, approchent toutes les autres ; c'est sur elles que le gain s'écrira d'abord. [Th. 0.5.2]

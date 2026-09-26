---
id: fpp/parcours-terme
ordre: 3
titre: Fixer aujourd'hui le prix d'un échange futur
source: poly, §2.3–§4.2
---

## Point de départ
Une action vaut 100 aujourd'hui et le taux sans risque à un an est de 4 %. À quel prix faut-il s'engager aujourd'hui à l'acheter dans un an ? La réponse ne demande aucune prévision sur l'action. [ajout]

## À savoir avant
- fpp/facteur-actualisation : c'est lui qui transporte le prix comptant jusqu'à l'échéance, dans chaque formule de prix à terme de ce parcours. [Prop. 2]
- fpp/valeur-actuelle-nette : elle dit ce que vaut aujourd'hui un échange futur, et c'est parce qu'elle est nulle à la signature que le prix à terme se détermine. [§2.3]
- fpp/taux-forward : c'est le taux d'un emprunt futur, un nombre lu dans la courbe au parcours précédent ; le FRA, raconté plus loin, permet de se l'assurer. [§2.3, Déf. 7]
- fpp/taux-de-change : c'est le prix d'une devise pour un échange fait aujourd'hui ; le forward de change, raconté plus loin, en fixe un pour un échange futur. [§2.4]

## Étapes
1. fpp/absence-arbitrage
   La réponse repose sur un seul principe, qui interdit de gagner sans risque et sans mise. [§3.1]
   Histoire : « La réponse ne demande aucune prévision sur l'action » — Elle ne demande qu'un principe : deux façons d'obtenir l'action dans un an qui donnent le même flux quoi qu'il arrive doivent coûter la même chose aujourd'hui. Sinon, on achèterait la moins chère en vendant l'autre, et l'on gagnerait sans risque ni mise. [ajout]

2. fpp/replication
   Ce principe se met en œuvre par un geste unique : fabriquer le flux futur avec ce qu'on peut acheter aujourd'hui. [§3.1]
   Histoire : « s'engager aujourd'hui à l'acheter dans un an » — Plutôt que de deviner ce que vaudra l'action dans un an, on fabrique le même engagement avec ce qui s'achète aujourd'hui, et l'on en lit le coût. [ajout]

3. fpp/replication-statique
   Pour livrer une action dans un an, la façon la plus simple est aussi la plus directe. [§3.1]
   Histoire : « Une action vaut 100 aujourd'hui et le taux sans risque à un an est de 4 % » — Emprunter 100, acheter l'action et la garder un an : on détient l'action et l'on doit 100 plus les intérêts, $100/0{,}9608\approx104{,}08$, puisqu'à 4 % continu un euro dû dans un an vaut 0,9608 aujourd'hui. S'engager à l'acheter à ce prix revient exactement au même. [ajout]

4. fpp/portage
   Détenir l'action jusqu'à l'échéance n'est pas neutre : elle peut verser des dividendes pendant ce temps. [§3.2]
   Suite : L'action verse, avant l'échéance, un dividende égal à 2 % de sa valeur. Combien d'actions faut-il acheter aujourd'hui pour en avoir exactement une dans un an ? [ajout]
   Histoire : « Combien d'actions faut-il acheter aujourd'hui » — Réinvesti en actions, le dividende fait grossir la position d'environ 2 % : il suffit d'en acheter environ 2 % de moins, $1-0{,}02=0{,}98$, pour en avoir une dans un an. Ce 0,98 est le portage. [ajout]

5. fpp/contrat-prime-nulle
   Le contrat qu'on cherche à évaluer ne coûte rien à la signature. Qu'est-ce qu'on cherche alors, si ce n'est pas un prix ? [§2.3, §3.1]
   Histoire : « À quel prix faut-il s'engager » — S'engager ne coûte rien à la signature : ni l'acheteur ni le vendeur ne paie. Ce qu'on cherche n'est donc pas le prix du contrat, qui est nul, mais le prix $K$ inscrit dedans, celui qui le rend nul. [ajout]

6. fpp/prix-a-terme
   La réplication et l'absence d'arbitrage donnent la réponse d'un coup, pour une famille entière de contrats. [Prop. 2, Prop. 3]
   Histoire : « à l'acheter dans un an » — La réponse tient en une formule, $K=S_t\Phi/D$ : le prix comptant $S_t$, multiplié par le portage $\Phi$, et divisé par le facteur d'actualisation $D$, qui le transporte jusqu'à l'échéance. Sans dividende, $\Phi=1$ et $D=0{,}9608$ : $100\times1/0{,}9608\approx104{,}08$. [ajout]

7. fpp/forward-action
   Premier membre de la famille, le cas de départ : une action livrée à terme. [§3.1, §3.2]
   Histoire : « un dividende égal à 2 % de sa valeur » — Avec ce dividende, le prix à terme de l'action, ce $K$ que le cours note $F(t,T)$ pour une action, baisse : $F(t,t+1)=100\times0{,}98/0{,}9608\approx102{,}00$, contre 104,08 sans dividende. [ajout]

8. fpp/forward-de-change
   Le même raisonnement vaut quand ce qu'on livre est une devise. [§2.4]
   Suite : Un exportateur recevra des dollars dans un an. Un euro vaut aujourd'hui 1,10 dollar, et le taux sans risque est de 2 % sur le dollar, soit un zéro-coupon à 0,9802. À quel taux de change peut-il s'engager dès aujourd'hui ? [ajout]
   Histoire : « À quel taux de change peut-il s'engager » — Le taux de change du jour, 1,10, ne vaut que pour un échange fait aujourd'hui ; celui qui s'appliquera dans un an n'est pas connu. Un taux fixé dès aujourd'hui pour un échange dans un an s'appelle un forward de change, et il se trouve comme pour l'action : en fabriquant soi-même l'échange. Pour disposer d'un euro dans un an, on achète aujourd'hui le zéro-coupon en euros, 0,9608 euro, soit $1{,}10\times0{,}9608\approx1{,}0569$ dollar, qu'on emprunte. Dans un an, on reçoit l'euro et l'on rembourse l'emprunt en dollars : $1{,}0569/0{,}9802\approx1{,}0782$, puisqu'un dollar emprunté aujourd'hui se rembourse $1/0{,}9802$ dans un an. Un euro livré dans un an coûte donc 1,0782 dollar sans risque : c'est le taux qui ne fait ni gagner ni perdre, $K(t,t+1)\approx1{,}0782$ dollar par euro. [ajout]

9. fpp/fra
   Et quand ce qu'on fixe à l'avance est un taux d'emprunt. [§2.3, Déf. 7]
   Suite : Une entreprise devra emprunter dans un an, pour un an ; le marché cote 0,9608 un euro payé dans un an et 0,9048 un euro payé dans deux ans. Quel taux peut-elle fixer dès aujourd'hui ? [ajout]
   Histoire : « Quel taux peut-elle fixer dès aujourd'hui » — Le FRA, *forward rate agreement*, est le contrat qui le fixe : il engage à recevoir 1 dans un an et à rendre $e^{K}$ dans deux ans. Comme il ne coûte rien à la signature, ses deux flux valent autant aujourd'hui, $0{,}9608=0{,}9048\,e^{K}$, d'où $K=\ln(0{,}9608/0{,}9048)\approx6\,\%$. C'est le taux forward entre un et deux ans, que la courbe donnait déjà au parcours « Comparer des flux séparés par le temps ou la devise » : la courbe le fait lire, le FRA le fait obtenir. [ajout]

10. fpp/compte-capitalise
    Le contrat à terme le plus échangé en bourse, le future, ne se règle pas en une fois à l'échéance : chaque jour, il verse à l'un ou à l'autre la variation de son prix. Ces règlements doivent être replacés, à des taux qu'on ne connaît pas encore. Comment transporter de la valeur dans ces conditions ? [§4.1, §4.2]
    Suite : Revenons à l'action qui verse 2 % de dividende, mais sur un marché de futures : chaque règlement se place au taux du jour, qu'on ne connaît pas à l'avance. Comment transporter de l'argent jusqu'à l'échéance dans ces conditions ? [ajout]
    Histoire : « qu'on ne connaît pas à l'avance » — On le place au jour le jour, en enchaînant les zéro-coupons courts, dont seul le premier est connu aujourd'hui : c'est le compte capitalisé. Un euro y devient $1/B(t,T)$ à l'échéance, avec $B(t,T)=\prod_kP(t_k,t_{k+1})$, le produit des prix de ces zéro-coupons. Pour voir l'enchaînement, prenons deux ans et des pas d'un an : si le taux vaut 4 % la première année puis 6 % la seconde, $B(t,t+2)=e^{-0{,}04}e^{-0{,}06}\approx0{,}9048$, et l'euro devient environ 1,105. [ajout]

11. fpp/replication-dynamique
    La réplication ne peut plus être posée une fois pour toutes : il faut la réajuster à chaque pas. [§4.2.2]
    Histoire : « chaque règlement se place au taux du jour » — On veut qu'à chaque date la stratégie vaille le prix du future multiplié par ce qu'est devenu un euro placé au compte capitalisé depuis $t_0=t$ ; comme les règlements y sont replacés, le nombre de contrats doit grossir au même rythme : on en détient $1/B(t_0,t_{i+1})$ en $t_i$, nombre connu dès $t_i$ puisque seul le taux de la période qui commence s'y ajoute. Avec les taux de l'étape précédente, $1/0{,}9608\approx1{,}0408$ contrat la première année, puis $1/0{,}9048\approx1{,}1052$ la seconde ; à l'échéance, la stratégie vaut le prix de l'action multiplié par 1,105. [ajout]

12. fpp/prix-future
    Le prix du contrat future s'en déduit. Coïncide-t-il avec le prix forward ? [§4.2]
    Histoire : « Revenons à l'action qui verse 2 % de dividende, mais sur un marché de futures » — Tant que les taux sont connus d'avance, le prix du future à un an sur l'action est celui du forward : 102,00 (104,08 si elle ne versait rien). Il ne s'en écarte que lorsque les taux futurs sont eux-mêmes aléatoires. [ajout]

## Point d'arrivée
Le prix d'un échange futur ne dépend d'aucune prévision : il est fixé par ce que coûte aujourd'hui sa réplication, statique pour un forward, dynamique pour un future. [ajout]

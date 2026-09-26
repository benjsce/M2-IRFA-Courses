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
- fpp/taux-forward : c'est le taux que le FRA fixe aujourd'hui pour un emprunt futur. [§2.3, Déf. 7]
- fpp/taux-de-change : c'est la grandeur que le forward de change fixe à terme. [§2.4]

## Étapes
1. fpp/absence-arbitrage
   La réponse repose sur un seul principe, qui interdit de gagner sans risque et sans mise. [§3.1]
   Histoire : « La réponse ne demande aucune prévision sur l'action » — Elle ne demande qu'un principe : deux façons d'obtenir l'action dans un an qui donnent le même flux quoi qu'il arrive doivent coûter la même chose aujourd'hui. Sinon, on achèterait la moins chère en vendant l'autre, et l'on gagnerait sans risque ni mise. [ajout]

2. fpp/replication
   Ce principe se met en œuvre par un geste unique : fabriquer le flux futur avec ce qu'on peut acheter aujourd'hui. [§3.1]
   Histoire : « s'engager aujourd'hui à l'acheter dans un an » — Plutôt que de deviner ce que vaudra l'action dans un an, on fabrique le même engagement avec ce qui s'achète aujourd'hui, et l'on en lit le coût. [ajout]

3. fpp/replication-statique
   Pour livrer une action dans un an, la façon la plus simple est aussi la plus directe. [§3.1]
   Histoire : « Une action vaut 100 aujourd'hui et le taux sans risque à un an est de 4 % » — Emprunter 100, acheter l'action et la garder un an : on détient l'action et l'on doit $100/0{,}9608\approx104{,}08$. S'engager à l'acheter à ce prix revient exactement au même. [ajout]

4. fpp/portage
   Détenir l'action jusqu'à l'échéance n'est pas neutre : elle peut verser des dividendes pendant ce temps. [§3.2]
   Suite : L'action verse, avant l'échéance, un dividende égal à 2 % de sa valeur. Combien d'actions faut-il acheter aujourd'hui pour en avoir exactement une dans un an ? [ajout]
   Histoire : « Combien d'actions faut-il acheter aujourd'hui » — Réinvesti en actions, le dividende fait grossir la position : il suffit d'en acheter environ 0,98 aujourd'hui pour en avoir une dans un an. Ce 0,98 est le portage. [ajout]

5. fpp/contrat-prime-nulle
   Le contrat qu'on cherche à évaluer ne coûte rien à la signature. Qu'est-ce qu'on cherche alors, si ce n'est pas un prix ? [§2.3, §3.1]
   Histoire : « À quel prix faut-il s'engager » — S'engager ne coûte rien à la signature : ni l'acheteur ni le vendeur ne paie. Ce qu'on cherche n'est donc pas le prix du contrat, qui est nul, mais le prix $K$ inscrit dedans, celui qui le rend nul. [ajout]

6. fpp/prix-a-terme
   La réplication et l'absence d'arbitrage donnent la réponse d'un coup, pour une famille entière de contrats. [Prop. 2, Prop. 3]
   Histoire : « à l'acheter dans un an » — La réponse tient en une formule, $K=S_t\Phi/D$ : le prix comptant, multiplié par le portage, et transporté jusqu'à l'échéance par le facteur d'actualisation. Sans dividende, $100\times1/0{,}9608\approx104{,}08$. [ajout]

7. fpp/forward-action
   Premier membre de la famille, le cas de départ : une action livrée à terme. [§3.1, §3.2]
   Histoire : « un dividende égal à 2 % de sa valeur » — Avec ce dividende, le prix à terme de l'action baisse : $F(t,t+1)=100\times0{,}98/0{,}9608\approx102{,}00$, contre 104,08 sans dividende. [ajout]

8. fpp/forward-de-change
   Le même raisonnement vaut quand ce qu'on livre est une devise. [§2.4]
   Suite : Un exportateur recevra des dollars dans un an. Un euro vaut aujourd'hui 1,10 dollar, et le taux sans risque est de 2 % sur le dollar, soit un zéro-coupon à 0,9802. À quel taux de change peut-il s'engager dès aujourd'hui ? [ajout]
   Histoire : « À quel taux de change peut-il s'engager » — Le même raisonnement, avec une devise à la place de l'action : $K(t,t+1)=1{,}10\times0{,}9608/0{,}9802\approx1{,}0782$ dollar par euro. [ajout]

9. fpp/fra
   Et quand ce qu'on fixe à l'avance est un taux d'emprunt. [§2.3, Déf. 7]
   Suite : Une entreprise devra emprunter dans un an, pour un an ; le marché cote 0,9608 un euro payé dans un an et 0,9048 un euro payé dans deux ans. Quel taux peut-elle fixer dès aujourd'hui ? [ajout]
   Histoire : « Quel taux peut-elle fixer dès aujourd'hui » — Le FRA s'écrit comme un prix à terme sur un taux : $0{,}9608=0{,}9048\,e^{K}$ donne $K\approx6\,\%$, le taux forward entre un et deux ans. [ajout]

10. fpp/compte-capitalise
    Un contrat future se règle chaque jour, et chaque règlement se replace à un taux qu'on ne connaît pas encore. Comment transporter de la valeur dans ces conditions ? [§4.2.2]
    Suite : Revenons à l'action, mais sur un marché de futures : le contrat se règle chaque jour, et chaque règlement se place au taux du jour, qu'on ne connaît pas à l'avance. Comment transporter de l'argent jusqu'à l'échéance dans ces conditions ? [ajout]
    Histoire : « qu'on ne connaît pas à l'avance » — On le place au jour le jour, en enchaînant les zéro-coupons courts : un euro devient $1/B(t,T)$ à l'échéance, avec $B(t,T)=\prod_kP(t_k,t_{k+1})$. Avec 4 % la première année puis 6 % la seconde, $B(t,t+2)=e^{-0{,}04}e^{-0{,}06}\approx0{,}9048$, et l'euro devient environ 1,105. [ajout]

11. fpp/replication-dynamique
    La réplication ne peut plus être posée une fois pour toutes : il faut la réajuster à chaque pas. [§4.2.2]
    Histoire : « chaque règlement se place au taux du jour » — Chaque règlement réinvesti grossit la position ; pour qu'elle vaille à la fin exactement un contrat, il faut en détenir $1/B$, et réajuster à chaque pas. Avec trois pas à 0,99, on détient successivement 1,0101, 1,0203 puis 1,0306 contrats. [ajout]

12. fpp/prix-future
    Le prix du contrat future s'en déduit, et il ne coïncide plus exactement avec le prix forward. [§4.2]
    Histoire : « Revenons à l'action, mais sur un marché de futures » — Tant que les taux sont connus d'avance, le prix du future sur l'action est celui du forward, 104,08. Il ne s'en écarte que lorsque les taux futurs sont eux-mêmes aléatoires. [ajout]

## Point d'arrivée
Le prix d'un échange futur ne dépend d'aucune prévision : il est fixé par ce que coûte aujourd'hui sa réplication, statique pour un forward, dynamique pour un future. [ajout]

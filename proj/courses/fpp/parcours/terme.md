---
id: fpp/parcours-terme
ordre: 3
titre: Fixer aujourd'hui le prix d'un échange futur
source: poly, §2.3–§4.2
---

## Point de départ
Un investisseur veut acheter une action dans un an, à un prix convenu dès aujourd'hui avec un vendeur. L'action vaut 100 aujourd'hui, et placer ou emprunter de l'argent sans risque coûte 4 % par an. Quel prix convenir ? Faut-il, pour le fixer, deviner ce que vaudra l'action dans un an ? [ajout]

## À savoir avant
- fpp/facteur-actualisation : c'est lui qui transporte le prix comptant jusqu'à l'échéance, dans chaque formule de prix à terme de ce parcours. [Prop. 2]
- fpp/valeur-actuelle-nette : elle dit ce que vaut aujourd'hui un échange futur, et c'est parce qu'elle est nulle à la signature que le prix à terme se détermine. [§2.3]
- fpp/taux-forward : c'est le taux d'un emprunt futur, un nombre lu dans la courbe au parcours précédent ; le FRA, raconté plus loin, permet de se l'assurer. [§2.3, Déf. 7]
- fpp/taux-de-change : c'est le prix d'une devise pour un échange fait aujourd'hui ; le forward de change, raconté plus loin, en fixe un pour un échange futur. [§2.4]

## Étapes
1. fpp/contrat-prime-nulle
   Avant de chercher ce prix, il faut savoir ce qu'on cherche : l'investisseur paie-t-il quelque chose en signant ? [§2.3, §3.1]
   Histoire : « Quel prix convenir » — Rien ne se paie à la signature : l'investisseur s'engage à payer dans un an, le vendeur à lui remettre l'action ce jour-là. L'inconnue n'est donc pas le prix du contrat, qui ne coûte rien, mais le prix écrit dedans, noté $K$ : celui pour lequel aucun des deux ne fait une mauvaise affaire, c'est-à-dire pour lequel l'engagement vaut zéro aujourd'hui. [ajout]

2. fpp/absence-arbitrage
   Comment trouver ce prix sans rien savoir de l'avenir de l'action ? [§3.1]
   Histoire : « Faut-il, pour le fixer, deviner ce que vaudra l'action dans un an » — Non. Un principe suffit : deux façons d'avoir l'action dans un an qui donnent exactement la même chose, quoi qu'il arrive, doivent coûter la même chose aujourd'hui. Sinon, on prendrait la moins chère en vendant l'autre, et l'on gagnerait sans risque et sans mise ; c'est ce que le marché ne laisse pas faire. [ajout]

3. fpp/replication
   Le contrat est une façon d'avoir l'action dans un an. Pour appliquer le principe, il en faut une seconde, dont on connaisse le coût. [§3.1]
   Histoire : « acheter une action dans un an » — Cette seconde façon se fabrique avec ce qui s'achète aujourd'hui. Si ce montage donne exactement ce que donne le contrat, le principe de l'étape précédente dit que le contrat vaut ce que coûte le montage : il suffit de lire ce coût. [ajout]

4. fpp/replication-statique
   Quel montage, ici ? Le plus simple : acheter l'action tout de suite, et attendre. [§3.1]
   Histoire : « L'action vaut 100 aujourd'hui, et placer ou emprunter de l'argent sans risque coûte 4 % par an » — L'investisseur emprunte 100, achète l'action et ne fait plus rien pendant un an. Au bout de l'année, il a l'action et doit rembourser 100 plus les intérêts : à 4 % continu, $100\,e^{0{,}04}=100/0{,}9608\approx104{,}08$. C'est exactement ce que donne le contrat, l'action contre un paiement dans un an, sans rien débourser aujourd'hui : le contrat doit donc fixer $K=104{,}08$. Le vendeur fait le même montage de son côté, il emprunte pour acheter l'action aujourd'hui et la *livre* dans un an contre $K$ ; c'est de son point de vue que la fiche le décrit. [ajout]

5. fpp/portage
   Attendre un an avec l'action n'est pas toujours neutre : pendant ce temps, elle peut rapporter quelque chose. [§3.2]
   Suite : Supposons que l'action verse, avant un an, un dividende égal à 2 % de sa valeur, que l'investisseur réinvestit en actions. Combien d'actions doit-il acheter aujourd'hui pour en avoir exactement une dans un an ? [ajout]
   Histoire : « Combien d'actions doit-il acheter aujourd'hui » — Le dividende réinvesti fait grossir le nombre d'actions d'environ 2 % : il suffit d'en acheter 2 % de moins, $1-0{,}02=0{,}98$ action. Ce 0,98 est le portage. [ajout]

6. fpp/forward-action
   Le montage coûte alors moins cher. Quel prix l'investisseur doit-il donc convenir ? [§3.1, §3.2]
   Histoire : « un dividende égal à 2 % de sa valeur » — Il n'emprunte plus que de quoi acheter 0,98 action, soit 98 ; dans un an, il a une action et doit $98/0{,}9608\approx102{,}00$. Le prix à convenir baisse d'autant : 102,00 au lieu de 104,08. Quand ce qu'on achète à terme est une action, le cours note ce prix $F(t,T)$, ici $F(t,t+1)=102{,}00$. [ajout]

7. fpp/prix-a-terme
   Les deux calculs, avec et sans dividende, ont la même forme. Est-ce un hasard ? [Prop. 2, Prop. 3]
   Histoire : « pour en avoir exactement une dans un an » — Non. Dans les deux cas, on paie aujourd'hui ce qu'il faut détenir pour avoir la chose dans un an, le prix $S_t$ multiplié par le portage $\Phi$, puis on transporte cette somme jusqu'à l'échéance en la divisant par le prix du zéro-coupon, noté $D$. D'où une seule formule, $K=S_t\Phi/D$ : sans dividende, $\Phi=1$ et $K=100/0{,}9608=104{,}08$ ; avec, $\Phi=0{,}98$ et $K=102{,}00$. Elle vaut pour tout ce qui se livre à terme : c'est le prix à terme. [ajout]

8. fpp/forward-de-change
   Et si ce que l'investisseur veut recevoir dans un an n'est pas une action, mais une devise ? [§2.4]
   Suite : L'investisseur recevra aussi des dollars dans un an, qu'il voudra changer en euros. Un euro vaut aujourd'hui 1,10 dollar, et le dollar se place à 2 % par an, soit un zéro-coupon en dollars à 0,9802. À quel taux de change peut-il s'engager dès aujourd'hui ? [ajout]
   Histoire : « À quel taux de change peut-il s'engager dès aujourd'hui » — Par le même montage, l'euro prenant la place de l'action. Pour avoir un euro dans un an, il achète aujourd'hui le zéro-coupon en euros, 0,9608 euro, qu'il paie avec des dollars empruntés : $1{,}10\times0{,}9608\approx1{,}0569$ dollar. Dans un an, il reçoit l'euro et rembourse $1{,}0569/0{,}9802\approx1{,}0782$ dollar. Un euro livré dans un an coûte donc 1,0782 dollar sans risque : c'est le forward de change, $K(t,t+1)\approx1{,}0782$. Il diffère du taux du jour, 1,10, parce que l'euro et le dollar ne rapportent pas le même intérêt. [ajout]

9. fpp/fra
   Et si ce qu'il veut fixer à l'avance est le taux d'un emprunt ? [§2.3, Déf. 7]
   Suite : L'investisseur devra aussi emprunter un euro dans un an, pour un an. Le marché cote 0,9608 un euro payé dans un an, et 0,9048 un euro payé dans deux ans. Peut-il fixer dès aujourd'hui le taux de cet emprunt ? [ajout]
   Histoire : « Peut-il fixer dès aujourd'hui le taux de cet emprunt » — Oui, par un contrat appelé FRA, *forward rate agreement* : il recevra 1 dans un an et rendra $e^{K}$ dans deux ans, $K$ étant le taux fixé aujourd'hui. Le contrat ne coûte rien à la signature, donc ses deux flux valent autant aujourd'hui : $0{,}9608=0{,}9048\,e^{K}$, d'où $K=\ln(0{,}9608/0{,}9048)\approx6\,\%$. C'est le taux forward du parcours « Comparer des flux séparés par le temps ou la devise » : la courbe le fait lire, le FRA le fait obtenir. [ajout]

10. fpp/compte-capitalise
    Sur les marchés organisés, ces engagements s'échangent sous une autre forme, le *future* : au lieu de tout régler dans un an, les deux parties se versent chaque jour la variation de son prix. L'argent reçu ou payé en route doit alors être placé ou emprunté, à des taux qu'on ne connaît pas encore. [§4.2.2]
    Suite : Pour voir ce que devient cet argent, prenons deux règlements seulement, un tous les six mois. Le premier semestre, l'argent se place à 4 % par an ; au second, à un taux qu'on ignore aujourd'hui, disons 6 %. Que devient un euro placé ainsi jusqu'à l'échéance ? [ajout]
    Histoire : « Que devient un euro placé ainsi jusqu'à l'échéance » — On le place six mois, puis on replace le tout six mois : il devient $e^{0{,}02}\times e^{0{,}03}=e^{0{,}05}\approx1{,}0513$. Le facteur qui ramène de l'échéance à aujourd'hui est le produit des deux zéro-coupons de six mois, $B(t,t+1)=e^{-0{,}02}\,e^{-0{,}03}\approx0{,}9512$ : c'est le compte capitalisé. Seul le premier facteur est connu aujourd'hui ; le second ne le sera que dans six mois. [ajout]

11. fpp/replication-dynamique
    Le montage de l'investisseur ne peut plus être posé une fois pour toutes : combien de futures doit-il détenir à chaque règlement ? [§4.2.2]
    Histoire : « à un taux qu'on ignore aujourd'hui » — Chaque règlement reçu est replacé et grossit comme le compte capitalisé ; pour que la stratégie suive, le nombre de futures détenus doit grossir au même rythme. Au premier semestre, il en détient l'inverse du premier facteur, $1/e^{-0{,}02}\approx1{,}0202$ ; au second, l'inverse du compte capitalisé sur l'année, $1/0{,}9512\approx1{,}0513$. Chacun de ces nombres est connu au moment où il faut l'appliquer, puisque seul le taux du semestre qui commence y entre. La fiche l'écrit $1/B(t_0,t_{i+1})$ au règlement $t_i$, $t_0$ étant aujourd'hui. [ajout]

12. fpp/prix-future
    Le prix du future s'en déduit. Est-il le même que le prix convenu dans un contrat à terme ordinaire ? [§4.2]
    Histoire : « disons 6 % » — Pas forcément. Si les taux étaient connus d'avance, 4 % toute l'année, le compte capitalisé serait le zéro-coupon, 0,9608, et le future sur l'action vaudrait exactement le prix à terme, 102,00. Il ne peut s'en écarter que parce que les taux à venir, comme ce 6 % qu'on ignore aujourd'hui, sont aléatoires. [ajout]

## Point d'arrivée
Le prix d'un échange futur ne dépend d'aucune prévision : il est fixé par ce que coûte aujourd'hui sa réplication, statique pour un contrat à terme ordinaire, qu'on appelle un forward, dynamique pour un future. [ajout]

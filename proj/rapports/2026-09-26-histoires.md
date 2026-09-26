# Rapport — histoires des parcours (dss, dup, fpp, pfo) — 2026-09-26

## Matériau traité

Aucun matériau nouveau. Après l'histoire du taux forward (rapport `2026-09-26-fpp-7`),
l'utilisateur a demandé de vérifier toutes les autres lignes « Histoire : » de la même
façon. Quatre critères, lus dans l'ordre du récit comme un étudiant qui le découvre :
calcul parachuté (un nombre dont on ne sait pas d'où il vient), lien rompu avec l'histoire
cumulée, terme ou symbole employé avant d'être défini, faute de calcul. Un agent par cours ;
chaque calcul refait en Python, relu ensuite par l'opérateur (échantillon : delta
$N(0{,}3)\approx0{,}618$, $e^{-0{,}1}=0{,}9048$, sens du terme de kurtosis de Cornish-Fisher
à 5 %, $u(x)=x^{0{,}6}$ vérifiée sur L4 slide 29).

Lignes lues : 56 (fpp), 76 (dss), 84 (dup), 45 (pfo). Réécrites : 21, 28, 18, 16. Seules des
lignes « Histoire : » ont changé ; citations, indentation et marqueurs conservés.

Fautes corrigées au passage : fpp bilan 4 (le rendement de l'actionnaire n'est pas celui de
l'actif fois le levier, seuls ses écarts le sont) ; fpp options 8 (9,93 − 3,92 = 6,01) ;
pfo risque 7 (au seuil de 5 %, les queues épaisses ramènent le quantile, seule l'asymétrie
le pousse vers les pertes) ; pfo risque 2 (0,0324 × 1 000 000 = 32 400) ; dss retrecir 12
(« même contraints » citait un modèle sans contrainte).

## Inventaire ajouté (à auditer par l'utilisateur)

Aucun élément.

## Notations ajoutées ou en collision

Aucune.

## Fiches créées

Aucune.

## Fiches modifiées

Aucune.

## Abstractions créées / insérées

Aucune.

## Abstractions en attente

pfo : portefeuille de variance minimale globale ; estimateur de volatilité ; mesure de
risque. dss : fonction d'activation ; indicateur de matrice de confusion. dup : dominance
stochastique ; mesure de risque.

## Parcours

**`fpp/parcours-bilan`**, étape 3 (`fpp/levier`), ligne « Histoire : »
- ancien : Histoire : « Que gagne l'actionnaire, et que risque-t-il » — Tout ce que font les 100 d'actifs retombe sur les 30 de l'actionnaire, puisque la dette, elle, est due quoi qu'il arrive. Le levier vaut $100/30\approx3{,}33$ : c'est lui qui transforme les gains et les risques de l'actif en ceux de l'actionnaire. [ajout]
- nouveau : Histoire : « Que gagne l'actionnaire, et que risque-t-il » — Tout ce que font les 100 d'actifs retombe sur les 30 de l'actionnaire, puisque la dette, elle, est due quoi qu'il arrive. Le levier, rapport de l'actif aux capitaux propres, vaut $100/30\approx3{,}33$ : c'est lui qui transforme les gains et les risques de l'actif en ceux de l'actionnaire. [ajout]
- raison : Terme non défini : le levier, nom de la notion de l'étape, était chiffré par 100/30 sans que le récit dise de quel rapport il s'agit.

**`fpp/parcours-bilan`**, étape 4 (`fpp/volatilite`), ligne « Histoire : »
- ancien : Histoire : « De combien varie celui de l'actionnaire » — Son rendement est celui de l'actif multiplié par le levier : sa volatilité vaut $3{,}33\times6\,\%=20\,\%$, plus de trois fois celle de l'actif. [ajout]
- nouveau : Histoire : « De combien varie celui de l'actionnaire » — Le coût de la dette, lui, ne bouge pas : chaque écart du rendement de l'actif arrive donc à l'actionnaire multiplié par le levier. Sa volatilité, l'écart type de son rendement, vaut $3{,}33\times6\,\%=20\,\%$, plus de trois fois celle de l'actif. [ajout]
- raison : Faux et terme non défini : le rendement de l'actionnaire n'est pas celui de l'actif multiplié par le levier (seuls ses écarts le sont, la dette coûtant un taux fixe, cf. l'identité de la fiche levier), et « volatilité » était employé sans être expliqué.

**`fpp/parcours-flux`**, étape 3 (`fpp/convention-capitalisation`), ligne « Histoire : »
- ancien : Histoire : « un taux peut s'entendre de plusieurs façons » — En capitalisation linéaire, 4 % sur un an font d'un euro 1,04 ; en capitalisation continue, $e^{0{,}04}\approx1{,}0408$. Pour ramener les 104, il faut savoir laquelle le marché emploie. [ajout]
- nouveau : Histoire : « un taux peut s'entendre de plusieurs façons » — En capitalisation linéaire, où l'intérêt est versé une seule fois en fin de période, 4 % sur un an font d'un euro 1,04 ; en capitalisation continue, où l'intérêt est réinvesti à chaque instant, ils en font $e^{0{,}04}\approx1{,}0408$. Pour ramener les 104, il faut savoir laquelle le marché emploie. [ajout]
- raison : Termes non définis et calcul parachuté : « capitalisation linéaire / continue » n'étaient pas expliquées, et l'exponentielle tombait sans raison.

**`fpp/parcours-flux`**, étape 4 (`fpp/facteur-actualisation`), ligne « Histoire : »
- ancien : Histoire : « 104 dans un an » — Au taux continu de 4 %, un euro payé dans un an vaut aujourd'hui $P(t,t+1)=e^{-0{,}04}\approx0{,}9608$. Les 104 valent donc $104\times0{,}9608\approx99{,}92$ aujourd'hui, un peu moins que 100. [ajout]
- nouveau : Histoire : « 104 dans un an » — Un euro payé dans un an vaut aujourd'hui ce qu'il faut placer pour l'obtenir : au taux continu de 4 %, l'inverse de $e^{0{,}04}$, soit $P(t,t+1)=e^{-0{,}04}\approx0{,}9608$. C'est le facteur d'actualisation. Les 104 valent donc $104\times0{,}9608\approx99{,}92$ aujourd'hui, un peu moins que 100. [ajout]
- raison : Calcul parachuté et notion non nommée : le passage de e^{0,04} (étape précédente) à e^{-0,04} n'était pas raisonné, et le nom de la notion n'apparaissait pas.

**`fpp/parcours-flux`**, étape 6 (`fpp/duration`), ligne « Histoire : »
- ancien : Histoire : « 100 dans deux ans » — Si le taux à deux ans monte d'un point, ce flux perd environ 2 % de sa valeur : sa sensibilité au taux est sa maturité, deux ans. Celui d'un an ne perd qu'environ 1 %. [ajout]
- nouveau : Histoire : « 100 dans deux ans » — Ce flux est actualisé sur deux années, au même taux chaque année ; si ce taux monte d'un point, l'actualisation prend deux points de plus et le flux perd environ 2 % de sa valeur. Sa sensibilité au taux est donc sa maturité, deux ans ; celui d'un an ne perd qu'environ 1 %. [ajout]
- raison : Terme non défini et calcul parachuté : « le taux à deux ans » n'est défini qu'à l'étape suivante (taux zéro-coupon), et les 2 % tombaient sans raisonnement.

**`fpp/parcours-flux`**, étape 7 (`fpp/taux-zero-coupon`), ligne « Histoire : »
- ancien : Histoire : « 0,9048 un euro payé dans deux ans » — Des prix à un an et à deux ans se comparent mal. Réécrits en taux annualisés, ils deviennent $R(t,t+1)=4\,\%$ et $R(t,t+2)=-\ln(0{,}9048)/2\approx5\,\%$ : une courbe qui monte. [ajout]
- nouveau : Histoire : « 0,9048 un euro payé dans deux ans » — Un titre qui verse un seul flux, 1 à une date fixée, s'appelle un zéro-coupon, et ces prix sont les siens. Des prix à un an et à deux ans se comparent mal ; on les réécrit en taux annualisé, le taux continu qui redonne le prix : $0{,}9048=e^{-2R}$ donne $R(t,t+2)=-\ln(0{,}9048)/2\approx5\,\%$, et de même $R(t,t+1)=4\,\%$. C'est le taux zéro-coupon, et sa courbe monte. [ajout]
- raison : Terme non défini et formule parachutée : « zéro-coupon » (réemployé à l'étape 8) n'était jamais défini, et −ln(0,9048)/2 tombait sans dire d'où il vient.

**`fpp/parcours-terme`**, étape 3 (`fpp/replication-statique`), ligne « Histoire : »
- ancien : Histoire : « Une action vaut 100 aujourd'hui et le taux sans risque à un an est de 4 % » — Emprunter 100, acheter l'action et la garder un an : on détient l'action et l'on doit $100/0{,}9608\approx104{,}08$. S'engager à l'acheter à ce prix revient exactement au même. [ajout]
- nouveau : Histoire : « Une action vaut 100 aujourd'hui et le taux sans risque à un an est de 4 % » — Emprunter 100, acheter l'action et la garder un an : on détient l'action et l'on doit 100 plus les intérêts, $100/0{,}9608\approx104{,}08$, puisqu'à 4 % continu un euro dû dans un an vaut 0,9608 aujourd'hui. S'engager à l'acheter à ce prix revient exactement au même. [ajout]
- raison : Calcul parachuté : 0,9608 n'est pas dans le point de départ, qui ne donne que le taux de 4 %.

**`fpp/parcours-terme`**, étape 4 (`fpp/portage`), ligne « Histoire : »
- ancien : Histoire : « Combien d'actions faut-il acheter aujourd'hui » — Réinvesti en actions, le dividende fait grossir la position : il suffit d'en acheter environ 0,98 aujourd'hui pour en avoir une dans un an. Ce 0,98 est le portage. [ajout]
- nouveau : Histoire : « Combien d'actions faut-il acheter aujourd'hui » — Réinvesti en actions, le dividende fait grossir la position d'environ 2 % : il suffit d'en acheter environ 2 % de moins, $1-0{,}02=0{,}98$, pour en avoir une dans un an. Ce 0,98 est le portage. [ajout]
- raison : Calcul parachuté : le 0,98 était donné sans dire comment il se déduit du dividende de 2 %.

**`fpp/parcours-terme`**, étape 8 (`fpp/forward-de-change`), ligne « Histoire : »
- ancien : Histoire : « À quel taux de change peut-il s'engager » — Le même raisonnement, avec une devise à la place de l'action : $K(t,t+1)=1{,}10\times0{,}9608/0{,}9802\approx1{,}0782$ dollar par euro. [ajout]
- nouveau : Histoire : « À quel taux de change peut-il s'engager » — Le même raisonnement, avec une devise à la place de l'action. Pour livrer un euro dans un an, il suffit d'acheter aujourd'hui le zéro-coupon en euros, 0,9608 euro, soit $1{,}10\times0{,}9608$ dollars ; empruntés en dollars, ils se remboursent dans un an divisés par 0,9802. Le taux qui ne fait ni gagner ni perdre est donc $K(t,t+1)=1{,}10\times0{,}9608/0{,}9802\approx1{,}0782$ dollar par euro. [ajout]
- raison : Calcul parachuté : la formule 1,10×0,9608/0,9802 tombait avec « le même raisonnement » sans que la réplication en devise soit dite.

**`fpp/parcours-terme`**, étape 9 (`fpp/fra`), ligne « Histoire : »
- ancien : Histoire : « Quel taux peut-elle fixer dès aujourd'hui » — Le FRA s'écrit comme un prix à terme sur un taux : $0{,}9608=0{,}9048\,e^{K}$ donne $K\approx6\,\%$, le taux forward entre un et deux ans. [ajout]
- nouveau : Histoire : « Quel taux peut-elle fixer dès aujourd'hui » — Le FRA, *forward rate agreement*, est le contrat qui le fixe : il engage à recevoir 1 dans un an et à rendre $e^{K}$ dans deux ans. Comme il ne coûte rien à la signature, ses deux flux valent autant aujourd'hui, $0{,}9608=0{,}9048\,e^{K}$, d'où $K=\ln(0{,}9608/0{,}9048)\approx6\,\%$, le taux forward entre un et deux ans. [ajout]
- raison : Terme non défini et formule parachutée : le sigle FRA n'était pas expliqué et l'égalité 0,9608=0,9048 e^K tombait sans dire quels flux elle égale.

**`fpp/parcours-terme`**, étape 10 (`fpp/compte-capitalise`), ligne « Histoire : »
- ancien : Histoire : « qu'on ne connaît pas à l'avance » — On le place au jour le jour, en enchaînant les zéro-coupons courts : un euro devient $1/B(t,T)$ à l'échéance, avec $B(t,T)=\prod_kP(t_k,t_{k+1})$. Avec 4 % la première année puis 6 % la seconde, $B(t,t+2)=e^{-0{,}04}e^{-0{,}06}\approx0{,}9048$, et l'euro devient environ 1,105. [ajout]
- nouveau : Histoire : « qu'on ne connaît pas à l'avance » — On le place au jour le jour, en enchaînant les zéro-coupons courts, dont seul le premier est connu aujourd'hui : c'est le compte capitalisé. Un euro y devient $1/B(t,T)$ à l'échéance, avec $B(t,T)=\prod_kP(t_k,t_{k+1})$, le produit des prix de ces zéro-coupons. Si le taux vaut 4 % la première année puis 6 % la seconde, $B(t,t+2)=e^{-0{,}04}e^{-0{,}06}\approx0{,}9048$, et l'euro devient environ 1,105. [ajout]
- raison : Notion non nommée et donnée parachutée : le compte capitalisé n'était pas nommé, B restait un produit sans lecture, et « 4 % puis 6 % » était posé comme un fait alors que les taux sont inconnus à l'avance.

**`fpp/parcours-terme`**, étape 11 (`fpp/replication-dynamique`), ligne « Histoire : »
- ancien : Histoire : « chaque règlement se place au taux du jour » — Chaque règlement réinvesti grossit la position ; pour qu'elle vaille à la fin exactement un contrat, il faut en détenir $1/B$, et réajuster à chaque pas. Avec trois pas à 0,99, on détient successivement 1,0101, 1,0203 puis 1,0306 contrats. [ajout]
- nouveau : Histoire : « chaque règlement se place au taux du jour » — Chaque règlement réinvesti grossit comme un euro placé au compte capitalisé ; pour que la valeur finale reste celle visée, la position suit ce rythme : on détient $1/B$ contrats, réajustés à chaque pas. Avec les taux de l'étape précédente, un contrat au départ, puis $1/0{,}9608\approx1{,}0408$ après un an. [ajout]
- raison : Mal relié à l'histoire : l'exemple « trois pas à 0,99 » introduisait des données étrangères au récit ; il reprend les taux de l'étape précédente. « vaille à la fin exactement un contrat » est remplacé par la formulation de la fiche (« la valeur finale reste celle visée »).

**`fpp/parcours-terme`**, étape 12 (`fpp/prix-future`), ligne « Histoire : »
- ancien : Histoire : « Revenons à l'action, mais sur un marché de futures » — Tant que les taux sont connus d'avance, le prix du future sur l'action est celui du forward, 104,08. Il ne s'en écarte que lorsque les taux futurs sont eux-mêmes aléatoires. [ajout]
- nouveau : Histoire : « Revenons à l'action, mais sur un marché de futures » — Tant que les taux sont connus d'avance, le prix du future sur l'action est celui du forward : 102,00 avec le dividende de 2 %, 104,08 sans. Il ne s'en écarte que lorsque les taux futurs sont eux-mêmes aléatoires. [ajout]
- raison : Mal relié à l'histoire cumulée : l'action du récit verse un dividende depuis l'étape 4 et son forward vaut 102,00 (étape 7) ; la ligne donnait 104,08 sans le dire.

**`fpp/parcours-risque-neutre`**, étape 2 (`fpp/mesure-risque-neutre`), ligne « Histoire : »
- ancien : Histoire : « son prix à terme à un an vaut 104,08 » — Tout prix s'écrit comme une moyenne actualisée, $\Pi\big(g(S_T)\big)=P(t,T)\,\mathbb{E}^{\mathbb{Q}}\big[g(S_T)\big]$, sous des poids $\mathbb{Q}$ que le marché à terme contraint : sous eux, l'action vaut en moyenne 104,08 dans un an, quoi que chacun croie de sa dérive. [ajout]
- nouveau : Histoire : « son prix à terme à un an vaut 104,08 » — Tout prix s'écrit comme une moyenne actualisée, $\Pi\big(g(S_T)\big)=P(t,T)\,\mathbb{E}^{\mathbb{Q}}\big[g(S_T)\big]$ : le prix d'un flux $g(S_T)$ versé en $T$ est sa moyenne sous une probabilité $\mathbb{Q}$, dite risque-neutre, ramenée à aujourd'hui. Le marché à terme la contraint : sous elle, l'action vaut en moyenne 104,08 dans un an, quoi que chacun croie de son rendement espéré. [ajout]
- raison : Termes non définis : la mesure risque-neutre, nom de la notion, n'était pas nommée (« des poids ℚ »), et « dérive » était employé sans explication.

**`fpp/parcours-risque-neutre`**, étape 3 (`fpp/contrat-derive`), ligne « Histoire : »
- ancien : Histoire : « même non linéaire » — Un flux qui dépend de l'action, linéaire comme le forward ou non comme une option, se valorise par cette même moyenne. Seule change l'inconnue : un prix $K$ pour un contrat qui ne coûte rien à la signature, une prime pour un contrat qui se paie. [ajout]
- nouveau : Histoire : « même non linéaire » — Un flux qui dépend de l'action, linéaire comme le forward ou non comme une option, droit d'acheter à un prix fixé sans y être obligé, se valorise par cette même moyenne. Seule change l'inconnue : un prix $K$ pour un contrat qui ne coûte rien à la signature, une prime pour un contrat qui se paie. [ajout]
- raison : Terme non défini : « option » était employé ici avant d'être expliqué (parcours options).

**`fpp/parcours-options`**, étape 1 (`fpp/payoff`), ligne « Histoire : »
- ancien : Histoire : « L'engagement ferme d'acheter au prix à terme » — Pour décrire un contrat, on dit ce qu'il verse selon le prix de l'action dans un an : une fonction de $S_T$. L'engagement ferme verse $S_T-104{,}08$, positif ou négatif ; le droit du départ versera $(S_T-100)^+$, jamais négatif. [ajout]
- nouveau : Histoire : « L'engagement ferme d'acheter au prix à terme » — Pour décrire un contrat, on dit ce qu'il verse selon le prix $S_T$ de l'action dans un an : cette fonction de $S_T$ est son payoff. L'engagement ferme verse $S_T-104{,}08$, positif ou négatif ; le droit du départ versera $(S_T-100)^+$, c'est-à-dire $S_T-100$ si c'est positif et 0 sinon. [ajout]
- raison : Symbole et terme non définis : la notation (·)^+ n'était pas expliquée, et le mot payoff, nom de la notion, n'apparaissait pas.

**`fpp/parcours-options`**, étape 6 (`fpp/parite-call-put`), ligne « Histoire : »
- ancien : Histoire : « L'engagement ferme » — Détenir le call et vendre le put, tous deux de strike 100, revient à s'engager ferme à acheter à 100 : $(S_T-100)^+-(100-S_T)^+=S_T-100$. Sans aucun modèle, $C_t-P_t=100-100\times0{,}9608=3{,}92$. [ajout]
- nouveau : Histoire : « L'engagement ferme » — Détenir le call et vendre le put, tous deux de strike 100, revient à s'engager ferme à acheter à 100 : $(S_T-100)^+-(100-S_T)^+=S_T-100$. Cet engagement vaut aujourd'hui l'action moins 100 euros payés dans un an ; l'écart entre le prix $C_t$ du call et le prix $P_t$ du put vaut donc, sans aucun modèle, $C_t-P_t=100-100\times0{,}9608=3{,}92$. C'est la parité call-put. [ajout]
- raison : Calcul parachuté et symboles non définis : C_t et P_t n'étaient pas présentés, et 100−100×0,9608 tombait sans dire pourquoi l'engagement vaut cela.

**`fpp/parcours-options`**, étape 8 (`fpp/valeur-temps`), ligne « Histoire : »
- ancien : Histoire : « Pourquoi plus que 3,92 » — Parce que l'action peut finir loin de 104,08 : quand elle monte, le call en profite ; quand elle baisse, il ne perd rien au-delà de zéro. Ce paiement convexe vaut plus que sa valeur en la moyenne, et l'écart, $9{,}93-3{,}92\approx6{,}00$, est la valeur temps. [ajout]
- nouveau : Histoire : « Pourquoi plus que 3,92 » — Parce que l'action peut finir loin de 104,08 : quand elle monte, le call en profite ; quand elle baisse, il ne perd rien au-delà de zéro. Ce paiement convexe vaut plus que sa valeur en la moyenne, et l'écart, $9{,}93-3{,}92$, soit environ 6, est la valeur temps. [ajout]
- raison : Faux : 9,93 − 3,92 fait 6,01, non 6,00 (l'écart exact, 9,925 − 3,920, vaut 6,005).

**`fpp/parcours-options`**, étape 10 (`fpp/modele-de-merton`), ligne « Histoire : »
- ancien : Histoire : « Que vaut ce que détient l'actionnaire » — Dans un an, il reçoit la valeur de l'entreprise moins la dette si elle est positive, rien sinon : c'est un call sur l'entreprise, de strike la dette. Avec un taux nul, ce call vaut 21,2 % de la valeur forward de l'entreprise, et le risque de faillite lui coûte un spread de crédit d'environ 149 points de base. [ajout]
- nouveau : Histoire : « Que vaut ce que détient l'actionnaire » — Dans un an, il reçoit la valeur de l'entreprise moins la dette si elle est positive, rien sinon : c'est un call sur l'entreprise, de strike la dette. Avec un taux nul, la formule de Black et Scholes donne à ce call 21,2 % de la valeur forward de l'entreprise ; la dette vaut donc le reste, 78,8 %, moins que les 80 % promis. Cet écart, exprimé en taux, est son spread de crédit, le supplément de rendement qui paie le risque de faillite : environ 149 points de base. [ajout]
- raison : Calcul parachuté et terme non défini : 21,2 % et 149 points de base tombaient sans dire d'où ils viennent, et « spread de crédit » n'était pas expliqué.

**`fpp/parcours-couverture`**, étape 6 (`fpp/delta`), ligne « Histoire : »
- ancien : Histoire : « ne veut pas parier sur l'action » — Pour ne plus dépendre du cours, la banque achète $\delta=N(0{,}3)\approx0{,}618$ action par call vendu : si l'action monte d'un euro, le call vendu lui coûte environ 0,618 de plus, et les actions lui rapportent autant. [ajout]
- nouveau : Histoire : « ne veut pas parier sur l'action » — Le delta dit de combien le prix du call bouge quand l'action monte d'un euro ; la formule de Black et Scholes le donne, $\delta=N(d_1)$, où $N$ est la fonction de répartition gaussienne et $d_1=\big(\ln(100/100)+0{,}04+0{,}2^2/2\big)/0{,}2=0{,}3$, soit $\delta\approx0{,}618$. La banque achète donc 0,618 action par call vendu : si l'action monte d'un euro, le call vendu lui coûte environ 0,618 de plus, et les actions lui rapportent autant. [ajout]
- raison : Calcul parachuté et symboles non définis : N(0,3) tombait sans dire ce que sont N ni 0,3, et le delta n'était pas nommé.

**`fpp/parcours-strategies`**, étape 3 (`fpp/amelioration-de-rendement`), ligne « Histoire : »
- ancien : Histoire : « Que peut-il vendre, et que gagne-t-il » — Il vend le call à la monnaie et encaisse 9,93 tout de suite ; en échange, il abandonne toute la hausse au-delà de 100. La hausse que l'épargnant achète d'un côté, c'est ce vendeur qui la cède de l'autre. [ajout]
- nouveau : Histoire : « Que peut-il vendre, et que gagne-t-il » — Il vend le call à la monnaie, c'est-à-dire de strike égal au cours actuel, 100, et encaisse 9,93 tout de suite ; en échange, il abandonne toute la hausse au-delà de 100. La hausse que l'épargnant achète d'un côté, c'est ce vendeur qui la cède de l'autre. [ajout]
- raison : Terme non défini : « à la monnaie » était employé sans explication.

**`dss/parcours-panorama`**, étape 11 (`dss/matrice-de-confusion`), ligne « Histoire : »
- ancien : Histoire : « est-il bon » — Non : il ne détecte aucun des 10 défauts. Le tableau des réussites et des erreurs le montre : 90 vrais négatifs, 10 faux négatifs, aucun vrai positif ; l'exactitude vaut 0,90, et la sensibilité 0. [ajout]
- nouveau : Histoire : « est-il bon » — Non : il ne détecte aucun des 10 défauts. Le tableau qui croise la réalité et la prédiction le montre : aucun vrai positif, défaut annoncé et survenu ; 10 faux négatifs, défauts manqués ; 90 vrais négatifs, bons clients reconnus ; aucune fausse alarme. L'exactitude, part des réponses justes sur les 100 dossiers, vaut 90/100 = 0,90 ; la sensibilité, part des 10 défauts qui sont détectés, vaut 0/10 = 0. [ajout]
- raison : termes non définis (vrai négatif, faux négatif, vrai positif, exactitude, sensibilité) et nombres 0,90 et 0 donnés sans leur calcul.

**`dss/parcours-panorama`**, étape 12 (`dss/courbe-roc`), ligne « Histoire : »
- ancien : Histoire : « Comment juger ce modèle sans choisir de seuil » — On trace, pour tous les seuils, la part des défauts détectés contre la part des bons clients refusés : c'est la courbe ROC. L'aire sous la courbe la résume ; une aire de 0,75 donne un GINI de 0,50. [ajout]
- nouveau : Histoire : « Comment juger ce modèle sans choisir de seuil » — On trace, pour tous les seuils, la part des défauts détectés contre la part des bons clients refusés : c'est la courbe ROC. L'aire sous la courbe, l'AUC, la résume en un nombre : 0,5 pour un modèle qui tire au hasard, 1 pour un modèle qui sépare parfaitement. Le cours la réétale en $\text{GINI}=2\times\mathrm{AUC}-1$, pour que le hasard vaille 0 : une aire de 0,75, par exemple, donne un GINI de $2\times0{,}75-1=0{,}50$. [ajout]
- raison : GINI employé sans définition et « une aire de 0,75 donne un GINI de 0,50 » parachuté : la formule GINI = 2×AUC − 1 et les repères 0,5 / 1 de l'aire manquaient.

**`dss/parcours-panorama`**, étape 13 (`dss/scoring-de-credit`), ligne « Histoire : »
- ancien : Histoire : « si un demandeur fera défaut » — C'est le scoring de crédit, fil du cours jusqu'à sa fin. Sur le jeu de données du cours, la régression logistique atteint un GINI de 51,36, la forêt aléatoire 57,84. [ajout]
- nouveau : Histoire : « si un demandeur fera défaut » — C'est le scoring de crédit, fil du cours jusqu'à sa fin, jugé par le GINI qu'on vient de voir, que le cours exprime en pour cent. Sur le jeu de données du cours, deux modèles qu'il met en concurrence à la fin, la régression logistique et la forêt aléatoire, atteignent un GINI de 51,36 et de 57,84 : la seconde ordonne mieux les demandeurs selon leur risque. [ajout]
- raison : GINI de 51,36 incompréhensible juste après un GINI de 0,50 (échelle en pour cent non dite) ; régression logistique et forêt aléatoire nommées sans dire ce qu'elles sont dans l'histoire.

**`dss/parcours-selection`**, étape 1 (`dss/moindres-carres-ordinaires`), ligne « Histoire : »
- ancien : Histoire : « Une régression sur les cinq » — La régression cherche les coefficients qui rendent la plus petite possible la somme des carrés des erreurs sur les 20 clients. Sur l'endettement et le revenu, elle donne $\hat y=3{,}30+0{,}076\,x_1-0{,}060\,x_2$, pour une somme de 22,43. [ajout]
- nouveau : Histoire : « Une régression sur les cinq » — La régression cherche les coefficients qui rendent la plus petite possible la somme des carrés des erreurs sur les 20 clients, notée RSS. Sur l'endettement $x_1$ et le revenu $x_2$, elle prédit la perte par $\hat y=3{,}30+0{,}076\,x_1-0{,}060\,x_2$, pour une RSS de 22,43 : divisée par les 20 clients, c'est l'erreur moyenne de 1,12 du point de départ. [ajout]
- raison : symboles $x_1$, $x_2$, $\hat y$ non définis ; la somme 22,43 n'était pas reliée à l'erreur moyenne 1,12 du point de départ ; la RSS, que les étapes suivantes emploient, n'était pas nommée.

**`dss/parcours-selection`**, étape 3 (`dss/surapprentissage`), ligne « Histoire : »
- ancien : Histoire : « trois variables sans aucun lien avec la perte » — Le modèle à cinq prédicteurs s'en sert pour coller au bruit des 20 clients : son erreur d'apprentissage baisse, de 1,12 à 0,98, et son erreur de test monte, de 1,16 à 1,83. [ajout]
- nouveau : Histoire : « trois variables sans aucun lien avec la perte » — Le modèle à cinq prédicteurs s'en sert pour coller au bruit des 20 clients : son erreur d'apprentissage, celle qu'il fait sur les clients qui ont servi à l'ajuster, baisse de 1,12 à 0,98, et son erreur de test monte, de 1,16 à 1,83. [ajout]
- raison : « erreur d'apprentissage » employée pour la première fois sans être définie.

**`dss/parcours-selection`**, étape 4 (`dss/critere-penalise`), ligne « Histoire : »
- ancien : Histoire : « quand on ne dispose pas des clients nouveaux » — On corrige l'erreur d'apprentissage par une pénalité qui grandit avec le nombre de prédicteurs. Passer de deux à cinq prédicteurs fait baisser l'erreur d'apprentissage de 0,14 et monter la pénalité du $C_p$ de 0,42 : le petit modèle l'emporte. [ajout]
- nouveau : Histoire : « quand on ne dispose pas des clients nouveaux » — On corrige l'erreur d'apprentissage par une pénalité qui grandit avec le nombre de prédicteurs, parce que chaque prédicteur ajouté la fait baisser, même quand il n'apporte rien. Passer de deux à cinq prédicteurs la fait baisser de 1,12 à 0,98, soit de 0,14 : si les trois prédicteurs ajoutés coûtent davantage en pénalité, le petit modèle l'emporte. Les critères qui suivent fixent ce coût. [ajout]
- raison : nommait le $C_p$, notion de l'étape suivante, et donnait une pénalité de 0,42 sans aucun moyen de la calculer (σ̂² et la formule n'arrivent qu'après) ; le 0,14 est désormais tiré des erreurs du point de départ.

**`dss/parcours-selection`**, étape 5 (`dss/cp-de-mallows`), ligne « Histoire : »
- ancien : Histoire : « Lesquels garder » — Avec $\hat\sigma^2=1{,}40$ estimé sur le modèle complet, $C_p=(22{,}43+2\times2\times1{,}40)/20=1{,}40$ pour le modèle à deux prédicteurs, contre 1,68 pour le modèle complet : le $C_p$ garde l'endettement et le revenu. [ajout]
- nouveau : Histoire : « Lesquels garder » — Le $C_p$ ajoute à la RSS une pénalité $2d\hat\sigma^2$ et divise le tout par le nombre $n$ de clients ; $d$ est le nombre de prédicteurs, $\hat\sigma^2$ la variance du bruit, estimée sur le modèle complet : sa RSS vaut 19,59, soit 20 fois son erreur moyenne de 0,98, et divisée par les 20 clients moins ses six coefficients elle donne $\hat\sigma^2\approx1{,}40$. Pour le modèle à deux prédicteurs, $C_p=(22{,}43+2\times2\times1{,}40)/20=1{,}40$ ; pour le modèle complet, $(19{,}59+2\times5\times1{,}40)/20=1{,}68$. La pénalité a monté de 0,42, bien plus que les 0,14 d'erreur gagnés : le $C_p$ garde l'endettement et le revenu. [ajout]
- raison : calcul parachuté : σ̂² et sa valeur 1,40, la formule du $C_p$ et le 1,68 du modèle complet apparaissaient sans explication ; la ligne relie maintenant la pénalité aux 0,14 de l'étape précédente.

**`dss/parcours-selection`**, étape 6 (`dss/aic`), ligne « Histoire : »
- ancien : Histoire : « avec une erreur moyenne de 0,98 contre 1,12 » — L'AIC part de cette erreur d'apprentissage et ajoute deux points par prédicteur : $20\log(22{,}43/20)+2\times2\approx6{,}29$ pour le modèle à deux prédicteurs, 9,59 pour le modèle complet. Même choix. [ajout]
- nouveau : Histoire : « avec une erreur moyenne de 0,98 contre 1,12 » — L'AIC vaut $-2\log L+2d$, où $L$ est la vraisemblance, la probabilité que le modèle ajusté donne aux données observées. Pour une régression à erreurs gaussiennes, $-2\log L$ vaut, à une constante près, $n\log(\mathrm{RSS}/n)$, $n$ fois le logarithme de cette erreur moyenne ; on y ajoute deux points par prédicteur : $20\log(22{,}43/20)+2\times2\approx6{,}29$ pour le modèle à deux prédicteurs, $20\log(19{,}59/20)+2\times5\approx9{,}59$ pour le modèle complet. Même choix. [ajout]
- raison : formule $20\log(22{,}43/20)$ parachutée (ni la forme $-2\log L+2d$ ni le passage à la RSS n'étaient dits) et 9,59 donné sans son calcul.

**`dss/parcours-selection`**, étape 7 (`dss/bic`), ligne « Histoire : »
- ancien : Histoire : « Les 20 clients de la banque » — Avec 20 clients, $\log20\approx3{,}0$ : la pénalité par prédicteur du BIC vaut une fois et demie celle du $C_p$. Il donne 1,54 contre 2,03, et garde lui aussi les deux bons prédicteurs. [ajout]
- nouveau : Histoire : « Les 20 clients de la banque » — Le BIC reprend le $C_p$ en remplaçant le facteur 2 de la pénalité par $\log n$. Avec 20 clients, $\log20\approx3{,}0$ : la pénalité par prédicteur vaut une fois et demie celle du $C_p$. Il donne $(22{,}43+3{,}0\times2\times1{,}40)/20\approx1{,}54$ contre $(19{,}59+3{,}0\times5\times1{,}40)/20\approx2{,}03$, et garde lui aussi les deux bons prédicteurs. [ajout]
- raison : 1,54 et 2,03 parachutés : la forme du BIC n'était pas donnée, on ne voyait pas d'où venait $\log 20$.

**`dss/parcours-selection`**, étape 8 (`dss/r2-ajuste`), ligne « Histoire : »
- ancien : Histoire : « ajuste mieux les 20 clients » — Le $R^2$ monte de 0,49 à 0,55 quand on passe à cinq prédicteurs, parce qu'il ne regarde que l'ajustement. Le $R^2$ ajusté, corrigé du nombre de prédicteurs, descend de 0,43 à 0,40. [ajout]
- nouveau : Histoire : « ajuste mieux les 20 clients » — Le $R^2$ vaut $1-\mathrm{RSS}/\mathrm{TSS}$, où TSS est l'erreur qu'on ferait en prédisant toujours la perte moyenne : c'est la part de la dispersion de la perte que le modèle explique. Il monte de 0,49 à 0,55 quand on passe à cinq prédicteurs, parce qu'il ne regarde que l'ajustement. Le $R^2$ ajusté divise la RSS par $n-d-1$ et la TSS par $n-1$, ce qui fait payer chaque prédicteur : il descend de 0,43 à 0,40. [ajout]
- raison : $R^2$ et $R^2$ ajusté employés sans définition ; la correction « du nombre de prédicteurs » n'était pas dite.

**`dss/parcours-selection`**, étape 12 (`dss/meilleur-sous-ensemble`), ligne « Histoire : »
- ancien : Histoire : « Lesquels garder » — Avec cinq prédicteurs, il y a 32 sous-ensembles à ajuster. Le meilleur à un prédicteur est, par hasard, une variable sans lien avec la perte ; le meilleur à deux est le bon, l'endettement et le revenu. [ajout]
- nouveau : Histoire : « Lesquels garder » — Avec cinq prédicteurs, chacun gardé ou écarté, il y a $2^5=32$ sous-ensembles à ajuster. Le meilleur à un prédicteur est, par hasard, une variable sans lien avec la perte ; le meilleur à deux est le bon, l'endettement et le revenu. [ajout]
- raison : 32 donné sans son calcul.

**`dss/parcours-selection`**, étape 13 (`dss/selection-pas-a-pas`), ligne « Histoire : »
- ancien : Histoire : « Peut-on n'en visiter qu'une petite fraction » — Oui : on ajoute ou l'on retire un prédicteur à la fois, en gardant à chaque pas le meilleur mouvement. Avec les cinq prédicteurs des 20 clients, chaque sens n'ajuste que 16 modèles au lieu de 32. [ajout]
- nouveau : Histoire : « Peut-on n'en visiter qu'une petite fraction » — Oui : on ajoute ou l'on retire un prédicteur à la fois, en gardant à chaque pas le meilleur mouvement. Avec les cinq prédicteurs des 20 clients, chaque sens ajuste le modèle de départ puis, à chaque pas, un modèle par prédicteur encore candidat : $1+5+4+3+2+1=16$ modèles au lieu de 32. [ajout]
- raison : 16 parachuté : le décompte n'était pas expliqué.

**`dss/parcours-retrecir`**, étape 1 (`dss/compromis-biais-variance`), ligne « Histoire : »
- ancien : Histoire : « limiter autrement ce que le modèle apprend » — Les moindres carrés sur les cinq prédicteurs sont sans biais, mais leurs coefficients bougent beaucoup d'un échantillon de 20 clients à l'autre. Les contraindre les écarte un peu des vrais coefficients et les rend plus stables : on y gagne quand la somme des deux erreurs baisse. [ajout]
- nouveau : Histoire : « limiter autrement ce que le modèle apprend » — Les moindres carrés sur les cinq prédicteurs sont sans biais, justes en moyenne sur tous les échantillons possibles, mais leurs coefficients bougent beaucoup d'un échantillon de 20 clients à l'autre : leur variance est forte. Les contraindre les écarte un peu des vrais coefficients, un biais, et les rend plus stables : on y gagne quand l'erreur de test, qui additionne le carré du biais, la variance et un bruit irréductible, baisse. [ajout]
- raison : biais et variance, les deux termes de la notion de l'étape, employés sans définition ; « la somme des deux erreurs » ne disait pas lesquelles.

**`dss/parcours-retrecir`**, étape 6 (`dss/reduction-de-dimension`), ligne « Histoire : »
- ancien : Histoire : « si la banque décrivait ses 20 clients par 30 prédicteurs » — Seconde voie : résumer ces 30 prédicteurs en quelques combinaisons, par exemple trois, et régresser la perte sur elles. Il n'y a plus que 4 coefficients à estimer au lieu de 31, ce que 20 clients permettent. [ajout]
- nouveau : Histoire : « si la banque décrivait ses 20 clients par 30 prédicteurs » — Seconde voie : résumer ces 30 prédicteurs en quelques combinaisons, par exemple trois, et régresser la perte sur elles. Il n'y a plus que 4 coefficients à estimer, constante comprise, au lieu de 31, ce que 20 clients permettent. [ajout]
- raison : 4 et 31 sans leur origine : la constante n'était pas dite.

**`dss/parcours-retrecir`**, étape 7 (`dss/decomposition-en-valeurs-singulieres`), ligne « Histoire : »
- ancien : Histoire : « les moindres carrés n'auraient même plus de solution unique » — Avec plus de prédicteurs que de clients, la matrice des prédicteurs a des directions sans aucune dispersion. Sa décomposition en valeurs singulières les met à nu : ridge rétrécit chaque direction d'un facteur $d_j^2/(d_j^2+\lambda)$, presque rien sur celles qui sont très dispersées, presque tout sur celles qui ne le sont pas. [ajout]
- nouveau : Histoire : « les moindres carrés n'auraient même plus de solution unique » — Avec plus de prédicteurs que de clients, la matrice des prédicteurs a des directions sans aucune dispersion, le long desquelles les données ne fixent aucun coefficient : d'où les solutions multiples. Sa décomposition en valeurs singulières les met à nu : elle donne à chaque direction $j$ un étirement $d_j$, qui mesure la dispersion des clients le long d'elle et vaut zéro sur ces directions-là. Ridge rétrécit chaque direction d'un facteur $d_j^2/(d_j^2+\lambda)$ : presque pas quand $d_j^2$ est grand devant $\lambda$, entièrement quand $d_j$ est nul. [ajout]
- raison : symbole $d_j$ non défini et facteur $d_j^2/(d_j^2+\lambda)$ parachuté ; le lien avec la citation (pourquoi plus de solution unique) n'était pas dit.

**`dss/parcours-retrecir`**, étape 12 (`dss/malediction-de-la-dimension`), ligne « Histoire : »
- ancien : Histoire : « Et si la banque décrivait ses 20 clients » — Même contraints, des prédicteurs sans lien avec la perte coûtent : sur les 20 clients, passer de deux à cinq prédicteurs faisait déjà monter l'erreur de test de 1,16 à 1,83. Une variable de plus ne paie que si elle est vraiment liée à la réponse. [ajout]
- nouveau : Histoire : « Et si la banque décrivait ses 20 clients » — Même contraints, des prédicteurs sans lien avec la perte coûtent : sur les 20 clients, passer de deux à cinq prédicteurs faisait monter l'erreur de test des moindres carrés de 1,16 à 1,83, et ni ridge ni le lasso, quelle que soit la force de leur contrainte, ne ramènent le modèle à cinq prédicteurs sous 1,8. Une variable de plus ne paie que si elle est vraiment liée à la réponse. [ajout]
- raison : mal relié : « même contraints » était illustré par un modèle sans contrainte ; vérifié sur les données (ridge et lasso sur cinq prédicteurs restent à 1,82 ou plus, pour tout λ).

**`dss/parcours-arbres`**, étape 2 (`dss/bootstrap`), ligne « Histoire : »
- ancien : Histoire : « Tirer 20 clients avec remise parmi les 20 de la banque » — Faute d'autres clients, on fabrique de nouveaux échantillons en tirant avec remise : certains clients reviennent deux fois, d'autres manquent. En moyenne, $20\times0{,}95^{20}\approx7{,}2$ clients restent de côté. [ajout]
- nouveau : Histoire : « Tirer 20 clients avec remise parmi les 20 de la banque » — Faute d'autres clients, on fabrique de nouveaux échantillons en tirant avec remise : certains clients reviennent deux fois, d'autres manquent. À chacun des 20 tirages, un client donné a 19 chances sur 20, soit 0,95, de ne pas sortir ; il manque donc à tout l'échantillon avec la probabilité $0{,}95^{20}\approx0{,}36$, et en moyenne $20\times0{,}36\approx7{,}2$ clients restent de côté. [ajout]
- raison : $20\times0{,}95^{20}$ parachuté : l'origine du 0,95 n'était pas dite.

**`dss/parcours-arbres`**, étape 3 (`dss/bagging`), ligne « Histoire : »
- ancien : Histoire : « chaque tirage donne un autre arbre » — On construit un arbre par tirage, et la perte prédite pour un nouveau client est la moyenne des pertes que prédisent tous les arbres, par exemple 500. [ajout]
- nouveau : Histoire : « chaque tirage donne un autre arbre » — On répète le tirage, disons 500 fois, et l'on construit un arbre par tirage ; la perte prédite pour un nouveau client est la moyenne des pertes que prédisent ces 500 arbres. C'est le bagging, de l'anglais bootstrap aggregating : agréger des arbres bâtis sur des tirages avec remise. [ajout]
- raison : « par exemple 500 » se lisait comme une perte prédite alors que c'est le nombre d'arbres (repris ensuite comme tel) ; le nom de la notion n'était pas expliqué.

**`dss/parcours-arbres`**, étape 4 (`dss/erreur-out-of-bag`), ligne « Histoire : »
- ancien : Histoire : « à quoi servent les clients laissés de côté » — Chaque client est absent d'environ 36 % des tirages : on le prédit avec les seuls arbres qui ne l'ont pas vu, environ 180 sur 500, et l'on moyenne ces erreurs sur les 20 clients. On obtient une erreur de test sans avoir mis un seul client de côté. [ajout]
- nouveau : Histoire : « à quoi servent les clients laissés de côté » — Un client absent d'un tirage est dit « hors du sac », out of bag, pour l'arbre correspondant ; il l'est pour environ 36 % des tirages, la probabilité $0{,}95^{20}$ calculée plus haut. On le prédit avec ces seuls arbres qui ne l'ont pas vu, environ 180 sur 500, et l'on moyenne ces erreurs sur les 20 clients. On obtient une erreur de test sans avoir mis un seul client de côté. [ajout]
- raison : 36 % sans lien au calcul de l'étape du bootstrap ; « hors du sac », nom de la notion, employé ensuite (étape de la permutation) sans jamais être défini.

**`dss/parcours-arbres`**, étape 6 (`dss/importance-par-impurete`), ligne « Histoire : »
- ancien : Histoire : « Quelles variables comptent » — Première mesure : additionner, pour chaque prédicteur, la baisse de la somme des carrés des erreurs obtenue à chaque coupure faite sur lui, et moyenner sur les 500 arbres. [ajout]
- nouveau : Histoire : « Quelles variables comptent » — Chaque arbre coupe les clients en deux groupes selon un seuil sur un prédicteur, et chaque coupure rend les groupes plus homogènes : elle fait baisser leur impureté, ici la somme des carrés des erreurs. Première mesure : additionner, pour chaque prédicteur, la baisse obtenue à chaque coupure faite sur lui, et moyenner sur les 500 arbres. [ajout]
- raison : « coupure » et « impureté », nom de la notion, jamais définis dans le récit.

**`dss/parcours-arbres`**, étape 8 (`dss/variance-d-une-moyenne-correlee`), ligne « Histoire : »
- ancien : Histoire : « Moyenner des arbres qui se ressemblent réduit-il la variance » — Non : avec une corrélation $\rho$ entre arbres, la variance de la moyenne vaut $\rho\,\sigma^2+(1-\rho)\,\sigma^2/B$. À $\rho=0{,}5$, elle ne descend jamais sous la moitié de celle d'un arbre, même avec 500 arbres. [ajout]
- nouveau : Histoire : « Moyenner des arbres qui se ressemblent réduit-il la variance » — Non : si chaque arbre a une variance $\sigma^2$ et deux arbres une corrélation $\rho$, la moyenne de $B$ arbres a pour variance $\rho\,\sigma^2+(1-\rho)\,\sigma^2/B$. Le second terme s'efface quand $B$ grandit, pas le premier : à $\rho=0{,}5$, elle ne descend jamais sous la moitié de celle d'un arbre, même avec 500 arbres. [ajout]
- raison : symboles $\sigma^2$ et $B$ non définis ; le raisonnement qui mène à « jamais sous la moitié » n'était pas dit.

**`dss/parcours-neurones`**, étape 3 (`dss/fonction-discriminante-lineaire`), ligne « Histoire : »
- ancien : Histoire : « Une frontière droite peut-elle les séparer » — Oui : la droite $x_1+x_2=\tfrac12$ laisse $(0,0)$ d'un côté et les trois autres points de l'autre. C'est la forme d'hypothèse la plus simple pour deux classes. [ajout]
- nouveau : Histoire : « Une frontière droite peut-elle les séparer » — Oui : en notant $x_1$ et $x_2$ les deux coordonnées d'un point, la droite $x_1+x_2=\tfrac12$ laisse $(0,0)$ d'un côté et les trois autres points de l'autre. C'est la forme d'hypothèse la plus simple pour deux classes. [ajout]
- raison : symboles $x_1$, $x_2$ non définis.

**`dss/parcours-neurones`**, étape 7 (`dss/fonction-d-activation`), ligne « Histoire : »
- ancien : Histoire : « comment en assembler plusieurs » — Pour que des neurones assemblés apprennent ensemble, la sortie de chacun doit être plus qu'un seuil sec : une fonction lisse, comme la sigmoïde $1/(1+e^{-a})$, qui varie un peu quand les poids varient un peu. [ajout]
- nouveau : Histoire : « comment en assembler plusieurs » — Pour que des neurones assemblés apprennent ensemble, la fonction qui donne la sortie de chacun, sa fonction d'activation, doit être plus qu'un seuil sec : une fonction lisse de la somme pondérée $a$ de ses entrées, comme la sigmoïde $1/(1+e^{-a})$, qui varie un peu quand les poids varient un peu. [ajout]
- raison : symbole $a$ non défini ; le nom de la notion n'apparaissait pas.

**`dss/parcours-neurones`**, étape 8 (`dss/reseau-multicouche`), ligne « Histoire : »
- ancien : Histoire : « pour dépasser cette limite » — Une couche cachée de deux neurones suffit : l'un calcule le « ou », l'autre le « et », et la sortie répond 1 quand le premier dit oui et le second non. C'est exactement le « ou exclusif ». [ajout]
- nouveau : Histoire : « pour dépasser cette limite » — Une couche cachée de deux neurones, placée entre les entrées et la sortie, suffit : l'un calcule le « ou », l'autre le « et », et la sortie répond 1 quand le premier dit oui et le second non. C'est exactement le « ou exclusif ». [ajout]
- raison : « couche cachée » employée sans définition.

**`dss/parcours-neurones`**, étape 11 (`dss/retropropagation`), ligne « Histoire : »
- ancien : Histoire : « Les poids de ce réseau à couche cachée » — Pour un poids de sortie, l'erreur se lit directement : si la sortie vaut 0,6 là où il fallait 1, $d_j=0{,}6\times0{,}4\times0{,}4=0{,}096$. Pour les poids cachés, on renvoie cette erreur vers l'arrière, chaque neurone caché en recevant une part proportionnelle à son poids vers la sortie. [ajout]
- nouveau : Histoire : « Les poids de ce réseau à couche cachée » — Pour un neurone de sortie, l'erreur à renvoyer est $d_j=o_j(1-o_j)(t_j-o_j)$ : l'écart entre la cible $t_j$ et la sortie $o_j$, multiplié par $o_j(1-o_j)$, la pente de la sigmoïde en ce point. Si la sortie vaut 0,6 là où il fallait 1, $d_j=0{,}6\times0{,}4\times0{,}4=0{,}096$. Pour les poids cachés, on renvoie cette erreur vers l'arrière, chaque neurone caché en recevant une part proportionnelle à son poids vers la sortie. [ajout]
- raison : calcul parachuté : $d_j=0{,}6\times0{,}4\times0{,}4$ sans la formule ni le sens des trois facteurs, et $d_j$ non défini.

**`dss/parcours-entrainement`**, étape 2 (`dss/garantie-pac`), ligne « Histoire : »
- ancien : Histoire : « Combien de clients lui faudrait-il pour l'entraîner » — Ce réseau compte 441 poids. La règle du cours, $m>W/\varepsilon$, demande pour une tolérance de 10 % plus de $441/0{,}1=4\,410$ exemples : les 20 clients de la banque en sont très loin. [ajout]
- nouveau : Histoire : « Combien de clients lui faudrait-il pour l'entraîner » — Ce réseau compte 441 poids : chacun des 20 neurones cachés reçoit les 20 entrées plus un poids de seuil, soit 420 poids, et la sortie reçoit les 20 neurones cachés plus un seuil, soit 21. La règle du cours, $m>W/\varepsilon$, demande un nombre d'exemples $m$ supérieur au nombre de poids $W$ divisé par la tolérance d'erreur $\varepsilon$ : pour 10 %, plus de $441/0{,}1=4\,410$ exemples. Les 20 clients de la banque en sont très loin. [ajout]
- raison : 441 parachuté (décompte non dit) ; symboles $m$, $W$, $\varepsilon$ non définis.

**`dss/parcours-entrainement`**, étape 9 (`dss/codage-des-variables`), ligne « Histoire : »
- ancien : Histoire : « situation familiale » — Elle se code un parmi $N$, une entrée par valeur, pour n'imposer aucun ordre ; la tranche d'âge peut se coder en thermomètre, ou par un seul réel, qui respecte son ordre ; l'endettement, par un seul réel ramené entre 0 et 1. [ajout]
- nouveau : Histoire : « situation familiale » — Elle se code un parmi $N$ : $N$ entrées, une par valeur possible, dont seule celle de la valeur prise vaut 1, pour n'imposer aucun ordre ; la tranche d'âge peut se coder en thermomètre, une entrée par tranche, allumées jusqu'à la sienne, ou par un seul réel, deux codages qui respectent son ordre ; l'endettement, par un seul réel ramené entre 0 et 1. [ajout]
- raison : « thermomètre » non défini et $N$ non défini.

**`dss/parcours-terrain`**, étape 1 (`dss/comparaison-de-modeles`), ligne « Histoire : »
- ancien : Histoire : « l'un compare tous les modèles sur un même problème de crédit » — Sur un même jeu de crédit, la forêt aléatoire gagne 6,48 points de GINI sur la régression logistique, et le séparateur à vaste marge en perd 22,98. [ajout]
- nouveau : Histoire : « l'un compare tous les modèles sur un même problème de crédit » — C'est le jeu du scoring de crédit : la forêt aléatoire y atteint un GINI de 57,84 contre 51,36 pour la régression logistique, soit 6,48 points de mieux, et le séparateur à vaste marge, un autre classifieur, tombe à 28,38, soit 22,98 points de moins. [ajout]
- raison : écarts 6,48 et 22,98 donnés sans les GINI dont ils se déduisent, sans lien avec le scoring du premier parcours ; séparateur à vaste marge nommé sans dire ce que c'est.

**`dup/parcours-risque`**, étape 10 (`dup/approximation-arrow-pratt`), ligne « Histoire : »
- ancien : Histoire : « Pouvait-on les prévoir sans refaire le calcul » — Oui, pour un pari aussi petit : la moitié de sa variance, 100, fois l'aversion absolue donne $\tfrac12\times100\times\tfrac{1}{200}=0{,}25$ et $\tfrac12\times100\times\tfrac{1}{100}=0{,}50$, les deux primes de l'histoire. Sur le premier pari, qui va de 0 à 100, elle donnerait 12,5 au lieu de 25 : il est trop grand. [ajout]
- nouveau : Histoire : « Pouvait-on les prévoir sans refaire le calcul » — Oui, pour un pari aussi petit : gagner ou perdre 10 a pour variance $10^2=100$, et la moitié de cette variance fois l'aversion absolue à 100 donne $\tfrac12\times100\times\tfrac{1}{200}=0{,}25$ et $\tfrac12\times100\times\tfrac{1}{100}=0{,}50$, les deux primes de l'histoire. Le premier pari, lui, est trop grand : vu comme 50 plus ou moins 50, de variance 2 500, avec l'aversion $\tfrac{1}{100}$ que $\sqrt{x}$ a en 50, elle donnerait 12,5 au lieu de 25. [ajout]
- raison : calcul parachuté : la variance 100 n'était pas dite comme celle du pari de ±10, et le 12,5 du premier pari tombait sans dire la variance (2 500) ni la richesse (50) où lire l'aversion.

**`dup/parcours-risque`**, étape 15 (`dup/crra`), ligne « Histoire : »
- ancien : Histoire : « Décuplons tout » — Richesse et pari décuplés, la prime du second agent est décuplée aussi : elle reste un demi pour cent de sa richesse. C'est ce que cette forme garde constant, et $\sqrt{x}$ en fait aussi partie, avec $\gamma=\tfrac12$. [ajout]
- nouveau : Histoire : « Décuplons tout » — Richesse et pari décuplés, la prime du second agent est décuplée aussi : elle reste un demi pour cent de sa richesse. Ce qui ne bouge pas ici est l'aversion relative, l'aversion absolue multipliée par la richesse : $x\times\tfrac1x=1$ à toute richesse pour $\ln x$, et $x\times\tfrac{1}{2x}=\tfrac12$ pour $\sqrt{x}$, qui fait donc aussi partie de cette forme, avec $\gamma=\tfrac12$ pour valeur de cette constante. [ajout]
- raison : terme et symbole non définis : « l'aversion relative » (au sens $xA(x)$) et $\gamma$ n'avaient jamais été expliqués dans le récit, et « $\gamma=\tfrac12$ » pour $\sqrt{x}$ tombait sans calcul.

**`dup/parcours-risque`**, étape 16 (`dup/utilite-logarithmique`), ligne « Histoire : »
- ancien : Histoire : « d'utilité $\ln x$ » — Le second agent a cette utilité, d'aversion relative 1 contre un demi pour le premier. Ses primes se calculent à la main : avec 100 en poche, son équivalent certain est $\sqrt{100\times200}\approx141{,}4$, d'où la prime de 8,6. [ajout]
- nouveau : Histoire : « d'utilité $\ln x$ » — Le second agent a cette utilité, d'aversion relative 1 contre un demi pour le premier. Ses primes se calculent à la main : avec 100 en poche, il finit avec 100 ou 200, et son utilité espérée $\tfrac12\ln100+\tfrac12\ln200$ est le logarithme de $\sqrt{100\times200}\approx141{,}4$, son équivalent certain ; la prime vaut donc $150-141{,}4\approx8{,}6$. [ajout]
- raison : calcul parachuté : $\sqrt{100\times200}$ apparaissait sans dire que c'est l'exponentielle de l'utilité espérée, ni d'où vient 8,6 (150 − 141,4).

**`dup/parcours-comparer`**, étape 3 (`dup/diversification`), ligne « Histoire : »
- ancien : Histoire : « Ce mélange est-il moins risqué que chacun des deux » — Son écart type vaut $50/\sqrt2\approx35{,}4$, au-dessous des 50 de chaque pari, et sa moyenne reste 50 : la covariance nulle entre les deux tirages l'abaisse, ce que les écarts types pris un à un ne montraient pas. [ajout]
- nouveau : Histoire : « Ce mélange est-il moins risqué que chacun des deux » — Le mélange s'écarte de 50 de 50 une fois sur deux et pas du tout sinon : sa variance, $\tfrac12\times50^2=1250$, est la moitié de celle d'un pari, et son écart type $50/\sqrt2\approx35{,}4$, au-dessous des 50 de chaque pari, pour une moyenne qui reste 50. Les deux tirages étant indépendants, leur covariance, qui mesure combien ils s'écartent ensemble de leur moyenne, est nulle : leurs écarts se compensent en partie, ce que les écarts types pris un à un ne montraient pas. [ajout]
- raison : calcul parachuté et terme non défini : $50/\sqrt2$ sortait sans calcul de la variance, et « covariance » n'était pas expliquée.

**`dup/parcours-comparer`**, étape 4 (`dup/utilite-quadratique`), ligne « Histoire : »
- ancien : Histoire : « Deux placements ont la même moyenne de 50 » — Pour qu'un agent classe ces deux paris par leurs seuls moyenne et écart type, il faut que son utilité soit de la forme $U(x)=\alpha x+\beta x^2$. Avec $\alpha=1$ et $\beta=-0{,}005$, le premier pari vaut 25 et le second environ 34,4 : il préfère celui d'écart type le plus faible. [ajout]
- nouveau : Histoire : « Deux placements ont la même moyenne de 50 » — Pour qu'un agent classe ces deux paris par leurs seuls moyenne et écart type, il faut que son utilité soit de la forme $U(x)=\alpha x+\beta x^2$. Avec $\alpha=1$ et $\beta=-0{,}005$, l'utilité espérée du premier pari est $\tfrac12U(0)+\tfrac12U(100)=\tfrac12\times50=25$, celle du second $\tfrac12U(25)+\tfrac12U(75)\approx\tfrac12(21{,}9+46{,}9)\approx34{,}4$ : il préfère celui d'écart type le plus faible. [ajout]
- raison : calcul parachuté : les valeurs 25 et 34,4 étaient données sans dire qu'il s'agit d'utilités espérées ni comment elles se calculent.

**`dup/parcours-comparer`**, étape 12 (`dup/ordre-concave`), ligne « Histoire : »
- ancien : Histoire : « La réponse la plus courante » — Elle désignait le bon pari, mais pour une mauvaise raison. Le premier est plus risqué parce que tout agent averse au risque préfère le second — avec $\sqrt{x}$, environ 6,83 contre 5 —, et non parce que son écart type est plus grand. [ajout]
- nouveau : Histoire : « La réponse la plus courante » — Elle désignait le bon pari, mais pour une mauvaise raison. Le premier est plus risqué parce que tout agent averse au risque préfère le second — avec $\sqrt{x}$, une utilité espérée de $\tfrac12\sqrt{25}+\tfrac12\sqrt{75}\approx6{,}83$ contre $\tfrac12\sqrt{0}+\tfrac12\sqrt{100}=5$ —, et non parce que son écart type est plus grand. [ajout]
- raison : calcul parachuté : 6,83 et 5 étaient donnés sans dire ce qu'ils mesurent ni d'où ils viennent.

**`dup/parcours-comparer`**, étape 13 (`dup/condition-cdf-integree`), ligne « Histoire : »
- ancien : Histoire : « la même moyenne de 50 » — Sur les deux paris, l'écart des aires sous les fonctions de répartition monte jusqu'à 12,5 en 25, y reste jusqu'à 75, puis redescend à 0 en 100 : positif partout, nul au bout, parce que les moyennes sont égales. Le test confirme que le premier est plus risqué. [ajout]
- nouveau : Histoire : « la même moyenne de 50 » — Le test cumule, de 0 jusqu'à chaque montant, l'écart entre les chances des deux paris de ne pas dépasser ce montant, c'est-à-dire entre leurs fonctions de répartition. Jusqu'à 25, le premier a déjà une chance sur deux, celle du 0, et le second aucune : l'écart cumulé monte à $\tfrac12\times25=12{,}5$. De 25 à 75, les deux chances valent un demi et il ne bouge pas. Au-delà de 75, le second est sûr de ne pas dépasser et le premier ne l'est qu'à moitié : l'écart redescend, jusqu'à 0 en 100 parce que les moyennes sont égales. Positif partout, nul au bout : le test confirme que le premier est plus risqué. [ajout]
- raison : calcul parachuté : le 12,5 et le profil monte-plat-redescend étaient annoncés sans le raisonnement qui les produit.

**`dup/parcours-comparer`**, étape 14 (`dup/statique-comparative-risque-accru`), ligne « Histoire : »
- ancien : Histoire : « doit-il en placer moins » — Pas forcément : ce n'est pas la concavité de son utilité qui décide, mais le signe de $U_{xxa}$. S'il est négatif, il en place moins ; s'il est positif, il en place plus. [ajout]
- nouveau : Histoire : « doit-il en placer moins » — Pas forcément : ce n'est pas la concavité de son utilité qui décide, mais la forme de ce que lui rapporte un peu plus de placement, $U_a$, en fonction du résultat $x$. Si ce gain marginal est concave en $x$, $U_{xxa}<0$, il en place moins ; s'il est convexe, $U_{xxa}>0$, il en place plus. [ajout]
- raison : symbole non défini : $U_{xxa}$ apparaissait sans que le récit ait dit ce qu'il mesure.

**`dup/parcours-violations`**, étape 2 (`dup/effet-consequence-commune`), ligne « Histoire : »
- ancien : Histoire : « 1 million avec 89 % » — Les deux paires ne diffèrent que par ce que leurs options ont en commun : 89 % de chances d'avoir 1 million dans la première, 89 % de chances de n'avoir rien dans la seconde. L'indépendance dit que changer cette part commune ne change pas le choix : préférer le million sûr impose $.11\,U(1)>.10\,U(5)+.01\,U(0)$, et préférer ensuite les 5 millions impose l'inverse. [ajout]
- nouveau : Histoire : « 1 million avec 89 % » — Les deux paires ne diffèrent que par ce que leurs options ont en commun : 89 % de chances d'avoir 1 million dans la première, 89 % de chances de n'avoir rien dans la seconde. L'indépendance dit que changer cette part commune ne change pas le choix. En utilité espérée, montants en millions, retirer des deux côtés la part commune, $.89\,U(1)$ puis $.89\,U(0)$, montre que préférer le million sûr impose $.11\,U(1)>.10\,U(5)+.01\,U(0)$, et que préférer ensuite les 5 millions impose l'inverse. [ajout]
- raison : calcul parachuté : l'inégalité en .11, .10 et .01 tombait sans dire qu'elle s'obtient en retirant la part commune de chaque paire.

**`dup/parcours-valeur`**, étape 5 (`dup/aversion-a-la-deception`), ligne « Histoire : »
- ancien : Histoire : « Un agent qui souffre de tomber sous ce qu'il attendait » — Avec $u(x)=x$ et $\alpha=1$, la première paire vaut 2 400 pour le sûr et environ 2 385 pour le billet : il prend les 2 400. La seconde vaut environ 494 pour les 2 500 et 492 pour les 2 400 : il prend les 2 500. C'est exactement le motif observé. [L3 slide 11]
- nouveau : Histoire : « Un agent qui souffre de tomber sous ce qu'il attendait » — Dans ce modèle, la valeur d'un billet est une moyenne où chaque résultat qui tombe sous cette valeur même compte $1+\alpha$ fois. Avec $u(x)=x$ et $\alpha=1$, seul le rien déçoit et il compte double : le billet vaut $(0{,}33\times2500+0{,}66\times2400)/(0{,}33+0{,}66+2\times0{,}01)\approx2385$, moins que les 2 400 sûrs, et l'agent prend les 2 400. Dans la seconde paire, de même, $0{,}33\times2500/(0{,}33+2\times0{,}67)\approx494$ pour les 2 500 et $0{,}34\times2400/(0{,}34+2\times0{,}66)\approx492$ pour les 2 400 : il prend les 2 500. C'est exactement le motif observé. [L3 slide 11]
- raison : calcul parachuté et symbole non défini : $\alpha$ n'était pas expliqué et les valeurs 2 385, 494 et 492 tombaient sans la règle qui les produit.

**`dup/parcours-poids`**, étape 2 (`dup/theorie-des-perspectives`), ligne « Histoire : »
- ancien : Histoire : « Comment un modèle tient-il compte de ce point de référence » — La théorie des perspectives code chaque résultat comme un gain ou une perte par rapport à ce point, et pondère chaque probabilité par $\pi$ : le billet vaut $\pi(0{,}01)v(98)+\pi(0{,}99)v(-2)$, avec $v(0)=0$. [ajout]
- nouveau : Histoire : « Comment un modèle tient-il compte de ce point de référence » — La théorie des perspectives code chaque résultat comme un gain ou une perte par rapport à ce point, lui donne une valeur $v$, nulle au point de référence, et pondère chaque probabilité par $\pi$ : le billet vaut $\pi(0{,}01)v(98)+\pi(0{,}99)v(-2)$. [ajout]
- raison : symbole non défini : $v$ apparaissait dans la formule sans avoir été introduit.

**`dup/parcours-poids`**, étape 4 (`dup/cpt`), ligne « Histoire : »
- ancien : Histoire : « il gagne 98 une fois sur cent, et perd 2 le reste du temps » — Refaite par le rang, la théorie des perspectives pondère séparément le côté des gains et celui des pertes. Avec la déformation du cours et $\beta=0{,}7$, la chance de gagner 98 compte pour environ 3,8 % au lieu de 1 % : c'est ce qui fait payer le billet plus que son espérance. [ajout]
- nouveau : Histoire : « il gagne 98 une fois sur cent, et perd 2 le reste du temps » — Refaite par le rang, la théorie des perspectives pondère séparément le côté des gains et celui des pertes, en déformant les probabilités cumulées par la fonction du cours, $\varphi(p)=p^\beta/\big(p^\beta+(1-p)^\beta\big)^{1/\beta}$, où $\beta$ règle l'écart à la diagonale. Avec $\beta=0{,}7$, la chance de gagner 98 compte pour $\varphi(0{,}01)\approx3{,}8\,\%$ au lieu de 1 % : c'est ce qui fait payer le billet plus que son espérance. [ajout]
- raison : calcul parachuté et symbole non défini : « la déformation du cours » et $\beta$ n'étaient pas donnés, si bien que 3,8 % ne se retrouvait pas.

**`dup/parcours-poids`**, étape 7 (`dup/aversion-second-ordre`), ligne « Histoire : »
- ancien : Histoire : « que devient la prime quand le pari rapetisse » — Elle s'évanouit comme le carré de sa taille : avec $\rho=0{,}01$, elle vaut environ $\tfrac{0{,}01}{2}\times10^2=0{,}5$ pour un pari de ±10, et $0{,}005$ pour un pari de ±1. [ajout]
- nouveau : Histoire : « que devient la prime quand le pari rapetisse » — Elle s'évanouit comme le carré de sa taille. Pour un agent dont l'aversion absolue à 100 vaut $\rho=0{,}01$, comme l'agent d'utilité $\ln x$, elle vaut environ la moitié de $\rho$ fois la variance : $\tfrac{0{,}01}{2}\times10^2=0{,}5$ pour un pari de ±10, et $\tfrac{0{,}01}{2}\times1^2=0{,}005$ pour un pari de ±1 ; dix fois plus petit, le pari coûte cent fois moins. [ajout]
- raison : symbole non défini : $\rho$ n'était ni défini ni rattaché à un agent de l'histoire.

**`dup/parcours-poids`**, étape 9 (`dup/aversion-premier-ordre`), ligne « Histoire : »
- ancien : Histoire : « gagner ou perdre 10 à pile ou face » — Pour refuser ce pari sans l'absurde de Rabin, il faut une prime proportionnelle à sa taille, et non à son carré : avec $\lambda=2$ et $\gamma=0$, elle vaut un tiers de la taille, 3,33, contre 0,5 sous l'utilité espérée, et elle reste un tiers quand le pari rapetisse. [ajout]
- nouveau : Histoire : « gagner ou perdre 10 à pile ou face » — Pour refuser ce pari sans l'absurde de Rabin, il faut une prime proportionnelle à sa taille, et non à son carré. C'est le cas si une perte pèse $\lambda=2$ fois un gain de même taille, sans autre courbure, $\gamma=0$ : pour que l'agent accepte le pari, il faut y ajouter une somme $r$ telle que $\tfrac12(10+r)=\tfrac12\times2\times(10-r)$, soit $r=10/3\approx3{,}33$, un tiers de la taille, contre 0,5 sous l'utilité espérée ; et elle reste un tiers quand le pari rapetisse. [ajout]
- raison : calcul parachuté et symboles non définis : $\lambda$ et $\gamma$ n'étaient pas expliqués ($\lambda$ ne l'est qu'à l'étape suivante), et 3,33 tombait sans calcul.

**`dup/parcours-poids`**, étape 10 (`dup/aversion-aux-pertes`), ligne « Histoire : »
- ancien : Histoire : « perd 2 le reste du temps » — La prime qui ne s'évanouit pas vient d'un coude au point de référence : une perte pèse $\lambda$ fois un gain de même taille. Avec $\lambda=2$ et $\beta=1$, perdre 10 vaut $-20$ et gagner 10 vaut $+10$ : le pari de ±10 vaut $-5$ et il est refusé. [ajout]
- nouveau : Histoire : « perd 2 le reste du temps » — La prime qui ne s'évanouit pas vient d'un coude au point de référence : une perte pèse $\lambda$ fois un gain de même taille. Avec $\lambda=2$ et $\beta=1$, ici l'exposant de la fonction de valeur et non celui de la déformation, qui la laisse linéaire de chaque côté, la perte de 2 du billet vaut $-4$ ; perdre 10 vaut $-20$ et gagner 10 vaut $+10$, de sorte que le pari de ±10 vaut $\tfrac12\times10-\tfrac12\times20=-5$ : il est refusé. [ajout]
- raison : symbole non défini et mal relié : $\beta$ n'était pas défini alors que l'étape 4 l'emploie pour autre chose, et la perte de 2 citée n'était pas utilisée.

**`dup/parcours-ambiguite`**, étape 16 (`dup/ceu`), ligne « Histoire : »
- ancien : Histoire : « des poids qui ne s'ajoutent pas » — Les poids de l'histoire forment une capacité convexe. Juger par l'intégrale de Choquet revient alors à juger par le maxmin, sur l'ensemble des probabilités qui donnent à chaque événement au moins son poids : les deux voies se rejoignent. [ajout]
- nouveau : Histoire : « des poids qui ne s'ajoutent pas » — Les poids de l'histoire forment une capacité convexe : une réunion d'événements pèse au moins la somme de ses morceaux, comme le noir-ou-jaune, deux tiers contre un sixième plus un sixième. Juger par l'intégrale de Choquet revient alors à juger par le maxmin, sur l'ensemble des probabilités qui donnent à chaque événement au moins son poids : ici $\pi(R)=\tfrac13$ et $\pi(N)$ entre $\tfrac16$ et $\tfrac12$. L'acte qui paie 0, 50 ou 100 y vaut au pire 41,7, sous $\pi(N)=\tfrac12$, comme par l'intégrale : les deux voies se rejoignent. [ajout]
- raison : terme non défini : « capacité convexe » n'était pas expliqué, et l'ensemble de probabilités annoncé n'était ni donné ni vérifié sur l'acte de l'histoire.

**`dup/parcours-portefeuille`**, étape 2 (`dup/poids-de-decision`), ligne « Histoire : »
- ancien : Histoire : « il pondère les états par leur rang » — Avec la déformation du cours, si le premier état paie le moins et le troisième le plus, les poids valent 0,2560, 0,2013 et 0,5426 au lieu de 0,2, 0,3 et 0,5 : le pire et le meilleur état pèsent plus que leur probabilité, celui du milieu moins. [ajout]
- nouveau : Histoire : « il pondère les états par leur rang » — Si le premier état paie le moins et le troisième le plus, les probabilités cumulées valent 0,2, 0,5 et 1, et chaque état pèse le saut qu'y fait la déformation de la théorie cumulative des perspectives, $\varphi$ avec $\beta=0{,}7$ : $\varphi(0{,}2)=0{,}2560$, $\varphi(0{,}5)-\varphi(0{,}2)=0{,}2013$ et $1-\varphi(0{,}5)=0{,}5426$, au lieu de 0,2, 0,3 et 0,5. Le pire et le meilleur état pèsent plus que leur probabilité, celui du milieu moins. [ajout]
- raison : calcul parachuté : « la déformation du cours » n'était pas nommée et les trois poids tombaient sans le mécanisme des sauts sur les probabilités cumulées.

**`dup/parcours-portefeuille`**, étape 4 (`dup/regroupement-des-etats`), ligne « Histoire : »
- ancien : Histoire : « contre l'ordre supposé pour calculer les poids » — On donne le même paiement aux deux états qui se disputent le rang, et l'on traite le bloc comme un seul résultat : les deux mauvais états reçoivent 0,437 chacun, et le meilleur 1,845. Cette solution vaut 1,0618, plus que les autres candidats, à 1,0405 et 1,0021. [ajout]
- nouveau : Histoire : « contre l'ordre supposé pour calculer les poids » — On donne le même paiement $a$ aux deux états qui se disputent le rang, et l'on traite le bloc comme un seul résultat : de probabilité 0,5, il coûte 0,6 et pèse $\varphi(0{,}5)\approx0{,}457$. Avec l'utilité du cours, $u(x)=x^{0{,}6}$, et le budget $0{,}6a+0{,}4b=1$, les deux mauvais états reçoivent 0,437 chacun, et le meilleur 1,845. Cette solution vaut 1,0618, plus que les meilleures solutions des autres ordres, à 1,0405 et 1,0021. [ajout]
- raison : calcul parachuté : l'utilité de l'investisseur n'avait jamais été donnée, de sorte que 0,437, 1,845 et les valeurs 1,0618, 1,0405, 1,0021 ne pouvaient pas se retrouver.

**`pfo/parcours-rendements`**, étape 5 (`pfo/rendement-arithmetique`), ligne « Histoire : »
- ancien : Histoire : « de combien a-t-elle monté » — Première réponse : +10 %, puis −10 %. Mais ces pourcentages ne s'additionnent pas : sur l'ensemble, la variation n'est pas nulle, elle vaut $1{,}1\times0{,}9-1=-1\,\%$. [ajout]
- nouveau : Histoire : « de combien a-t-elle monté » — Première réponse : +10 %, puis −10 %. Mais ces pourcentages ne s'additionnent pas, ils se composent en se multipliant : 100 devient $100\times1{,}1\times0{,}9=99$, si bien que sur l'ensemble la variation n'est pas nulle, elle vaut $99/100-1=-1\,\%$. [ajout]
- raison : calcul parachuté : le produit $1{,}1\times0{,}9$ apparaissait sans dire que les variations se composent en se multipliant.

**`pfo/parcours-rendements`**, étape 6 (`pfo/rendement-logarithmique`), ligne « Histoire : »
- ancien : Histoire : « Les deux questions ont plusieurs réponses » — Seconde réponse : $\ln(110/100)\approx+9{,}53\,\%$, puis $\ln(99/110)\approx-10{,}54\,\%$. Leur somme, $-1{,}01\,\%$, est exactement le rendement logarithmique sur l'ensemble, $\ln(99/100)$. [ajout]
- nouveau : Histoire : « Les deux questions ont plusieurs réponses » — Seconde réponse, le rendement logarithmique : le logarithme du rapport des deux prix, $\ln(110/100)\approx+9{,}53\,\%$, puis $\ln(99/110)\approx-10{,}54\,\%$. Le logarithme changeant le produit des rapports en somme, leur somme, $-1{,}01\,\%$, est exactement le rendement logarithmique sur l'ensemble, $\ln(99/100)$. [ajout]
- raison : terme non défini et calcul parachuté : les $\ln$ apparaissaient sans dire ce qu'est un rendement logarithmique, ni pourquoi leur somme retombe sur celui de l'ensemble.

**`pfo/parcours-rendements`**, étape 7 (`pfo/piege-d-agregation`), ligne « Histoire : »
- ancien : Histoire : « Quel est son rendement » — Arithmétiquement, $\tfrac12\times10\,\%+\tfrac12\times(-10\,\%)=0$ : le portefeuille n'a ni gagné ni perdu. La moyenne des rendements logarithmiques donne pourtant $-0{,}50\,\%$ : ils s'additionnent entre dates, pas entre actifs. [ajout]
- nouveau : Histoire : « Quel est son rendement » — Arithmétiquement, $\tfrac12\times10\,\%+\tfrac12\times(-10\,\%)=0$ : le portefeuille n'a ni gagné ni perdu. En rendements logarithmiques, +10 % et −10 % valent, comme à l'étape précédente, $+9{,}53\,\%$ et $-10{,}54\,\%$ ; leur moyenne donne pourtant $-0{,}50\,\%$ : ils s'additionnent entre dates, pas entre actifs. [ajout]
- raison : calcul parachuté : le $-0{,}50\,\%$ tombait sans que soient rappelés les deux rendements logarithmiques dont il est la moyenne.

**`pfo/parcours-nettoyage`**, étape 3 (`pfo/filtre-z-score-glissant`), ligne « Histoire : »
- ancien : Histoire : « Un même seuil peut-il juger toutes les périodes » — Oui, si la moyenne et l'écart type sont recalculés sur les vingt derniers rendements, et tout rendement dont le score dépasse 3 en valeur absolue remplacé par 0. Un −4 % dans une fenêtre qui, lui compris, a un écart type de 1 % est effacé ; le même −4 % dans une fenêtre agitée, d'écart type 2 %, est gardé. [ajout]
- nouveau : Histoire : « Un même seuil peut-il juger toutes les périodes » — Oui, si la moyenne et l'écart type sont recalculés sur les vingt derniers rendements, et tout rendement à plus de trois écarts types de cette moyenne remplacé par 0. Pour une moyenne nulle, un −4 % dans une fenêtre qui, lui compris, a un écart type de 1 % est à 4 écarts types : il est effacé ; le même −4 % dans une fenêtre agitée, d'écart type 2 %, n'est qu'à 2 écarts types : il est gardé. [ajout]
- raison : terme non défini et calcul implicite : « le score » n'avait jamais été nommé par l'histoire, et les 4 et 2 écarts types qui décident d'effacer ou de garder n'étaient pas écrits.

**`pfo/parcours-volatilite`**, étape 2 (`pfo/ewma`), ligne « Histoire : »
- ancien : Histoire : « Que faut-il croire de sa volatilité aujourd'hui » — L'EWMA mélange la variance de la veille et le carré du dernier rendement : avec $\lambda=0{,}94$, $0{,}94\times0{,}0001+0{,}06\times0{,}02^2=0{,}000118$, soit une volatilité d'environ 1,09 %. Elle monte, sans oublier le passé. [ajout]
- nouveau : Histoire : « Que faut-il croire de sa volatilité aujourd'hui » — L'EWMA, moyenne mobile à pondération exponentielle, mélange la variance de la veille, $0{,}01^2=0{,}0001$ pour 1 % par jour, et le carré du dernier rendement, en donnant au passé le poids $\lambda=0{,}94$ usuel pour des données journalières : $0{,}94\times0{,}0001+0{,}06\times0{,}02^2=0{,}000118$, soit une volatilité de $\sqrt{0{,}000118}\approx1{,}09\,\%$. Elle monte, sans oublier le passé. [ajout]
- raison : terme non défini et calcul parachuté : le sigle EWMA n'était pas expliqué, et ni l'origine de 0,0001 ni celle de $\lambda=0{,}94$ n'étaient dites.

**`pfo/parcours-volatilite`**, étape 3 (`pfo/matrice-de-covariance`), ligne « Histoire : »
- ancien : Histoire : « un actif varie de 1 % par jour, un autre de 2 % » — Pour les deux actifs ensemble, on range les variances et la covariance dans une matrice. Annualisée par 252 : $0{,}01^2\times252=0{,}0252$ et $0{,}02^2\times252=0{,}1008$ sur la diagonale, $0{,}5\times0{,}01\times0{,}02\times252=0{,}0252$ hors de la diagonale. [ajout]
- nouveau : Histoire : « un actif varie de 1 % par jour, un autre de 2 % » — Pour les deux actifs ensemble, on range dans une matrice les variances et la covariance, qui vaut la corrélation fois le produit des écarts types. Portées à l'année en multipliant par ses 252 séances : $0{,}01^2\times252=0{,}0252$ et $0{,}02^2\times252=0{,}1008$ sur la diagonale, $0{,}5\times0{,}01\times0{,}02\times252=0{,}0252$ hors de la diagonale. [ajout]
- raison : calcul parachuté : le terme croisé $0{,}5\times0{,}01\times0{,}02$ apparaissait sans dire que la covariance est la corrélation fois le produit des écarts types, ni ce que sont les 252.

**`pfo/parcours-non-normalite`**, étape 7 (`pfo/queues-epaisses`), ligne « Histoire : »
- ancien : Histoire : « un écart de plus de vingt écarts types » — Les écarts lointains arrivent bien plus souvent que la loi normale ne le dit : une loi de Laplace de même variance dépasse trois écarts types avec une probabilité de 1,4 %, contre 0,27 % pour la loi normale. C'est ce que la kurtosis mesure. [ajout]
- nouveau : Histoire : « un écart de plus de vingt écarts types » — Les écarts lointains arrivent bien plus souvent que la loi normale ne le dit. Une loi de Laplace, dont la densité décroît comme $e^{-|x|}$ et non comme $e^{-x^2/2}$, dépasse à variance égale trois écarts types avec une probabilité de 1,4 %, contre 0,27 % pour la loi normale ; sa kurtosis, qui mesure ce poids des queues, vaut 6 au lieu de 3. [ajout]
- raison : objet introduit sans le dire : la loi de Laplace arrivait sans un mot sur ce qui la distingue de la loi normale ni sur sa kurtosis.

**`pfo/parcours-non-normalite`**, étape 10 (`pfo/test-de-jarque-bera`), ligne « Histoire : »
- ancien : Histoire : « La normalité tient-elle » — Jarque-Bera combine les deux écarts : $JB=\tfrac{1000}{6}\big(0{,}25+\tfrac94\big)\approx416{,}7$, très au-delà du seuil de 5,99 qui correspond au niveau de 5 %. La normalité est rejetée. [ajout]
- nouveau : Histoire : « La normalité tient-elle » — Jarque-Bera combine les deux écarts à la loi normale, l'asymétrie $S$ et l'excès de kurtosis $K_{\mathrm{ex}}$, kurtosis moins les 3 de la loi normale, sur $T$ rendements : $JB=\tfrac{T}{6}\big(S^2+\tfrac{K_{\mathrm{ex}}^2}{4}\big)=\tfrac{1000}{6}\big((-0{,}5)^2+\tfrac{3^2}{4}\big)\approx416{,}7$. Si la loi était normale, $JB$ suivrait une loi du khi-deux à deux degrés de liberté, qui ne dépasse 5,99 qu'une fois sur vingt ; très au-delà, la normalité est rejetée. [ajout]
- raison : calcul parachuté et terme non défini : la formule arrivait déjà évaluée, $0{,}25$ et $9/4$ sans leur origine, le seuil de 5,99 sans sa loi, et « excès de kurtosis » n'avait jamais été défini.

**`pfo/parcours-risque`**, étape 1 (`pfo/quantile`), ligne « Histoire : »
- ancien : Histoire : « Combien peut-il perdre en une mauvaise journée » — Une « mauvaise journée » doit se chiffrer : une des 5 % pires, par exemple. Le rendement qui sépare ces 5 % du reste est un quantile ; pour des rendements normaux de moyenne 0,05 % et d'écart type 2 %, il vaut $0{,}05\,\%-1{,}6449\times2\,\%\approx-3{,}24\,\%$. [ajout]
- nouveau : Histoire : « Combien peut-il perdre en une mauvaise journée » — Une « mauvaise journée » doit se chiffrer : une des 5 % pires, par exemple. Le rendement qui sépare ces 5 % du reste est un quantile. Pour une loi normale, il se trouve toujours à 1,6449 écarts types sous la moyenne, valeur que donne la table de la loi normale ; pour des rendements de moyenne 0,05 % et d'écart type 2 %, il vaut $0{,}05\,\%-1{,}6449\times2\,\%\approx-3{,}24\,\%$. [ajout]
- raison : calcul parachuté : le 1,6449 tombait sans dire qu'il est le quantile à 5 % de la loi normale centrée réduite.

**`pfo/parcours-risque`**, étape 2 (`pfo/valeur-a-risque`), ligne « Histoire : »
- ancien : Histoire : « Un portefeuille de 1 000 000 » — Rapporté au capital, ce quantile devient une perte : si ses rendements étaient normaux, le portefeuille ne perdrait plus de $0{,}0324\times1\,000\,000\approx32\,397$ qu'une journée sur vingt. C'est sa VaR à 95 % sur un jour. [ajout]
- nouveau : Histoire : « Un portefeuille de 1 000 000 » — Rapporté au capital, ce quantile, $-3{,}2397\,\%$ avant arrondi, devient une perte : si ses rendements étaient normaux, le portefeuille ne perdrait plus de $0{,}032397\times1\,000\,000\approx32\,397$ qu'une journée sur vingt. C'est sa valeur à risque, ou VaR, à 95 % sur un jour. [ajout]
- raison : faux et terme non défini : $0{,}0324\times1\,000\,000$ fait 32 400, pas 32 397 (écart d'arrondi), et le sigle VaR n'était pas développé.

**`pfo/parcours-risque`**, étape 3 (`pfo/valeur-a-risque-conditionnelle`), ligne « Histoire : »
- ancien : Histoire : « combien perd-il en moyenne » — C'est la CVaR, la perte moyenne sur les 5 % de jours les pires. Si les rendements étaient normaux, elle vaudrait 40 754, bien au-delà des 32 397 du seuil. [ajout]
- nouveau : Histoire : « combien perd-il en moyenne » — C'est la CVaR, ou valeur à risque conditionnelle, la perte moyenne sur les 5 % de jours les pires. Si les rendements étaient normaux, la moyenne de ces pires rendements se trouverait à $\varphi(1{,}645)/0{,}05\approx2{,}063$ écarts types sous la moyenne, $\varphi$ étant la densité de la loi normale, plus loin que le seuil à 1,645 : $0{,}05\,\%-2{,}063\times2\,\%\approx-4{,}08\,\%$, soit une perte de 40 754, bien au-delà des 32 397 du seuil. [ajout]
- raison : calcul parachuté : 40 754 tombait sans aucun calcul qui y mène.

**`pfo/parcours-risque`**, étape 7 (`pfo/developpement-de-cornish-fisher`), ligne « Histoire : »
- ancien : Histoire : « une asymétrie de −0,5 » — Le quantile gaussien, $-1{,}645$, se corrige avec les deux moments du portefeuille : l'asymétrie négative et les queues épaisses le poussent vers les pertes, à $-1{,}722$. [ajout]
- nouveau : Histoire : « une asymétrie de −0,5 » — Le quantile gaussien, $z_\alpha=-1{,}645$, se corrige avec l'asymétrie $S=-0{,}5$ et l'excès de kurtosis $K=3$ : $q_\alpha\approx z_\alpha+\tfrac{S}{6}(z_\alpha^2-1)+\tfrac{K}{24}(z_\alpha^3-3z_\alpha)-\tfrac{S^2}{36}(2z_\alpha^3-5z_\alpha)$. L'asymétrie négative le pousse vers les pertes de $-0{,}142$ ; à ce seuil, la kurtosis le ramène de $+0{,}061$ et le dernier terme de $+0{,}005$ : il arrive à $-1{,}7217$. [ajout]
- raison : faux et calcul parachuté : au seuil de 5 %, le terme de kurtosis ($z_\alpha^3-3z_\alpha>0$) pousse le quantile vers les gains, pas vers les pertes ; et −1,722 tombait sans la formule qui le donne.

**`pfo/parcours-risque`**, étape 8 (`pfo/var-de-cornish-fisher`), ligne « Histoire : »
- ancien : Histoire : « un excès de kurtosis de 3 » — Avec le quantile corrigé, la VaR passe de 32 397 à 33 935. La CVaR, qui moyenne toute la queue, bouge bien davantage, de 40 754 à 53 511, parce que la kurtosis pèse surtout loin du seuil. [ajout]
- nouveau : Histoire : « un excès de kurtosis de 3 » — Avec le quantile corrigé, la VaR passe de 32 397 à $-(0{,}05\,\%-1{,}7217\times2\,\%)\times1\,000\,000\approx33\,935$. La CVaR, qui moyenne toute la queue, doit corriger chacun de ses quantiles avant d'en faire la moyenne, et bouge bien davantage, de 40 754 à 53 511 : plus d'environ 1,73 écart type sous la moyenne, le terme de kurtosis change de signe et pousse fort vers les pertes. [ajout]
- raison : calcul parachuté : 33 935 et 53 511 tombaient sans le calcul de l'une ni la méthode de l'autre, et « la kurtosis pèse surtout loin du seuil » ne disait pas qu'elle y change de sens.

**`pfo/parcours-portefeuille`**, étape 2 (`pfo/moments-du-portefeuille`), ligne « Histoire : »
- ancien : Histoire : « ils ne sont pas corrélés » — À parts égales, le mélange rapporte $\tfrac12\times6+\tfrac12\times10=8\,\%$, et sa volatilité vaut $\sqrt{0{,}25\times0{,}01+0{,}25\times0{,}04}\approx11{,}18\,\%$ : moins que la moyenne des deux, 15 %, parce que les actifs ne bougent pas ensemble. [ajout]
- nouveau : Histoire : « ils ne sont pas corrélés » — À parts égales, le mélange rapporte la moyenne pondérée $\tfrac12\times6+\tfrac12\times10=8\,\%$. Sa variance est la somme des variances pondérées par le carré des poids, sans terme croisé puisque la corrélation est nulle : $0{,}5^2\times0{,}10^2+0{,}5^2\times0{,}20^2=0{,}0125$, d'où une volatilité de $\sqrt{0{,}0125}\approx11{,}18\,\%$ : moins que la moyenne des deux, 15 %, parce que les actifs ne bougent pas ensemble. [ajout]
- raison : calcul parachuté : $0{,}25\times0{,}01+0{,}25\times0{,}04$ apparaissait sans dire que ce sont carrés des poids et variances, ni pourquoi il n'y a pas de terme croisé.

**`pfo/parcours-portefeuille`**, étape 5 (`pfo/frontiere-efficiente`), ligne « Histoire : »
- ancien : Histoire : « l'un rapporte 6 % par an avec une volatilité de 10 % » — Pour chaque rendement visé, on cherche la répartition la moins risquée. La moins risquée de toutes place 80 % dans ce premier actif : 6,8 % de rendement pour 8,94 % de volatilité, moins que chacun des deux. Les autres cibles tracent une courbe à partir de ce point. [ajout]
- nouveau : Histoire : « l'un rapporte 6 % par an avec une volatilité de 10 % » — Pour chaque rendement visé, on cherche la répartition la moins risquée. La moins risquée de toutes, les actifs n'étant pas corrélés, répartit les poids en raison inverse des variances : $0{,}04/(0{,}01+0{,}04)=80\,\%$ dans ce premier actif, pour $0{,}8\times6+0{,}2\times10=6{,}8\,\%$ de rendement et $\sqrt{0{,}8^2\times0{,}01+0{,}2^2\times0{,}04}\approx8{,}94\,\%$ de volatilité, moins que chacun des deux. Les autres cibles tracent une courbe à partir de ce point. [ajout]
- raison : calcul parachuté : les 80 %, 6,8 % et 8,94 % tombaient sans le raisonnement qui les donne.

**`pfo/parcours-portefeuille`**, étape 7 (`pfo/portefeuille-tangent`), ligne « Histoire : »
- ancien : Histoire : « Combien mettre dans chacun » — Le mélange qui paie le mieux le risque place deux tiers dans le premier actif et un tiers dans le second : 7,33 % de rendement, 9,43 % de volatilité, un ratio de 0,566. C'est le point où la droite partie des 2 % touche la courbe. [ajout]
- nouveau : Histoire : « Combien mettre dans chacun » — Le mélange qui paie le mieux le risque donne à chaque actif, les deux n'étant pas corrélés, un poids proportionnel à son rendement au-delà des 2 % divisé par sa variance : $4/0{,}01=400$ contre $8/0{,}04=200$, soit deux tiers dans le premier actif et un tiers dans le second. Il rapporte 7,33 % pour 9,43 % de volatilité, soit 0,566 de rendement au-delà des 2 % par unité de volatilité. C'est le point où la droite partie des 2 % touche la courbe. [ajout]
- raison : calcul parachuté : les poids deux tiers / un tiers tombaient sans raisonnement, et « un ratio » n'était pas défini par l'histoire.

Aucune étape ajoutée, retirée ni déplacée ; aucune transition ni « Suite » modifiée.

## Dette

Aucune.

## Contradictions source

- **fpp — §2.3** : « $P(t,S)=(1+(S-T)L(t,S))^{-1}$ » ; la durée du taux linéaire vu en
  $t$ est $S-t$, et $T$ n'est pas défini à cet endroit. Coquille probable ; la fiche
  écrit $S-t$.

## Questions pour l'utilisateur

Signalé par l'audit, sans modification (transitions, « Suite », fond) :

**fpp**

- `fpp/parcours-bilan`, étape 3 (`fpp/levier`), transition : « la part de l'actif financée par l'actionnaire » désigne 30/100, l'inverse du levier défini par la fiche (actif / capitaux propres = 100/30).
- `fpp/parcours-flux`, étape 6 (`fpp/duration`), transition : « un mouvement de la courbe » parle de la courbe des taux avant l'étape 7, qui la définit.
- `fpp/parcours-terme`, étape 10 (`fpp/compte-capitalise`), transition : « Un contrat future » n'est pas défini à cet endroit ; seule la Suite qui suit dit qu'il se règle chaque jour. Cette Suite, « Revenons à l'action », ne précise pas s'il s'agit de l'action avec le dividende de l'étape 4 (l'histoire de l'étape 12 le précise maintenant).
- `fpp/parcours-terme`, étape 11 (`fpp/replication-dynamique`), fond : détenir 1/B(t_0,t_i) contrats fait valoir à l'échéance 1/B(t_0,T) fois le gain d'un forward, pas « exactement un contrat » comme le disait l'ancienne histoire. La nouvelle ligne reprend la formule de la fiche (« la valeur finale reste celle visée »). La fiche elle-même mérite une relecture sur ce point.

**dss**

- `dss/parcours-arbres`, point de départ : « Un arbre de décision isolé prédit mal » — l'arbre de décision n'est défini nulle part dans le récit (aucune fiche). La coupure et l'impureté sont désormais expliquées à l'étape 6, mais le départ suppose l'objet connu.
- `dss/parcours-panorama` (étape 13) et `dss/parcours-terrain` (étape 1) : la régression logistique et le séparateur à vaste marge n'ont ni fiche ni étape. Les histoires les présentent seulement comme des modèles mis en concurrence ; aucune définition sourcée n'est possible sans nouvelle fiche.
- `dss/parcours-neurones`, étape 10 : « l'opposé de son gradient » — le gradient n'est pas défini, mais la phrase dit ce qu'il désigne (la direction de plus forte baisse). Laissé tel quel.
- `dss/parcours-selection`, étape 1 : la citation « Une régression sur les cinq » accompagne une régression sur deux prédicteurs ; la citation est gardée telle quelle, la phrase le compense.
- Calculs vérifiés en Python sur le monde des 20 clients (graine 78, figures/cp-de-mallows.py) : erreurs 1,12 / 0,98 / 1,16 / 1,83, σ̂²=1,40, Cp 1,40 / 1,68, AIC 6,29 / 9,59, BIC 1,54 / 2,03, R² 0,49 / 0,55, R² ajusté 0,43 / 0,40, validation croisée 1,66 / 2,22, chemins ascendant et descendant, 45 % de la première composante, 3,73 en PCR à deux composantes, poids PLS 0,57 / 0,62, dernier prédicteur gardé par le lasso (le bruit le plus corrélé, 0,50 contre 0,46 pour l'endettement), 0,95^20, 441 poids, écarts de GINI. Aucune erreur trouvée ; la seule inexactitude était logique (retrecir, étape 12).

**dup**

- `dup/parcours-poids`, étape 2, ligne « Suite : » : « Celui qui achète le billet 2 » se lit comme « le billet numéro 2 » ; il faudrait « le billet au prix de 2 ». Pas de faute de calcul, donc non modifiée.
- `dup/parcours-poids`, étape 6, ligne « Histoire : » : les valeurs 14,250 et 14,875 viennent de L4 slide 34 (la fiche le dit), mais la déformation qui les produit n'est donnée ni par l'histoire ni par la fiche. Le lecteur ne peut donc pas les recalculer. De plus, la ligne porte `[ajout]` alors que les chiffres sont sourcés. La phrase dit honnêtement « Le cours donne une déformation » : laissée telle quelle.
- `dup/parcours-poids`, étape 8, ligne « Histoire : » : les chiffres de Rabin (945, 1 680, 1 575) ont été vérifiés et sont justes. Ils sont tirés de L2 slide 27 mais marqués `[ajout]`, et ils ne se déduisent pas en une phrase. C'est l'énoncé du théorème : laissé tel quel.
- `dup/parcours-ambiguite`, étape 17, ligne « Histoire : » : le prix d'achat de 0 et le prix de vente de 66,7 supposent l'ensemble des compositions de l'étape 9, avec π(N) entre 0 et 2/3. Or l'agent de l'étape 16, celui des poids non additifs, a π(N) entre 1/6 et 1/2, et avec lui on obtiendrait 16,7 et 50. « L'agent de l'urne » est donc ambigu. Le calcul est juste pour l'agent maxmin de l'étape 11 : non modifié, à trancher par l'utilisateur.
- `dup/parcours-portefeuille`, étape 6, ligne « Histoire : » : la formule 10/400 suppose une aversion absolue égale à 1 (c'est la forme de la fiche), et ce n'est pas dit. Écart mineur : non modifié.
- `dup/parcours-comparer`, étape 14 : l'exemple ln(1+ax) de la fiche est connu et n'a pas été traité. Seule la ligne « Histoire : » a été corrigée, parce qu'elle employait $U_{xxa}$ sans le définir.

**pfo**

- `pfo/parcours-non-normalite`, étape 10, ligne « Suite : » : emploie « excès de kurtosis » avant que le récit l'ait défini (l'étape 5 ne parle que de la kurtosis, 3 pour une loi normale). L'histoire de l'étape le définit désormais ; la suite est laissée telle quelle.
- `pfo/parcours-portefeuille`, étape 3, ligne « Suite : » : les rendements journaliers d'exemple (moyenne 0,04 %, écart type 1 %) ne correspondent à aucun des deux actifs du départ (6 %/10 % et 10 %/20 % par an) ; l'annualisation donne 10,08 % et 15,87 %, qui ne se raccrochent à rien. Recommandation : prendre les chiffres journaliers de l'un des deux actifs, p. ex. le second, 10 %/252 ≈ 0,0397 % et 20 %/√252 ≈ 1,26 %.
- `pfo/parcours-nettoyage`, étape 2, ligne « Histoire : » : nomme l'écart « en écarts types » sans jamais dire « score z », le nom de la notion ; ce n'est pas un défaut (le mot n'est pas employé), mais l'étape 3 ne peut donc pas parler de « score ». J'ai reformulé l'étape 3 sans ce mot.
- `pfo/parcours-risque`, étape 8 : 53 511 est la CVaR corrigée intégrée sur la grille du listing (0,0001 à 0,05, trapèzes) ; l'intégrale sur toute la queue donne environ 53 940. Ce n'est pas faux (c'est le calcul du cours, et la fiche le dit sous « Cesse d'être valide quand »), mais le chiffre est propre à cette grille.

Questions antérieures :

1. **dss — source, slide 174** : d'après le rédacteur, qui a lu l'image de la slide, les
   deux étiquettes sous la formule de décroissance des poids sont inversées (« $w_{ij}$ =
   weight-cost parameter », « $\lambda$ is decayed… »). La fiche suit le sens voulu. *À
   vérifier sur la slide ; si c'est confirmé, le noter en contradiction de la source.*
2. **dss — deux graphies du même poids** : le registre écrit $\phi_{mj}$ (slide 72), la Forme
   des moindres carrés partiels $\hat\varphi_{mj}$ comme la slide 90. *Recommandation :
   déclarer la variante au registre, sans rien renommer.*
3. **fpp — §7.1** : le poly appelle $T$ « time to maturity », une durée, alors que la
   condition terminale $C(T,x)$ en fait la date d'échéance. La rubrique écrit « échéance ».
   *Recommandation : le porter en contradiction interne de la source.*
4. **fpp — §7.2.2** : $C$ et $x$ sont réemployés après les changements de variables pour
   d'autres objets (valeur forward, logarithme du forward) ; la rubrique le dit, en
   `[ajout]`. *Recommandation : laisser ainsi.*
5. **fpp — §1.4** : $\pi_E$ et $\pi_A$ sans tilde, lettre de l'espérance, pour des
   variations réalisées. *Recommandation : laisser la rubrique dire la différence.*
6. **dup — collision interne de $\beta$** : paramètre de la pondération de CPT (L3 slide
   38) et exposant de la fonction de valeur à la slide suivante. *Recommandation : la
   déclarer au registre de dup, dans une session sur les notations.*
7. dss — un second tirage pour illustrer le rétrécissement ? Dans le monde des 20
   clients, une variable de bruit est corrélée à la perte par hasard (0,50), et ridge ou
   le lasso n'y battent pas les moindres carrés. *Recommandation : garder ce monde, et en
   tirer un second, plus riche en prédicteurs de bruit, pour le seul parcours « Garder
   toutes les variables » si l'utilisateur veut des gains chiffrés pour ridge.*
8. En fin de parcours, le rappel accumule le départ et toutes les suites : sur
   `dup/parcours-comparer`, six suites à la dernière étape. *Recommandation : le garder
   ainsi ; replier les suites antérieures si l'utilisateur le trouve encombrant.*
9. dss — les exemples des fiches de « rétrécir » restent sur les données Credit du
   cours : les histoires ne les ont pas remplacés (voir la question 7).
10. Les autres fiches de dss sans exemple : les compléter parcours par parcours.
   Recommandation : oui.
11. pfo — garder les arêtes vers dup (`depend_de: [fpp, dup]`) ? Recommandation : oui.
12. pfo — une fiche à part pour le portefeuille de variance minimale globale ?
   Recommandation : non tant qu'aucun chapitre ne le développe.
13. pfo — calculer les parties A et B de l'exercice 3 sur données réelles ?
14. fpp — corriger la note de collision de $l$ et la section « Contradiction » de
    `fpp/ex-16` (le spread est fini en $l=1$) ? Recommandation : oui.
15. fpp — le domaine de $l$ dans l'exercice 16 : à demander à l'enseignant.
16. fpp — la convention $X_t$ : garder la collision déclarée.
17. dss — les trois emplois de $\lambda$ : à demander à l'enseignant.
18. dss — des fiches pour l'arbre de décision, la régression logistique, le SVM ? Attendre
    un support.
19. dup — un relevé des symboles LaTeX du corps absents du registre (avertissement), dans
    une session dédiée au validateur.
20. dup — `dup/maxmin-eu` reste la plus longue fiche du dépôt.
21. **dup — faute probable dans l'exemple de `dup/statique-comparative-risque-accru`** :
    avec $U(x,a)=\ln(1+ax)$ et $x$ uniforme sur $\{40,60\}$, $U_a=x/(1+ax)>0$ partout ;
    la condition du premier ordre $\int U_a\,dF=0$ n'a pas de solution, et le $a$
    optimal n'existe pas. Le lien du parcours ne s'appuie donc pas sur cet exemple.
    *Recommandation : le remplacer par un paiement qui peut être négatif (un rendement en
    excès), après accord ; l'exemple est un `[ajout]`, la source n'est pas en cause.*
22. dup — la forme paramétrique de la courbe de la figure de pondération est un choix,
    non un énoncé : laisser ainsi.
23. pfo — contradictions de la source à confirmer auprès de l'enseignant : chapitre 2
    (signe de l'éq. 2.25, α « niveau de confiance » Déf. 2.5.1, $F$ normale p. 34,
    kurtosis p. 23, $K=3$ Table 2.1, légende Fig. 2.2) et chapitre 3 (légende Fig. 3.1,
    $R_t$ logarithmique au §3.0.7, $W^T\mu$ sur rendements logarithmiques, vérification
    de l'exercice 2).
24. pfo — CVaR de Cornish-Fisher : garder 53 511, valeur du listing (grille tronquée à
    0,0001), ou écrire aussi la valeur de l'intégrale complète, environ 53 940, dans
    « Cesse d'être valide quand » ? *Recommandation : ajouter une phrase à cette rubrique,
    qui dise que le chiffre dépend de la borne basse de la grille.*

## Validation

`263 notions · 0 erreur(s) · 0 avertissement(s)` ; garde-fous : tous se déclenchent ; site
reconstruit.

---
id: fpp/parcours-options
ordre: 5
titre: Évaluer un droit sans obligation
source: poly, §6
---

## Point de départ
Payer quelque chose aujourd'hui pour avoir le droit, et non l'obligation, d'acheter l'action à 100 dans un an. L'engagement ferme d'acheter au prix à terme se signait gratuitement ; combien vaut ce droit ? [ajout]

## À savoir avant
- fpp/mesure-risque-neutre : c'est le moteur de valorisation du parcours ; la valeur d'une option y est l'espérance actualisée de son paiement. [Prop. 6, §6.2]
- fpp/replication-dynamique : c'est elle qui garantit qu'un contrat à prime se réplique, même quand son paiement n'est pas linéaire. [§4.2.2]
- fpp/facteur-actualisation : il actualise le strike dans la parité call-put. [Prop. 7]
- fpp/modele-black-scholes : c'est l'hypothèse sur le sous-jacent qui rend le prix d'une option calculable en forme fermée. [§6.4]
- fpp/responsabilite-limitee : c'est le plancher de l'actionnaire, posé à la fin du premier parcours, que la dernière étape évalue enfin. [§1.4, exo. 16]

## Étapes
1. fpp/payoff
   Pour parler d'un contrat, il faut d'abord dire ce qu'il verse, en fonction de ce qu'on observera. [Déf. 11]
   Histoire : « L'engagement ferme d'acheter au prix à terme » — Pour décrire un contrat, on dit ce qu'il verse selon le prix $S_T$ de l'action dans un an : cette fonction de $S_T$ est son payoff. L'engagement ferme verse $S_T-104{,}08$, positif ou négatif ; le droit du départ versera $(S_T-100)^+$, c'est-à-dire $S_T-100$ si c'est positif et 0 sinon. [ajout]

2. fpp/contrat-a-prime
   Le contrat du point de départ se paie à la signature. Qu'est-ce que cela change à ce qu'on cherche ? [§6]
   Histoire : « Payer quelque chose aujourd'hui » — Pour l'engagement ferme, le prix d'échange était l'inconnue, et le contrat ne coûtait rien. Ici le prix d'échange, 100, est donné ; l'inconnue devient ce qu'on paie aujourd'hui, la prime. [ajout]

3. fpp/option
   La famille la plus importante de ces contrats laisse à son détenteur le choix d'exercer ou non. [Déf. 9]
   Histoire : « le droit, et non l'obligation » — C'est ce qui fait une option : à l'échéance, son détenteur choisit d'acheter ou non, et n'exerce que si cela lui rapporte. [ajout]

4. fpp/call
   Premier droit élémentaire : celui du point de départ, du côté de l'acheteur. [Déf. 9]
   Histoire : « d'acheter l'action à 100 dans un an » — Le droit d'acheter au prix $K=100$ dans un an est un call. Si l'action finit à 104,08, il paie 4,08 ; si elle finit sous 100, on n'exerce pas et il ne paie rien. [ajout]

5. fpp/put
   Second droit élémentaire, symétrique du premier. [Déf. 9]
   Suite : Un autre investisseur veut, lui, le droit de vendre l'action à 100 dans un an. Que lui verse ce droit ? [ajout]
   Histoire : « Que lui verse ce droit » — Il paie $(100-S_T)^+$ : 4 si l'action finit à 96, rien si elle finit au-dessus de 100. C'est un put. [ajout]

6. fpp/parite-call-put
   Ces deux droits sont-ils indépendants l'un de l'autre ? L'absence d'arbitrage les lie, sans aucun modèle. [Prop. 7]
   Histoire : « L'engagement ferme » — Détenir le call et vendre le put, tous deux de strike 100, revient à s'engager ferme à acheter à 100 : $(S_T-100)^+-(100-S_T)^+=S_T-100$. Cet engagement vaut aujourd'hui l'action moins 100 euros payés dans un an ; l'écart entre le prix $C_t$ du call et le prix $P_t$ du put vaut donc, sans aucun modèle, $C_t-P_t=100-100\times0{,}9608=3{,}92$. C'est la parité call-put. [ajout]

7. fpp/valeur-intrinseque
   Pour comprendre ce que coûte le droit de choisir, on compare son prix à ce que vaudrait le contrat si rien n'était aléatoire. [Déf. 12]
   Histoire : « combien vaut ce droit » — Premier repère : si l'action valait à coup sûr sa moyenne risque-neutre, 104,08, le call paierait 4,08, soit $0{,}9608\times4{,}08\approx3{,}92$ aujourd'hui. C'est sa valeur intrinsèque. [ajout]

8. fpp/valeur-temps
   L'écart entre les deux est ce que l'incertitude ajoute, et son signe dépend de la forme du paiement. [Déf. 13]
   Suite : Avec une volatilité de 20 %, ce call se vend 9,93. Pourquoi plus que 3,92 ? [ajout]
   Histoire : « Pourquoi plus que 3,92 » — Parce que l'action peut finir loin de 104,08 : quand elle monte, le call en profite ; quand elle baisse, il ne perd rien au-delà de zéro. Ce paiement convexe vaut plus que sa valeur en la moyenne, et l'écart, $9{,}93-3{,}92$, soit environ 6, est la valeur temps. [ajout]

9. fpp/formule-black-scholes
   Sous le modèle de référence, tout cela se calcule en une formule fermée. [§6.4, §6.5]
   Histoire : « se vend 9,93 » — La formule le calcule : $S_t=100$, $K=100$, $r=4\,\%$, $\sigma=20\,\%$ et un an donnent 9,925 pour le call et 6,004 pour le put ; leur écart, 3,92, est bien celui de la parité. [ajout]

10. fpp/modele-de-merton
   Le premier parcours laissait l'actionnaire d'une entreprise endettée avec une perte bornée en bas. Que vaut ce qu'il détient, et que coûte à l'entreprise le risque qu'elle fasse faillite ? [exos §2.1]
   Suite : Revenons à l'actionnaire d'une entreprise endettée, qui ne perd jamais plus que sa mise. Supposons la dette due dans un an, égale à 80 % de la valeur forward de l'entreprise, et une volatilité de l'actif de 20 %. Que vaut ce que détient l'actionnaire, et que coûte à l'entreprise le risque de faillite ? [ajout]
   Histoire : « Que vaut ce que détient l'actionnaire » — Dans un an, il reçoit la valeur de l'entreprise moins la dette si elle est positive, rien sinon : c'est un call sur l'entreprise, de strike la dette. Avec un taux nul, la formule de Black et Scholes donne à ce call 21,2 % de la valeur forward de l'entreprise ; la dette vaut donc le reste, 78,8 %, moins que les 80 % promis. Cet écart, exprimé en taux, est son spread de crédit, le supplément de rendement qui paie le risque de faillite : environ 149 points de base. [ajout]

## Point d'arrivée
Le droit d'acheter vaut plus que l'engagement ferme au même prix, parce qu'il n'oblige à rien quand l'action baisse : l'écart entre les deux est exactement un put. [Prop. 7]

Son prix dépasse aussi sa valeur intrinsèque, parce que son paiement est convexe ; cette valeur temps, la formule de Black et Scholes la chiffre. [Déf. 13, §6.4]

Le même outil évalue un bilan : les fonds propres d'une entreprise endettée sont un call sur sa valeur, et son spread de crédit est le prix d'un put. [exo. 16]

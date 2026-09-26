---
id: fpp/parcours-options
ordre: 5
titre: Évaluer un droit sans obligation
source: poly, §6
---

## Point de départ
L'investisseur hésite. S'engager ferme à acheter l'action à 104,08 dans un an l'oblige à payer ce prix même si elle s'effondre. Il préférerait avoir seulement le droit de l'acheter à 100 dans un an, s'il le veut. Un tel droit ne peut pas être gratuit : combien vaut-il ? [ajout]

## À savoir avant
- fpp/mesure-risque-neutre : c'est le moteur de valorisation du parcours ; la valeur d'une option y est l'espérance actualisée de son paiement. [Prop. 6, §6.2]
- fpp/replication-dynamique : c'est elle qui garantit qu'un contrat à prime se réplique, même quand son paiement n'est pas linéaire. [§4.2.2]
- fpp/facteur-actualisation : il actualise le strike dans la parité call-put. [Prop. 7]
- fpp/modele-black-scholes : c'est l'hypothèse sur le sous-jacent qui rend le prix d'une option calculable en forme fermée. [§6.4]
- fpp/responsabilite-limitee : c'est le plancher de l'actionnaire, posé à la fin du premier parcours, que la dernière étape évalue enfin. [§1.4, exo. 16]

## Étapes
1. fpp/payoff
   Pour comparer l'engagement et le droit, il faut dire ce que chacun verse dans un an, selon le prix qu'aura l'action. [Déf. 11]
   Histoire : « S'engager ferme à acheter l'action à 104,08 dans un an » — Notons $S_T$ le prix de l'action dans un an. L'engagement verse $S_T-104{,}08$, positif ou négatif. Le droit verse $S_T-100$ si c'est positif, et rien sinon, ce qu'on écrit $(S_T-100)^+$. Cette fonction de $S_T$, ce que le contrat verse, s'appelle son payoff. [ajout]

2. fpp/contrat-a-prime
   Le droit ne se signe pas gratuitement. Qu'est-ce que cela change à ce qu'on cherche ? [§6]
   Histoire : « Un tel droit ne peut pas être gratuit » — Pour l'engagement ferme, rien ne se payait à la signature, et l'inconnue était le prix écrit dans le contrat. Ici, le prix d'achat, 100, est écrit d'avance ; l'inconnue devient ce que l'investisseur paie aujourd'hui pour avoir le droit : la prime. [ajout]

3. fpp/option
   Ce qui sépare le droit de l'engagement tient en un mot : le choix. [Déf. 9]
   Histoire : « s'il le veut » — Dans un an, l'investisseur regarde le prix de l'action et décide : il n'achète que si cela lui rapporte. Un contrat qui laisse ce choix à son détenteur s'appelle une option. [ajout]

4. fpp/call
   Son option à lui est celle d'acheter. Que lui rapporte-t-elle, selon le prix de l'action ? [Déf. 9]
   Histoire : « le droit de l'acheter à 100 dans un an » — Le droit d'acheter à un prix fixé, ici $K=100$, s'appelle un call, et $K$ son strike. Si l'action finit à 104,08, il paie 4,08 ; si elle finit sous 100, l'investisseur n'achète pas, et le call ne paie rien. [ajout]

5. fpp/put
   Le droit inverse existe, et il protège contre la baisse. [Déf. 9]
   Suite : L'investisseur possède aussi des actions, et voudrait être sûr de pouvoir les vendre au moins 100 dans un an. Que lui verserait le droit de vendre l'action à 100 dans un an ? [ajout]
   Histoire : « Que lui verserait le droit de vendre l'action à 100 dans un an » — Il paie $(100-S_T)^+$ : 4 si l'action finit à 96, rien si elle finit au-dessus de 100. Ce droit de vendre s'appelle un put. [ajout]

6. fpp/parite-call-put
   Le call et le put de même strike sont-ils liés ? Sans aucune hypothèse sur l'action, oui. [Prop. 7]
   Histoire : « S'engager ferme » — Détenir le call et avoir vendu le put, tous deux de strike 100, verse $(S_T-100)^+-(100-S_T)^+=S_T-100$ dans tous les cas : c'est s'engager ferme à acheter l'action à 100. Cet engagement vaut aujourd'hui l'action, 100, moins les 100 euros qu'on paiera dans un an, qui valent $100\times0{,}9608=96{,}08$ aujourd'hui : 3,92. En notant $C_t$ le prix du call et $P_t$ celui du put, à ne pas confondre avec le zéro-coupon $P(t,T)$, on a donc $C_t-P_t=3{,}92$. C'est la parité call-put ; elle donne l'écart entre les deux primes, pas chacune d'elles. [ajout]

7. fpp/formule-black-scholes
   Pour obtenir chaque prime, il faut une hypothèse sur la façon dont l'action varie : celle du modèle de Black et Scholes. [§6.4, §6.5]
   Suite : L'action a une volatilité de 20 % par an. Que vaut le call de l'investisseur ? [ajout]
   Histoire : « Que vaut le call de l'investisseur » — Le modèle donne une formule fermée : avec l'action à 100, un strike de 100, un taux de 4 %, une volatilité de 20 % et un an, le call vaut 9,925 et le put 6,004. Leur écart, 3,92, est bien celui de la parité. Le droit coûte donc environ 9,93. [ajout]

8. fpp/valeur-intrinseque
   9,93, c'est bien plus que les 3,92 que vaut l'engagement ferme au même prix. Pour comprendre d'où vient l'écart, retirons d'abord l'aléa. [Déf. 12]
   Histoire : « une volatilité de 20 % par an » — Si l'action ne variait pas et valait à coup sûr sa moyenne risque-neutre, 104,08, le call paierait 4,08 à coup sûr, soit $0{,}9608\times4{,}08\approx3{,}92$ aujourd'hui. C'est sa valeur intrinsèque : le call évalué comme si rien n'était aléatoire. Elle retrouve les 3,92 de l'engagement ferme, parce qu'en 104,08, au-dessus de son strike, le call paie comme l'engagement. [ajout]

9. fpp/valeur-temps
   Le reste de la prime vient donc de l'aléa lui-même. Pourquoi l'aléa vaut-il quelque chose ? [Déf. 13]
   Histoire : « même si elle s'effondre » — Parce que le droit n'a pas ce défaut de l'engagement. Quand l'action monte, le call en profite ; quand elle s'effondre, il ne perd rien au-delà de zéro. Un paiement ainsi coudé vers le haut, qu'on dit convexe, vaut plus que ce qu'il paierait en la moyenne : l'écart, $9{,}93-3{,}92$, soit environ 6, est la valeur temps. [ajout]

10. fpp/modele-de-merton
   Le premier parcours laissait l'actionnaire d'une entreprise endettée avec une perte bornée en bas. Que vaut ce qu'il détient, et que coûte à l'entreprise le risque qu'elle fasse faillite ? [exos §2.1]
   Suite : Revenons à l'actionnaire d'une entreprise endettée, qui ne perd jamais plus que sa mise. Supposons un taux nul, une dette due dans un an égale à 80 % de la valeur de l'entreprise, et une volatilité de l'actif de 20 %. Que vaut ce que détient l'actionnaire, et que coûte à l'entreprise le risque de faillite ? [ajout]
   Histoire : « Que vaut ce que détient l'actionnaire » — Dans un an, il reçoit la valeur de l'entreprise moins la dette si elle est positive, rien sinon : c'est un call sur l'entreprise, de strike la dette. La formule de Black et Scholes donne à ce call 21,2 % de la valeur de l'entreprise ; la dette vaut donc le reste, 78,8 %, moins que les 80 % promis. Cet écart, exprimé en taux, est son spread de crédit, le supplément de rendement qui paie le risque de faillite : environ 149 points de base, soit 1,49 %. [ajout]

## Point d'arrivée
Le droit d'acheter vaut plus que l'engagement ferme au même prix, parce qu'il n'oblige à rien quand l'action baisse : l'écart entre les deux est exactement un put. [Prop. 7]

Son prix dépasse aussi sa valeur intrinsèque, parce que son paiement est convexe ; cette valeur temps, la formule de Black et Scholes la chiffre. [Déf. 13, §6.4]

Le même outil évalue un bilan : les fonds propres d'une entreprise endettée sont un call sur sa valeur, et son spread de crédit traduit en taux le prix d'un put. [exo. 16]

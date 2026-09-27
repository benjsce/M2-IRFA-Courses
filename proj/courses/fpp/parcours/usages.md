---
id: fpp/parcours-usages
ordre: 8
titre: Ce qu'on construit avec des options
source: §9, exos §2.1, exos §2.2
---

## Point de départ
Un épargnant dispose de 100 pour un an. Il ne veut pas risquer de perdre son capital, mais aimerait profiter de la hausse de l'action, qui vaut 100. Le taux est de 4 %. [ajout]

## À savoir avant
- fpp/parite-call-put : elle montre que les deux façons de garantir le capital, zéro-coupon plus call ou action plus put, paient la même chose. [Prop. 7]
- fpp/formule-black-scholes : elle donne le prix du call, 9,93, donc la part de la hausse que l'épargnant peut s'offrir. [§6.4]
- fpp/option : calls et puts sont les briques de toutes les formes de paiement que l'on construit ici. [Déf. 9]
- fpp/formule-de-black : elle évalue un call sur la valeur forward des actifs d'une entreprise, ce que sont ses actions. [éq. 11]
- fpp/responsabilite-limitee : elle arrête à zéro les pertes des actionnaires, et c'est ce plancher qui fait de leurs actions une option. [§1.4]

## Étapes
1. fpp/produit-a-capital-garanti
   Comment garantir le capital tout en gardant une part de la hausse ? [§9.2]
   Histoire : « Il ne veut pas risquer de perdre son capital, mais aimerait profiter de la hausse de l'action » — Un zéro-coupon de 96,08 lui rend 100 à coup sûr ; les 3,92 qui restent achètent 0,395 call : il touchera 39,5 % de la hausse. [ajout]

2. fpp/combinaison-d-options
   L'épargnant regarde ce que d'autres font avec des options : peut-on parier sur l'ampleur d'un mouvement sans parier sur son sens ? [§9.1]
   Suite : Son voisin n'a aucune idée du sens dans lequel l'action va bouger, mais il est sûr qu'elle bougera beaucoup. Quel placement lui rapporte, que l'action monte ou baisse ? [ajout]
   Histoire : « Quel placement lui rapporte, que l'action monte ou baisse » — Il achète un straddle, un call et un put de strike 100 : 15,93 en tout, pour recevoir $|S_T-100|$ dans un an. [ajout]

3. fpp/modele-de-merton
   Que valent des actions dont la perte s'arrête à zéro, et à quel taux l'entreprise emprunte-t-elle ? [exo. 16]
   Suite : L'épargnant hésite à acheter plutôt les actions de l'entreprise du premier parcours : 100 d'actifs, une dette de 80 à rembourser dans un an, et des actifs dont la volatilité serait de 20 %. Que valent aujourd'hui ces actions ? [ajout]
   Histoire : « Que valent aujourd'hui ces actions » — Ces actions sont un call sur les actifs, de strike 80 : elles valent 23,91. La dette vaut donc 76,09, et l'entreprise emprunte avec un spread de crédit de 1,01 %. [ajout]

## Point d'arrivée
Avec des options, on dessine le paiement que l'on veut : un capital garanti, un pari sur l'ampleur d'un mouvement. Et les actions d'une entreprise endettée sont elles-mêmes une option sur ses actifs. [ajout]

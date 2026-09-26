---
id: fpp/parcours-risque-neutre
ordre: 5
titre: Donner un prix à un paiement aléatoire
source: §5
---

## Point de départ
Une banque doit coter un contrat qui paiera dans un an l'excédent de l'action sur 100, si elle le dépasse ; l'action vaut 100 aujourd'hui. Le taux à un an est de 4 %. Ses analystes attendent une hausse moyenne de 8 %. Quelle moyenne prendre pour fixer le prix ? [ajout]

## À savoir avant
- fpp/prix-forward : il donne 104,08, le prix auquel l'action se livre dans un an ; c'est sur lui que la moyenne cherchée va tomber. [Déf. 8]
- fpp/valeur-actuelle-nette : elle actualisait des flux certains ; la banque doit faire de même avec la moyenne d'un flux aléatoire. [Déf. 4]
- fpp/dividendes-intermediaires : un dividende daté abaissait le prix forward ; un dividende continu en est la limite. [§3.2]
- fpp/volatilite : elle mesure de combien l'action s'écarte de sa moyenne, 20 % par an, et le cours va dire comment ce nombre change avec la durée. [Déf. 2]

## Étapes
1. fpp/probabilite-risque-neutre
   Sous quelle probabilité prendre la moyenne d'un paiement aléatoire pour que son prix reste cohérent avec ceux du marché ? [§5.1]
   Histoire : « Quelle moyenne prendre pour fixer le prix » — Pas celle des analystes : celle sous laquelle l'action vaut en moyenne son prix forward, $E^{\mathbb Q}(S_1)=104{,}08$ ; le prix du contrat est cette moyenne du paiement, actualisée par 0,9608. [ajout]

2. fpp/taux-de-dividende
   Comment compter un dividende versé non plus à une date, mais en continu ? [§5.2.1]
   Suite : La banque cote aussi un autre titre, qui vaut 100 et verse en continu un dividende de 2 % par an. [ajout]
   Histoire : « verse en continu un dividende de 2 % par an » — Son prix forward à un an est plus bas : $100\,e^{0,04-0,02}=102{,}02$. [ajout]

3. fpp/tendance-risque-neutre
   À quel rythme ces titres doivent-ils croître en moyenne dans les calculs de la banque ? [§5.2]
   Histoire : « Ses analystes attendent une hausse moyenne de 8 % » — Cette tendance n'entre pas dans le prix : sous $\mathbb Q$, l'action croît au taux $\mu=r=4\,\%$, et le titre à dividende à $\mu=r-d=2\,\%$. [ajout]

4. fpp/echelonnement-de-la-variance
   Comment passer de la dispersion sur un an à la dispersion sur une autre durée ? [§5.3]
   Suite : Il faut aussi savoir de combien l'action peut s'écarter de sa moyenne : sa volatilité est de 20 % par an. Le contrat dure un an ; un contrat voisin dure trois mois. [ajout]
   Histoire : « un contrat voisin dure trois mois » — Sur trois mois, l'écart type du log-rendement vaut $20\,\%\times\sqrt{0{,}25}=10\,\%$ : la moitié de celui d'un an, et non le quart. [ajout]

5. fpp/transformee-de-laplace-gaussienne
   Si le logarithme du prix a une moyenne donnée, quelle est la moyenne du prix lui-même ? [Th. 1]
   Suite : La banque écrit le prix de l'action dans un an sous la forme $100\,e^{Y}$, avec $Y$ gaussien d'écart type 20 %. [ajout]
   Histoire : « avec $Y$ gaussien d'écart type 20 % » — La moyenne de $e^{Y}$ dépasse $e^{E(Y)}$ du facteur $e^{0,2^2/2}=e^{0,02}$ : pour que la moyenne du prix soit $100\,e^{0,04}$, il faut donner à $Y$ la moyenne $0{,}04-0{,}02=0{,}02$. [ajout]

6. fpp/modele-black-scholes
   Quelle loi, au complet, décrit alors le prix de l'action dans un an ? [§5.4]
   Histoire : « sous la forme $100\,e^{Y}$ » — C'est le modèle de Black et Scholes : sous $\mathbb Q$, le prix dans un an a pour médiane 102,02 et pour moyenne 104,08, le prix forward. [ajout]

## Point d'arrivée
La banque sait décrire le prix de l'action dans un an sous la probabilité qui sert à fixer les prix : une loi log-normale, centrée sur le prix forward, de volatilité 20 %. Pour coter son contrat, il ne lui reste qu'à y intégrer le paiement. [ajout]

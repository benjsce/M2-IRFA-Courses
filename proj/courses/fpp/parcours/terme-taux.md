---
id: fpp/parcours-terme-taux
ordre: 3
titre: Fixer aujourd'hui un taux ou un change futur
source: §2.3, §2.4
---

## Point de départ
Dans un an, une entreprise devra emprunter pour un an. Aujourd'hui, les taux zéro-coupon de l'euro valent 4 % à un an et 5 % à deux ans ; personne ne sait quel sera, dans un an, le taux à un an. L'entreprise peut-elle fixer dès aujourd'hui le taux de cet emprunt ? [ajout]

## À savoir avant
- fpp/taux-zero-coupon : il fournit les 4 % et les 5 % du jour, et le taux à un an qu'on observera dans un an, $R(T,S)$, qui est l'inconnue dont l'entreprise veut se protéger ; relu en prix de zéro-coupon, il ramène en t chaque flux des contrats, un par devise pour le change. [§2.3, §2.4]
- fpp/courbe-des-taux : c'est dans la courbe du jour, entre ses points à un an et à deux ans, que se lira le taux cherché. [Déf. 6]

## Étapes
1. fpp/fra
   Quel contrat permettrait de connaître aujourd'hui le taux d'un emprunt qu'on ne fera que dans un an ? [Déf. 7]
   Histoire : « fixer » — Dans un an, l'entreprise empruntera au taux du moment, $R(T,S)$, et en paiera les intérêts dans deux ans. Le FRA lui verse à cette date les intérêts à ce même taux et lui fait payer en échange ceux d'un taux $K$ écrit aujourd'hui : les intérêts variables se compensent, il ne lui reste à payer que ceux au taux $K$. L'échange fixe son emprunt dès la signature. [ajout]

2. fpp/absence-d-arbitrage
   Signer ne coûte rien, et pourtant le taux écrit au contrat n'est pas libre. [Prop. 5]
   Suite : Signer le FRA ne coûte rien. Qu'est-ce qui empêche d'y écrire n'importe quel taux ? [ajout]
   Histoire : « Qu'est-ce qui empêche d'y écrire n'importe quel taux » — L'absence d'arbitrage. Acheter aujourd'hui le zéro-coupon à un an et vendre celui à deux ans reproduit l'emprunt futur, à un taux connu dès maintenant ; un taux $K$ qui s'en écarterait offrirait un gain certain sans mise, et c'est ce que le principe interdit. [ajout]

3. fpp/taux-forward
   Quel taux fixe rend donc le contrat gratuit, avec la courbe du jour ? [§2.3]
   Histoire : « le taux de cet emprunt » — Avec 4 % à un an et 5 % à deux ans : sur deux ans, les intérêts continus totalisent 10 points, dont 4 pour la première année : la seconde doit porter les 6 qui restent. L'entreprise fixe son emprunt à $K=6\,\%$. [ajout]

4. fpp/taux-forward-instantane
   Et si la période garantie se réduisait à un instant ? [§2.3]
   Suite : La trésorière de l'entreprise voudrait le taux garanti non plus pour une année entière, mais pour chaque instant à venir. [ajout]
   Histoire : « pour chaque instant à venir » — Si ce taux est constant sur chaque année, il vaut 4 % pendant la première et 6 % pendant la seconde ; l'aire sous la courbe, 0,10, redonne le zéro-coupon à deux ans, $e^{-0,10}=0{,}9048$. [ajout]

5. fpp/taux-de-change
   Comment lire le prix d'une devise dans une autre, et dans quel sens ? [§2.4]
   Suite : La même entreprise, européenne, recevra aussi dans un an 1 million de dollars d'un client américain. Aujourd'hui, un euro vaut 1,10 dollar. [ajout]
   Histoire : « un euro vaut 1,10 dollar » — Dans la convention du poly, l'euro est la devise locale et $X_t=1{,}10$ ; changé aujourd'hui, le million de dollars ferait 909 091 euros. [ajout]

6. fpp/change-a-terme
   Comme le taux d'un emprunt futur, le change d'un échange futur peut se fixer aujourd'hui. [§2.4]
   Suite : Le taux du dollar à un an est de 5 %. À quel change convertir dès aujourd'hui le million de dollars qui arrivera dans un an ? [ajout]
   Histoire : « À quel change convertir dès aujourd'hui » — À $K=1{,}10\times0{,}9608/0{,}9512\approx1{,}1111$ dollar par euro : le million deviendra 900 045 euros, un peu moins qu'au comptant, parce que le dollar rapporte plus d'intérêts que l'euro. [ajout]

## Point d'arrivée
Un taux et un change futurs se fixent aujourd'hui sans rien payer, et leur valeur se lit dans les prix du jour : 6 % pour l'emprunt, 1,1111 dollar par euro pour le change. Ni l'un ni l'autre n'est une prévision. [ajout]

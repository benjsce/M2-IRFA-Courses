---
id: dup/parcours-portefeuille
ordre: 7
titre: Choisir un portefeuille avec ces modèles
source: L3 slides 42–46, L4 slides 17–34, L4 slides 63–67
---

## Point de départ
Les modèles des parcours précédents changent-ils ce qu'un investisseur achète, et le prix auquel un marché s'équilibre ? Le cours pose la question pour deux d'entre eux, la pondération par rang et l'ambiguïté. [ajout]

## À savoir avant
- dup/rdu : c'est le modèle de préférence de la première moitié du parcours, où les états comptent selon le rang de leur paiement. [L3 slide 42]
- dup/cara : c'est l'utilité de tous les investisseurs de la seconde moitié, choisie parce qu'elle rend la demande calculable. [L4 slide 63]
- dup/equivalent-certain : c'est ce que l'investisseur de la seconde moitié maximise, et qui devient une expression simple sous paiement gaussien. [L4 slide 63]
- dup/maxmin-eu : c'est le critère de l'investisseur ambigu, qui juge chaque position sous le modèle le plus défavorable. [L4 slide 64]

## Étapes
1. dup/portefeuille-rdu
   Le premier problème est d'écrire le programme de l'investisseur quand ses poids dépendent du rang de ses propres paiements. [L3 slide 42]

2. dup/poids-de-decision
   Ce que pèse un état ne se lit plus sur sa probabilité, mais sur l'endroit où tombe son paiement dans le classement. [L4 slide 17]

3. dup/prix-par-unite-de-poids
   Qu'est-ce qui décide alors de l'allocation entre les états, à la place du prix rapporté à la probabilité ? [L4 slide 28]

4. dup/regroupement-des-etats
   Que faire quand la solution ne respecte pas l'ordre qu'on avait supposé pour calculer les poids ? [L4 slide 31, L4 slide 33]

5. dup/assurance-de-portefeuille
   Ce qui en résulte ressemble à un produit que l'on connaît : un plancher de protection en bas, et plus de richesse dans le meilleur état. [L4 slide 32]

6. dup/demande-cara-normale
   Seconde moitié, sur un marché : il faut d'abord la demande d'un investisseur ordinaire qui connaît la loi du paiement. [L4 slide 63]

7. dup/demande-sous-ambiguite
   Que devient cette demande quand l'investisseur ne connaît la moyenne du paiement qu'à un intervalle près ? [L4 slide 64, L4 slide 65]

8. dup/equilibre-sous-ambiguite
   Si le marché réunit des investisseurs des deux sortes, quel prix l'équilibre ? [L4 slide 66]

## Point d'arrivée
La pondération par rang produit une assurance de portefeuille que l'utilité espérée ne produit pas. L'ambiguïté produit des plages de prix où l'on n'échange pas, et elle déplace l'équilibre du marché. [ajout]

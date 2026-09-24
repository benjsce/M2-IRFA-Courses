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

2. fpp/replication
   Ce principe se met en œuvre par un geste unique : fabriquer le flux futur avec ce qu'on peut acheter aujourd'hui. [§3.1]

3. fpp/replication-statique
   Pour livrer une action dans un an, la façon la plus simple est aussi la plus directe. [§3.1]

4. fpp/portage
   Détenir l'action jusqu'à l'échéance n'est pas neutre : elle peut verser des dividendes pendant ce temps. [§3.2]

5. fpp/contrat-prime-nulle
   Le contrat qu'on cherche à évaluer ne coûte rien à la signature. Qu'est-ce qu'on cherche alors, si ce n'est pas un prix ? [§2.3, §3.1]

6. fpp/prix-a-terme
   La réplication et l'absence d'arbitrage donnent la réponse d'un coup, pour une famille entière de contrats. [Prop. 2, Prop. 3]

7. fpp/forward-action
   Premier membre de la famille, le cas de départ : une action livrée à terme. [§3.1, §3.2]

8. fpp/forward-de-change
   Le même raisonnement vaut quand ce qu'on livre est une devise. [§2.4]

9. fpp/fra
   Et quand ce qu'on fixe à l'avance est un taux d'emprunt. [§2.3, Déf. 7]

10. fpp/compte-capitalise
    Un contrat future se règle chaque jour, et chaque règlement se replace à un taux qu'on ne connaît pas encore. Comment transporter de la valeur dans ces conditions ? [§4.2.2]

11. fpp/replication-dynamique
    La réplication ne peut plus être posée une fois pour toutes : il faut la réajuster à chaque pas. [§4.2.2]

12. fpp/prix-future
    Le prix du contrat future s'en déduit, et il ne coïncide plus exactement avec le prix forward. [§4.2]

## Point d'arrivée
Le prix d'un échange futur ne dépend d'aucune prévision : il est fixé par ce que coûte aujourd'hui sa réplication, statique pour un forward, dynamique pour un future. [ajout]

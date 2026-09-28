---
id: dup/parcours-epargne
ordre: 9
titre: Épargner quand on se sait impatient
source: L5 slides 25–52
---

## Point de départ
Quelqu'un a 100 à consommer sur trois périodes ; ce qu'il ne consomme pas est placé sans rendement. Son utilité de chaque période est $\ln c$, et il est biaisé pour le présent : il décote de moitié tout ce qui n'est pas aujourd'hui, sans autre actualisation. Que consommerait-il à chaque période s'il pouvait décider aujourd'hui pour toutes ? [L5 slide 25, ajout]

## À savoir avant
- dup/actualisation-quasi-hyperbolique : elle donne les poids de chaque moi, 1 pour son présent et $\beta\delta^t$ pour la suite ; ici $\beta=\tfrac12$ et $\delta=1$ tout au long. [L5 slide 25]
- dup/sophistication : chaque moi sait ce que feront les suivants, ce qui permet de résoudre à rebours tout le parcours. [L5 slide 25]
- dup/coherence-dynamique : c'est parce que le plan d'aujourd'hui ne tient pas qu'un moyen de s'engager a une valeur. [L5 slide 42]

## Étapes
1. dup/engagement-complet
   La première question est celle d'un plan que personne ne pourrait défaire. [L5 slide 26]
   Histoire : « s'il pouvait décider aujourd'hui pour toutes » — Il pèse 1 la période 1, $\tfrac12$ les deux autres, et le budget vaut 100 : $\beta=\tfrac12$, $\delta=R=1$. Avec $\ln c$, l'équation $u'(c_1)=\beta\delta R\,u'(c_2)$ donne $c_2=\tfrac12c_1$, puis $c_3=c_2$ : il s'engagerait sur 50, 25 et 25. [L5 slide 26, ajout]

2. dup/euler-sans-engagement
   Mais le moi de la période 2 décidera lui-même, et il n'est pas d'accord. [L5 slide 27]
   Suite : Il ne peut pas s'engager : à chaque période, c'est le moi du moment qui choisit. À quel taux le moi 1 actualise-t-il alors la période suivante ? [ajout]
   Histoire : « À quel taux le moi 1 actualise-t-il alors la période suivante » — Le moi 2, avec 50, décote la période 3 de moitié : il consomme les deux tiers de ce qu'il reçoit, 33,3, et laisse 16,7. Un euro de plus qu'on lui transmet serait donc consommé aux deux tiers, que le moi 1 pèse $\tfrac12$, et épargné au tiers, qu'il pèse 1 : il actualise la période 2 par $\tfrac23\times\tfrac12+\tfrac13\times1=\tfrac23$, et non par $\tfrac12$. Avec ce facteur, son équation donne encore 50 pour lui, mais la suite n'est plus 25 et 25. [L5 slide 29, ajout]

3. dup/valeur-de-continuation-non-concave
   Avec le logarithme, tout se calcule à la main, parce que la règle du moi 2 est une droite. [L5 slide 31]
   Suite : Avec une autre utilité, ou un revenu à venir, la règle du moi 2 se courbe. La consommation du moi 1 varie-t-elle encore sans à-coups avec sa richesse ? [ajout]
   Histoire : « varie-t-elle encore sans à-coups avec sa richesse » — Pas toujours. Quand la règle se courbe, un euro de plus pour le moi 2 est de moins en moins consommé, et la part épargnée pèse deux fois plus pour le moi 1, $1/\beta=2$ : la valeur de la richesse transmise peut devenir convexe par endroits. La consommation du moi 1 saute alors d'un niveau à l'autre pour une variation infime de sa richesse. [L5 slide 31, L5 slide 32]

4. dup/relation-d-euler-hyperbolique
   Le cours passe ensuite à un horizon sans fin, avec un revenu du travail aléatoire. [L5 slide 37]
   Suite : Supposons qu'il vive indéfiniment et reçoive chaque période un revenu incertain. Il n'y a plus de dernier moi d'où partir : comment chaque moi consomme-t-il ? [ajout]
   Histoire : « Il n'y a plus de dernier moi d'où partir » — Tous les moi suivent une même règle, qui ne dépend que de la richesse. La condition du moi $t$ reprend le facteur de l'étape précédente, en espérance, avec la pente de la règle de demain : si le moi suivant consomme un dixième de tout euro de plus, le facteur vaut $0{,}1\times\tfrac12+0{,}9\times1=0{,}95$, et l'impatience ne pèse presque plus. [L5 slide 39, L5 slide 40, ajout]

5. dup/actif-illiquide
   Jusqu'ici, rien ne permet au moi d'aujourd'hui de protéger son épargne contre les moi suivants. [L5 slide 42]
   Suite : Désormais, il gagne un revenu chaque période et l'épargne rapporte 10 % par période. Il peut aussi placer une partie de sa richesse dans un fonds de retraite, qu'on ne peut pas consommer dans la période où il rapporte. Que change ce placement ? [ajout]
   Histoire : « un fonds de retraite, qu'on ne peut pas consommer dans la période où il rapporte » — Si le moi précédent lui a laissé 3,82 en liquide et 18,18 dans le fonds, et qu'il gagne 5 cette période, il peut consommer au plus $5+1{,}1\times3{,}82=9{,}2$, alors que ses ressources font 29,2. Le reste ne peut que passer au moi suivant : en remplissant le fonds, le moi d'avant a lié les mains de celui-ci. [L5 slide 43, ajout]

6. dup/jeu-des-moi-successifs
   Avec deux actifs et de nombreuses périodes, il faut une méthode pour trouver ce que chaque moi choisit. [L5 slide 45]
   Suite : L'horizon compte $T$ périodes, donc $T$ moi, et chacun place ou consomme en sachant ce que feront les autres. Comment trouver ce qu'ils choisissent ? [ajout]
   Histoire : « chacun place ou consomme en sachant ce que feront les autres » — C'est un jeu à $T$ joueurs, résolu à rebours depuis le dernier moi. Deux moi voisins n'arbitrent pas de la même façon : dans le problème à trois périodes, le moi 1 voulait autant consommer en 2 qu'en 3, le moi 2 deux fois plus en 2 qu'en 3 : d'où les 25 et 25 du plan, et les 33,3 et 16,7 que le moi 2 choisit. [L5 slide 45, ajout]

7. dup/conditions-d-equilibre-de-laibson
   Reste à caractériser l'équilibre de ce jeu, avec son fonds de retraite. [L5 slide 47]
   Suite : Son revenu vaut 10 les périodes impaires et 5 les paires ; il a 20 dans le fonds au départ, rien en liquide, et son actualisation compense exactement le rendement, $\delta R=1$. Que consomme-t-il les périodes où son revenu tombe à 5 ? [ajout]
   Histoire : « Que consomme-t-il les périodes où son revenu tombe à 5 » — 9,2. Les moi impairs consomment leur revenu, 10, et placent en liquide 3,82, que le moi pair suivant consomme : $5+1{,}1\times3{,}82=9{,}2$. Le reste du fonds, 18,18, échappe au moi pair et reconstitue les 20. Les conditions le confirment : chaque moi consomme tout son liquide, ce qu'il destine au lendemain va en liquide, et le reste dans le fonds. [L5 slide 50, L5 slide 51, ajout]

## Point d'arrivée
Sans engagement, l'agent actualise demain par un facteur qui dépend de ce que son moi suivant fera d'un euro de plus, et ce calcul peut perdre toute régularité. Un actif illiquide lui rend une part d'engagement : l'épargne passe d'un moi au suivant sans que le moi du milieu puisse y toucher. [ajout]

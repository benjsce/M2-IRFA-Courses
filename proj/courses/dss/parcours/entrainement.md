---
id: dss/parcours-entrainement
ordre: 6
titre: Entraîner un réseau qui généralise
source: slides 164–202
---

## Point de départ
Une régression à 19 prédicteurs passerait exactement par les 20 clients de la banque, sans rien avoir appris. [ajout]

Un réseau qui a plus de poids que d'exemples peut faire de même : apprendre par cœur ses exemples d'entraînement. Ce qu'on veut, c'est qu'il réponde juste sur des cas qu'il n'a jamais vus. [slide 165]

## À savoir avant
- dss/reseau-multicouche : c'est le modèle qu'on entraîne dans tout le parcours, et dont on doit choisir la taille. [slide 165, slide 176]
- dss/retropropagation : c'est la procédure d'entraînement que le parcours apprend à arrêter, à régulariser et à organiser. [slide 174, slide 180]
- dss/erreur-de-test : c'est ce que la généralisation désigne, pour un réseau : l'erreur sur des cas non vus. [slide 165]
- dss/surapprentissage : c'est le danger que l'arrêt précoce et la décroissance des poids combattent. [slide 173]
- dss/regularisation : c'est l'idée que la décroissance des poids reprend du bloc sur la régression. [slide 174]
- dss/validation-croisee : c'est ce qui organise les jeux de données d'un entraînement fiable. [slide 181]
- dss/reseau-de-neurones-artificiel : ce sont ses entrées qu'il faut préparer, puisqu'un réseau ne lit que des nombres. [slide 187]
- dss/interpretabilite : c'est ce que l'analyse d'un réseau entraîné cherche à retrouver. [slide 194]

## Étapes
1. dss/generalisation
   Le but de l'entraînement, dit en une question : le réseau répond-il juste hors de ses exemples ? [slide 165]
   Histoire : « qu'il réponde juste sur des cas qu'il n'a jamais vus » — Pour la banque, ces cas sont ses futurs clients : un réseau qui prédit exactement la perte des 20 anciens, et mal celle des nouveaux, n'a rien appris d'utile. C'est sur des cas mis de côté que se juge l'entraînement. [ajout]

2. dss/garantie-pac
   Combien d'exemples faut-il pour espérer une bonne réponse, compte tenu de la taille du réseau ? [slide 168]
   Suite : La banque envisage un réseau à 20 entrées et 20 neurones cachés pour prédire la perte. Combien de clients lui faudrait-il pour l'entraîner ? [ajout]
   Histoire : « Combien de clients lui faudrait-il pour l'entraîner » — Ce réseau compte 441 poids : chacun des 20 neurones cachés reçoit les 20 entrées plus un poids de seuil, soit 420 poids, et la sortie reçoit les 20 neurones cachés plus un seuil, soit 21. La règle du cours, $m>W/\varepsilon$, demande un nombre d'exemples $m$ supérieur au nombre de poids $W$ divisé par la tolérance d'erreur $\varepsilon$ : pour 10 %, plus de $441/0{,}1=4\,410$ exemples. Les 20 clients de la banque en sont très loin. [ajout]

3. dss/architecture-du-reseau
   Cette borne pèse sur un choix qu'on fait avant d'entraîner : la forme du réseau. [slide 176]
   Histoire : « 20 neurones cachés » — La borne pèse sur la forme du réseau : avec 20 clients, il faut un réseau de quelques poids seulement. Trop de poids exige trop d'exemples ; trop peu ne laisse pas la liberté d'apprendre la règle. [ajout]

4. dss/arret-precoce
   Pendant l'entraînement, à quel moment s'arrêter ? [slide 173]
   Histoire : « apprendre par cœur ses exemples d'entraînement » — Pendant l'entraînement, l'erreur sur les exemples d'apprentissage baisse toujours. On suit aussi celle d'un jeu mis de côté, et l'on s'arrête quand elle se met à remonter, avant que le réseau n'apprenne par cœur. [ajout]

5. dss/decroissance-des-poids
   Plutôt que d'arrêter, on peut aussi empêcher les poids inutiles de grossir. [slide 174]
   Histoire : « plus de poids que d'exemples » — Plutôt que d'arrêter, on pénalise la somme des carrés des poids, comme ridge pénalisait celle des coefficients : avec $\lambda=0{,}1$, un poids que rien ne renforce perd un dixième de sa valeur à chaque mise à jour. [ajout]

6. dss/protocole-d-entrainement
   Ces réglages se décident sur quelles données, et comment savoir qu'on ne s'est pas trompé en les choisissant ? [slide 180]
   Histoire : « des cas qu'il n'a jamais vus » — Ces réglages se choisissent sur un jeu de test, et ne peuvent donc pas se juger sur lui : il faut un troisième jeu, jamais touché. Avec 20 clients, on ne peut pas en couper trois ; le cours recommande alors une validation croisée en dix blocs, qui donne dix modèles et une erreur moyenne. [ajout]

7. dss/preparation-des-donnees
   Avant tout cela, les données doivent être mises en état d'être apprises. [slide 187]
   Suite : Aux dossiers de ses clients, la banque ajoute leur situation familiale et leur tranche d'âge. Que faut-il faire aux données avant de les donner au réseau ? [ajout]
   Histoire : « Que faut-il faire aux données avant de les donner au réseau » — Les rassembler, les nettoyer, choisir ce qu'on garde, puis les transformer : un réseau entraîné par rétropropagation n'accepte que des nombres, typiquement entre 0 et 1. [ajout]

8. dss/type-de-donnee
   Tous les attributs ne se traitent pas de la même façon : cela dépend de leur nature. [slide 188]
   Histoire : « leur situation familiale et leur tranche d'âge » — Les deux ne sont pas de même nature. La situation familiale est nominale — célibataire, marié, divorcé —, sans ordre ; la tranche d'âge est ordinale — jeune, adulte, senior —, dans un ordre. L'endettement, lui, est continu. [ajout]

9. dss/codage-des-variables
   Il faut ensuite les traduire en nombres, et la traduction n'est pas neutre. [slide 191]
   Histoire : « situation familiale » — Elle se code un parmi $N$ : $N$ entrées, une par valeur possible, dont seule celle de la valeur prise vaut 1, pour n'imposer aucun ordre ; la tranche d'âge peut se coder en thermomètre, une entrée par tranche, allumées jusqu'à la sienne, ou par un seul réel, deux codages qui respectent son ordre ; l'endettement, par un seul réel ramené entre 0 et 1. [ajout]

10. dss/analyse-post-entrainement
    Le travail fini, reste une boîte de poids. Peut-on encore comprendre ce qu'elle a retenu ? [slide 194]
    Suite : Le réseau entraîné, un régulateur demande à la banque pourquoi il juge un client risqué. Que peut-on lire dans ses poids ? [ajout]
    Histoire : « Que peut-on lire dans ses poids » — Peu de chose directement. On peut faire varier une entrée, l'endettement par exemple, et regarder la perte prédite bouger, ou retirer les attributs un à un et mesurer ce qu'on perd. Ces analyses donnent des vues du réseau, pas sa règle. [ajout]

## Point d'arrivée
Un réseau utile est un réseau qui généralise : cela se décide dans sa taille, dans le moment où l'on arrête l'entraînement, dans la façon de préparer les données, et se vérifie sur des données réservées. [ajout]

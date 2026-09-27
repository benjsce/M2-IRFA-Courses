---
id: dss/parcours-entrainement
ordre: 6
titre: Entraîner un réseau qui généralise
source: slides 164–202
---

## Point de départ
Une régression à 19 prédicteurs, soit 20 coefficients avec la constante, passerait exactement par les 20 clients de la banque, sans rien avoir appris. [ajout]

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
   Un réseau a d'autant plus de poids qu'il est grand. [slide 168]
   Suite : La banque envisage un réseau qui prenne en entrée les cinq prédicteurs de ses clients, l'endettement, le revenu et trois variables sans lien avec la perte, avec 20 neurones cachés. Combien de clients lui faudrait-il pour l'entraîner ? [ajout]
   Histoire : « Combien de clients lui faudrait-il pour l'entraîner » — Ce réseau compte 141 poids : chacun des 20 neurones cachés reçoit les 5 entrées plus un poids de seuil, soit 120 poids, et la sortie reçoit les 20 neurones cachés plus un seuil, soit 21. La règle du cours, $m>W/\varepsilon$, demande un nombre d'exemples $m$ supérieur au nombre de poids $W$ divisé par la tolérance d'erreur $\varepsilon$ : pour 10 %, plus de $141/0{,}1=1\,410$ exemples. Les 20 clients de la banque en sont très loin. [ajout]

3. dss/architecture-du-reseau
   Cette borne pèse sur un choix qu'on fait avant d'entraîner : la forme du réseau. [slide 176]
   Suite : Combien de neurones cachés, et combien de couches, la banque peut-elle se permettre ? [ajout]
   Histoire : « Combien de neurones cachés, et combien de couches » — Vingt neurones cachés, c'est bien trop pour 20 clients. La même règle, lue à l'envers, n'autorise même pas deux poids, puisque $20\times0{,}1=2$ : un seul neurone sur les cinq prédicteurs en a déjà six. La banque n'a pas assez de clients pour un réseau, quelle que soit sa forme ; avec plus d'exemples, la borne dit combien de neurones cachés on peut se permettre. Trop de poids exige trop d'exemples ; trop peu ne laisse pas la liberté d'apprendre la règle. [ajout]

4. dss/preparation-des-donnees
   Le nombre de poids dépend aussi du nombre d'entrées, donc de ce qu'on donne au réseau et de la façon de le lui donner. [slide 187]
   Suite : Aux dossiers de ses clients, la banque ajoute leur situation familiale et leur tranche d'âge. Que faut-il faire aux données avant de les donner au réseau ? [ajout]
   Histoire : « Que faut-il faire aux données avant de les donner au réseau » — Les rassembler, les nettoyer, choisir ce qu'on garde, puis les transformer : un réseau entraîné par rétropropagation n'accepte que des nombres, typiquement entre 0 et 1. Choisir ce qu'on garde, c'est déjà choisir le nombre d'entrées. [ajout]

5. dss/type-de-donnee
   Les attributs ajoutés ne ressemblent pas à l'endettement. [slide 188]
   Suite : La situation familiale, la tranche d'âge et l'endettement sont-ils de même nature ? [ajout]
   Histoire : « sont-ils de même nature » — Les deux ne sont pas de même nature. La situation familiale est nominale — célibataire, marié, divorcé —, sans ordre ; la tranche d'âge est ordinale — jeune, adulte, senior —, dans un ordre. L'endettement, lui, est continu. [ajout]

6. dss/codage-des-variables
   Un réseau n'accepte que des nombres. [slide 191]
   Suite : Comment traduire en nombres une situation familiale ou une tranche d'âge ? [ajout]
   Histoire : « Comment traduire en nombres » — La situation familiale se code un parmi $N$ : $N$ entrées, une par valeur possible, dont seule celle de la valeur prise vaut 1, pour n'imposer aucun ordre ; la tranche d'âge peut se coder en thermomètre, une entrée par tranche, allumées jusqu'à la sienne, ou par un seul réel, deux codages qui respectent son ordre ; l'endettement, par un seul réel ramené entre 0 et 1. La situation familiale prend ainsi trois entrées, et la tranche d'âge en thermomètre trois autres : le réseau passe de 5 à 11 entrées, et de 141 à 261 poids, soit plus de 2 610 exemples pour la même tolérance de 10 %. Coder la tranche d'âge par un seul réel économise deux entrées, et 40 poids. [ajout]

7. dss/arret-precoce
   Les entrées fixées, reste l'entraînement lui-même. [slide 173]
   Suite : Pendant l'entraînement, à quel moment s'arrêter ? [ajout]
   Histoire : « à quel moment s'arrêter » — Sur les clients qui servent à l'entraîner, l'erreur du réseau baisse à chaque passage, et baisserait jusqu'à ce qu'il ait appris leurs pertes par cœur. On met donc quelques clients de côté et l'on suit aussi leur erreur : elle baisse d'abord, puis remonte quand le réseau se met à apprendre ce qui n'appartient qu'aux autres. C'est à ce minimum qu'on arrête l'entraînement, avant qu'il n'apprenne par cœur. [ajout]

8. dss/decroissance-des-poids
   Arrêter n'est pas le seul remède. [slide 174]
   Suite : Peut-on empêcher les poids inutiles de grossir ? [ajout]
   Histoire : « empêcher les poids inutiles de grossir » — Plutôt que d'arrêter, on pénalise la somme des carrés des poids, comme ridge pénalisait celle des coefficients : avec $\lambda=0{,}1$, un poids que rien ne renforce perd un dixième de sa valeur à chaque mise à jour. [ajout]

9. dss/protocole-d-entrainement
   Arrêt et pénalité se règlent, et ces réglages se choisissent sur des données. [slide 180]
   Suite : Sur quels clients régler, et sur lesquels juger ? [ajout]
   Histoire : « Sur quels clients régler, et sur lesquels juger » — Ces réglages se choisissent sur un deuxième jeu de clients, que la slide appelle *validation test set* : un jeu qui sert à régler, pas à juger. Puisque les réglages ont été choisis pour lui, l'erreur qu'on y lit est trop optimiste ; l'erreur de test, sur des cas vraiment jamais vus, se mesure sur un troisième jeu, dit de production, que rien n'a touché. Avec 20 clients, on ne peut pas en couper trois ; le cours recommande alors une validation croisée en dix blocs, qui donne dix modèles et une erreur moyenne. [slide 180, ajout]

10. dss/analyse-post-entrainement
    Le travail fini, reste une boîte de poids. [slide 194]
    Suite : Le réseau entraîné et vérifié, la banque veut savoir sur quoi il s'appuie : sur l'endettement et le revenu, ou sur les trois variables sans lien avec la perte ? Que peut-on lire dans ses poids ? [ajout]
    Histoire : « Que peut-on lire dans ses poids » — Peu de chose directement. On peut faire varier une entrée, l'endettement par exemple, et regarder la perte prédite bouger, ou retirer les attributs un à un et mesurer ce qu'on perd : un réseau qui perdrait beaucoup sans une des variables sans lien aurait appris du bruit. Ces analyses donnent des vues du réseau, pas sa règle. [ajout]

## Point d'arrivée
Un réseau utile est un réseau qui généralise : cela se décide dans sa taille, que fixe aussi le nombre d'entrées, donc la façon de préparer et de coder les données, puis dans le moment où l'on arrête l'entraînement, et se vérifie sur des données réservées. [ajout]

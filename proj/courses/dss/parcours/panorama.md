---
id: dss/parcours-panorama
ordre: 1
titre: Ce qu'apprendre à partir de données veut dire
source: slides 1–22
---

## Point de départ
Le cours s'ouvre sur un avertissement : de 1999 à 2009, les noyades en piscine ont suivi le nombre de films où jouait Nicolas Cage, sans avoir rien à voir avec eux. [slide 4]

Une banque dispose des dossiers de 20 anciens clients en défaut : leur endettement, leur revenu, et la perte qu'ils lui ont coûtée. Que peut-elle en apprendre, et comment saura-t-elle si ce qu'elle a appris est juste ? [ajout]

## Étapes
1. dss/correlation-fallacieuse
   Premier réflexe à perdre : prendre une coïncidence statistique pour un lien. [slide 4]
   Histoire : « sans avoir rien à voir avec eux » — Deux séries peuvent monter et descendre ensemble par pure coïncidence. Si la banque trouve, parmi ce qu'elle sait de ses 20 clients, une variable qui suit la perte, elle devra se demander si le lien existe ou si le hasard l'a fabriqué. [ajout]

2. dss/science-des-donnees
   Une fois prévenu, le cours dresse la carte du domaine selon ce qu'on attend des données. [slide 6]
   Histoire : « Que peut-elle en apprendre » — Tout dépend de ce qu'elle attend : décrire ses 20 dossiers, prédire la perte d'un nouveau client, ou laisser un système décider seul. Le cours range le domaine selon cet objectif. [ajout]

3. dss/fouille-de-donnees
   Au plus simple, on se contente d'ordonner un jeu de données figé et d'y repérer des motifs. [slide 6]
   Histoire : « Une banque dispose des dossiers de 20 anciens clients en défaut » — Au plus simple, elle ordonne ces dossiers tels qu'ils sont, sans rien prédire : repérer, par exemple, que les pertes les plus lourdes vont aux clients les plus endettés. [ajout]

4. dss/apprentissage-automatique
   Un cran plus loin, le programme ne se contente plus de décrire : il s'améliore à partir des exemples. [slide 7]
   Histoire : « Que peut-elle en apprendre » — Un cran plus loin, un programme tire de ces 20 exemples une règle qui prédit la perte, et l'améliore quand de nouveaux dossiers arrivent. [ajout]

5. dss/intelligence-artificielle
   À l'autre extrémité de la carte, le système devrait s'adapter seul à un environnement qui change. [slide 6]
   Histoire : L'histoire de la banque ne va pas jusque-là : à l'autre extrémité du domaine, un système accorderait seul les crédits et s'adapterait, sans intervention, quand l'économie change. Le cours le situe, puis s'en tient en deçà. [ajout]

6. dss/apprentissage-supervise
   Revenons à l'apprentissage automatique : tout dépend de ce qu'on fournit à l'algorithme avec chaque exemple. Premier cas, le plus fréquent dans le cours. [slide 7]
   Histoire : « leur endettement, leur revenu, et la perte qu'ils lui ont coûtée » — Chaque dossier donne une entrée, l'endettement et le revenu, et la réponse attendue, la perte : c'est un exemple étiqueté. Prédire la perte à partir de l'entrée est un apprentissage supervisé. [ajout]

7. dss/apprentissage-non-supervise
   Que peut-on apprendre si l'on ne dispose d'aucune réponse attendue ? [slide 7]
   Suite : Supposons que la banque n'ait que l'endettement et le revenu de ses clients, sans connaître leur perte. Que peut-elle encore apprendre ? [ajout]
   Histoire : « Que peut-elle encore apprendre » — Sans réponse à prédire, elle peut chercher une structure dans les entrées seules, par exemple des groupes de clients qui se ressemblent. [ajout]

8. dss/apprentissage-par-renforcement
   Et si l'on n'a qu'un signal de réussite, qui arrive après coup ? [slide 9]
   Suite : Et si elle n'apprenait qu'en prêtant, et en découvrant des mois plus tard si le prêt a été remboursé ? [ajout]
   Histoire : « en découvrant des mois plus tard si le prêt a été remboursé » — Elle agirait, puis recevrait après coup un signal de réussite, et chercherait à rendre la somme de ces signaux la plus grande possible : c'est l'apprentissage par renforcement. [ajout]

9. dss/domaine-d-application
   Où ces méthodes servent-elles concrètement ? Le cours fait le tour des secteurs avant d'entrer dans la technique. [slide 14]
   Histoire : « Une banque » — La banque n'est qu'un secteur parmi d'autres : le cours passe en revue ceux où ces méthodes servent, avant d'entrer dans la technique. [ajout]

10. dss/interpretabilite
    Un modèle qui prédit bien ne suffit pas toujours : il faut parfois pouvoir expliquer pourquoi il prédit ce qu'il prédit. [slide 13]
    Suite : Un régulateur demande à la banque pourquoi un client est jugé plus risqué qu'un autre. Suffit-il que le modèle prédise bien ? [ajout]
    Histoire : « Suffit-il que le modèle prédise bien » — Non : il faut pouvoir lire dans le modèle l'effet des variables qui comptent, par exemple de combien la perte attendue monte quand l'endettement gagne un point. [ajout]

11. dss/matrice-de-confusion
    Pour juger un classifieur, il faut d'abord compter ses réussites et ses erreurs, en distinguant leurs sortes. [slide 10]
    Suite : La banque veut aussi décider, avant de prêter, si un demandeur fera défaut. Sur 100 dossiers passés, 10 ont fait défaut. Un modèle qui annonce toujours « pas de défaut » a raison 90 fois sur 100 : est-il bon ? [ajout]
    Histoire : « est-il bon » — Non : il ne détecte aucun des 10 défauts. Le tableau qui croise la réalité et la prédiction le montre : aucun vrai positif, défaut annoncé et survenu ; 10 faux négatifs, défauts manqués ; 90 vrais négatifs, bons clients reconnus ; aucune fausse alarme. L'exactitude, part des réponses justes sur les 100 dossiers, vaut 90/100 = 0,90 ; la sensibilité, part des 10 défauts qui sont détectés, vaut 0/10 = 0. [ajout]

12. dss/courbe-roc
    Ces comptes dépendent du seuil de décision. Comment juger le classifieur sans en choisir un ? [slide 12]
    Suite : Un meilleur modèle donne à chaque demandeur une probabilité de défaut, et la banque choisit le seuil au-delà duquel elle refuse. Comment juger ce modèle sans choisir de seuil ? [ajout]
    Histoire : « Comment juger ce modèle sans choisir de seuil » — On trace, pour tous les seuils, la part des défauts détectés contre la part des bons clients refusés : c'est la courbe ROC. L'aire sous la courbe, l'AUC, la résume en un nombre : 0,5 pour un modèle qui tire au hasard, 1 pour un modèle qui sépare parfaitement. Le cours la réétale en $\text{GINI}=2\times\mathrm{AUC}-1$, pour que le hasard vaille 0 : une aire de 0,75, par exemple, donne un GINI de $2\times0{,}75-1=0{,}50$. [ajout]

13. dss/scoring-de-credit
    L'application qui servira de fil au cours, jusqu'à l'article qui le conclut : accorder ou non un crédit. [slide 17]
    Histoire : « si un demandeur fera défaut » — C'est le scoring de crédit, fil du cours jusqu'à sa fin, jugé par le GINI qu'on vient de voir, que le cours exprime en pour cent. Sur le jeu de données du cours, deux modèles qu'il met en concurrence à la fin, la régression logistique et la forêt aléatoire, atteignent un GINI de 51,36 et de 57,84 : la seconde ordonne mieux les demandeurs selon leur risque. [ajout]

## Point d'arrivée
Apprendre, dans ce cours, c'est surtout prédire une réponse à partir d'exemples étiquetés, et juger la prédiction sur ses erreurs. Le reste du cours propose des façons de le faire. [ajout]

---
id: dss/parcours-panorama
ordre: 1
titre: Ce qu'apprendre à partir de données veut dire
source: slides 1–22
---

## Point de départ
Une banque a vu 20 de ses clients faire défaut. Le dossier de chacun donne son endettement, son revenu, trois autres renseignements, et la perte que son défaut a coûtée à la banque. Qu'y voit-on en rangeant ces dossiers ? Un nouveau client demande un prêt. Que peut-elle apprendre de ces 20 dossiers sur ce qu'il lui coûterait s'il faisait défaut, et comment saura-t-elle si ce qu'elle a appris est juste ? [ajout]

## Étapes
1. dss/fouille-de-donnees
   Premier geste : ouvrir les 20 dossiers et les ranger, sans rien chercher à prédire. [slide 6]
   Histoire : « Qu'y voit-on en rangeant ces dossiers » — Rangés par endettement, les dossiers parlent : les dix clients les plus endettés ont coûté en moyenne 4,36 milliers d'euros, les dix autres 2,84. Mais l'un des trois autres renseignements sépare presque aussi bien, 4,19 contre 3,01, et suit même la perte de plus près : sa corrélation avec elle vaut 0,50, celle de l'endettement 0,46. Ranger ainsi un jeu de données figé pour y repérer des motifs, sans rien prédire, c'est la fouille de données. [ajout]

2. dss/correlation-fallacieuse
   La fouille a trouvé un renseignement qui suit la perte. [slide 4]
   Suite : Ce renseignement suit la perte de plus près que l'endettement. La fait-il monter ? [ajout]
   Histoire : « La fait-il monter » — Rien, dans les 20 dossiers, ne permet de le dire : deux séries peuvent monter et descendre ensemble sans que rien ne les relie, et rien dans les données ne distingue une coïncidence d'un lien. Le cours le montre par les noyades en piscine, qui ont suivi de 1999 à 2009 le nombre de films où jouait Nicolas Cage. Seuls d'autres clients peuvent trancher : sur 20 000 clients nouveaux, ce renseignement ne sépare plus rien, la moitié où il est le plus bas perd en moyenne 3,03, l'autre 2,97. [slide 4, ajout]

3. dss/science-des-donnees
   Décrire les 20 dossiers ne dit donc pas ce qui vaudra pour le client suivant. [slide 6]
   Suite : Décrire, prédire, s'adapter : qu'attendre, au juste, des données ? [ajout]
   Histoire : « qu'attendre, au juste, des données » — Le cours découpe le domaine sur un seul axe, ce qu'on attend que le système fasse seul : décrire un jeu de données figé, ce que la banque vient de faire ; apprendre une règle qui vaille pour des données qu'il n'a pas vues ; ou s'adapter seul à un monde qui change. Savoir ce que coûterait un client absent des dossiers relève du deuxième objectif. [ajout]

4. dss/apprentissage-automatique
   Cette règle, qui l'écrit ? [slide 7]
   Histoire : « Que peut-elle apprendre de ces 20 dossiers » — Personne ne l'écrit : un programme la tire des 20 exemples, par exemple une formule qui donne la perte à partir de l'endettement et du revenu, et c'est sur des clients qu'il n'a pas vus, comme les 20 000 de tout à l'heure, qu'on voit si elle tient. Pendant qu'il apprend, les dossiers ne changent pas : l'environnement est fermé. C'est l'apprentissage automatique. [ajout]

5. dss/apprentissage-supervise
   Que reçoit le programme avec chacun des 20 dossiers, pour apprendre ? [slide 7]
   Histoire : « et la perte que son défaut a coûtée à la banque » — Il reçoit une entrée, l'endettement, le revenu et les trois autres renseignements, et la réponse attendue, la perte. L'écart entre la perte qu'il prédit et la perte réelle lui dit de combien il se trompe, et c'est cet écart qu'il cherche à réduire. Apprendre sur des couples formés d'une entrée et de sa réponse, c'est l'apprentissage supervisé ; les composantes de l'entrée s'appellent les prédicteurs, et ce qu'on prédit, la réponse. [ajout]

6. dss/scoring-de-credit
   Jusqu'ici, la banque prédit ce que coûte un client une fois le défaut arrivé. [slide 17]
   Suite : Avant de prêter, elle voudrait savoir si un demandeur fera défaut. Elle reprend les dossiers de tous ses anciens emprunteurs, ceux qui ont fait défaut comme ceux qui ont remboursé. Peut-elle apprendre à reconnaître les premiers ? [ajout]
   Histoire : « Peut-elle apprendre à reconnaître les premiers » — Oui, et l'apprentissage reste supervisé : la réponse n'est plus une perte mais une étiquette à deux valeurs, défaut ou non, et les prédicteurs décrivent l'emprunteur. Prévoir ainsi le défaut, pour décider d'un octroi, d'un suivi ou d'un recouvrement, c'est le scoring de crédit ; le cours y revient à sa toute fin. [slide 17, ajout]

7. dss/matrice-de-confusion
   Un modèle qui range chaque demandeur dans une classe, défaut ou non, s'appelle un classifieur ; reste à le juger. [slide 10, ajout]
   Suite : Sur 100 dossiers passés, 10 ont fait défaut. Un modèle qui annonce toujours « pas de défaut » a raison 90 fois sur 100 : est-il bon ? [ajout]
   Histoire : « est-il bon » — Non : il ne détecte aucun des 10 défauts. Le tableau qui croise la réalité et la prédiction le montre : aucun vrai positif, défaut annoncé et survenu ; 10 faux négatifs, défauts manqués ; 90 vrais négatifs, bons clients reconnus ; aucune fausse alarme. L'exactitude, part des réponses justes sur les 100 dossiers, vaut 90/100 = 0,90 ; la sensibilité, part des 10 défauts qui sont détectés, vaut 0/10 = 0. [ajout]

8. dss/courbe-roc
   Ces comptes dépendent aussi du seuil au-delà duquel le modèle annonce un défaut. [slide 12, ajout]
   Suite : Un meilleur modèle donne à chaque demandeur une probabilité de défaut, et la banque choisit le seuil au-delà duquel elle refuse. Comment juger ce modèle sans choisir de seuil ? [ajout]
   Histoire : « Comment juger ce modèle sans choisir de seuil » — On trace, pour tous les seuils, la part des défauts détectés contre la part des bons clients refusés : c'est la courbe ROC. L'aire sous la courbe, l'AUC, la résume en un nombre : 0,5 pour un modèle qui tire au hasard, 1 pour un modèle qui sépare parfaitement. Le cours la réétale en $\text{GINI}=2\times\mathrm{AUC}-1$, pour que le hasard vaille 0 : si le modèle de la banque a une aire de 0,75, son GINI vaut $2\times0{,}75-1=0{,}50$. [ajout]

9. dss/domaine-d-application
   Un GINI de 0,50 laisse de la marge. [slide 14]
   Suite : Pour le relever, la banque regarde les secteurs où ces techniques ont réussi. D'où y est venu le progrès ? [ajout]
   Histoire : « les secteurs où ces techniques ont réussi » — Du texte à l'image, du risque opérationnel à la cybersécurité, de l'industrie à la pharmacie et au crédit, le cours attribue le succès de ces techniques à l'accès à des données nouvelles et à de meilleures infrastructures, plus qu'à des algorithmes nouveaux. Au crédit, collecter sur le web les données des comptes bancaires des nouveaux clients relève le GINI et le profit de 10 % à 20 % sur ce segment. [slide 14, slide 17, ajout]

10. dss/interpretabilite
    Les données nouvelles ont un revers. [slide 13]
    Suite : Des données nouvelles, ce sont aussi des variables en plus, dont beaucoup ne comptent pas. Le modèle se lit-il encore ? [ajout]
    Histoire : « Le modèle se lit-il encore » — De moins en moins bien. Quand les prédicteurs sont nombreux, beaucoup n'ont aucun effet sur la réponse, comme le renseignement des 20 dossiers qui suivait la perte par hasard, et les laisser dans le modèle rend plus difficile à voir l'effet de ceux qui comptent. Le modèle serait plus facile à interpréter si l'on retirait les variables sans importance, en mettant leurs coefficients à zéro. [slide 13, ajout]

## Point d'arrivée
Apprendre, dans ce cours, c'est surtout tirer d'exemples étiquetés une règle qui prédit, et la juger sur des cas qu'elle n'a pas vus, par ses erreurs et leurs sortes. Pour les 20 dossiers, une question reste ouverte : lesquels de leurs renseignements la règle doit-elle garder ? [ajout]

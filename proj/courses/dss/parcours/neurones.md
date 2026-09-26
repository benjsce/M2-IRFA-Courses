---
id: dss/parcours-neurones
ordre: 5
titre: Du neurone au réseau qui apprend
source: slides 128–163
---

## Point de départ
Quatre points suffisent à mettre en défaut une frontière linéaire : $(0,0)$ et $(1,1)$ dans une classe, $(0,1)$ et $(1,0)$ dans l'autre, le « ou exclusif ». Aucune droite ne les sépare. [slide 149]

Le bloc sur les réseaux de neurones part d'un neurone unique et montre comment en assembler plusieurs pour dépasser cette limite. [slide 148]

## À savoir avant
- dss/apprentissage-supervise : c'est le cadre de tout le bloc ; un réseau apprend à partir d'exemples dont on connaît la réponse. [slide 130, slide 133]

## Étapes
1. dss/reseau-de-neurones-artificiel
   D'où vient l'idée : calculer avec beaucoup d'unités simples reliées entre elles, comme un cerveau. [slide 129]
   Histoire : « part d'un neurone unique » — L'idée vient du cerveau : beaucoup d'unités simples, chacune calculant peu, reliées par des connexions pondérées. Ce que sait le réseau tient tout entier dans ces poids. [ajout]

2. dss/apprentissage-inductif
   Qu'est-ce qu'un tel réseau cherche, au juste, quand on lui montre des exemples ? [slide 133]
   Histoire : « Quatre points » — Le réseau ne connaît pas la règle qui classe ces points ; il n'en voit que des exemples, et cherche, parmi les règles qu'il sait représenter, celle qui les reproduit le mieux. [ajout]

3. dss/fonction-discriminante-lineaire
   La forme d'hypothèse la plus simple, pour deux classes : une frontière droite. [slide 134]
   Suite : Prenons d'abord un problème plus simple, le « ou » logique : $(0,0)$ dans une classe, les trois autres points dans l'autre. Une frontière droite peut-elle les séparer ? [ajout]
   Histoire : « Une frontière droite peut-elle les séparer » — Oui : en notant $x_1$ et $x_2$ les deux coordonnées d'un point, la droite $x_1+x_2=\tfrac12$ laisse $(0,0)$ d'un côté et les trois autres points de l'autre. C'est la forme d'hypothèse la plus simple pour deux classes. [ajout]

4. dss/perceptron
   Le premier neurone artificiel réalise exactement cette frontière. [slide 138, slide 139]
   Histoire : « le « ou » logique » — Un seul neurone réalise cette frontière : il somme ses entrées pondérées et répond 1 si la somme dépasse un seuil. Avec des poids de 1 et un seuil de $\tfrac12$, il calcule exactement le « ou ». [ajout]

5. dss/regle-delta
   Comment ajuste-t-il ses poids à partir de ses erreurs ? [slide 144]
   Histoire : « un neurone unique » — Le neurone ne reçoit pas ses poids, il les apprend : après chaque exemple, il corrige chaque poids en proportion de son erreur et de l'entrée correspondante. S'il répond 0 au point $(1,0)$ au lieu de 1, le poids de $x_1$ augmente. [ajout]

6. dss/limite-du-perceptron
   Cette règle ne sauve pas tout : il existe des classes qu'aucune frontière droite ne sépare. [slide 148]
   Histoire : « Aucune droite ne les sépare » — Sur le « ou exclusif », $(0,0)$ et $(1,1)$ d'un côté, $(0,1)$ et $(1,0)$ de l'autre, sont en diagonale : aucune droite ne les sépare, et la règle de correction peut tourner sans fin sans y parvenir. [ajout]

7. dss/fonction-d-activation
   Pour aller plus loin, la sortie de chaque unité doit pouvoir être autre chose qu'un simple seuil. [slide 151]
   Histoire : « comment en assembler plusieurs » — Pour que des neurones assemblés apprennent ensemble, la fonction qui donne la sortie de chacun, sa fonction d'activation, doit être plus qu'un seuil sec : une fonction lisse de la somme pondérée $a$ de ses entrées, comme la sigmoïde $1/(1+e^{-a})$, qui varie un peu quand les poids varient un peu. [ajout]

8. dss/reseau-multicouche
   Avec ces unités, on peut empiler une couche intermédiaire, et la limite tombe. [slide 141, slide 151]
   Histoire : « pour dépasser cette limite » — Une couche cachée de deux neurones, placée entre les entrées et la sortie, suffit : l'un calcule le « ou », l'autre le « et », et la sortie répond 1 quand le premier dit oui et le second non. C'est exactement le « ou exclusif ». [ajout]

9. dss/apprentissage-profond
   Empiler davantage de couches donne l'apprentissage profond qu'annonçait l'introduction. [slide 8]
   Histoire : « en assembler plusieurs » — Empiler davantage de couches cachées, chacune combinant les sorties de la précédente, donne l'apprentissage profond : des caractéristiques de plus en plus élaborées, extraites couche après couche. [ajout]

10. dss/descente-de-gradient
    Comment entraîner un réseau dont la sortie dépend des poids de plusieurs couches ? D'abord, un principe général de minimisation. [slide 160]
    Suite : Les poids de ce réseau à couche cachée, on vient de les donner à la main. Comment les trouver à partir des quatre exemples seuls ? [ajout]
    Histoire : « Comment les trouver à partir des quatre exemples seuls » — On mesure l'erreur par la somme des carrés des écarts sur les quatre points, et l'on déplace chaque poids d'un petit pas dans la direction où elle baisse le plus vite, l'opposé de son gradient. [ajout]

11. dss/retropropagation
    Ce principe demande de savoir quelle part de l'erreur revient à chaque poids caché. [slide 153, slide 154]
    Histoire : « Les poids de ce réseau à couche cachée » — Pour un neurone de sortie, l'erreur à renvoyer est $d_j=o_j(1-o_j)(t_j-o_j)$ : l'écart entre la cible $t_j$ et la sortie $o_j$, multiplié par $o_j(1-o_j)$, la pente de la sigmoïde en ce point. Si la sortie vaut 0,6 là où il fallait 1, $d_j=0{,}6\times0{,}4\times0{,}4=0{,}096$. Pour les poids cachés, on renvoie cette erreur vers l'arrière, chaque neurone caché en recevant une part proportionnelle à son poids vers la sortie. [ajout]

12. dss/descente-avec-inertie
    L'entraînement peut osciller ou ralentir ; une correction simple l'accélère. [slide 161]
    Suite : Sur le « ou exclusif », l'erreur descend souvent en zigzag, ou stagne longtemps sur un plateau. Peut-on accélérer l'entraînement ? [ajout]
    Histoire : « Peut-on accélérer l'entraînement » — On ajoute à chaque correction une fraction de la précédente : les pas qui vont dans le même sens s'additionnent, ceux qui zigzaguent se compensent. [ajout]

13. dss/apprentissage-en-ligne-ou-par-lot
    Reste à décider quand appliquer les corrections : après chaque exemple, ou après les avoir tous vus. [slide 163]
    Histoire : « à partir des quatre exemples seuls » — On peut corriger les poids après chacun des quatre points, soit quatre mises à jour par passage, ou une seule fois après les avoir vus tous, sur la somme de leurs erreurs. [ajout]

## Point d'arrivée
Un seul neurone trace une frontière droite ; plusieurs couches d'unités non linéaires tracent n'importe quelle frontière, et la rétropropagation sait les entraîner. [ajout]

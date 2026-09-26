---
id: dss/parcours-retrecir
ordre: 3
titre: Garder toutes les variables, mais les contraindre
source: slides 46–95
---

## Point de départ
Sur les 20 clients, sélectionner des prédicteurs donne à chacun soit son coefficient de moindres carrés, soit zéro : il est gardé ou jeté. Et si la banque décrivait ses 20 clients par 30 prédicteurs, les moindres carrés n'auraient même plus de solution unique. Peut-on garder tous les prédicteurs, et limiter autrement ce que le modèle apprend ? [ajout]

## À savoir avant
- dss/moindres-carres-ordinaires : c'est le modèle que les méthodes du parcours modifient, en contraignant ses coefficients ou en changeant ses prédicteurs. [slide 46, slide 71]
- dss/erreur-de-test : c'est la quantité que chaque méthode cherche à réduire. [slide 53]
- dss/validation-croisee : c'est l'outil qui fixe l'intensité de la contrainte. [slide 68]
- dss/surapprentissage : c'est le danger qui grandit quand le nombre de variables approche celui des observations. [slide 92]

## Étapes
1. dss/compromis-biais-variance
   L'idée qui rend possible tout ce parcours : un modèle volontairement moins exact peut prédire mieux. [slide 53]
   Histoire : « limiter autrement ce que le modèle apprend » — Les moindres carrés sur les cinq prédicteurs sont sans biais, mais leurs coefficients bougent beaucoup d'un échantillon de 20 clients à l'autre. Les contraindre les écarte un peu des vrais coefficients et les rend plus stables : on y gagne quand la somme des deux erreurs baisse. [ajout]

2. dss/regularisation
   Première famille : ajouter à l'ajustement une contrainte sur la taille des coefficients. [slide 46]
   Histoire : « Peut-on garder tous les prédicteurs » — On les garde tous, et l'on ajoute à la somme des carrés des erreurs une pénalité sur la taille des coefficients : plus elle pèse, plus ils sont tirés vers zéro, sans qu'aucun soit écarté d'avance. [ajout]

3. dss/regression-ridge
   La contrainte la plus simple porte sur la somme de leurs carrés. [slide 48]
   Histoire : « soit son coefficient de moindres carrés, soit zéro » — Ridge ne choisit plus entre les deux : la pénalité $\lambda\sum_j\beta_j^2$ rapproche tous les coefficients de zéro, d'autant plus que $\lambda$ est grand, sans en annuler aucun. À $\lambda=0$, on retrouve les moindres carrés ; pour $\lambda$ très grand, le modèle nul. [ajout]

4. dss/lasso
   Change-t-on quelque chose en mesurant autrement la taille des coefficients ? [slide 62, slide 63]
   Histoire : « il est gardé ou jeté » — Avec une pénalité en valeur absolue, les coefficients tombent exactement à zéro l'un après l'autre : le lasso rétrécit et sélectionne à la fois. Sur les 20 clients, le dernier prédicteur qu'il garde est pourtant une des trois variables sans lien avec la perte, celle que le hasard y a le plus corrélée : la contrainte ne distingue pas un lien d'une coïncidence. [ajout]

5. dss/choix-du-parametre-de-reglage
   Reste à décider à quel point contraindre. [slide 68]
   Histoire : « limiter autrement » — Reste à choisir la force de la contrainte. On retient la valeur de $\lambda$ qui minimise l'erreur estimée par validation croisée : les blocs de clients qui servaient à comparer des modèles servent ici à comparer des valeurs de $\lambda$. [ajout]

6. dss/reduction-de-dimension
   Seconde famille : garder l'information de tous les prédicteurs, mais en fabriquer un plus petit nombre. [slide 71]
   Histoire : « si la banque décrivait ses 20 clients par 30 prédicteurs » — Seconde voie : résumer ces 30 prédicteurs en quelques combinaisons, par exemple trois, et régresser la perte sur elles. Il n'y a plus que 4 coefficients à estimer au lieu de 31, ce que 20 clients permettent. [ajout]

7. dss/decomposition-en-valeurs-singulieres
   Pour fabriquer ces nouveaux prédicteurs, il faut un outil d'algèbre linéaire. [slide 58]
   Histoire : « les moindres carrés n'auraient même plus de solution unique » — Avec plus de prédicteurs que de clients, la matrice des prédicteurs a des directions sans aucune dispersion. Sa décomposition en valeurs singulières les met à nu : ridge rétrécit chaque direction d'un facteur $d_j^2/(d_j^2+\lambda)$, presque rien sur celles qui sont très dispersées, presque tout sur celles qui ne le sont pas. [ajout]

8. dss/composante-principale
   Il désigne des directions privilégiées dans le nuage des prédicteurs. [slide 74]
   Histoire : « Sur les 20 clients » — Les directions les plus dispersées du nuage des prédicteurs sont les composantes principales. Sur les cinq prédicteurs des 20 clients, tirés indépendamment les uns des autres, aucune ne domine vraiment : la première ne porte qu'environ 45 % de leur variance. [ajout]

9. dss/regression-composantes-principales
   Régresser sur ces directions est la première méthode de la famille. [slide 75]
   Histoire : « Peut-on garder tous les prédicteurs » — On régresse la perte sur les premières composantes. Sur les 20 clients, deux composantes laissent une erreur de test de 3,73, et il faut les cinq, c'est-à-dire ne rien réduire, pour retrouver 1,83 : les composantes résument les prédicteurs, pas ce qui explique la perte. [ajout]

10. dss/moindres-carres-partiels
    Mais ces directions ont été choisies sans regarder la réponse. Et si on la regardait ? [slide 86, slide 87]
    Histoire : « limiter autrement ce que le modèle apprend » — Les moindres carrés partiels choisissent les directions en regardant la perte : la première pèse chaque prédicteur selon son lien avec elle. Sur les 20 clients, elle donne un poids fort à l'endettement, 0,57, mais aussi à la variable de bruit que le hasard a liée à la perte, 0,62. [ajout]

11. dss/haute-dimension
    Tout cela devient indispensable quand les prédicteurs sont aussi nombreux que les observations. [slide 91]
    Histoire : « par 30 prédicteurs » — Avec 30 prédicteurs pour 20 clients, il y a plus de variables que d'observations. Les moindres carrés passent alors exactement par tous les points, avec une erreur d'apprentissage nulle, et ne disent plus rien : seules les méthodes de ce parcours restent utilisables. [ajout]

12. dss/malediction-de-la-dimension
    Dans ce régime, ajouter une variable a un coût, même quand on sait la contraindre. [slide 92]
    Histoire : « Et si la banque décrivait ses 20 clients » — Même contraints, des prédicteurs sans lien avec la perte coûtent : sur les 20 clients, passer de deux à cinq prédicteurs faisait déjà monter l'erreur de test de 1,16 à 1,83. Une variable de plus ne paie que si elle est vraiment liée à la réponse. [ajout]

## Point d'arrivée
On peut garder toutes les variables et contraindre leurs coefficients, ou les résumer en quelques directions ; dans les deux cas, on échange un peu de biais contre beaucoup de variance. [slide 53]

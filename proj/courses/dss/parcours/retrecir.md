---
id: dss/parcours-retrecir
ordre: 3
titre: Garder toutes les variables, mais les contraindre
source: slides 46–95
---

## Point de départ
Sur les 20 clients, sélectionner des prédicteurs donne à chacun soit son coefficient de moindres carrés, soit zéro : il est gardé ou jeté. Bien choisie, la sélection paie, puisque l'erreur de test vaut 1,16 avec l'endettement et le revenu seuls, contre 1,83 avec les cinq prédicteurs ; mal choisie, elle coûte, et la sélection ascendante s'y est trompée. Peut-on garder tous les prédicteurs, et limiter autrement ce que le modèle apprend ? Un modèle ainsi limité serait moins exact sur les 20 clients : pourquoi prédirait-il mieux ? [ajout]

## À savoir avant
- dss/moindres-carres-ordinaires : c'est le modèle que les méthodes du parcours modifient, en contraignant ses coefficients ou en changeant ses prédicteurs. [slide 46, slide 71]
- dss/erreur-de-test : c'est la quantité que chaque méthode cherche à réduire. [slide 53]
- dss/validation-croisee : c'est l'outil qui fixe l'intensité de la contrainte. [slide 68]
- dss/surapprentissage : c'est le danger qui grandit quand le nombre de variables approche celui des observations. [slide 92]

## Étapes
1. dss/compromis-biais-variance
   Limiter un modèle, c'est accepter qu'il se trompe davantage sur les clients qu'il voit. [slide 53]
   Histoire : « pourquoi prédirait-il mieux » — Les moindres carrés sur les cinq prédicteurs sont sans biais, justes en moyenne sur tous les échantillons possibles, mais leurs coefficients bougent beaucoup d'un échantillon de 20 clients à l'autre : leur variance est forte. Les contraindre les écarte un peu des vrais coefficients, un biais, et les rend plus stables : on y gagne quand l'erreur de test, qui additionne le carré du biais, la variance et un bruit irréductible, baisse. [ajout]

2. dss/regularisation
   Première façon de limiter ce qu'il apprend : contraindre la taille de ses coefficients. [slide 46]
   Histoire : « Peut-on garder tous les prédicteurs » — Oui : les cinq prédicteurs restent tous dans le modèle, et c'est la taille de leurs coefficients qu'on limite. À la somme des carrés des erreurs sur les 20 clients, on ajoute une pénalité qui grandit avec les coefficients : un coefficient ne s'éloigne de zéro que s'il fait baisser l'erreur plus qu'il n'alourdit la pénalité. Plus elle pèse, plus tous sont tirés vers zéro, sans qu'il faille décider d'avance, comme la sélection ascendante, lesquels jeter. [ajout]

3. dss/regression-ridge
   Reste à choisir comment mesurer la taille des coefficients. [slide 48]
   Suite : Première mesure, la plus simple : la somme de leurs carrés. Que deviennent alors les cinq coefficients ? [ajout]
   Histoire : « la somme de leurs carrés » — Ils rétrécissent tous sans qu'aucun ne s'annule : c'est la régression ridge. La pénalité $\lambda\sum_j\beta_j^2$ rapproche tous les coefficients de zéro, d'autant plus que $\lambda$ est grand, sans choisir entre garder et jeter. À $\lambda=0$, on retrouve les moindres carrés ; pour $\lambda$ très grand, le modèle nul. [ajout]

4. dss/lasso
   Une seconde mesure de la taille est possible. [slide 62, slide 63]
   Suite : Et si l'on mesurait leur taille par la somme de leurs valeurs absolues ? [ajout]
   Histoire : « la somme de leurs valeurs absolues » — Avec une pénalité en valeur absolue, les coefficients tombent exactement à zéro l'un après l'autre : le lasso rétrécit et sélectionne à la fois. Sur les 20 clients, le dernier prédicteur qu'il garde est pourtant une des trois variables sans lien avec la perte, celle que le hasard y a le plus corrélée : la contrainte ne distingue pas un lien d'une coïncidence. [ajout]

5. dss/choix-du-parametre-de-reglage
   Ridge et le lasso laissent un réglage ouvert. [slide 68]
   Suite : Tous deux dépendent de $\lambda$. Quelle force de pénalité prendre ? [ajout]
   Histoire : « Quelle force de pénalité prendre » — On retient la valeur de $\lambda$ qui minimise l'erreur estimée par validation croisée : les blocs de clients qui servaient à comparer des modèles servent ici à comparer des valeurs de $\lambda$. Sur les 20 clients, les mêmes cinq blocs de 4 retiennent pour ridge un $\lambda$ voisin de 5, et l'erreur de test monte de 1,83 à 2,43 ; pour le lasso, un $\lambda$ voisin de 2,5, et elle vaut 1,87. Sur si peu de clients, l'erreur estimée par validation croisée est elle-même bruitée : elle réclame une contrainte, et la contrainte dégrade la prédiction. [ajout]

6. dss/reduction-de-dimension
   Contraindre les coefficients n'est pas la seule façon de limiter le modèle. [slide 71]
   Suite : Peut-on résumer les cinq prédicteurs en quelques prédicteurs nouveaux ? [ajout]
   Histoire : « résumer les cinq prédicteurs en quelques prédicteurs nouveaux » — Oui : on fabrique quelques combinaisons des cinq, par exemple deux, et l'on régresse la perte sur elles. Il n'y a plus que 3 coefficients à estimer, constante comprise, au lieu de 6, et aucun prédicteur n'est écarté : chacun entre dans les combinaisons. [ajout]

7. dss/decomposition-en-valeurs-singulieres
   Reste à choisir ces combinaisons. [slide 58]
   Suite : Dans quelles directions les 20 clients s'étalent-ils, et de combien ? [ajout]
   Histoire : « Dans quelles directions les 20 clients s'étalent-ils, et de combien » — La décomposition en valeurs singulières de la matrice des cinq prédicteurs, centrés et réduits, donne des directions de leur espace et, pour chacune, un étirement $d_j$ qui mesure la dispersion des clients le long d'elle : de 6,7 pour la plus étirée à 2,1 pour la moins étirée. Elle relit au passage ridge, qui rétrécit chaque direction d'un facteur $d_j^2/(d_j^2+\lambda)$ : avec le $\lambda$ voisin de 5 de la validation croisée, 0,90 pour la plus étirée, 0,47 pour la moins étirée. [ajout]

8. dss/composante-principale
   Les directions sont connues, avec leur étirement. [slide 74]
   Suite : Laquelle de ces directions garder pour résumer les cinq prédicteurs ? [ajout]
   Histoire : « Laquelle de ces directions garder » — Les plus étirées : ce sont les composantes principales. Sur les 20 clients, la première porte environ 45 % de la dispersion des cinq prédicteurs, et elle les mêle tous les cinq, l'endettement comme les trois variables sans lien. [ajout]

9. dss/regression-composantes-principales
   Les composantes principales résument les cinq prédicteurs. [slide 75]
   Suite : Que vaut une régression de la perte sur les premières composantes ? [ajout]
   Histoire : « une régression de la perte sur les premières composantes » — Peu de chose : sur les 20 clients, deux composantes laissent une erreur de test de 3,73, et il faut les cinq, c'est-à-dire ne rien réduire, pour retrouver 1,83 : les composantes résument les prédicteurs, pas ce qui explique la perte. [ajout]

10. dss/moindres-carres-partiels
    Mais ces directions ont été choisies sans regarder la réponse. [slide 86, slide 87]
    Suite : Et si l'on choisissait les directions en regardant la perte ? [ajout]
    Histoire : « choisissait les directions en regardant la perte » — Les moindres carrés partiels choisissent les directions en regardant la perte : la première pèse chaque prédicteur selon son lien avec elle. Sur les 20 clients, elle donne un poids fort à l'endettement, 13,6, et plus fort encore à la variable de bruit que le hasard a liée à la perte, 14,8. [ajout]

11. dss/haute-dimension
    Sur cinq prédicteurs, aucune de ces méthodes n'a approché le 1,16 de la sélection. [slide 91]
    Suite : Si la banque décrivait ses 20 clients par 30 prédicteurs, que pourraient encore faire les moindres carrés ? [ajout]
    Histoire : « Si la banque décrivait ses 20 clients par 30 prédicteurs » — Avec plus de variables que d'observations, les moindres carrés ont une infinité de solutions, qui passent toutes exactement par les 20 clients avec une erreur d'apprentissage nulle : ils ne disent plus rien. Ridge, le lasso et les composantes principales donnent encore une réponse. L'exemple des 20 clients ne va pas jusque-là, et ne chiffre pas ce qu'elles y gagneraient. [ajout]

12. dss/malediction-de-la-dimension
    Reste ce que coûtent les variables en trop. [slide 92]
    Suite : Contraindre les coefficients suffit-il à rendre inoffensifs les prédicteurs sans lien avec la perte ? [ajout]
    Histoire : « rendre inoffensifs les prédicteurs sans lien avec la perte » — Non : même contraints, des prédicteurs sans lien avec la perte coûtent : sur les 20 clients, passer de deux à cinq prédicteurs faisait monter l'erreur de test des moindres carrés de 1,16 à 1,83, et ni ridge ni le lasso, quelle que soit la force de leur contrainte, ne ramènent le modèle à cinq prédicteurs sous 1,8. Une variable de plus ne paie que si elle est vraiment liée à la réponse. [ajout]

## Point d'arrivée
Contraindre les coefficients, ou résumer les prédicteurs en quelques directions, c'est accepter un peu de biais dans l'espoir de perdre davantage de variance. [slide 53]

Sur les 20 clients, l'échange ne paie pas : aucune de ces méthodes ne ramène l'erreur de test sous 1,8, loin du 1,16 de la sélection. Une variable sans lien, que le hasard a liée à la perte autant que l'endettement, ne se distingue pas d'un vrai prédicteur sur ces 20 clients : ni rétrécir ni combiner ne sait la mettre à part, et la validation croisée, sur si peu de clients, choisit mal la force de la contrainte. Ces méthodes ne deviennent indispensables que lorsque les prédicteurs sont aussi nombreux que les clients, là où les moindres carrés ne répondent plus. [ajout]

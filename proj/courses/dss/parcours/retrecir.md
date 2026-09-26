---
id: dss/parcours-retrecir
ordre: 3
titre: Garder toutes les variables, mais les contraindre
source: slides 46–95
---

## Point de départ
Sur les 20 clients, sélectionner des prédicteurs donne à chacun soit son coefficient de moindres carrés, soit zéro : il est gardé ou jeté. Bien choisie, la sélection paie, puisque l'erreur de test vaut 1,16 avec l'endettement et le revenu seuls, contre 1,83 avec les cinq prédicteurs ; mal choisie, elle coûte, et la sélection ascendante s'y est trompée. Peut-on garder tous les prédicteurs, et limiter autrement ce que le modèle apprend ? [ajout]

## À savoir avant
- dss/moindres-carres-ordinaires : c'est le modèle que les méthodes du parcours modifient, en contraignant ses coefficients ou en changeant ses prédicteurs. [slide 46, slide 71]
- dss/erreur-de-test : c'est la quantité que chaque méthode cherche à réduire. [slide 53]
- dss/validation-croisee : c'est l'outil qui fixe l'intensité de la contrainte. [slide 68]
- dss/surapprentissage : c'est le danger qui grandit quand le nombre de variables approche celui des observations. [slide 92]

## Étapes
1. dss/compromis-biais-variance
   Pourquoi un modèle volontairement moins exact pourrait-il prédire mieux ? [slide 53]
   Histoire : « limiter autrement ce que le modèle apprend » — Les moindres carrés sur les cinq prédicteurs sont sans biais, justes en moyenne sur tous les échantillons possibles, mais leurs coefficients bougent beaucoup d'un échantillon de 20 clients à l'autre : leur variance est forte. Les contraindre les écarte un peu des vrais coefficients, un biais, et les rend plus stables : on y gagne quand l'erreur de test, qui additionne le carré du biais, la variance et un bruit irréductible, baisse. [ajout]

2. dss/regularisation
   Première façon de limiter ce qu'il apprend : contraindre la taille de ses coefficients. [slide 46]
   Histoire : « Peut-on garder tous les prédicteurs » — On les garde tous, et l'on ajoute à la somme des carrés des erreurs une pénalité sur la taille des coefficients : plus elle pèse, plus ils sont tirés vers zéro, sans qu'aucun soit écarté d'avance. [ajout]

3. dss/regression-ridge
   La contrainte la plus simple porte sur la somme de leurs carrés. [slide 48]
   Histoire : « soit son coefficient de moindres carrés, soit zéro » — Ridge ne choisit plus entre les deux : la pénalité $\lambda\sum_j\beta_j^2$ rapproche tous les coefficients de zéro, d'autant plus que $\lambda$ est grand, sans en annuler aucun. À $\lambda=0$, on retrouve les moindres carrés ; pour $\lambda$ très grand, le modèle nul. [ajout]

4. dss/lasso
   Change-t-on quelque chose en mesurant autrement la taille des coefficients ? [slide 62, slide 63]
   Histoire : « il est gardé ou jeté » — Avec une pénalité en valeur absolue, les coefficients tombent exactement à zéro l'un après l'autre : le lasso rétrécit et sélectionne à la fois. Sur les 20 clients, le dernier prédicteur qu'il garde est pourtant une des trois variables sans lien avec la perte, celle que le hasard y a le plus corrélée : la contrainte ne distingue pas un lien d'une coïncidence. [ajout]

5. dss/choix-du-parametre-de-reglage
   Ridge et le lasso dépendent de $\lambda$ : quelle valeur prendre ? [slide 68]
   Histoire : « limiter autrement » — On retient la valeur de $\lambda$ qui minimise l'erreur estimée par validation croisée : les blocs de clients qui servaient à comparer des modèles servent ici à comparer des valeurs de $\lambda$. Sur les 20 clients, les mêmes cinq blocs de 4 retiennent pour ridge un $\lambda$ voisin de 5, et l'erreur de test monte de 1,83 à 2,43 ; pour le lasso, un $\lambda$ voisin de 2,5, et elle vaut 1,87. Sur si peu de clients, l'erreur estimée par validation croisée est elle-même bruitée : elle réclame une contrainte, et la contrainte dégrade la prédiction. [ajout]

6. dss/reduction-de-dimension
   Plutôt que de contraindre les coefficients, peut-on résumer les cinq prédicteurs en un plus petit nombre de prédicteurs nouveaux ? [slide 71]
   Histoire : « Peut-on garder tous les prédicteurs » — Oui : on fabrique quelques combinaisons des cinq, par exemple deux, et l'on régresse la perte sur elles. Il n'y a plus que 3 coefficients à estimer, constante comprise, au lieu de 6, et aucun prédicteur n'est écarté : chacun entre dans les combinaisons. [ajout]

7. dss/decomposition-en-valeurs-singulieres
   Quelles combinaisons ? Il faut d'abord savoir dans quelles directions les 20 clients s'étalent, et de combien. [slide 58]
   Histoire : « Sur les 20 clients » — La décomposition en valeurs singulières de la matrice des cinq prédicteurs, centrés et réduits, donne des directions de leur espace et, pour chacune, un étirement $d_j$ qui mesure la dispersion des clients le long d'elle : de 6,7 pour la plus étirée à 2,1 pour la moins étirée. Elle relit au passage ridge, qui rétrécit chaque direction d'un facteur $d_j^2/(d_j^2+\lambda)$ : avec le $\lambda$ voisin de 5 de la validation croisée, 0,90 pour la plus étirée, 0,47 pour la moins étirée. [ajout]

8. dss/composante-principale
   Laquelle de ces directions garder pour résumer les cinq prédicteurs ? [slide 74]
   Histoire : « Sur les 20 clients » — Les plus étirées : ce sont les composantes principales. Sur les 20 clients, la première porte environ 45 % de la dispersion des cinq prédicteurs, et elle les mêle tous les cinq, l'endettement comme les trois variables sans lien. [ajout]

9. dss/regression-composantes-principales
   Que vaut alors une régression de la perte sur les premières composantes ? [slide 75]
   Histoire : « Peut-on garder tous les prédicteurs » — Peu de chose : sur les 20 clients, deux composantes laissent une erreur de test de 3,73, et il faut les cinq, c'est-à-dire ne rien réduire, pour retrouver 1,83 : les composantes résument les prédicteurs, pas ce qui explique la perte. [ajout]

10. dss/moindres-carres-partiels
    Mais ces directions ont été choisies sans regarder la réponse. Et si on la regardait ? [slide 86, slide 87]
    Histoire : « limiter autrement ce que le modèle apprend » — Les moindres carrés partiels choisissent les directions en regardant la perte : la première pèse chaque prédicteur selon son lien avec elle. Sur les 20 clients, elle donne un poids fort à l'endettement, 13,6, et plus fort encore à la variable de bruit que le hasard a liée à la perte, 14,8. [ajout]

11. dss/haute-dimension
    Sur cinq prédicteurs, aucune de ces méthodes n'a approché le 1,16 de la sélection. Quand deviennent-elles indispensables ? [slide 91]
    Suite : Si la banque décrivait ses 20 clients par 30 prédicteurs, que pourraient encore faire les moindres carrés ? [ajout]
    Histoire : « Si la banque décrivait ses 20 clients par 30 prédicteurs » — Avec plus de variables que d'observations, les moindres carrés ont une infinité de solutions, qui passent toutes exactement par les 20 clients avec une erreur d'apprentissage nulle : ils ne disent plus rien. Ridge, le lasso et les composantes principales donnent encore une réponse. L'exemple des 20 clients ne va pas jusque-là, et ne chiffre pas ce qu'elles y gagneraient. [ajout]

12. dss/malediction-de-la-dimension
    Dans ce régime, ajouter une variable a un coût, même quand on sait la contraindre. [slide 92]
    Histoire : « Peut-on garder tous les prédicteurs » — Même contraints, des prédicteurs sans lien avec la perte coûtent : sur les 20 clients, passer de deux à cinq prédicteurs faisait monter l'erreur de test des moindres carrés de 1,16 à 1,83, et ni ridge ni le lasso, quelle que soit la force de leur contrainte, ne ramènent le modèle à cinq prédicteurs sous 1,8. Une variable de plus ne paie que si elle est vraiment liée à la réponse. [ajout]

## Point d'arrivée
Contraindre les coefficients, ou résumer les prédicteurs en quelques directions, c'est accepter un peu de biais dans l'espoir de perdre davantage de variance. [slide 53]

Sur les 20 clients, l'échange ne paie pas : aucune de ces méthodes ne ramène l'erreur de test sous 1,8, loin du 1,16 de la sélection. Une variable sans lien, que le hasard a liée à la perte autant que l'endettement, ne se distingue pas d'un vrai prédicteur sur ces 20 clients : ni rétrécir ni combiner ne sait la mettre à part, et la validation croisée, sur si peu de clients, choisit mal la force de la contrainte. Ces méthodes ne deviennent indispensables que lorsque les prédicteurs sont aussi nombreux que les clients, là où les moindres carrés ne répondent plus. [ajout]

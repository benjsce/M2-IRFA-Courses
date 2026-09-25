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

2. dss/regularisation
   Première famille : ajouter à l'ajustement une contrainte sur la taille des coefficients. [slide 46]

3. dss/regression-ridge
   La contrainte la plus simple porte sur la somme de leurs carrés. [slide 48]

4. dss/lasso
   Change-t-on quelque chose en mesurant autrement la taille des coefficients ? [slide 62, slide 63]

5. dss/choix-du-parametre-de-reglage
   Reste à décider à quel point contraindre. [slide 68]

6. dss/reduction-de-dimension
   Seconde famille : garder l'information de tous les prédicteurs, mais en fabriquer un plus petit nombre. [slide 71]

7. dss/decomposition-en-valeurs-singulieres
   Pour fabriquer ces nouveaux prédicteurs, il faut un outil d'algèbre linéaire. [slide 58]

8. dss/composante-principale
   Il désigne des directions privilégiées dans le nuage des prédicteurs. [slide 74]

9. dss/regression-composantes-principales
   Régresser sur ces directions est la première méthode de la famille. [slide 75]

10. dss/moindres-carres-partiels
    Mais ces directions ont été choisies sans regarder la réponse. Et si on la regardait ? [slide 86, slide 87]

11. dss/haute-dimension
    Tout cela devient indispensable quand les prédicteurs sont aussi nombreux que les observations. [slide 91]

12. dss/malediction-de-la-dimension
    Dans ce régime, ajouter une variable a un coût, même quand on sait la contraindre. [slide 92]

## Point d'arrivée
On peut garder toutes les variables et contraindre leurs coefficients, ou les résumer en quelques directions ; dans les deux cas, on échange un peu de biais contre beaucoup de variance. [slide 53]

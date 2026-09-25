---
id: dss/parcours-selection
ordre: 2
titre: Choisir les variables d'une régression
source: slides 23–45
---

## Point de départ
Les 20 clients de la banque sont décrits par cinq prédicteurs : l'endettement, le revenu, et trois variables sans aucun lien avec la perte. Une régression sur les cinq ajuste mieux les 20 clients qu'une régression sur les deux premiers, avec une erreur moyenne de 0,98 contre 1,12 ; sur 20 000 clients nouveaux, elle se trompe davantage, 1,83 contre 1,16. Lesquels garder, quand on ne dispose pas des clients nouveaux ? [ajout]

## À savoir avant
- dss/apprentissage-supervise : c'est le cadre de tout le parcours ; chaque exemple porte la réponse que la régression doit reproduire. [slide 25]
- dss/interpretabilite : c'est l'une des deux raisons de réduire le nombre de variables ; un modèle à peu de prédicteurs se lit. [slide 27]

## Étapes
1. dss/moindres-carres-ordinaires
   Le point de départ de tout le bloc est le modèle linéaire le plus classique. [slide 25]

2. dss/erreur-de-test
   Pour juger un modèle, l'erreur sur les données qui ont servi à l'ajuster est trompeuse. Laquelle regarder ? [slide 37]

3. dss/surapprentissage
   Le piège que cette erreur-là permet de voir : un modèle trop souple qui colle aux données. [slide 27]

4. dss/critere-penalise
   On ne dispose pas toujours de données fraîches. Peut-on estimer l'erreur de test à partir de l'erreur d'apprentissage seule ? [slide 39]

5. dss/cp-de-mallows
   Première réponse, pour les moindres carrés. [slide 41]

6. dss/aic
   Deuxième réponse, qui ne se limite pas à la régression linéaire. [slide 42]

7. dss/bic
   Troisième réponse, plus sévère avec les grands modèles quand l'échantillon grandit. [slide 43]

8. dss/r2-ajuste
   Quatrième réponse, la seule qui se lise à la hausse. [slide 44]

9. dss/validation-croisee
   Plutôt que de corriger l'erreur d'apprentissage, on peut aussi estimer directement l'autre. [slide 45]

10. dss/selection-de-variables
    Ces outils permettent enfin de comparer des modèles de tailles différentes. Première stratégie pour en réduire la taille. [slide 28]

11. dss/selection-de-sous-ensemble
    La façon la plus directe : ne garder qu'une partie des prédicteurs. [slide 28]

12. dss/meilleur-sous-ensemble
    Si l'on essaie toutes les parties possibles, lequel choisir ? [slide 29]

13. dss/selection-pas-a-pas
    Avec des dizaines de prédicteurs, le nombre de parties explose. Peut-on n'en visiter qu'une petite fraction ? [slide 32]

14. dss/selection-ascendante
    On peut partir de rien et avancer. [slide 34]

15. dss/selection-descendante
    Ou partir de tout et reculer. [slide 35]

## Point d'arrivée
Pour choisir des variables, on estime l'erreur de test, par une pénalité ou par validation croisée, et l'on parcourt les sous-ensembles, tous ou pas à pas. [ajout]

Sur les 20 clients, le $C_p$, l'AIC, le BIC, le $R^2$ ajusté et la validation croisée désignent tous le modèle à l'endettement et au revenu ; la sélection descendante le retrouve, la sélection ascendante, piégée par une variable de bruit, le manque. [ajout]

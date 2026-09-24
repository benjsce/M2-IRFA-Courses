---
id: dss/parcours-selection
ordre: 2
titre: Choisir les variables d'une régression
source: slides 23–45
---

## Point de départ
On dispose de dizaines de prédicteurs pour expliquer une réponse. Les mettre tous dans une régression la rend meilleure sur les données d'apprentissage, et pourtant souvent pire sur de nouvelles données. Lesquels garder ? [slide 27]

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

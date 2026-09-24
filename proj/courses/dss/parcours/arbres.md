---
id: dss/parcours-arbres
ordre: 4
titre: Des arbres à la forêt
source: slides 96–127
---

## Point de départ
Un arbre de décision isolé prédit mal, mais il s'ajuste très vite : on peut se permettre d'en construire beaucoup. Comment faire pour qu'ils n'apprennent pas tous la même chose ? [slide 97]

## À savoir avant
- dss/compromis-biais-variance : c'est ce que les méthodes d'ensemble exploitent ; un arbre isolé a une variance forte, et moyenner plusieurs arbres la réduit sans toucher au biais. [ajout]
- dss/validation-croisee : c'est ce que l'erreur hors du sac remplace, sans avoir à réserver de données. [slide 102]
- dss/interpretabilite : c'est ce que l'on perd en moyennant des centaines d'arbres, et que l'importance des variables tente de rendre. [slide 104]
- dss/surapprentissage : c'est le risque propre au boosting, qui corrige sans fin les erreurs restantes. [slide 123]

## Étapes
1. dss/methode-d-ensemble
   L'idée de départ : plutôt qu'un arbre, beaucoup d'arbres, à condition qu'ils ne se ressemblent pas tous. [slide 97]

2. dss/bootstrap
   Pour construire beaucoup d'arbres, il faut beaucoup d'échantillons, alors qu'on n'en a qu'un. [slide 99]

3. dss/bagging
   Avec ces échantillons, la première méthode d'ensemble va de soi. [slide 98]

4. dss/erreur-out-of-bag
   Chaque arbre laisse de côté une partie des données. Peut-on s'en servir pour juger l'ensemble ? [slide 102]

5. dss/importance-des-variables
   L'ensemble prédit mieux qu'un arbre, mais on ne sait plus quelles variables comptent. [slide 104]

6. dss/importance-par-impurete
   Première réponse : additionner ce que chaque coupure sur une variable a apporté. [slide 104, slide 105]

7. dss/importance-par-permutation
   Seconde réponse : brouiller une variable et regarder ce qu'on perd. [slide 106]

8. dss/variance-d-une-moyenne-correlee
   Retour au bagging : moyenner des arbres réduit-il la variance autant qu'on l'espère ? [slide 108]

9. dss/foret-aleatoire
   Si les arbres se ressemblent trop, comment les forcer à différer ? [slide 110, slide 111]

10. dss/boosting
    Une tout autre façon d'assembler des arbres : non plus en parallèle, mais les uns après les autres. [slide 122]

## Point d'arrivée
Un arbre seul est instable ; beaucoup d'arbres, rendus différents par le rééchantillonnage, le hasard des coupures ou la correction successive des erreurs, prédisent bien, au prix d'une lecture moins directe. [ajout]

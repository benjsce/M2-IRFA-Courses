---
id: dss/parcours-arbres
ordre: 4
titre: Des arbres à la forêt
source: slides 96–127
---

## Point de départ
Un arbre de décision isolé prédit mal, mais il s'ajuste très vite : on peut se permettre d'en construire beaucoup. [slide 97]

Tirer 20 clients avec remise parmi les 20 de la banque en laisse en moyenne 7 de côté, et chaque tirage donne un autre arbre. Comment faire pour que ces arbres n'apprennent pas tous la même chose, et à quoi servent les clients laissés de côté ? [ajout]

## À savoir avant
- dss/compromis-biais-variance : c'est ce que les méthodes d'ensemble exploitent ; un arbre isolé a une variance forte, et moyenner plusieurs arbres la réduit sans toucher au biais. [ajout]
- dss/validation-croisee : c'est ce que l'erreur hors du sac remplace, sans avoir à réserver de données. [slide 102]
- dss/interpretabilite : c'est ce que l'on perd en moyennant des centaines d'arbres, et que l'importance des variables tente de rendre. [slide 104]
- dss/surapprentissage : c'est le risque propre au boosting, qui corrige sans fin les erreurs restantes. [slide 123]

## Étapes
1. dss/methode-d-ensemble
   L'idée de départ : plutôt qu'un arbre, beaucoup d'arbres, à condition qu'ils ne se ressemblent pas tous. [slide 97]
   Histoire : « on peut se permettre d'en construire beaucoup » — Au lieu d'un arbre sur les 20 clients, on en construit beaucoup et l'on combine leurs prédictions de la perte ; encore faut-il qu'ils ne répètent pas tous le même arbre. [ajout]

2. dss/bootstrap
   Pour construire beaucoup d'arbres, il faut beaucoup d'échantillons, alors qu'on n'en a qu'un. [slide 99]
   Histoire : « Tirer 20 clients avec remise parmi les 20 de la banque » — Faute d'autres clients, on fabrique de nouveaux échantillons en tirant avec remise : certains clients reviennent deux fois, d'autres manquent. En moyenne, $20\times0{,}95^{20}\approx7{,}2$ clients restent de côté. [ajout]

3. dss/bagging
   Avec ces échantillons, la première méthode d'ensemble va de soi. [slide 98]
   Histoire : « chaque tirage donne un autre arbre » — On construit un arbre par tirage, et la perte prédite pour un nouveau client est la moyenne des pertes que prédisent tous les arbres, par exemple 500. [ajout]

4. dss/erreur-out-of-bag
   Chaque arbre laisse de côté une partie des données. Peut-on s'en servir pour juger l'ensemble ? [slide 102]
   Histoire : « à quoi servent les clients laissés de côté » — Chaque client est absent d'environ 36 % des tirages : on le prédit avec les seuls arbres qui ne l'ont pas vu, environ 180 sur 500, et l'on moyenne ces erreurs sur les 20 clients. On obtient une erreur de test sans avoir mis un seul client de côté. [ajout]

5. dss/importance-des-variables
   L'ensemble prédit mieux qu'un arbre, mais on ne sait plus quelles variables comptent. [slide 104]
   Suite : Cinq cents arbres ne se lisent pas comme une régression. Quelles variables comptent dans la perte qu'ils prédisent ? [ajout]
   Histoire : « Quelles variables comptent dans la perte qu'ils prédisent » — On attribue à chaque prédicteur une part du travail de l'ensemble. Si l'ensemble a bien appris, l'endettement et le revenu en reçoivent l'essentiel, et les trois variables sans lien presque rien. [ajout]

6. dss/importance-par-impurete
   Première réponse : additionner ce que chaque coupure sur une variable a apporté. [slide 104, slide 105]
   Histoire : « Quelles variables comptent » — Première mesure : additionner, pour chaque prédicteur, la baisse de la somme des carrés des erreurs obtenue à chaque coupure faite sur lui, et moyenner sur les 500 arbres. [ajout]

7. dss/importance-par-permutation
   Seconde réponse : brouiller une variable et regarder ce qu'on perd. [slide 106]
   Histoire : « Cinq cents arbres ne se lisent pas comme une régression » — Seconde mesure : mélanger au hasard la colonne d'un prédicteur entre les clients hors du sac, et regarder de combien la prédiction se dégrade. Une variable sans lien avec la perte, même si elle a servi à couper, ne coûte rien quand on la brouille. [ajout]

8. dss/variance-d-une-moyenne-correlee
   Retour au bagging : moyenner des arbres réduit-il la variance autant qu'on l'espère ? [slide 108]
   Suite : Les arbres sont bâtis sur des tirages des mêmes 20 clients, et se ressemblent. Moyenner des arbres qui se ressemblent réduit-il la variance autant qu'on l'espère ? [ajout]
   Histoire : « Moyenner des arbres qui se ressemblent réduit-il la variance » — Non : avec une corrélation $\rho$ entre arbres, la variance de la moyenne vaut $\rho\,\sigma^2+(1-\rho)\,\sigma^2/B$. À $\rho=0{,}5$, elle ne descend jamais sous la moitié de celle d'un arbre, même avec 500 arbres. [ajout]

9. dss/foret-aleatoire
   Si les arbres se ressemblent trop, comment les forcer à différer ? [slide 110, slide 111]
   Histoire : « Comment faire pour que ces arbres n'apprennent pas tous la même chose » — À chaque coupure, on ne laisse candidats que quelques prédicteurs tirés au hasard, par exemple 2 des 5 : trois fois sur cinq, le prédicteur le plus fort n'est pas candidat, et les arbres cessent de se ressembler. [ajout]

10. dss/boosting
    Une tout autre façon d'assembler des arbres : non plus en parallèle, mais les uns après les autres. [slide 122]
    Suite : Et si, au lieu de construire les arbres indépendamment, chacun corrigeait ce que les précédents ont manqué ? [ajout]
    Histoire : « chacun corrigeait ce que les précédents ont manqué » — Le boosting ajuste chaque petit arbre sur les pertes que l'ensemble prédit encore mal, les résidus, et n'en ajoute qu'une fraction $\lambda$, par exemple un centième : l'ensemble apprend lentement, arbre après arbre. [ajout]

## Point d'arrivée
Un arbre seul est instable ; beaucoup d'arbres, rendus différents par le rééchantillonnage, le hasard des coupures ou la correction successive des erreurs, prédisent bien, au prix d'une lecture moins directe. [ajout]

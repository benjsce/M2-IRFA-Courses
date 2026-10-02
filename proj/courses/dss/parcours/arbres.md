---
id: dss/parcours-arbres
ordre: 4
titre: Des arbres à la forêt
source: slides 96–127
---

## Point de départ
Un arbre de décision prédit la perte d'un client par une suite de questions à seuil sur ses prédicteurs, et lui attribue la perte moyenne des anciens clients qui ont répondu de même. Sur les 20 clients de la banque, sa première question est « $x_3\le0{,}22$ ? », qui sépare 8 clients de perte moyenne 2,43 et 12 de perte moyenne 4,39 ; or $x_3$ est l'une des trois variables sans aucun lien avec la perte, qu'une coïncidence de l'échantillon a liée à elle. [slide 115, ajout]

Mais un arbre isolé prédit mal : cette question dépend de quelques clients. Retirez-en deux, et dans 42 cas sur 190 la première question ne porte plus sur $x_3$, l'arbre change, et sa prédiction avec lui. En revanche, un arbre se construit en un instant. Plutôt que de se fier à un seul arbre aussi instable, ne peut-on en combiner beaucoup ? [slide 97, slide 98, ajout]

## À savoir avant
- dss/arbre-de-decision : c'est la brique de tout le parcours ; chaque méthode assemble des arbres, et c'est leur instabilité qu'elle combat. [slide 97, slide 98]
- dss/compromis-biais-variance : c'est ce que les méthodes d'ensemble exploitent ; un arbre isolé a une variance forte, et moyenner plusieurs arbres la réduit sans toucher au biais. [ajout]
- dss/validation-croisee : c'est ce que l'erreur hors du sac remplace, sans avoir à réserver de données. [slide 102]
- dss/interpretabilite : c'est ce que l'on perd en moyennant des centaines d'arbres, et que l'importance des variables tente de rendre. [slide 104]
- dss/surapprentissage : c'est le risque propre au boosting, qui corrige sans fin les erreurs restantes. [slide 123]

## Étapes
1. dss/methode-d-ensemble
   L'idée de départ : plutôt qu'un arbre, beaucoup d'arbres, à condition qu'ils ne se ressemblent pas tous. [slide 97]
   Histoire : « ne peut-on en combiner beaucoup » — Oui : au lieu d'un seul arbre sur les 20 clients, on en construit beaucoup et l'on moyenne leurs prédictions de la perte. Un arbre change avec quelques clients ; la moyenne de nombreux arbres change beaucoup moins, comme la moyenne de nombreuses mesures bruitées. Encore faut-il qu'ils ne répètent pas tous le même arbre. [slide 97, slide 98, ajout]

2. dss/bootstrap
   Des arbres différents demandent des données différentes, et la banque n'a qu'un échantillon. [slide 99]
   Suite : Pour construire beaucoup d'arbres, il faudrait beaucoup d'échantillons de clients ; la banque n'a que ses 20 anciens clients. Peut-on en fabriquer d'autres à partir de celui-là ? [ajout]
   Histoire : « Peut-on en fabriquer d'autres à partir de celui-là » — Oui, en tirant 20 clients avec remise parmi les 20 de la banque, et en recommençant : certains clients reviennent deux fois, d'autres manquent. À chacun des 20 tirages, un client donné a 19 chances sur 20, soit 0,95, de ne pas sortir ; il manque donc à tout l'échantillon avec la probabilité $0{,}95^{20}\approx0{,}36$, et en moyenne $20\times0{,}36\approx7{,}2$ clients restent de côté. [ajout]

3. dss/bagging
   Avec ces échantillons, la première méthode d'ensemble va de soi. [slide 98]
   Suite : Chaque tirage donne un autre arbre. Comment en tirer une seule prédiction de la perte ? [ajout]
   Histoire : « Comment en tirer une seule prédiction de la perte » — On répète le tirage, disons 500 fois, et l'on construit un arbre par tirage ; la perte prédite pour un nouveau client est la moyenne des pertes que prédisent ces 500 arbres. C'est le bagging, de l'anglais bootstrap aggregating : agréger des arbres bâtis sur des tirages avec remise. [ajout]

4. dss/erreur-out-of-bag
   Chaque arbre laisse de côté une partie des données. [slide 102]
   Suite : Chaque tirage laisse en moyenne 7 des 20 clients de côté. À quoi servent les clients laissés de côté ? [ajout]
   Histoire : « À quoi servent les clients laissés de côté » — Un client absent d'un tirage est dit « hors du sac », out of bag, pour l'arbre correspondant ; il l'est pour environ 36 % des tirages, la probabilité $0{,}95^{20}$ calculée plus haut. On le prédit avec ces seuls arbres qui ne l'ont pas vu, environ 180 sur 500, et l'on moyenne ces erreurs sur les 20 clients. On obtient une erreur de test sans avoir mis un seul client de côté. [ajout]

5. dss/variance-d-une-moyenne-correlee
   Les 500 arbres ne sont pas indépendants les uns des autres. [slide 108]
   Suite : Les arbres sont bâtis sur des tirages des mêmes 20 clients, et se ressemblent. Moyenner des arbres qui se ressemblent réduit-il la variance autant qu'on l'espère ? [ajout]
   Histoire : « Moyenner des arbres qui se ressemblent réduit-il la variance » — Non : si chaque arbre a une variance $\sigma^2$ et deux arbres une corrélation $\rho$, la moyenne de $B$ arbres a pour variance $\rho\,\sigma^2+(1-\rho)\,\sigma^2/B$. Le second terme s'efface quand $B$ grandit, pas le premier : à $\rho=0{,}5$, elle ne descend jamais sous la moitié de celle d'un arbre, même avec 500 arbres. [ajout]

6. dss/foret-aleatoire
   La moyenne bute sur la ressemblance des arbres. [slide 110, slide 111]
   Suite : Sur 500 tirages, près d'un arbre sur deux commence par la même question, sur $x_3$. Comment faire pour que ces arbres n'apprennent pas tous la même chose ? [ajout]
   Histoire : « Comment faire pour que ces arbres n'apprennent pas tous la même chose » — À chaque coupure, on ne laisse candidats que quelques prédicteurs tirés au hasard, par exemple 2 des 5 : trois fois sur cinq, le prédicteur le plus fort n'est pas candidat, et les arbres cessent de se ressembler. [ajout]

7. dss/importance-des-variables
   La forêt prédit mieux qu'un arbre, mais on ne sait plus quelles variables comptent. [slide 104]
   Suite : Cinq cents arbres ne se lisent pas comme une régression. Quelles variables comptent dans la perte qu'ils prédisent ? [ajout]
   Histoire : « Quelles variables comptent dans la perte qu'ils prédisent » — On attribue à chaque prédicteur une part du travail de la forêt. On espère que l'endettement et le revenu en reçoivent l'essentiel, et les trois variables sans lien presque rien ; sur les 20 clients, les deux mesures qui suivent diront si c'est le cas. [ajout]

8. dss/importance-par-impurete
   Deux mesures répondent. [slide 104, slide 105]
   Suite : Première mesure : additionner ce que chaque coupure sur une variable a fait gagner. Que donne-t-elle ? [ajout]
   Histoire : « additionner ce que chaque coupure sur une variable a fait gagner » — Chaque arbre coupe les clients en deux groupes selon un seuil sur un prédicteur, et chaque coupure rend les groupes plus homogènes : elle fait baisser leur impureté, ici la somme des carrés des erreurs. Première mesure : additionner, pour chaque prédicteur, la baisse obtenue à chaque coupure faite sur lui, sur les 500 arbres. Sur les 20 clients, l'endettement en reçoit environ 21 % et le revenu 16 % ; les trois variables sans lien, plus de 60 % à elles trois, et la plus liée à la perte par hasard, 27 %, davantage que l'endettement. Des arbres poussés jusqu'au bout coupent aussi sur le bruit, et chaque coupure compte. [ajout]

9. dss/importance-par-permutation
   L'impureté compte aussi les coupures faites sur le bruit. [slide 106]
   Suite : Seconde mesure : que perd la forêt quand on brouille une variable ? [ajout]
   Histoire : « que perd la forêt quand on brouille une variable » — Seconde mesure : mélanger au hasard la colonne d'un prédicteur entre les clients, et regarder de combien l'erreur hors du sac se dégrade. Une variable qui a servi à couper sans rien apprendre ne coûte presque rien quand on la brouille : c'est le cas de deux des trois variables sans lien. Sur les 20 clients, arbre par arbre comme le fait le cours, brouiller l'endettement fait monter l'erreur de 0,31 ; brouiller la variable liée par hasard, autant ; les deux autres, de 0,09 et de rien ; le revenu, dont l'effet est réel mais plus faible, de rien non plus. La permutation classe mieux que l'impureté, mais, comme la régression, elle ne peut pas distinguer une coïncidence d'un lien sur si peu de clients. [ajout]

10. dss/boosting
    Une tout autre façon d'assembler des arbres : non plus en parallèle, mais les uns après les autres. [slide 122]
    Suite : Et si, au lieu de construire les arbres indépendamment, chacun corrigeait ce que les précédents ont manqué ? [ajout]
    Histoire : « chacun corrigeait ce que les précédents ont manqué » — Le premier petit arbre, à une seule coupure, est ajusté sur les pertes des 20 clients, et l'on n'en ajoute qu'une fraction $\lambda$, un centième ; ce qu'il laisse, le résidu de chaque client, devient la cible de l'arbre suivant, et ainsi de suite. Chaque arbre corrige ce que les précédents ont manqué, un centième à la fois : pour une perte moyenne de 3,60, la prédiction moyenne ne vaut que 0,34 après 10 arbres, 2,28 après 100, et n'atteint 3,60 qu'après 1 000. [ajout]

## Point d'arrivée
Un arbre seul est instable ; beaucoup d'arbres, rendus différents par le rééchantillonnage, le hasard des coupures ou la correction successive des erreurs, prédisent bien, au prix d'une lecture moins directe. [ajout]

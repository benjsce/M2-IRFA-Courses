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
   D'où viennent ces erreurs moyennes : que fait, au juste, une régression sur les 20 clients ? [slide 25]
   Histoire : « une régression sur les deux premiers » — La régression cherche les coefficients qui rendent la plus petite possible la somme des carrés des erreurs sur les 20 clients, notée RSS. Sur l'endettement $x_1$ et le revenu $x_2$, elle prédit la perte par $\hat y=3{,}30+0{,}076\,x_1-0{,}060\,x_2$, pour une RSS de 22,43 : divisée par les 20 clients, c'est l'erreur moyenne de 1,12 du point de départ. Sur les cinq prédicteurs, la RSS descend à 19,59, l'erreur moyenne de 0,98. [ajout]

2. dss/selection-de-variables
   Chaque prédicteur ajouté fait baisser l'erreur sur les 20 clients. Pourquoi alors vouloir en garder moins ? [slide 28]
   Histoire : « Lesquels garder » — Pour deux raisons. La précision d'abord : le modèle à cinq prédicteurs se trompe davantage sur les clients nouveaux, parce que 20 clients, ce n'est pas beaucoup plus que ses six coefficients à estimer. La lecture ensuite : sur l'endettement et le revenu seuls, le modèle dit que la perte monte avec le premier et baisse avec le second ; trois coefficients de plus, sans objet, brouillent cette lecture. [ajout]

3. dss/selection-de-sous-ensemble
   La façon la plus directe d'en avoir moins : en retirer. [slide 28]
   Histoire : « cinq prédicteurs » — Garder l'endettement et le revenu et écarter les trois autres revient à donner aux trois un coefficient nul, et aux deux premiers leurs coefficients de moindres carrés calculés sur eux seuls, 0,076 et −0,060. Chaque partie des cinq prédicteurs donne ainsi un modèle ; il reste à savoir laquelle garder. [ajout]

4. dss/erreur-de-test
   Pour choisir quelle partie garder, il faut juger chaque modèle. L'erreur sur les clients qui ont servi à l'ajuster est trompeuse : laquelle regarder ? [slide 37]
   Histoire : « sur 20 000 clients nouveaux, elle se trompe davantage » — L'erreur qui compte, l'erreur de test, est celle sur des clients que le modèle n'a pas vus : 1,16 pour le modèle à deux prédicteurs, 1,83 pour le modèle à cinq, quand leurs erreurs d'apprentissage, sur les 20 clients qui ont servi à les ajuster, disaient l'inverse. [ajout]

5. dss/surapprentissage
   Pourquoi le modèle à cinq prédicteurs, meilleur sur les 20 clients, est-il pire sur les nouveaux ? [slide 27]
   Histoire : « trois variables sans aucun lien avec la perte » — Il a appris le bruit de ces 20 clients-là. Les trois variables sans lien y reçoivent des coefficients de 0,37, −0,25 et −0,38, alors que leur effet sur la perte est nul : le modèle a pris pour une règle des coïncidences propres à l'échantillon, qu'aucun client nouveau ne reproduit. Plus le modèle a de prédicteurs, plus il trouve de ces coïncidences à ajuster. [ajout]

6. dss/critere-penalise
   On ne dispose pas toujours de données fraîches. Peut-on estimer l'erreur de test à partir de l'erreur d'apprentissage seule ? [slide 39]
   Histoire : « quand on ne dispose pas des clients nouveaux » — On corrige l'erreur d'apprentissage par une pénalité qui grandit avec le nombre de prédicteurs, parce que chaque prédicteur ajouté la fait baisser, même quand il n'apporte rien. Passer de deux à cinq prédicteurs la fait baisser de 1,12 à 0,98, soit de 0,14 : si les trois prédicteurs ajoutés coûtent davantage en pénalité, le petit modèle l'emporte. Les critères qui suivent fixent ce coût. [ajout]

7. dss/cp-de-mallows
   Quel prix faire payer à chaque prédicteur ? Pour les moindres carrés, un premier critère le fixe à partir de la variance du bruit. [slide 41]
   Histoire : « Lesquels garder » — Le $C_p$ ajoute à la RSS une pénalité $2d\hat\sigma^2$ et divise le tout par le nombre $n$ de clients ; $d$ est le nombre de prédicteurs, $\hat\sigma^2$ la variance du bruit, estimée sur le modèle complet, à cinq prédicteurs : sa RSS vaut 19,59, soit 20 fois son erreur moyenne de 0,98, et divisée par les 20 clients moins ses six coefficients, constante comprise, elle donne $\hat\sigma^2\approx1{,}40$. Pour le modèle à deux prédicteurs, $C_p=(22{,}43+2\times2\times1{,}40)/20=1{,}40$ ; pour le modèle complet, $(19{,}59+2\times5\times1{,}40)/20=1{,}68$. La pénalité a monté de 0,42, bien plus que les 0,14 d'erreur gagnés : le $C_p$ garde l'endettement et le revenu. [ajout]

8. dss/aic
   Le $C_p$ repose sur la somme des carrés des erreurs, propre aux moindres carrés. Existe-t-il un prix qui vaille pour tout modèle ajusté, régression ou non ? [slide 42]
   Histoire : « avec une erreur moyenne de 0,98 contre 1,12 » — L'AIC vaut $-2\log L+2d$, où $L$ est la vraisemblance, la probabilité que le modèle ajusté donne aux données observées. Pour une régression à erreurs gaussiennes, $-2\log L$ vaut, à une constante près, $n\log(\mathrm{RSS}/n)$, $n$ fois le logarithme de cette erreur moyenne ; on y ajoute deux points par prédicteur : $20\log(22{,}43/20)+2\times2\approx6{,}29$ pour le modèle à deux prédicteurs, $20\log(19{,}59/20)+2\times5\approx9{,}59$ pour le modèle complet. Même choix. [ajout]

9. dss/bic
   Le $C_p$ et l'AIC font payer chaque prédicteur au même prix, quel que soit le nombre de clients. Quand les clients sont nombreux, ce prix suffit-il ? [slide 43]
   Histoire : « Les 20 clients de la banque » — Le BIC reprend le $C_p$ en remplaçant le facteur 2 de la pénalité par $\log n$. Avec 20 clients, $\log20\approx3{,}0$ : la pénalité par prédicteur vaut une fois et demie celle du $C_p$. Il donne $(22{,}43+3{,}0\times2\times1{,}40)/20\approx1{,}54$ contre $(19{,}59+3{,}0\times5\times1{,}40)/20\approx2{,}03$, et garde lui aussi les deux bons prédicteurs. [ajout]

10. dss/r2-ajuste
    Et le $R^2$, la mesure d'ajustement qu'on lit d'habitude, peut-il départager les deux modèles ? [slide 44]
    Histoire : « ajuste mieux les 20 clients » — Le $R^2$ vaut $1-\mathrm{RSS}/\mathrm{TSS}$, où TSS est l'erreur qu'on ferait en prédisant toujours la perte moyenne : c'est la part de la dispersion de la perte que le modèle explique. Il monte de 0,49 à 0,55 quand on passe à cinq prédicteurs, parce qu'il ne regarde que l'ajustement. Le $R^2$ ajusté divise la RSS par $n-d-1$ et la TSS par $n-1$, ce qui fait payer chaque prédicteur : il descend de 0,43 à 0,40. [ajout]

11. dss/validation-croisee
    Ces quatre critères corrigent l'erreur d'apprentissage par une formule, et le $C_p$ comme le BIC supposent connue la variance du bruit. Peut-on estimer l'erreur de test sans formule ? [slide 45]
    Histoire : « quand on ne dispose pas des clients nouveaux » — On en fabrique : les 20 clients coupés en 5 blocs de 4, chaque modèle ajusté sur 16 et testé sur les 4 autres, cinq fois. L'erreur moyenne vaut 1,66 pour le modèle à deux prédicteurs, 2,22 pour le modèle complet : même verdict, sans aucune formule. [ajout]

12. dss/meilleur-sous-ensemble
    Jusqu'ici, on n'a comparé que deux modèles. Mais il y a bien d'autres parties des cinq prédicteurs : faut-il les essayer toutes ? [slide 29]
    Histoire : « Lesquels garder » — Avec cinq prédicteurs, chacun gardé ou écarté, il y a $2^5=32$ sous-ensembles à ajuster. On retient le meilleur de chaque taille : à un prédicteur, c'est par hasard une variable sans lien avec la perte ; à deux, le bon, l'endettement et le revenu. Entre ces meilleurs, le $C_p$ tranche pour celui à deux prédicteurs. [ajout]

13. dss/selection-pas-a-pas
    Essayer toutes les parties se fait avec cinq prédicteurs. Le peut-on encore avec des dizaines ? [slide 32]
    Suite : Si la banque décrivait ses clients par 40 variables, il faudrait ajuster $2^{40}$ modèles, plus de mille milliards. Peut-on n'en visiter qu'une petite fraction ? [ajout]
    Histoire : « Peut-on n'en visiter qu'une petite fraction » — Oui : on ajoute ou l'on retire un prédicteur à la fois, en gardant à chaque pas le meilleur mouvement. Avec les cinq prédicteurs des 20 clients, chaque sens ajuste le modèle de départ puis, à chaque pas, un modèle par prédicteur encore candidat : $1+5+4+3+2+1=16$ modèles au lieu de 32. [ajout]

14. dss/selection-ascendante
    On peut partir de rien et avancer. [slide 34]
    Histoire : « trois variables sans aucun lien avec la perte » — Partie de rien, la sélection ascendante fait entrer d'abord une de ces variables, la meilleure seule par hasard, puis une seconde, puis le revenu, et n'atteint l'endettement qu'au quatrième pas. Le $C_p$ retient alors un modèle à quatre prédicteurs dont deux inutiles, d'erreur de test 1,77 contre 1,16. [ajout]

15. dss/selection-descendante
    Ou partir de tout et reculer. [slide 35]
    Histoire : « l'endettement, le revenu » — Partie des cinq, la sélection descendante retire tour à tour les trois variables sans lien et retombe sur l'endettement et le revenu, que le $C_p$ retient : là où l'ascendante s'est trompée, elle trouve le bon modèle. [ajout]

## Point d'arrivée
Pour choisir des variables, on estime l'erreur de test, par une pénalité ou par validation croisée, et l'on parcourt les sous-ensembles, tous ou pas à pas. [ajout]

Sur les 20 clients, le $C_p$, l'AIC, le BIC, le $R^2$ ajusté et la validation croisée désignent tous le modèle à l'endettement et au revenu ; la sélection descendante le retrouve, la sélection ascendante, piégée par une variable de bruit, le manque. [ajout]

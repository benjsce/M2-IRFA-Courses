---
id: dup/parcours-valeur
ordre: 4
titre: Affaiblir l'indépendance sans toucher aux probabilités
source: L1 slides 55–57, L3 slides 3–17
---

## Point de départ
Beaucoup préfèrent 1 M sûr à $(5\text{M},{,}10;1\text{M},{,}89;0,{,}01)$, et pourtant $(5\text{M},{,}10;0,{,}90)$ à $(1\text{M},{,}11;0,{,}89)$. [L1 slide 42]

Ces violations d'Allais demandent d'affaiblir l'axiome d'indépendance. Une première famille de modèles le fait en gardant les probabilités telles quelles, et en rendant la valeur d'un résultat dépendante de la loterie où il se trouve. [L1 slide 55, L3 slide 3]

## À savoir avant
- dup/utilite-esperee : c'est le cas particulier que chaque modèle du parcours retrouve quand on remet l'indépendance entière. [L3 slide 13]
- dup/equivalent-certain : il sert de seuil dans les modèles de déception, et de critère dans le dernier modèle, qui compare plusieurs équivalents certains. [L3 slide 9, L3 slide 16]
- dup/effet-certitude : c'est la violation que le dernier modèle du parcours est construit pour expliquer. [L3 slide 15]

## Étapes
1. dup/eu-locale
   La façon la plus générale d'affaiblir l'axiome : ne garder de l'utilité espérée que son comportement pour de petits changements de probabilité. [L3 slide 13]
   Histoire : « Ces violations d'Allais demandent d'affaiblir l'axiome d'indépendance » — La façon la plus prudente de l'affaiblir : garder l'utilité espérée pour les petits changements de probabilité seulement. L'agent se comporte alors, autour de chaque billet, comme sous l'utilité espérée, mais avec une utilité locale $\Upsilon(x;P)$ qui peut changer d'un billet à l'autre, assez pour choisir différemment dans les deux paires. [ajout]

2. dup/famille-chew-dekel
   Entre ce cas très général et l'utilité espérée, le cours isole une famille qui garde une propriété intuitive des mélanges. [L3 slide 3]
   Histoire : « en rendant la valeur d'un résultat dépendante de la loterie où il se trouve » — Cette famille le fait en gardant une propriété intuitive : un mélange de deux loteries se situe toujours entre elles dans l'ordre de l'agent. Chaque résultat y reçoit une valeur $\Gamma(x,V(P))$ qui dépend de la valeur de la loterie entière. [ajout]

3. dup/utilite-ponderee
   Premier membre, le plus proche de l'utilité espérée : jusqu'où peut-on affaiblir l'axiome en gardant une formule simple ? [L3 slide 5]
   Histoire : « en gardant les probabilités telles quelles » — Les probabilités restent celles de l'énoncé ; c'est chaque résultat qui reçoit un poids $w(x)$, et ce poids déforme la part avec laquelle il compte. Un poids plus fort sur le rien fait compter le 1 % de risque du billet plus que 1 %. [ajout]

4. dup/utilite-implicite
   On affaiblit encore d'un cran si ce poids peut dépendre de la loterie avec laquelle on mélange. [L3 slide 7]
   Histoire : « dépendante de la loterie où il se trouve » — Un cran plus loin, le poids d'un résultat dépend aussi de la valeur de la loterie qui le contient, $w(x,V(P))$ : le rien du billet peut peser plus lourd à côté d'un million presque sûr qu'à côté de 5 millions improbables. [ajout]

5. dup/aversion-a-la-deception
   Un modèle de la famille reçoit une interprétation psychologique précise : ce qui fait mal, c'est de tomber sous ce qu'on attendait de la loterie. [L3 slide 9]
   Suite : Le cours reprend le paradoxe avec des montants plus petits : 2 400 sûrs, ou 2 500 avec 33 % de chances, 2 400 avec 66 % et rien avec 1 % ; puis 2 500 avec 33 % de chances, ou 2 400 avec 34 %. Un agent qui souffre de tomber sous ce qu'il attendait de la loterie fait-il les choix observés ? [L3 slide 11]
   Histoire : « Un agent qui souffre de tomber sous ce qu'il attendait » — Dans ce modèle, la valeur d'un billet est une moyenne où chaque résultat qui tombe sous cette valeur même compte $1+\alpha$ fois. Avec $u(x)=x$ et $\alpha=1$, seul le rien déçoit et il compte double : le billet vaut $(0{,}33\times2500+0{,}66\times2400)/(0{,}33+0{,}66+2\times0{,}01)\approx2385$, moins que les 2 400 sûrs, et l'agent prend les 2 400. Dans la seconde paire, de même, $0{,}33\times2500/(0{,}33+2\times0{,}67)\approx494$ pour les 2 500 et $0{,}34\times2400/(0{,}34+2\times0{,}66)\approx492$ pour les 2 400 : il prend les 2 500. C'est exactement le motif observé. [L3 slide 11]

6. dup/aversion-a-la-deception-generalisee
   Faut-il que la déception commence exactement à l'équivalent certain ? Le cours desserre ce seuil. [L3 slide 12]
   Histoire : « tomber sous ce qu'il attendait » — Dans le modèle précédent, la déception commence dès qu'on tombe sous l'équivalent certain du billet, les 2 385 du premier billet de l'exemple. Le modèle généralisé ne la fait commencer que sous une fraction $\delta$ de cet équivalent : tomber juste un peu en dessous ne déçoit pas encore, et $\delta=1$ redonne le modèle précédent. [ajout]

7. dup/eu-prudente
   Une dernière voie, hors de la famille, part de l'effet de certitude : l'agent hésite entre plusieurs fonctions d'utilité et se montre prudent. [L3 slide 15, L3 slide 16]
   Histoire : « Beaucoup préfèrent 1 M sûr » — Le modèle part de là : l'agent hésite entre plusieurs fonctions d'utilité et retient, pour chaque billet, le plus bas des équivalents certains. Le million sûr vaut 1 million sous toutes ; le billet risqué est jugé par la plus prudente d'entre elles, et le sûr l'emporte. [ajout]

## Point d'arrivée
Tous ces modèles gardent les probabilités objectives et changent ce qu'un résultat vaut. L'autre grande famille fait l'inverse, et c'est elle qui domine la suite du cours. [L1 slide 55]

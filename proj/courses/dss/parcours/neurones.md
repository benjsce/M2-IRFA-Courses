---
id: dss/parcours-neurones
ordre: 5
titre: Du neurone au réseau qui apprend
source: slides 128–163
---

## Point de départ
Quatre points suffisent à mettre en défaut une frontière linéaire : $(0,0)$ et $(1,1)$ dans une classe, $(0,1)$ et $(1,0)$ dans l'autre, le « ou exclusif ». Aucune droite ne les sépare. [slide 149]

Le bloc sur les réseaux de neurones part d'un neurone unique et montre comment en assembler plusieurs pour dépasser cette limite. [slide 148]

## À savoir avant
- dss/apprentissage-supervise : c'est le cadre de tout le bloc ; un réseau apprend à partir d'exemples dont on connaît la réponse. [slide 130, slide 133]

## Étapes
1. dss/reseau-de-neurones-artificiel
   D'où vient l'idée : calculer avec beaucoup d'unités simples reliées entre elles, comme un cerveau. [slide 129]

2. dss/apprentissage-inductif
   Qu'est-ce qu'un tel réseau cherche, au juste, quand on lui montre des exemples ? [slide 133]

3. dss/fonction-discriminante-lineaire
   La forme d'hypothèse la plus simple, pour deux classes : une frontière droite. [slide 134]

4. dss/perceptron
   Le premier neurone artificiel réalise exactement cette frontière. [slide 138, slide 139]

5. dss/regle-delta
   Comment ajuste-t-il ses poids à partir de ses erreurs ? [slide 144]

6. dss/limite-du-perceptron
   Cette règle ne sauve pas tout : il existe des classes qu'aucune frontière droite ne sépare. [slide 148]

7. dss/fonction-d-activation
   Pour aller plus loin, la sortie de chaque unité doit pouvoir être autre chose qu'un simple seuil. [slide 151]

8. dss/reseau-multicouche
   Avec ces unités, on peut empiler une couche intermédiaire, et la limite tombe. [slide 141, slide 151]

9. dss/apprentissage-profond
   Empiler davantage de couches donne l'apprentissage profond qu'annonçait l'introduction. [slide 8]

10. dss/descente-de-gradient
    Comment entraîner un réseau dont la sortie dépend des poids de plusieurs couches ? D'abord, un principe général de minimisation. [slide 160]

11. dss/retropropagation
    Ce principe demande de savoir quelle part de l'erreur revient à chaque poids caché. [slide 153, slide 154]

12. dss/descente-avec-inertie
    L'entraînement peut osciller ou ralentir ; une correction simple l'accélère. [slide 161]

13. dss/apprentissage-en-ligne-ou-par-lot
    Reste à décider quand appliquer les corrections : après chaque exemple, ou après les avoir tous vus. [slide 163]

## Point d'arrivée
Un seul neurone trace une frontière droite ; plusieurs couches d'unités non linéaires tracent n'importe quelle frontière, et la rétropropagation sait les entraîner. [ajout]

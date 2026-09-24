---
id: dss/parcours-entrainement
ordre: 6
titre: Entraîner un réseau qui généralise
source: slides 164–202
---

## Point de départ
Un réseau assez grand peut apprendre par cœur ses exemples d'entraînement. Ce qu'on veut, c'est qu'il réponde juste sur des cas qu'il n'a jamais vus. [slide 165]

## À savoir avant
- dss/reseau-multicouche : c'est le modèle qu'on entraîne dans tout le parcours, et dont on doit choisir la taille. [slide 165, slide 176]
- dss/retropropagation : c'est la procédure d'entraînement que le parcours apprend à arrêter, à régulariser et à organiser. [slide 174, slide 180]
- dss/erreur-de-test : c'est ce que la généralisation désigne, pour un réseau : l'erreur sur des cas non vus. [slide 165]
- dss/surapprentissage : c'est le danger que l'arrêt précoce et la décroissance des poids combattent. [slide 173]
- dss/regularisation : c'est l'idée que la décroissance des poids reprend du bloc sur la régression. [slide 174]
- dss/validation-croisee : c'est ce qui organise les jeux de données d'un entraînement fiable. [slide 181]
- dss/reseau-de-neurones-artificiel : ce sont ses entrées qu'il faut préparer, puisqu'un réseau ne lit que des nombres. [slide 187]
- dss/interpretabilite : c'est ce que l'analyse d'un réseau entraîné cherche à retrouver. [slide 194]

## Étapes
1. dss/generalisation
   Le but de l'entraînement, dit en une question : le réseau répond-il juste hors de ses exemples ? [slide 165]

2. dss/garantie-pac
   Combien d'exemples faut-il pour espérer une bonne réponse, compte tenu de la taille du réseau ? [slide 168]

3. dss/architecture-du-reseau
   Cette borne pèse sur un choix qu'on fait avant d'entraîner : la forme du réseau. [slide 176]

4. dss/arret-precoce
   Pendant l'entraînement, à quel moment s'arrêter ? [slide 173]

5. dss/decroissance-des-poids
   Plutôt que d'arrêter, on peut aussi empêcher les poids inutiles de grossir. [slide 174]

6. dss/protocole-d-entrainement
   Ces réglages se décident sur quelles données, et comment savoir qu'on ne s'est pas trompé en les choisissant ? [slide 180]

7. dss/preparation-des-donnees
   Avant tout cela, les données doivent être mises en état d'être apprises. [slide 187]

8. dss/type-de-donnee
   Tous les attributs ne se traitent pas de la même façon : cela dépend de leur nature. [slide 188]

9. dss/codage-des-variables
   Il faut ensuite les traduire en nombres, et la traduction n'est pas neutre. [slide 191]

10. dss/analyse-post-entrainement
    Le travail fini, reste une boîte de poids. Peut-on encore comprendre ce qu'elle a retenu ? [slide 194]

## Point d'arrivée
Un réseau utile est un réseau qui généralise : cela se décide dans sa taille, dans le moment où l'on arrête l'entraînement, dans la façon de préparer les données, et se vérifie sur des données réservées. [ajout]

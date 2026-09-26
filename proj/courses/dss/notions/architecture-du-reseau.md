---
id: dss/architecture-du-reseau
nom: Architecture du réseau
type: notion
statut: source
construite_a_partir_de:
- dss/garantie-pac
alias:
- network design
- network architecture
refs:
- slide 166
- slide 169
- slide 170
- slide 176
- slide 177
---

## Ce que c'est
Le choix du nombre de couches, du nombre de nœuds par couche et des connexions entre eux. [slide 176]

## Ce qui la définit
Ce choix fixe le nombre de poids du réseau, et c'est par là qu'il commande la généralisation. [slide 176]

La borne $m>W/\varepsilon$ se lit ici dans l'autre sens. **Connu** : les exemples dont on dispose, $m$, et la tolérance visée, $\varepsilon$. **Cherché** : le nombre de poids qu'on peut se permettre, moins de $\varepsilon\,m$, et donc le nombre de nœuds cachés. [slide 170, ajout]

Le cours en fait un compromis : trop de poids exige trop d'exemples, trop peu ne laisse pas la liberté de construire la fonction voulue ; entre les deux, un nombre optimal de poids, donc de nœuds cachés. [slide 170]

La connectivité est un second levier : restreindre l'espace des hypothèses par une connectivité sélective, des poids partagés ou des connexions récursives. Le cours mentionne aussi des méthodes automatiques dans les deux sens, l'augmentation par corrélation en cascade et l'élagage des poids. [slide 176, slide 177]

## Le chemin jusqu'ici
Le critère vient de dss/garantie-pac : il faut plus de $W/\varepsilon$ exemples pour $W$ poids. Sans cette borne, le nombre de nœuds cachés resterait une question de goût ; avec elle, il se compare aux exemples disponibles. [ajout]

La borne elle-même chiffre dss/generalisation, la capacité à répondre juste hors des exemples, qui se juge sur dss/erreur-de-test. [ajout]

L'objet à dimensionner est un dss/reseau-multicouche : la dss/limite-du-perceptron impose sa couche cachée, et la dss/fonction-d-activation de chaque nœud la rend entraînable. Ses nœuds reprennent le dss/perceptron, l'unité d'un dss/reseau-de-neurones-artificiel qui calcule une dss/fonction-discriminante-lineaire. [ajout]

Les exemples qu'on compte sont ceux de dss/apprentissage-inductif, munis de leur réponse attendue comme le veut dss/apprentissage-supervise. [ajout]

## Exemple minimal
Un réseau 20-20-1 compte 441 poids : 400 connexions de l'entrée vers la couche cachée, 20 de la couche cachée vers la sortie, et 21 seuils, un par nœud caché et un pour la sortie. [slide 166, slide 169, ajout]

## Geste de calcul type
Partir des exemples, pas du réseau : $\varepsilon\,m$ donne le plafond de poids, puis on compte les poids du réseau envisagé. La banque a 20 clients et tolère 10 % d'erreur : elle peut se permettre moins de $0{,}1\times20=2$ poids, alors qu'un seul neurone branché sur ses cinq prédicteurs en compte déjà 6, cinq entrées et un seuil. [ajout]

## Cesse d'être valide quand
La borne fixe le nombre de poids, donc de nœuds cachés ; elle ne dit rien du nombre de couches, pour lequel le cours ne donne que des méthodes automatiques et un compromis à trouver. [slide 176]

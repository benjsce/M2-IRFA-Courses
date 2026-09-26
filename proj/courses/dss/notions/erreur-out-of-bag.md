---
id: dss/erreur-out-of-bag
nom: Erreur out-of-bag
type: notion
statut: source
construite_a_partir_de:
- dss/bagging
- dss/validation-croisee
alias:
- out-of-bag error
- OOB
refs:
- slide 102
---

## Ce que c'est
L'erreur estimée sur les observations absentes de chaque échantillon bootstrap, sans jeu de validation séparé. [slide 102]

## Ce qui la définit
Le tirage avec remise laisse en moyenne un tiers des observations de côté à chaque fois : ce sont les observations out-of-bag de cet arbre. [slide 102]

On prédit alors chaque observation avec les seuls arbres pour lesquels elle était absente, et l'on agrège sur toutes les observations. On obtient une erreur quadratique ou un taux de mauvais classement. [slide 102]

Le gain est de protocole : l'estimation vient gratuitement avec l'ajustement, il n'y a pas de découpage à organiser. [slide 102]

![Six échantillons bootstrap parmi dix observations, tirés pour le dessin. Chaque case compte les tirages d'une observation pour un arbre, et un point marque une observation hors du sac. La colonne encadrée se lit comme la fiche le demande : cette observation est prédite par les seuls arbres dont elle était absente.](figures/erreur-out-of-bag.svg) [ajout]

## Le chemin jusqu'ici
Deux fils. dss/bootstrap, dss/apprentissage-supervise, dss/erreur-de-test et dss/compromis-biais-variance mènent à dss/bagging ; dss/validation-croisee donne l'idée à laquelle on la compare. [ajout]

Le tirage avec remise laisse un tiers des observations de côté à chaque fois : l'estimation hors échantillon est déjà là, il suffit de la lire. C'est une validation croisée qui ne coûte rien de plus que l'ajustement. [ajout]

## Exemple minimal
Avec $B=500$ arbres, chaque observation est prédite par environ 185 arbres pour lesquels elle était hors du sac. [ajout]

## Geste de calcul type
Suivre l'erreur out-of-bag au fil des arbres et arrêter l'entraînement quand elle se stabilise. [slide 116]

## Cesse d'être valide quand
Elle est propre aux méthodes par bootstrap : le boosting, qui n'en fait pas, n'y a pas droit et doit passer par la validation croisée. [slide 123, slide 126]

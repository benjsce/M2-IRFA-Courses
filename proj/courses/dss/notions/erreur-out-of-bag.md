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
On cherche une erreur sur des données non vues sans en mettre de côté. Chaque arbre en a déjà : le tirage avec remise laisse en moyenne un tiers des observations hors de son échantillon, ce sont ses observations out-of-bag. [slide 102]

On prédit alors chaque observation avec les seuls arbres pour lesquels elle était absente, et l'on agrège sur toutes les observations. On obtient une erreur quadratique ou un taux de mauvais classement. [slide 102]

Le gain est de protocole : l'estimation vient gratuitement avec l'ajustement, il n'y a pas de découpage à organiser. [slide 102]

![Six échantillons bootstrap parmi dix observations, tirés pour le dessin. Chaque case compte les tirages d'une observation pour un arbre, et un point marque une observation hors du sac. La colonne encadrée se lit comme la fiche le demande : cette observation est prédite par les seuls arbres dont elle était absente.](figures/erreur-out-of-bag.svg) [ajout]

## Le chemin jusqu'ici
dss/bagging fournit les arbres : ajustés sur les couples observés de dss/apprentissage-supervise, chacun sur son échantillon de dss/bootstrap, puis moyennés pour réduire la variance, comme le veut dss/compromis-biais-variance. [ajout]

dss/validation-croisee fournit l'idée qu'on retrouve ici : estimer l'erreur que définit dss/erreur-de-test sur des observations qui n'ont pas servi à l'ajustement. [ajout]

## Exemple minimal
Sur les 20 clients, chaque tirage de 20 clients avec remise laisse un client donné de côté avec la probabilité $0{,}95^{20}\approx0{,}36$ : sur 500 arbres, ce client est prédit par les quelque 180 qui ne l'ont pas vu, un peu plus du tiers qu'annonce le cours. [slide 102, ajout]

## Geste de calcul type
Suivre l'erreur out-of-bag au fil des arbres et arrêter l'entraînement quand elle se stabilise. [slide 116]

## Cesse d'être valide quand
Elle est propre aux méthodes par bootstrap : le boosting, qui n'en fait pas, n'y a pas droit et doit passer par la validation croisée. [slide 123, slide 126]

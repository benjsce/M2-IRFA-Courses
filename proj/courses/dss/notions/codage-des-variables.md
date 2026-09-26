---
id: dss/codage-des-variables
nom: Codage des variables
type: notion
statut: source
construite_a_partir_de:
- dss/type-de-donnee
alias:
- transformation and encoding
refs:
- slide 191
- slide 192
- slide 193
---

## Ce que c'est
Traduire un attribut en entrées numériques du réseau, par un codage qui respecte le rapport entre ses valeurs. [slide 191]

## Ce qui la définit
Pour une valeur nominale ou ordinale, trois codages : un parmi $N$, où $N$ entrées représentent les $N$ valeurs et une seule vaut 1 ; le thermomètre, où les entrées s'allument jusqu'à la valeur ; ou une seule entrée réelle, si l'attribut est ordinal. [slide 191]

Le choix suit le rapport entre les valeurs. Célibataire, marié, divorcé n'ont pas d'ordre : un parmi $N$ n'en impose aucun. Jeune, adulte, senior sont rangés : le thermomètre ou la valeur réelle gardent ce rang. [slide 191, ajout]

Pour une valeur continue, le cours classe quatre codages de 1,6 : un seul réel, 0,16, est correct ; les bits d'un nombre binaire sont mauvais ; un parmi $N$ par intervalles n'est pas terrible, à cause des discontinuités ; des intervalles flous qui se recouvrent sont le meilleur. [slide 193]

Deux consignes complètent le codage. Les attributs continus se normalisent, en les divisant par leur norme, par leur somme, ou en les centrant puis en les divisant par leur variance ; la slide présente ces normalisations comme une façon de décorréler les attributs, et ajoute une mise à l'échelle linéaire pour une distribution uniforme, logarithmique ou en puissance pour une distribution asymétrique. Et les valeurs cibles doivent vivre entre 0,1 et 0,9, pas entre 0 et 1. [slide 191, slide 192, slide 193]

Diviser un attribut par un nombre ne change pourtant aucune corrélation : ces normalisations mettent les attributs à la même échelle, elles ne les décorrèlent pas. [ajout]

## Le chemin jusqu'ici
Le codage est la dernière étape de dss/preparation-des-donnees, celle de la transformation. Il dépend de dss/type-de-donnee : c'est la nature de l'attribut, nominale, ordinale ou continue, qui décide du codage. [ajout]

La contrainte vient du dss/reseau-de-neurones-artificiel, qui n'accepte que des nombres, typiquement entre 0 et 1. Et ce qu'on code, ce sont les entrées et les sorties désirées des exemples de dss/apprentissage-supervise, d'où la consigne propre aux cibles. [ajout]

## Exemple minimal
La valeur 4 se code (0 1 0 0 0) en un parmi $N$, (1 1 1 1 0) en thermomètre, ou 0,4 en valeur réelle. [slide 191]

![La valeur 4 sous les trois codages de l'exemple, une case par entrée du réseau, dans l'ordre de la slide : un parmi $N$ n'allume qu'une case, le thermomètre les allume jusqu'à la valeur, et la valeur réelle tient en une seule entrée remplie aux quatre dixièmes.](figures/codage-des-variables.svg) [ajout]

Les cases sont recopiées de la slide. En un parmi $N$, la seule règle est qu'une case et une seule vaut 1 ; 0,4 et 0,16 sont les valeurs ramenées entre 0 et 1, ici divisées par 10, une échelle que le cours ne précise pas. [slide 191, ajout]

## Geste de calcul type
Compter les entrées que coûte chaque codage, car chaque entrée ajoute un poids par nœud caché. La banque ajoute à ses cinq prédicteurs la situation familiale, en un parmi $N$, soit 3 entrées, et la tranche d'âge en thermomètre, 3 entrées aussi : 11 entrées au lieu de 5, et un réseau à 20 nœuds cachés passe de 141 à $20\times(11+1)+21=261$ poids. [ajout]

## Cesse d'être valide quand
Le cours donne un classement de qualité sans justification chiffrée : les intervalles flous sont dits meilleurs, sans mesure à l'appui. [ajout]

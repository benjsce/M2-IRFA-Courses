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
La mise en entrées numériques d'un attribut, et le choix de représentation que cela impose. [slide 191]

## Ce qui la définit
Pour une valeur nominale ou ordinale, trois codages : un parmi $N$, thermomètre, ou une valeur réelle si l'attribut est ordinal. Le choix doit tenir compte du rapport entre les valeurs — célibataire, marié, divorcé n'est pas jeune, adulte, senior. [slide 191]

Pour les valeurs continues, le cours classe explicitement quatre codages : un seul réel est correct, les bits d'un nombre binaire sont mauvais, un parmi $N$ par intervalles n'est pas terrible à cause des discontinuités, et des intervalles flous qui se recouvrent sont le meilleur. [slide 193]

La normalisation décorrèle les attributs : euclidienne, en pourcentage, ou par la variance. Une échelle linéaire convient à une distribution uniforme, une échelle non linéaire à une distribution asymétrique. [slide 192]

Une consigne revient deux fois : les valeurs cibles doivent vivre dans 0,1 – 0,9 et non dans 0,0 – 1,0. [slide 191, slide 193]


## Le chemin jusqu'ici
Quatre maillons en file : dss/apprentissage-supervise, dss/reseau-de-neurones-artificiel, dss/preparation-des-donnees, puis dss/type-de-donnee. [ajout]

Chaque maillon restreint le suivant. Le réseau impose du numérique continu, la préparation organise la transformation, le type décide laquelle appliquer. [ajout]

## Exemple minimal
La valeur 4 se code (0 1 0 0 0) en un parmi $N$, (1 1 1 1 0) en thermomètre, ou 0,4 si l'attribut est ordinal. [slide 191]

![La valeur 4 sous les trois codages de l'exemple, une case par entrée du réseau : un parmi $N$ n'allume qu'une case, le thermomètre les allume jusqu'à la valeur, et la valeur réelle tient en une seule entrée remplie aux quatre dixièmes.](figures/codage-des-variables.svg) [ajout]

## Geste de calcul type
Coder 1,6 comme un réel unique 0,16 plutôt que comme un binaire : la représentation binaire casse la continuité que le réseau exploite. [slide 193]

## Cesse d'être valide quand
Le cours donne un classement de qualité sans justification chiffrée : les intervalles flous sont dits meilleurs, sans mesure à l'appui. [ajout]

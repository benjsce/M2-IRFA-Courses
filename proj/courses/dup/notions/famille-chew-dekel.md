---
id: dup/famille-chew-dekel
nom: Préférences de Chew-Dekel
symbole: $\Gamma$
type: abstraite
statut: source
cas_de: dup/axiome-independance
parametre: la forme sous laquelle l’indépendance est affaiblie
construite_a_partir_de:
- dup/utilite-esperee
alias:
- Chew-Dekel
- betweenness
- intermédiarité
refs:
- L3 slide 3
- L3 slide 4
- L3 slide 17
---

## Ce que c'est
La famille des préférences qui conservent l’intermédiarité : un mélange se situe toujours entre ses composantes. [L3 slide 3]

## Forme
$$V(P)=\sum_i p_i\,\Gamma\big(x_i,V(P)\big)$$ [L3 slide 4]

## Ce que les symboles modélisent
$\Gamma$ prend deux arguments : un résultat, et la valeur de la loterie où ce résultat figure. Le second est tout l'écart avec l'utilité espérée — la contribution d'un gain y dépend de la loterie qui l'entoure, au lieu d'être fixée une fois pour toutes. [L3 slide 4]

## Ce que les membres partagent
L’axiome d’intermédiarité : mélanger deux loteries indifférentes ne crée ni valeur ni coût, et mélanger une meilleure et une moins bonne donne un intermédiaire. L’indépendance l’implique, la réciproque est fausse. [L3 slide 3]

La représentation est implicite : la contribution d’un résultat peut dépendre de la valeur globale de la loterie. À valeur fixée l’équation est linéaire en probabilités, donc les courbes d’indifférence restent des droites — mais elles cessent d’être parallèles. [L3 slide 4]

## Pourquoi ce niveau existe
Le cours présente ces modèles l’un après l’autre, et sa table du §17 les range explicitement ensemble ; ils ne diffèrent que par la façon dont la probabilité compensatrice est autorisée à varier. Les séparer ferait manquer la progression : $\rho=\lambda$, puis $\rho$ indépendant de $R$, puis $\rho(R)$. [L3 slide 17]

## Le chemin jusqu'ici
La famille se lit contre dup/utilite-esperee, elle-même construite sur dup/loterie et dup/fonction-utilite. [ajout]

La famille se définit par ce qu'elle **garde** de l'utilité espérée — l'intermédiarité — et par ce qu'elle abandonne, l'indépendance. On ne peut donc pas la poser avant elle : c'est un affaiblissement, et un affaiblissement se définit par rapport à ce qu'il affaiblit. [ajout]

## Exemple minimal
Sur les quatre loteries d’Allais, le membre « aversion à la déception » avec $u(x)=x$ et $\alpha=1$ donne 2 385,15, 2 400, 494,01 et 491,57. [L3 slide 11]

## Geste de calcul type
Poser $V$ inconnue, écrire $V=\sum_i p_i\Gamma(x_i,V)$, puis résoudre ce point fixe : c’est le geste commun à tous les membres de la famille. [L3 slide 4]

## Cesse d'être valide quand
L’intermédiarité interdit de désirer strictement le mélange de deux loteries indifférentes : un goût pour la randomisation sort de toute la famille. [L3 slide 6, L3 slide 18]

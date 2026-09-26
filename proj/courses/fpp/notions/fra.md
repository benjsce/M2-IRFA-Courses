---
id: fpp/fra
nom: Forward Rate Agreement
type: notion
statut: source
construite_a_partir_de:
- fpp/taux-zero-coupon
alias:
- FRA
- accord de taux futur
- contrat de taux à terme
refs:
- Déf. 7
---

## Ce que c'est
Un contrat signé en t qui échange en S des intérêts à un taux K fixé aujourd'hui contre des intérêts au taux qui sera observé en T, pour la période de T à S. [Déf. 7]

## Forme
$$\text{flux en }S\ :\quad \underbrace{e^{R(T,S)(S-T)}}_{\text{reçu, inconnu en }t}\;-\;\underbrace{e^{K(S-T)}}_{\text{payé, fixé en }t}$$ [Déf. 7]

## Ce que les symboles modélisent
$t$ est la date de signature, $T$ le début de la période couverte, $S$ sa fin. $K$ est le taux fixe écrit au contrat. $R(T,S)$ est le taux zéro-coupon de $T$ à $S$ tel qu'on l'observera en $T$ : aujourd'hui, personne ne le connaît. [Déf. 7]

## Ce qui la définit
Celui qui paie le fixe veut connaître dès aujourd'hui le taux d'un emprunt qu'il fera plus tard. Il reçoit en $S$ ce que rapporterait 1 placé de $T$ à $S$ au taux du moment et paie ce que rapporterait 1 placé au taux $K$ ; les capitaux se compensent, seuls les intérêts s'échangent. [Déf. 7, ajout]

Ce qui est **connu** à la signature : les trois dates et $K$. Ce qui reste **inconnu** : $R(T,S)$. Le contrat transforme un taux futur inconnu en un taux fixé aujourd'hui ; quel $K$ le rend gratuit, c'est la question du taux forward. [Déf. 7, §2.3]

![Les flux du FRA sur l'échéancier : le taux variable est fixé en T et inconnu aujourd'hui ; en S, on reçoit l'intérêt variable et on paie l'intérêt fixe, écrit dès la signature.](figures/fra.svg) [Déf. 7, ajout]

## Le chemin jusqu'ici
fpp/taux-zero-coupon définit $R(T,S)$, le même objet que $R(t,T)$ mais vu depuis une date future, et c'est cette date qui le rend inconnu. fpp/zero-coupon fournit l'unité empruntée de $T$ à $S$, et fpp/capitalisation la convention continue dans laquelle intérêts fixes et variables s'écrivent. [ajout]

## Exemple minimal
Signé aujourd'hui pour la période qui va d'un an à deux ans, au taux fixe de 6 % : dans deux ans, on paie $e^{0,06}\approx1{,}0618$ par unité et on reçoit $e^{R(T,S)}$. [ajout]

## Geste de calcul type
Le jour du paiement, calculer l'écart des deux intérêts : si le taux observé dans un an est 7 %, on reçoit $e^{0,07}-e^{0,06}\approx0{,}0107$ par unité. [ajout]

## Cesse d'être valide quand
Le poly écrit le FRA en capitalisation continue ; pour des périodes courtes, le marché cite plutôt des taux linéaires, comme la courbe elle-même. Et le contrat suppose que la contrepartie paiera. [Déf. 6, ajout]

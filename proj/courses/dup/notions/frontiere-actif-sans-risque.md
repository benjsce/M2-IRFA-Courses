---
id: dup/frontiere-actif-sans-risque
nom: Actif sans risque et actif risqué
symbole: $a$
type: notion
statut: source
construite_a_partir_de:
- dup/moyenne-variance
alias:
- riskless and risky asset
refs:
- L1 slide 12
---

## Ce que c'est
Mélanger un actif sans risque et un actif risqué trace un segment de droite dans le plan écart type-moyenne. [L1 slide 12]

## Forme
$$\tilde r_p=ar_0+(1-a)\tilde r,\qquad \mu_p=ar_0+(1-a)\mu_r,\qquad \sigma_p=|1-a|\,\sigma_r$$ [L1 slide 12]

## Ce qui la définit
L’écart type est proportionnel à la part risquée : la frontière est une droite, et emprunter au taux $r_0$ la prolonge au-delà du portefeuille tout risqué. [L1 slide 12]

## Le chemin jusqu'ici
dup/loterie puis dup/moyenne-variance. [ajout]

dup/loterie et dup/moyenne-variance suffisent parce que tout se passe dans le plan écart type–moyenne : c'est de la géométrie, pas de la théorie de la décision. La fiche *Diversification* a le même socle, pour la même raison. Ajouter un actif sans risque y trace une droite, parce qu'un actif de variance nulle ne peut pas courber le mélange. [ajout]

## Exemple minimal
Avec $r_0=2\%$, $\mu_r=8\%$, $\sigma_r=20\%$ et $a=\tfrac12$ : $\mu_p=5\%$ et $\sigma_p=10\%$. [ajout]

## Geste de calcul type
Choisir la part risquée $1-a$, lire $\mu_p$ et $\sigma_p$ sur la droite : avec $r_0=2\,\%$, $\mu_r=8\,\%$ et $\sigma_r=20\,\%$, chaque point de $\sigma_p$ achète 0,3 point de $\mu_p$. [L1 slide 12]

## Cesse d'être valide quand
La linéarité de $\sigma_p$ tient parce qu’un des deux actifs a une variance nulle ; avec deux actifs risqués il faut la covariance. [L1 slide 13]

---
id: dup/aversion-relative
nom: Comparaison des aversions
type: notion
statut: source
construite_a_partir_de:
- dup/aversion-absolue-arrow-pratt
alias:
- relative risk attitude
- plus averse que
refs:
- L1 slide 30
---

## Ce que c'est
Un agent est plus averse qu’un autre s’il refuse toute loterie qui laisse l’autre indifférent, à toute richesse. [L1 slide 30]

## Forme
$$\forall X,w_0:\quad \mathbb{E}u_2(w_0+X)=u_2(w_0)\implies \mathbb{E}u_1(w_0+X)\le u_1(w_0)$$ [L1 slide 30]

## Ce qui la définit
La condition nécessaire et suffisante est l’existence d’une transformation concave : $u_1=\phi(u_2)$ avec $\phi$ concave. [L1 slide 30]

La démonstration tient en quatre lignes : définition de $\phi$, inégalité de Jensen, indifférence de $u_2$, définition de $\phi$ à nouveau. [L1 slide 30]

## Exemple minimal
$u_1(z)=-1/z$ est plus averse que $u_2(z)=\ln z$ : $A_1=2/z$ contre $A_2=1/z$. [ajout]

## Geste de calcul type
Ne pas comparer les $u$, ni les $u''$ : comparer les $A$. C’est la seule comparaison qui ait un contenu observable en termes de paris refusés. [L1 slide 33]

## Cesse d'être valide quand
L’ordre est partiel : deux agents dont les $A$ se croisent ne sont comparables à aucune richesse globale. [ajout]

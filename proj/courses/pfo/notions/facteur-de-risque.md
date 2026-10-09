---
id: pfo/facteur-de-risque
nom: Facteur de risque
type: abstraite
statut: source
cas_de: pfo/modele-factoriel
parametre: la façon de construire la série du facteur, à partir des rendements observés
construite_a_partir_de: []
alias:
- risk factor
- facteur commun
- common factor
- facteur
refs:
- §4.2.2
- §4.2.3
- p. 62
- §4.3.2
---

## Ce que c'est
Une série de rendements, construite à partir des actifs observés, dont les mouvements se retrouvent dans ceux de beaucoup d'actifs à la fois. [§4.2.2, p. 62]

## Ce que les membres partagent
Chacun est une série datée, une valeur par date, obtenue en combinant des rendements d'actifs ; un actif s'y expose par un coefficient que la régression estime. Le facteur ne dépend pas de l'actif qu'on étudie ; l'exposition, si. [p. 62, p. 65]

Ils diffèrent par la façon de les construire. Fama et French trient les entreprises selon une caractéristique — la capitalisation, le ratio book-to-market — et prennent le rendement d'un groupe moins celui de l'autre. L'analyse en composantes principales combine les rendements selon un vecteur propre de leur matrice de covariance, sans rien supposer de leur sens économique. [§4.2.2, §4.2.3, p. 62]

## Pourquoi ce niveau existe
Le cours oppose les facteurs « définis a priori par une théorie économique » à ceux qui sont « extraits directement des données », et les fait entrer dans la même régression. Les réunir montre que ce choix porte sur la construction de la série, et non sur ce qu'on en fait ensuite. [p. 62]

## Ce qui reste libre
| facteur | construction | choisi |
|---|---|---|
| marché, $R_{m,t}-R_{f,t}$ | portefeuille de marché moins taux sans risque | a priori |
| SMB | petites moins grandes capitalisations | a priori |
| HML | ratio book-to-market élevé moins faible | a priori |
| $PC_{k,t}$ | rendements combinés par le vecteur propre $V_k$ | extrait des données |
[§4.2.1, §4.2.2, §4.2.3]

## Cesse d'être valide quand
Un facteur peut être construit sans que son interprétation suive : une prime de taille positive ne prouve pas qu'elle rémunère le seul risque d'illiquidité, et une composante principale n'a pas d'interprétation économique garantie. [p. 59, p. 62]

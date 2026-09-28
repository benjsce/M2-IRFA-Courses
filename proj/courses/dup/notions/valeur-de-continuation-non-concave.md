---
id: dup/valeur-de-continuation-non-concave
nom: Valeur de continuation non concave
type: notion
statut: source
construite_a_partir_de:
- dup/euler-sans-engagement
alias:
- pathologies de la consommation
- violations of monotonicity and continuity
- non-concave V
refs:
- L5 slide 31
- L5 slide 32
- L5 slide 33
- L5 slide 34
- L5 slide 35
---

## Ce que c'est
Sans engagement, la valeur que le moi 1 attache à la richesse transmise peut ne pas être concave, et sa consommation sauter quand sa richesse varie un peu. [L5 slide 31]

## Ce qui la définit
Le moi 1 pèse la richesse transmise par $V'(w_2)=u'(c_2)\,c_2'+\tfrac1\beta\,u'(c_2)\,(1-c_2')$. Quand $w_2$ augmente, deux effets s'opposent. Le moi 2 consomme plus, $u'(c_2)$ baisse, et $V'$ avec lui. Mais si $c_2''<0$, la part consommée $c_2'$ baisse aussi, et la part épargnée, que le moi 1 pèse $1/\beta>1$ fois plus, augmente : $V'$ monte. [L5 slide 31]

Si le second effet l'emporte, $V$ n'est pas concave. La consommation $c_1(w_1)$ peut alors cesser d'être croissante et continue en la richesse. [L5 slide 31]

![D'après la slide 32 : la valeur βδRV(w₂), avec une bosse où elle n'est pas concave, et une droite de pente u′(c₁) qui la touche en deux points. Le moi 1 choisit w₂ là où la pente de la courbe égale u′(c₁). Quand la richesse du moi 1 franchit ce seuil, le point de contact saute de l'un à l'autre : la richesse transmise w₂ saute, et la consommation c₁ avec elle.](figures/valeur-de-continuation-non-concave.svg) [L5 slide 32, ajout]

Cela compte à double titre. Dès quatre périodes, un saut de la consommation en $T-2$ rend discontinue la valeur de la période $T-3$, et les équations d'Euler ne caractérisent plus les solutions. Surtout, avec des moyens d'engagement plus généraux, il peut n'exister aucune solution récursive. [L5 slide 33]

Les remèdes relèvent de deux familles : des conditions sur l'utilité, le risque et $\beta$ proche de 1 qui rendent la consommation continue, ou des approches qui acceptent le saut et lissent la valeur, comme l'équilibre de jeu ou la maîtrise de soi coûteuse. [L5 slide 34, L5 slide 35]

## Le chemin jusqu'ici
dup/euler-sans-engagement écrivait la condition du moi 1 en supposant $V$ dérivable et concave, ce que suppose aussi sa règle résolue à rebours par dup/sophistication, et ce que ne demandait pas dup/engagement-complet, où le moi 1 choisissait tout. C'est la décote $\beta$ de dup/actualisation-quasi-hyperbolique qui donne à la part épargnée son poids $1/\beta$ : sans dup/biais-pour-le-present, les deux effets ne s'opposeraient pas. [L5 slide 28, L5 slide 31]

Le reste du socle est la même chaîne que pour cette équation : dup/utilite-actualisee et dup/fonction-utilite pour les poids et les utilités, dup/actualisation-exponentielle prise en défaut par dup/inversion-des-preferences-dans-le-temps, puis dup/stationnarite, dup/invariance-temporelle et dup/coherence-dynamique pour dire pourquoi le moi 2 dévie. [L5 slide 22]

## Cesse d'être valide quand
Avec une utilité logarithmique et sans revenu, la règle du moi 2 est linéaire, $c_2''=0$, et $V$ reste concave. Des conditions de ce type sur l'utilité suffisent à trois périodes, mais des revenus et une contrainte d'emprunt peuvent rendre la consommation discontinue même sous CRRA. [L5 slide 34, ajout]

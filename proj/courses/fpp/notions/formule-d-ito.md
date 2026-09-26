---
id: fpp/formule-d-ito
nom: Formule d'Itô
type: notion
statut: source
construite_a_partir_de:
- fpp/modele-black-scholes
alias:
- Itô's lemma
- lemme d'Itô
- Ito formula
refs:
- §7.1
- éq. 15
- exo. 14
---

## Ce que c'est
La règle qui donne la variation d'une fonction du prix de l'action, avec un terme en dérivée seconde que le calcul différentiel ordinaire n'a pas. [§7.1]

## Forme
$$dC=\Big(\frac{\partial C}{\partial t}+\mu S\frac{\partial C}{\partial S}+\frac12\sigma^2S^2\frac{\partial^2C}{\partial S^2}\Big)dt+\frac{\partial C}{\partial S}\,\sigma S\,dW_t$$ [§7.1]

## Ce que les symboles modélisent
$C(t,S_t)$ est le prix de l'option, fonction de la date et du prix de l'action ; $S$ suit l'équation $dS_t=S_t(\mu\,dt+\sigma\,dW_t)$. Le premier terme est la dérive de $C$, le second son bruit. [§7.1, éq. 15]

## Ce qui la définit
Ce qui est **connu** : la dynamique de l'action. Ce qu'on **cherche** : celle de l'option, qui en est une fonction. Le calcul ordinaire donnerait la dérivée en $t$ et la pente en $S$ ; Itô ajoute $\tfrac12\sigma^2S^2\,\partial^2C/\partial S^2$, parce qu'un mouvement brownien bouge de l'ordre de $\sqrt{dt}$ et que son carré, de l'ordre de $dt$, ne se néglige pas. [§7.1, ajout]

Le livre d'exercices l'applique au prix forward $F_t=S_t\,e^{r(T-t)}$ : sous la probabilité risque-neutre, $dF_t=F_t\,\sigma\,dW_t$, sans dérive. [exo. 14]

![Le prix du call C(S) et sa tangente en S : pour un mouvement ±ΔS, la moyenne de C(S − ΔS) et C(S + ΔS) dépasse C(S) de ½ ∂²C/∂S² ΔS², l'écart que la tangente ne voit pas et que la formule d'Itô ajoute.](figures/formule-d-ito.svg) [ajout]

## Le chemin jusqu'ici
fpp/modele-black-scholes donne l'équation que suit l'action ; la formule d'Itô la propage à toute fonction de l'action. Le terme en $\sigma^2$ vient de ce que fpp/echelonnement-de-la-variance appliqué à fpp/volatilite fait croître la variance comme le temps. [ajout]

La tendance du modèle vient de fpp/tendance-risque-neutre et de fpp/probabilite-risque-neutre, qui la fixent sur fpp/prix-forward net du fpp/taux-de-dividende et des fpp/dividendes-intermediaires ; fpp/transformee-de-laplace-gaussienne en corrigeait la moyenne. En amont, fpp/cash-and-carry sous fpp/absence-d-arbitrage, l'actualisation de fpp/valeur-actuelle-nette et de fpp/zero-coupon, la convention de fpp/capitalisation. [ajout]

## Exemple minimal
Sur un jour de bourse, avec $\sigma=20\,\%$, l'action à 100 bouge d'ordinaire de 1,25 ; le terme de courbure du call vaut alors $\tfrac12\times0{,}019\times1{,}25^2\approx0{,}015$. [ajout]

## Geste de calcul type
Pour une fonction du prix, écrire les trois dérivées, placer la dérivée seconde avec $\tfrac12\sigma^2S^2$ dans la dérive, la pente avec $\sigma S$ devant $dW_t$ : pour $F_t=S_t\,e^{r(T-t)}$, $\partial F/\partial t=-rF$ et la dérive sous $\mathbb Q$ s'annule. [exo. 14]

## Cesse d'être valide quand
La fonction doit être deux fois dérivable en $S$ et une fois en $t$ ; au strike, à l'échéance, le payoff ne l'est pas. [§7.2.1, ajout]

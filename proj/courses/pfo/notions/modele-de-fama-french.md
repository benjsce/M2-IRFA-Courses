---
id: pfo/modele-de-fama-french
nom: Modèle de Fama-French à trois facteurs
symbole: '$s_i$, $h_i$'
type: notion
statut: source
cas_de: pfo/modele-factoriel
construite_a_partir_de:
- pfo/regression-du-medaf
- pfo/facteur-smb
- pfo/facteur-hml
alias:
- Fama-French three-factor model
- modèle de Fama et French
- Fama-French
- modèle multifactoriel
- multi-factor model
refs:
- §4.2.2
- p. 59
- p. 82
---

## Ce que c'est
La régression du MEDAF à laquelle Fama et French ajoutent deux facteurs, la taille et la valeur, pour expliquer ce que le marché seul n'explique pas. [§4.2.2]

## Forme
$$R_{i,t}-R_{f,t}=\alpha_i+\beta_i\,(R_{m,t}-R_{f,t})+s_i\,SMB_t+h_i\,HML_t+\epsilon_{i,t}$$ [§4.2.2]

## Ce que les symboles modélisent
$SMB_t$ et $HML_t$ sont les valeurs, à la date $t$, des facteurs de taille et de valeur. $s_i$ est l'exposition de l'actif au premier, de combien son rendement au-delà du taux sans risque bouge quand les petites capitalisations battent les grandes d'un point ; $h_i$ son exposition au second. $\beta_i$, $\alpha_i$ et $\epsilon_{i,t}$ gardent leur sens de la régression du MEDAF, mais leurs valeurs estimées changent quand on ajoute les deux facteurs. [§4.2.2, ajout]

## Ce qui la définit
**Connus** : les rendements de l'actif, du marché, et les séries SMB et HML sur la même période. **Cherchées** : les trois expositions et la constante. Le rendement expliqué se monte facteur par facteur. [§4.2.2, p. 82]

![Un mois où le marché fait 4 % au-delà du taux sans risque, SMB 2 % et HML −2 %, pour une petite entreprise de croissance d'expositions β_i = 1,5, s_i = 0,6, h_i = −0,4 et d'alpha nul. Les marches s'empilent : 1,5 × 4 = 6, puis 0,6 × 2 = 1,2, puis −0,4 × (−2) = 0,8 ; total 8 %, ε à part. Dessous, la Forme : R_i,t − R_f,t = α_i + β_i (R_m,t − R_f,t) + s_i SMB_t + h_i HML_t + ε_i,t.](figures/modele-de-fama-french.svg) [ajout]

Le cours le présente comme la réponse aux limites empiriques du MEDAF à un seul facteur, introduite par Eugene Fama et Kenneth French en 1993. Un $s_i$ positif rapproche l'actif des petites capitalisations ; un $h_i$ positif, du style Value, négatif, du style Growth. [§4.2.2, p. 60]

## Le chemin jusqu'ici
Le modèle reprend pfo/regression-du-medaf, une estimation par dss/moindres-carres-ordinaires sur des couples observés comme dans dss/apprentissage-supervise, et lui ajoute deux colonnes : pfo/facteur-smb et pfo/facteur-hml. Le second trie les entreprises par un ratio dont le numérateur vient de fpp/bilan ; tous deux, comme le premier facteur, s'appuient sur les capitalisations de pfo/portefeuille-de-marche. [ajout]

Le premier facteur reste celui de pfo/medaf, mesuré par pfo/beta, contre un marché que le modèle identifie à pfo/portefeuille-tangent, choisi sur pfo/frontiere-efficiente par pfo/ratio-de-sharpe. Le risque s'y chiffre avec pfo/moments-du-portefeuille et pfo/matrice-de-covariance, dont fpp/volatilite fait la diagonale et que fpp/echelonnement-de-la-variance annualise. [ajout]

Tous les facteurs sont des rendements de portefeuilles, donc des moyennes pondérées, exactes en pfo/rendement-arithmetique et non en pfo/rendement-logarithmique selon pfo/piege-d-agregation. dup/moyenne-variance, qui réduit chaque dup/loterie à deux nombres, et dup/diversification, qui efface le risque propre, restent le décor : seul ce qui est commun à beaucoup d'actifs peut être un facteur. [ajout]

## Exemple minimal
Un mois où le marché fait 4 % au-delà du taux sans risque, avec $SMB=2\,\%$ et $HML=-2\,\%$, une action d'expositions $\beta_i=1{,}5$, $s_i=0{,}6$, $h_i=-0{,}4$ et d'alpha nul est attendue à 8 % au-delà du taux sans risque. [ajout]

## Geste de calcul type
$1{,}5\times4+0{,}6\times2+(-0{,}4)\times(-2)=6+1{,}2+0{,}8=8\,\%$. Pour l'estimer, régresser le rendement de l'actif au-delà du taux sans risque sur les trois colonnes `Mkt-RF`, `SMB` et `HML` des données de Kenneth French, divisées par 100, avec `sm.add_constant`. [p. 82, ajout]

## Cesse d'être valide quand
Comparer son $R^2$ à celui du MEDAF le favorise mécaniquement, puisqu'il contient le MEDAF ; ce qui départage les deux est la significativité de $s_i$ et de $h_i$. [p. 83, ajout]

Les deux facteurs ajoutés sont des constats empiriques : le modèle n'en donne pas l'explication économique. [p. 59, p. 60]

## Origine
- exercice pfo/ex-08 : MEDAF et Fama-French estimés sur les rendements mensuels de AAPL, 2021–2025 [p. 81, p. 82, p. 83]

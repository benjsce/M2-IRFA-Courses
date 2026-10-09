---
id: pfo/coefficient-de-determination
nom: Coefficient de détermination
symbole: '$R^2$, $\bar Y$'
type: notion
statut: source
construite_a_partir_de:
- pfo/regression-du-medaf
alias:
- R²
- R-squared
- R carré
- part de variance expliquée par la régression
refs:
- p. 63
- p. 77
---

## Ce que c'est
La part de la dispersion de la variable expliquée que la régression reproduit, entre zéro et un. [p. 63]

## Forme
$$R^2=1-\frac{\sum_{t=1}^{T}(Y_t-\hat Y_t)^2}{\sum_{t=1}^{T}(Y_t-\bar Y)^2}$$ [p. 63]

## Ce que les symboles modélisent
$Y_t$ est la valeur observée à la date $t$, $\hat Y_t$ celle que prédit la droite, $\bar Y$ la moyenne des $Y_t$. Le numérateur est la somme des carrés des résidus, ce que la droite laisse ; le dénominateur, la dispersion totale autour de la moyenne. $R^2$ n'est pas le carré d'un rendement : c'est une proportion, sans unité. [p. 62, p. 63]

## Ce qui la définit
**Connues** : la dispersion totale de l'actif autour de sa moyenne et celle qui reste autour de la droite. **Cherchée** : la part que la droite emporte. Un $R^2$ de 0,64 dit que le modèle explique 64 % de la variabilité observée de $Y$ dans l'échantillon, et que 36 % restent hors des variables du modèle. [p. 63]

![La dispersion totale du second actif sur les 60 mois, Σ(Y_t − Ȳ)² = 2 477, se partage en 1 210 que la droite du marché reproduit et 1 266 de résidus, Σ(Y_t − Ŷ_t)². R² = 1 − 1 266 / 2 477 = 0,489. Dessous, la Forme : R² = 1 − Σ(Y_t − Ŷ_t)² / Σ(Y_t − Ȳ)².](figures/coefficient-de-determination.svg) [ajout]

Dans une régression du MEDAF, c'est la part du risque de l'actif qui vient du marché, son risque systématique ; le reste, $1-R^2$, est son risque spécifique. [p. 69, p. 77, ajout]

## Le chemin jusqu'ici
$R^2$ juge l'ajustement de pfo/regression-du-medaf, faite par dss/moindres-carres-ordinaires sur des couples d'une variable expliquée et d'une variable explicative, le cadre de dss/apprentissage-supervise ; les moindres carrés rendent justement minimal le numérateur de la Forme. [ajout]

La variable explicative est le marché de pfo/medaf, ce pfo/portefeuille-de-marche que le modèle identifie à pfo/portefeuille-tangent, choisi sur pfo/frontiere-efficiente par pfo/ratio-de-sharpe ; la pente mesure pfo/beta. Le partage du risque que lit $R^2$ est celui de pfo/moments-du-portefeuille et de pfo/matrice-de-covariance, où fpp/volatilite remplit la diagonale et que fpp/echelonnement-de-la-variance annualise. [ajout]

Ces rendements s'agrègent comme pfo/piege-d-agregation le permet en pfo/rendement-arithmetique, non en pfo/rendement-logarithmique. dup/moyenne-variance, qui résume chaque dup/loterie par deux nombres, et dup/diversification, qui efface la part que $R^2$ laisse de côté, donnent son sens à ce partage. [ajout]

## Exemple minimal
Sur les 60 mois simulés, le marché explique 49 % de la dispersion du second actif ; dans le monde dont ils sont tirés, la vraie part est de 50 %. [ajout]

## Geste de calcul type
Lire `model.rsquared`, ou le calculer : $1-1\,266/2\,477=0{,}489$, en $\%^2$. La vraie part vient du bêta : $\beta_2^2\,\mathrm{Var}(R_m)/\mathrm{Var}(R_2)=1{,}5^2\times0{,}00889/0{,}04=0{,}5$. [p. 63, ajout]

## Cesse d'être valide quand
Ajouter une variable explicative ne peut pas faire baisser $R^2$ sur l'échantillon : comparer le MEDAF et le modèle de Fama et French par leur $R^2$ favorise mécaniquement le second. Un $R^2$ plus élevé n'en fait pas un meilleur modèle hors de l'échantillon. [p. 83, ajout]

Un $R^2$ faible ne dit pas que le bêta est mal estimé : dans l'exemple, la moitié du risque est spécifique, et le bêta a pourtant une statistique t de 7,45. [ajout]

## Origine
- exercice pfo/ex-05 : sur 60 mois simulés, $R^2=0{,}87$ [p. 73, ajout]
- exercice pfo/ex-08 : comparer le $R^2$ du MEDAF et celui du modèle de Fama et French [p. 83]

---
id: dss/critere-penalise
nom: Critère pénalisé
type: principe
statut: source
construite_a_partir_de:
- dss/moindres-carres-ordinaires
- dss/erreur-de-test
refs:
- slide 38
- slide 39
- slide 40
---

## Ce que c'est
Estimer l'erreur de test en corrigeant l'erreur d'apprentissage d'une pénalité qui croît avec le nombre de variables. [slide 39]

## Ce qui la définit
**Ce qu'on connaît** : l'erreur d'apprentissage, $\mathrm{RSS}/n$, calculée sur les données qui ont servi à ajuster. **Ce qu'on cherche** : l'erreur de test, qu'on ne voit pas. Le trou entre les deux grandit avec le nombre de variables, puisque chaque variable ajoutée fait baisser l'erreur d'apprentissage, même quand elle n'apporte rien. Le critère pénalisé estime ce trou par une pénalité qui ne dépend que de ce nombre. [slide 38, slide 39]

Tous corrigent l'erreur d'apprentissage selon la taille du modèle, et tous servent au même usage : comparer des modèles qui n'ont pas le même nombre de variables. Le $C_p$ et le BIC ajoutent une pénalité à la RSS ; l'AIC pénalise une log-vraisemblance, et le $R^2$ ajusté divise chaque somme de carrés par ses degrés de liberté. [slide 39, slide 41, slide 42, slide 43, slide 44]

Le $C_p$, l'AIC et le BIC se lisent dans le sens « plus petit vaut mieux », le $R^2$ ajusté dans l'autre. [slide 40, slide 44]

C'est la voie indirecte. Elle ne demande qu'un ajustement par modèle, là où la validation croisée en demande un par bloc — mais elle suppose une forme de modèle, ce que la validation croisée ne suppose pas. Le critère ne touche pas aux coefficients, qui restent ceux des moindres carrés : il ne départage que des modèles déjà ajustés. [slide 38, slide 45, ajout]


## Le chemin jusqu'ici
dss/moindres-carres-ordinaires fournit la RSS, l'erreur d'apprentissage que le critère corrige, et dss/erreur-de-test la quantité qu'il cherche à approcher. dss/apprentissage-supervise est le cadre où l'on peut mesurer l'une et l'autre, puisque chaque exemple porte sa réponse. Sans la distinction entre les deux erreurs, la pénalité n'aurait pas d'objet. [ajout]

## Exemple minimal
Sur les 20 clients, le modèle à l'endettement et au revenu a une erreur d'apprentissage de 1,12 et une erreur de test de 1,16 ; le modèle complet, à cinq prédicteurs, 0,98 et 1,83. Le trou passe de 0,04 à 0,85. La pénalité du $C_p$ l'estime à 0,28 puis 0,70 : l'estimation est grossière, mais elle grandit avec le trou, et connu plus pénalité fait 1,40 contre 1,68, le même classement que l'erreur de test. [ajout]

## Cesse d'être valide quand
Ces critères estiment l'erreur de test, ils ne la mesurent pas : leur pénalité repose sur une hypothèse de modèle, et, pour le $C_p$ et le BIC, la variance du bruit doit elle-même être estimée. [ajout]

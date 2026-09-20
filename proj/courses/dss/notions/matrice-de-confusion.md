---
id: dss/matrice-de-confusion
nom: Matrice de confusion
type: notion
statut: source
construite_a_partir_de:
- dss/apprentissage-supervise
alias:
- confusion matrix
refs:
- slide 10
- slide 11
---

## Ce que c'est
Le tableau qui croise la condition réelle et la condition prédite, et dont se déduit toute mesure de performance d'un classifieur. [slide 11]

## Forme
$$\begin{array}{c|cc} & \text{prédit }+ & \text{prédit }- \\ \hline \text{réel }+ & \mathrm{TP} & \mathrm{FN} \\ \text{réel }- & \mathrm{FP} & \mathrm{TN} \end{array}$$ [slide 11]

## Ce qui la définit
Les quatre cases épuisent les cas : un positif correctement détecté, un négatif correctement rejeté, une fausse alarme et un manqué. Tout le reste est un rapport entre ces quatre nombres et leurs marges. [slide 10]

Le choix de la marge par laquelle on divise décide de ce que la mesure dit. Diviser par la ligne des réels positifs donne la sensibilité ; par la colonne des prédits positifs, la précision. Les deux peuvent être très éloignées sur une classe rare. [slide 10, slide 11]


## Le chemin jusqu'ici
Le socle se réduit à dss/apprentissage-supervise, qui fournit l'étiquette. [ajout]

Sans étiquette, il n'y a rien à croiser : la matrice confronte une vérité connue à une prédiction, et il faut les deux. [ajout]

## Exemple minimal
Sur 100 cas dont 10 positifs, un classifieur qui prédit toujours « négatif » a une exactitude de 0,90 et une sensibilité de 0. [ajout]

## Geste de calcul type
Avant de lire un indicateur, repérer son dénominateur : $\mathrm{P}$ et $\mathrm{N}$ sont les marges de la vérité, $\mathrm{PP}$ et $\mathrm{PN}$ celles de la prédiction. C'est ce qui sépare la sensibilité de la précision. [slide 11]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| dénominateur | réels positifs $\mathrm{P}$ | sensibilité $\mathrm{TPR}=\mathrm{TP}/\mathrm{P}$ |
| dénominateur | réels négatifs $\mathrm{N}$ | spécificité $\mathrm{TNR}=\mathrm{TN}/\mathrm{N}$ |
| dénominateur | prédits positifs $\mathrm{PP}$ | précision $\mathrm{PPV}=\mathrm{TP}/\mathrm{PP}$ |
| dénominateur | population totale | exactitude $\mathrm{ACC}=(\mathrm{TP}+\mathrm{TN})/(\mathrm{P}+\mathrm{N})$ |
| combinaison | moyenne harmonique de $\mathrm{PPV}$ et $\mathrm{TPR}$ | score $F_1$ |
[slide 10, slide 11]

## Cesse d'être valide quand
Toutes ces mesures sont calculées à un seuil de décision fixé. Comparer deux modèles à seuil fixé mélange la qualité du score et le choix du seuil ; c'est ce que la courbe ROC sépare. [ajout]

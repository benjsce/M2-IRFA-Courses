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

## Ce que les symboles modélisent
Positif désigne la classe qu'on cherche à détecter, ici le défaut ; négatif, l'autre. $\mathrm{TP}$ compte les positifs réels que le classifieur déclare positifs, les cas détectés ; $\mathrm{FN}$ les positifs réels qu'il déclare négatifs, les manqués. $\mathrm{FP}$ compte les négatifs réels déclarés positifs, les fausses alarmes ; $\mathrm{TN}$ les négatifs réels correctement rejetés. [slide 11, ajout]

$\mathrm{P}=\mathrm{TP}+\mathrm{FN}$ et $\mathrm{N}=\mathrm{FP}+\mathrm{TN}$ sont les marges de la vérité, les réels positifs et négatifs ; $\mathrm{PP}=\mathrm{TP}+\mathrm{FP}$ et $\mathrm{PN}=\mathrm{FN}+\mathrm{TN}$ celles de la prédiction. [slide 10, slide 11]

Ce sont des effectifs, pas des taux : un taux ne naît qu'en divisant par une marge. Dans chaque sigle, la première lettre dit si la prédiction est juste, la seconde ce qui a été prédit ; un faux négatif est donc un cas réellement positif. [ajout]

## Ce qui la définit
Les quatre cases épuisent les cas : un positif correctement détecté, un négatif correctement rejeté, une fausse alarme et un manqué. Tout le reste est un rapport entre ces quatre nombres et leurs marges. [slide 10]

Le choix de la marge par laquelle on divise décide de ce que la mesure dit. Diviser $\mathrm{TP}+\mathrm{TN}$ par tous les cas donne l'exactitude ; diviser $\mathrm{TP}$ par la seule ligne des réels positifs, la sensibilité. Sur une classe rare, les deux peuvent tout opposer. [slide 10, slide 11]

## Le chemin jusqu'ici
Le socle se réduit à dss/apprentissage-supervise, qui fournit l'étiquette. Sans étiquette, il n'y a rien à croiser : la matrice confronte une vérité connue à une prédiction, et il faut les deux. [ajout]

## Exemple minimal
Sur 100 dossiers dont 10 défauts, un classifieur qui annonce toujours « pas de défaut » a une exactitude de 0,90 et une sensibilité de 0. [ajout]

![Les cent dossiers de l'exemple, un carré chacun, rangés dans leur case : les dix défauts, colorés, sont tous en FN, les quatre-vingt-dix autres en TN, et les cases TP et FP sont vides. Divisé par la seule ligne des réels positifs, encadrée, le tableau donne une sensibilité de 0 sur 10 ; divisé par le tableau entier, une exactitude de 90 sur 100.](figures/matrice-de-confusion.svg) [ajout]

## Geste de calcul type
Repérer le dénominateur, puis diviser. La sensibilité divise par la ligne des réels positifs : $0/10=0$. L'exactitude divise par le tableau entier : $90/100=0{,}90$. [slide 10, ajout]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| dénominateur | réels positifs $\mathrm{P}$ | sensibilité $\mathrm{TPR}=\mathrm{TP}/\mathrm{P}$ |
| dénominateur | réels négatifs $\mathrm{N}$ | spécificité $\mathrm{TNR}=\mathrm{TN}/\mathrm{N}$ |
| dénominateur | prédits positifs $\mathrm{PP}$ | précision $\mathrm{PPV}=\mathrm{TP}/\mathrm{PP}$ |
| dénominateur | population totale | exactitude $\mathrm{ACC}=(\mathrm{TP}+\mathrm{TN})/(\mathrm{P}+\mathrm{N})$ |
[slide 10, slide 11]

## Cesse d'être valide quand
Toutes ces mesures sont calculées à un seuil de décision fixé. Comparer deux modèles à seuil fixé mélange la qualité du score et le choix du seuil ; c'est ce que la courbe ROC sépare. [ajout]

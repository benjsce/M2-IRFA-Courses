---
id: dss/smote
nom: SMOTE
type: notion
statut: source
construite_a_partir_de:
- dss/preparation-des-donnees
alias:
- SMOTE
- synthetic minority over-sampling technique
refs:
- slide 220
- slide 229
- slide 233
---

## Ce que c'est
Sur-échantillonner la classe minoritaire en fabriquant des observations synthétiques. [slide 229]

## Ce qui la définit
Le déséquilibre des classes est un problème de préparation, pas de modèle : un classifieur entraîné sur un jeu où une classe est rare apprend surtout à prédire l'autre. [slide 229, ajout]

**Connu** : les observations rares et, pour chacune, ses plus proches voisines rares. **Cherché** : de nouvelles observations rares, plausibles. SMOTE les prend sur le segment qui joint une observation rare à l'une de ses voisines, à une fraction $u$ du chemin tirée au hasard entre 0 et 1 : $x_{\text{nouveau}}=x_i+u\,(x_{\text{voisine}}-x_i)$. [ajout]

![Un nuage construit pour le dessin : beaucoup d'observations majoritaires, cinq rares. Chaque point synthétique, creux, est pris sur le segment qui joint une observation rare à l'une de ses voisines rares ; aucune n'est recopiée.](figures/smote.svg) [ajout]

La technique ne recopie donc pas les observations rares, elle en construit de nouvelles entre elles : c'est ce qui la sépare d'un simple sur-échantillonnage, qui dupliquerait les mêmes points. [ajout]

## Le chemin jusqu'ici
SMOTE est une étape de dss/preparation-des-donnees : il agit sur le jeu avant l'apprentissage, là où le cours demande de déterminer les probabilités a priori des catégories et de traiter le biais de volume. [slide 189, ajout]

La classe qu'on rééquilibre est une étiquette, la sortie désirée de dss/apprentissage-supervise ; et le cours pose la préparation comme une contrainte du dss/reseau-de-neurones-artificiel, qui apprendrait sinon à répondre la catégorie nombreuse par défaut. [ajout]

## Exemple minimal
Dans l'étude du cours sur les biais, le jeu « genre » compte 113 femmes pour 484 hommes : c'est la classe des femmes que SMOTE complète avant de chercher si le genre est prédictible. [slide 220, slide 233, ajout]

## Cesse d'être valide quand
Les observations synthétiques n'apportent aucune information nouvelle : elles rééquilibrent le compte, elles ne remplacent pas des données manquantes. Le cours ne discute pas ce que cela fait aux mesures de performance. [ajout]

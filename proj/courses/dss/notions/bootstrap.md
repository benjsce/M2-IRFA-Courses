---
id: dss/bootstrap
nom: Bootstrap
type: notion
statut: source
construite_a_partir_de: []
alias:
- bootstrap
refs:
- slide 99
---

## Ce que c'est
Tirer avec remise dans l'échantillon pour en fabriquer plusieurs autres de même taille. [slide 99]

## Ce qui la définit
L'idée que le cours met en avant est celle d'une multiplication artificielle des réalisations : si l'on disposait de plusieurs échantillons, on pourrait calculer plusieurs prédictions et les moyenner. Le bootstrap fournit ces échantillons à partir d'un seul. [slide 98, slide 99]

Le tirage avec remise a une conséquence qui servira plus loin : toutes les observations ne sont pas utilisées dans chaque échantillon, et en moyenne un tiers d'entre elles en sont absentes. [slide 102]

## Exemple minimal
Sur 100 observations, un tirage avec remise de 100 observations en laisse environ 37 de côté. [slide 102]

## Cesse d'être valide quand
Les échantillons tirés d'un même jeu ne sont pas indépendants entre eux — c'est ce qui limitera le gain du bagging. [slide 108]

---
id: dup/aversion-forte-au-risque
nom: Aversion forte au risque
type: notion
statut: source
construite_a_partir_de:
- dup/pessimisme
- dup/accroissement-de-risque
alias:
- strong risk aversion
- aversion au risque au sens fort
refs:
- L3 slide 32
- L4 slide 15
- L4 slide 34
---

## Ce que c'est
Refuser tout étalement préservant la moyenne, et non seulement préférer la moyenne certaine à la loterie qui la porte. [L4 slide 15]

## Forme
$$U(X)\le u\big(\mathbb{E}_\varphi[X]\big)\le u\big(\mathbb{E}[X]\big)$$ [L4 slide 15]

## Ce qui la définit
La forme faible ne met en balance qu'une loterie et sa moyenne certaine, et elle est acquise dès que $u$ est croissante concave et que la déformation est pessimiste — c'est la chaîne d'inégalités ci-dessus. La forme forte demande davantage : rejeter n'importe quel étalement préservant la moyenne, donc respecter la dominance stochastique du second ordre. [L4 slide 15]

Sous utilité dépendante du rang, cela exige que $u$ **et** $\varphi$ soient toutes deux croissantes concaves. La conséquence est directe pour le portefeuille : la concavité de l'utilité seule ne justifie pas d'écarter tous les portefeuilles porteurs d'un risque supplémentaire de moyenne nulle. [L4 slide 15]

Le cours en donne le contre-exemple. Avec $u(x)=x$ et une déformation pessimiste mais non concave, ajouter un risque équitable de $\pm5$ à l'un des résultats augmente la valeur, alors que la moyenne ne bouge pas. Préférer le certain à un pari équitable n'entraîne donc pas qu'on déteste tout risque ajouté à l'intérieur d'un portefeuille existant. [L4 slide 34]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite se combinent en dup/utilite-esperee, dont dup/rdu déforme les probabilités cumulées ; dup/pessimisme dit dans quel sens penche cette déformation, et c'est lui qui donne la forme faible. [ajout]

Il fallait par ailleurs savoir ce qu'est « plus de risque à moyenne égale », et c'est dup/accroissement-de-risque qui le définit. La forme forte se lit exactement sur cet ordre partiel : refuser tout ce qu'il déclare plus risqué. Les deux amonts répondent donc à deux questions distinctes — avec quoi on évalue, et sur quoi porte le refus. [ajout]

## Exemple minimal
$X=(10;0{,}4\,|\,20;0{,}6)$ et $Y$, qui remplace le résultat 20 par 15 ou 25 à parts égales, ont la même moyenne 16 ; pourtant $Y$ vaut 14,875 contre 14,250 pour $X$. [L4 slide 34]

## Geste de calcul type
Vérifier les deux concavités séparément, celle de $u$ et celle de $\varphi$ : la forme faible se contente du pessimisme, la forme forte tombe dès que la déformation cesse d'être concave. [L4 slide 15]

## Cesse d'être valide quand
Les arguments de diversification reposent sur la forme forte : ils demandent donc une restriction sur la déformation des probabilités, et pas seulement sur l'utilité. [L4 slide 34]

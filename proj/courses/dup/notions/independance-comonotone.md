---
id: dup/independance-comonotone
nom: Indépendance comonotone
type: notion
statut: source
cas_de: dup/independance-restreinte
valeur: le mélange n’est imposé qu’entre actes comonotones
construite_a_partir_de:
- dup/cadre-anscombe-aumann
alias:
- comonotonie
- comonotonicity
- comonotonic independence
- axiome 7
refs:
- L4 slide 59
---

## Ce que c'est
L’indépendance n’est exigée qu’entre actes comonotones, c’est-à-dire entre actes qui ne classent jamais deux états en sens opposés. [L4 slide 59]

## Forme
$$\big(z(s)-z(t)\big)\big(y(s)-y(t)\big)\ge0\ \ \forall s,t\in S;\qquad f\succsim g\iff\alpha f+(1-\alpha)h\succsim\alpha g+(1-\alpha)h$$ [L4 slide 59]

## Ce qui la définit
Deux fonctions réelles sont comonotones quand leurs écarts entre deux états sont toujours de même signe ; deux actes le sont quand leurs vecteurs d’utilité le sont. La condition ne dit pas qu’ils se ressemblent, seulement qu’ils s’accordent sur l’ordre des états. [L4 slide 59]

Mélanger des actes comonotones ne couvre rien : il n’existe aucun état où l’un compense l’autre, puisqu’ils montent et descendent ensemble. L’axiome impose donc l’indépendance là où elle ne coûte rien, et reste muet là où le mélange apporterait un gain de couverture — ce silence est exactement la place qu’occupera la capacité non additive. [L4 slide 59]

## Le chemin jusqu'ici
dup/acte et dup/loterie s’emboîtent dans dup/cadre-anscombe-aumann, qui donne à la fois le mélange entre actes et le vecteur d’utilité sur lequel se lit l’ordre des états. [ajout]

La comonotonie est une propriété de ce vecteur, pas de l’acte pris isolément : sans le cadre, il n’y aurait ni mélange à restreindre ni classement à comparer. L’affaiblissement de l’axiome se formule donc ici, et nulle part plus haut. [ajout]

## Exemple minimal
Parier sur rouge et parier sur bleu ne sont pas comonotones — l’un place l’état rouge au-dessus de l’état bleu, l’autre l’inverse — et l’axiome ne dit donc rien de leur mélange. [ajout]

## Geste de calcul type
Comparer les deux vecteurs d’utilité état par état : s’il existe deux états où les écarts sont de signes opposés, les actes ne sont pas comonotones et l’axiome ne s’applique pas. [L4 slide 59]

## Cesse d'être valide quand
L’axiome ne porte que sur des actes deux à deux comonotones, et il est muet partout ailleurs. C’est ce qui laisse passer une croyance non additive, mais aussi ce qui l’empêche d’imposer à elle seule l’aversion à l’ambiguïté. [L4 slide 59, L4 slide 60]

---
id: dup/dara
nom: Aversion absolue décroissante
type: notion
statut: source
construite_a_partir_de:
- dup/aversion-absolue-arrow-pratt
alias:
- DARA
- decreasing absolute risk aversion
refs:
- L1 slide 34
---

## Ce que c'est
L’hypothèse, largement acceptée, que l’on devient moins averse au risque à mesure qu’on s’enrichit. [L1 slide 34]

## Forme
$$-\dfrac{u'''(z)}{u''(z)}\ \ge\ -\dfrac{u''(z)}{u'(z)}\qquad\text{pour tout }z$$ [L1 slide 34]

## Ce qui la définit
C’est exactement l’équivalent de « la prime de risque décroît avec la richesse initiale », et donc de « $A(w_0)$ décroît avec $w_0$ ». [L1 slide 34]

La condition fait apparaître la dérivée troisième : la décroissance de l’aversion exige de la prudence. [ajout]

## Exemple minimal
L’utilité logarithmique est DARA : $A(z)=1/z$ passe de $0{,}01$ à 100 à $0{,}001$ à 1000. [L1 slide 35]

## Geste de calcul type
Vérifier le signe de $A'(z)$. Si l’utilité est CRRA, la propriété est acquise : $A(z)=\gamma/z$ décroît toujours. [L1 slide 35]

## Cesse d'être valide quand
L’utilité quadratique la viole : son aversion absolue $A(z)=(c-z)^{-1}$ croît avec la richesse. [L1 slide 35, L1 slide 15]

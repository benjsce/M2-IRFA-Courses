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

## Le chemin jusqu'ici
Il faut dup/fonction-utilite, puis dup/aversion-absolue-arrow-pratt pour disposer d'un $A(z)$ que l'on puisse faire varier. [ajout]

DARA est une hypothèse sur la façon dont $A(z)$ varie avec la richesse ; elle suppose donc que $A$ existe et soit définie en tout point. C'est une hypothèse empirique, pas un théorème, et le socle court le montre : rien dans le cours ne l'impose. [ajout]

## Exemple minimal
L’utilité logarithmique est DARA : $A(z)=1/z$ passe de $0{,}01$ à 100 à $0{,}001$ à 1000. [L1 slide 35]

![L'aversion absolue de l'utilité logarithmique décroît avec la richesse ; celle de l'utilité quadratique croît, et explose au point de satiété. Pour la quadratique on a pris $c=100$, le point de satiété de l'exemple de la fiche sur l'utilité quadratique ; les deux courbes se croisent à 50.](figures/dara.svg) [ajout]

## Geste de calcul type
Vérifier le signe de $A'(z)$. Si l’utilité est CRRA, la propriété est acquise : $A(z)=\gamma/z$ décroît toujours. [L1 slide 35]

## Cesse d'être valide quand
L’utilité quadratique la viole : son aversion absolue $A(z)=(c-z)^{-1}$ croît avec la richesse. [L1 slide 35, L1 slide 15]

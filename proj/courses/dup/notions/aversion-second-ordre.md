---
id: dup/aversion-second-ordre
nom: Aversion au risque du second ordre
type: notion
statut: source
construite_a_partir_de:
- dup/approximation-arrow-pratt
alias:
- second-order risk aversion
refs:
- L2 slide 21
- L2 slide 24
- L3 slide 40
---

## Ce que c'est
Sous utilité espérée dérivable, la prime d’un petit pari de moyenne nulle est proportionnelle à la variance, donc au carré de l’écart type. [L2 slide 21]

## Forme
$$r(\sigma)\approx\dfrac{\rho}{2}\sigma^2,\qquad \rho=-\dfrac{u''(x)}{u'(x)}$$ [L3 slide 40]

## Ce qui la définit
La conséquence est forte : la moyenne agit au premier ordre et l’écart type seulement au second, donc un agent à utilité espérée accepte toujours un petit pari actuariellement favorable. [L2 slide 24]

C’est ce qui rend difficile d’expliquer qu’on renonce à des investissements favorables, ou qu’on s’assure complètement à prime défavorable. [L2 slide 21]

## Exemple minimal
Pour un pari de $\pm\sigma$ à pile ou face avec $\rho=0{,}01$ et $\sigma=10$ : la prime vaut environ $0{,}5$. [ajout]

## Geste de calcul type
Développer l’équivalent certain à l’ordre deux en $\sigma$ : le terme d’ordre un s’annule pour un pari de moyenne nulle, il ne reste que le terme en $\sigma^2$. [L3 slide 40]

## Cesse d'être valide quand
Suppose $u$ deux fois dérivable au point considéré : un coude en ce point produit une aversion du premier ordre, d’un tout autre ordre de grandeur. [L3 slide 41]

---
id: dup/actualisation-quasi-hyperbolique
nom: Actualisation quasi-hyperbolique
symbole: $\beta$
type: notion
statut: source
cas_de: dup/utilite-actualisee
construite_a_partir_de:
- dup/biais-pour-le-present
alias:
- quasi-hyperbolic discounting
- préférences (β, δ)
- β-δ preferences
refs:
- L5 slide 13
- L5 slide 14
- L5 slide 42
---

## Ce que c'est
L'actualisation exponentielle, avec en plus un même facteur $\beta<1$ qui frappe tout ce qui n'est pas aujourd'hui. [L5 slide 13]

## Forme
$$D(t)=\begin{cases}1 & t=0\\ \beta\,\delta^{t} & t>0\end{cases}\qquad U=u_0+\beta\left(\delta u_1+\delta^2u_2+\delta^3u_3+\dots\right)$$ [L5 slide 13]

## Ce que les symboles modélisent
$\beta$, entre 0 et 1, est le biais pour le présent : la décote qu'une utilité subit du seul fait de ne pas être immédiate, quelle que soit sa date. $\delta$, entre 0 et 1, garde son rôle exponentiel entre deux dates futures. La lettre $\beta$ nomme ailleurs dans le cours le coefficient de l'utilité quadratique et l'exposant de la pondération cumulative, sans rapport. [L5 slide 13, ajout]

## Ce qui la définit
C'est l'extension la plus simple du modèle exponentiel qui admette un biais pour le présent : $D(0)/D(\tau)=1/(\beta\delta^\tau)$, plus grand que $D(t)/D(t+\tau)=1/\delta^\tau$ pour tout $t>0$. [L5 slide 13]

![Les poids D(t) semaine par semaine, avec δ = 0,9 et β = ½ : en pointillé ceux du modèle exponentiel, δᵗ ; en plein ceux du modèle quasi-hyperbolique, qui valent 1 aujourd'hui puis sont tous abaissés du même facteur β. La mesure à la première semaine est ce facteur : D(t) = βδᵗ pour t > 0.](figures/actualisation-quasi-hyperbolique.svg) [ajout]

Entre deux dates futures, le rapport des poids ne dépend que de $\delta$ : les engagements qui ne touchent pas au présent restent cohérents d'une période à l'autre, ce qui simplifie beaucoup l'analyse, et c'est ce qui le distingue de l'actualisation hyperbolique. [L5 slide 42]

## Le chemin jusqu'ici
dup/biais-pour-le-present est la condition à satisfaire, posée sur la fonction de dup/utilite-actualisee. Le modèle y répond en changeant le moins possible dup/actualisation-exponentielle, celle que dup/inversion-des-preferences-dans-le-temps avait prise en défaut : il garde $\delta$ et ne touche qu'au poids du présent, les utilités restant celles de dup/fonction-utilite. [L5 slide 12, L5 slide 13]

## Exemple minimal
$\beta=\tfrac12$, $\delta=1$, $u(x)=x$ : 110 dans quatre semaines vaut 55 aujourd'hui, et 110 dans trente semaines aussi. [L5 slide 14]

## Geste de calcul type
Pour 100 tout de suite contre 110 dans quatre semaines : $u(100)=100>55=\beta\delta^4u(110)$, on prend les 100. Pour 100 dans vingt-six semaines contre 110 dans trente : $\beta\delta^{26}u(100)=50<55=\beta\delta^{30}u(110)$, on prend les 110. Les deux choix sont reproduits. [L5 slide 14]

## Cesse d'être valide quand
Le biais porte aussi sur le futur proche et pas seulement sur le présent : préférer 100 dans une semaine à 110 dans cinq, mais 110 dans trente à 100 dans vingt-six, ne s'explique pas par un modèle où toutes les dates futures sont décotées du même $\beta$. [L5 slide 15]

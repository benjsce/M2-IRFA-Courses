---
id: fpp/modele-de-merton
nom: Modèle de Merton
symbole: '$l$, $s$'
type: notion
statut: source
construite_a_partir_de:
- fpp/responsabilite-limitee
- fpp/formule-de-black
- fpp/parite-call-put
alias:
- Merton model
- modèle de la firme
- spread de crédit
- credit spread
- dette risquée
refs:
- exos §2.1
- exo. 16
---

## Ce que c'est
Le modèle où les capitaux propres d'une entreprise endettée sont un call sur la valeur de ses actifs, de strike le nominal de sa dette. [exo. 16]

## Forme
$$E_0=e^{-rT}F_T\big(N(d_1)-l\,N(d_2)\big),\qquad s=-\frac1T\ln\Big(N(d_2)+\frac1l\,N(-d_1)\Big),\qquad d_{1,2}=\frac{-\ln l\pm\frac{\sigma^2T}{2}}{\sigma\sqrt T}$$ [exo. 16]

## Ce que les symboles modélisent
$l$, égal à $D/F_T$, rapporte le nominal $D$ de la dette, un zéro-coupon d'échéance $T$, à la valeur forward $F_T$ des actifs : 0 pour une entreprise sans dette, 1 pour une entreprise dont la dette absorbe tout. Ce n'est pas le levier $l_t=A_t/E_t$ du poly. $s$ est le spread de crédit : l'entreprise emprunte au taux $r+s$, et sa dette vaut $D\,e^{-(r+s)T}$. $\sigma$ est ici la volatilité des actifs, $E_0$ la valeur des capitaux propres aujourd'hui. [exo. 16]

## Retrouver la formule
![La valeur des actifs à l'échéance partagée entre créanciers et actionnaires pour une dette de nominal D : les créanciers reçoivent min(S_T, D), les actionnaires (S_T − D)⁺, le payoff d'un call de strike D. Les deux parts s'empilent pour redonner S_T.](figures/modele-de-merton.svg) [exo. 16, ajout]

À l'échéance, les créanciers sont payés d'abord : 80 si les actifs valent plus, tout sinon. Les actionnaires, protégés par la responsabilité limitée, reçoivent $(S_T-D)^+$ : un call sur les actifs, de strike la dette. [exo. 16]

Le bilan partage les actifs entre les deux : la dette reçoit $S_T-(S_T-D)^+=D-(D-S_T)^+$, un zéro-coupon de nominal $D$ moins un put. [exo. 16]

Avec des actifs de 100, une volatilité de 20 %, une dette de 80 à un an et un taux de 4 % : la formule de Black donne 23,91 aux capitaux propres, la dette vaut donc 76,09, et $80\,e^{-(0,04+s)}=76{,}09$ donne un spread de 1,01 %. [ajout]

En lettres, en égalant $D\,e^{-(r+s)T}$ à $D\,e^{-rT}$ moins le put de Black : [exo. 16]

$$s=-\frac1T\ln\Big(N(d_2)+\frac1l\,N(-d_1)\Big)$$ [exo. 16]

## Ce qui la définit
Ce qui est **connu** : la valeur des actifs, leur volatilité, le nominal de la dette et le taux. Ce qu'on **cherche** : ce que valent les capitaux propres et à quel taux l'entreprise emprunte. Le poly avait annoncé qu'il reviendrait sur l'effet du plancher des capitaux propres : le livre d'exercices le fait ici. [exo. 16, §1.4]

Plus de risque sur les actifs fait monter le call et le put à la fois : les actionnaires y gagnent, les créanciers y perdent. Un dividende versé aux actionnaires abaisse la valeur forward des actifs, renchérit le put et creuse le spread. Quand $l$ tend vers 0, le spread s'annule ; quand $l$ tend vers 1, il explose. [exo. 16]

## Le chemin jusqu'ici
fpp/responsabilite-limitee fait des capitaux propres un paiement coudé, qui est exactement celui d'une option ; fpp/formule-de-black lui donne un prix à partir de la valeur forward des actifs ; fpp/parite-call-put transforme la dette en zéro-coupon moins un put, et fait apparaître le spread. [ajout]

Le décor est celui du premier chapitre : fpp/bilan partage les actifs entre dette et capitaux propres, fpp/levier et fpp/effet-de-levier disaient déjà que les seconds amplifient le risque des premiers, décrit par fpp/prime-de-risque et fpp/volatilite. [ajout]

Le prix du call demande le reste du cours : fpp/prix-a-terme et fpp/prix-forward pour la valeur forward des actifs, que fpp/cash-and-carry obtient sous fpp/absence-d-arbitrage, nette du fpp/taux-de-dividende et des fpp/dividendes-intermediaires ; fpp/formule-black-scholes, fpp/modele-black-scholes, fpp/probabilite-risque-neutre et fpp/tendance-risque-neutre pour la loi, avec fpp/echelonnement-de-la-variance et fpp/transformee-de-laplace-gaussienne ; fpp/option et fpp/payoff pour le paiement ; fpp/valeur-actuelle-nette, fpp/zero-coupon et fpp/capitalisation pour l'actualisation. [ajout]

## Exemple minimal
Des actifs de 100, de volatilité 20 %, une dette de nominal 80 à un an, un taux de 4 % : les capitaux propres valent 23,91, la dette 76,09, et le spread de crédit 1,01 %. [ajout]

## Geste de calcul type
Calculer $F_T$ et $l=D/F_T$, ici $80/104{,}08=0{,}769$, puis $d_1$ et $d_2$, puis le call de Black pour les capitaux propres et le spread par la formule. [exo. 16, ajout]

## Cesse d'être valide quand
La dette est un seul zéro-coupon et la faillite ne peut survenir qu'à son échéance ; la valeur des actifs suit un modèle log-normal ; et ni cette valeur ni sa volatilité ne s'observent directement. [exo. 16, ajout]

---
id: fpp/responsabilite-limitee
nom: Responsabilité limitée
type: notion
statut: source
construite_a_partir_de:
- fpp/effet-de-levier
alias:
- limited liability
- faillite
- bankruptcy
refs:
- §1.4
---

## Ce que c'est
La règle qui empêche la valeur des capitaux propres de devenir négative, si bien que l'actionnaire ne peut pas perdre plus que sa mise. [§1.4]

## Forme
$$E_t = \max(A_t - D_t,\ 0),\qquad \text{faillite dès que}\quad \tilde\pi_A \le -\frac{1}{l_t}$$ [§1.4]

## Ce que les symboles modélisent
$A_t$, $D_t$ et $E_t$ sont les postes du bilan à la date où l'on regarde ; $l_t$ est le levier d'où l'on part ; $\tilde\pi_A$ la variation relative des actifs sur la période. Le poly écrit le seuil sans tilde ; il s'agit bien de la variation réalisée, pas de sa moyenne. [§1.4, ajout]

## Ce qui la définit
La règle a été introduite pour encourager l'entreprise : quand l'entreprise ne peut plus payer ses factures, ou quand ses actifs valent moins que ses dettes, elle est en faillite, la valeur des capitaux propres est ramenée à 0, et c'est la dette qui encaisse la perte. [§1.4]

On connaît le levier ; on cherche quelle baisse des actifs efface les capitaux propres. En négligeant le coût de la dette, l'effet de levier transforme une baisse relative $x$ des actifs en une baisse $l_t\,x$ des capitaux propres ; elle atteint $-100\,\%$ pour $x = 1/l_t$. [§1.4]

Le poly annonce qu'il reviendra sur l'effet de ce plancher sur la valeur des capitaux propres et de la dette ; le livre d'exercices le fait avec le modèle de Merton, où ce plancher fait des capitaux propres une option. [§1.4, exo. 16]

![Les capitaux propres à l'échéance en fonction des actifs, pour une dette de 80 : ils suivent les actifs au-dessus de 80 et restent à 0 en dessous, là où sans la règle ils deviendraient négatifs.](figures/responsabilite-limitee.svg) [ajout]

## Le chemin jusqu'ici
fpp/bilan fait des capitaux propres la différence entre les actifs et la dette : rien, dans l'égalité seule, ne l'empêche d'être négative, et c'est ce que la règle interdit. [ajout]

fpp/levier et fpp/effet-de-levier disent à quelle vitesse on s'approche de ce plancher : les capitaux propres bougent $l_t$ fois plus vite que les actifs. fpp/prime-de-risque et fpp/volatilite décrivent le mouvement des actifs lui-même, et disent donc si une baisse de $1/l_t$ est un accident fréquent ou exceptionnel. [ajout]

## Exemple minimal
Des actifs de 100, une dette de 80, un levier de 5 : si les actifs tombent à 75, les capitaux propres vaudraient $-5$ ; ils valent 0, et les créanciers récupèrent 75 au lieu de 80. [ajout]

## Geste de calcul type
Calculer le seuil $-1/l_t$ et le comparer à la volatilité des actifs : avec un levier de 5, il faut une baisse de 20 %, soit cinq écarts types pour des actifs de volatilité 4 %. [§1.4, ajout]

## Cesse d'être valide quand
Le seuil $-1/l_t$ néglige le coût de la dette pendant la période, comme le précise le poly. Et la faillite peut survenir avant, par défaut de paiement, quand l'entreprise ne peut plus payer ses factures alors que ses actifs dépassent encore sa dette. [§1.4]

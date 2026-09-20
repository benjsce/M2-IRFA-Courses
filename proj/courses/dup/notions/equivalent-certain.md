---
id: dup/equivalent-certain
nom: Équivalent certain
symbole: $c$
type: notion
statut: source
construite_a_partir_de:
- dup/utilite-esperee
alias:
- certainty equivalent
- CE
refs:
- L1 slide 9
---

## Ce que c'est
Le montant certain qui procure exactement l’utilité espérée du pari. [L1 slide 9]

## Forme
$$U(c)=\mathbb{E}[U(\tilde x)]$$ [L1 slide 9]

## Ce qui la définit
Il traduit une distribution entière en un seul nombre, exprimé dans l’unité des résultats et non dans celle des utilités. [L1 slide 9]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite donnent dup/utilite-esperee, donc un nombre attaché à chaque pari. [ajout]

L'équivalent certain fait le chemin inverse : il retraduit ce nombre en montant. C'est une inversion de $U$, et c'est ce qui rend l'utilité espérée comparable à une somme d'argent — sans quoi elle resterait une échelle sans unité. Presque tout ce que le cours mesure ensuite passera par là. [ajout]

## Exemple minimal
Avec $u(x)=\sqrt{x}$ et le pari $(0,\tfrac12;100,\tfrac12)$ : $c=25$. [ajout]

## Geste de calcul type
Calculer $\mathbb{E}[U(\tilde x)]$, puis inverser l’utilité : $c=U^{-1}\big(\mathbb{E}[U(\tilde x)]\big)$. [ajout]

## Cesse d'être valide quand
Il suppose $U$ inversible, donc strictement croissante ; sans cela plusieurs montants certains conviennent. [ajout]

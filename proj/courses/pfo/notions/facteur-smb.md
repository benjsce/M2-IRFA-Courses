---
id: pfo/facteur-smb
nom: Facteur SMB
symbole: '$SMB$, $R_{\mathrm{Small}}$, $R_{\mathrm{Big}}$'
type: notion
statut: source
cas_de: pfo/facteur-de-risque
valeur: trier les entreprises par capitalisation, petites moins grandes
construite_a_partir_de:
- pfo/portefeuille-de-marche
alias:
- SMB
- Small Minus Big
- prime de taille
- size premium
- facteur de taille
refs:
- §4.2.2
- p. 59
---

## Ce que c'est
Le rendement d'un portefeuille de petites capitalisations moins celui d'un portefeuille de grandes capitalisations, sur la même période. [§4.2.2, p. 59]

## Forme
$$SMB=R_{\mathrm{Small}}-R_{\mathrm{Big}}$$ [p. 59]

## Ce que les symboles modélisent
$R_{\mathrm{Small}}$ est le rendement d'un portefeuille d'entreprises de petite capitalisation, $R_{\mathrm{Big}}$ celui d'un portefeuille de grandes ; $SMB$ est leur écart, un rendement, une valeur par période. La forme du cours est simplifiée : elle ne dit ni combien d'entreprises entrent dans chaque groupe, ni où passe la frontière. [p. 59]

## Ce qui la définit
**Connus** : les rendements des petites et des grandes entreprises sur une période. **Cherché** : de combien les petites ont battu les grandes. Une valeur positive dit que les petites capitalisations ont mieux rendu sur la période ; négative, que ce sont les grandes. [p. 59]

Cet écart, souvent positif, s'appelle la prime de taille. On peut le lire comme la rémunération de risques propres aux petites entreprises : une liquidité moindre, une plus grande sensibilité aux conditions de financement, une plus grande vulnérabilité à la conjoncture. [p. 59]

## Le chemin jusqu'ici
Le tri se fait sur la capitalisation, prix de l'action fois nombre d'actions, la grandeur qui pondère pfo/portefeuille-de-marche. Chaque groupe est lui-même un portefeuille dont le rendement est une moyenne pondérée, exacte en pfo/rendement-arithmetique et non en pfo/rendement-logarithmique, comme le rappelle pfo/piege-d-agregation. [ajout]

## Exemple minimal
Un mois où les petites capitalisations font 3 % et les grandes 1 %, $SMB=2\,\%$. [ajout]

## Geste de calcul type
Les données de Kenneth French donnent la série toute faite, en pourcentage : une valeur de 2,50 se lit 0,025 et se divise par 100 avant la régression. [p. 82]

## Cesse d'être valide quand
Il faut distinguer le constat de son interprétation : une prime de taille positive n'implique pas que la surperformance des petites capitalisations rémunère exclusivement leur risque d'illiquidité. [p. 59]

## Origine
- exercice pfo/ex-08 : le coefficient de AAPL sur SMB et sa significativité disent son profil de taille [p. 82, p. 83]

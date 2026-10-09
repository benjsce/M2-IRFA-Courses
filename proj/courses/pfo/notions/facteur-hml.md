---
id: pfo/facteur-hml
nom: Facteur HML
symbole: '$HML$, $R_{\mathrm{High\,B/M}}$, $R_{\mathrm{Low\,B/M}}$'
type: notion
statut: source
cas_de: pfo/facteur-de-risque
valeur: trier les entreprises par ratio book-to-market, élevé moins faible
construite_a_partir_de:
- pfo/portefeuille-de-marche
- fpp/bilan
alias:
- HML
- High Minus Low
- prime de valeur
- value premium
- book-to-market
- Value et Growth
refs:
- §4.2.2
- p. 60
---

## Ce que c'est
Le rendement des entreprises dont le ratio book-to-market est élevé moins celui des entreprises dont il est faible, sur la même période. [§4.2.2, p. 60]

## Forme
$$HML=R_{\mathrm{High\,B/M}}-R_{\mathrm{Low\,B/M}},\qquad \text{Book-to-Market}=\frac{\text{capitaux propres comptables (actifs − dettes)}}{\text{capitalisation boursière}}$$ [p. 60]

## Ce que les symboles modélisent
$R_{\mathrm{High\,B/M}}$ est le rendement d'un portefeuille d'entreprises à book-to-market élevé, $R_{\mathrm{Low\,B/M}}$ celui d'un portefeuille à book-to-market faible ; $HML$ est leur écart, une valeur par période. Le book-to-market rapporte ce que valent les capitaux propres dans les comptes à ce que la bourse paie pour eux. [p. 60]

## Ce qui la définit
**Connus** : le bilan comptable et la capitalisation de chaque entreprise, puis les rendements des deux groupes. **Cherché** : de combien les entreprises que la bourse paie peu, au regard de leurs comptes, ont battu celles qu'elle paie cher. [p. 60]

![Deux entreprises au même bilan : 100 d'actifs, 80 de dette, donc 20 de capitaux propres comptables. La bourse capitalise la première à 25, la seconde à 100. Book-to-market : 20/25 = 0,8, côté High, dite Value ; 20/100 = 0,2, côté Low, dite Growth. Dessous, la Forme : HML = R_High B/M − R_Low B/M.](figures/facteur-hml.svg) [ajout]

Un book-to-market élevé caractérise les entreprises Value, dont la valeur comptable est grande au regard de leur valorisation ; un book-to-market faible, le style Growth, dont la valorisation dépasse de loin la valeur comptable. Un HML positif dit que les Value ont mieux rendu sur la période. Une exposition positive au facteur traduit une orientation Value, une exposition négative une orientation Growth. [p. 60]

## Le chemin jusqu'ici
Le numérateur du ratio vient de fpp/bilan : les capitaux propres sont ce qui reste des actifs une fois la dette déduite, ici lus dans les comptes. Le dénominateur est la capitalisation qui pondère pfo/portefeuille-de-marche, prix de l'action fois nombre d'actions. [ajout]

Chaque groupe est un portefeuille dont le rendement est une moyenne pondérée, exacte en pfo/rendement-arithmetique et non en pfo/rendement-logarithmique, comme le dit pfo/piege-d-agregation. [ajout]

## Exemple minimal
Un mois où les entreprises Value font 0,5 % et les Growth 2,5 %, $HML=-2\,\%$ : ce mois-là, la croissance l'a emporté. [ajout]

## Geste de calcul type
Pour une entreprise de 100 d'actifs et 80 de dette, capitalisée à 25 : capitaux propres comptables $100-80=20$, book-to-market $20/25=0{,}8$. Capitalisée à 100, le même bilan donne 0,2. [ajout]

## Cesse d'être valide quand
Une entreprise dont les dettes dépassent les actifs a des capitaux propres comptables négatifs : son ratio est négatif et le tri n'a plus de sens. [ajout]

Comme pour la taille, l'écart observé ne dit pas à lui seul quel risque il rémunère. [p. 59, ajout]

## Origine
- exercice pfo/ex-08 : le signe du coefficient de AAPL sur HML dit si l'action se comporte en Value ou en Growth [p. 83]

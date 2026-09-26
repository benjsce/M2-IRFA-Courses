---
id: pfo/remplissage-des-valeurs-manquantes
nom: Remplissage des valeurs manquantes
type: notion
statut: source
construite_a_partir_de: []
alias:
- forward fill
- backward fill
- ffill
- bfill
- remplissage avant
- remplissage arrière
refs:
- p. 11
- p. 12
---

## Ce que c'est
Le remplacement de chaque valeur manquante d'une série par la dernière valeur connue avant elle, ou à défaut par la première valeur connue après elle. [p. 11, p. 12]

## Forme
$$\mathrm{NaN} \longrightarrow \begin{cases} \text{dernière valeur connue avant,} & \text{si elle existe,} \\ \text{première valeur connue après,} & \text{sinon.} \end{cases}$$ [p. 12]

## Ce que les symboles modélisent
$\mathrm{NaN}$, « Not a Number », est la marque que pandas pose sur une valeur manquante : une case vide de la série, et non un zéro ni un prix nul. [p. 11]

« Avant » et « après » s'entendent dans l'ordre des dates de la série : la dernière valeur connue avant est une observation passée, la première valeur connue après une observation future. La flèche dit ce que la case reçoit ; ce n'est pas une égalité. [p. 12, ajout]

## Ce qui la définit
Elle enchaîne deux opérations : `ffill()` propage vers l'avant la dernière observation disponible, puis `bfill()` comble en remontant les valeurs manquantes du début de série, que rien ne précède. L'expression `raw_prices.ffill().bfill()` rend ainsi une série sans valeur manquante dès qu'au moins une observation existe. [p. 11, p. 12]

Dans le cours, elle sert à combler les trous de liquidité : les jours fériés propres à chaque place, où une bourse est fermée pendant que les autres cotent. [Listing 1.1]

## Exemple minimal
La série [100, NaN, NaN, 105, NaN, 110] devient [100, 100, 100, 105, 105, 110] après `ffill()`. [p. 12]

## Geste de calcul type
Sur [NaN, NaN, 100, 105, NaN], `ffill()` rend [NaN, NaN, 100, 105, 105] et laisse vides les deux premières valeurs, faute d'observation avant elles ; `bfill()` les remplit ensuite avec 100. [p. 12]

![La série du poly, NaN, NaN, 100, 105, NaN, et d'où vient chaque valeur recopiée. `ffill()` recopie 105 dans la case vide qui le suit ; les deux premières cases, que rien ne précède, restent vides ; `bfill()` y recopie 100, la première valeur connue après elles.](figures/remplissage-des-valeurs-manquantes.svg) [ajout]

## Cesse d'être valide quand
Le `bfill()` du début de série recopie une valeur future dans le passé : dans un backtest, c'est une information que personne ne possédait à cette date. [ajout]

Un prix recopié produit un rendement nul le jour du trou et reporte tout le mouvement sur le jour de la réouverture. Quand l'index réunit des places qui ne cotent pas les mêmes jours — des actions et le Bitcoin, qui cote aussi le week-end —, les actions reçoivent des rendements nuls chaque samedi et chaque dimanche, et leur variance par ligne s'en trouve diluée. [ajout]

---
id: <code>/<slug>
nom: <Nom de la notion>
symbole: "$...$"                      # facultatif ; doit figurer dans notation.yml
type: notion                          # principe | notion | abstraite
statut: source                        # source | ajout
cas_de: <code>/<slug-du-parent>       # facultatif ; jamais pour un principe
valeur: <valeur du paramètre du parent>   # obligatoire si le parent est une abstraite
parametre: <paramètre qui distingue les membres>   # obligatoire si type = abstraite
construite_a_partir_de:
- <code>/<slug>
alias:
- <autre nom>
refs:
- "§x.y"
---

## Ce que c'est
Une phrase, ≤ 220 caractères. [§x.y]

## Forme
$$ ... $$ [§x.y]

## Ce qui la définit
<!-- pour une abstraite : « Ce que les membres partagent », puis « Pourquoi ce niveau existe » -->
... [§x.y]

## Exemple minimal
Une instance chiffrée, une ligne, sans calcul. [ajout]

## Geste de calcul type
Comment on s'en sert, sur un cas, trois lignes. [ajout]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| ... | ... | ... |
[§x.y]

## Cesse d'être valide quand
... [§x.y]

## Origine
- exercice <code>/ex-nn : ce qu'il a révélé [ajout]

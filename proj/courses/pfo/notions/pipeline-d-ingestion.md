---
id: pfo/pipeline-d-ingestion
nom: Pipeline d'ingestion et de filtrage
type: notion
statut: source
construite_a_partir_de:
- pfo/remplissage-des-valeurs-manquantes
- pfo/filtre-z-score-glissant
alias:
- data ingestion pipeline
- market data pipeline
- yf.download
- prix de clôture ajusté
- Adj Close
- garbage in, garbage out
refs:
- p. 7
- §1.3.3
- Listing 1.1
---

## Ce que c'est
La chaîne qui télécharge les prix de clôture ajustés, comble les trous, calcule les rendements logarithmiques et neutralise les rendements aberrants. [Listing 1.1, §1.3.3]

## Ce qui la définit
Le cours la motive par le principe « garbage in, garbage out » : des données d'entrée corrompues produisent des résultats anormaux dans tout modèle en aval, et les données de marché sont asynchrones, incomplètes, bruitées et soumises aux règles du carnet d'ordres. [p. 7]

Le listing 1.1 en fixe les étapes. `yf.download(tickers, start, end)["Adj Close"]` ramène un tableau dont les lignes sont des dates et les colonnes des actifs ; `ffill().bfill()` comble les trous ; `np.log(prices / prices.shift(1)).dropna()` calcule les rendements et retire la première ligne, vide ; le filtre à vingt jours remplace par 0 les rendements de score supérieur à 3. [Listing 1.1, p. 10, p. 11, p. 14]

Le prix de clôture ajusté convient à l'analyse des rendements parce qu'il tient compte des dividendes et des divisions d'actions. [p. 11]

## Le chemin jusqu'ici
Le pipeline enchaîne deux traitements dans un ordre qui compte. pfo/remplissage-des-valeurs-manquantes agit sur les prix, avant tout calcul, pour que chaque date ait une valeur pour chaque actif. [ajout]

Le passage à pfo/rendement-logarithmique vient ensuite, et c'est sur ces rendements seulement que pfo/filtre-z-score-glissant applique pfo/score-z. Inverser l'ordre ne marcherait pas : un prix manquant produit deux rendements manquants, et un filtre n'a rien à dire d'une valeur absente. [ajout]

## Ce qui reste libre
| élément | valeur du cours |
|---|---|
| actifs | Apple, CAC 40, Nikkei 225, Bitcoin en dollars |
| période | du 2022-01-01 inclus au 2026-01-01 exclu |
| fenêtre du filtre | 20 lignes du tableau |
| seuil | 3 écarts types |
| valeur de remplacement | 0 |
[p. 10, p. 11, Listing 1.1]

## Cesse d'être valide quand
Les versions récentes de `yfinance` ajustent les prix par défaut (`auto_adjust=True`) : la colonne `Close` est alors déjà ajustée et `"Adj Close"` n'existe plus, si bien que la ligne du cours échoue. Il faut passer `auto_adjust=False`, ou lire `Close`. [ajout]

Le tableau réunit les dates de toutes les places. Le Bitcoin cotant tous les jours, l'index compte environ 365 lignes par an, et la fenêtre de vingt lignes couvre vingt jours calendaires, pas vingt séances. [ajout]

Les prix ajustés sont recalculés rétroactivement à chaque nouveau dividende : deux exécutions du même script à des dates différentes ne rendent pas exactement les mêmes séries. [ajout]

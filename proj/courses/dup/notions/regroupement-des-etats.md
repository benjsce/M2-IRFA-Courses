---
id: dup/regroupement-des-etats
nom: Regroupement des états
type: notion
statut: source
construite_a_partir_de:
- dup/prix-par-unite-de-poids
alias:
- bunching
- mise en bloc des états
refs:
- L4 slide 31
- L4 slide 33
---

## Ce que c'est
Donner le même paiement à plusieurs états voisins quand l'ordre supposé ne tient pas, et traiter le bloc obtenu comme un seul résultat. [L4 slide 33]

## Forme
$$u'(z)=\eta\,\frac{\sum_{s\in B}q_s}{\sum_{s\in B}\pi_s},\qquad \sum_{s\in B}\pi_s=\varphi(P_b)-\varphi(P_{a-1})$$ [L4 slide 33]

## Ce que les symboles modélisent
$\kappa_s$ est un multiplicateur de Lagrange : il vaut zéro tant que deux états voisins reçoivent des paiements différents, et devient positif quand la contrainte d'ordre mord. Sa valeur n'a pas de lecture économique directe ; c'est son annulation, ou non, qui dit si deux états forment un bloc. [L4 slide 27]

## Ce qui la définit
Quand des états consécutifs $B=\{a,\dots,b\}$ partagent le même paiement $z$, la somme de leurs conditions du premier ordre annule les multiplicateurs internes : il ne reste que le prix total du bloc rapporté à son poids total, pourvu que les contraintes aux bords du bloc ne soient pas actives. [L4 slide 33]

Le poids d'un bloc est le saut cumulé sur tout le bloc, et il ne dépend donc pas de l'ordre interne : des paiements égaux forment un seul résultat, ce qui lève l'indétermination du rang à l'intérieur du bloc. [L4 slide 31]

La méthode générale suit trois temps : proposer un ordre et calculer les poids cumulés qu'il donne ; résoudre le problème concave sous les contraintes d'ordre, en regroupant les états adjacents dont les paiements non contraints violent l'ordre supposé ; comparer enfin les solutions obtenues d'un ordre à l'autre. [L4 slide 33]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite se combinent en dup/utilite-esperee, que dup/rdu déforme par le rang ; dup/poids-de-decision en tire le poids d'un état et dup/portefeuille-rdu pose le programme d'allocation, dont dup/prix-par-unite-de-poids donne la condition du premier ordre. [ajout]

C'est cette condition qui échoue sur l'exemple du cours : l'allocation qu'elle produit renverse l'ordre dont elle est issue. Cette fiche est la sortie de cet échec — on cesse d'espérer un ordre strict et on laisse deux états se confondre. Elle vient donc nécessairement après le rapport prix sur poids, puisqu'elle en répare le mode d'emploi. [ajout]

## Exemple minimal
Sur le marché du cours, les deux mauvais états reçoivent le même paiement : $x^{\mathrm{RDU}}=(0{,}437;0{,}437;1{,}845)$, de valeur 1,0618 contre 1,0405 et 1,0021 pour les autres maxima régionaux. [L4 slide 31]

## Geste de calcul type
Réunir en un bloc les états dont l'ordre est violé, remplacer leurs prix et leurs poids par leurs sommes, résoudre le problème réduit, puis vérifier que l'ordre obtenu entre blocs est bien celui qu'on avait supposé. [L4 slide 33]

## Cesse d'être valide quand
La concavité ne rend les conditions suffisantes qu'à ordre fixé : un ordre cohérent ne prouve pas l'optimalité globale, et il faut comparer les six ordres possibles sur trois états. L'intuition de l'utilité espérée ne survit d'ailleurs qu'à moitié — à états équiprobables, l'optimum donne bien plus de richesse aux états les moins chers, mais avec des probabilités inégales le classement inverse de $q_s/p_s$ peut ne pas tenir. [L4 slide 31, L4 slide 33]

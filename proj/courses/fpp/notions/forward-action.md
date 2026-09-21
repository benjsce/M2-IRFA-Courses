---
id: fpp/forward-action
nom: Prix forward d’une action
symbole: $F(t,T)$
type: notion
statut: source
cas_de: fpp/prix-a-terme
valeur: $\Phi$ selon le dividende, $D=P(t,T)$
construite_a_partir_de:
- fpp/portage
- fpp/facteur-actualisation
refs:
- §3.1
- §3.2
---

## Ce que c'est
Le prix convenu aujourd’hui pour acheter une action à une date future. [§3.1, §3.2]

## Forme
$$F(t,T)=\dfrac{S_t\,\Phi}{P(t,T)}$$ [§3.1, §3.2]

## Ce que les symboles modélisent
$S_t$ est le prix auquel on peut acheter l'action tout de suite ; $F(t,T)$ celui auquel on s'engage aujourd'hui à l'acheter en $T$. Les deux sont connus en $t$ : le prix forward n'est pas une prévision du prix futur, c'est un prix d'aujourd'hui pour une livraison différée. [§3.1, Déf. 8]

## Ce qui la définit
C’est le cas le plus simple du prix à terme : règlement unique, dans la devise du sous-jacent. Tout le contenu propre tient dans $\Phi$. [ajout]

## Le chemin jusqu'ici
Le socle réunit des briques indépendantes. fpp/portage dit ce que coûte ou rapporte la détention du sous-jacent jusqu'à l'échéance ; fpp/facteur-actualisation, construit sur fpp/convention-capitalisation, dit ce que coûte l'argent immobilisé. [ajout]

Le prix forward est le comptant corrigé de ces deux termes, et de rien d'autre. Remarquez ce qui n'est pas dans le socle : aucune probabilité, aucune prévision. Le prix forward n'est pas une anticipation du cours futur. [ajout]

## Exemple minimal
Action à 100, dividende proportionnel de 2 % avant l’échéance, $P(0,1)=0{,}9608$ : $F(0,1)=102{,}00$. [ajout]

## Geste de calcul type
Repérer d’abord la nature du dividende : proportionnel donne $\Phi=1-\sum_i d_i$. Avec 2 % de dividende et $P(0,1)=0{,}9608$, $F=100\times0{,}98/0{,}9608=102{,}00$. [§3.2]

## Cesse d'être valide quand
Suppose le sous-jacent détenable et vendable à découvert sans coût. [ajout]

## Origine
- exercice fpp/ex-02 : la formule se lit dans le sens direct, alors que fpp/ex-01 la lit à l'envers pour retrouver le comptant. Même formule, deux gestes [ajout]
- exercice fpp/ex-05 : geste manquant — lire la formule comme une équation en $D$ pour extraire le **dividende implicite** d'un forward coté. C'est l'usage le plus courant sur le marché [ajout]

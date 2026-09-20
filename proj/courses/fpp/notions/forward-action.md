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

## Ce qui la définit
Cas le plus simple du prix à terme : règlement unique, devise du sous-jacent. Tout le contenu propre tient dans $\Phi$. [ajout]

## Exemple minimal
Action à 100, dividende proportionnel de 2 % avant l’échéance, $P(0,1)=0{,}9608$ : $F(0,1)=102{,}00$. [ajout]

## Geste de calcul type
Repérer d’abord la nature du dividende : proportionnel donne $\Phi=1-\sum_i d_i$. Avec 2 % de dividende et $P(0,1)=0{,}9608$, $F=100\times0{,}98/0{,}9608=102{,}00$. [§3.2]

## Cesse d'être valide quand
Suppose le sous-jacent détenable et vendable à découvert sans coût. [ajout]

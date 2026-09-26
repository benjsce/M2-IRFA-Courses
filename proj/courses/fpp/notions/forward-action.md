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

$\Phi$ est le portage : la part du comptant qui paie l'action livrée en $T$, sans les dividendes versés d'ici là. $P(t,T)$ est le prix aujourd'hui d'un euro payé en $T$. [§3.2, ajout]

## Retrouver la formule
![Les deux jambes du forward, avec deux dividendes proportionnels avant l'échéance. L'acheteur à terme reçoit l'action en $T$ mais pas les dividendes versés avant : ramenée en $t$, sa jambe vaut $S_t\Phi$ avec $\Phi=1-d_1-d_2$, et non $S_t$ ; elle est connue aujourd'hui. La jambe argent, $F(t,T)$ payé en $T$, est le montant cherché ; elle vaut $F(t,T)P(t,T)$ en $t$. Les deux sont égales à la signature, et c'est la formule.](figures/forward-action.svg) [ajout]

Acheter à terme, c'est recevoir une action en $T$ contre $F(t,T)$ payé en $T$. **Connus aujourd'hui** : le comptant $S_t$, les dividendes à venir, donc $\Phi$, et le zéro-coupon $P(t,T)$. **Cherché** : $F(t,T)$. Le contrat ne coûte rien à la signature : il suffit de dire ce que vaut aujourd'hui chacune des deux jambes. [ajout]

Jambe action : les dividendes versés avant $T$ vont à qui détient l'action, pas à l'acheteur à terme. L'action livrée en $T$ vaut donc aujourd'hui le comptant moins ce que valent aujourd'hui ces dividendes. [§3.2]

Avec des dividendes proportionnels, chacun vaut aujourd'hui $d_iS_t$ : l'action livrée en $T$ vaut $S_t-\sum_i d_iS_t=S_t\Phi$, avec $\Phi=1-\sum_i d_i$. [§3.2]

Jambe argent : $F(t,T)$ payé en $T$ vaut aujourd'hui $F(t,T)P(t,T)$. [ajout]

Le contrat ne coûte rien à la signature : les deux jambes valent autant, $F(t,T)P(t,T)=S_t\Phi$. [ajout]

$$F(t,T)=\dfrac{S_t\,\Phi}{P(t,T)}$$ [ajout]

## Ce qui la définit
C’est le cas le plus simple du prix à terme : règlement unique, dans la devise du sous-jacent. Tout le contenu propre tient dans $\Phi$. [ajout]

## Le chemin jusqu'ici
Le socle réunit des briques indépendantes. fpp/portage dit ce que coûte ou rapporte la détention du sous-jacent jusqu'à l'échéance ; fpp/facteur-actualisation, construit sur fpp/convention-capitalisation, dit ce que coûte l'argent immobilisé. [ajout]

Le prix forward est le comptant corrigé de ces deux termes, et de rien d'autre. Remarquez ce qui n'est pas dans le socle : aucune probabilité, aucune prévision. Le prix forward n'est pas une anticipation du cours futur. [ajout]

## Exemple minimal
Action à 100, dividende proportionnel de 2 % avant l’échéance, $P(t,t+1)=0{,}9608$ : $F(t,t+1)=102{,}00$. [ajout]

## Geste de calcul type
Repérer d’abord la nature du dividende : proportionnel donne $\Phi=1-\sum_i d_i$. Avec 2 % de dividende et $P(t,t+1)=0{,}9608$, $F=100\times0{,}98/0{,}9608=102{,}00$. [§3.2]

## Cesse d'être valide quand
Suppose le sous-jacent détenable et vendable à découvert sans coût. [ajout]

## Origine
- exercice fpp/ex-02 : la formule se lit dans le sens direct, alors que fpp/ex-01 la lit à l'envers pour retrouver le comptant. Même formule, deux gestes [ajout]
- exercice fpp/ex-05 : geste manquant — lire la formule comme une équation en $D$ pour extraire le **dividende implicite** d'un forward coté. C'est l'usage le plus courant sur le marché [ajout]

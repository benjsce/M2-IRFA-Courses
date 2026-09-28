---
id: dup/conditions-d-equilibre-de-laibson
nom: Conditions d'équilibre de Laibson
symbole: '$\bar\alpha$, $\bar y$, $\underline y$'
type: notion
statut: source
construite_a_partir_de:
- dup/jeu-des-moi-successifs
- dup/actif-illiquide
alias:
- equilibrium conditions
- conditions P1–P4
- hypothèse A1
refs:
- L5 slide 46
- L5 slide 47
- L5 slide 48
- L5 slide 49
- L5 slide 50
- L5 slide 51
---

## Ce que c'est
Quatre conditions marginales qui caractérisent l'unique équilibre du jeu de consommation avec actifs liquide et illiquide : qui consomme tout son liquide, et quel actif reste vide. [L5 slide 47]

## Forme
Avec $\bar\alpha_t=\max_{\tau>t}(\delta R)^{\tau-t}u'(c_\tau)$ : [L5 slide 48]
$$\begin{aligned}&\text{P1}\quad u'(c_t)\ge\beta\,\bar\alpha_t\\&\text{P2}\quad u'(c_t)>\beta\,\bar\alpha_t\implies c_t=y_t+R\,x_{t-1}\\&\text{P3}\quad u'(c_{t+1})<\bar\alpha_{t+1}\implies x_t=0\\&\text{P4}\quad u'(c_{t+1})>\bar\alpha_{t+1}\implies z_t=0\end{aligned}$$ [L5 slide 47]

## Ce que les symboles modélisent
$\bar\alpha$, écrit $\bar\alpha_t$ quand on le calcule en $t$, est la plus forte utilité marginale à venir, chaque date ramenée en $t$ par $(\delta R)^{\tau-t}$ : ce que rapporterait au mieux un euro épargné aujourd'hui. Le moi $t$ la pèse $\beta$ ; celui de $t+1$, qui la regarde depuis la période d'après, la pèse entièrement. $\bar y$ et $\underline y$ sont les deux revenus des exemples, le haut et le bas. [L5 slide 48, L5 slide 49, L5 slide 50]

## Ce qui la définit
Le connu : revenus, richesse initiale, préférences quasi-hyperboliques de tous les moi. Le trou : ce que chaque moi consomme et place. Sous l'hypothèse A1, $u'(y_t)\ge\beta(\delta R)^{\tau-t}u'(y_\tau)$ pour tout $\tau>t$, le jeu a un unique équilibre parfait, caractérisé par P1 à P4 pour $1\le t\le\tau\le T$, et par $z_T=x_T=0$ : tout est consommé à la fin. [L5 slide 46, L5 slide 47]

P1 et P2 disent que le moi $t$ épargne tant que $\beta\bar\alpha_t$ dépasse son utilité marginale, et qu'autrement il consomme tout son liquide. P3 et P4 disent que ce qu'on destine au moi de demain va en liquide, et ce qu'on destine plus loin, en illiquide, hors de sa portée. [L5 slide 47, L5 slide 48]

A1 et P1, P2 impliquent $c_t\ge y_t$ : aucun moi n'épargne sur son propre revenu. L'hypothèse est restrictive, mais sans elle des gains discontinus apparaissent, comme sans engagement, et les conditions marginales ne caractérisent plus l'équilibre. [L5 slide 46, L5 slide 47]

![L'exemple du revenu qui alterne, avec δR = 1, un rendement brut de 1,1, un revenu de 10 les périodes impaires et de 5 les paires, et une richesse initiale de 20 placée en illiquide. Le revenu, en pointillé, tombe à 5 une période sur deux ; la consommation, en trait plein, ne tombe qu'à 9,2 = 5 + 20 × (1,1² − 1) : chaque moi pair consomme ce que le moi impair lui a laissé en liquide, c_t = y_t + R x_{t−1}.](figures/conditions-d-equilibre-de-laibson.svg) [L5 slide 51, ajout]

## Le chemin jusqu'ici
dup/jeu-des-moi-successifs pose le jeu entre moi, et dup/actif-illiquide les deux actifs et leurs contraintes ; les conditions sont les conditions du premier ordre de ce jeu-là. Elles comparent chaque moi à $\beta$ fois le futur, les poids de dup/actualisation-quasi-hyperbolique, résolus à rebours comme le veut dup/sophistication. [L5 slide 45, L5 slide 47]

L'actif illiquide sert d'engagement parce que dup/coherence-dynamique tombe sous dup/biais-pour-le-present, ce que le plan de dup/engagement-complet ne pouvait voir : ce plan était celui d'un moi seul. En amont, les choix de dup/inversion-des-preferences-dans-le-temps démentent dup/actualisation-exponentielle et violent dup/stationnarite en respectant dup/invariance-temporelle ; tous les moi partagent la dup/utilite-actualisee et les utilités de dup/fonction-utilite. [L5 slide 22, L5 slide 42]

## Exemple minimal
Revenu constant de 10, $R=1{,}1$, $\delta R=1$, richesse initiale 100 répartie en 9,09 de liquide et 90,91 d'illiquide : chaque moi consomme $10+0{,}1\times100=20$, et les placements se reproduisent à l'identique. [L5 slide 49, ajout]

## Geste de calcul type
Calculer $\bar\alpha_t$ sur les consommations candidates ; si $u'(c_t)>\beta\bar\alpha_t$, vérifier que le moi $t$ consomme tout son liquide ; comparer $u'(c_{t+1})$ à $\bar\alpha_{t+1}$ pour savoir lequel des deux actifs le moi $t$ laisse vide. [L5 slide 47, L5 slide 48]

## Cesse d'être valide quand
L'hypothèse A1 échoue, par exemple sous $\delta R=1$ et $u=\log$ quand un revenu futur tombe sous $\beta$ fois le revenu présent : l'équilibre peut perdre l'unicité et les conditions marginales cessent de le décrire. Dans l'exemple alterné, il faut aussi $\underline y+z_0(R^2-1)\le\bar y$ ; sinon la consommation des moi pairs dépasserait celle des moi impairs, et la solution change. [L5 slide 46, L5 slide 50, L5 slide 51]

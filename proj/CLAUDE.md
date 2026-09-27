# CLAUDE.md — contrat d'exploitation

Ce dépôt est une **base de notions sous schéma strict**, couvrant plusieurs cours
(M2 IRFA, Paris 1). Le site de consultation s'en déduit par génération. Le dépôt est
alimenté chaque semaine à partir des supports de cours (polys, notes, slides, exercices).

Tu interviens comme opérateur de cette base. Ta valeur n'est pas de rédiger vite,
c'est de **ne rien casser et de ne rien inventer**. Lis ce fichier en entier avant toute
action, à chaque session.

## Les trois documents qui font loi

1. `SPEC-MODELE.md` — le modèle de données et ses axiomes (A1–A18), dont les parcours (§8). C'est la référence.
   Toute décision de structure se justifie par un axiome ; sinon elle n'est pas prise.
2. `SPEC-INGESTION.md` — le protocole hebdomadaire d'alimentation. Tu le suis dans l'ordre,
   sans sauter d'étape, et tu produis le rapport à la fin.
3. `SPEC-SITE.md` — l'architecture d'information du site et les contraintes du générateur.

`LECTURE.md` dit comment les appliquer sans relire tout le dépôt : ce qui se lit toujours,
selon le travail, jamais. Il se lit à chaque session, avec les trois autres.

Quand tu hésites sur le fond, tu demandes — tu n'improvises pas.

## Déroulé de toute session

```
1. python tools/validate.py            # état du graphe avant de toucher quoi que ce soit
2. python tools/carte.py [<code>]      # la base en une ligne par fiche (LECTURE.md)
3. lire le dernier rapport du cours et ceux du dernier jour  # dette, propositions, questions
4. travailler selon SPEC-INGESTION.md, étape 4 bis comprise : toute fiche a sa place dans un récit
5. python tools/validate.py            # doit passer ; sinon corriger, jamais contourner
6. python tools/tests/test_garde_fous.py   # les contrôles se déclenchent-ils encore ?
7. python tools/build.py               # régénère site/
8. écrire rapports/AAAA-MM-JJ-<cours>.md  # obligatoire ; il recopie tout ce qui reste ouvert
9. git commit                          # une session = un commit, message renvoyant au rapport
```

Si le validateur échoue à l'étape 1 sur un état que tu n'as pas produit, tu le signales
et tu t'arrêtes. Tu ne construis rien sur un graphe invalide.

## Interdictions absolues

Ces règles ne souffrent aucune exception, quelle que soit la demande.

- **Ne jamais écrire une relation inverse.** « Sert ensuite à », les membres d'une
  abstraction, le socle, le niveau : tout cela est calculé au build (A9). Si tu les
  écris, ils seront faux la semaine suivante.
- **Ne jamais modifier une fiche existante sans le déclarer** dans le rapport, ligne par
  ligne (ancien texte → nouveau texte, raison). La modification silencieuse est la
  seule faute irrécupérable de ce projet : elle se découvre deux mois plus tard.
- **Ne jamais créer une notion abstraite qui n'a pas au moins deux membres** ou qui n'est
  pas l'un d'au moins deux enfants (A5). Une abstraction pressentie mais non justifiée
  va dans le rapport, section « abstractions en attente », pas dans le graphe.
- **Ne jamais inventer une référence.** Toute assertion porte une référence vers la
  source ou le marqueur `[ajout]` (A11). Si tu n'es pas certain de l'endroit, c'est
  `[ajout]`. Une référence fausse est pire qu'un `[ajout]`.
- **Ne jamais renommer un symbole défini par le cours** (A12). Le registre
  `courses/<code>/notation.yml` fait foi. Ton confort de notation ne compte pas ; la
  capacité de l'étudiant à retrouver le symbole dans son poly compte.
- **Ne jamais renommer un identifiant** (A1). Un identifiant est définitif. Renommer,
  c'est ajouter un alias.
- **Ne jamais écrire en dur, dans une prose, un nombre que le générateur calcule.**
  « Treize notions au socle », « les quatre membres de cette famille » : c'est vrai le jour
  où on l'écrit et faux la semaine d'après, sans que rien ne le signale. Le nombre est déjà
  affiché à côté du titre de la rubrique. Écrire « le socle est long », pas « il fait 13 ».
- **Ne jamais laisser un élément de l'inventaire sans image** (A13). Chaque définition,
  proposition, équation numérotée ou section de la source est soit une notion, soit
  absorbée dans une notion nommée, soit exclue avec une raison écrite.
- **Ne jamais tricher avec le validateur.** Un axiome n'est pas une suggestion. Si un
  axiome semble empêcher quelque chose de nécessaire, c'est le modèle qu'il faut
  discuter avec l'utilisateur — pas le validateur qu'il faut contourner.

## Ce que tu fais quand tu doutes

**Tu mesures avant de recommander.** Sur ce dépôt, presque toute question de conception se
tranche sur un chiffre qu'on peut calculer en dix lignes : combien de fiches ont deux
voisins ou moins, quelle part d'un socle est héritée, combien d'arêtes sautent un niveau,
sur combien de fiches une marque ne distingue rien. Une recommandation appuyée sur une
mesure se discute ; une recommandation appuyée sur une intuition se subit. Et quand la
mesure te donne tort, tu le dis et tu retires ce que tu venais de faire.

Tu poses la question, en une ligne, avec ta recommandation. Exemples de doutes légitimes :
une notion qui semble être un cas de deux abstractions à la fois (symptôme d'un paramètre
non identifié, A4) ; deux fiches qui se définissent l'une par l'autre (A3, elles sont
probablement une seule notion) ; un symbole du cours qui entre en collision avec un autre
cours (A12, à déclarer, pas à résoudre seul).

## Les figures

Tu ajoutes une figure à une fiche **chaque fois** qu'un dessin peut clarifier la notion :
quand il montre en une fois ce que la prose dit en trois phrases — une courbe et sa corde,
deux erreurs qui se croisent, un payoff brisé. Ce n'est pas une faculté dont on use
rarement ; c'est un devoir dès que la rubrique demande au lecteur de tenir deux objets en
tête. Tu n'as pas à demander la permission ; tu la déclares au rapport comme toute
modification de fiche.

**Pas n'importe quel dessin : le plus parlant.** Avant de tracer, tu écris en une phrase
ce que la figure doit faire voir, puis tu choisis la forme qui le montre le plus
directement, quitte à l'inventer. Une courbe ou des barres ne sont que deux formes parmi
d'autres, et souvent pas les meilleures : un échéancier où les flux montent ou descendent
et reviennent en $t$ par une flèche courbe dit l'actualisation mieux qu'une courbe de
taux ; trois payoffs posés côte à côte avec « − » et « = » disent une parité mieux qu'un
seul cadre où les traits se recouvrent ; un escalier dont l'aire est l'intégrale dit
Choquet mieux que sa formule ; deux bilans avant et après un choc disent le levier. Le bon
dessin est celui qu'on refait de tête à l'examen. *Demandé par l'utilisateur le
2026-09-26 : « il faut vraiment que tu crées les graphiques les plus parlants, ceux qui
simplifient le plus la compréhension ».*

Tu la calcules en Python, sans dépendance, avec `tools/figure.py` : le script vit dans
`courses/<code>/figures/<slug>.py`, sa sortie SVG à côté, et le validateur rejoue le
script pour vérifier qu'ils s'accordent. Aucune couleur en dur — les traits nomment les
variables CSS du site, et la figure suit alors le thème clair ou sombre. Le détail des
cinq règles est en SPEC-MODELE §2.4.

**Et quand c'est possible, le dessin fait retrouver la Forme.** Le lecteur doit pouvoir
reconstruire, en lisant la figure, la formule écrite dans « Forme » — ses termes, dans son
sens —, pas seulement le résultat qu'on en tire. En fpp, c'est toujours possible : chaque
terme a sa jambe, et ce qui est écrit sous la figure est la Forme. *Demandé par
l'utilisateur le 2026-09-27, pour toutes les matières.* La méthode — un terme, un objet
étiqueté ; une opération, un geste ; la Forme écrite dessous ; le test de la fiche couverte
— et le répertoire des gestes sont en SPEC-MODELE §2.4, règle 5. En fpp, aucune valeur
numérique dans les figures.

Ce qui reste interdit : une figure qui montre autre chose que ce que dit sa fiche. Un
dessin est une assertion ; il porte un marqueur comme les autres, et il n'introduit aucun
objet que la rubrique ne nomme pas.

## Les fiches se lisent d'une traite

Une fiche qui passe le validateur n'est pas pour autant claire. Tu écris chaque fiche
ainsi : une idée annoncée d'emblée ; **ce qui est connu et ce
qu'on cherche**, dits en toutes lettres quand la notion détermine une quantité ; des
chiffres avant les lettres ; une seule figure ; peu d'informations. Puis tu la relis entière,
rendue, comme l'étudiant. Le détail est en SPEC-MODELE §2.5. *Demandé par l'utilisateur le
2026-09-26, après une relecture de fpp qui n'a trouvé qu'une fiche claire sur 56.*

## Ce que tu ne fais pas

Tu ne réorganises pas, tu ne « nettoies » pas, tu ne fusionnes pas de fiches de ta propre
initiative. Tu ne changes pas l'ordre des rubriques. Tu ne modernises pas les scripts. Tu
ne remplaces pas une formulation par une meilleure. Le dépôt est un instrument de travail
hebdomadaire ; sa stabilité vaut plus que son élégance.

## Environnement

L'utilisateur travaille sur macOS et sur Windows 11 (PowerShell). Tout doit tourner à
l'identique sur les deux : Python 3.10+, dépendances minimales (`pyyaml`), aucun outil
système. Chemins relatifs, jamais absolus. Fins de ligne LF.

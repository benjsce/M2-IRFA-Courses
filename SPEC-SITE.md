# SPEC-SITE — architecture d'information et générateur

Le site est **généré** depuis `courses/` par `tools/build.py`. Il est statique : des
fichiers HTML dans `site/`, sans serveur. Il s'ouvre en double-cliquant `site/index.html`
et se publie tel quel sur GitHub Pages.

## 1. Le problème à résoudre

Un cours entier compte 100 à 300 notions. Afficher le graphe complet, ou une page
défilante, est inutilisable : la charge de repérage écrase la charge d'apprentissage.
L'architecture d'information sert à une seule chose : **que la personne ne voie jamais
plus que ce qu'elle cherche, et trouve en un clic ce qu'elle cherchera ensuite.**

## 2. Règles de charge cognitive

Ces règles sont des contraintes du générateur, pas des conseils.

1. **Une notion par écran.** La fiche est la page. Tout le reste est à un clic.
2. **Jamais le graphe entier.** Aucune vue ne dessine plus que : le voisinage de dépendance
   à rayon 1 d'une notion, ou l'arbre d'abstraction d'un cours replié au-delà de deux
   niveaux.
3. **Les rubriques dans le même ordre partout**, avec les mêmes intitulés, y compris
   quand elles sont vides (omises, mais jamais réordonnées). La prévisibilité supprime le
   coût de repérage.
   **Deux rubriques générées voisines ne doivent jamais se ressembler si elles portent des
   relations différentes.** La fiche en affiche trois : « cas particulier de » ($A$),
   « construite à partir de » ($D$) et le socle ($D^{+}$). Leur intitulé replié porte la
   distinction — « autre relation », « n prérequis directs », « n prérequis en tout » — et
   l'arête d'abstraction se distingue aussi visuellement des deux autres. Le lien entre les
   deux dernières est énoncé une fois, en français, dans « construite à partir de ».
   *N'a pas marché, et a été retiré* : marquer dans le socle les lignes qui sont des
   dépendances directes. Cela recopiait la section voisine à l'intérieur du socle, et sur
   19 fiches sur 97 toutes les lignes portaient la marque.
4. **Sept éléments par liste au plus.** Au-delà, regrouper (par niveau, par cours, par
   type) et replier les groupes. **L'intitulé d'un groupe porte le périmètre de la liste,
   pas seulement la clé de regroupement.** Trois listes groupent par niveau — « toutes les
   notions », les notions sans famille de la carte du cours, la même liste sous l'arbre —
   et elles écrivaient toutes « niveau 0 (1) ». Un lecteur a lu cela sur une liste filtrée
   et en a conclu que `dup` n'avait qu'une notion de niveau 0 ; il en a dix. Les groupes
   d'une liste filtrée écrivent donc « niveau 0 (1 sans famille) », et la liste dit au-dessus
   combien le cours compte de notions en tout, avec le lien pour les voir toutes.
5. **Divulgation progressive.** À l'ouverture d'une fiche : « Ce que c'est », « Forme »,
   « Ce qui la définit ». Les autres rubriques sont repliées, dans l'ordre, et se
   déplient d'un clic. L'état de pliage est mémorisé par navigateur (`localStorage`).
6. **Le socle est clos, et il le dit.** Lire le socle d'une fiche suffit : aucune de ses
   notions ne renvoie à une notion absente de la liste (SPEC-MODELE §6). La page l'écrit,
   parce que c'est ce qui autorise le lecteur à s'arrêter. Le fait que le niveau soit le
   plus long chemin et non une chaîne se dit là où les niveaux s'expliquent — la carte du
   cours et `aide.html` — et non dans le socle : c'est explicatif, pas actionnable.

7. **Les deux directions de dépendance sont des listes, jamais des graphes.** Le socle
   ($D^{+}$, amont, transitif) et « sert ensuite à » ($D^{-1}$, aval, rayon 1) sont plats,
   ordonnés par niveau croissant, avec un état « déjà su » persistant par navigateur —
   **le même pour les deux, et partagé entre toutes les fiches** — et le compteur
   « n notions, k à voir ». L'asymétrie des deux rayons est voulue : l'amont doit être
   exhaustif parce qu'il faut tout savoir avant, l'aval ne peut pas l'être parce qu'une
   notion fondamentale débloque tout le cours.
8. **Deux relations, deux traitements visuels**, jamais confondus : la dépendance est une
   liste de pastilles ; l'abstraction est un arbre. Aucune arête d'abstraction n'apparaît
   dans une vue de dépendance et réciproquement. Une fiche **mène** à l'arbre, sur sa
   propre carte ; elle n'en dessine jamais un morceau.
9. **Les ajouts sont distinguables et masquables.** Une notion `ajout` ou un paragraphe
   `[ajout]` porte une marque visible ; un interrupteur global les masque ; la projection
   qui reste est valide (A11). **Une rubrique obligatoire (SPEC-MODELE §2.1) dont tout le
   contenu est `[ajout]` ne disparaît jamais silencieusement** : elle reste, et dit que son
   contenu est masqué. Sans cela, masquer les ajouts retire « Cesse d'être valide quand » de
   la majorité des fiches, et le lecteur conclut que la notion n'a pas de limite.
10. **Recherche instantanée** sur nom, alias, symbole, depuis toute page, sans rechargement.
11. **Aucune animation** sauf celles qui répondent à un geste (ouvrir, plier, filtrer).
12. **Aucune page de lecture ne parle du modèle.** Un numéro d'axiome, un nom de fichier
    de spécification, « généré », « au build », « transitif », « rayon 1 », « projection
    stricte », « l'opérateur » : ces mots ne veulent rien dire pour qui n'a pas construit
    cette base, et ils occupent la place de la phrase qui aiderait. Une note générée dit
    **ce que le lecteur doit en faire**, jamais d'où elle vient. Le vocabulaire propre au
    site — niveau, socle, cas particulier de, ajout — n'est défini qu'en un seul endroit,
    `aide.html`, et les pages y renvoient au lieu de se réexpliquer.
    *Mesure du 2026-09-20, avant la règle* : sur les 151 pages produites, **151**
    portaient au moins un de ces termes dans leur texte visible, dont 405 références
    d'axiome et, dans le pied de page de chacune, « généré par `tools/build.py` selon
    `SPEC-SITE.md` … calculées au build (A9) ». Après : 24 pages, dont 11 rapports
    d'ingestion, `aide.html` elle-même, et 12 fiches où le mot est du contenu de cours
    (la *dette* d'un bilan, un *opérateur* de prix, une relation *transitive*).
13. **Ce qui regarde la fabrication est séparé de ce qui regarde la lecture.** Dette,
    fautes de protocole, inventaire, rapports : ces informations restent — elles sont ce
    qui rend la base auditable — mais elles vivent dans un bloc replié, en bas de page,
    qui annonce qu'il ne concerne pas la lecture du cours. Elles ne sont jamais mêlées
    aux notions.

## 3. Les pages

```
site/
  index.html                      sélecteur de cours + recherche globale
  aide.html                       comment lire ce site : le vocabulaire, en un seul endroit
  <code>/index.html               carte du cours : principes, abstractions de niveau 1,
                                  composants sans généralisation, dette ; recherche
  <code>/notions.html             toutes les notions du cours, par niveau, avec les cases
                                  « déjà su » ; la seule page qui les contienne toutes
  <code>/n/<slug>.html            la fiche
  <code>/arbre.html               arbre d'abstraction pliable (replié > 2 niveaux)
  <code>/inventaire.html          la couverture de la source, pour l'audit hebdomadaire
  <code>/exercices.html           les exercices du cours, groupés par section de la source
  <code>/exercices/<slug>.html    énoncé, solution officielle, résolution, fiches touchées
  rapports/<date>.html            les rapports d'ingestion
```

### 3.1 La fiche `<code>/n/<slug>.html`

Dans cet ordre, sans exception :

1. En-tête : nom, symbole, type, cours, niveau, références principales, marque `ajout`,
   et un lien vers l'arbre du cours **visant la carte de cette notion**. Le type, le
   niveau et la marque `ajout` sont eux-mêmes des liens vers la section d'`aide.html`
   qui les définit.
2. Ce que c'est.
3. Forme.
4. Ce qui la définit / Ce que les membres partagent.
5. *(abstraite)* Le paramètre qui les distingue — table membre → valeur, **générée**.
6. *(abstraite)* Pourquoi ce niveau existe.
7. Cas particulier de — une pastille, **générée**, avec la mention « autre relation :
   ce n'est pas un prérequis ».
8. Construite à partir de — pastilles, depuis le front matter.
9. Socle complet — liste **générée**, ordonnée par niveau, cases « déjà su », compteur.
    Amont **transitif** ($D^{+}$) : un plan de lecture, donc exhaustif.
10. Sert ensuite à — liste **générée** ($D^{-1}$), de même forme que le socle : ordonnée
    par niveau, mêmes cases « déjà su », même compteur. Aval à **rayon 1**, jamais
    transitif. Les deux rubriques se suivent : « ce qu'il faut avant » et « ce que ça
    ouvre après » se lisent d'un seul tenant.
11. Exemple minimal.
12. Geste de calcul type.
13. Ce qui reste libre.
14. Cesse d'être valide quand — visuellement distinguée (bordure), c'est la rubrique
    la plus lue.
15. Membres — *(abstraite)* pastilles, **générée** ($A^{-1}$).
16. Origine.

Aucune vue de la fiche ne dessine de graphe : la règle 2 en réserve le droit à l'arbre
d'abstraction, qui a sa page. Un schéma de voisinage à rayon 1 a existé jusqu'au
2026-09-20 ; il a été retiré parce qu'il redessinait exactement « construite à partir de »
et « sert ensuite à », et que 38 fiches sur 47 avaient deux voisins ou moins.

Les pastilles sont des liens. Un lien vers une notion d'un autre cours porte le code du
cours. Un lien vers un id `a-venir` est rendu comme texte barré avec la mention « à
venir », jamais comme lien mort.

### 3.2 bis La liste `<code>/notions.html`

**C'est la seule page qui contienne toutes les notions du cours.** Ni la carte du cours,
qui s'arrête au premier niveau d'abstraction, ni l'inventaire, dont certaines notions ne
sont l'image d'aucun élément, ne les listent toutes ; l'arbre les a toutes mais sous forme
de graphe.

Elle les donne par niveau croissant — donc dans un ordre de lecture possible du cours
entier — avec **les mêmes cases « déjà su » que les socles**, partagées, et un compteur
global. Elle sert à la révision : « ai-je tout vu ? ».

C'est une **destination, pas un passage** : on y accède depuis la carte du cours et depuis
l'accueil, jamais au fil d'une lecture. La règle 1 tient donc : la personne ne voit la
liste entière que lorsqu'elle la demande.

### 3.2 quater La liste `<code>/exercices.html`

Elle n'existe que si le cours a des exercices. Les exercices y sont groupés par section
de la source, dans l'ordre du document, chacun avec sa référence et les pastilles des
notions qu'il met en jeu.

Elle a été ajoutée le 2026-09-20 sur un constat : `courses/fpp/` est passé de 3 à 20
exercices, et **aucune page n'y menait**. On n'y arrivait que depuis la rubrique
« Origine » d'une des 30 fiches qui les citent, ou par la recherche. Un exercice est un
matériau que l'on veut parcourir pour lui-même, pas seulement rencontrer en chemin :
c'est donc une destination, comme `notions.html` (§3.2 bis), et elle est annoncée dans le
bloc d'entrée de la carte du cours.

### 3.2 ter La page `aide.html`

Une page, atteignable depuis l'en-tête et le pied de page de **toutes** les pages. Elle
apprend le site à quelqu'un qui n'a pas construit la base. Son plan est figé, parce que
d'autres pages pointent sur ses ancres : `niveau`, `socle`, `abstraction`, `types`,
`ajouts`, `memoire`, `fabrication`.

Elle est le seul endroit où le site s'explique. Tout ce que les pages de lecture ont
cessé de dire — pourquoi une liste est close, pourquoi « cas particulier de » n'est pas
un prérequis, ce que le filtre des ajouts retire, ce que le site retient du lecteur —
s'y trouve, une fois, en français, avec la comparaison des deux relations en tableau.
La dernière section, `fabrication`, garde ce que le pied de page disait jadis sur toutes
les pages : le schéma, les rubriques recalculées, le validateur, les documents. Qui veut
le savoir le trouve ; les autres ne le lisent plus 151 fois.

### 3.2 La carte du cours `<code>/index.html`

Tout regroupement par niveau, ici comme dans le socle, **explique ce qu'est un niveau** :
le nombre de notions à traverser au plus long pour atteindre celle-ci, donc un ordre de
lecture, ni un degré de difficulté ni un degré d'importance. Sans cette phrase, « niveau 2 »
ne veut rien dire pour le lecteur.

Ce qu'on voit, dans l'ordre : un **bloc d'entrée** qui dit combien de notions compte le
cours et donne quatre chemins selon ce que la personne cherche (découvrir, tout voir,
commencer à lire, voir les familles, s'entraîner sur les exercices, chercher un terme
précis) ; les principes, glosés en une ligne ; pour
chaque principe ses abstractions directes avec leur nombre de membres ; « les autres
notions » (sans `cas_de` et sans type principe) ; enfin, replié et annoncé comme tel, le
suivi de la rédaction (règle 13). Rien d'autre. Le détail est à un clic.

Le bloc d'entrée existe parce que la page ne peut pas se deviner : quatre destinations y
sont accessibles sans qu'aucune soit désignée, et la bonne dépend de ce que la personne
sait déjà du cours.

### 3.3 L'arbre `<code>/arbre.html`

Voir §5 pour l'algorithme. Un seul type d'arête. Replié au-delà de deux niveaux à
l'ouverture. Cliquer un nœud ouvre la fiche. Boutons : tout déplier, tout replier, zoom,
masquer les ajouts. Le canevas se déplace au glisser (souris et tactile). Les nœuds
`ajout` sont marqués. Sous l'arbre : la liste « notions qui n'appartiennent à aucune
famille », qui est une information et non un oubli.

**L'arbre est atteignable depuis toutes les pages d'un cours** : la carte, la liste des
notions, l'inventaire, un exercice, et chaque fiche. Il est un chemin de lecture, pas un
outil de fabrication : il ne va jamais dans le bloc replié de la règle 13.

**Arrivée depuis une fiche.** Le lien porte l'identifiant de la notion (clé `n` du
fragment, §4). À l'ouverture, la page déplie toute la chaîne des parents de cette notion,
encadre sa carte, ajuste l'échelle pour que la racine tienne dans le cadre — sans
descendre sous 0,5, illisible — et l'annonce en une ligne au-dessus du canevas. Centrer
la carte seule ne suffisait pas : cela poussait hors cadre précisément la lignée qu'on
vient voir.

**Et quand la notion n'a pas de carte.** Un nœud n'existe que pour une notion qui a un
parent, des membres, ou le type principe : **48 notions sur 123 — 39 % — n'en ont pas**
(mesure du 2026-09-20). Le lien existe quand même, parce que l'arbre doit être
atteignable de partout, mais il s'intitule alors « arbre du cours » et non « voir dans
l'arbre », et la page d'arrivée nomme la notion, dit pourquoi elle n'y figure pas, ouvre
le groupe replié qui la contient dans la liste du bas et l'y marque. Une notion qui
n'appartient à aucune famille est un fait sur le cours ; le site le dit deux fois plutôt
que de laisser chercher.

## 4. Contraintes du générateur

- **Python 3.10+**, dépendances : `pyyaml` seulement. Un seul point d'entrée :
  `python tools/build.py`. Idempotent. Tourne à l'identique sur macOS et Windows.
- **Le site doit s'ouvrir en `file://`.** Donc : aucune requête `fetch` vers un fichier
  local. Les données d'une page sont incorporées dans la page. L'index de recherche est
  un script inclus dans chaque page ou un unique fichier chargé par balise `<script>`.
- **Formules** : MathJax 3, sortie SVG, chargé depuis un CDN par défaut ; option
  `--offline` qui copie MathJax dans `site/vendor/` pour un usage sans réseau. Les fontes
  du texte sont des fontes système ; aucune dépendance externe autre que MathJax.
- **Une page = un fichier autonome** (CSS et JS inclus), ≤ 300 ko hors MathJax.
- **L'état de lecture traverse les pages par l'URL.** Thème, pliage des rubriques et
  cases « déjà su » suivent la personne d'une page à l'autre. `localStorage` ne peut pas
  le garantir : **mesuré le 2026-09-20**, ouvert en `file://`, Firefox donne à chaque
  document son propre stockage — le profil de l'utilisateur contenait 18 dossiers
  `storage/default/file++++…+site+dup+n+<fiche>.html`, un par fiche visitée. Le thème
  devait donc être rebasculé sur chaque page, et l'affirmation « une case cochée le reste
  sur toutes les fiches », écrite sur 123 pages, était fausse.
  Le générateur écrit donc l'état dans le **fragment** de l'URL et le recopie dans chaque
  lien interne de la page : `#t:d~a:0~p:1-0…~s:<tampon>.<bits>~v:<ancre>`. Un bit par
  notion, six bits par caractère ; l'ordre des bits est celui de `window.ETAT_IDS`, et le
  tampon est calculé dessus — dès qu'une notion entre au dépôt il change, et un lien
  copié la semaine précédente **perd** ses cases au lieu d'en cocher de mauvaises.
  `localStorage` reste, en secours, pour une page rouverte sans fragment.
  Les clés de pliage voyagent par position dans `CLES_PLI` : `sec()` refuse au build une
  clé absente de cette liste, faute de quoi le pliage d'une rubrique nouvelle cesserait
  silencieusement de traverser.
- **Thème clair / sombre** suivant le système, commutable.
- **Responsive** : lisible sur un téléphone en portrait. L'arbre y est utilisable au doigt.
- **Accessibilité minimale** : navigation au clavier, focus visible, contrastes
  suffisants, animations désactivées si `prefers-reduced-motion`.
- **Aucune donnée personnelle** ne quitte le navigateur. `localStorage` sert aux états
  « déjà su », pliage, thème ; tout accès est protégé par `try/catch`.
- **`build.py` échoue si `validate.py` échoue.** Il ne génère jamais depuis un graphe
  invalide.

## 5. L'arbre d'abstraction : algorithme et garantie

Disposition en colonnes par profondeur, cartes de largeur fixe $w$, colonnes espacées de
$c > w$, hauteur des cartes mesurée une fois toutes cartes visibles (une carte masquée
mesure zéro ; on ne mesure jamais une carte masquée), écart vertical $g$.

Pour chaque colonne $d$, une ordonnée $y^{\text{next}}_d$, initialement 0, **jamais
décroissante**. Placement récursif d'un nœud $n$ de profondeur $d$ :

1. si $n$ n'a pas d'enfant visible : $\text{top}(n) = y^{\text{next}}_d$ ;
2. sinon, placer d'abord ses enfants ; soit $m$ le milieu vertical entre le premier et le
   dernier ; $\text{top}(n) = \max\!\big(y^{\text{next}}_d,\ m - h(n)/2\big)$ ; si le
   maximum a joué, soit $\delta$ l'écart : décaler tout le sous-arbre de $\delta$ vers le
   bas et avancer de $\delta$ les $y^{\text{next}}_{d'}$ des seules colonnes $d'$ que le
   sous-arbre occupe ;
3. $y^{\text{next}}_d \leftarrow \text{top}(n) + h(n) + g$.

Les racines sont placées l'une après l'autre, chaque nouvelle racine démarrant sous le
maximum de tous les $y^{\text{next}}$.

**Propriétés garanties**, chacune avec sa raison :
- *Aucune superposition dans une colonne* : les tops d'une colonne sont posés au plus tôt
  à $y^{\text{next}}_d$, avancé de la hauteur après chaque pose ; le décalage d'un
  sous-arbre n'augmente que des écarts et avance les compteurs des colonnes concernées.
- *Aucune superposition entre colonnes* : bandes verticales disjointes puisque $c > w$.
- *Aucune arête ne traverse une carte* : chaque arête est une courbe de Bézier dont les
  points de contrôle ont pour abscisse le milieu de l'entre-colonne ; son abscisse reste
  donc dans la bande vide entre le bord droit du parent et le bord gauche de l'enfant.
- *Parent centré sur ses enfants* : restauré par le décalage exact de l'étape 2.

**Test de propriété obligatoire** (`tools/tests/test_layout.py`, exécuté par `build.py`) :
pour au moins 1 000 configurations de pliage tirées au hasard sur chaque arbre de cours,
et pour 3 jeux de hauteurs aléatoires par configuration, vérifier que (i) tous les
rectangles visibles sont deux à deux disjoints, (ii) l'abscisse de chaque arête est
comprise entre le bord droit de son parent et le bord gauche de son enfant, (iii) chaque
parent visible a son ordonnée entre celles de son premier et de son dernier enfant
visible. Le build échoue si un test échoue. En complément, la page elle-même exécute la
vérification (i) après chaque re-disposition et l'écrit dans la console du navigateur.

Ce que l'algorithme ne garantit pas : la compacité. Un arbre de dix niveaux et deux cents
nœuds est large. C'est pourquoi la règle 2 impose le repli par défaut : la garantie de
non-chevauchement vaut pour toute taille, la lisibilité non.

## 6. Publication

`site/` est commité. GitHub Pages est configuré sur le dossier `site/` de la branche
principale. Le site est alors accessible à une adresse publique depuis n'importe quel
appareil. Un `.nojekyll` vide est présent dans `site/` pour que GitHub ne retraite pas
les fichiers.

## 7. Point d'export prévu (non construit)

`tools/export_cards.py` : pour chaque fiche, produire des germes de cartes (recto proposé,
verso, fiche d'origine) au format attendu par le dépôt de flashcards. Pas dans le
périmètre initial ; l'interface est : une fiche → zéro ou plusieurs germes, jamais
l'inverse.

# Klauss

[![hackmd-github-sync-badge](https://hackmd.io/wklSLzVuQR6UeAmgtLQ77Q/badge)](https://hackmd.io/wklSLzVuQR6UeAmgtLQ77Q)


## nombre de jugadors
Mínim dos jugadors.
Probablement ampliable a 3+ jugadors.

## descripció
### abstracció
Els jugadors adquireixen informació per a resoldre un trencaclosques.

L'adquisició d'informació és a través de diferents mecàniques on els jugadors interactuen amb els elements del joc.

El guanyador és qui aconsegueix tenir prou informació per a resoldre el problema, abans que els altres jugadors.

### tema
  - detectius que resolen un assassinat
  - exploradors o pirates que busquen un tresor
  - aprenents de mag o cuiners que busquen la recepta òptima...???
  - 

### solució 
La solució del problema a resoldre es determina aleatòriament al principi.

La solució està composta de parts d'un trencaclosques. 

Cal que decidim si la solució és única i pre-establerta, o si depèn del transcórrer de la partida. La primera opció és més fàcil i objectiva, però limita les opcions. La segona fa qu el joc sigui una mica més complicat i el fa més difícil d'escalar (jugar-lo amb pocs jugadors).

Cal que les parts lliguin?

Una resposta parcial permet considerar puntuacions que permeten la sensació de proximitat/llunyania a l'èxit: e.g. el jugador x ha quedat a 5% de guanyar.

Una idea: hi ha una sèrie de "condicions inicials" determinades a l'atzar: plovia, hi havia un sopar, era de nit, etc.

Cada sospitós també té una sèrie de coartades o històries, també determinades a l'atzar: estava regant el jardí, estava parlant amb noséqui, etc.

La feina dels investigadors és trobar les discrepàncies entre les històries.

Problema: si les discrepàncies no són 100% objectives, com es decideix qui menteix i com? Ho voten els investigadors? Què hi guanyen?

Seguint amb la idea que proposes: pensava que amb l'ordinador podem fer que es crei una situació on tot lligui. Aleshores superposar-hi les històries vistes per cada un dels personatges, és a dir el que cada un pot saber del que ha passat. I finalment l'assassí té una història que en general coincideix però que en algun punt discrepa amb els altres.

... potser és massa complicat, però crec que m'agradaria mirar-ho una mica més a fons abans de descartar-ho.


## detectius (TBC)
A partir d'aquí assumeixo que el tema són detectius, però crec que hauria de ser possible abstreure'n les idees i canviar-ne el tema si pensem que una altra cosa ens agrada més.

Cada detectiu te una habilitat diferent.

### resum
El personatge X ha desaparegut. Es sospita un assassinat. Alguns detectius han estat contractats i se'ls ha demanat trobar el culpable. El detectiu que pugui demostrar primer qui és l'assassí guanya.

### final
El joc s'acaba quan algun dels detectius pot demostrar qui és l'assassí.
La demostració inclou poder explicar els detalls del cas:
  - Qui ha mort
  - On
  - Com
  - Quan
  - Per què -  motivacio

### mecàniques
Els jugadors descarten cartes de la seva mà per fer accions.

Poden:
- fer l'acció de la carta que descarten, o bé
- fer una acció estàndard.

### fluxe del joc
El joc està estructurat en torns i etapes.
Cada etapa inclou un nombre indeterminat de torns.
 
#### _torns_
Cada torn els jugadors (detectius) fan:
  - selecció d'accions
  - aplicació de les accions seleccionades

##### limitants per a les accions
Cada jugador té un nombre _n_ de _tokens_ per torn.
Cada acció té un cost en tokens.
D'aquesta manera el total d'accions per torn queda limitat i les accions més útils requereixen major nombre de tokens.

Tracking de temps - 
Podem fer que el cost estigui relacionat amb el temps. Fer accions llargues si tenen mes valor o curtes (en temps) si tenen menys valor.


##### accions possibles
Les accions poden ser:
  - moviment
  - proposta de solució
  - requisició d'informació a d'altres jugadors
  - adquisició d'informació d'objectes
  - interacció d'objectes
  - amagar informació

> **AFER** cal especificar el detall per a cada acció possible i com les accions interactuen amb accions d'altres detectius.

###### moviment
Al moure's, un jugador obté informació si arriba a una part no coneguda del mapa. 

El mapa és desconegut a l'inici de la partida. 

###### proposta de solució
En qualsevol (?) moment un jugador pot proposar la solució. Si l'encerta s'acaba el joc i guanya. Si s'equivoca li permet guanyar informació però cal que s'agreguin dificultats al seu joc.

###### interacció amb d'altres jugadors

###### interacció amb elements del joc
###### ocultació d'informació


#### _etapes_
Cada etapa cal aconseguir resoldre part del problema:
  1. Trobar el cos, determinar quan va morir i on va ocorrer l'assassinat
  2. Determinar la causa de la mort i els objectes (armes?) implicats
  3. Determinar qui és l'assassí i quin va ser el motiu


### elements del joc
  - personatges - poden ser morts o vius, poden ser assassins o no
  - objectes - inclou: armes, objectes petits contextuals (e.g. làmpada, got), elements contextuals (e.g. piscina, endoll).
  - llocs: habitacions, parts d'un mapa
  - jugadors/detectius

## detalls per a la implementació

### idees
- en Python?
- array amb ["ocasio",
             "mitjans",
             "motivacio"]
- elements de l'escenari ["llocs", "personatges", "mitjans", "temps", "coartades"]
- ["pistes"]
- Ens cal "tags", que son caracteristiques de tots els elements del joc, i que permeten decidir si certes combinacions son viables o no.
- Els "tags" son informacio que es el que podem anar aconseguint.
- Maneres d'aconseguir dades
    - investigar un lloc
    - interrogar un sospitos
    - investigar l'escenari del crim
    - 
- per a cada element calen restriccions.
- quantificacio en hores
- Que poden fer els investigadors: 
    - 
- llista tancada de sospitosos/personatges (disponible al principi)

### disseny per a la implementació
#### descripció dels elements
##### llocs
El mapa és d'un poblet petit e.g. 10 cases.

Cada casa té uns atributs estàtics.

**idea**: potser per a la narrativa val la pena considerar els camins entre llocs. És a dir, si dos llocs són a distància 1, existeix un camí que els uneix, i per a passar d'un lloc a l'altre cal passar un temps al camí. 

_atributs estàtics_
  - `id_lloc`: un string, possiblement un hash de la resta d'atributs? e.g. "asdf1"
  - `nom_lloc`: un string amb significat, e.g. "botiga", "casa1"
  - `contingut_objectes_estatics`: array d'identificadors d'objectes estàtics 
  - `grandaria`: enter que defineix la grandaria del lloc. Inicialment 1 (petita), 2 (mitjana) o 3 (gran). Defineix el nombre de personatges que hi poden concórrer.
  - `estada_minima`: enter que defineix el mínim nombre d'unitats de temps que un personatge cal que sigui en un lloc.
  - `estada_maxima`: enter que defineix el màxim nombre d'unitats de temps que cal que un personatge **viu** sigui en un lloc.
  - `probabilitat_de_sortir`: nombre aleatori entre 0 i 1 que defineix la probabilitat de que un personatge que és en aquest lloc hi romangui la següent unitat de temps. 
  - `relacions_valides`: taules a considerar per a validar relacions??

_atributs dinàmics_
  - `personatges`: diccionari o array d'arrays que ens mostra per a cada unitat de temps quins personatges són en aquest lloc.
  - `objectes_mòbils`: diccionari o array d'arrays que ens mostra per a cada unitat de temps quins objectes mòbils són en aquest lloc.

##### personatges

_atributs estàtics_
  - `id_personatge`: string, possiblement un hash de la resta d'atributs? e.g. "asdf1"
  - `nom_personatge`: un string amb un nom intel·ligible.
  - `força`: enter entre 1 i 10 (serveix per a definir la capacitat de atacar per força un altre personatge).
  - `intel·ligencia`: enter entre 1 i 10 (serveix per a definir la capacitat d'enganyar)
  - `habilitat`: diccionari amb parelles d'`id_objecte` i un booleà que defineix si el personatge té l'habilitat d'usar l'objecte.
  - `velocitat`: ??? idea ... volem fer que per alguns personatges puguin moure's més que d'altres en el mateix nombre d'unitats de temps?
  - `capacitat`: enter que defineix el màxim d'objectes (segons pes?) que un personatge pot dur en un moment concret.
  - `relacions_valides`: taules a considerar per a validar relacions??

_atributs dinàmics_
  - ``

##### objectes_mòbils

_atributs estàtics_
  - `id_objecte`: string, possiblement un hash de la resta d'atributs? e.g. "asdf1"
  - `nom_objecte`: string intel·ligible e.g. "ganivet", "corda".
  - ``



#### descripció de les relacions possibles
  - `contingut_lloc`: taula amb dues columnes, una amb el `id_lloc` i l'altra amb l'`id_objecte`. Defineix les combinacions de lloc i contingut que són vàlides. 
  - `lloc_lloc`: taula amb tres columnes, `id_lloc_origen`, `id_lloc_destí`, `distancia` (enter). Defineix la dimensió de l'esforç necessari per anar d'un lloc a un altre. 
  - `raons_personatge_lloc`: taula amb les raons per les quals el personatge x pot ser en el lloc y



#### restriccions & _assumptions_
  - dos personatges que concorren en un mateix lloc es veuen - i.e. saben que l'altre personatge era en aquell lloc en aquell moment i poden proporcionar aquesta informació.
  - 




---

## ideas
- players abilities build on as game progresses
- the game is about getting enough information to solve a puzzle, this is achieved by trading information with other players and extracting information from the game world
- the game follows the following mechanics:
	- there are turns
	- each turn is composed of three parts:
		1. Each player decides what they'll do in that turn with the available knowledge they have. This can include providing a solution to the problem
		2. The game evaluates what information each player gets from applying their strategies. The effects can be that a user wins or that a user is no longer able to find a solution.
	
	- there is a unique answer for all players
	- the question to answer is made up of a few parts and some of them may also be composed of other sub parts
	- The results of an action can be to acquire information, to upskill, to win, to lose, to increase the difficulty of the solution (e.g. add extra parts that need to be specified) for you or others, to simplify the solution (to avoid needing to get subparts of the solution) for you or others.
	- Randomness comes with the options you get to prepare in (1), but the evaluation of the effects (2) is deterministic.  
	- A missed attempt to solve the problem hampers the options to win by adding extra complexity to the solution for that player.
	- Complexity in the game must come from the interaction and combination of effects and rules, rather than by having complex rules, elements or mechanics. These three must be as simple as possible.
	- Variables that compose the answer could be:
		- Location (can be used for more than one part of the answer, e.g. where the murder was committed and where the weapon is hidden, escape route)
		- Characters
		- Tools
		- Order in which things happened
		- Objects that affected the action
		- Interactions between characters
		- Quantitative measures - time of the event, force of the impact, speed of xxx
	- A map is likely to be necessary.
	- Theme ideas:
		- crime scene
		- treasure hunt
	- Frame:
		- Colony of animals (ants, bees)
		- Planet, asteroid belt
		- House/mansion/castle
		- Metro
		- Sewers
	- Actions to gather info
		- exchange information with other players
		- explore location
		- move (to get to location)
		- check for combinations of elements: e.g. weapon vs wound, prints vs weapon, character vs prints, etc.
		- players are the detectives? players interact question suspects but also discuss with each other?
		- Can suspects lie? can other detectives lie?
		- 





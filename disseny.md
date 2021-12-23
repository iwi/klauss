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

## detectius (TBC)
A partir d'aquí assumeixo que el tema són detectius, però crec que hauria de ser possible abstreure'n les idees i canviar-ne el tema si pensem que una altra cosa ens agrada més.

### resum
El personatge X ha desaparegut. Es sospita un assassinat. Alguns detectius han estat contractats i se'ls ha demanat trobar el culpable. El detectiu que pugui demostrar primer qui és l'assassí guanya.

### final
El joc s'acaba quan algun dels detectius pot demostrar qui és l'assassí.
La demostració inclou poder explicar els detalls del cas:
  - Qui ha mort
  - On
  - Com
  - Quan
  - Per què

### mecàniques
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


### Elements del joc
  - personatges - poden ser morts o vius, poden ser assassins o no
  - objectes - inclou: armes, objectes petits contextuals (e.g. làmpada, got), elements contextuals (e.g. piscina, endoll).
  - llocs: habitacions, parts d'un mapa
  - jugadors/detectius




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





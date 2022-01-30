# Klauss

[![hackmd-github-sync-badge](https://hackmd.io/wklSLzVuQR6UeAmgtLQ77Q/badge)](https://hackmd.io/wklSLzVuQR6UeAmgtLQ77Q)


## nombre de jugadors
Dos jugadors.

###### **POTENCIAL / DISCUSSIÓ**
  - 3+ caldrà considerar-ne les complexitats en l'intercanvi d'informació.
  - solitari vs. AI

## abstracció
Els jugadors adquireixen informació per a resoldre un trencaclosques.

L'adquisició d'informació és a través de diferents mecàniques on els jugadors interactuen amb els elements del joc.

El guanyador és qui aconsegueix tenir prou informació per a resoldre el problema, abans que els altres jugadors.

## tema
Detectius que resolen un assassinat en un escenari tancat.

## solució 
La solució del problema a resoldre es determina aleatòriament al principi i queda establerta; per tant és estàtica tota la partida.

La solució està composta de parts d'un trencaclosques. 

###### **POTENCIAL / DISCUSSIÓ**
  - Vam considerar i de moment descartar que la solució variés al llarg de la partida. De moment descartada per ser massa complicat. Tot i que podria considerar-se una altra vegada ens va semblar que calia prendre aquesta decisió al principi perquè té implicacions fortes en les decisions de mecànica del joc i en tot el desenvolupament.

La feina dels investigadors és trobar les discrepàncies entre les històries.

Una resposta parcial permet considerar puntuacions que permeten la sensació de proximitat/llunyania a l'èxit: e.g. el jugador x ha quedat a 5% de guanyar.

## plantejament
Hi ha una sèrie de "condicions inicials" determinades a l'atzar: plovia, hi havia un sopar, era de nit, etc.

Cada sospitós també té una sèrie de coartades o històries, també determinades a l'atzar: estava regant el jardí, estava parlant amb noséqui, etc.

Amb l'ajut de l'ordinador es crearà un escenari on tot lligui. Aleshores superposar-hi les històries vistes per cada un dels personatges, és a dir el que cada un pot saber del que ha passat. I finalment l'assassí té una història que en general coincideix però que en algun punt discrepa amb els altres.

## jugadors
Cada jugador és un detectiu que vol resoldre el cas d'assassinat.

Cada detectiu te una habilitat diferent. 

## Relat d'una partida imaginària

Comença la partida. L'escriptor apareix mort al bany de casa seva.  
Els investigadors hi arriben a les 8 AM.

L'investigador Auguste Dupin analitza l'escena del crim per recollir informació. Per exemple:
- Hora probable de la mort (un rang d'hores)
- Causa de la mort
- Instrument de la mort ("arma", o "eina", "verí", etc.).
- Pistes (objectes, empremptes, etc.)

>Aquestes són possibles les opcions que té un invesigador en l'escena de l'asssassinat: investigar hora, causa, instrument, pistes. Investigar-ho porta temps. Caldria evitar que el primer que faci un investigador sigui investigar aquestes 4 coses, i que tothom faci el mateix. Potser es podria fer que quan un investigador descobreix una cosa, tots els que estiguin a la mateixa sala també ho descobreixen (mode multijugador).

Auguste decideix que vol saber l'hora de la mort. Pot intentar esbrinar-ho ell mateix amb la seva habilitat (investigació?), o pot sol·licitar un informe forense. La primera opció li portarà només una estona (1 hora?), mentre que la segona li demana molt més temps (3 hores?).

Auguste utilitza investigació. Té un 7/10 en aquesta habilitat. Com millor sigui la seva tirada, més afinarà el temps. Si falla de molt, no en tindrà ni idea. Si fa una pífia, pot arribar a una conclusió equivocada.

Fa una bona tirada (però ell no ho sap), i el resultat li diu que l'hora de la mort són entres les 2 i les 3 AM.

L'investigador Pare Brown, també va a l'escena del crim, però decideix investigar la causa de la mort. Decideix demanar un informe forense, que triga (3 hores?) però li dóna la certitud que l'escriptor ha mort ofegat sota l'aigua i que té marques de violència, com si algú l'hagués subjectat dins la banyera.

> Això fa pensar que les pistes poden tenir diferents nivells, i que el nivell d'èxit de les tirades fa que es desvetlli més o menys informació. Per exemple, el motiu de la mort pot dir: 1) ofegat, 2) marques de violència, 3) ADN de l'assassí a les ungles.

Auguste decideix interrogar sospitosos, per veure qui podria haver estat a aquella hora al bany.

Brown, en canvi, decideix estudiar tots els sospitosos per veure qui tindria prou força per ofegar la víctima i, probablement, tingui marques o esgarrapades provocades per la víctima.

> Problema: si l'assassinat l'ha de fer algú amb força, pot ser que eliminem molts sospitosos de cop. Potser tampoc és problema, perquè encara cal demostrar-ho. Que un jugador sàpiga massa aviat qui és l'assassí no és problema si encara ho ha de demostrar.

Auguste interroga tots els sospitosos. Els pregunta on eren entre les 2 i les 3 AM de la nit anterior. Tothom li diu que estaven dormint, però ell descobreix que almenys tres menteixen. Com?

La vella li diu que dormia, però quan interroga el rodamón, aquest li diu que va veure llum a casa de la vella a aquella hora. Com arriba a aquesta conclusió?

Quan Auguste interroga el rodamón, li fa diverses preguntes. Ho fa utilitzant la seva habilitat (interrogació?), amb la que hi té un 8/10 i per tant se'n fia bastant. Li pregunta: on eres entre les 2 i les 3AM de la nit anterior? El rodamón diu: al carrer.

> És a dir, que una de les accions dels investigadors és preguntar a un personatge on eren en una determinada hora, o al revés, si han estat en algun lloc en un moment donat.

També li pregunta si va veure alguna cosa estranya. I el rodamón li diu que va veure llum a casa a la vella.

> És a dir, que l'investigador li pot preguntar a un personatge si en un lloc i una hora determinades, ha estat en contacte (visual o físic), amb un altre personatge. Això implica que l'ordinador "sàpiga" que el rodamón ha vist llum a casa a la vella a aquella hora. Com? Llocs que "es toquen"?

Brown, per la seva banda, interroga sospitosos per trobar els forts. Utilitza la seva habilitat (insight?). 

> Els investigadors tenen una acció que és "calibrar" un personatges, que vol dir descobrir algunes de les seves "etiquetes". Poden mirar d'esbrinar si en tenen una de determinada (més fàcil), o saber quines tenen en general (més difícil i atzarós).

Després d'unes hores d'investigació (cada acció consumeix una hora?), Tant Auguste com Brown tenen tres sospitosos. Auguste té una persona sense coartada i dues que menteixen.

> Els personatges han de tenir un element coartada, que pot ser falsa o certa.

Brown té tres personatges que són forts i per tant poden haver comès l'assassinat.

> En aquest moment, si Auguste i Brown comparteixen informació, podrien saber qui és l'assassí creuant els tres de l'un i els tres de l'altre, si només un coincideix.

Els dos investigadors comparteixen la informació (cal una acció "compartir informació"), de manera que tots dos ja saben qui és l'assassí. 

> Brown podria fer una anàlisi d'ADN del cadàver per acusar l'assassí, però això no es pot fer sense proves. En tot cas, només es pot fer una anàlisi així amb una persona, no s'hi val a fer anàlisis a tothom per resoldre un cas. En quin moment es pot fer una anàlisi d'ADN?

Auguste decideix tornar a l'escena del crim i buscar-hi empremptes de l'assassí.

> No es poden buscar empremptes en general, cal buscar-les d'una persona en concret. Es podria "trencar el joc" fent 10 accions seguides de buscar empremtes? Com evitar-ho? Perquè porten molt de temps? Necessites proves prèvies? Potser per buscar proves primer cal tenir pistes...

Brown per la seva banda decideix registrar la casa de l'assassí quan no hi és, i hi troba les joies de la víctima.

> Algunes pistes han de tenir la categoria de prova i són les que fan guanyar. Podem fer-ho qualitativament (això és pista, això és prova) o per acumulació (calen tres pistes per tancar algú).

Els dos han resolt el cas, però el que ho ha fet primer guanya.

> No hi he posat cap pista falsa. Si un investigador falla per molt una tirada, pot arribar a conclusions falses.

> Potser cada sospitós ha de tenir un "estatus": innocent, sospitós, assassí, investigat... Aquest estatus es fa automàticament, no el posa el jugador. Si un jugador vol fer un anàlisi d'empremtes a un sospitós, ha d'aconseguir que tingui un estatus d'investigat, per exemple, i només ho pot aconseguir acumulant pistes: mentides, objectes, falta de coartada, etc.


###### **A FER**
  - Cal estudiar a fons quines habilitats poden tenir in de quina manera afectaran la manera en la que els jugadors obtenen informació. @rogerG quines idees en tens?

## final
??? El joc s'acaba quan algun dels detectius pot demostrar qui és l'assassí.
La demostració inclou poder explicar els detalls del cas:
  - Qui és l'assassí
  - Per què -  motivacio
  - Qui ha mort (o això ja se sap?)
  - On
  - Com
  - Quan
  
###### **A FER**
  - Cal decidir quins aspectes cal proporcionar com a solució. Només el nom de l'assassí? o també detalls sobre la motivació, la forma d'assassinar, etc.


## mecàniques
El joc està estructurat en **accions**, **torns** i **etapes**.  
Cada etapa inclou un nombre indeterminat de torns i cada torn un nombre d'accions.

###### **A FER**
  - Decidir si cal limitar el nombre de torns.
  - Decidir si tenir els dos nivells "etapa" i "torn" val la pena.
 
### _etapes_
Cada etapa cal aconseguir resoldre part del problema:
  1. Trobar el cos, determinar quan va morir i on va ocórrer l'assassinat
  2. Determinar la causa de la mort i els objectes (armes?) implicats
  3. Determinar qui és l'assassí i quin va ser el motiu

###### **A FER**
  - Què determina una etapa?
  - Com de llarga és una etapa?
  - Guanyar etapes determina el resultat final del joc?

### _torns_
Cada torn els detectius fan:
  - selecció d'accions
  - aplicació de les accions seleccionades

Després de cada torn s'avalua la situació.

### limitant d'accions per torn/etapa
Els jugadors disposen de **tokens** que representen el cost de fer les accions.  
Cada jugador té un nombre _n_ de _tokens_ per torn.  
Cada acció té un cost en tokens.  
D'aquesta manera el total d'accions per torn queda limitat i les accions més útils requereixen major nombre de tokens.  


###### **A FER**
  - Cal calibrar el cost de les accions per a fer el joc interessant i dinàmic.

###### **POTENCIAL / DISCUSSIÓ**
  - Els tokens poden estar relacionats amb el pas del temps, de manera que l'ús dels tokens sigui una forma d'expressar que determinades accions impliquen més temps.  
  - @rogerG vas mencionar el concepte de "cartes" - no l'acabo d'entendre, 
> Els jugadors descarten cartes de la seva mà per fer accions.
> Poden:
>  - fer l'acció de la carta que descarten, o bé
>  - fer una acció estàndard.

### _accions_ 
Les accions que poden fer els investigadors/detectius poden ser:
  - moviment? 
  - proposta de solució
  - requisició d'informació a d'altres jugadors
  - adquisició d'informació d'objectes via anàlisi directa o fent dos objectes interactuar.
  - amagar informació
  - ...

###### **A FER**
  - cal especificar el detall per a cada acció possible i com interactuen les accions d'un detectiu amb les dels altres.
  - moviment - cal acordar si volem que els detectius es moguin o si poden investigar sense haver de passejar-se pel mapa.
  - considerar si calen d'altres accions possibles

#### moviment
Al moure's, un jugador obté informació si arriba a una part no coneguda del mapa. 

El mapa és desconegut a l'inici de la partida. 


###### **A FER**
  - Els aspectes de la secció _moviment_ cal discutir-los - no tinc clar si és millor que el mapa sigui conegut de bon principi.
  - Una opció seria que quins llocs hi ha sigui conegut, però on estan situats no?

#### proposta de solució
En qualsevol (?) moment un jugador pot proposar la solució. Si l'encerta s'acaba el joc i guanya. Si s'equivoca li permet guanyar informació però cal que s'agreguin dificultats al seu joc.

#### interacció amb d'altres jugadors
> a escriure

#### interacció amb elements del joc
> a escriure

#### ocultació d'informació
> a escriure

## escenari
La idea és que donats uns elements inicials del joc (personatges, llocs i objectes, i rang temporal), es crei un escenari on per a cada unitat temporal en el rang quedi determinat on és cada element i en quina situació està.

Existeixen restriccions en les relacions dels elements del joc. És a dir casos impossibles que l'escenari no pot acceptar.

La determinació de l'escenari del joc es crearà iterativament de manera que es validi que les restriccions del joc es compleixen.

Les etapes de creació de l'escenari cal validar-les i després automatitzar-les. En principi, esperem que les iteracions vagin de més restrictives i importants per al joc a les més flexibles i possiblement intrascendents per al resultat.

Per a descriure l'escenari cal determinar:
  1. el mort
  2. on ha mort
  3. en quin moment ha mort
  4. on ha estat abans de morir
  5. quin ha estat la manera d'assassinar (mètode, arma, causa de la mort)
  6. qui ha estat l'assassí
  7. si el cadàver ha estat traslladat - on, quan i per qui (l'assassí?)
  8. on ha estat l'assassí abans de l'assassinat
  9. on ha estat l'assassí després de l'assassinat
  10. on s'ha deixat/amagat l'arma
  11. on han estat la resta de personatges durant tot el rang de temps
  12. on són tots els objectes durant tot el rang de temps (i qui els ha mogut)
  
### elements del joc

Cal una llista de
  - [x] personatges - poden ser morts o vius, poden ser assassins o no
  - [x] objectes - inclou: armes, objectes petits contextuals (e.g. làmpada, got), elements contextuals (e.g. piscina, endoll).
  - [x] llocs: cases en un mapa
  - [x] jugadors/detectius
  - [x] accions que poden fer els investigadors (veure secció d'accions)
  - [x] habilitats especials dels investigadors
  - [ ] rang de temps i unitats de temps
  - [ ] motius per assassinar?
  - [ ] maneres d'assassinar


### llocs
El mapa és d'un poblet petit e.g. 10 cases.

Cada casa té uns atributs estàtics.

###### **POTENCIAL / DISCUSSIÓ**
  - Potser per a la narrativa val la pena considerar els camins entre llocs. És a dir, si dos llocs són a distància 1, existeix un camí que els uneix, i per a passar d'un lloc a l'altre cal passar un temps al camí. 

_atributs estàtics_
  - `id_lloc`: un string, possiblement un hash de la resta d'atributs? e.g. "asdf1"
  - `nom_lloc`: un string amb significat, e.g. "botiga", "casa1"
  - `contingut_objectes_estatics`: array d'identificadors d'objectes estàtics 
  - `grandaria`: enter que defineix la grandària del lloc. Inicialment 1 (petita), 2 (mitjana) o 3 (gran). Defineix el nombre de personatges que hi poden concórrer.
  - `estada_minima`: enter que defineix el mínim nombre d'unitats de temps que un personatge cal que sigui en un lloc.
  - `estada_maxima`: enter que defineix el màxim nombre d'unitats de temps que cal que un personatge **viu** sigui en un lloc.
  - `probabilitat_de_sortir`: nombre aleatori entre 0 i 1 que defineix la probabilitat de que un personatge que és en aquest lloc hi romangui la següent unitat de temps. 
  - `relacions_valides`: taules a considerar per a validar relacions??

_atributs dinàmics_
  - `personatges`: diccionari o array d'arrays que ens mostra per a cada unitat de temps quins personatges són en aquest lloc.
  - `objectes_mòbils`: diccionari o array d'arrays que ens mostra per a cada unitat de temps quins objectes mòbils són en aquest lloc.

---
### personatges
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

#### exemples de personatges 
- La vella darrera la cortina: "mentidera", "xafardera", "casolana", "lenta" [tortuga].
- El rodamón: "covard", "necessitat", "nòmada", "pobre", "idealista". [cranc ermità]
- L'escriptor: "observador", "tranquil", "hàbil" [ós].
- La jugadora: "endeutada", "inquieta", "xerraire", "mentidera" [serp].
- L'empresària: "adinerada", "ambiciósa", "intel·ligent", "mentidera" [llop].
- L'estudiant:   
    ["força": CERT,  
    "intel·ligència": CERT,  
    "velocitat": CERT,  
    "diners": FALS,  
    "destresa": CERT,  
    "nocturnitat": CERT,  
    "animal identificador": "pop"]
- L'estrangera o forana  
    ["força": FALS,  
    "intel·ligència": CERT,  
    "velocitat": CERT,  
    "diners": CERT,  
    "destresa": CERT,  
    "nocturnitat": CERT,  
    "animal identificador": "mosca"]
- El predicador  
    ["força": FALS,  
    "intel·ligència": CERT,  
    "velocitat": FALS,  
    "diners": FALS,  
    "destresa": CERT,  
    "nocturnitat": FALS,  
    "animal identificador": "lloro"]  
- El científic [guineu]  
    ["força": FALS,  
    "intel·ligència": CERT,  
    "velocitat": FALS,  
    "diners": FALS,  
    "destresa": CERT,  
    "nocturnitat": CERT,  
    "animal identificador": "pop"]  
    
 

| Personatge | animal       | força | intel·ligència | velocitat | diners | nocturnitat | destresa |
|:---------- |:------------ |:-----:|:--------------:|:---------:|:------:|:-----------:|:--------:|
| Vella      | tortuga      |  No   |       Sí       |    No     |   Sí   |     No      |    No    |
| Rodamon    | cranc ermità |  No   |       No       |    No     |   No   |     No      |    Sí    |
| Jugadora   | serp         |  No   |       Sí       |    No     |   No   |     Sí      |    Sí    |
| Escriptor  | ós           |  No   |       Sí       |    No     |   No   |     Sí      |    Sí    |
| Empresària | llop         |  No   |       Sí       |    Sí     |   Sí   |     No      |    No    |
| Estudiant  | pop          |  Sí   |       Sí       |    Sí     |   No   |     Sí      |    No    |
| Estrangera | mosca        |  Sí   |       No       |    Sí     |   Sí   |     Sí      |    Sí    |
| Predicador | lloro        |  No   |       Sí       |    No     |   No   |     No      |    No    |
| Científic  | guineu       |  No   |       Sí       |    No     |   No   |     Sí      |    Sí    |
| Botiguer   | mosquit      |  No   |       No       |    No     |   Sí   |     No      |    Sí    |
| Cuiner | ratolí      |  No   |       Sí      |    No     |   No   |     Sí      |    Sí    |

###### **A FER**
  - Calcular la distància entre elements (personatges, objectes, llocs) la distància depèn de les difrències/similituds entre elements. Cal que tots els personatges siguin diferents en alguna característica?
    
### objectes_mòbils

_atributs estàtics_
  - `id_objecte`: string, possiblement un hash de la resta d'atributs? e.g. "asdf1"
  - `nom_objecte`: string intel·ligible e.g. "ganivet", "corda".
  - ``

#### exemple d'objectes
- La pistola: "arma", "fàcil", "il·legal", "soroll".
- El martell: "eina", "força".
- El verí de rates: "neteja", "ingestió", "mortal".
- El fals graó: "trampa", "difícil", "localitzat", "ineficaç".
- La serra a motor: "eina", "força", "soroll".
- La gilette: "eina", "habilitat", "difícil".

| Objecte              | causa mort per ... | cal força | cal destresa | sospitós | parany / cal intel·ligència | ràpid | sorollós | cal sigil | efectiu |
|:-------------------- |:------------------ |:---------:|:------------:|:--------:|:---------------------------:|:-----:|:--------:|:---------:|:-------:|
| pistola              | ferida             |    No     |      No      |    Sí    |             No              |  Sí   |    Sí    |    Sí     |   Sí    |
| martell              | contusió           |    Sí     |      No      |    No    |             No              |  Sí   |    No    |    Sí     |   Sí    |
| verí                 | falla vital        |    No     |      No      |    Sí    |             Sí              |  No   |    No    |    No     |   Sí    |
| fals graó            | contusió           |    No     |      Sí      |    No    |             Sí              |  Sí   |    Sí    |    Sí     |   No    |
| serra motora         | ferida             |    Sí     |      No      |    No    |             No              |  Sí   |    Sí    |    No     |   Sí    |
| ganiveta             | ferida             |    No     |      Sí      |    No    |             No              |  Sí   |    No    |    Sí     |   No    |
| corda                | ofec               |    Sí     |      No      |    No    |             No              |  Sí   |    No    |    Sí     |   No    |
| explosiu             | ferida             |    No     |      Sí      |    Sí    |             Sí              |  Sí   |    Sí    |    No     |   No    |
| làmpara              | contusió           |    Sí     |      No      |    No    |             No              |  Sí   |    No    |    Sí     |   No    |
| habitació congelador | falla vital        |    No     |      No      |    No    |             Sí              |  No   |    No    |    No     |   No    |
| estatueta            | contusió           |    Sí     |      No      |    No    |             No              |  Sí   |    No    |    Sí     |   No    |
| bossa de plàstic     | ofec               |    Sí     |      Sí      |    No    |             No              |  Sí   |    No    |    Sí     |   Sí    |
|                      |                    |           |              |          |                             |       |          |           |         |

### llocs

#### exemples de llocs
- La cuina: "foc", "droga", "electricitat".
- El garatge: "eina", "electricitat", "droga", "neteja".
- El bany: "aigua", "electricitat", "neteja".
- 

| Lloc                 | amagar? | matar sense objectes? | # portes | visible de cases contígues? | màxim persones | entrada lliure |
|:-------------------- |:-------:|:---------------------:|:--------:|:---------------------------:|:--------------:|:--------------:|
| Casa de <personatge> |   Sí    |          No           |    2     |             No              |       3        |       No       |
| Hotel                |   Sí    |          No           |    3     |             No              |       5        |       Sí       |
| Botiga               |   No    |          No           |    1     |             No              |       3        |       Sí       |
| Metge                |   No    |          No           |    1     |             No              |       2        |       Sí       |
| Restaurant           |   Sí    |    Sí (congelador)    |    1     |             No              |       5        |       Sí       |
| Piscina              |   No    |     Sí (piscina)      |    1     |             Sí              |       5        |       Sí       |
| Parking              |   No    |       Sí (fum)        |    2     |             Sí              |       4        |       Sí       |


### descripció de les relacions possibles
> [name=iwi][time=Sun, Jan 23, 2022 2:54 PM] una prova de comentari en markdown :grin: 
    
  - `contingut_lloc`: taula amb dues columnes, una amb el `id_lloc` i l'altra amb l'`id_objecte`. Defineix les combinacions de lloc i contingut que són vàlides. 
  - `lloc_lloc`: taula amb tres columnes, `id_lloc_origen`, `id_lloc_destí`, `distancia` (enter). Defineix la dimensió de l'esforç necessari per anar d'un lloc a un altre. 
  - `raons_personatge_lloc`: taula amb les raons per les quals el personatge x pot ser en el lloc y

### restriccions & _assumptions_
  - dos personatges que concorren en un mateix lloc es veuen - i.e. saben que l'altre personatge era en aquell lloc en aquell moment i poden proporcionar aquesta informació.
  - 

---
---
### idees
pistes i proves -
    - evidencia - calen objectes/proves que demostrin ...
    - 
    com fer-ho?

    
    
    
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





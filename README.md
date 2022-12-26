# Klauss

## Abstracció del joc
Hi ha hagut un assassinat. El culpable ha deixat $n$ pistes que l'inculpen. La resta de sospitosos ($s_i$) han deixat $m$ ($<< n$) de les mateixes pistes que els inculpen. Hi ha $k$ llocs i en cada lloc hi ha $n_k$ pistes que inculpen al culpable i poden o no inculpar a daltres sospitosos.

La utilitat d'una pista pot ser:
  1. determinant - la pista només apunta al culpable
  2. útil - la pista apunta a menys del p% dels sospitosos
  3. soroll - la pista apunta a més del q% dels sospitosos

Ens calen els següents passos ...

  _Preparació de l'escenari_
  1. generar el culpable
  2. generar les pistes per a cada lloc
    - generar la utilitat de les pistes
    - generar les pistes segons la seva utilitat

_Simulació de la investigació_
  3. donat un lloc escollir les pistes que hi pot trobar l'investigador.
  4. escollir d'entre les pistes trobades
  5. simular la investigació de les pistes
    - emmascarar les pistes amb probabilitats
    - acumular les troballes
  6. comprovar/refinar la investigació d'alguna pista (pendent)


## Pendents
Ens cal definir quin temps hi ha disponible i quina és la despesa de temps durant la investigació.

Ens cal considerar quin efecte tenen les habilitats dels investigadors en la seva capacitat de trobar/investigar pistes.



## Creació de pistes, investigadors i llocs
Disposem de generadors de $llocs$, $pistes$ i $investigadors$.

Amb aquestes peces podem crear un escenari.

Ens cal definir:

  - `n_sospitosos`: enter que determina el nombre de sospitosos.
  - `utilitats`: diccionari amb tres claus `determinant`, `util` i `soroll` el valor de les quals representa la probabilitat que una pista apunti a d'altres sospitosos a més a més del culpable.
  - `distribucio_nivell_emmascaracio`: diccionari amb dues claus `veritat` i `mentida` llurs valors representen la probabilitat que l'emmascaració retorni el valor cert o fals. La suma dels dos valors cal que sigui igual o menor a 1. En cas de ser menor a 1, la probabilitat restant cau a que la investigació sigui 'inconcloent'.

### Llocs
Els llocs es creen amb
- un nom
- un tipus
- unes coordenades al mapa

Cada lloc rep un identificador únic.

### Pistes
Les pistes només es poden crear dins d'un lloc. Per tant cal primer crear un lloc per a poder crear una pista.

Les pistes es creen amb:
- un nom
- un nivell d'utilitat
- un nombre de sospitosos a qui pot apuntar
- un culpable a qui cal que apunti
- informació sobre els nivells d'utilitat.

Com que cada pista cal que estigui lligada a un lloc, el lloc on ha estat creada esdevé una propietat de la pista.

A més a més cada pista té un identificador únic.

Les pistes poden:
- ser mostrades `mostra_pista()`
- ser emmascarades `emmascara()`


### Investigadors
Un investigador ...

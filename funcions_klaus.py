# Funció per a crear sèrie de pistes

# Dependencies
import random
import numpy as np

# Funcions

# Creació del culpable
def crea_culpable(nombre_de_sospitosos):
    """ Crear una llista on tots els elements són falsos menys un
    S'enten que el culpable és l'element True.
    """
    culpable = random.choice(range(nombre_de_sospitosos))
    respostes_reals = np.array(np.zeros(nombre_de_sospitosos), dtype=bool)
    respostes_reals[culpable] = True
    return respostes_reals, culpable.

# Creació de les pistes
def genera_utilitat_pistes(n_pistes):
    """ Crear una llista de la dificultat de les pistes.
    """
    utilitat_pistes = []
    for pista in range(n_pistes):
        dificultats = ['determinant',
                       'util',
                       'soroll']
        dificultat = random.choice(dificultats)
        utilitat_pistes.append(dificultat)

    return utilitat_pistes

def genera_pista(n_sospitosos, culpable, utilitat_pista, utilitats):
    """ Crea un array de si una pista apunta o no a cada sospitós.
    """
    pista_sospitosos = []
    for sospitos in range(n_sospitosos):
        if sospitos == culpable:
            indicador = True
        else:
            prob = random.uniform(0, 1)
            indicador = prob < utilitats[utilitat_pista]
        pista_sospitosos.append(indicador)

    return pista_sospitosos

# Investigació de les pistes
def aplicar_sort(realitat, probabilitats):
    """ Donada una realitat determinar què ens dirà la pista.
    La decisió de la pista és aleatòria amb probabilitats determinades per la
    variable `probabilitats`.

    @param `realitat`: Un booleà, o bé `True` o bé `False`.
    @param `probabilitats`: Un array amb tres valors que sumen 1. El primer
    correspon a 'veritat', el segon a 'inconcloent' i el tercer a 'mentida'.

    @return Un booleà amb la resposta.
    """
    sort = random.choices(population = ['veritat', 'inconcloent', 'mentida'],
                          weights = probabilitats)[0]
    if sort == 'veritat':
        return realitat
    elif sort == 'inconcloent':
        return None
    else:
        return not(realitat)

def generar_respostes(respostes_reals, probabilitats):
    """
    """
    respostes_modificades = map(lambda x: aplicar_sort(x, probabilitats), respostes_reals)
    return list(respostes_modificades)

def bool_a_int(array_boolea):
    """ Converteix els elemnts d'un array de booleans en 0s i 1s.
    True -> 1
    False -> 0
    None -> 0
    """
    return [1 if x else 0 for x in array_boolea]
    # return [None if x == None else 1 if x else 0 for x in array_boolea]  # alternativa per si cal retornar quelcom diferent per a None que per a False

def comptar_acumulat(llista_de_respostes):
    """ Compta el nombre de True per a cada columna d'una matriu.
    """
    llista_enters = list(map(bool_a_int, llista_de_respostes))
    llista_enters_transposada = np.transpose(llista_enters)
    total = list(map(lambda x: sum(x), llista_enters_transposada))
    return total

def generar_llista_de_respostes(n_preguntes, respostes_reals, probabilitats):
    """ Generar respostes modificades en base a les respostes reals i les probabilitats.
    """
    llista_de_respostes_modificades = []
    for pregunta in range(n_preguntes):
        respostes_modificades = generar_respostes(respostes_reals, probabilitats)
        llista_de_respostes_modificades.append(respostes_modificades)

    return llista_de_respostes_modificades
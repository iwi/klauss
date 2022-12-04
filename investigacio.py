# Investigació

# Dependencies
import random
import numpy as np

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
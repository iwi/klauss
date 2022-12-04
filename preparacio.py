# Set up del joc

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
    return respostes_reals, culpable

# Creació de les pistes
def genera_utilitat_pistes(n_pistes, proporcio_utilitats):
    """ Crear una llista de la dificultat de les pistes.
    """
    utilitat_pistes = []
    for pista in range(n_pistes):
        dificultats = ['determinant',
                       'util',
                       'soroll']
        dificultat = random.choices(population = dificultats,
                                    weights = proporcio_utilitats)
        utilitat_pistes.append(dificultat)

    return sum(utilitat_pistes, [])

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
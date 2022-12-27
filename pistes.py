# Dependencies
import random
import numpy as np
import uuid

class Pista():
    """Tipus pista

    """

    def __init__(self, nom, utilitat, n_sospitosos, lloc, culpable, utilitats):
        self.id = uuid.uuid1()
        self.nom = nom
        self.utilitat = utilitat
        self.lloc = lloc
        self.n_sospitosos = n_sospitosos
        self.investigada = False
        self.culpable = culpable
        self.indicadors = self.__genera_indicadors(utilitats)

    def __genera_indicadors(self, utilitats):
        """ Crea un array de si una pista apunta o no a cada sospitós.
        """
        indicadors = []
        for sospitos in range(self.n_sospitosos):
            if sospitos == self.culpable:
                indicador = True
            else:
                prob = random.uniform(0, 1)
                indicador = prob < utilitats[self.utilitat]
            indicadors.append(indicador)

        return(indicadors)

    def __str__(self):
        """Mostra els detalls de la pista
        Fent ús del mètode màgic __str__ fem que print() funcioni per a imprimir objectes de tipus pista.

         https://www.pythontutorial.net/python-oop/python-__str__/
         https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html
        """
        return "Id: {} \n".format(self.id) +\
               "Nom: {} \n".format(self.nom) +\
               "Utilitat: {} \n".format(self.utilitat) +\
               "Lloc: {} \n".format(self.lloc) +\
               "Indicadors: {} \n".format(self.indicadors) +\
               "Investigada?  {} \n".format(self.investigada) +\
               "Nombre de sospitosos: {} \n".format(self.n_sospitosos) +\
               "Culpable: {} \n".format(self.culpable)

    def emmascara(self, distribucio_nivell_emmascaracio):
        """ Crea indicadors per a una pista

        El nivell d'emmascaració ens dóna les probabilitats
        que l'emmascaració de l'indicador de cada sospitós
        sigui correcte.

        @param `nivell_emmascaracio`: diccionari amb tres claus,
        `veritat`, `mentida` amb valors que sumin <= 1.
        @param `nivell_emmascaracio`:

        @return un array amb els indicadors de la pista emmascarats
        """

        indicadors_emmascarats = map(lambda sospitos: self.__emmascara_indicador(distribucio_nivell_emmascaracio,
                                                                               sospitos),
                                     range(self.n_sospitosos))

        return(list(indicadors_emmascarats))

    def __emmascara_indicador(self, distribucio_nivell_emmascaracio, sospitos):
        """ Emmascara l'indicador d'un sospitós
        """

        keys = list(distribucio_nivell_emmascaracio.keys())
        keys.append("inconcloent")
        values = list(distribucio_nivell_emmascaracio.values())
        values.append(1 - sum(distribucio_nivell_emmascaracio.values()))

        nivell_emmascaracio = random.choices(population = keys, weights = values)[0]

        print("sospitós número {}".format(sospitos))
        print(nivell_emmascaracio)
        if nivell_emmascaracio == 'veritat':
            return self.indicadors[sospitos]
        elif nivell_emmascaracio == 'mentida':
            return not(self.indicadors[sospitos])
        else:
            return None

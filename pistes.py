# Dependencies
import random
import numpy as np
import uuid

class Pista():
    """Tipus pista

    """

    def __init__(self, nom, utilitat, culpabilitat, utilitats):
        self.id = uuid.uuid1()
        self.nom = nom
        self.utilitat = utilitat
        self.n_sospitosos = len(culpabilitat)
        self.culpabilitat = culpabilitat
        self.indicadors = self.__genera_indicadors(utilitats)

    def __genera_indicadors(self, utilitats):
        """ Crea un array de si una pista apunta o no a cada sospitós.
        """
        indicadors = {}
        for culpable in self.culpabilitat:
            if not self.culpabilitat[culpable]:
                # els sospitosos no culpables tenen probabilitat de ser apuntats per aquesta pista
                prob = random.uniform(0, 1)
                indicadors.update({culpable : prob < utilitats[self.utilitat]})
            else:
                # el culpable
                indicadors.update({culpable : True})

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
               "Culpabilitat: {} \n".format(self.culpabilitat) +\
               "Indicadors: {} \n".format(self.indicadors) +\
               "Nombre de sospitosos: {} \n".format(self.n_sospitosos)

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

        # preparació de la distribució ... això hauria de ser fora
        keys = list(distribucio_nivell_emmascaracio.keys())
        keys.append("inconcloent")
        values = list(distribucio_nivell_emmascaracio.values())
        values.append(1 - sum(distribucio_nivell_emmascaracio.values()))

        indicadors_emmascarats = {}
        for indicador in self.indicadors:
            nivell_emmascaracio = random.choices(population = keys, weights = values)[0]
            if nivell_emmascaracio == 'veritat':
                indicadors_emmascarats.update({indicador: self.indicadors[indicador]})
            elif nivell_emmascaracio == 'mentida':
                indicadors_emmascarats.update({indicador: not self.indicadors[indicador]})
            else:
                indicadors_emmascarats.update({indicador: None})

        return(indicadors_emmascarats)

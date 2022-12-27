# Dependencies
import uuid

class LlistaSospitosos:
    """ Llista de sospitosos amb un culpable

    """

    def __init__(self, noms, nom_culpable):
        self.id = uuid.uuid1()
        self.sospitosos = self.__genera_sospitosos(noms, nom_culpable)

    def __genera_sospitosos(self, noms, nom_culpable):
        """ Crea un array de si una pista apunta o no a cada sospitós.
        """
        sospitosos = {}
        for nom in noms:
            if nom == nom_culpable:
                indicador = True
            else:
                indicador = False
            print(nom)
            print(indicador)
            sospitosos.update({nom: indicador})

        return(sospitosos)

    def __str__(self):
        """Mostra els detalls de la pista
        Fent ús del mètode màgic __str__ fem que print() funcioni per a imprimir objectes de tipus pista.

         https://www.pythontutorial.net/python-oop/python-__str__/
         https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html
        """
        return "Id: {} \n".format(self.id) +\
               "Culpabilitat: {} \n".format(self.sospitosos)

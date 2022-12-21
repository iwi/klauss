import uuid
import random

class Investigador():
    """Tipus investigador

    """

    def __init__(self, nom, habilitats):
        """ Definició de l'investigador
        """
        self.id = uuid.uuid1()
        self.nom = nom
        self.habilitats = habilitats
        self.pistes_trobades = []
        self.pistes_investigades = []
        self.investigacions = []

    def investiga_pista(self, pista_trobada, distribucio_nivell_emmascaracio):
        """ .
        """

        if pista_trobada.id not in self.pistes_investigades:
            print("aquesta pista no la tens.")
        else:

            resultat_investigacio_pista = pista_trobada.emmascara(distribucio_nivell_emmascaracio)
            self.investigacions.append({"nom_pista" : pista_trobada.id,
                                        "resultats" : resultat_investigacio_pista})

    def cerca_pista(self, lloc):
        """ Cerquem una pista dins un lloc i l'afegim a les pistes trobades
        """

        index_pista = random.randint(0, len(lloc.pistes))
        pista = lloc.pistes[index_pista]
        if pista not in self.pistes_trobades:
            self.pistes_trobades.append(pista)
        else:
            print("has trobat una pista que ja tenies, segueix buscant-ne")



class Lloc():
    """ Tipus lloc

    Cada lloc tindrà un número de pistes
    """

    def __init__(self, nom):
        """ Definició de l'investigador
        """
        self.id = uuid.uuid1()
        self.nom = nom
        self.pistes = []

    def afegeix_pista(self, pista):
        """ .
        """

        if pista.id not in self.pistes:
            print("afegint pista nova a {}...".format(self.nom))
            self.pistes.append(pista.id)
            print("fet.")
        else:
            print("Aquesta pista ja hi era.")


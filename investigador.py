import uuid
import random
from math import sqrt

class Investigador():
    """Tipus investigador
    """

    def __init__(self, nom, posicio_inicial, habilitats):
        """ Definició de l'investigador
        """
        self.id = uuid.uuid1()
        self.nom = nom
        self.posicio = posicio_inicial
        self.habilitats = habilitats
        self.pistes_trobades = []
        self.pistes_investigades = []
        self.investigacions = []
        self.llocs_investigats = []
        self.temps = 0

    def investiga_pista(self, pista, distribucio_nivell_emmascaracio):
        """ .
        """

        # gasta temps
        self.temps += 2

        if pista not in self.pistes_trobades:
            print("aquesta pista no la tens.")
        else:
            resultat_investigacio_pista = pista.emmascara(distribucio_nivell_emmascaracio)
            self.investigacions.append({"id_pista" : pista.id,
                                        "resultats" : resultat_investigacio_pista})

    def cerca_pista(self, lloc):
        """ Cerquem una pista dins un lloc i l'afegim a les pistes trobades
        """

        # gasta temps
        self.temps += 1

        # mètode de trobar una pista dins el lloc aleatori - pot millorar-se
        index_pista = random.randint(0, len(lloc.pistes) - 1)
        pista = lloc.pistes[index_pista]
        if pista not in self.pistes_trobades:
            self.pistes_trobades.append(pista)
        else:
            print("has trobat una pista que ja tenies, segueix buscant-ne")

    def mou(self, nova_posicio):

        # gasta temps
        self.temps += sqrt((self.posicio[0] - nova_posicio[0])**2 + (self.posicio[1] - nova_posicio[1])**2)

        # canvia de posició
        self.posicio[0] = nova_posicio[0]
        self.posicio[1] = nova_posicio[1]
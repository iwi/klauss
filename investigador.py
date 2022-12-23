import uuid
import random

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

    def investiga_pista(self, pista, distribucio_nivell_emmascaracio):
        """ .
        """

        if pista not in self.pistes_trobades:
            print("aquesta pista no la tens.")
        else:
            resultat_investigacio_pista = pista.emmascara(distribucio_nivell_emmascaracio)
            self.investigacions.append({"id_pista" : pista.id,
                                        "resultats" : resultat_investigacio_pista})

    def cerca_pista(self, lloc):
        """ Cerquem una pista dins un lloc i l'afegim a les pistes trobades
        """

        # mètode de trobar una pista dins el lloc aleatori - pot millorar-se
        index_pista = random.randint(0, len(lloc.pistes) - 1)
        pista = lloc.pistes[index_pista]
        if pista not in self.pistes_trobades:
            self.pistes_trobades.append(pista)
        else:
            print("has trobat una pista que ja tenies, segueix buscant-ne")

    def mou(self, moviment):
        self.posicio[0] += moviment[0]
        self.posicio[1] += moviment[1]

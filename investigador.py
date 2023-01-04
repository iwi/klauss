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
        self.llocs_visitats = []
        self.temps = 0

    def mostra_investigador(self):
        """Mostra els detalls de l'investigador

        """
        print("Id: {}".format(self.id))
        print("Nom: {}".format(self.nom))
        print("Posició: {}".format(self.posicio))
        print("Habilitats: {}".format(self.habilitats))
        print("Temps gastat: {}".format(self.temps))
        [print("Pistes trobades: {}".format(x.nom)) for x in self.pistes_trobades]
        [print("Pistes investigades: {}".format(x.nom)) for x in self.pistes_investigades]
        [print("Llocs visitats: {}".format(x.nom)) for x in self.llocs_visitats]
        [print("Investigacions: {}".format(x)) for x in self.investigacions]

    def __str__(self):
        """Mostra els detalls de l'investigador
        Fent ús del mètode màgic __str__ fem que print() funcioni per a imprimir objectes de tipus investigador.

         https://www.pythontutorial.net/python-oop/python-__str__/
         https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html
        """
        part1 = "Id: {}".format(self.id) + "\n" +\
                "Nom: {}".format(self.nom) + "\n" +\
                "Posició: {}".format(self.posicio) + "\n" +\
                "Habilitats: {}".format(self.habilitats) + "\n" +\
                "Temps gastat: {}".format(self.temps)
        part2 = '\n'.join(["Pistes trobades: {}".format(x.nom) for x in list(set(self.pistes_trobades))])
        part3 = '\n'.join(["Pistes investigades: {}".format(x.nom) for x in list(set(self.pistes_investigades))])
        part4 = '\n'.join(["Llocs visitats: {}".format(x.nom) for x in list(set(self.llocs_visitats))])
        part5 = '\n'.join(["Investigacions: {}".format(x) for x in self.investigacions])

        return part1 + "\n" +\
               part2 + "\n" +\
               part3 + "\n" +\
               part4 + "\n" +\
               part5

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
            self.pistes_investigades.append(pista)

    def cerca_pista(self, lloc):
        """ Cerquem una pista dins un lloc i l'afegim a les pistes trobades
        """

        # gasta temps
        self.temps += 0.1

        # mètode de trobar una pista dins el lloc aleatori - pot millorar-se
        index_pista = random.randint(0, len(lloc.pistes) - 1)
        pista = lloc.pistes[index_pista]
        if pista not in self.pistes_trobades:
            self.pistes_trobades.append(pista)
            self.llocs_visitats.append(lloc)
        else:
            print("has trobat una pista que ja tenies, segueix buscant-ne")

    def mou(self, nova_posicio):

        # gasta temps
        self.temps += sqrt((self.posicio[0] - nova_posicio[0])**2 + (self.posicio[1] - nova_posicio[1])**2)

        # canvia de posició
        self.posicio[0] = nova_posicio[0]
        self.posicio[1] = nova_posicio[1]

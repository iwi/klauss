import uuid
import pistes

class Lloc():
    """ Tipus lloc

    Cada lloc tindrà un número de pistes
    """

    def __init__(self, nom, tipus, coordenades):
        """ Definició del lloc
        """
        self.id = uuid.uuid1()
        self.nom = nom
        self.tipus = tipus
        self.coordenades = coordenades
        self.pistes = []

    def __str__(self):
        """Mostra'n els detalls
        Fent ús del mètode màgic __str__ fem que print() funcioni per a imprimir objectes de tipus pista.

         https://www.pythontutorial.net/python-oop/python-__str__/
         https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html
        """
        return "Id: {} \n".format(self.id) +\
               "Nom: {} \n".format(self.nom) +\
               "Tipus: {} \n".format(self.tipus) +\
               "Coordenades: {} \n".format(self.coordenades) +\
               "Pistes: {} \n".format(self.pistes)

    def afegeix_pista(self,
                      nom_pista,
                      utilitat_pista,
                      n_sospitosos_pista,
                      culpable_pista,
                      utilitats_pista):
        """ Afegeix una pista al lloc.
        """

        nova_pista = pistes.Pista(
            nom = nom_pista,
            utilitat = utilitat_pista,
            n_sospitosos = n_sospitosos_pista,
            culpable = culpable_pista,
            utilitats = utilitats_pista)

        print("afegint pista nova a {}...".format(self.nom))
        self.pistes.append(nova_pista)
        print("fet.")

import uuid

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


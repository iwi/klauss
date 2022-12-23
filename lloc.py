import uuid
import pistes

class Lloc():
    """ Tipus lloc

    Cada lloc tindrà un número de pistes
    """

    def __init__(self, nom, tipus):
        """ Definició del lloc
        """
        self.id = uuid.uuid1()
        self.nom = nom
        self.tipus = tipus
        self.pistes = []

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
            lloc = self.id,
            culpable = culpable_pista,
            utilitats = utilitats_pista)

        print("afegint pista nova a {}...".format(self.nom))
        self.pistes.append(nova_pista)
        print("fet.")

# Dependencies
import random
import numpy as np

class Pista():
    """Tipus pista

    """

    def __init__(self, nom, utilitat, n_sospitosos, lloc, culpable, utilitats):
        self.nom = nom
        self.utilitat = utilitat
        self.lloc = lloc
        self.n_sospitosos = n_sospitosos
        self.investigada = False
        self.culpable = culpable
        self.indicadors = self.genera_indicadors(utilitats)

    def genera_indicadors(self, utilitats):
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

    def mostrar_pista(self):
        """Mostra els detalls de la pista

        """
        print("Nom: {}".format(self.nom))
        print("Utilitat: {}".format(self.utilitat))
        print("Lloc: {}".format(self.lloc))
        print("Indicadors: {}".format(self.indicadors))
        print("Investigada?  {}".format(self.investigada))
        print("Nombre de sospitosos: {}".format(self.n_sospitosos))
        print("Culpable: {}".format(self.culpable))

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

        indicadors_emmascarats = map(lambda sospitos: self.emmascara_indicador(distribucio_nivell_emmascaracio,
                                                                               sospitos),
                                     range(self.n_sospitosos))

        return(list(indicadors_emmascarats))

    def emmascara_indicador(self, distribucio_nivell_emmascaracio, sospitos):
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

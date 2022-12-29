# Klauss

# Dependències
from importlib import reload
#import sys


# Mòduls
import pistes
import investigador as inv
import lloc
import llista_sospitosos as sos

# reload imports
pistes = reload(pistes)
inv = reload(inv)
lloc = reload(lloc)
sos = reload(sos)

# Determinar el nombre de sospitosos
n_sospitosos = 5

# Determinar la probabilitat de cada tipus de pista d'apuntar a sospitosos no-culpables.
utilitats = {'determinant': 0,
             'util': 0.2,
             'soroll': 0.4}

# Determinar el nivell d'emmascarament de les pistes (emmascaració o emmascarat?)
# Considerar fer-lo variable? e.g. podem fer que els valors segueixin una distribució.
# !!passar-ho a enters per a no perdre precisió
distribucio_nivell_emmascaracio = {'veritat': 0.7,
                                   'mentida': 0.2}
                                   #,'inconcloent': 1 - veritat - mentida}




# Creem una llista de sospitosos i decidim qui és el culpable
sospitosos = ["pinguí", "mona", "foca", "esquirol", "guineu"]
culpable = "foca"

llista_sospitosos = sos.LlistaSospitosos(sospitosos, culpable)

print(llista_sospitosos)

# Creem un lloc
nom_lloc = "menjador"
tipus_lloc = "habitacio casa"
posicio = [2, 2]
ll1 = lloc.Lloc(nom_lloc, tipus_lloc, posicio)

print(ll1)


# Afegir-hi algunes pistes
ll1.afegeix_pista(nom_pista = "empremptes",
                  utilitat_pista = "util",
                  n_sospitosos_pista = n_sospitosos,
                  culpable_pista = culpable,
                  utilitats_pista = utilitats)

ll1.afegeix_pista(nom_pista = "dna",
                  utilitat_pista = "determinant",
                  n_sospitosos_pista = n_sospitosos,
                  culpable_pista = culpable,
                  utilitats_pista = utilitats)

ll1.afegeix_pista(nom_pista = "cabell",
                  utilitat_pista = "soroll",
                  n_sospitosos_pista = n_sospitosos,
                  culpable_pista = culpable,
                  utilitats_pista = utilitats)
